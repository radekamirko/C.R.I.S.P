# Agent / Skill Map

**Project:** Longevity Intelligence Platform
**Date:** 2026-03-23

---

## Agent Overview

| Agent | Responsibility | Inputs | Outputs | Sprint |
|---|---|---|---|---|
| data-sync-agent | Pulls and normalises all external data sources daily | Garmin API, Apple HealthKit, Open-Meteo, OpenAQ | Structured daily snapshot in Supabase | 2 |
| training-agent | Generates evening training suggestion with full context and reasoning | Daily snapshot, user profile, goal, training history, science layer | Proposed workout + reasoning text | 3 |
| nutrition-agent | Processes meal photos, identifies food, surfaces glycemic + inflammation insight | Meal photo, user profile, science layer | Confirmed meal log + insight text | 4 |
| science-layer-agent | RAG retrieval over curated longevity science content | Query from training or nutrition agent | Relevant science excerpts with citations | 3 + 4 |
| memory-agent | Manages persistent user context — profile, goals, history, baseline | All session data | Formatted context object for each Claude call | 1+ |
| scoring-agent | Calculates weekly sub-scores and overall longevity score trend | 7-day aggregated data from all logs | 4 sub-scores + overall score + trend direction | 5 |

---

## Agent Detail

### data-sync-agent
**Responsibility:** Runs daily (background) to pull fresh data from all external sources and store normalised records.

**Inputs:**
- Garmin Health API: HRV, sleep score, body battery, training load, activities
- Apple HealthKit: steps, active energy, resting HR, VO2max (if available)
- Open-Meteo: tomorrow's weather forecast for user location
- OpenAQ: current and forecast AQI for user location

**Outputs:**
- `daily_snapshots` table in Supabase: one record per user per day with all metrics
- `environmental_context` table: weather + AQI per user per day

**Boundaries:**
- Read-only from all external APIs
- Never writes back to Garmin or Apple
- Caches environmental data — one fetch per location per day maximum
- Fails gracefully: if a source is unavailable, marks that field as null with a `source_unavailable` flag — never blocks the daily flow

**SKILL.md location:** `skills/data-sync-agent/SKILL.md`

---

### training-agent
**Responsibility:** Generates a contextual training suggestion each evening based on the full user state.

**Inputs:**
- Today's daily snapshot (HRV, sleep, body battery, training load)
- Tomorrow's environmental context (weather, AQI)
- User profile (goal, training history, fitness baseline)
- Last 7 days of confirmed workouts
- science-layer-agent retrieval (relevant training/recovery science)

**Outputs:**
- Proposed workout (type, duration, intensity, description)
- Reasoning text (plain language explanation referencing HRV, load, AQI, goal)
- Confidence level (high / medium / low — shown to user as context)

**Boundaries:**
- Never auto-saves — always requires user confirmation
- Never uses medical language: "your HRV suggests" not "your heart is showing signs of"
- Fallback: if data is incomplete, generates a conservative suggestion and flags which data was missing
- Must reference the user's active goal in every suggestion

**SKILL.md location:** `skills/training-agent/SKILL.md`

---

### nutrition-agent
**Responsibility:** Processes meal photos, identifies food items and portions, surfaces science-backed nutritional insight.

**Inputs:**
- Meal photo (from device camera)
- User profile (dietary preferences, goals, known conditions from family history)
- science-layer-agent retrieval (glycemic index, inflammation markers for identified foods)

**Outputs:**
- Draft food log (list of identified items + estimated portions)
- Glycemic spike risk rating (low / medium / high)
- Inflammation flag (yes / no + which items)
- Optional nudge: connection to next day training/recovery if relevant

**Boundaries:**
- Draft always shown to user before any data is committed
- Never commits without explicit user confirmation
- Fallback: if photo recognition fails or confidence is low, surface manual search
- Never frames insight as medical advice: "research suggests" not "you should avoid"

**SKILL.md location:** `skills/nutrition-agent/SKILL.md`

---

### science-layer-agent
**Responsibility:** RAG retrieval over a curated longevity science knowledge base. Called by training-agent and nutrition-agent to ground suggestions in evidence.

**Inputs:**
- Query string from calling agent (e.g. "low HRV recovery recommendations" or "glycemic index white rice")

**Outputs:**
- Relevant science excerpts (2-3 passages max)
- Source citations (study title, journal, year)

**Boundaries:**
- Only retrieves — never generates scientific claims independently
- Source material must be peer-reviewed (PubMed, major journals)
- If no relevant result found, returns empty — calling agent uses its own reasoning
- Citations always included in output for transparency

**SKILL.md location:** `skills/science-layer-agent/SKILL.md`

---

### memory-agent
**Responsibility:** Builds and maintains the persistent user context object that is injected into every Claude API call.

**Inputs:**
- User profile (Supabase)
- Active goals
- Last 30 days of training logs
- Last 30 days of nutrition logs
- Longevity baseline indicators
- Recent weekly scores (if available)

**Outputs:**
- Formatted context object (structured text) injected as system context into each agent call
- Keeps token usage within Claude context window limits

**Boundaries:**
- Never stores raw PII in Claude prompts — uses anonymised references
- Truncates history intelligently (most recent + most relevant, not raw dump)
- Updated after each user-confirmed action (workout save, meal log)

**SKILL.md location:** `skills/memory-agent/SKILL.md`

---

### scoring-agent (Sprint 5)
**Responsibility:** Calculates weekly longevity sub-scores and overall score trend.

**Inputs:**
- 7 days of daily snapshots (fitness, nutrition, recovery, environmental)
- Prior week's scores (for trend calculation)
- User baseline indicators (for relative scoring)

**Outputs:**
- 4 sub-scores: fitness, nutrition, recovery, environment (0-100 each)
- Overall score (weighted composite)
- Trend direction vs prior week (up / flat / down)
- Weekly insight digest (2-3 key patterns surfaced by LLM)

**Boundaries:**
- Requires minimum 5 days of data in a week to calculate — otherwise shows incomplete state
- Framed as personal progress mirror — never compared to external benchmarks
- Score language is motivational, never judgmental
- Requires minimum 2 weeks of history before trend is shown

**SKILL.md location:** `skills/scoring-agent/SKILL.md`

---

## Agent Handoff Map

```
User action
    │
    ├── Evening open app
    │       └── memory-agent → training-agent → science-layer-agent → UI suggestion
    │
    ├── Meal photo snap
    │       └── nutrition-agent → science-layer-agent → UI review screen
    │
    ├── Background (daily)
    │       └── data-sync-agent → Supabase daily_snapshots
    │
    └── Weekly (Sunday)
            └── scoring-agent → memory-agent → UI weekly digest
```
