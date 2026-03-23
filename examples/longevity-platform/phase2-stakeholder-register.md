# Stakeholder Register

**Project:** Longevity Intelligence Platform
**Date:** 2026-03-23

---

| Stakeholder | Role | Impact | Change for them | Notes |
|---|---|---|---|---|
| End user (health-conscious 35-50+) | Core user | High | Better | Replaces fragmented 4-5 app workflow with one persistent, contextually aware experience |
| Mirko Radeka | Builder + business owner | High | Better | POC validates concept, path to early users and monetization |
| Garmin | Data provider (API) | Low | Neutral | API terms must be respected; no write access at POC stage |
| Apple (HealthKit) | Data provider (API) | Low | Neutral | API terms must be respected; no write access at POC stage |
| Regulators (FTC) | Risk stakeholder | Med | Neutral | "We show data, you decide" framing must be maintained — no efficacy claims |

---

## Baseline Measurements

| Metric | Current value | Source | Notes |
|---|---|---|---|
| Time per daily session | ~15 min | User self-report | Includes prompting until suggestion is acceptable |
| Apps touched per session | 4-5 | User self-report | Garmin, Strava, ChatGPT, AirQI, Weather |
| Context re-entry | Every session | User self-report | Goal, weekly summary, health snapshot — all manual, every time |
| Manual steps count | 10+ | Observed workflow | Screenshot upload, location share, weather check, Garmin reformat |
| Food logging friction | Manual entry per meal | User self-report | LoseIt — no photo recognition, no inflammation/glycemic insight |
| Inflammation / glycemic signal | Zero | User self-report | LoseIt provides calories only |
| Food ↔ training connection | None | User self-report | Two completely separate workflows with no shared context |
| Frustration score | ~7/10 | Inferred | User iterates until acceptable; workaround is the norm |

---

## Success Targets

| Metric | Baseline | Target | Type |
|---|---|---|---|
| Daily session time | ~15 min | <2 min | >85% reduction |
| Apps touched | 4-5 | 1 | Absolute |
| Context re-entry | Every session | Never | 100% elimination |
| Training suggestion quality | Hit or miss | Contextually aware (HRV + load + weather + air) | Qualitative |
| Nutrition logging friction | Manual text entry | Photo snap | Qualitative |
| Inflammation / glycemic insight | Zero | Present | Absolute |
| Food ↔ training connection | None | Visible in same session | Absolute |

---

## Second-Order Effects

- Better training suggestions → fewer junk sessions → faster HM sub 1:50 progression
- Food + recovery connected → user sees patterns previously invisible → platform stickiness
- Low friction logging → higher data quality → better insights → more user trust (flywheel)

---

## Human-in-the-Loop Zones

- Photo food recognition must be user-confirmed before logging (misidentification risk)
- Training suggestions must never be framed as medical advice — UI copy must reinforce this
- No autonomous actions at POC stage — all suggestions require explicit user confirmation
