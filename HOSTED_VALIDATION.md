# College Basketball hosted validation — October 24, 2026

Live app: https://college-basketball-statistical-research.streamlit.app/

Repository: https://github.com/Pokered03/College-Basketball-Statistical-Research

Independent public repository and free deployment were authorized. The other five dashboards and existing Multi-Sport Value Engine were not modified.

## Independent software and data checks

The fresh published copy passed 43 applicable tests, with three unrelated adapter cases skipped (2.30 seconds). The final source project also passed all 43. Tests include filtered D-I membership, source/box reconciliation, missing data, chronological leakage, status/identity validation, failed-refresh retention, app rendering without network calls, package checksum/size/truncation failures and last-good-database retention. TBD source tipoffs preserve the calendar date and withhold the placeholder time.

Current registry: 366 source-registered teams in the ending-year 2027 preseason. There are no completed games in that season. Prior seasons 2024, 2025 and 2026 cover 362, 364 and 365 teams respectively. The 2027 registry uses previous available standings plus published conference membership and is provisional until official current-season standings are published; these are source-observed counts, not independent certification of membership completeness.

The prepared database is 34.50 MiB and is published as an approximately 5.56 MiB gzip file plus SHA-256 manifest. The host restores it on disk in 1 MiB streaming blocks, with a process lock, a 256 MiB expansion cap and atomic replacement only after hash/size validation. Unchanged reruns reuse the verified file. No full historical table is loaded into RAM. The worker restores the previous package before a current-season update, retaining historical records, then publishes a new checked package. No expanded database or transient restore state is committed.

Fresh public-copy 64-switch AppTest (including initial package restoration): cold render 0.348 seconds, switching p95 0.084 seconds, peak process RSS 162.70 MiB. Local cached active-season worker: 21.27 seconds and 306.06 MiB. Local SQLite integrity and HTTP health/root checks passed. These measurements met the local targets of startup under 10 seconds, switching under 2 seconds, UI under 350 MiB and worker under 650 MiB. The retained stress-256.json is an earlier local build measurement, not a fresh deployed stress test.

## Initial live verification

- Independent Streamlit Community Cloud deployment uses main/app.py, Python 3.12 and PyArrow 24.0.0.
- The current-season October 24 empty schedule showed nearby November dates and clear guidance. Manual current-season teams displayed N/A and PASS rather than prior-season values.
- November 2 calendar selection loaded a published Lafayette–Butler matchup with honest missing-statistics warnings. The final source-marked American University–Cincinnati tipoff displayed Time unavailable rather than midnight.
- Historical ending-year 2026 Rutgers–Northwestern research rendered offensive/defensive/situational split statistics, opponent-adjusted efficiencies, sample counts and ranks. Last 3/5/10 switching, neutral venue, manual spread -3.5 and total 145.5 inputs worked. Retrospective confidence stayed PASS.
- Timestamped completed-game rotations and reported starters were visible for both teams, explicitly distinct from live injuries or future lineup confirmations.
- Initial sampled web-process peak 176.0 MiB; exposed cgroup limit 3072 MiB; container samples approximately 727.1–744.7 MiB, including other processes and file cache. Post-restart process sample 164.5 MiB. These are initial observations, not sustained hosted-load bounds.
- A controlled reboot recovered with the preseason explanation and historical comparison functioning. A second session independently displayed the current-season upcoming schedule while the first retained historical manual research. This is ordinary restart/two-session verification, not a multi-user stress test.
- First hosted refresh succeeded in 43 seconds: https://github.com/Pokered03/College-Basketball-Statistical-Research/actions/runs/40125357511 . The app picked up its 2026-10-24T19:27:42.947932+00:00 timestamp.
- Final corrected refresh succeeded in 54 seconds and published a new compressed package: https://github.com/Pokered03/College-Basketball-Statistical-Research/actions/runs/40125728232 . The live app exposed worker timestamp 2026-10-24T19:32:41.243220+00:00.

## Model and confidence limits

Chronological held-out baseline test: 6,253 games; Brier about 0.19552 versus 0.25 constant probability; calibration error 0.02455; scoring-margin MAE 9.386 points; total MAE 13.604 points. Simple comparison baselines were margin MAE 10.996 and total MAE 15.234. Earlier/later fitted-game samples are 908 / 5,345 (fewer than 10 versus 10+ prior fitted team games; minimum eligibility five). These measurements do not prove future accuracy or profitability. Historical pages are season-end descriptive research with hindsight, not reconstructed pregame pages.

The baseline scoring model does not apply validated injury, minutes/role-change or tracking adjustments. Win estimates require sufficient current data and the validation gate. Model separation score is distinct from model reliability. No verified historical college-basketball market lines are integrated, so spread/total confidence stays PASS. The current preseason has no observed team summaries, so its confidence stays PASS.

## Updates and outstanding work

ENABLE_FREE_REFRESH=true. Daily 10:47 UTC (6:47 AM Eastern daylight time / 5:47 AM standard time), subject to GitHub scheduling delays/inactivity policies and upstream freshness. Standard free public runner; no paid API, Odds API credits, paid hosting or Actions cache/artifact storage. This is daily updating, not live settlement.

Remaining: official current-season membership verification, more complete current data once play begins, reliable injuries/availability and calibrated player-role effects, verified market-line/category evaluation, actual iPhone/MacBook testing, sustained multi-user load, long-term stability and extended failure recovery. Missing values stay N/A. Source attribution and original trademark rights are preserved; no logos are distributed.

Status: live development dashboard with initial independent hosted checks; full requested professional completion is not claimed. Reboot only this app after imported engine changes; data-only packages refresh through database revision keys. See SIX_DASHBOARD_STATUS.md for the all-six checkpoint.
