# Sprint Plan

**Project:** Longevity Intelligence Platform
**Date:** 2026-03-23
**Target:** POC complete by late April 2026

---

## Sprint Overview

| Sprint | Goal | Dependencies | Deliverables | Target dates |
|---|---|---|---|---|
| Sprint 1 | Foundation — auth, onboarding, user profile | None | Working app shell, auth, profile stored in Supabase | Week of 2026-03-23 |
| Sprint 2 | Data Integration — Garmin, Apple Health, Weather, AQI | Sprint 1 | All external data auto-pulled and stored | Week of 2026-03-30 |
| Sprint 3 | Training Intelligence — evening suggestion loop | Sprint 2 | Contextual training suggestion end-to-end | Week of 2026-04-06 |
| Sprint 4 | Nutrition Intelligence — photo logging + insight | Sprint 2 | Photo snap → log → insight working end-to-end | Week of 2026-04-13 |
| Sprint 5 | Longevity Score — weekly sub-scores + digest | Sprint 3 + 4 | Weekly score, trend view, insight digest | Post-POC |

---

## Sprint Detail

### Sprint 1 — Foundation
**Dependencies:** None
**Goal:** Working app shell with auth, onboarding, and persistent user profile in Supabase.

**User stories:**
- [ ] US-01: Sign up / login with email + password
- [ ] US-02: Connect Garmin via OAuth
- [ ] US-03: Connect Apple Health via HealthKit
- [ ] US-04: Health profile form (age, sex, weight, height, family history)
- [ ] US-05: Goal setting (performance + longevity)
- [ ] US-06: Longevity baseline indicators log (grip, sit-to-stand, VO2max)

**Quality gates:**
- [ ] No secrets in code — all API keys in env vars
- [ ] Supabase auth working with RLS policies on user data
- [ ] User profile persists across sessions
- [ ] Garmin OAuth token stored securely (not in client)
- [ ] Apple HealthKit permissions scoped to minimum required
- [ ] Basic error states handled (failed auth, failed connection)

---

### Sprint 2 — Data Integration
**Dependencies:** Sprint 1 complete

**User stories:**
- [ ] US-07: Daily HRV, sleep, body battery pull from Garmin
- [ ] US-08: Training load pull from Garmin (last 7 days)
- [ ] US-09: Tomorrow's weather fetch (Open-Meteo, user location)
- [ ] US-10: AQI fetch for user location (OpenAQ)

**Quality gates:**
- [ ] Data normalised and stored in Supabase with timestamps
- [ ] Failed API calls handled gracefully — stale data flagged, not hidden
- [ ] Location permission scoped correctly on device
- [ ] No raw API responses stored — only processed, structured data
- [ ] All pulls tested with real Garmin and Apple Watch data

---

### Sprint 3 — Training Intelligence
**Dependencies:** Sprint 2 complete

**User stories:**
- [ ] US-11: Evening training suggestion generated automatically
- [ ] US-12: Reasoning displayed (HRV, load, weather, AQI, goal)
- [ ] US-13: User can tweak suggestion before confirming
- [ ] US-14: Confirmed workout saved to Supabase training log

**Quality gates:**
- [ ] Claude prompt tested across at least 5 different data scenarios
- [ ] Suggestion never uses medical language or prescriptive framing
- [ ] Fallback shown if data is incomplete (e.g. Garmin sync failed)
- [ ] Response time under 5 seconds for suggestion generation
- [ ] User confirmation required — no auto-save without explicit action

---

### Sprint 4 — Nutrition Intelligence
**Dependencies:** Sprint 2 complete (can run parallel to Sprint 3)

**User stories:**
- [ ] US-15: Photo snap → food item recognition via vision model
- [ ] US-16: Review + correct recognised items before logging
- [ ] US-17: Glycemic spike risk + inflammation flag displayed per meal
- [ ] US-18: Nudge surfaced if meal affects next day training/recovery

**Quality gates:**
- [ ] Vision model tested across at least 10 diverse meal photos
- [ ] User correction flow works before any data is committed
- [ ] Insight never uses medical language — science framing only
- [ ] Fallback to manual search if photo recognition fails
- [ ] Meal data stored in Supabase with timestamp and user confirmation flag

---

### Sprint 5 — Longevity Score (Post-POC)
**Dependencies:** Sprint 3 + Sprint 4 complete

**User stories:**
- [ ] US-19: Weekly sub-scores (fitness, nutrition, recovery, environment)
- [ ] US-20: Overall longevity score with week-over-week trend
- [ ] US-21: Weekly insight digest

**Quality gates:**
- [ ] Score calculation logic documented and testable
- [ ] Score framed as personal progress mirror — not medical metric
- [ ] Trend requires minimum 2 weeks of data before displaying
- [ ] Insight digest reviewed for tone — no prescriptive language
