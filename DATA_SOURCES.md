# Sources, permissions and coverage

Primary integrated source: [hoopR MBB / SportsDataverse](https://github.com/sportsdataverse/hoopR-mbb-data).

CC BY 4.0; modified by this research application

Only the independent men's Division I adapter runs. Data are from hoopR / SportsDataverse under CC BY 4.0, filtered and aggregated by this application. The upstream notice is retained in notices/hoopR-mbb-CC-BY-4.0.md. Original source/trademark rights remain; no logos are distributed. There are no paid feeds, Odds API keys or direct ESPN scraping in this app.

## Snapshot coverage at build time

```json
[
  {
    "season": 2024,
    "teams_with_completed_games": 362,
    "registered_teams": 362,
    "schedule_games": 5731,
    "latest_final": "2024-04-08"
  },
  {
    "season": 2025,
    "teams_with_completed_games": 364,
    "registered_teams": 364,
    "schedule_games": 5769,
    "latest_final": "2025-04-07"
  },
  {
    "season": 2026,
    "teams_with_completed_games": 365,
    "registered_teams": 365,
    "schedule_games": 5767,
    "latest_final": "2026-04-06"
  },
  {
    "season": 2027,
    "teams_with_completed_games": 0,
    "registered_teams": 366,
    "schedule_games": 1593,
    "latest_final": null
  }
]
```

These counts describe source observations, not independently certified official membership completeness. The current college-basketball preseason registry uses the latest available standings plus published conference membership; verify new-season changes when an official standings file becomes available. See the live coverage table for later updates.

## Expanded integrations and remaining gaps

Bench points and observed completed-game rotations are now integrated where five reported starters and player points reconcile with the final score. The current preseason has no completed games; historical seasons have reported starter/minute/lineup-change context. These are observed roles, not next-game availability, official usage rate or calibrated injury effects.

## Freshness and preseason limitations

The ending-year 2027 season is preseason at this checkpoint. Current-season teams and published future schedules are available, but there are no completed-game summaries or current-season probabilities yet. The application shows N/A and PASS rather than borrowing prior-season performance as current data. Select 2026, 2025 or 2024 for historical research. Those summaries describe season-end performance, not a reconstructed pregame view.

Daily free update is scheduled at 10:47 UTC (6:47 AM Eastern daylight time / 5:47 AM standard time), subject to GitHub delays. Registered-team counts are source observations; transitional D-I membership needs verification as official new-season standings become available.
