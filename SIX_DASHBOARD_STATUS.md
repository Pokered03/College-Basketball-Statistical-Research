# Six independent sports research dashboards — status report

Recorded October 24, 2026, Eastern time. **All six have separate public GitHub repositories and live Streamlit development deployments with individual initial checks. The full professional specification is not complete.** The table records the latest individual checks; it is not a simultaneous six-app load test.

| Dashboard | Live access | Repository | Applicable tests passed | Initial hosted process peak |
|---|---|---|---:|---:|
| NFL | https://nfl-statistical-research.streamlit.app/ | https://github.com/Pokered03/NFL-Statistical-Research | 36 | 161.5 MiB |
| NBA | https://nba-statistical-research.streamlit.app/ | https://github.com/Pokered03/NBA-Statistical-Research | 38 | 170.7 MiB |
| MLB | https://mlb-statistical-research.streamlit.app/ | https://github.com/Pokered03/MLB-Statistical-Research | 42 | 171.2 MiB |
| NHL | https://nhl-statistical-research.streamlit.app/ | https://github.com/Pokered03/NHL-Statistical-Research | 35 | 170.2 MiB |
| College Football | https://college-football-statistical-research.streamlit.app/ | https://github.com/Pokered03/College-Football-Statistical-Research | 37 | 166.6 MiB |
| College Basketball | https://college-basketball-statistical-research.streamlit.app/ | https://github.com/Pokered03/College-Basketball-Statistical-Research | 43 | 176.0 MiB |

Test counts include repeated shared engineering checks within each independent application, not 231 distinct scientific hypotheses. Unrelated sport-adapter cases are explicitly skipped. Each repository's HOSTED_VALIDATION.md is the detailed evidence record. Local tests, initial browser checks and sampled hosted memory do not establish sustained production reliability or complete research coverage.

## Delivered architecture and research

Each application has its own execution, database, analysis engine, prepared summaries, bounded caches, data worker, refresh workflow, testing and URL. No runtime imports, databases or worker processes are shared between sports. The existing Multi-Sport Value Engine was not modified.

Dark dense matchup tables show offensive, defensive and situational statistics, meaningful metric direction, observed sample sizes, split-specific ranks and advantages. Season, last 3/5/10, venue, available first-half and historical comparisons are implemented. Schedules and manual team comparison are supported. Research estimates expose chronological validation, uncertainty and limitations. Missing observations remain N/A. Unsupported confidence categories remain PASS.

- NFL: all 32 teams; scoring, passing/rushing and available play-by-play metrics. Historical spread/total gates were evaluated and failed, so those categories stay PASS.
- NBA: all 30 teams; possession-based team metrics and observed rotation context. Early-season small samples withhold probabilities. Rest/lineup context is not a validated causal forecast adjustment.
- MLB: all 30 teams; official current-season logs supplied both boxes for 2,465 completed games at the checkpoint. Official probable pitchers are timestamped and explicitly not confirmed. Regular-season dagger cells and postseason-inclusive rolling windows have different documented scopes.
- NHL: all 32 current teams; observed shots, faceoffs, Corsi/Fenwick, published pre-shot xG, explicitly defined xG >=0.20 chances and aggregate goalie GSAx where input reconciliation passes. Future starting goalies are not invented.
- College Football: 138 FBS and 128 FCS source-registered teams. The Division dropdown separates team lists, schedules, nearby dates and ranking populations. Cross-division selection is excluded. Histories retain actual covered opponents; the model/calibration is not independently validated for each division. Uneven FCS play-by-play coverage is disclosed. TBD kickoffs are withheld.
- College Basketball: NCAA men's D-I source registry, including 366 provisional current-season teams. The ending-year 2027 season has no completed games yet. Current statistics stay N/A/PASS; prior seasons are available for historical research. Observed rotations, bench scoring and opponent-adjusted possession efficiencies are documented; no verified next-game lineup is implied.

## Daily automatic updates

| Sport | Daily UTC schedule | Eastern daylight time | Eastern standard time |
|---|---|---|---|
| NFL | 10:17 | 6:17 AM | 5:17 AM |
| NBA | 10:23 | 6:23 AM | 5:23 AM |
| MLB | 10:29 | 6:29 AM | 5:29 AM |
| NHL | 10:35 | 6:35 AM | 5:35 AM |
| College Football | 10:41 | 6:41 AM | 5:41 AM |
| College Basketball | 10:47 | 6:47 AM | 5:47 AM |

Each workflow is enabled and its initial manually triggered hosted run passed. GitHub schedules may be delayed or pause after repository inactivity, and upstream publication can lag. This is daily prepared-data updating, not instant live-game settlement. Standard free public runners and free public Streamlit deployments are configured; no paid API, Odds API credits, paid hosting, or Actions cache/artifact storage was enabled. Public visibility for all six was approved.

## Memory and loading evidence

All apps use indexed selected-team reads and prepared summaries rather than fitting models or loading full historical tables during page rendering. Expensive collection and fitting run in independent workers. Latest local matchup switching p95 was below 0.11 seconds for the recorded checks; initial hosted process samples were below the 350 MiB development target. Hosting exposed a 3072 MiB cgroup limit in the observed containers; total container usage includes more than the web process. These values are observations, not guaranteed future hosting allocations.

College Basketball publishes its 34.5 MiB SQLite database as an approximately 5.6 MiB gzip asset with a SHA-256 manifest. Streaming 1 MiB blocks restore it to disk. A lock, checksum, size cap, last-good-file retention and atomic replacement are tested; unchanged reruns reuse the verified file. No whole-database in-memory decompression is used.

## Validation limits and remaining work

Each sport has time-based out-of-sample baseline validation. Estimated win probability and model reliability are separate concepts; the displayed separation score is not a guarantee. Historical summary pages contain hindsight and are not reconstructed historical pregame pages. No profitability or guaranteed accuracy claim is made. Advanced tracking/player metrics are generally descriptive inputs, not validated causal forecast effects.

Shared unfinished work: real iPhone/MacBook-specific verification, sustained multi-user hosted load, long-duration stability and extended failure recovery; more complete injury/availability inputs and calibrated lineup/rest effects; stronger sport-specific model comparisons and reliability categories. Initial restart checks do not replace these tests.

Specific gaps include MLB bullpen workloads, handedness/park/weather adjustments, wRC+/xFIP/Statcast and calibrated starter effects; NHL confirmed goalies, special-teams denominators and period splits; more complete FCS event coverage and separately calibrated FBS/FCS probability models; college basketball current-season membership verification when official standings appear, current availability, true usage/role effects and market-line validation. NFL, NBA and other sport-specific proprietary/tracking inputs remain limited as documented individually. Missing data are not replaced by unrelated statistics.

## Authorizations and next work

No additional credential or payment is needed for the currently configured free pipelines. Paid/licensed statistics, paid hosting or any Odds API usage require explicit approval before use. A service may independently require future account confirmation; it will not be bypassed. There are no automatic wagers, betting picks or parlays in these research applications.

Next development priorities are filling legally reusable free-data gaps, separating division-specific college-football calibration, refining sport-specific models and confidence validation, and completing device/load/stability checks. All six URLs can be bookmarked separately. Current milestone: **six independent live development dashboards; full project completion remains open.**
