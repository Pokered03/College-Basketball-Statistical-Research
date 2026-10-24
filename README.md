# College Basketball Statistical Research Dashboard

Status: **live development dashboard with initial hosted verification; not complete.**

This repository is a single-sport, standalone Streamlit research application. It has no runtime dependency on another project, no imports from another dashboard, and no access to the existing Multi-Sport Value Engine. Every project has its own SQLite file, worker, model, caches, dependency specification and optional refresh workflow.

## Run locally

Python 3.12 is the tested runtime. From this repository directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m streamlit run app.py
```

The bundled `data/research.sqlite.gz` is real research data, not a demonstration fixture. A checked SHA-256 manifest and bounded 1 MiB streaming decompression restore the indexed SQLite file on disk, without loading historical tables into RAM. Subsequent unchanged reruns reuse the verified file. The application renders prepared summaries only and never fetches game or odds feeds during a page rerun.

## Use the dashboard

Choose a season and Eastern-time research date. Select a scheduled matchup, or choose Manual teams to compare any two registered teams. Team A is away and Team B is home unless Neutral venue is selected. Choose Last 3, Last 5 or Last 10; season, venue and available first-half splits remain visible alongside it. Swipe a wide statistical table horizontally on an iPhone. Sources, observed sample counts, ranking populations and update timestamps are exposed in the page.

Records and rankings are against covered opponents, not automatically an official league record. Historical seasons show descriptive season-end summaries, not reconstructed pregame pages. Upcoming rest is calendar days since the latest recorded final; it is not a predictive model input. No team logos are distributed pending verified usage rights.

## Refresh this sport only

Initial/full history build:

```bash
python -m research.pipeline
```

Routine active-season update:

```bash
python scripts/package_data.py unpack
python -m research.pipeline --seasons 2027
```

The worker downloads cached, approved free sources, validates IDs and statuses, updates the indexed store, builds summaries and runs chronological validation outside Streamlit. It publishes one SQLite file atomically. Network failures retain the last good file; same-database overlapping refreshes are rejected by a process lock. The source cache uses ETags/Last-Modified and bounded file downloads. Historical source files are not downloaded on a routine active-season refresh.

No Odds API key is read, requested, or used. No paid data integration is enabled.

## Expanded data integrations and remaining limitations

Bench points and observed completed-game rotations are now integrated where five reported starters and player points reconcile with the final score. The current preseason has no completed games; historical seasons have reported starter/minute/lineup-change context. These are observed roles, not next-game availability, official usage rate or calibrated injury effects.

Unverified injury/availability feeds, some requested advanced inputs, real-device testing and sustained hosted load/stability checks remain unfinished. The full specification has not been completed.

## Confidence panels

The baseline opponent-adjusted scoring model is fitted separately for this sport. Win probabilities are shown only after the empirical validation gate passes and the matchup has enough recent current-season data. A separation score is mathematically derived from calibrated probability; it is not a guarantee or a model-reliability percentage. Spread/total panels remain PASS unless both historical-line and confidence-category release gates pass. No historical college basketball market-line validation is integrated. Manual spread/total lines are supported; no betting picks are generated.

Read [METHODOLOGY.md](METHODOLOGY.md), [DATA_SOURCES.md](DATA_SOURCES.md) and [reports/backtest.json](reports/backtest.json). Backtest predictions can be regenerated; the large CSV audit output is excluded from routine Git commits.

## Independent verification

```bash
python -m pytest -q
python scripts/package_data.py unpack
python scripts/check_data.py
python scripts/benchmark.py
python scripts/smoke_server.py
```

Tests cover weighted aggregation, missing data, rank direction, duplicate/corrected results, postponed games, future-data leakage, invalid identities, read-only SQL, source-host restrictions, HTML escaping, app reruns, failed-source preservation and refresh locking. Tests for unrelated sport adapters are explicitly skipped.

The local target is cold AppTest render under 10 seconds, matchup switching under 2 seconds, and peak web-process RSS under 350 MiB. Worker target is under 650 MiB. These are development targets, **not verified hosting limits**. Reports record actual measurements, environment and whether a hosted resource limit was tested. AppTest is functional UI verification, not a real MacBook/iPhone browser rendering test.

## GitHub and live deployment

Repository: https://github.com/Pokered03/College-Basketball-Statistical-Research

Dashboard: https://college-basketball-statistical-research.streamlit.app/

Public visibility and free deployment were approved. The app uses Streamlit Community Cloud, main/app.py and Python 3.12. Initial live-browser, actual resource-limit, two-session and ordinary restart checks passed. See HOSTED_VALIDATION.md for the evidence and unfinished checks. No changes were made to the existing Multi-Sport Value Engine.

## Independent automatic updates

ENABLE_FREE_REFRESH=true is enabled. The daily cron is 10:47 UTC (6:47 AM Eastern daylight time / 5:47 AM standard time), subject to GitHub delays, inactivity policies and upstream data availability. Standard free public runners are configured; no cache/artifact storage, paid API or Odds API credits are used. Private-repository execution is blocked by the workflow condition. This is daily prepared-data updating, not instant game settlement.

The worker restores the last published database, updates the current season, validates it and commits the compressed store, manifest and model report. Historical data and summaries stay available. Monitor Git history growth under long-term use; an approved independent object store can be added later. Full professional feature, device and stability completion is not claimed.

## Publishing prepared updates

After a successful data refresh, run `python scripts/package_data.py pack`. Commit the compressed store, its manifest and the backtest report. The workflow unpacks the last published database before updating so historical seasons remain available. A process lock, checksum validation, 256 MiB expansion cap and atomic replacement preserve the last good local file when a package is damaged. Neither the expanded database nor local package-state files are committed. After imported engine code changes, reboot this independent deployment; ordinary data packages invalidate caches through the expanded file revision.

## Current season

The 2026–27 season (ending year 2027) has no completed games in the source at this checkpoint. Choose an earlier season and Manual teams for historical comparisons. Upcoming 2027-season matchups show N/A and PASS until enough new-season observations exist. TBD start times are withheld rather than displayed as midnight.

## Live verification

https://college-basketball-statistical-research.streamlit.app/

Read HOSTED_VALIDATION.md for observed tests and limits, and SIX_DASHBOARD_STATUS.md for the six-app development checkpoint. Real-device and sustained hosted load/stability verification remain unfinished.
