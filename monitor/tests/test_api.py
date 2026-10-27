import json
from datetime import datetime, timezone

import pytest

from check import classify_api, match_expect, record
from common import load_resources
from summarize import build_badges, build_summary, render_status

DISPROT = json.dumps({"acc": "P03265", "disprot_id": "DP00003", "regions": [{"start": 1}]})
SPA_FALLBACK = "<!doctype html><html><head><title>PED</title></head><body><app-root></app-root></body></html>"


@pytest.mark.parametrize("doc,expect,problem", [
    ({"acc": "P03265"}, {"field": "acc", "equals": "P03265"}, None),
    ({"acc": "Q99999"}, {"field": "acc", "equals": "P03265"}, "acc=Q99999"),
    ({"other": 1}, {"field": "acc", "equals": "P03265"}, "missing:acc"),
    ({"count": 47427}, {"field": "count", "min": 1}, None),
    ({"count": 0}, {"field": "count", "min": 1}, "count=0"),
    ({"items": [1, 2, 3]}, {"field": "items", "min": 2}, None),       # min on a list -> its length
    ([{"entry_id": "FC00001"}], {"field": "0.entry_id", "equals": "FC00001"}, None),
    ([], {"field": "0.entry_id", "equals": "FC00001"}, "missing:0.entry_id"),
    ([{"name": "CAID3"}], {"min_items": 1, "field": "0.name"}, None),
    ([], {"min_items": 1}, "too_few_items:0"),
    ({"a": 1}, {"min_items": 1}, None),
    ("text", {"min_items": 1}, "not_a_list"),
    ({"x": {"y": True}}, {"field": "x.y"}, None),                     # field alone: must exist
    ({"x": True}, {"field": "x", "min": 1}, "x=True"),                # booleans are not numbers
    ({"anything": 1}, {}, None),
])
def test_match_expect(doc, expect, problem):
    assert match_expect(doc, expect) == problem


def test_api_ok():
    got = classify_api(200, {"Content-Type": "application/json"}, DISPROT,
                       expect={"field": "acc", "equals": "P03265"})
    assert got == {"state": "up", "reason": "ok", "url_review": False}


def test_api_wrong_payload_is_down_with_bad_payload_reason():
    got = classify_api(200, {}, DISPROT, expect={"field": "acc", "equals": "P04637"})
    assert got["state"] == "down" and got["reason"] == "bad_payload:acc=P03265"


def test_api_html_fallback_is_not_json():
    # A web app that serves its index.html for every path answers 200 even when the API is gone.
    assert classify_api(200, {}, SPA_FALLBACK)["reason"] == "bad_payload:not_json"


def test_api_truncated_body_is_reported():
    assert classify_api(200, {}, DISPROT[:20], truncated=True)["reason"] == "bad_payload:too_large"


@pytest.mark.parametrize("code,reason,url_review", [
    (500, "http_500", False), (502, "http_502", False), (404, "http_404", True),
    (403, "http_403", False), (429, "http_429", False),   # fine for a website, not for an API client
])
def test_api_http_errors_are_down(code, reason, url_review):
    got = classify_api(code, {}, "{}")
    assert got == {"state": "down", "reason": reason, "url_review": url_review}


def test_api_connection_errors_and_challenges_are_down(fixture_text):
    assert classify_api(None, error_kind="read_timeout") == \
        {"state": "down", "reason": "read_timeout", "url_review": False}
    got = classify_api(403, {"cf-mitigated": "challenge"}, fixture_text("cloudflare_challenge.html"))
    assert got["state"] == "down" and got["reason"] == "challenge:cloudflare"


CONFIG = """
resources:
- id: alpha
  name: Alpha DB
  group: Databases
  url: https://alpha.example.org
  repo: Org/alpha
  check: {verify_tls: false, url: https://alpha.example.org/home}
  api:
    url: https://alpha.example.org/api/1
    expect: {field: id, equals: "1"}
- id: beta
  name: Beta tool
  url: https://beta.example.org
- id: gamma
  name: Gamma
  url: https://gamma.example.org
  api: https://gamma.example.org/api
  enabled: false
"""


def test_api_blocks_become_their_own_targets(tmp_path):
    cfg = tmp_path / "resources.yml"
    cfg.write_text(CONFIG)
    targets = load_resources(cfg)
    assert [t["id"] for t in targets] == ["alpha", "alpha--api", "beta"]
    web, api = targets[0], targets[1]
    assert web["kind"] == "web" and api["kind"] == "api"
    assert api == {"id": "alpha--api", "name": "Alpha DB API", "url": "https://alpha.example.org/api/1",
                   "kind": "api", "parent": "alpha", "group": "Databases",
                   "expect": {"field": "id", "equals": "1"}, "check": {"verify_tls": False}, "notify": None,
                   "enabled": True}
    assert "repo" not in api  # code activity is tracked once, on the website target
    # A disabled resource disables its API too; the shorthand `api: <url>` is accepted.
    everything = load_resources(cfg, enabled_only=False)
    assert [t["id"] for t in everything] == ["alpha", "alpha--api", "beta", "gamma", "gamma--api"]
    assert everything[-1]["url"] == "https://gamma.example.org/api" and everything[-1]["expect"] == {}


def test_summary_splits_websites_and_apis(tmp_path):
    cfg = tmp_path / "resources.yml"
    cfg.write_text(CONFIG)
    targets = load_resources(cfg)
    now = datetime(2026, 10, 26, 12, 0, tzinfo=timezone.utc)
    base = {"checked_at": "2026-10-26T12:00:00Z", "url_review": False, "code": 200, "latency_ms": 300}
    record(tmp_path, {
        "alpha": {**base, "id": "alpha", "url": "https://alpha.example.org/home", "state": "up", "reason": "ok"},
        "alpha--api": {**base, "id": "alpha--api", "url": "https://alpha.example.org/api/1", "state": "down",
                       "reason": "bad_payload:not_json"},
        "beta": {**base, "id": "beta", "url": "https://beta.example.org", "state": "up", "reason": "ok"},
    }, now)
    summary = build_summary(targets, tmp_path, now)
    assert summary["resource_count"] == 2 and summary["api_count"] == 1
    assert summary["totals"]["up"] == 2 and summary["totals"]["down"] == 0
    assert summary["totals_api"] == {"up": 0, "down": 1, "unknown": 0, "bad_payload": 1, "apis": 1}
    api_row = next(r for r in summary["resources"] if r["id"] == "alpha--api")
    assert api_row["kind"] == "api" and api_row["parent"] == "alpha" and api_row["group"] == "Databases"

    badges = build_badges(summary)
    assert badges["api"]["message"] == "0/1" and badges["api"]["color"] == "red"
    assert badges["down"]["message"] == "1"      # counts websites and APIs
    md = render_status(summary, [])
    assert "2 websites and 1 APIs" in md and "wrong payload **1**" in md
    assert "Alpha DB API" in md
