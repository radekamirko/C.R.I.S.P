# Sprint Plan

**Project:** Znam Coveka
**Date:** 2026-03-24
**Goal:** Launch-ready MVP before autumn 2026 busy season

---

## Sprint Overview

| Sprint | Focus | Features | Gate |
|---|---|---|---|
| 1 | Foundation | Project setup, auth, DB schema, Docker, Railway deploy | Working auth + deployed shell |
| 2 | Tradie onboarding | Profile setup (URL auto-fill + manual), vetting queue, admin approval | Tradie can sign up and be approved |
| 3 | Job posting + matching | Homeowner posts job, AI matching engine, shortlist generation | Homeowner can post and receive shortlist |
| 4 | Tradie feed + selection | Tradie job feed, apply, homeowner selection, notifications | End-to-end job match flow working |
| 5 | Messaging + completion | In-platform messaging, job completion, reviews, rebook | Full job lifecycle complete |
| 6 | Polish + implicit signals | Preference learning loop, photos, availability updates, admin funnel, remaining notifications | All MVP features complete |
| 7 | Pre-launch | QA, performance, security review, privacy policy, seeding Belgrade tradies | Launch-ready |

Do not start Sprint N+1 before Sprint N is working end-to-end.

---

## Sprint 1: Foundation

**Goal:** Working auth, deployed infrastructure, DB schema ready for Sprint 2.

**Features:**
- Project scaffold: Next.js 14 App Router + TypeScript + Tailwind + Docker
- Railway EU deployment pipeline (CI/CD from Git)
- Supabase project setup (EU region)
- Auth: Google OAuth + Apple Sign-In (homeowner) + email (tradie) — Supabase Auth
- Role system: homeowner / tradie / admin roles in DB
- DB schema: users, tradies, jobs, matches, messages, reviews tables
- Basic navigation shells: homeowner tab bar + tradie tab bar + /admin route
- Row-level security (RLS) policies on all tables
- Environment variables wired and verified

**Quality gate:** Auth works (sign in, session persists, role-gated routes). App deploys to Railway EU. /admin route is admin-only.

**AI Spec:** `docs/ai-spec-sprint1.md`

---

## Sprint 2: Tradie Onboarding & Vetting

**Goal:** A tradie can sign up, submit a profile, and be approved by admin.

**Features:**
- Tradie profile setup flow (URL auto-fill via Claude API + manual fallback)
- Portfolio photo upload (mobile-first, Supabase Storage)
- Availability setup (day/time pattern)
- /pending holding screen (post-submission)
- Admin approval queue (/admin/approvals)
- AI pre-screen summary per tradie application (Claude API)
- Approve/reject action with optional rejection note
- Email notifications: profile received, approved, rejected (Resend)

**Quality gate:** Tradie signs up → submits profile → admin approves → tradie sees live status. URL auto-fill tested with 10 real Belgrade tradie URLs.

**AI Spec:** `docs/ai-spec-sprint2.md`
**Integration Specs needed:** `docs/ai-spec-claude-api.md`, `docs/ai-spec-supabase.md`, `docs/ai-spec-resend.md`

---

## Sprint 3: Job Posting + AI Matching

**Goal:** Homeowner posts a job and receives a shortlist with AI explanations.

**Features:**
- Job posting flow (3-step: what + where/when + preferences)
- Google Maps autocomplete for location (Belgrade)
- Budget range + urgency preferences
- Optional photo upload on job post (C5)
- AI matching engine: filter (trade + location + availability) → rank → select top 3
- Claude API: generate personalised explanation per matched tradie
- Shortlist displayed to homeowner (/jobs/[id])
- Matching in-progress screen (skeleton cards + reassuring copy)
- Email notification to homeowner when shortlist ready (K1)
- Email notification to matched tradies (K2)

**Quality gate:** Homeowner posts job → matching runs → shortlist with AI explanations appears within 60 seconds. Test with 5 real job descriptions against approved tradie profiles.

**AI Spec:** `docs/ai-spec-sprint3.md`
**Integration Specs needed:** `docs/ai-spec-google-maps.md`

---

## Sprint 4: Tradie Feed + Selection + Notifications

**Goal:** Full push/pull matching flow. Homeowner selects a tradie.

**Features:**
- Tradie job feed (/feed): matched jobs (top) + open jobs (below)
- Tradie applies to open job (E2)
- Tradie sees applied jobs marked in feed (E5)
- Homeowner sees tradie applications alongside AI shortlist
- Homeowner selects tradie (F1) — confirmation modal
- Selected tradie notified: email + in-app (F2, K3)
- Non-selected tradies notified (F3)
- Homeowner email when tradie applies (K4)
- Homeowner confirmation screen post-selection (F4)

**Quality gate:** Full flow from job post → tradie applies → homeowner selects → all parties notified. End-to-end tested with real accounts.

**AI Spec:** `docs/ai-spec-sprint4.md`

---

## Sprint 5: Messaging + Job Completion + Reviews

**Goal:** Full job lifecycle — from selection to completion to review.

**Features:**
- In-platform messaging (Supabase Realtime) — homeowner ↔ tradie per job (G1)
- Message history persisted per job (G3)
- Email notification on new message (K5, G2)
- Job completion: homeowner marks complete (H1)
- Star rating + optional review (H2)
- Review appears on tradie profile immediately (H3)
- Rebook same tradie CTA post-completion (H4)
- Tradie updates availability (B6)
- Tradie updates portfolio photos post-approval (B7)

**Quality gate:** Full lifecycle tested end-to-end: select → message → complete → review → rebook.

**AI Spec:** `docs/ai-spec-sprint5.md`

---

## Sprint 6: Polish + Implicit Signals + Admin Funnel

**Goal:** All MVP features complete. Platform is measurable.

**Features:**
- Implicit signal recording: who selected, rating given, rebook indicator (D5/I1)
- Admin job funnel view: posted → matched → accepted → completed (J1 — final polish)
- Admin dispute resolution view with job history + message trail (J2 — final polish)
- Empty states on all screens (no blank screens)
- Error states on all flows (OAuth failure, no matches, API timeout)
- Loading states (skeleton screens on shortlist + feed)
- Mobile responsiveness audit across all screens
- Onboarding preference questions wired to matching engine

**Quality gate:** All MVP user stories pass manual QA. No blank screens. All empty/error states handled.

**AI Spec:** `docs/ai-spec-sprint6.md`

---

## Sprint 7: Pre-Launch

**Goal:** Launch-ready. Tradies seeded. Legal minimum met.

**Tasks:**
- Privacy policy drafted and linked (Mirko — legal)
- Terms of service drafted (Mirko — legal)
- Security review: RLS policies audited, secrets check, admin route hardened
- Performance: Lighthouse score > 80 on mobile
- Supabase EU region verified for ZZPL compliance
- Railway EU deployment latency tested from Belgrade
- Docker image optimised (multi-stage build)
- Seed 20+ Belgrade painters and plumbers (Mirko — manual outreach)
- Smoke test: full homeowner + tradie journey on production
- Monitoring: Supabase dashboard + Railway logs — reactive setup confirmed

**Quality gate:** 20+ approved tradies live. Full journey smoke-tested on production. Privacy policy live.

---

## Quality Gates (all sprints)

- No secrets in Git (verified before every commit)
- RLS policies tested — user can never access another user's data
- All environment variables present before deploy (fail loudly if missing)
- /admin route inaccessible to non-admin roles
- No Pages Router patterns — App Router only
- Claude API calls always have a fallback if the API is unavailable
