# AI Spec — Sprint 1: Foundation & Onboarding

**Project:** Longevity Intelligence Platform
**Feature / Sprint:** Sprint 1 — Foundation
**Date:** 2026-03-23
**Author:** Mirko Radeka
**Status:** Approved

> This document is the brief for Claude Code.
> Be specific. Ambiguity here = bugs later.

---

## Context

The platform has no intelligence value without a persistent user profile. Sprint 1 creates the foundation everything else builds on: auth, wearable connections, and a complete onboarding flow that captures the user's health profile, goals, and longevity baseline. Without this, no downstream agent can personalise its output.

Linked to: `phase1-problem-statement.md` — the core pain is context loss across sessions. This sprint eliminates that permanently.

---

## Scope

**In:**
- Supabase project setup (auth, database schema, RLS policies)
- React Native (Expo) app shell with navigation structure
- Email + password auth (sign up, login, logout)
- Garmin Health API OAuth connection flow
- Apple HealthKit permission request and basic read test
- Onboarding flow (5 screens max):
  1. Personal profile (age, sex, weight, height)
  2. Family history (cardiovascular, metabolic, cancer — multi-select)
  3. Goals (performance goal + longevity intent)
  4. Wearable connections (Garmin, Apple Health)
  5. Longevity baseline indicators (grip strength, sit-to-stand, VO2max — all optional)
- All data persisted to Supabase on completion
- Onboarding skippable after wearable connection — baseline indicators can be completed later

**Out:**
- Any data pulling or sync (Sprint 2)
- Any AI suggestion or insight (Sprint 3+)
- Social features
- Android support
- Password reset flow (post-POC)

---

## Inputs & Outputs

| # | Input | Type | Source | Required? |
|---|---|---|---|---|
| 1 | Email + password | string | User | Yes |
| 2 | Age, sex, weight, height | number / enum | User | Yes |
| 3 | Family history flags | array of enums | User | No |
| 4 | Performance goal | string | User | Yes |
| 5 | Longevity intent (free text or preset) | string | User | Yes |
| 6 | Garmin OAuth token | OAuth token | Garmin API | Yes (can skip for Apple-only) |
| 7 | Apple HealthKit permission grant | boolean | Device OS | Yes (can skip for Garmin-only) |
| 8 | Baseline indicators (grip, sit-to-stand, VO2max) | number | User | No |

| # | Output | Type | Destination | Notes |
|---|---|---|---|---|
| 1 | User auth record | JWT + UUID | Supabase Auth | Row created on signup |
| 2 | User profile record | object | `user_profiles` table | Full profile persisted |
| 3 | User goals record | object | `user_goals` table | Goal + intent stored |
| 4 | Wearable connection records | object | `wearable_connections` table | Tokens stored server-side only |
| 5 | Baseline indicators record | object | `longevity_baselines` table | Nullable fields — optional at setup |

---

## Database Schema (Sprint 1)

```sql
-- user_profiles
id uuid references auth.users primary key
age integer
sex text
weight_kg decimal
height_cm decimal
family_history text[] -- ['cardiovascular', 'metabolic', 'cancer']
created_at timestamptz default now()

-- user_goals
id uuid primary key
user_id uuid references user_profiles
performance_goal text -- e.g. "Run HM sub 1:50"
longevity_intent text -- e.g. "Live healthier longer"
created_at timestamptz default now()

-- wearable_connections
id uuid primary key
user_id uuid references user_profiles
provider text -- 'garmin' | 'apple_health'
access_token text -- encrypted, server-side only
refresh_token text -- encrypted, server-side only
connected_at timestamptz default now()

-- longevity_baselines
id uuid primary key
user_id uuid references user_profiles
grip_strength_kg decimal nullable
sit_to_stand_score integer nullable -- number of stands in 30s
vo2max decimal nullable
resting_hr integer nullable
tested_at date
created_at timestamptz default now()
```

---

## Acceptance Criteria

- [ ] Given a new user, when they sign up with email + password, then a Supabase auth record is created and they are redirected to onboarding
- [ ] Given an onboarding user, when they complete all required fields and submit, then all data is persisted to Supabase and they land on the home screen
- [ ] Given an onboarding user, when they skip baseline indicators, then onboarding completes without error and indicators remain null
- [ ] Given a user connecting Garmin, when OAuth completes successfully, then the access token is stored server-side only and never appears in client storage or logs
- [ ] Given a returning user, when they open the app, then they are taken directly to home screen without repeating onboarding
- [ ] Given a failed Garmin OAuth, when the error occurs, then the user sees a clear error message and can retry or skip
- [ ] Given any user table, when accessed, then Supabase RLS policies ensure users can only read and write their own rows

---

## Agent / Skill Dependencies

| Agent / Skill | Role in this feature | Input it provides | Output it needs |
|---|---|---|---|
| memory-agent | Not yet active — builds on Sprint 1 output | — | Completed user profile + goals from Supabase |

---

## Prompt Architecture

No AI prompts in Sprint 1. This sprint is pure data and auth infrastructure.

---

## Constraints & Rules

- **Security:** Garmin and Apple OAuth tokens MUST be stored server-side only. Never in AsyncStorage, SecureStore client-side, or any log.
- **Data handling:** All user tables must have RLS enabled before Sprint 1 ships. PII (age, weight, family history) must never appear in application logs.
- **Performance:** Onboarding flow must complete end-to-end in under 5 minutes for a motivated user.
- **Error handling:** Every API call (Supabase, Garmin OAuth) must have an explicit error state shown to the user — no silent failures.
- **Fallback:** If Garmin OAuth fails, user can proceed with Apple Health only (and vice versa). At least one wearable connection is encouraged but not gated.

---

## Test Cases

| # | Scenario | Input | Expected output | Type |
|---|---|---|---|---|
| T1 | Happy path — full onboarding | All fields completed, Garmin connected | Profile in DB, redirected to home | Functional |
| T2 | Skip baseline indicators | Required fields complete, baseline skipped | Profile saved, null baseline fields, no error | Edge |
| T3 | Garmin OAuth failure | OAuth returns error | Error message shown, retry option available, can proceed with Apple only | Negative |
| T4 | Returning user opens app | Valid session exists | Bypasses onboarding, lands on home | Functional |
| T5 | RLS policy test | Attempt to read another user's profile via Supabase client | 403 / empty result returned | Security |
| T6 | Duplicate signup | Email already registered | Clear error: "account already exists" | Negative |

---

## Open Questions

- [ ] Does Garmin Health API developer access require approval before we can test OAuth in Sprint 1? (See A1 in assumptions log — validate immediately)
- [ ] Should Apple HealthKit request all permissions at onboarding or incrementally per feature? (Recommendation: incrementally — less intimidating)
- [ ] What encryption does Supabase apply to stored OAuth tokens — is column-level encryption needed?

---

## Notes for Claude Code

- Use Expo SDK 51+ for React Native — do not eject from managed workflow unless HealthKit forces it
- Supabase client should be initialised once at app root and accessed via context — not re-initialised per screen
- All Supabase writes use service role key server-side (via Supabase Edge Functions) — client uses anon key with RLS only
- Garmin OAuth redirect URI must match exactly what is registered in the Garmin developer portal
- Family history is stored as a text array — use Postgres array operators for future queries
- Baseline indicators table should support multiple rows per user (for periodic re-tests) — use `tested_at` date as the differentiator
