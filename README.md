# BioComp resource monitor

Uptime **and backend-API** monitoring of the BioComputing UP resources (DisProt, MobiDB,
RepeatsDB, PED, FuzDB, APICURON, CAID, RING and others). It runs every 20 minutes on free GitHub
Actions and publishes a dashboard on GitHub Pages that also shows the DOME ecosystem from
[dome-tracking](https://github.com/BioComputingUP/dome-tracking).

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/monitoring.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml)
[![responding](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/up.json)](https://biocomputingup.github.io/BioComp_resource_monitor/)
[![APIs](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/api.json)](https://biocomputingup.github.io/BioComp_resource_monitor/)
[![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/down.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/monitor-data/STATUS.md#needs-attention)
[![runs in last 24h](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/runs-24h.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml)

**🖥️ Dashboard: https://biocomputingup.github.io/BioComp_resource_monitor/** ·
**📄 [STATUS.md](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/monitor-data/STATUS.md)** ·
**🚨 [Outages](https://github.com/BioComputingUP/BioComp_resource_monitor/issues?q=label%3Aoutage)**

## What it checks

- **25 websites** in four groups: databases, tools, lab & registries, and the legacy tools on
  `old.protein.bio.unipd.it`. Each is classified up, challenged (a bot check) or down.
- **7 backend APIs** (DisProt, MobiDB, RepeatsDB, PED, FuzDB, APICURON, CAID). An API is **up**
  only if it answers with JSON containing a known record. If it answers with anything else,
  such as the web app's HTML page, it is **wrong payload**, which is shown apart from
  **down**.
- **Code activity** of each resource's GitHub repo.
- After **two failed runs in a row** an issue is opened, which emails @gavinf97. It closes
  itself when the target recovers.

The list is in [`monitor/resources.yml`](monitor/resources.yml). How it works, the definitions
and the common tasks are in [`monitor/README.md`](monitor/README.md).

## Finish setup (about 10 minutes)

GitHub's own scheduler drops most runs: `dome-tracking` gets about 17 of the 72 runs it should
get a day. A free external cron that triggers the workflow fixes this, as it has for ECD. You do
this once, and it can fix `dome-tracking` at the same time.

1. **Make a token.** Go to <https://github.com/settings/personal-access-tokens/new> and create a
   *fine-grained* token:
   - **Resource owner:** BioComputingUP
   - **Repository access:** only select repositories → `BioComp_resource_monitor` and `dome-tracking`
   - **Permissions → Repository → Actions:** Read and write. Nothing else.
   - **Expiration:** 1 year. Copy the token.
   - If the org requires approval, an org owner approves it at *BioComputingUP → Settings →
     Personal access tokens → Pending requests*.
2. **Create the cron job.** Sign up at <https://cron-job.org> (free) → *Create cronjob*:
   - **URL:** `https://api.github.com/repos/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml/dispatches`
   - **Execution schedule:** Custom → every day, every hour, minutes **15, 35, 55**
   - **Advanced → Request method:** `POST`
   - **Advanced → Headers:**
     `Authorization: Bearer <your token>` ·
     `Accept: application/vnd.github+json` ·
     `X-GitHub-Api-Version: 2022-11-28`
   - **Advanced → Request body:** `{"ref":"main"}`
   - **Notifications:** on, for failed executions
3. **Fix dome-tracking too.** Click *Clone* on that job and change only:
   - **URL:** `https://api.github.com/repos/BioComputingUP/dome-tracking/actions/workflows/tracker-check.yml/dispatches`
   - **Minutes:** **5, 25, 45**
4. **Test.** Press *Test run* on each job. The answer must be **204**. 401/403 means the token or
   its permission is wrong. 404 means the URL is wrong or the token lacks access to that repo.
   Then check:
   ```bash
   gh run list -R BioComputingUP/BioComp_resource_monitor --event workflow_dispatch -L 3
   gh run list -R BioComputingUP/dome-tracking --event workflow_dispatch -L 3
   ```
   Within a day, the dashboard's **runs in 24 h** for both shows close to 72 of 72, in green.
5. **Set a calendar reminder** a week before the token expires. Regenerate the token and paste
   the new one into both jobs. Until then, runs fall back to GitHub's crons and the runs-in-24 h
   figure turns amber.

*If the org does not allow fine-grained tokens:* use a classic token
(<https://github.com/settings/tokens>) with only the `repo` scope, in the same header.

**Optional:** to show code activity for the private repos (`mobidb-ui`, `ring-ui`, `bup-ui`),
add a read-only `ACTIVITY_TOKEN` secret. See
[monitor/README.md → Common tasks](monitor/README.md#3-common-tasks).

## Free-plan limits

| Limit | How it is handled |
|---|---|
| Scheduled runs are best-effort | External `workflow_dispatch` trigger (above). The 4 GitHub crons an hour are a backup only |
| Actions minutes | The repo is **public**, so minutes are free and unmetered. A run takes about 1–2 minutes |
| Pages: 10 builds an hour | At most 7 runs an hour (3 external + 4 backup) |
| Schedules disabled after 60 days without activity | Only the backup is affected. The external trigger keeps running. The dashboard shows **STALE** after 3 h without a run |
| API rate limit (1,000 requests an hour) | About 15 GitHub API calls a run |

Results live on the [`monitor-data`](https://github.com/BioComputingUP/BioComp_resource_monitor/tree/monitor-data)
branch, one commit per day. `main` holds only the code.
