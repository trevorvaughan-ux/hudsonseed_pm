"""
HudsonSeed Health Monitor
Heartbeat agent. Runs on Railway (loop) + GitHub Actions (cron 4h).
Logs status to Supabase agent_runs table.
"""
import os
import sys
import time
import json
from datetime import datetime, timezone

import requests
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")  # optional
LOOP_MODE = os.getenv("LOOP_MODE", "false").lower() == "true"
LOOP_INTERVAL_SEC = int(os.getenv("LOOP_INTERVAL_SEC", "300"))  # 5 min default

def fail_fast_if_missing_env():
    missing = []
    if not SUPABASE_URL:
        missing.append("SUPABASE_URL")
    if not SUPABASE_KEY:
        missing.append("SUPABASE_SERVICE_ROLE_KEY")
    if missing:
        print(f"FATAL: missing env vars: {missing}", file=sys.stderr)
        sys.exit(1)

def log_run(supabase, status: str, message: str):
    try:
        supabase.table("agent_runs").insert({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "service": "health_monitor",
            "status": status,
            "message": message,
        }).execute()
    except Exception as e:
        print(f"WARN: failed to write to agent_runs: {e}", file=sys.stderr)

def check_supabase_reachable(supabase) -> bool:
    try:
        supabase.table("agent_runs").select("id").limit(1).execute()
        return True
    except Exception as e:
        print(f"Supabase reachability check failed: {e}", file=sys.stderr)
        return False

def post_slack(message: str):
    if not SLACK_WEBHOOK:
        return
    try:
        requests.post(SLACK_WEBHOOK, json={"text": message}, timeout=10)
    except Exception as e:
        print(f"WARN: slack post failed: {e}", file=sys.stderr)

def one_run(supabase):
    ts = datetime.now(timezone.utc).isoformat()
    print(f"{ts} - HudsonSeed Health Monitor RUNNING")
    if check_supabase_reachable(supabase):
        log_run(supabase, "OK", "Supabase reachable; heartbeat logged")
        post_slack("✅ HudsonSeed Health Monitor: heartbeat OK")
        return 0
    else:
        log_run(supabase, "DEGRADED", "Supabase select failed")
        post_slack("⚠️ HudsonSeed Health Monitor: Supabase unreachable")
        return 1

def main():
    fail_fast_if_missing_env()
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    if not LOOP_MODE:
        # Single run (GitHub Actions cron)
        sys.exit(one_run(supabase))

    # Loop mode (Railway long-running)
    print(f"Loop mode ON, interval={LOOP_INTERVAL_SEC}s")
    while True:
        try:
            one_run(supabase)
        except Exception as e:
            print(f"ERROR in run loop: {e}", file=sys.stderr)
            try:
                log_run(supabase, "ERROR", str(e)[:500])
            except Exception:
                pass
        time.sleep(LOOP_INTERVAL_SEC)

if __name__ == "__main__":
    main()
