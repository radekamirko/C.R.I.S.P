# [Project Name]

> Compile this file from your completed CRISP docs/ folder.
> This is the single source of truth Claude reads at the start of every session.
> Keep it current — update after every sprint.

---

## What this project is
_(From docs/problem-statement.md — one sentence)_


## Why it exists
_(Painkiller: what pain does it solve? For whom?)_


## Desired outcome
_(From docs/stakeholder-register.md — what does success look like?)_


## Constraints
_(From docs/problem-statement.md — budget, time, legal, technical)_

- Budget: 
- Timeline: 
- Legal/Compliance: 
- Technical: 

## What we are building
_(Internal tool / External product. Summary of scope from docs/initial-backlog.md)_


## What we are NOT building
_(From docs/initial-backlog.md — out of scope / POST-MVP)_


## Tech stack
_(From Phase 4A tech stack proposal)_

| Layer | Tool | Notes |
|---|---|---|
| | | |

## Folder structure
_(Describe key directories and what lives where)_

```
/
├── 
├── 
└── 
```

## Agents / Skills in this project
_(From Phase 4E agent map — name, responsibility, SKILL.md location)_

| Agent/Skill | Responsibility | Location |
|---|---|---|
| | | skills/[name]/SKILL.md |

## Environment Variables

> Never commit these to version control. All keys live in `.env.local` (or equivalent).
> Claude: if a required variable is missing or undefined, stop and flag it — do not proceed or hardcode a fallback.

| Variable | Purpose | Where to get it | Required? | Sprint introduced |
|---|---|---|---|---|
| | | | Yes / No | |

**Rules:**
- All secrets accessed via environment variables — never hardcoded
- `.env.local` (or equivalent) is always in `.gitignore` — verify before first commit
- Server-side secrets (OAuth tokens, service role keys) never sent to client
- If a variable is missing at runtime, fail loudly with a clear error — no silent fallbacks

**`.env.local` template** _(copy this, never commit the filled version)_:
```
# [Service name]
VARIABLE_NAME=
```

## Human-in-the-loop zones
_(From docs/risk-assessment.md — where Claude must NOT act autonomously)_

- 
- 

## Security rules
_(Non-negotiable — Claude must follow these always)_

- Never log or expose PII
- Never commit secrets or API keys
- All environment variables verified present before use — fail loudly if missing
- 

## Current sprint
_(Update this at the start of each sprint)_

**Sprint:** 
**Goal:** 
**AI Spec:** `docs/ai-spec-[name].md`

## Open questions
_(Unresolved — Claude should flag these, not assume answers)_

- 

---

## CRISP Output Manifest

> All project discovery and spec documents live in `docs/`. 
> If a file is marked ✅ it exists and is current. If ❌ it is missing or incomplete — flag before proceeding with any work that depends on it.

### Phase 1 — Clarify
| File | Status | Notes |
|---|---|---|
| `docs/problem-statement.md` | ✅ / ❌ | |
| `docs/buy-vs-build-matrix.md` | ✅ / ❌ | |
| `docs/market-research.md` | ✅ / ❌ / N/A (internal) | |
| `docs/value-proposition-canvas.md` | ✅ / ❌ / N/A (internal) | |
| `docs/swot.md` | ✅ / ❌ / N/A (internal) | |

### Phase 2 — Results
| File | Status | Notes |
|---|---|---|
| `docs/stakeholder-register.md` | ✅ / ❌ | Includes baseline metrics + success criteria |

### Phase 3 — Investigate
| File | Status | Notes |
|---|---|---|
| `docs/process-flow.md` | ✅ / ❌ | |
| `docs/user-journey-map.md` | ✅ / ❌ | |
| `docs/project-goals.md` | ✅ / ❌ | |
| `docs/ux-discovery.md` | ✅ / ❌ / N/A (non-UI) | |

### Phase 4 — Spec
| File | Status | Notes |
|---|---|---|
| `docs/design-system.md` | ✅ / ❌ / N/A (non-UI) | |
| `docs/ux-spec.md` | ✅ / ❌ / N/A (non-UI) | |
| `docs/initial-backlog.md` | ✅ / ❌ | MVP tags applied |
| `docs/assumptions-log.md` | ✅ / ❌ | |
| `docs/risk-assessment.md` | ✅ / ❌ | |
| `docs/mvp-prioritization.md` | ✅ / ❌ | HVLE scores + MVP line |
| `docs/sprint-plan.md` | ✅ / ❌ | |
| `docs/ai-spec-[sprint/feature].md` | ✅ / ❌ | One per sprint — list all below |
| `docs/ai-spec-[integration].md` | ✅ / ❌ / N/A | One per 3rd party service — list all below |

**AI Specs written:**
- [ ] `docs/ai-spec-` 
- [ ] `docs/ai-spec-` 

**Integration specs written:**
- [ ] `docs/ai-spec-` _(service name)_
- [ ] `docs/ai-spec-` _(service name)_
