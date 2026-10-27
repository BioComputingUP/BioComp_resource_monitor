from datetime import datetime, timedelta, timezone

import pytest

from common import iso, load_resources
from notify import GitHub, load_notify_config, marker, parse_marker, plan_actions

NOW = datetime(2026, 9, 25, 12, 0, tzinfo=timezone.utc)
CFG = {"people": ["ivanmicetic"], "min_consecutive_down": 2}
RESOURCES = [
    {"id": "alpha", "name": "Alpha", "url": "https://alpha.example.org"},
    {"id": "beta", "name": "Beta", "url": "https://beta.example.org"},
]


def st(state, consecutive=0, since="2026-09-25T11:20:00Z", reason=None):
    return {"state": state, "since": since, "consecutive_down": consecutive,
            "reason": reason or ("ok" if state != "down" else "http_502"), "code": 502 if state == "down" else 200,
            "error": None, "url": "https://x.example.org"}


def test_one_failed_run_is_not_enough_two_are():
    assert plan_actions(RESOURCES, {"alpha": st("down", 1)}, [], CFG, NOW) == []
    [a] = plan_actions(RESOURCES, {"alpha": st("down", 2)}, [], CFG, NOW)
    assert a["action"] == "open" and a["title"] == "🔴 Alpha is down"
    assert a["assignees"] == ["ivanmicetic"]
    assert "cc @ivanmicetic" in a["body"] and "`http_502`" in a["body"]
    assert parse_marker(a["body"]) == ("alpha", "2026-09-25T11:20:00Z")


def test_still_down_with_an_open_issue_does_nothing():
    issues = [{"number": 7, "id": "alpha", "since": "2026-09-25T11:20:00Z"}]
    assert plan_actions(RESOURCES, {"alpha": st("down", 9)}, issues, CFG, NOW) == []


def test_back_up_closes_with_the_outage_duration():
    issues = [{"number": 7, "id": "alpha", "since": "2026-09-25T10:00:00Z"}]
    [a] = plan_actions(RESOURCES, {"alpha": st("up", since="2026-09-25T11:40:00Z")}, issues, CFG, NOW)
    assert a["action"] == "close" and a["number"] == 7
    assert "Alpha is back up" in a["comment"] and "1 h 40 min" in a["comment"]
    assert "2026-09-25T11:40:00Z" in a["comment"]


def test_challenged_counts_as_up_and_unknown_is_skipped():
    issues = [{"number": 3, "id": "beta", "since": None}]
    [a] = plan_actions(RESOURCES, {"beta": st("challenged")}, issues, CFG, NOW)
    assert a["action"] == "close" and "after about" not in a["comment"]
    assert plan_actions(RESOURCES, {"alpha": {"state": "unknown"}}, [], CFG, NOW) == []
    assert plan_actions(RESOURCES, {}, [], CFG, NOW) == []


def test_simulated_outage_opens_a_test_issue_then_closes_cleanly():
    state = {"alpha": st("up", since="2026-09-20T00:00:00Z")}
    [a] = plan_actions(RESOURCES, state, [], CFG, NOW, simulate="alpha")
    assert a["title"] == "[test] 🔴 Alpha is down" and "Test only" in a["body"]
    assert state["alpha"]["state"] == "up"                       # recorded data untouched

    # The next normal run sees it up. It has been up since before the simulated outage, so the
    # duration runs to now rather than going negative.
    issues = [{"number": 9, "id": "alpha", "since": iso(NOW)}]
    [c] = plan_actions(RESOURCES, state, issues, CFG, NOW + timedelta(minutes=20))
    assert c["action"] == "close" and "about 20 min" in c["comment"]


def test_reconciling_twice_is_idempotent():
    state = {"alpha": st("down", 3), "beta": st("up")}
    [a] = plan_actions(RESOURCES, state, [], CFG, NOW)
    issues = [{"number": 1, "id": a["id"], "since": parse_marker(a["body"])[1]}]
    assert plan_actions(RESOURCES, state, issues, CFG, NOW) == []


def test_marker_round_trip():
    assert parse_marker("text\n" + marker("dome-ml", "2026-09-25T11:20:00Z")) == ("dome-ml", "2026-09-25T11:20:00Z")
    assert parse_marker(marker("dome-ml", None)) == ("dome-ml", None)
    assert parse_marker("no marker here") is None


def test_config_block_is_read_with_defaults(tmp_path):
    cfg_file = tmp_path / "resources.yml"
    cfg_file.write_text("notify:\n  people: [someone]\nresources: []\n")
    cfg = load_notify_config(cfg_file)
    assert cfg["people"] == ["someone"] and cfg["min_consecutive_down"] == 2


def test_a_resource_can_add_its_own_people_for_its_website_and_api(tmp_path):
    cfg_file = tmp_path / "resources.yml"
    cfg_file.write_text("resources:\n- id: nto\n  name: NTO\n  url: https://nto.example.org\n"
                        "  notify: [gavinf97, ivanmicetic]\n  api: https://nto.example.org/api\n")
    targets = load_resources(cfg_file)
    state = {t["id"]: st("down", 2) for t in targets}
    opened = plan_actions(targets, state, [], CFG, NOW)
    assert [a["id"] for a in opened] == ["nto", "nto--api"]
    for a in opened:
        assert a["assignees"] == ["ivanmicetic", "gavinf97"]
        assert "cc @ivanmicetic @gavinf97" in a["body"]
    # other resources get only the global people
    [a] = plan_actions(RESOURCES, {"alpha": st("down", 2)}, [], CFG, NOW)
    assert a["assignees"] == ["ivanmicetic"]


class FakeResponse:
    def __init__(self, status, payload=None, text=""):
        self.status_code, self._payload, self.text = status, payload, text

    def json(self):
        return self._payload


def test_open_issue_retries_without_assignees_when_assignment_is_rejected(monkeypatch):
    calls = []

    def request(method, url, timeout, **kw):
        calls.append(kw["json"]["assignees"])
        return FakeResponse(422, text="Validation Failed") if kw["json"]["assignees"] else FakeResponse(201, {"number": 5})

    gh = GitHub("org/repo", "t")
    monkeypatch.setattr(gh.s, "request", request)
    assert gh.open_issue("t", "b", ["gavinf97"]) == 5
    assert calls == [["gavinf97"], []]


def test_existing_label_is_not_an_error_but_other_failures_are(monkeypatch):
    gh = GitHub("org/repo", "t")
    monkeypatch.setattr(gh.s, "request", lambda *a, **k: FakeResponse(422, text="already_exists"))
    gh.ensure_label()
    monkeypatch.setattr(gh.s, "request", lambda *a, **k: FakeResponse(500, text="boom"))
    with pytest.raises(RuntimeError):
        gh.close_issue(1, "c")


def test_open_issues_ignores_prs_and_unmarked_issues(monkeypatch):
    payload = [{"number": 1, "body": marker("alpha", "2026-09-25T11:00:00Z")},
               {"number": 2, "body": "hand-written outage report"},
               {"number": 3, "body": marker("beta", ""), "pull_request": {}}]
    gh = GitHub("org/repo", None)
    monkeypatch.setattr(gh.s, "request", lambda *a, **k: FakeResponse(200, payload))
    assert gh.open_issues() == [{"number": 1, "id": "alpha", "since": "2026-09-25T11:00:00Z"}]
