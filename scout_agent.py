# hudsonseed_pm/scout_agent.py

import os
import sys
from datetime import datetime
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
LOOP_MODE = os.getenv("LOOP_MODE", "false").lower() == "true"
LOOP_INTERVAL_SEC = int(os.getenv("LOOP_INTERVAL_SEC", "3600"))

if not SUPABASE_URL or not SUPABASE_KEY:
    print("ERROR: Missing Supabase env vars")
    sys.exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Expanded real JCPS schools
REAL_SCHOOLS = [
    {"school_name": "Frank R. Conwell School - PS 3", "address": "111 Bright Street, Jersey City, NJ 07302", "phone": "201-915-6100", "type": "Elementary", "district": "Jersey City Public Schools"},
    {"school_name": "Jotham W. Wakeman School - PS 6", "address": "100 St. Pauls Ave, Jersey City, NJ 07306", "phone": "201-915-6110", "type": "Elementary", "district": "Jersey City Public Schools"},
    # Add 10+ more real schools here for volume
    {"school_name": "Liberty High School", "address": "Jersey City, NJ", "phone": "", "type": "High", "district": "Jersey City Public Schools"},
]

def scout_and_insert():
    inserted = 0
    for school in REAL_SCHOOLS:
        existing = supabase.table("leads").select("id").eq("school_name", school["school_name"]).execute()
        if existing.data:
            print(f"✓ Exists: {school['school_name']}")
            continue
        data = {
            "school_name": school["school_name"],
            "address": school.get("address"),
            "phone": school.get("phone"),
            "contact_name": "Principal",
            "status": "new",
            "source": "scout_agent",
            "district": school.get("district"),
            "school_type": school.get("type"),
            "last_scouted": datetime.now().isoformat()
        }
        supabase.table("leads").insert(data).execute()
        inserted += 1
        print(f"✅ Inserted: {school['school_name']}")
    print(f"[{datetime.now()}] Scout cycle: {inserted} new schools")
    return inserted

if __name__ == "__main__":
    print("=== HudsonSeed Scout Agent Started ===")
    scout_and_insert()
    if LOOP_MODE:
        while True:
            scout_and_insert()
            time.sleep(LOOP_INTERVAL_SEC)