# CLAUDE STATUS — June 10, 2026
> Load this first in any new session. This is the source of truth.

---

## WAKE-UP INSTRUCTION
"Read CLAUDE_STATUS_2026-06-10.md from hudsonseed_pm repo and resume."

---

## WHERE WE ARE — PITCH MACHINE

### VERIFIED WORKING ✅
- Layer 1: Gmail draft generation from Google Sheet — LIVE
- Layer 2: Reply detection + classification (COMMUNITY / NOT) — LIVE
- Layer 3: Auto-send materials within 5 min of principal reply — LIVE
- `machineTick` trigger fires every 5 minutes, clean completions
- Master sheet: `LAYER2_JC_BETA_1.1_MASTER`
- Bound to Apps Script in Google Sheets

### DRAFTS STATUS
- 23 real JCBOE principal drafts staged in Gmail Drafts
- ~6 have "Dear Principal TBD" — need real names before sending
- Trevor sends manually every ~10 minutes (his rule)
- NYC District 1 + District 2 drafts staged (`@schools.nyc.gov` format)
- Brooklyn pre-seed: Success Academy Williamsburg, Uncommon Williamsburg Collegiate, PS 110

### ARCHITECTURE RULES (LOCKED — DO NOT CHANGE)
- Google Sheets = sole source of truth (runtime reads)
- Supabase `pebhikfbpgntedvbxqph` = write-only for new data pushes only
- Classification: binary COMMUNITY or NOT (no PRIORITY/WARM tiers)
- NYC outreach: warm pre-seed framing only — NO vendor 9615 claim
- Pixel ban: ABSOLUTE — engagement measured by replies only
- From address: `trevorvaughan@hudsonseed.com` (human name, never role address)
- Em-dashes: BANNED from all copy

### WARM LEADS
- **Janeen Maniscalco** (Principal, PS34 Barack Obama Community School) — warm referral in
- **Valerie Roper** (Community School Director, Center for Supportive Schools) — gatekeeper for 9 JC community schools, CSS finding vendor partners is literally her job. Draft ready, NOT sent yet.
- **Judy Rose** (judyrose1988@gmail.com) — AI visibility cold pitch, Trevor declined 6/9. CLOSED.

---

## TODAY'S COMPLETED WORK — June 10, 2026

### Email Auth (hudsonseed.com) — ALL GREEN ✅
- SPF ✅ (was already live)
- DKIM ✅ (was already live)  
- DMARC ✅ CONFIRMED LIVE — `v=DMARC1; p=none; rua=mailto:trevorvaughan@hudsonseed.com`
  - Verified via dns.google, TTL 3600, resolving from GoDaddy
  - GoDaddy UI showed "conflict" = record already existed from prior attempt
- **ALL THREE GREEN → CLEAR TO SEND**

### Infrastructure Cleanup
- GitHub Actions health monitor cron DISABLED (was spamming 6x/day — missing secrets)
- Railway config files deleted from `hudsonseed_pm` repo (`railway.toml`, `railway.json`)
- `health_monitor.py` deleted from `hudsonseed_pm` repo
- `.github/workflows/` deleted from `hudsonseed_pm` repo
- Railway is now **website-only** (`hudsonseed-website` repo → Railway → www.hudsonseed.com)

### Health Monitor → Migrated to Google Apps Script
- File: `HudsonSeed_HealthMonitor.gs` (in outputs)
- Hits Supabase every 4 hours via `UrlFetchApp`
- SILENT on success, emails only on failure
- **SETUP NOT YET DONE** — Trevor needs to:
  1. script.google.com → New project → paste the .gs file
  2. Script Properties: `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY`
  3. Run `createTrigger()` once
  4. Run `testRun()` once to verify

---

## WHAT'S NEXT (in order)

1. **Fix the 6 "Dear Principal TBD" drafts** — pull real names, update before sending
2. **Send Valerie Roper draft** — highest leverage lead, CSS = 9 JC schools
3. **Apps Script health monitor setup** (5 min task, Trevor does it)
4. **Judy Rose email** — already handled/closed
5. **Continue manual sends** — Trevor ~10min cadence

---

## REPO MAP
- `hudsonseed_pm` (github.com/trevorvaughan-ux/hudsonseed_pm) — Pitch Machine agents
- `hudsonseed-website` — live at Railway → hudsonseed-website-production.up.railway.app
- `hudsonseed-memory` — memory repo

## KEY IDs
- Supabase project: `pebhikfbpgntedvbxqph`
- Supabase URL: `https://pebhikfbpgntedvbxqph.supabase.co`
- Railway project: `2fb7c7dc-efbd-445c-8974-4afe05d47e0e`
- Master Sheet: `LAYER2_JC_BETA_1.1_MASTER`
- Drive Mission Control: `1Kq0wChkZE0yA5M_MAmOHb_aqnHTyWN81a8WK7OVxadA`

## CREDENTIALS (in vault doc Trevor uploads)
- GitHub PAT, Railway token, Supabase keys, SMTP — all in daily vault upload

---

## CONTEXT PROMPT FOR NEW SESSION

```
WAKE UP CLAUDE. Load context from hudsonseed_pm repo: CLAUDE_STATUS_2026-06-10.md

You are working with Trevor Vaughan on HudsonSeed (K-12 yoga/mindfulness, $1K/day Q4 2026 goal).
Primary mission right now: Pitch Machine fully autonomous — 23 JCBOE drafts staged, ~6 need real principal names before sending. Warm lead Valerie Roper (CSS, 9 JC schools) draft ready to send.

Email auth ALL GREEN as of June 10 (SPF/DKIM/DMARC verified). Clear to send.
Railway = website only. Pitch Machine runs on Apps Script + Google Sheets + Supabase.
Health monitor migrated to Apps Script (setup pending).

Clone hudsonseed_pm with PAT from vault. Read the status file. Resume.
```
