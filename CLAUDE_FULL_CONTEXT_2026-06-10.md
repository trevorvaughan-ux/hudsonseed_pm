# CLAUDE FULL SESSION CONTEXT — June 10, 2026
# This is not a status file. This is a brain transfer.
# A new Claude reads this and operates at the level of the session that wrote it.
# Written by Claude Sonnet 4.6 after a full working session with Trevor Vaughan.

---

## WHO YOU ARE WORKING WITH

Trevor Vaughan. 52. Union City NJ. Sober since 8/6/13 — that date matters, it's his foundational pivot. Former Wall Street energy broker (~20 years), now founder of HudsonSeed. 500HR ERYT+RCYT. Works out 4x/week (bench 245, curl 70lb). Practices yoga 4x/week including Iyengar at Yogamaya. Dog named Poochie.

**How Trevor operates:**
- Direct. No fluff. Hates Groundhog Day resets more than anything.
- OSAAT: One Step At A Time. Don't jump ahead of him.
- Externalization Rule: if it's not written down it doesn't exist.
- GitHub-First Rule: search for prior art before every build.
- He owns business decisions. You own technical decisions.
- When he says "fix it" — fix it. Don't ask 4 clarifying questions.
- He will tell you if you're wrong. Trust that.
- Humor is fine. Sarcasm is fine. But stay operational during work mode.
- He hates em-dashes. They're banned. "AI slop / the burning bush" is his phrase for it.

**Trevor's AI division of labor (LOCKED):**
- Claude = building + execution
- Grok = thinking + research
- Do NOT overlap. Do NOT suggest "maybe ask Grok about this."

---

## THE MISSION

**HudsonSeed** — K-12 yoga and mindfulness. S-Corp. trevorvaughan@hudsonseed.com.
- Goal: reach 1 million kids
- Revenue goal: $1,000/day by Q4 2026
- Current phase: school outreach via Pitch Machine → land first paying contracts

