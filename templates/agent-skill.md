---
name: [agent-name]
description: [One sentence — what this agent does and when it's triggered. Be specific enough that Claude can decide whether to invoke it.]
---

# [Agent Name]

## Responsibility

_(One paragraph. What is this agent's job? What problem does it solve within the system? What does it own end-to-end?)_

---

## Inputs

| # | Input | Type | Source | Required? | Notes |
|---|---|---|---|---|---|
| 1 | | string / number / object / array / file | user / API / DB / agent / context | Yes / No | |
| 2 | | | | | |

---

## Outputs

| # | Output | Type | Destination | Notes |
|---|---|---|---|---|
| 1 | | string / number / object / array | user / API / DB / agent | |
| 2 | | | | |

---

## Boundaries

> These are non-negotiable. Claude must follow them every time this agent runs.

**This agent must never:**
- 
- 

**This agent must always:**
- 
- 

**Human-in-the-loop triggers:**
_(List any output or situation that requires human review before the agent proceeds or commits)_
- 

**Fallback behavior:**
_(What does this agent do if inputs are incomplete, an API fails, or confidence is low?)_
- 

---

## Handoffs

### Calls (outbound)

| Agent / Service | When | Input passed | Output expected |
|---|---|---|---|
| | _(condition that triggers the call)_ | | |

### Called by (inbound)

| Agent / Trigger | When this agent is invoked | What it receives | What it returns |
|---|---|---|---|
| | | | |

_(None — if this agent is standalone)_

---

## System Prompt

> This is the prompt injected as system context when this agent runs.
> Edit this carefully — tone, constraints, and framing live here.

```
You are [agent name], a [role description] for [product name].

Your job: [one sentence description of the core task]

## Context you will receive
[Describe what structured context is passed in — user profile, data snapshot, etc.]

## Your output
[Describe exactly what you return — format, structure, tone]

## Rules
- [Non-negotiable constraint]
- [Non-negotiable constraint]
- [Non-negotiable constraint]

## What you must never do
- [Hard boundary]
- [Hard boundary]

## Tone and language
- [Tone guideline]
- [Language constraint — e.g. "never use medical language"]
```

---

## Prompt Design Notes

_(Reasoning behind key prompt decisions — useful when revisiting or debugging output quality)_

- 
- 

---

## Quality Gates

Before this agent's output is used or shown to the user:

- [ ] Output is within expected format/structure
- [ ] No prohibited language used (check Boundaries above)
- [ ] Fallback triggered if confidence is low or inputs were incomplete
- [ ] Human-in-the-loop check passed if required

---

## Test Cases

| # | Scenario | Input | Expected output | Pass/Fail |
|---|---|---|---|---|
| T1 | Happy path — full inputs | | | |
| T2 | Partial inputs / missing data | | Fallback triggered, partial output flagged | |
| T3 | Boundary violation check | | Prohibited content absent from output | |

---

## Notes for Claude Code

_(Implementation specifics — where this agent lives in the codebase, how it's invoked, any library or API dependencies)_

- **File location:** `lib/agents/[name].ts` _(or equivalent)_
- **Invoked by:** _(screen / other agent / cron / background job)_
- **Dependencies:** _(APIs, DB tables, other agents)_
