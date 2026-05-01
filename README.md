# hudsonseed_pm — Health Monitor Agent

Heartbeat agent for the HudsonSeed Pitch Machine ecosystem.

## What it does
Every `LOOP_INTERVAL_SEC` seconds (default 300):
1. Pings Supabase (`agent_runs` table) — confirms DB reachability.
2. Inserts a heartbeat row: `service=health_monitor`, `status=OK|DEGRADED|ERROR`.
3. Optionally posts to Slack via `SLACK_WEBHOOK`.

## Deploy targets
- **Railway**: long-running service. `LOOP_MODE=true` → runs forever in `while True`.
- **GitHub Actions**: cron `0 */4 * * *` → single-shot, exits 0/1.

## Required env
| Var | Where | Notes |
|---|---|---|
| `SUPABASE_URL` | Railway env + GitHub Secret | `https://pebhikfbpgntedvbxqph.supabase.co` |
| `SUPABASE_SERVICE_ROLE_KEY` | Railway env + GitHub Secret | service_role JWT |
| `SLACK_WEBHOOK` | optional | Slack incoming webhook URL |
| `LOOP_MODE` | Railway only | `"true"` for daemon mode |
| `LOOP_INTERVAL_SEC` | Railway only | default `300` |

## Crash history
- 4/27-28: 5x crashes. Root cause: `health_monitor.py` was overwritten with the YAML workflow file (commit `2c77a1c`). Python tried to parse YAML → SyntaxError on every restart. Also `agent_runs` table didn't exist in Supabase.
- 5/1: Fixed. Python restored, hardened (env-var fail-fast, exception handling, loop mode), `agent_runs` table created.
