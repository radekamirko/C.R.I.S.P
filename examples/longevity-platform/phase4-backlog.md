# Initial Backlog

**Project:** Longevity Intelligence Platform
**Date:** 2026-03-23
**Version:** v0.1

---

## Epics

| # | Epic | Description | Priority |
|---|---|---|---|
| E1 | Foundation | Auth, database, user profile, onboarding flow | High |
| E2 | Data Integration | Garmin API, Apple HealthKit, Weather, AQI auto-pull | High |
| E3 | Training Intelligence | Evening planning loop — contextual workout suggestion | High |
| E4 | Nutrition Intelligence | Photo logging, glycemic + inflammation insight | High |
| E5 | Longevity Score | Weekly sub-scores, trend insights, weekly digest | Medium |
| E6 | Baseline Check-ins | Monthly longevity indicator re-tests (grip, sit-to-stand, etc.) | Low |

---

## User Stories

### E1 — Foundation

| ID | As a... | I want to... | So that... | Priority | Sprint | Status |
|---|---|---|---|---|---|---|
| US-01 | New user | Sign up with email and password | I can access the platform securely | High | 1 | Backlog |
| US-02 | New user | Connect my Garmin account via OAuth | My wearable data syncs automatically | High | 1 | Backlog |
| US-03 | New user | Connect Apple Health | My iPhone health data syncs automatically | High | 1 | Backlog |
| US-04 | New user | Complete a health profile (age, sex, weight, height, family history) | The platform knows my context permanently | High | 1 | Backlog |
| US-05 | New user | Set my goals (sub 1:50 HM, longevity) | Every suggestion is goal-aware | High | 1 | Backlog |
| US-06 | New user | Log my longevity baseline indicators (grip strength, sit-to-stand, VO2max) | I have a starting point to measure progress against | Medium | 1 | Backlog |

### E2 — Data Integration

| ID | As a... | I want to... | So that... | Priority | Sprint | Status |
|---|---|---|---|---|---|---|
| US-07 | Returning user | Have my HRV, sleep, and body battery pulled automatically each day | I never have to screenshot or manually enter wearable data | High | 2 | Backlog |
| US-08 | Returning user | Have my training load pulled from Garmin automatically | The platform knows my weekly load without me saying anything | High | 2 | Backlog |
| US-09 | Returning user | Have tomorrow's weather fetched automatically based on my location | Suggestions account for conditions without me sharing manually | High | 2 | Backlog |
| US-10 | Returning user | Have AQI fetched automatically for my location | Training suggestions account for air quality | High | 2 | Backlog |

### E3 — Training Intelligence

| ID | As a... | I want to... | So that... | Priority | Sprint | Status |
|---|---|---|---|---|---|---|
| US-11 | User | Open the app in the evening and see a training suggestion for tomorrow | I can plan ahead without doing any work | High | 3 | Backlog |
| US-12 | User | See the reasoning behind the suggestion (HRV, load, weather, AQI) | I trust it and understand why | High | 3 | Backlog |
| US-13 | User | Tweak the suggestion (intensity, duration, type) before confirming | I stay in control | High | 3 | Backlog |
| US-14 | User | Have the confirmed workout saved in the platform | My training history builds automatically | High | 3 | Backlog |

### E4 — Nutrition Intelligence

| ID | As a... | I want to... | So that... | Priority | Sprint | Status |
|---|---|---|---|---|---|---|
| US-15 | User | Snap a photo of my meal and have it recognised automatically | I don't have to manually search and log every item | High | 4 | Backlog |
| US-16 | User | Review and correct the recognised items before they're logged | Accuracy stays high | High | 4 | Backlog |
| US-17 | User | See a glycemic spike risk and inflammation flag for each meal | I understand what the science says about what I just ate | High | 4 | Backlog |
| US-18 | User | See a nudge when a meal might affect tomorrow's training or recovery | Food and training feel connected | Medium | 4 | Backlog |

### E5 — Longevity Score

| ID | As a... | I want to... | So that... | Priority | Sprint | Status |
|---|---|---|---|---|---|---|
| US-19 | User | See weekly sub-scores for fitness, nutrition, recovery, and environment | I know which pillar to focus on | Medium | 5 | Backlog |
| US-20 | User | See my overall longevity score trend week over week | I can see if I'm moving in the right direction | Medium | 5 | Backlog |
| US-21 | User | Read a weekly insight digest highlighting key patterns | I get value without having to analyse raw data | Medium | 5 | Backlog |

### E6 — Baseline Check-ins

| ID | As a... | I want to... | So that... | Priority | Sprint | Status |
|---|---|---|---|---|---|---|
| US-22 | User | Be prompted monthly to re-test my longevity baseline indicators | I can track long-term physical trajectory | Low | 6 | Backlog |

---

## Out of Scope (POC)

- Garmin workout export / direct sync
- Apple Watch write-back
- Social or community features
- Clinical integrations or medical records
- Prescriptive health advice — never (product positioning constraint)
- Web app — mobile only for POC
- Android — iOS first for POC

## Future Considerations

- Garmin Connect IQ workout export (Sprint 5+)
- Blood biomarker integration (e.g. via API from lab providers)
- Supplement tracking and science layer
- Sleep coaching integration (Oura, WHOOP data import)
- Longevity report PDF export for GP visits
