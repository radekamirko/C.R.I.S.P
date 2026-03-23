# Longevity Intelligence Platform

> Copy this file to the root of the project repository before starting any build session.
> This is the single source of truth Claude reads at the start of every session.

---

## What this project is

A B2C longevity intelligence platform that curates and surfaces the latest scientifically backed data on quality of life and lifespan — personalised to the user's biometric data from Garmin and Apple Watch — with persistent long-term memory. The user is always in the driver's seat.

## Why it exists

Health-conscious people in their late 30s+ are spending 15+ minutes daily fragmented across 4-5 apps (Garmin, Strava, ChatGPT, AirQI, LoseIt), re-entering context every session, getting training and nutrition insights with no environmental awareness and no memory of what came before. No single tool connects personal biometric data to longevity science with long-term memory.

## Desired outcome

1. A user completes their daily training + nutrition loop in under 2 minutes with zero manual context re-entry
2. Training suggestions feel contextually aware — they reflect HRV, training load, weather, and air quality without prompting
3. Food logging is faster and more insightful than LoseIt — photo snap works, inflammation and glycemic signal is present

## Constraints

- **Budget:** Bootstrapped — minimise spend, use free tiers wherever possible
- **Timeline:** POC target late April 2026 — 4 sprints of 1 week each
- **Legal/Compliance:** US market first. Not a HIPAA covered entity. "We show data, you decide" framing — no health claims, no prescriptive advice. FTC rules apply.
- **Technical:** Solo builder (Mirko + Claude Code). Expo managed workflow preferred — do not eject unless absolutely necessary.

## What we are building

An iOS mobile app (React Native / Expo) with:
- Onboarding: health profile, goals, wearable connections, longevity baseline
- Daily training loop: evening contextual workout suggestion (auto-pulled data, no manual entry)
- Daily nutrition loop: photo-snap meal logging with glycemic + inflammation insight
- Weekly longevity score: 4 sub-scores (fitness, nutrition, recovery, environment) + trend digest

## What we are NOT building

- Garmin workout export / write-back (Phase 2)
- Android support (Phase 2)
- Social or community features
- Clinical integrations or medical records
- Prescriptive health advice — ever
- Password reset (post-POC)
- Web app

## Tech stack

| Layer | Choice |
|---|---|
| Mobile | React Native (Expo SDK 51+) |
| Backend / DB | Supabase (Postgres + Auth + Storage) |
| LLM | Claude API — claude-sonnet-4-6 |
| Food recognition | Claude vision or GPT-4o vision |
| Memory | Supabase (structured) + Claude long context |
| Garmin data | Garmin Health API (OAuth 2.0) |
| Apple Health | Apple HealthKit (via Expo) |
| Weather | Open-Meteo (free, no key) |
| Air quality | OpenAQ API |
| Science layer | RAG via Supabase pgvector |

## Folder structure

```
/
├── app/                    # Expo Router screens
│   ├── (auth)/             # Login, signup
│   ├── (onboarding)/       # 5-step onboarding flow
│   ├── (tabs)/             # Main app: home, training, nutrition, profile
│   └── _layout.tsx
├── components/             # Shared UI components
├── lib/
│   ├── supabase.ts         # Supabase client (singleton)
│   ├── claude.ts           # Claude API client
│   └── agents/             # Agent logic (one file per agent)
│       ├── data-sync.ts
│       ├── training.ts
│       ├── nutrition.ts
│       ├── science-layer.ts
│       └── memory.ts
├── skills/                 # SKILL.md per agent
├── supabase/
│   ├── migrations/         # SQL migrations
│   └── functions/          # Edge Functions (server-side API calls)
├── assets/
├── CLAUDE.md               # This file
└── .env.local              # Never committed — API keys live here
```

## Agents / Skills in this project

| Agent | Responsibility | Location |
|---|---|---|
| data-sync-agent | Daily pull from Garmin, Apple Health, weather, AQI | `skills/data-sync-agent/SKILL.md` |
| training-agent | Evening training suggestion with full context | `skills/training-agent/SKILL.md` |
| nutrition-agent | Photo food recognition + glycemic/inflammation insight | `skills/nutrition-agent/SKILL.md` |
| science-layer-agent | RAG retrieval over longevity science knowledge base | `skills/science-layer-agent/SKILL.md` |
| memory-agent | Persistent user context object for all Claude calls | `skills/memory-agent/SKILL.md` |
| scoring-agent | Weekly sub-scores + longevity trend (Sprint 5) | `skills/scoring-agent/SKILL.md` |

## Human-in-the-loop zones

- Training suggestion: NEVER auto-saved — user must explicitly confirm before any workout is stored
- Food photo recognition: NEVER auto-committed — user reviews and corrects before logging
- Goal updates: NEVER changed by Claude — user edits only via profile settings
- Baseline indicators: NEVER inferred — manual user entry only

## Security rules

- Never log or expose PII (age, weight, family history, location, health data)
- Never commit secrets, API keys, or OAuth tokens to version control
- All user tables have Supabase RLS enabled — users can only access their own rows
- Garmin and Apple OAuth tokens stored server-side only (Supabase Edge Functions) — never in client storage
- All Claude API calls use anonymised context — no raw PII in prompts
- HTTPS everywhere — no HTTP fallback

## Language and tone rules (non-negotiable)

- NEVER prescribe: not "you should", "you must", "avoid X"
- ALWAYS frame as science: "research suggests", "the data shows", "studies indicate"
- NEVER use medical language: not "symptoms", "diagnosis", "treatment", "condition"
- ALWAYS keep user in control: "here's what the science says — you decide"

## Current sprint

**Sprint:** 1 — Foundation
**Goal:** Auth, onboarding, user profile, wearable connections persisted to Supabase
**AI Spec:** `projects/longevity-platform/phase4-ai-spec-sprint1.md`

## Open questions

- [ ] Garmin Health API developer access — apply immediately and confirm approval timeline (Risk R1)
- [ ] Apple HealthKit permissions — incremental vs upfront at onboarding
- [ ] Supabase OAuth token encryption — confirm column-level encryption requirement
- [ ] Legal review of UI copy before public launch (not a POC blocker)
