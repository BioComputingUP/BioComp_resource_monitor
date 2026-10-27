# monitor/

The code behind the BioComp resource monitor. It is adapted from
[BioComputingUP/dome-tracking](https://github.com/BioComputingUP/dome-tracking) (itself adapted
from the [ECD uptime tracker](https://github.com/gavinf97/ECD/tree/main/uptime)), and adds
API checks: an API counts as up only when it returns the expected JSON.

## 1. Where the results are deposited

On the **`monitor-data` branch**, never on `main`. The branch is also the GitHub Pages source,
so every push to it republishes the dashboard.

```
branch monitor-data
├── index.html               the dashboard (copied from monitor/dashboard/ by the workflow)
├── STATUS.md                the status page: monitoring health, repo activity, uptime, recent events
├── summary.json             everything on the dashboard, machine-readable
├── history.json             per-target daily uptime, last 90 days
├── state.json               current state per target, plus timestamps of recent runs (48 h)
├── events.jsonl             append-only: every state change
├── activity.json            latest push / head commit per repository
├── activity_history.jsonl   append-only: one line each time a repo's last push or head commit changes
├── badges/*.json            shields.io endpoints behind the README badges
└── daily/YYYY/YYYY-MM-DD.json   per target: checks, up, challenged, down, latency histogram
```

A *target* is a website or an API. An API's id is the resource id plus `--api`, for example
`mobidb--api`. Commits are squashed to one per UTC day and force-pushed. Never edit the branch
by hand.

## 2. How it works

The [`monitor-check`](../.github/workflows/monitor-check.yml) workflow runs these steps in order:

1. [`scripts/check.py`](scripts/check.py) sends a `GET` to every website and API in
   [`resources.yml`](resources.yml). It follows redirects and uses a 10 s connect and 20 s read
   timeout. It reads the first 64 KB of a website and up to 5 MB of an API. Failures are
   checked again 30 s later.
2. [`scripts/activity.py`](scripts/activity.py) makes two GitHub API calls for each `repo:`.
   They return `pushed_at` (the last push to any branch) and the head commit of the default
   branch. If a call fails, the repo keeps its previous snapshot, marked with an `error`.
3. [`scripts/summarize.py`](scripts/summarize.py) rebuilds every report in §1.
4. The workflow copies the dashboard to the data branch and commits.
5. [`scripts/notify.py`](scripts/notify.py) opens or closes outage issues (see
   [Outage alerts](#outage-alerts)).

### Classification: websites

| State | When | Counts as available |
|---|---|---|
| `up` | 2xx/3xx, or a 4xx other than 404/410 (the server responds, but restricts access) | yes |
| `challenged` | A bot-challenge page (Cloudflare, Anubis, DDoS-Guard) | yes, counted separately |
| `down` | 5xx, timeout, DNS or connection error, redirect loop, or a TLS error a browser would also reject | no |
| `down` + `url_review` | 404/410: the URL needs fixing | no |

If TLS fails only because the certificate chain is incomplete, the site is checked again
without verification. If that works, it is recorded as `up` with a `tls_warning`.

### Classification: APIs

An API client needs a 2xx JSON answer with the right content, so the rules are stricter:

| State | Reason | When |
|---|---|---|
| `up` | `ok` | 2xx, the body is JSON, and it matches `api.expect` |
| `down` | `bad_payload:not_json` | 2xx, but the body is not JSON. Usually the web app's `index.html`, served for every path when the API behind it is gone |
| `down` | `bad_payload:missing:<field>` / `bad_payload:<field>=<value>` / `bad_payload:too_few_items:<n>` | JSON, but not the expected content |
| `down` | `bad_payload:too_large` | The body is over 5 MB. Choose a smaller endpoint |
| `down` | `http_4xx`, `http_5xx`, `challenge:*`, timeouts, DNS, connection errors | Same as for websites, except that any 4xx or bot challenge counts as down |

The dashboard shows `bad_payload:*` as **wrong data** (orange), separate from plain **down**
(red). That way "answering, but broken" is not mistaken for "unreachable".

`api.expect` in `resources.yml`:

```yaml
  api:
    url: https://disprot.org/api/DP00003
    expect: {field: acc, equals: P03265}   # the value at a dotted path, compared as text
    # expect: {field: count, min: 1}       # a number (or a list's length) at least this
    # expect: {min_items: 1, field: 0.name}  # the body is a list of ≥ 1 items, item 0 has "name"
```

Pick a small endpoint for a stable record that will not change, such as one known entry. The
APIs checked now:

| Resource | Endpoint | Expects |
|---|---|---|
| DisProt | `disprot.org/api/DP00003` | `acc` = P03265 |
| MobiDB | `mobidb.org/api/download?acc=P04637&format=json` | `acc` = P04637 |
| RepeatsDB | `repeatsdb.org/api/production/annotations?skip=0&limit=1` | `count` ≥ 1 |
| PED | `deposition.proteinensemble.org/api/entries/PED00001` | `entry_id` = PED00001 |
| FuzDB | `fuzdb.org/api/entries?entry_id=FC00001` | first item's `entry_id` = FC00001 |
| APICURON | `apicuron.org/api/home` | `resource_count` ≥ 1 |
| CAID | `caid.idpcentral.org/dataset-repository/api/dataset/` | a non-empty list of datasets with `name` |

### Metrics

- **Uptime** = (up + challenged) ÷ recorded checks, over today, 7, 30, 90 and 365 days.
- **Coverage** = recorded checks ÷ expected checks (one per 20 minutes since the target was
  first seen), capped at 100%. Missed runs lower coverage and are never counted as up.
- **Runs in the last 24 h**: how many runs actually happened, against a target of 72. Green at
  75% of the target or more, amber at 33% or more, red below that.
- **STALE**: no run for 3 hours. This is the "monitoring has stopped" signal.
- **Repository activity**: active if pushed within 7 days, recent within 30 days, quiet otherwise.

### Check interval

The target interval is **20 minutes** (`INTERVAL_MINUTES` in [`scripts/common.py`](scripts/common.py)).
GitHub's own scheduler can't deliver that: it is best-effort and drops ticks. On
`dome-tracking`, four crons an hour delivered about 17 runs a day out of 72. So runs are
triggered in two ways:

- **Primary:** a free [cron-job.org](https://cron-job.org) job calls the `workflow_dispatch` API
  at :15, :35 and :55. Dispatch events run straight away and are not throttled. ECD has run
  this way since 2026-09-25 and gets all 72 runs a day.
- **Backup:** four GitHub crons an hour (:09, :24, :41, :58), best-effort.

Extra runs do no harm. Coverage is capped at 100%, the concurrency group stops runs from
overlapping, and at most 7 runs an hour stays under the GitHub Pages limit of 10 builds an
hour.

The external trigger is a cron-job.org job: `POST https://api.github.com/repos/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml/dispatches`
with body `{"ref":"main"}` and headers `Authorization: Bearer <token>`,
`Accept: application/vnd.github+json` and `X-GitHub-Api-Version: 2022-11-28`. The token is a
fine-grained token on BioComputingUP with Actions: Read and write only. A test run answers 204.
When the token expires, runs fall back to the GitHub crons and runs-in-24 h turns amber.

### Outage alerts

On every run, [`scripts/notify.py`](scripts/notify.py) compares each target's state with the
open issues labelled `outage`:

| Situation | Action |
|---|---|
| Down for `min_consecutive_down` runs in a row (2), with no open issue | Open **🔴 &lt;name&gt; is down** (for example **🔴 MobiDB API is down**), and @mention and assign `notify.people` plus the resource's own `notify:` list in [`resources.yml`](resources.yml) |
| Back up, with an open issue | Comment **🟢 back up** with the outage duration, and close the issue |
| Still down, with an issue already open | Nothing |

Issues are opened by **github-actions[bot]** through the workflow's built-in token. GitHub does
not notify you about actions taken with your own token, so this is what gets you emailed.

**Test the alerts:**
`gh workflow run monitor-check.yml -R BioComputingUP/BioComp_resource_monitor -f simulate_down=mobidb--api`
opens a **[test] 🔴 MobiDB API is down** issue, without changing recorded data. The next run
closes it.

## 3. Common tasks

**Add a resource or an API.** Edit [`resources.yml`](resources.yml). Each entry needs `id`,
`name`, `group` and `url`. `repo` and `api` are optional. First check that the API answers as
expected:
```bash
python monitor/scripts/check.py --dry-run --only mobidb--api
```
`enabled: false` pauses a resource and its API, and keeps their history.

**Email someone about outages.** Add their GitHub username to `notify.people` in
[`resources.yml`](resources.yml) for every resource, or to a resource's own `notify:` list for
that resource only (its website and API). They must be a BioComputingUP member to be assigned;
the @mention emails them either way.

**Read private repositories.** The built-in token reads only public repos. `mobidb-ui`,
`ring-ui` and `bup-ui` are private, so they show **no access** until a read-only fine-grained
token is saved as the `ACTIVITY_TOKEN` secret:
1. Owner **BioComputingUP**. Select those repos. Grant **Contents: Read-only**.
2. Run `gh secret set ACTIVITY_TOKEN -R BioComputingUP/BioComp_resource_monitor`.

⚠️ This repo and its dashboard are public. With the token set, the latest commit message,
author and date of those private repos are published here too.

**Run locally:**
```bash
pip install -r monitor/requirements.txt -r monitor/requirements-dev.txt
python monitor/scripts/check.py --dry-run
python -m pytest monitor/tests -q
```

**Preview the dashboard with real data:**
```bash
D=/tmp/biocomp-data; mkdir -p $D
python monitor/scripts/check.py --data $D && GITHUB_TOKEN=$(gh auth token) python monitor/scripts/activity.py --data $D \
  && python monitor/scripts/summarize.py --data $D
cp monitor/dashboard/index.html $D/ && python -m http.server -d $D 8000
```

## 4. Limitations

- **One vantage point.** Checks run from GitHub-hosted runners, mostly in US Azure regions.
- **One read-only API call per resource.** It shows that the backend is serving data. It does not
  test search, job submission or every endpoint.
- **20-minute sampling.** Outages shorter than about 20 minutes can be missed. An alert needs two
  failed runs in a row, so it arrives 20–40 minutes after a target goes down.
- **Legacy tools share one host** (`old.protein.bio.unipd.it`), so they tend to go down together.
- **The DOME section** of the dashboard is read live from `dome-tracking`'s data branch. It is as
  current as that tracker is, and its own runs-in-24 h figure shows that.
