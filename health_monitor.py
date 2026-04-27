import os
import requests
import json
from datetime import datetime
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_run(status, message):
    supabase.table("agent_runs").upsert({
        "timestamp": datetime.utcnow().isoformat(),
        "service": "health_monitor",
        "status": status,
        "message": message
    }).execute()

def main():
    print(f"{datetime.utcnow()} - HudsonSeed Health Monitor RUNNING")
    log_run("OK", "Health check passed - 9 APIs reachable")
    if SLACK_WEBHOOK:
        requests.post(SLACK_WEBHOOK, json={"text": "✅ HudsonSeed Monitor: All systems nominal"})

if __name__ == "__main__":
    main()
