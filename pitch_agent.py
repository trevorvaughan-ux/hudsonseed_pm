import os
import sys
import time
import json
from datetime import datetime
from supabase import create_client, Client

# Env fail-fast
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
LOOP_MODE = os.getenv("LOOP_MODE", "false").lower() == "true"
LOOP_INTERVAL_SEC = int(os.getenv("LOOP_INTERVAL_SEC", "600"))

if not SUPABASE_URL or not SUPABASE_KEY:
    print("ERROR: Missing Supabase env vars")
    sys.exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_pending_schools():
    """Pull schools ready for pitch (status=new or retry)"""
    response = supabase.table("leads").select("*").eq("status", "new").limit(10).execute()
    return response.data

def generate_pitch(school):
    """Real pitch logic - expand later with LLM call if needed"""
    return {
        "subject": f"Yoga/Mindfulness for {school.get('school_name', 'Your School')} - HudsonSeed Pilot",
        "body": f"""Hi {school.get('contact_name', 'Admin')},

HudsonSeed brings daily 10-min yoga + mindfulness to K-12. 
Proven in Jersey City. Zero cost pilot for {school.get('school_name')}.

Next step: 15-min call?
""",
        "status": "generated"
    }

def run_pitch_cycle():
    schools = get_pending_schools()
    print(f"[{datetime.now()}] Processing {len(schools)} schools")
    
    for school in schools:
        pitch = generate_pitch(school)
        # Log to agent_runs + update lead
        supabase.table("agent_runs").insert({
            "service": "pitch_agent",
            "status": "SUCCESS",
            "details": json.dumps({"school_id": school.get("id"), "pitch": pitch})
        }).execute()
        
        supabase.table("leads").update({
            "status": "pitched",
            "last_pitched": datetime.now().isoformat()
        }).eq("id", school.get("id")).execute()
        
        print(f"  ✓ Pitched to {school.get('school_name')}")
    
    return len(schools)

if __name__ == "__main__":
    print("=== HudsonSeed Pitch Agent Level 2 Started ===")
    if LOOP_MODE:
        while True:
            try:
                run_pitch_cycle()
                time.sleep(LOOP_INTERVAL_SEC)
            except Exception as e:
                print(f"ERROR: {e}")
                time.sleep(60)
    else:
        run_pitch_cycle()
        print("Single run complete.")