# AI Spec

**Project:** 
**Feature / Sprint:** 
**Date:** 
**Author:** 
**Status:** Draft / Review / Approved

> This document is the brief for Claude Code (or any AI implementor).
> Be specific. Ambiguity here = bugs later.

---

## Context
_(Why does this feature exist? What problem does it solve? Link back to Phase 1 problem statement.)_


## Scope
_(What is IN this spec. What is explicitly OUT.)_

**In:**
- 
- 

**Out:**
- 
- 

---

## Inputs & Outputs

| # | Input | Type | Source | Required? |
|---|---|---|---|---|
| 1 | | string / number / object / file | user / API / DB / agent | Yes / No |

| # | Output | Type | Destination | Notes |
|---|---|---|---|---|
| 1 | | | user / API / DB / agent | |

---

## Acceptance Criteria
_(When is this done? Written as testable statements.)_

- [ ] Given [context], when [action], then [expected result]
- [ ] Given [context], when [action], then [expected result]
- [ ] Given [context], when [action], then [expected result]

---

## Agent / Skill Dependencies

| Agent / Skill | Role in this feature | Input it provides | Output it needs |
|---|---|---|---|
| | | | |

---

## Prompt Architecture
_(For AI-powered features only)_

**Model:** Claude / GPT-4 / other  
**Interaction type:** Single-turn / Multi-turn / Agent loop  
**System prompt location:** `skills/[name]/SKILL.md`

**Key prompt design notes:**
- 
- 

**Guardrails:**
- What should the model never do or say?
- What should trigger a human-in-the-loop fallback?

---

## Constraints & Rules

- **Security:** 
- **Data handling:** _(PII? Logging allowed?)_
- **Performance:** _(Response time expectations)_
- **Error handling:** _(What happens when it fails?)_
- **Fallback:** _(What does the user see if the AI fails?)_

---

## Test Cases

| # | Scenario | Input | Expected output | Type |
|---|---|---|---|---|
| T1 | Happy path | | | Functional |
| T2 | Edge case | | | Edge |
| T3 | Failure / error | | | Negative |

---

## Open Questions
_(Unresolved decisions that need answering before build starts)_

- [ ] 
- [ ] 

---

## Notes for Claude Code
_(Anything specific Claude should know when implementing this)_

