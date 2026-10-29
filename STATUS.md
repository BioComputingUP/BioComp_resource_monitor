# BioComp resource monitor status

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/monitoring.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml) [![up](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/up.json)](#all-resources) [![api](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/api.json)](#all-resources) [![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/down.json)](#needs-attention) [![runs 24h](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/runs-24h.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml) [![activity](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/activity.json)](#repository-activity)

## 🟢 Monitoring is ACTIVE

| | |
|---|---|
| **Monitored** | 32 websites and 8 APIs — every one, every 20 minutes, continuously |
| **Last check** | 2026-10-29T23:23:54Z (0 min ago) |
| **Runs in the last 24 h** | 20 of a target 72 |
| **Checks recorded** | 49 runs since monitoring began |
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
| PED | [BioComputingUP/ped5-ui](https://github.com/BioComputingUP/ped5-ui) `main` | 2026-09-07T12:26:09Z (52 days ago) | 🔴 quiet (≥30 d) | [`40b2996`](https://github.com/BioComputingUP/ped5-ui/commit/40b2996038ee81412725d4737d6e4d3f67f287a3) Test local configuration — Ivan Mičetić, 2026-09-07 |
| APICURON | [BioComputingUP/apicuron](https://github.com/BioComputingUP/apicuron) `master` | 2026-10-29T16:14:46Z (7 h ago) | 🟢 active (<7 d) | [`a397af0`](https://github.com/BioComputingUP/apicuron/commit/a397af0d44fa2d5ec9ccf489455388be72149f81) Merge pull request #20 from BioComputingUP/fix/report-submission-global-fields — Mehdi Zoubiri, 2026-10-29 |
| RING | [BioComputingUP/ring-ui](https://github.com/BioComputingUP/ring-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| BioComputing UP website | [BioComputingUP/bup-ui](https://github.com/BioComputingUP/bup-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| NTO Registry | [BioComputingUP/nto-registry](https://github.com/BioComputingUP/nto-registry) `main` | 2026-10-22T15:37:29Z (7 days ago) | 🟡 recent (<30 d) | [`9057881`](https://github.com/BioComputingUP/nto-registry/commit/90578813a42b509c956b8ddfe0a72f05351166fd) Security: update site dependencies to clear npm audit advisories — Gavin Farrell, 2026-10-22 |
| DOME-ML website | [BioComputingUP/dome-ml-ui](https://github.com/BioComputingUP/dome-ml-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| DOME Registry | [BioComputingUP/dome-registry](https://github.com/BioComputingUP/dome-registry) `main` | 2026-07-29T13:14:04Z (92 days ago) | 🔴 quiet (≥30 d) | [`4978003`](https://github.com/BioComputingUP/dome-registry/commit/4978003db56b9a36bc078689ceb4bf51679be708) Add dome 2.0 schema + Logo modification — abdelghaniomar, 2026-07-29 |
| DOME Copilot | [IFCA-Advanced-Computing/dome-copilot](https://github.com/IFCA-Advanced-Computing/dome-copilot) `master` | 2026-03-30T11:32:42Z (213 days ago) | 🔴 quiet (≥30 d) | [`e157c7b`](https://github.com/IFCA-Advanced-Computing/dome-copilot/commit/e157c7b56b2ef326dd9b3523b270591ba65a3542) feat: make the model names configurable — Ignacio Heredia, 2026-03-30 |
| OSAI | [BioComputingUP/dome-ml-osai-ui](https://github.com/BioComputingUP/dome-ml-osai-ui) | — (never) | ⚪ unknown ⚠️ 404: repository not found or private; the token cannot read it (set the ACTIVITY_TOKEN secret) | — |
| DOME Observatory | [BioComputingUP/dome-ml-observatory](https://github.com/BioComputingUP/dome-ml-observatory) `main` | 2026-10-22T15:36:34Z (7 days ago) | 🟡 recent (<30 d) | [`c749889`](https://github.com/BioComputingUP/dome-ml-observatory/commit/c749889b8f9b3cf3366c1a31e4bf7392bdbf0d14) Security: update dependencies to clear npm audit advisories — gavinfarrell, 2026-10-22 |

---

## Needs attention

### 🔴 Currently down

None — every monitored website and API is up.

### 🔗 Check URL needs review

None.

### 📉 Below 99.00% over the last 30 days

**1** resources, worst first.

| Resource | 30d uptime | 30d coverage | Down checks |
|---|---|---|---|
| [PED API](https://deposition.proteinensemble.org/api/entries/PED00001) | 97.96% | 26.06% | 1 |

---

## All resources

All 32 websites and 8 APIs, sorted by name. Sortable and searchable on the [dashboard](https://biocomputingup.github.io/BioComp_resource_monitor/).

| Resource | State | Today | 7d | 30d | 90d | 365d | Coverage 30d | p95 30d |
|---|---|---|---|---|---|---|---|---|
| [Align2](http://old.protein.bio.unipd.it/align2/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤2000 ms |
| [APICURON](https://apicuron.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [APICURON API](https://apicuron.org/api/home) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [BioComputing UP website](https://biocomputingup.it/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [BLUUES](https://bluues.biocomputingup.it/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 25.68% | ≤5000 ms |
| [BLUUES](http://old.protein.bio.unipd.it/bluues/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤2000 ms |
| [CAID](https://caid.idpcentral.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [CAID API](https://caid.idpcentral.org/dataset-repository/api/dataset/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [DisProt](https://disprot.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [DisProt API](https://disprot.org/api/DP00003) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [DOME Copilot](https://dome-copilot.ifca.es/) | 🟢 up ⚠️ TLS | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 25.27% | ≤1000 ms |
| [DOME Observatory](https://observatory.dome-ml.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 25.27% | ≤1000 ms |
| [DOME Registry](https://registry.dome-ml.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 25.27% | ≤5000 ms |
| [DOME Registry API](https://registry.dome-ml.org/api/review?skip=0&limit=1) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 25.27% | ≤5000 ms |
| [DOME-ML website](https://dome-ml.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 25.27% | ≤5000 ms |
| [FELLS](http://old.protein.bio.unipd.it/fells/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤2000 ms |
| [FuzDB](https://fuzdb.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [FuzDB API](https://fuzdb.org/api/entries?entry_id=FC00001) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [FuzDrop](https://fuzdrop.bio.unipd.it/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [FuzPred](https://fuzpred.bio.unipd.it/predictor) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [IDPcentral](https://idpcentral.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤10000 ms |
| [INGA](https://inga.bio.unipd.it/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [MobiDB](https://mobidb.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [MobiDB API](https://mobidb.org/api/download?acc=P04637&format=json) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [NEEMO](http://old.protein.bio.unipd.it/neemo/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [NTO Registry](https://nto-registry.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤1000 ms |
| [OSAI](https://osai.dome-ml.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 25.27% | ≤1000 ms |
| [PASTA](https://pasta.biocomputingup.it/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 25.68% | ≤5000 ms |
| [PASTA 2.0](http://old.protein.bio.unipd.it/pasta2/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤2000 ms |
| [PED](https://proteinensemble.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [PED API](https://deposition.proteinensemble.org/api/entries/PED00001) | 🟢 up | 100.00% | 97.96% | 97.96% | 97.96% | 97.96% | 26.06% | ≤5000 ms |
| [PhytotypeDB](http://phytotypedb.bio.unipd.it/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤2000 ms |
| [RAPHAEL](http://old.protein.bio.unipd.it/raphael/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤2000 ms |
| [RepeatsDB](https://repeatsdb.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [RepeatsDB API](https://repeatsdb.org/api/production/annotations?skip=0&limit=1) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤10000 ms |
| [RepeatsDB-lite](http://old.protein.bio.unipd.it/repeatsdb-lite/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤2000 ms |
| [RING](https://ring.biocomputingup.it/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |
| [RUBI](http://old.protein.bio.unipd.it/rubi/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤2000 ms |
| [SODA](http://old.protein.bio.unipd.it/soda/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤2000 ms |
| [VHLdb](https://vhldb.org/) | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 26.06% | ≤5000 ms |

---

## Recent state changes

The newest entries from `events.jsonl`, the full audit trail of every state change.

| When (UTC) | Resource | Change | Detail |
|---|---|---|---|
| 2026-10-29T00:05:25Z | PED API | 🔴 down → 🟢 up | `ok` |
| 2026-10-28T23:58:51Z | PED API | 🟢 up → 🔴 down | `read_timeout` |
| 2026-10-27T11:00:42Z | DOME Observatory | new → 🟢 up | `ok` |
| 2026-10-27T11:00:42Z | OSAI | new → 🟢 up | `ok` |
| 2026-10-27T11:00:42Z | DOME Copilot | new → 🟢 up | `ok` |
| 2026-10-27T11:00:42Z | DOME Registry API | new → 🟢 up | `ok` |
| 2026-10-27T11:00:42Z | DOME Registry | new → 🟢 up | `ok` |
| 2026-10-27T11:00:42Z | DOME-ML website | new → 🟢 up | `ok` |
| 2026-10-27T10:59:29Z | dome | new → 🟢 up | `ok` |
| 2026-10-27T10:59:29Z | PASTA | new → 🟢 up | `ok` |
| 2026-10-27T10:59:29Z | BLUUES | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | SODA | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | RUBI | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | RepeatsDB-lite | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | RAPHAEL | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | PASTA 2.0 | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | NEEMO | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | FELLS | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | BLUUES | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | Align2 | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | NTO Registry | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | BioComputing UP website | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | INGA | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | FuzPred | new → 🟢 up | `ok` |
| 2026-10-27T09:19:14Z | FuzDrop | new → 🟢 up | `ok` |

---

Generated by [monitor/scripts/summarize.py](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/main/monitor/scripts/summarize.py) at **2026-10-29T23:24:08Z**, and rewritten after every check. Machine-readable: [summary.json](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/monitor-data/summary.json).