**The product pitch (memorize this, it's the voice):**
"This is a 100% asynchronous, on-demand tool built to save teacher sanity, not take up their time. If a teacher has a chaotic transition after recess, they don't have to prep a lesson or schedule a session — they just pull up Hanuman on the whiteboard, press play, and let the asynchronous coach guide the classroom for 2 minutes while the teacher catches their breath."

**Pull quotes (for tight spaces):**
- "Press play. Catch your breath."
- "Built to save teacher sanity, not take up their time."
- "100% asynchronous, on-demand. No prep, no schedule."
- "A 2-minute reset, whenever the moment calls for it."

**Hanuman** = AI yoga coach mascot. Wise smiling bear/monkey. Bottom-right floating bubble on website. This is the product's face.

**S.E.L.F. framework** = Self-awareness, Emotional Intelligence, Leadership, Flow. Trevor's core IP from prior company Mettāflow. It's in every pitch and every grant. Don't treat it as jargon — it's the backbone.

**Class Close ritual:** "I am happy. I am safe. I am brave. I am strong. I am love."

---

## THE PITCH MACHINE — FULL ARCHITECTURE

### What it is
Three-layer automated school outreach system. Runs on Google Apps Script bound to a Google Sheet. Targets JC (Jersey City) principals and NYC principals.

### Layer 1
Generates Gmail drafts from Google Sheet data. Each row = one school. Pulls principal name, email, school name, inserts into template. Verified working.

### Layer 2  
Reply detection + classification. Reads inbox, detects replies to outreach emails, classifies as COMMUNITY or NOT (binary — no PRIORITY, no WARM, those tiers were removed). Verified live.

### Layer 3
Auto-send materials within 5 minutes of a principal reply classified as COMMUNITY. This is NOT draft — this is auto-send. Verified live.

### The trigger
`machineTick` — fires every 5 minutes. Clean completions confirmed. This is the heartbeat of the whole system.

### Master sheet
`LAYER2_JC_BETA_1.1_MASTER` — this is the runtime source of truth. Google Sheets ID in Drive.

### ARCHITECTURE RULES — LOCKED, DO NOT CHANGE
1. Google Sheets = sole source of truth for runtime reads
2. Supabase = write-only, new data pushes only (never read from in runtime)
3. Classification = binary: COMMUNITY or NOT. No other tiers.
4. NYC outreach = warm pre-seed framing ONLY. Never claim vendor 9615 in email body.
5. Pixel ban = ABSOLUTE. Engagement measured by replies only. 9-to-1 scale. Update only on actual responses, never speculative.
6. From address = trevorvaughan@hudsonseed.com always. Never role addresses (outreach@, schools@). Principals delete those.
7. Em-dashes = banned from all copy.
8. Trevor sends manually every ~10 minutes. Layer 3 auto-sends on reply only.

### Why these rules exist (so you don't accidentally break them)
- Sheets-as-truth: avoids multi-AI version drift. Claude, Grok, Gemini were all hitting different versions of code simultaneously — this was the fix.
- Binary classification: PRIORITY/WARM tiers caused ambiguity and stalls. Removed June 2026.
- Pixel ban: Trevor's rule about authentic engagement signals only. No vanity metrics.
- Role addresses: principals at JCBOE actually delete emails from non-human addresses. Verified from experience.

---

## CURRENT DRAFT STATUS

- 23 real JCBOE principal drafts in Gmail Drafts
- ~6 have "Dear Principal TBD" — these need real names before Trevor sends them
- Trevor reviews and sends manually, ~10 min cadence
- NYC District 1 + District 2 drafts staged using predicted `@schools.nyc.gov` format
- Brooklyn pre-seed: Success Academy Williamsburg, Uncommon Williamsburg Collegiate, PS 110

**Next action on drafts:** Pull real names for the 6 TBD drafts. Names come from the Master Sheet or public school directories.

---

## WARM LEADS — ACTIVE

### Valerie Roper (HIGHEST PRIORITY)
- Title: Community School Director, Center for Supportive Schools (CSS)
- Why she matters: CSS manages 9 JC community schools. Finding vendor partners is LITERALLY her job description. This is not a cold call — Janeen Maniscalco (Principal, PS34) referred her.
- Status: Draft ready. NOT sent yet.
- The play: CSS as entry point = multi-school deal, not one-off. Don't pitch her like a principal. Pitch her like a partner who controls a portfolio.
- Do NOT send without Trevor's explicit go-ahead.

### Janeen Maniscalco
- Principal, PS34 Barack Obama Community School
- The warm referral source. She's the reason Valerie is in play.
- Already engaged. Treat her as an ally, not a prospect.

### Judy Rose
- judyrose1988@gmail.com
- Sent Trevor a cold pitch about AI visibility / getting HudsonSeed surfaced in AI results
- Trevor replied 6/9/26: "No thanks, 95% of my business comes through referrals. My bottleneck is vendor codes. Unless you specifically have a list of vendor codes or relationships, there isn't much to talk about."
- CLOSED. Do not resurface this thread.

---

## INFRASTRUCTURE MAP

### What runs where
- **Pitch Machine**: Google Apps Script (bound to Master Sheet) — this is the LIVE system
- **Website**: Railway → `hudsonseed-website-production.up.railway.app` → pending custom domain `www.hudsonseed.com`
- **CRM**: Supabase project `pebhikfbpgntedvbxqph` — JC Schools data
- **Health Monitor**: MIGRATED from Railway/GitHub Actions → Google Apps Script (setup pending as of 6/10)

### Railway = WEBSITE ONLY
As of June 10, 2026, Railway is exclusively for the website. The Pitch Machine repo (`hudsonseed_pm`) has had all Railway config stripped. Do not try to deploy anything Pitch Machine related to Railway.

### GitHub repos
- `trevorvaughan-ux/hudsonseed_pm` — Pitch Machine agents (pitch_agent.py, scout_agent.py)
- `trevorvaughan-ux/hudsonseed-website` — website source
- `trevorvaughan-ux/hudsonseed-memory` — memory/context repo

### Supabase
- Project ID: `pebhikfbpgntedvbxqph`
- URL: `https://pebhikfbpgntedvbxqph.supabase.co`
- Key table: `agent_runs` (heartbeat logs, health monitor writes here)
- New key as of 6/10: `[SUPABASE_SERVICE_ROLE_KEY — get from Trevor vault doc]`

### Website status
- Live at Railway URL
- Custom domain `www.hudsonseed.com` via GoDaddy — DNS connection pending (was blocked by 2FA/phone issue)
- Design: "Science of Calm" — cream `#FDF8F0` + teal `#4A9EA6`, Playfair Display + DM Sans
- Hero video from Gemini needs re-encode: `ffmpeg -i in.mp4 -c:v libx264 -pix_fmt yuv420p -profile:v main -movflags +faststart -c:a aac out.mp4`
- Mobile responsiveness = hard requirement. Principals view on phones.

---

## WHAT GOT DONE TODAY (June 10, 2026)

### Email auth — ALL GREEN ✅
- DMARC confirmed live in DNS: `v=DMARC1; p=none; rua=mailto:trevorvaughan@hudsonseed.com`
- Verified via dns.google API. GoDaddy UI was misleading — record existed from prior attempt, conflict error proved it.
- SPF ✅ DKIM ✅ DMARC ✅ — Trevor is CLEAR TO SEND

### Infrastructure cleanup
- GitHub Actions health monitor cron removed (was firing 6x/day, missing secrets = failure email every run)
- Railway config (`railway.toml`, `railway.json`) deleted from `hudsonseed_pm`
- `health_monitor.py` deleted from `hudsonseed_pm`
- `.github/workflows/` deleted from `hudsonseed_pm`
- All pushed to main, commit `d69bb0f`

### Health monitor migration
- Rewrote as Google Apps Script (`HudsonSeed_HealthMonitor.gs`)
- Uses `UrlFetchApp` to hit Supabase REST API directly
- Silent on success. Emails Trevor ONLY on failure. No more noise.
- Setup not done yet — Trevor needs to paste into script.google.com, add two Script Properties, run `createTrigger()` once, run `testRun()` once.
- Script properties needed: `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY`

### Judy Rose thread
- Trevor already handled it. Closed cleanly 6/9. Do not reopen.

---

## KEY DRIVE FILE IDs
- Master Outreach Directory: `12lfZvSLec1EXwal2Rs9f5kF0n5SYhs3KYcRJVIlqbzc`
- JC Schools Full Schema Jun1 2026: `14cS76UUfsKLBn_lQoJ2Sn4WweB0HhjaCFj5sNL1s1UQ`
- Mission Control: `1Kq0wChkZE0yA5M_MAmOHb_aqnHTyWN81a8WK7OVxadA`
- HudsonSeed-Ops folder: `12bzlIftqV4rQTDM6esm_KnxWZJ2ux5Ky`

---

## TREVOR'S OPERATING FRAMEWORK (use these to think like him)
- **OSAAT**: One Step At A Time. Don't skip steps, don't build ahead of the current bucket.
- **Externalization Rule**: If it's in Trevor's head it doesn't exist. Everything gets written down.
- **GitHub-First Rule**: Search for prior art in repos before building anything new.
- **Karpathy CLAUDE.md four rules**: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution.
- **Bucket system**: B1=Outreach Engine (CURRENT), B2=Revenue Tracker, B3=Teacher Recruitment, B4=YogaRenew Sales, B5=Grant Engine, B6=NJ Conference+TEDx, B7=Flett Automation, B8=Finance+Tax, B9=Health+Sleep+Fitness. Complete one fully before next.
- **Truth standard**: BUILT = committed to GitHub. DEPLOYED = running + executable. VERIFIED = actually returning real data. Never say "done" until all three.

---

## WHAT TREVOR DOES NOT WANT
- Long preambles before doing the thing
- "Great question!" or any sycophantic opener
- Asking him to copy-paste, click UIs, or relay information
- Stubs, templates, or example code — real executable code only
- Saying "done" before it's verified
- Offering to help when you should just be helping
- Groundhog Day resets ("as I mentioned earlier...")
- Bullet points for emotional/sensitive responses
- Multiple questions in one response — pick the most important one

---

## HOW TO WAKE UP IN A NEW SESSION

1. Trevor will paste a short prompt + possibly upload his credentials vault doc
2. Clone `hudsonseed_pm`: `git clone https://trevorvaughan-ux:PAT@github.com/trevorvaughan-ux/hudsonseed_pm.git`
3. Read this file
4. State what you know, what's next, ask ONE question if needed
5. Get to work

**The one-liner Trevor uses to wake you:**
"WAKE UP CLAUDE. Load CLAUDE_FULL_CONTEXT_2026-06-10.md from hudsonseed_pm. Resume Pitch Machine work. Credentials in vault doc."

---

## IMMEDIATE NEXT ACTIONS (when you resume)

1. Fix the 6 "Dear Principal TBD" drafts — pull real names from Master Sheet or NJDOE directory
2. Send Valerie Roper draft — Trevor approves first, then send
3. Trevor sets up Apps Script health monitor (5 min, he does steps 1-3)
4. Continue clearing draft queue — Trevor sends manually, you support with names/content fixes
5. www.hudsonseed.com custom domain — still pending GoDaddy DNS + 2FA resolution

