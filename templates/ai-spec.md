# AI Spec

**Project:** 
**Feature / Sprint:** 
**Date:** 
**Author:** 
**Status:** Draft / Review / Approved ← must be Approved before build starts
**NFRs in scope:** _(list which NFRs from docs/problem-statement.md apply to this sprint — e.g. encryption at rest, 99.9% uptime, Docker deployment)_

> This document is the brief for Claude Code (or any AI implementor).
> Be specific. Ambiguity here = bugs later.
> Status must be Approved and all Open Questions resolved before any code is written.

---

## Context
_(Why does this feature exist? What problem does it solve? Link back to Phase 1 problem statement and the goal in docs/project-goals.md it serves.)_


## Scope
_(What is IN this spec. What is explicitly OUT.)_

**In:**
- 
- 

**Out:**
- 
- 

---

## Version-Sensitive Dependencies
_(List any libraries used in this sprint where version matters — especially if the API changed between major versions. Claude must use the pinned versions from CLAUDE.md, not assume latest.)_

| Library | Pinned version | Breaking change to watch |
|---|---|---|
| | | e.g. "use createRoot not ReactDOM.render" |

_(None — if this sprint introduces no version-sensitive usage)_

---

## Environment Variables

> New variables introduced in this sprint only. Full list lives in `CLAUDE.md`.
> Claude: confirm all variables below are present in `.env.local` before writing any code that depends on them.

| Variable | Purpose | Where to get it | Required? |
|---|---|---|---|
| | | | Yes / No |

_(None — if this sprint introduces no new secrets)_

---

## Inputs & Outputs

| # | Input | Type | Source | Required? |
|---|---|---|---|---|
| 1 | | string / number / object / file | user / API / DB / agent | Yes / No |

| # | Output | Type | Destination | Notes |
|---|---|---|---|---|
| 1 | | | user / DB / agent | |

---

## 3rd Party Integrations
_(Complete one block per external API or service. Skip section entirely if none.)_

> **Before filling this in manually:** use the web research protocol below.
> Browse the official dev docs, extract what's needed, and pre-fill this section.
> Only ask the client for what the docs don't answer (API keys, account-specific config).

> **Security rule:** All credentials for this integration are server-side only. Never expose keys, tokens, or secrets to the client. The implementation spec must include a server-side API route or function that wraps all authenticated calls. Flag any design that routes secrets through the client as a blocker — do not proceed until resolved.

### Web Research Protocol (per integration)

1. **Find the docs**
   - Search: "[service name] developer documentation", "[service name] API reference", "[service name] REST API"
   - Prefer official docs. Skip anything behind login or paywall — note it as a gap.

2. **Extract auth method**
   - What auth does it use? OAuth2 / API key / JWT / Basic / other?
   - Where does the token/key go? Header / query param / body?
   - Is there a token refresh flow? What are expiry rules?
   - Any scopes or permissions required for our use case?

3. **Map the endpoints we need**
   - For each piece of data we need or action we trigger: find the exact endpoint
   - Document: method, path, required headers, query params, request body, response shape
   - Note rate limits, pagination, and any documented error codes

4. **Map to our DB and logic**
   - For each API response field: where does it land in our schema?
   - Any transformation needed (units, formats, naming)?
   - What do we store vs what do we discard?
   - Any webhooks or polling required to keep data fresh?

5. **Flag gaps**
   - Anything missing from public docs → list as Open Questions below

---

### Integration: [Service Name]

**Docs URL:**
**Auth method:**

#### Authentication

| Field | Value / Location | Notes |
|---|---|---|
| Token type | | OAuth2 / API key / JWT / Basic |
| Header / param name | | e.g. `Authorization: Bearer {token}` |
| Token expiry | | |
| Refresh flow | | Yes / No — describe if yes |
| Required scopes / permissions | | |
| Env var name | | e.g. `GARMIN_API_KEY` |

#### Endpoints

| # | Purpose | Method | Path | Auth required? |
|---|---|---|---|---|
| 1 | | GET/POST/PUT/DELETE | | Yes / No |
| 2 | | | | |

**Endpoint detail** _(repeat per endpoint)_

**Endpoint 1 — [purpose]**
- Method + path:
- Required headers:
- Query params:
- Request body:
```json
{}
```
- Response:
```json
{}
```
- Rate limit:
- Error codes to handle:

#### DB Mapping

| API field | Our DB table | Our column | Transformation needed |
|---|---|---|---|
| | | | |

#### Logic Notes
_(How does this integration fit into our app flow? When is it called, by what, triggered how?)_

---

## Database Schema
_(For sprints that introduce new tables or modify existing ones. Skip if not applicable.)_

```sql
-- table_name
column_name type constraints
```

**Migration notes:**
_(Any data migration concerns, RLS policies, indexes needed)_

---

## Business Logic & Rules
_(Decision points from docs/process-flow.md that this sprint implements. HITL zones from docs/stakeholder-register.md.)_

- 
- 

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
_(For AI-powered features only. Remove section if sprint has no AI calls.)_

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

- **Security:** _(cross-ref NFRs — encryption, access control)_
- **Data handling:** _(PII? Logging allowed?)_
- **Performance:** _(Response time expectations from NFRs)_
- **Error handling:** _(What happens when it fails?)_
- **Fallback:** _(What does the user see if the AI or service fails?)_

---

## Test Requirements

> Pre-fill from `docs/process-flow.md` — every process step in scope for this sprint has a success condition. Each success condition = one required test.
> Add edge cases and failure paths on top.
> All tests in this section must be written and passing before the sprint is marked done.
> After every run, append results to `docs/test-log.md` in plain English.

### From process-flow success conditions
_(One row per step in docs/process-flow.md that this sprint implements)_

| Step | Success condition (from process-flow.md) | Test written? |
|---|---|---|
| | _(paste the plain-English success condition here)_ | Yes / No |
| | | |

### Additional test cases

| # | Scenario | Input | Expected output | Type |
|---|---|---|---|---|
| T1 | Happy path | | | Functional |
| T2 | Edge case | | | Edge |
| T3 | Failure / error | | | Negative |

**Test log:** After every run → append entry to `docs/test-log.md`. Plain English. Non-technical client must be able to read it.

---

## Open Questions
> Generated from sprint content during Phase 4E. All must be answered before Status → Approved.
> See phase4-spec/SKILL.md for category prompts used to generate these.

- [ ] 
- [ ] 

---

## Notes for Claude Code
_(Anything specific Claude should know when implementing this)_
