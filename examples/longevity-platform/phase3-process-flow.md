# Process Flow

**Project:** Longevity Intelligence Platform
**Process name:** Full User Workflow
**Track:** AS-IS + TO-BE
**Date:** 2026-03-23
**Mapped with:** Mirko Radeka

---

## AS-IS Process (Current broken workflow)

| Step # | Actor | Action | Input | Output | Tool used | Decision? | Pain point? |
|---|---|---|---|---|---|---|---|
| 1 | User | Check sleep, HRV, body battery | Wearable data | Mental note | Garmin Connect | No | No |
| 2 | User | Review recent training load | Activity history | Mental note | Strava | No | No |
| 3 | User | Navigate to custom project | — | Chat open | ChatGPT | No | Yes — context switching |
| 4 | User | Type weekly summary | Memory | Text input | ChatGPT | No | Yes — manual, repetitive |
| 5 | User | Screenshot health snapshot, upload | Garmin screen | Image in chat | ChatGPT | No | Yes — manual capture |
| 6 | User | Re-state goal | Memory | Text input | ChatGPT | No | Yes — repeated every session |
| 7 | User | Ask for today's suggestion | All above | Suggestion | ChatGPT | No | — |
| 8 | User | Evaluate suggestion | Experience | Accept / reject | — | Yes | Yes — often wrong |
| 9 | User | Share location for air quality | Location | AQI context added | ChatGPT | No | Yes — should be automatic |
| 10 | User | Share weather if needed | Manual | Weather context added | ChatGPT | No | Yes — should be automatic |
| 11 | User | Iterate until suggestion is acceptable | Prompts | Final workout | ChatGPT | Yes | Yes — unpredictable iterations |
| 12 | User | Ask to reformat for Garmin | Workout text | Garmin-formatted output | ChatGPT | No | Yes — extra step |
| 13 | User | Manually import workout to Garmin | Formatted output | Workout in Garmin | Garmin Connect | No | Yes — full round trip |
| 14 | User | Eat a meal | — | — | — | No | — |
| 15 | User | Manually search and log food | Memory / label | Calorie log | LoseIt | No | Yes — slow, tedious |
| 16 | User | No inflammation or glycemic insight | — | — | LoseIt | No | Yes — critical gap |
| 17 | User | No food ↔ recovery connection | — | — | — | No | Yes — critical gap |

---

## TO-BE Process (New platform)

### Flow 1: Onboarding (one-time)

| Step # | Actor | Action | Input | Output | Tool used | Decision? |
|---|---|---|---|---|---|---|
| 1 | User | Sign up, connect Garmin + Apple Watch | OAuth | Wearable data synced | Platform | No |
| 2 | User | Complete health profile | Age, sex, weight, height, family history | Persistent user context | Platform | No |
| 3 | User | Set goals | Performance + longevity goals | Goal layer saved | Platform | No |
| 4 | User | Log longevity baseline indicators | Grip strength, sit-to-stand, VO2max, resting HR | Baseline snapshot | Platform | No |
| 5 | Platform | Establish starting longevity sub-scores | All onboarding data | Initial score | Platform | No |

### Flow 2: Evening — Training Planning (daily)

| Step # | Actor | Action | Input | Output | Tool used | Decision? |
|---|---|---|---|---|---|---|
| 1 | Platform | Auto-pull wearable data | Garmin/Apple Watch API | HRV, sleep, load, body battery | Background sync | No |
| 2 | Platform | Fetch tomorrow's weather + AQI | Location | Environmental context | Weather + AQI APIs | No |
| 3 | Platform | Generate training suggestion | All context + longevity science layer | Proposed workout with reasoning | LLM + science layer | No |
| 4 | User | Review suggestion | Proposal | Accept or tweak | Platform UI | Yes |
| 5 | Platform | Save confirmed workout | User decision | Workout logged | Platform | No |

### Flow 3: Throughout Day — Nutrition Logging

| Step # | Actor | Action | Input | Output | Tool used | Decision? |
|---|---|---|---|---|---|---|
| 1 | User | Snap meal photo | Camera | Draft food log | Vision model | No |
| 2 | User | Confirm or correct items/portions | Draft log | Confirmed meal | Platform UI | Yes |
| 3 | Platform | Surface glycemic + inflammation insight | Logged meal + science layer | Contextual insight | LLM + science layer | No |
| 4 | Platform | Connect food to next day recovery/training | Meal data + training plan | Nudge if relevant | Platform | No |

### Flow 4: Weekly Review

| Step # | Actor | Action | Input | Output | Tool used | Decision? |
|---|---|---|---|---|---|---|
| 1 | Platform | Calculate weekly sub-scores | 7 days of fitness, nutrition, recovery, environment data | 4 sub-scores | Platform | No |
| 2 | Platform | Calculate overall longevity score | Sub-scores + trend vs prior week | Score + trend direction | Platform | No |
| 3 | Platform | Surface key insights and anomalies | Score delta + data patterns | Weekly digest | LLM | No |
| 4 | User | Review and reflect | Digest | — | Platform UI | Yes |
| 5 | Platform | Prompt monthly baseline re-test (if due) | Last test date | Reminder | Platform | No |

---

## Friction Inventory (AS-IS)

- 4-5 apps open per session
- Goal re-stated every single session
- Weekly context typed manually every session
- Health snapshot captured by screenshot and uploaded manually
- Environmental data (AQI, weather) fetched manually via location share
- Workout suggestion requires multiple iterations
- Accepted workout must be reformatted and manually re-imported to Garmin
- Nutrition logged manually per item — no photo recognition
- Zero inflammation or glycemic insight from current tool
- No connection between food and training or recovery data

## Decision Points (Human-in-the-loop)

- User must confirm training suggestion before it is saved (never auto-applied)
- User must confirm food log after photo recognition (misidentification risk)
- User controls goal and baseline updates — platform never overwrites these

## Key Observations

- The user IS the target user — every friction point is lived, not assumed
- The current workflow is a fully manual integration layer between 5 tools that don't talk to each other
- The real value is not smarter suggestions — it's eliminating the re-entry tax and connecting the loops
- Environmental context (AQI, weather) is currently a manual afterthought — should be a default input
- The food ↔ training connection is completely invisible today and could be a significant differentiator
