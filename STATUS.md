# BioComp resource monitor status

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/monitoring.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml) [![up](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/up.json)](#all-resources) [![api](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/api.json)](#all-resources) [![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/down.json)](#needs-attention) [![runs 24h](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/runs-24h.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml) [![activity](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/activity.json)](#repository-activity)

## 🟢 Monitoring is ACTIVE

| | |
|---|---|
| **Monitored** | 32 websites and 8 APIs — every one, every 20 minutes, continuously |
| **Last check** | 2026-11-08T23:55:19Z (0 min ago) |
| **Runs in the last 24 h** | 89 of a target 72 |
| **Checks recorded** | 610 runs since monitoring began |
| **Runs on** | [GitHub Actions → monitor-check](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml) |
| **Visual dashboard** | https://biocomputingup.github.io/BioComp_resource_monitor/ |

### Right now

🟢 up **32** · 🟡 challenged **0** · 🔴 down **0** · ⚪ never checked **0** · 🔗 check URL to review **0**

**APIs:** 🟢 OK **8** of 8 · 🔴 down **0** (of which 🟠 responding with the wrong payload **0**)

An API counts as up only when it answers 2xx with JSON that matches its `api.expect` in resources.yml; a `bad_payload:*` reason means it answered, but with the wrong content. Uptime = (up + challenged) ÷ recorded checks. Coverage = recorded ÷ expected checks. 99.00% is a reference line only; it sorts the list below. Full definitions: [monitor/README.md](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/main/monitor/README.md).

---

## Repository activity

`Last push` is the latest push to **any** branch; `Head commit` is the tip of the default branch. The full timeline is in [activity_history.jsonl](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/monitor-data/activity_history.jsonl).

| Resource | Repository | Last push | Activity | Head commit |
|---|---|---|---|---|
| MobiDB | [BioComputingUP/mobidb-ui](https://github.com/BioComputingUP/mobidb-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| PED | [BioComputingUP/ped5-ui](https://github.com/BioComputingUP/ped5-ui) `main` | 2026-09-07T12:26:09Z (62 days ago) | 🔴 quiet (≥30 d) | [`40b2996`](https://github.com/BioComputingUP/ped5-ui/commit/40b2996038ee81412725d4737d6e4d3f67f287a3) Test local configuration — Ivan Mičetić, 2026-09-07 |
| APICURON | [BioComputingUP/apicuron](https://github.com/BioComputingUP/apicuron) `master` | 2026-11-06T14:59:38Z (2 days ago) | 🟢 active (<7 d) | [`9f58463`](https://github.com/BioComputingUP/apicuron/commit/9f58463dca6b295818adf7dd8145d85547a100eb) Merge pull request #30 from BioComputingUP/feat/resource-managers — Mehdi Zoubiri, 2026-11-05 |
| RING | [BioComputingUP/ring-ui](https://github.com/BioComputingUP/ring-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| BioComputing UP website | [BioComputingUP/bup-ui](https://github.com/BioComputingUP/bup-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| NTO Registry | [BioComputingUP/nto-registry](https://github.com/BioComputingUP/nto-registry) `main` | 2026-10-22T15:37:29Z (17 days ago) | 🟡 recent (<30 d) | [`9057881`](https://github.com/BioComputingUP/nto-registry/commit/90578813a42b509c956b8ddfe0a72f05351166fd) Security: update site dependencies to clear npm audit advisories — Gavin Farrell, 2026-10-22 |
| DOME-ML website | [BioComputingUP/dome-ml-ui](https://github.com/BioComputingUP/dome-ml-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| DOME Registry | [BioComputingUP/dome-registry](https://github.com/BioComputingUP/dome-registry) `main` | 2026-07-29T13:14:04Z (102 days ago) | 🔴 quiet (≥30 d) | [`4978003`](https://github.com/BioComputingUP/dome-registry/commit/4978003db56b9a36bc078689ceb4bf51679be708) Add dome 2.0 schema + Logo modification — abdelghaniomar, 2026-07-29 |
| DOME Copilot | [IFCA-Advanced-Computing/dome-copilot](https://github.com/IFCA-Advanced-Computing/dome-copilot) `master` | 2026-03-30T11:32:42Z (223 days ago) | 🔴 quiet (≥30 d) | [`e157c7b`](https://github.com/IFCA-Advanced-Computing/dome-copilot/commit/e157c7b56b2ef326dd9b3523b270591ba65a3542) feat: make the model names configurable — Ignacio Heredia, 2026-03-30 |
| OSAI | [BioComputingUP/dome-ml-osai-ui](https://github.com/BioComputingUP/dome-ml-osai-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| DOME Observatory | [BioComputingUP/dome-ml-observatory](https://github.com/BioComputingUP/dome-ml-observatory) `main` | 2026-10-22T15:36:34Z (17 days ago) | 🟡 recent (<30 d) | [`c749889`](https://github.com/BioComputingUP/dome-ml-observatory/commit/c749889b8f9b3cf3366c1a31e4bf7392bdbf0d14) Security: update dependencies to clear npm audit advisories — gavinfarrell, 2026-10-22 |

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
| [RepeatsDB](https://repeatsdb.org/) | 96.23% | 67.11% | 23 |
| [RepeatsDB API](https://repeatsdb.org/api/production/annotations?skip=0&limit=1) | 96.23% | 67.11% | 23 |
| [BioComputing UP website](https://biocomputingup.it/) | 98.20% | 67.11% | 11 |

---

## All resources

All 32 websites and 8 APIs, sorted by name. Sortable and searchable on the [dashboard](https://biocomputingup.github.io/BioComp_resource_monitor/).

| Resource | State | Today | 7d | 30d | 90d | 365d | Coverage 30d | p95 30d |
|---|---|---|---|---|---|---|---|---|
| [Align2](http://old.protein.bio.unipd.it/align2/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤5000 ms |
| [APICURON](https://apicuron.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [APICURON API](https://apicuron.org/api/home) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [BioComputing UP website](https://biocomputingup.it/) | 🟢 up | 97.73% | 97.83% | 98.20% | 98.20% | 98.20% | 67.11% | ≤5000 ms |
| [BLUUES](https://bluues.biocomputingup.it/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.26% | ≤2000 ms |
| [BLUUES](http://old.protein.bio.unipd.it/bluues/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤5000 ms |
| [CAID](https://caid.idpcentral.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [CAID API](https://caid.idpcentral.org/dataset-repository/api/dataset/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [DisProt](https://disprot.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [DisProt API](https://disprot.org/api/DP00003) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [DOME Copilot](https://dome-copilot.ifca.es/) | 🟢 up ⚠️ TLS | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.22% | ≤1000 ms |
| [DOME Observatory](https://observatory.dome-ml.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.22% | ≤1000 ms |
| [DOME Registry](https://registry.dome-ml.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.22% | ≤1000 ms |
| [DOME Registry API](https://registry.dome-ml.org/api/review?skip=0&limit=1) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.22% | ≤2000 ms |
| [DOME-ML website](https://dome-ml.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.22% | ≤2000 ms |
| [FELLS](http://old.protein.bio.unipd.it/fells/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤5000 ms |
| [FuzDB](https://fuzdb.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [FuzDB API](https://fuzdb.org/api/entries?entry_id=FC00001) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [FuzDrop](https://fuzdrop.bio.unipd.it/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [FuzPred](https://fuzpred.bio.unipd.it/predictor) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [IDPcentral](https://idpcentral.org/) | 🟢 up | 100.00% | 99.41% | 99.51% | 99.51% | 99.51% | 67.11% | ≤5000 ms |
| [INGA](https://inga.bio.unipd.it/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [MobiDB](https://mobidb.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [MobiDB API](https://mobidb.org/api/download?acc=P04637&format=json) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [NEEMO](http://old.protein.bio.unipd.it/neemo/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤5000 ms |
| [NTO Registry](https://nto-registry.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤1000 ms |
| [OSAI](https://osai.dome-ml.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.22% | ≤1000 ms |
| [PASTA](https://pasta.biocomputingup.it/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.26% | ≤2000 ms |
| [PASTA 2.0](http://old.protein.bio.unipd.it/pasta2/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤2000 ms |
| [PED](https://proteinensemble.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [PED API](https://deposition.proteinensemble.org/api/entries/PED00001) | 🟢 up | 100.00% | 99.80% | 99.67% | 99.67% | 99.67% | 67.11% | ≤5000 ms |
| [PhytotypeDB](http://phytotypedb.bio.unipd.it/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤2000 ms |
| [RAPHAEL](http://old.protein.bio.unipd.it/raphael/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤2000 ms |
| [RepeatsDB](https://repeatsdb.org/) | 🟢 up | 100.00% | 95.47% | 96.23% | 96.23% | 96.23% | 67.11% | ≤2000 ms |
| [RepeatsDB API](https://repeatsdb.org/api/production/annotations?skip=0&limit=1) | 🟢 up | 100.00% | 95.47% | 96.23% | 96.23% | 96.23% | 67.11% | ≤5000 ms |
| [RepeatsDB-lite](http://old.protein.bio.unipd.it/repeatsdb-lite/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤2000 ms |
| [RING](https://ring.biocomputingup.it/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |
| [RUBI](http://old.protein.bio.unipd.it/rubi/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤5000 ms |
| [SODA](http://old.protein.bio.unipd.it/soda/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 67.11% | ≤2000 ms |
| [VHLdb](https://vhldb.org/) | 🟢 up | 100.00% | 99.80% | 99.84% | 99.84% | 99.84% | 67.11% | ≤2000 ms |

---

## Recent state changes

The newest entries from `events.jsonl`, the full audit trail of every state change.

| When (UTC) | Resource | Change | Detail |
|---|---|---|---|
| 2026-11-08T22:55:17Z | BioComputing UP website | 🔴 down → 🟢 up | `ok` |
| 2026-11-08T22:35:18Z | BioComputing UP website | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-08T15:23:19Z | BioComputing UP website | 🔴 down → 🟢 up | `ok` |
| 2026-11-08T15:15:28Z | BioComputing UP website | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-07T06:15:27Z | BioComputing UP website | 🔴 down → 🟢 up | `ok` |
| 2026-11-07T05:55:19Z | BioComputing UP website | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-06T11:28:06Z | BioComputing UP website | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T11:28:06Z | IDPcentral | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T11:15:31Z | BioComputing UP website | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-06T11:15:31Z | IDPcentral | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-06T09:55:21Z | RepeatsDB API | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T09:55:21Z | RepeatsDB | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T03:35:18Z | RepeatsDB API | 🟢 up → 🔴 down | `tls_error` |
| 2026-11-06T03:35:18Z | RepeatsDB | 🟢 up → 🔴 down | `tls_error` |
| 2026-11-06T02:35:18Z | BioComputing UP website | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T02:35:18Z | IDPcentral | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T02:15:29Z | BioComputing UP website | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-06T02:15:29Z | IDPcentral | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-06T00:35:19Z | DOME Observatory | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T00:35:19Z | OSAI | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T00:35:19Z | DOME Registry API | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T00:35:19Z | DOME Registry | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T00:35:19Z | DOME-ML website | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T00:35:19Z | PASTA | 🔴 down → 🟢 up | `ok` |
| 2026-11-06T00:35:19Z | BLUUES | 🔴 down → 🟢 up | `ok` |

---

Generated by [monitor/scripts/summarize.py](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/main/monitor/scripts/summarize.py) at **2026-11-08T23:55:25Z**, and rewritten after every check. Machine-readable: [summary.json](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/monitor-data/summary.json).
