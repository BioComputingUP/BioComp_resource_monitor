# BioComp resource monitor status

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/monitoring.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml) [![up](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/up.json)](#all-resources) [![api](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/api.json)](#all-resources) [![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/down.json)](#needs-attention) [![runs 24h](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/runs-24h.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml) [![activity](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/activity.json)](#repository-activity)

## 🟢 Monitoring is ACTIVE

| | |
|---|---|
| **Monitored** | 32 websites and 9 APIs — every one, every 20 minutes, continuously |
| **Last check** | 2026-11-28T20:55:22Z (0 min ago) |
| **Runs in the last 24 h** | 84 of a target 72 |
| **Checks recorded** | 2290 runs since monitoring began |
| **Runs on** | [GitHub Actions → monitor-check](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml) |
| **Visual dashboard** | https://biocomputingup.github.io/BioComp_resource_monitor/ |

### Right now

🟢 up **32** · 🟡 challenged **0** · 🔴 down **0** · ⚪ never checked **0** · 🔗 check URL to review **0**

**APIs:** 🟢 OK **9** of 9 · 🔴 down **0** (of which 🟠 responding with the wrong payload **0**)

An API counts as up only when it answers 2xx with JSON that matches its `api.expect` in resources.yml; a `bad_payload:*` reason means it answered, but with the wrong content. Uptime = (up + challenged) ÷ recorded checks. Coverage = recorded ÷ expected checks. 99.00% is a reference line only; it sorts the list below. Full definitions: [monitor/README.md](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/main/monitor/README.md).

---

## Repository activity

`Last push` is the latest push to **any** branch; `Head commit` is the tip of the default branch. The full timeline is in [activity_history.jsonl](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/monitor-data/activity_history.jsonl).

| Resource | Repository | Last push | Activity | Head commit |
|---|---|---|---|---|
| MobiDB | [BioComputingUP/mobidb-ui](https://github.com/BioComputingUP/mobidb-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| PED | [BioComputingUP/ped5-ui](https://github.com/BioComputingUP/ped5-ui) `main` | 2026-09-07T12:26:09Z (82 days ago) | 🔴 quiet (≥30 d) | [`40b2996`](https://github.com/BioComputingUP/ped5-ui/commit/40b2996038ee81412725d4737d6e4d3f67f287a3) Test local configuration — Ivan Mičetić, 2026-09-07 |
| APICURON | [BioComputingUP/apicuron](https://github.com/BioComputingUP/apicuron) `master` | 2026-11-20T08:47:02Z (8 days ago) | 🟡 recent (<30 d) | [`4b3dae3`](https://github.com/BioComputingUP/apicuron/commit/4b3dae3057896f16929d6a9e405705b47d73b54d) feat(ui): tracked output cards filter and scroll to partner resources, NTO Registry under Learn more — Mehdi-SK, 2026-11-20 |
| RING | [BioComputingUP/ring-ui](https://github.com/BioComputingUP/ring-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| BioComputing UP website | [BioComputingUP/bup-ui](https://github.com/BioComputingUP/bup-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| NTO Registry | [BioComputingUP/nto-registry](https://github.com/BioComputingUP/nto-registry) `main` | 2026-10-22T15:37:29Z (37 days ago) | 🔴 quiet (≥30 d) | [`9057881`](https://github.com/BioComputingUP/nto-registry/commit/90578813a42b509c956b8ddfe0a72f05351166fd) Security: update site dependencies to clear npm audit advisories — Gavin Farrell, 2026-10-22 |
| DOME-ML website | [BioComputingUP/dome-ml-ui](https://github.com/BioComputingUP/dome-ml-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| DOME Registry | [BioComputingUP/dome-registry](https://github.com/BioComputingUP/dome-registry) `main` | 2026-07-29T13:14:04Z (122 days ago) | 🔴 quiet (≥30 d) | [`4978003`](https://github.com/BioComputingUP/dome-registry/commit/4978003db56b9a36bc078689ceb4bf51679be708) Add dome 2.0 schema + Logo modification — abdelghaniomar, 2026-07-29 |
| DOME Copilot | [IFCA-Advanced-Computing/dome-copilot](https://github.com/IFCA-Advanced-Computing/dome-copilot) `master` | 2026-03-30T11:32:42Z (243 days ago) | 🔴 quiet (≥30 d) ⚠️ API error, showing last known | [`e157c7b`](https://github.com/IFCA-Advanced-Computing/dome-copilot/commit/e157c7b56b2ef326dd9b3523b270591ba65a3542) feat: make the model names configurable — Ignacio Heredia, 2026-03-30 |
| OSAI | [BioComputingUP/dome-ml-osai-ui](https://github.com/BioComputingUP/dome-ml-osai-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| DOME Observatory | [BioComputingUP/dome-ml-observatory](https://github.com/BioComputingUP/dome-ml-observatory) `main` | 2026-11-25T18:30:47Z (3 days ago) | 🟢 active (<7 d) | [`fba9d17`](https://github.com/BioComputingUP/dome-ml-observatory/commit/fba9d174a64a7ae43382ff58fec38229a5bedf41) Close out v1.9.2: the data-links refresh is loaded; refresh facet stats from the live API — gavinfarrell, 2026-11-25 |

---

## Needs attention

### 🔴 Currently down

None — every monitored website and API is up.

### 🔗 Check URL needs review

None.

### 📉 Below 99.00% over the last 30 days

**3** resources, worst first.

| Resource | 30d uptime | 30d coverage | Down checks |
|---|---|---|---|
| [DOME Copilot](https://copilot.dome-ml.org/) | 95.14% | 100.00% | 109 |
| [RepeatsDB](https://repeatsdb.org/) | 98.66% | 100.00% | 30 |
| [RepeatsDB API](https://repeatsdb.org/api/production/annotations?skip=0&limit=1) | 98.66% | 100.00% | 30 |

---

## All resources

All 32 websites and 9 APIs, sorted by name. Sortable and searchable on the [dashboard](https://biocomputingup.github.io/BioComp_resource_monitor/).

| Resource | State | Today | 7d | 30d | 90d | 365d | Coverage 30d | p95 30d |
|---|---|---|---|---|---|---|---|---|
| [Align2](http://old.protein.bio.unipd.it/align2/) | 🟢 up | 100.00% | 99.83% | 99.96% | 99.96% | 99.96% | 100.00% | ≤5000 ms |
| [APICURON](https://apicuron.org/) | 🟢 up | 100.00% | 99.48% | 99.73% | 99.74% | 99.74% | 100.00% | ≤2000 ms |
| [APICURON API](https://apicuron.org/api/home) | 🟢 up | 100.00% | 99.30% | 99.69% | 99.69% | 99.69% | 100.00% | ≤2000 ms |
| [BioComputing UP website](https://biocomputingup.it/) | 🟢 up | 100.00% | 100.00% | 99.42% | 99.43% | 99.43% | 100.00% | ≤5000 ms |
| [BLUUES](https://bluues.biocomputingup.it/) | 🟢 up | 100.00% | 99.48% | 99.78% | 99.78% | 99.78% | 100.00% | ≤2000 ms |
| [BLUUES](http://old.protein.bio.unipd.it/bluues/) | 🟢 up | 100.00% | 99.83% | 99.96% | 99.96% | 99.96% | 100.00% | ≤5000 ms |
| [CAID](https://caid.idpcentral.org/) | 🟢 up | 100.00% | 99.83% | 99.82% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [CAID API](https://caid.idpcentral.org/dataset-repository/api/dataset/) | 🟢 up | 100.00% | 99.48% | 99.73% | 99.74% | 99.74% | 100.00% | ≤2000 ms |
| [DisProt](https://disprot.org/) | 🟢 up | 100.00% | 99.65% | 99.78% | 99.78% | 99.78% | 100.00% | ≤2000 ms |
| [DisProt API](https://disprot.org/api/DP00003) | 🟢 up | 100.00% | 98.95% | 99.60% | 99.61% | 99.61% | 100.00% | ≤5000 ms |
| [DOME Copilot](https://copilot.dome-ml.org/) | 🟢 up | 100.00% | 99.65% | 95.14% | 95.23% | 95.23% | 100.00% | ≤1000 ms |
| [DOME Observatory](https://observatory.dome-ml.org/) | 🟢 up | 100.00% | 99.65% | 99.82% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [DOME Registry](https://registry.dome-ml.org/) | 🟢 up | 100.00% | 99.30% | 99.73% | 99.74% | 99.74% | 100.00% | ≤2000 ms |
| [DOME Registry API](https://registry.dome-ml.org/api/review?skip=0&limit=1) | 🟢 up | 100.00% | 99.65% | 99.82% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [DOME-ML website](https://dome-ml.org/) | 🟢 up | 100.00% | 99.65% | 99.78% | 99.78% | 99.78% | 100.00% | ≤2000 ms |
| [FELLS](http://old.protein.bio.unipd.it/fells/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [FELLS API](http://old.protein.bio.unipd.it/fellsws/status/123456789012345678901234) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [FuzDB](https://fuzdb.org/) | 🟢 up | 100.00% | 99.65% | 99.82% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [FuzDB API](https://fuzdb.org/api/entries?entry_id=FC00001) | 🟢 up | 100.00% | 99.65% | 99.82% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [FuzDrop](https://fuzdrop.bio.unipd.it/) | 🟢 up | 100.00% | 99.48% | 99.73% | 99.74% | 99.74% | 100.00% | ≤2000 ms |
| [FuzPred](https://fuzpred.bio.unipd.it/predictor) | 🟢 up | 100.00% | 99.30% | 99.73% | 99.74% | 99.74% | 100.00% | ≤2000 ms |
| [IDPcentral](https://idpcentral.org/) | 🟢 up | 100.00% | 99.30% | 99.64% | 99.65% | 99.65% | 100.00% | ≤10000 ms |
| [INGA](https://inga.bio.unipd.it/) | 🟢 up | 100.00% | 99.30% | 99.69% | 99.69% | 99.69% | 100.00% | ≤2000 ms |
| [MobiDB](https://mobidb.org/) | 🟢 up | 100.00% | 99.65% | 99.82% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [MobiDB API](https://mobidb.org/api/download?acc=P04637&format=json) | 🟢 up | 100.00% | 99.65% | 99.78% | 99.78% | 99.78% | 100.00% | ≤2000 ms |
| [NEEMO](http://old.protein.bio.unipd.it/neemo/) | 🟢 up | 100.00% | 99.83% | 99.96% | 99.96% | 99.96% | 100.00% | ≤2000 ms |
| [NTO Registry](https://nto-registry.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [OSAI](https://osai.dome-ml.org/) | 🟢 up | 100.00% | 99.65% | 99.82% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [PASTA](https://pasta.biocomputingup.it/) | 🟢 up | 100.00% | 99.65% | 99.78% | 99.78% | 99.78% | 100.00% | ≤2000 ms |
| [PASTA 2.0](http://old.protein.bio.unipd.it/pasta2/) | 🟢 up | 100.00% | 99.83% | 99.96% | 99.96% | 99.96% | 100.00% | ≤5000 ms |
| [PED](https://proteinensemble.org/) | 🟢 up | 100.00% | 99.30% | 99.69% | 99.69% | 99.69% | 100.00% | ≤2000 ms |
| [PED API](https://deposition.proteinensemble.org/api/entries/PED00001) | 🟢 up | 100.00% | 98.78% | 99.33% | 99.30% | 99.30% | 100.00% | ≤5000 ms |
| [PhytotypeDB](http://phytotypedb.bio.unipd.it/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [RAPHAEL](http://old.protein.bio.unipd.it/raphael/) | 🟢 up | 100.00% | 99.83% | 99.96% | 99.96% | 99.96% | 100.00% | ≤2000 ms |
| [RepeatsDB](https://repeatsdb.org/) | 🟢 up | 100.00% | 99.48% | 98.66% | 98.69% | 98.69% | 100.00% | ≤2000 ms |
| [RepeatsDB API](https://repeatsdb.org/api/production/annotations?skip=0&limit=1) | 🟢 up | 100.00% | 99.48% | 98.66% | 98.69% | 98.69% | 100.00% | ≤5000 ms |
| [RepeatsDB-lite](http://old.protein.bio.unipd.it/repeatsdb-lite/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [RING](https://ring.biocomputingup.it/) | 🟢 up | 100.00% | 99.48% | 99.73% | 99.74% | 99.74% | 100.00% | ≤2000 ms |
| [RUBI](http://old.protein.bio.unipd.it/rubi/) | 🟢 up | 100.00% | 99.83% | 99.96% | 99.96% | 99.96% | 100.00% | ≤5000 ms |
| [SODA](http://old.protein.bio.unipd.it/soda/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [VHLdb](https://vhldb.org/) | 🟢 up | 100.00% | 99.65% | 99.78% | 99.78% | 99.78% | 100.00% | ≤2000 ms |

---

## Recent state changes

The newest entries from `events.jsonl`, the full audit trail of every state change.

| When (UTC) | Resource | Change | Detail |
|---|---|---|---|
| 2026-11-27T22:15:29Z | PED API | 🔴 down → 🟢 up | `ok` |
| 2026-11-27T21:55:22Z | PED API | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-26T14:35:33Z | PED API | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T14:35:33Z | DisProt API | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T14:15:31Z | DOME Registry | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T14:15:31Z | FuzDrop | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T14:15:31Z | RING | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T14:15:31Z | IDPcentral | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T14:15:31Z | CAID API | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T14:15:31Z | PED API | 🟢 up → 🔴 down | `connection_error` |
| 2026-11-26T14:15:31Z | DisProt API | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-26T13:55:33Z | DOME Registry | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-26T13:55:33Z | FuzDrop | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-26T13:55:33Z | RING | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-26T13:55:33Z | IDPcentral | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-26T13:55:33Z | CAID API | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-26T11:55:25Z | RUBI | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T11:55:25Z | RAPHAEL | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T11:55:25Z | PASTA 2.0 | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T11:55:25Z | NEEMO | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T11:55:25Z | BLUUES | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T11:55:25Z | Align2 | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T11:55:25Z | DOME Copilot | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T11:55:25Z | DOME Registry API | 🔴 down → 🟢 up | `ok` |
| 2026-11-26T11:35:24Z | RUBI | 🟢 up → 🔴 down | `http_503` |

---

Generated by [monitor/scripts/summarize.py](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/main/monitor/scripts/summarize.py) at **2026-11-28T20:55:32Z**, and rewritten after every check. Machine-readable: [summary.json](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/monitor-data/summary.json).
