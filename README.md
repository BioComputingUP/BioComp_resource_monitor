# BioComp resource monitor

Uptime and API monitoring of the BioComputing UP resources. It runs every 20 minutes: a cron job
triggers the check on free GitHub Actions, and the results are published to a dashboard on GitHub
Pages.

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/monitoring.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml)
[![responding](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/up.json)](https://biocomputingup.github.io/BioComp_resource_monitor/)
[![APIs](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/api.json)](https://biocomputingup.github.io/BioComp_resource_monitor/)
[![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/down.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/monitor-data/STATUS.md#needs-attention)
[![runs in last 24h](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/BioComputingUP/BioComp_resource_monitor/monitor-data/badges/runs-24h.json)](https://github.com/BioComputingUP/BioComp_resource_monitor/actions/workflows/monitor-check.yml)

Dashboard: https://biocomputingup.github.io/BioComp_resource_monitor/ ·
[STATUS.md](https://github.com/BioComputingUP/BioComp_resource_monitor/blob/monitor-data/STATUS.md) ·
[Outages](https://github.com/BioComputingUP/BioComp_resource_monitor/issues?q=label%3Aoutage)

## What it checks

- Websites: each is classified as up, challenged (a bot check) or down.
- APIs: an API is up only if it answers with JSON containing a known record. Any other answer,
  such as the web app's HTML page, is shown as wrong payload, separately from down.
- Code activity of each resource's GitHub repo.

The list is in [`monitor/resources.yml`](monitor/resources.yml). How it works, the definitions
and the common tasks are in [`monitor/README.md`](monitor/README.md).

## Outage emails

After two failed runs in a row, an issue is opened and Ivan Micetic
([ivanmicetic](https://github.com/ivanmicetic)), the BioComp admin, is emailed. The issue closes
itself when the resource is back up.

Others can be added through Ivan, either for all resources or for one specific resource, in
[`monitor/resources.yml`](monitor/resources.yml):

```yaml
notify:
  people: [ivanmicetic]       # emailed about every resource

- id: nto-registry
  ...
  notify: [gavinf97]          # also emailed when this resource (website or API) is down
```

## Free-plan limits

| Limit | How it is handled |
|---|---|
| Scheduled runs are best-effort | An external cron job triggers each run. The 4 GitHub crons an hour are only a backup |
| Actions minutes | The repo is public, so minutes are free and unmetered. A run takes about 1–2 minutes |
| Pages: 10 builds an hour | At most 7 runs an hour (3 external + 4 backup) |
| Schedules disabled after 60 days without activity | Only the backup is affected; the external trigger keeps running. The dashboard shows STALE after 3 h without a run |
| API rate limit (1,000 requests an hour) | About 15 GitHub API calls a run |

Results live on the [`monitor-data`](https://github.com/BioComputingUP/BioComp_resource_monitor/tree/monitor-data)
branch, one commit per day. `main` holds only the code.
