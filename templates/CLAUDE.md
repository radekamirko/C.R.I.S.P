# [Project Name]

> Compile this file from your completed Mileva Method documents.
> This is the single source of truth Claude reads at the start of every session.

---

## What this project is
_(From problem-statement.md — one sentence)_


## Why it exists
_(Painkiller: what pain does it solve? For whom?)_


## Desired outcome
_(From stakeholder-register.md — what does success look like?)_


## Constraints
_(From problem-statement.md — budget, time, legal, technical)_

- Budget: 
- Timeline: 
- Legal/Compliance: 
- Technical: 

## What we are building
_(Internal tool / External product. Summary of scope from initial-backlog.md)_


## What we are NOT building
_(From initial-backlog.md — out of scope)_


## Tech stack
_(From Phase 4A tech stack proposal)_


## Folder structure
_(Describe key directories and what lives where)_

```
/
├── 
├── 
└── 
```

## Agents / Skills in this project
_(From Phase 4B agent map — name, responsibility, SKILL.md location)_

| Agent/Skill | Responsibility | Location |
|---|---|---|
| | | skills/[name]/SKILL.md |

## Environment Variables

> Never commit these to version control. All keys live in `.env.local` (or equivalent).
> Claude: if a required variable is missing or undefined, stop and flag it — do not proceed or hardcode a fallback.

| Variable | Purpose | Where to get it | Required? | Sprint introduced |
|---|---|---|---|---|
| | | | Yes / No | |
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

# [Service name]
VARIABLE_NAME=
```

## Human-in-the-loop zones
_(From risk-assessment.md — where Claude must NOT act autonomously)_

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
**AI Spec:** `templates/ai-spec.md`

## Open questions
_(Unresolved — Claude should flag these, not assume answers)_

- 
