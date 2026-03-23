# Risk Assessment

**Project:** Longevity Intelligence Platform
**Date:** 2026-03-23

---

## Risk Register

| # | Risk | Category | Likelihood | Impact | Score | Mitigation | Owner |
|---|---|---|---|---|---|---|---|
| R1 | Garmin Health API access delayed or denied | Technical | M | H | High | Apply for API access immediately — approval can take weeks. Have manual CSV import as fallback for POC. | Mirko |
| R2 | Apple HealthKit review rejection on App Store | Technical | L | H | High | Keep HealthKit usage scoped to minimum, document purpose clearly, avoid any clinical language in app. | Mirko |
| R3 | Food photo recognition accuracy too low for trust | Technical | M | H | High | Always show recognition result before logging — user corrects, never auto-commits. Set expectations in UX copy. | Mirko |
| R4 | FTC flags product as making health claims | Legal | L | H | High | Strict language policy: "the science says X" not "you should do X". Legal review of all UI copy before public launch. | Mirko |
| R5 | Claude API costs spike with real users | Business | M | M | Medium | Implement caching for repeated context. Monitor token usage per session. Set spend alerts from day 1. | Mirko |
| R6 | User drops off after onboarding (too much data entry) | Business | H | M | Medium | Keep onboarding to under 5 minutes. Make baseline indicators optional at setup — can complete later. | Mirko |
| R7 | Garmin or Apple change API terms mid-build | Technical | L | M | Medium | Build data layer as abstraction — swap source without breaking downstream logic. | Mirko |
| R8 | Solo builder burnout / scope creep | People | M | H | High | Hard POC scope enforced. Longevity score deferred to Sprint 5. No new features during POC sprints. | Mirko |
| R9 | User health data breach | Security | L | H | High | Supabase RLS on all user tables. No PII in logs. Encryption at rest. Garmin/Apple tokens never stored client-side. | Mirko |
| R10 | Open-Meteo or OpenAQ API rate limits hit | Technical | L | L | Low | Cache environmental data per location per day — one fetch, not per-session. | Mirko |

**Score = Likelihood × Impact:** HH = Critical, HM/MH = High, MM = Medium, rest = Low

---

## Human-in-the-Loop Zones

| Process step | Why human needed | Guardrail implemented |
|---|---|---|
| Training suggestion confirmation | User must own the decision — no auto-applied workouts | ✅ Explicit confirm button required before saving |
| Food photo recognition review | Vision model will misidentify — user corrects before commit | ✅ Review screen always shown before logging |
| Longevity baseline indicator logging | Self-reported physical tests — user must perform and enter | ✅ Manual entry only, no auto-inference |
| Goal updates | Platform never changes user goals autonomously | ✅ Goals only editable from profile settings by user |
| Monthly baseline re-test prompt | Reminder only — user decides when and if to re-test | ✅ Prompt only, no gate or forced flow |

---

## Security Posture

- **Data classification:** Sensitive personal health data (biometrics, nutrition, location)
- **PII involved:** Yes — age, sex, weight, location, health indicators
- **Auth mechanism:** Supabase Auth (email + password, JWT), Garmin OAuth 2.0, Apple HealthKit permissions
- **Data residency requirement:** US (initial market) — Supabase region: us-east-1
- **Compliance framework:** Not a HIPAA covered entity. FTC health claim rules apply. No medical claims.

## Security Rules (non-negotiable)

- Never log or expose PII in application logs
- Never commit secrets, API keys, or tokens to version control
- All user data tables protected by Supabase Row Level Security (RLS)
- Garmin and Apple OAuth tokens stored server-side only — never in client storage
- All Claude API calls: no raw user PII in prompts — use anonymised context references
- HTTPS enforced everywhere — no HTTP fallback

## Open Security Questions

- [ ] Does Garmin Health API require a data processing agreement (DPA) before production use?
- [ ] What is the minimum HealthKit permission scope needed — confirm before App Store submission
- [ ] Should user data be deletable on request (soft GDPR posture even for US market)?
