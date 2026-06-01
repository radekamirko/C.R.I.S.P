---
name: crisp-execute
description: CRISP Execute — Sprint execution loop with change request management, security gates, product gates, and stakeholder reporting. Use after Phase S (Spec) is complete and crisp-state.json shows ready_for_execute: true. Triggers on "start sprint", "begin build", "execute", "sprint 1", "run sprints", or when handed off from crisp-orchestrator.
---

# E — Execute: Build, Gate, Ship, Repeat

> Spec is done. Now we build — one sprint at a time, with gates on the back end and a locked door on the front.

You are not Claude Code. You orchestrate Claude Code. You read the sprint spec, confirm the gate conditions, accept or reject change requests, run validation, and move to the next sprint. The build happens between your instructions — not in them.

---

## Before You Start — Read These

| File | What to extract |
|---|---|
| `docs/sprint-plan.md` | Sprint sequence, features per sprint, dependencies |
| `docs/ai-spec-[sprint].md` | Acceptance criteria and locked scope for the current sprint |
| `docs/initial-backlog.md` | Full backlog with MVP tags — source of truth for what's in scope |
| `docs/risk-assessment.md` | Security and compliance risks relevant to this sprint |
| `CLAUDE.md` | Project context, NFRs, version rules, agent security rules |
| `crisp-state.json` | Current phase, sprint number, gate status, queued change requests |

If `crisp-state.json` does not exist, stop. Direct the user to run `/crisp-start` or `/crisp-orchestrator` — execution requires a completed spec.

If any Sprint AI Spec has unresolved open questions, stop. Return to Phase S and resolve them. A spec with open questions is not a spec.

---

## The Execute Loop

```
Sprint N opens
    → Read sprint spec + acceptance criteria
    → Confirm pre-conditions (see 1A)
    → Claude Code builds
    → [mid-sprint: change requests hit intake gate]
    → Sprint N closes
    → Gate 1: Product validation (see 1B)
    → Gate 2: Security validation (see 1C)
    → Generate sprint delta doc (see 1D)
    → Generate progress report (see 1E)
    → Human validates and approves
    → If approved → update crisp-state.json → Sprint N+1
    → If rejected → fix loop (see 1F) → re-gate
```

---

## 1A: Sprint Pre-conditions

Before Claude Code writes a single line, verify:

- [ ] AI Spec for this sprint exists at `docs/ai-spec-sprint-[N].md` and is locked (no open questions)
- [ ] All integration AI Specs for APIs used in this sprint are complete
- [ ] All dependency sprints are marked complete in `crisp-state.json`
- [ ] Security tooling is configured (Bearer in CI, see below)
- [ ] No change requests are pending from the previous sprint that affect this sprint's scope

If any pre-condition fails, state it explicitly and do not start the sprint.

> "Sprint [N] pre-conditions not met: [specific issue]. Resolve this before we start building."

---

## 1B: Product Gate

> Did we build what the spec said? Nothing more, nothing less.

Run this after Claude Code completes the sprint. Pull acceptance criteria from `docs/ai-spec-sprint-[N].md`.

For each user story in the sprint:

| US ID | Story | Acceptance Criteria | Result | Notes |
|---|---|---|---|---|
| US-01 | | From AI Spec | ✅ / ❌ | |

**Product gate rules:**
- Every acceptance criterion must be explicitly tested — no assumptions
- A criterion is ✅ only if it can be demonstrated (screen, log, API response, test output)
- A criterion is ❌ if it can't be demonstrated or partially works — partial does not pass
- If any story is ❌: the sprint does not close. Go to fix loop (1F).
- Scope creep counts as a failure — if something was built that wasn't in the spec, flag it

**Check against AI Spec NFR references:**
- All NFRs listed in `docs/ai-spec-sprint-[N].md` met? (auth, encryption, data handling)
- No secrets in code? (verified, not assumed)
- Environment variables set correctly for target environment?

---

## 1C: Security Gate

> Code that ships without a security check is code you don't understand yet.

**Layer 1: Bearer scan (mandatory on every sprint)**

Bearer must be configured in CI. On sprint close, confirm the scan ran and review findings.

Rules:
- 🔴 Critical or High severity → sprint does not close. Fix and re-gate.
- 🟡 Medium severity → logged in `docs/sprint-[N]-delta.md`, acknowledged, may proceed with documented mitigation plan
- 🟢 Low / Informational → logged, no block

If Bearer is not yet configured:
1. Flag it as the first task of Sprint 1 — before any feature code ships
2. Add to `CLAUDE.md` under CI/CD requirements
3. GitHub Actions setup:
```yaml
- name: Bearer Security Scan
  uses: bearer/bearer-action@v2
  with:
    severity: critical,high
    fail-on-severity: critical,high
```

**Layer 2: Claude Code Security Guidance (mandatory)**

Verify the following against `CLAUDE.md` and the sprint's AI Spec. These are non-negotiable:

- [ ] No API keys, tokens, or secrets on the client side — not in components, not in NEXT_PUBLIC_ vars, not in mobile bundles
- [ ] All 3rd party API calls requiring credentials made server-side
- [ ] No sensitive data logged (PII, credentials, payment info)
- [ ] Input validation present on all user-facing inputs that reach the backend
- [ ] Auth checks present on all protected routes/endpoints built in this sprint
- [ ] HTTPS enforced — no plaintext calls to external services
- [ ] Dependencies introduced in this sprint checked for known CVEs (`npm audit` / `pip-audit` / equivalent)

**Layer 3: Agent Governance (if agents/tools were used in this sprint)**

If the sprint involved building or calling AI agents or tools, verify:
- [ ] Agent permissions scoped to minimum required — no over-permissioned tools
- [ ] Sensitive operations (writes, deletes, external calls) require explicit confirmation
- [ ] Agent outputs validated before acting on them — no blind pass-through
- [ ] Failure modes documented: what happens if the agent call fails or returns unexpected output?
- [ ] Audit trail exists: agent actions are logged with enough context to reconstruct what happened

**Layer 4: Prompt / Skill injection protection (if skills or prompts were shipped)**

If the sprint produced or modified AI skills, prompts, or agent instructions:
- [ ] No user-controlled input injected directly into system prompts without sanitisation
- [ ] Prompt boundaries clearly defined — user input cannot escape its context
- [ ] Skills reviewed for instruction injection vulnerabilities before shipping

> **Security is conditioning, not a feature.** Nobody asks for it. Nobody cheers when it passes. You will care deeply when production goes down because of something that would have taken 20 minutes to fix at sprint close.

---

## 1D: Change Request Intake

> The current sprint is locked. New requirements go on the queue. No exceptions.

When a new requirement arrives mid-sprint or between sprints:

**Step 1: Classify**
- Bug fix → goes into current sprint fix loop if sprint is in fix mode, or queued if sprint is in build mode
- Scope change to current sprint → rejected from current sprint, queued to next
- New feature → queued, elicited, slotted

**Step 2: Elicit (new features and scope changes only)**

Same CRISP pattern — pre-fill a strawman, present it, one round of corrections:

> "Got it. Here's what I think you're asking for: [pre-fill]. Is that right, or am I off?"

Then:
- What problem does this solve? (link to a goal in `docs/project-goals.md` or flag as new)
- Does it conflict with anything already specced or built?
- What's the rough effort? (T-shirt: XS/S/M/L/XL)
- Which sprint does this belong to?

**Step 3: Impact check**
- Does this change any acceptance criteria already locked in a completed sprint? → Flag immediately, do not silently revise locked specs
- Does this require a new AI Spec? → Create it before the sprint that builds it
- Does this add a new 3rd party integration? → Integration AI Spec required before build

**Step 4: Queue and confirm**
- Add to `crisp-state.json` under `change_requests[]`
- Confirm sprint slot with the human: "I'm slotting this to Sprint [N]. Correct?"
- Update `docs/initial-backlog.md` with the new item and sprint tag
- Continue current sprint unchanged

**The hard rule:** Current sprint scope is frozen from the moment it starts. No exceptions. Mid-sprint changes to scope are the #1 source of project chaos. The queue exists so nothing gets lost — not so changes get blocked forever.

---

## 1E: Sprint Delta Doc → `docs/sprint-[N]-delta.md`

Generate at every sprint close, before the human validates.

```markdown
# Sprint [N] Delta — [Date]

## Sprint Goal
[Goal from sprint-plan.md]

## What was specced vs what shipped

| US ID | Story | Specced | Shipped | Delta |
|---|---|---|---|---|
| US-01 | | ✅ | ✅ | None |
| US-02 | | ✅ | ❌ | [reason — slipped to Sprint N+1] |

## Scope that slipped
[List any stories that didn't ship, with reason and new sprint assignment]

## Change requests received this sprint
| Request | Classification | Slotted to | Notes |
|---|---|---|---|
| [description] | New feature / Scope change / Bug | Sprint N+1 | |

## Product gate result
✅ Passed / ❌ Failed — [findings if failed]

## Security gate result
✅ Passed / ❌ Failed — [Bearer findings, manual check results]

## Open items going into Sprint [N+1]
[List anything that needs attention before next sprint starts]
```

---

## 1F: Fix Loop

When a gate fails — product or security — do not close the sprint.

1. State the failure clearly: what failed, why, what needs to change
2. Claude Code fixes the specific failing criteria — scope limited to what failed
3. Re-run the gate that failed
4. If it passes: document in delta doc, close the sprint
5. If it fails again: escalate to human — something in the spec may need to change

> Do not patch your way through a failed security gate. A Critical finding is not a "note for later." It is a stop sign.

---

## 1F: Progress Report → `docs/sprint-[N]-report.md`

Generate after delta doc is complete and gates have passed. Two sections, one file.

---

### Section 1: Technical Snapshot
*(For you, the team, and Claude Code context)*

```markdown
## Technical Snapshot — Sprint [N]

**Status:** Complete / In progress / Blocked
**Sprint goal:** [one line]
**Date range:** [start → close]

### Delivery
- Acceptance criteria: [X/Y passed]
- Stories complete: [X/Y]
- Stories slipped: [list with reason]

### Gates
- Product gate: ✅ / ❌ [summary]
- Security gate: ✅ / ❌ [findings summary]
  - Bearer: [result]
  - Manual checks: [result]

### Change requests
- Received this sprint: [N]
- Queued to Sprint [N+1]: [list]

### Blockers / Open items
[Anything the next sprint needs to know]

### crisp-state.json at close
[Paste current state]
```

---

### Section 2: Stakeholder Report
*(Plain language — copy-paste this into an email or Notion)*

```markdown
## Project Update — [Project name] — [Date]

**Status:** 🟢 On track / 🟡 Slipping / 🔴 Blocked

### What we shipped this week
[Feature-level, business language. Not "implemented auth" — "Users can now log in and manage their account."]

### What's next
[Next sprint deliverables in plain terms — what will the client be able to do or see after next sprint]

### Decisions needed from you
[Anything blocked on stakeholder input — specific, not vague. If nothing, say so.]

### Change requests received
[Plain description of anything queued — "We received a request to add X. It's been added to Sprint N."]
```

> Review the stakeholder section before it goes anywhere. It is a draft, not an auto-send.

---

## Sprint Close Sequence

When both gates pass:

1. Generate `docs/sprint-[N]-delta.md`
2. Generate `docs/sprint-[N]-report.md`
3. Update `crisp-state.json`:
```json
{
  "sprints_complete": [..., N],
  "current_sprint": N+1,
  "gates": {
    "sprint_N": {
      "product": "passed",
      "security": "passed",
      "date": "YYYY-MM-DD"
    }
  }
}
```
4. Present stakeholder report section to human for review
5. Confirm: "Sprint [N] is closed. Ready to start Sprint [N+1]?"
6. On confirmation — open Sprint N+1, run 1A pre-conditions

---

## All Sprints Complete

When `crisp-state.json` shows all sprints in `sprints_complete` and no remaining items in backlog above the MVP line:

> "All MVP sprints are complete. Product and security gates passed for each. The project is ready for Phase P (Prove) — validation against your Phase R success metrics.
>
> Say 'Start Phase P' to close the loop."

Hand off to `../phase5-prove/SKILL.md`.

---

## Exit Checklist

**Per sprint:**
- [ ] Sprint AI Spec was locked before build started — no open questions
- [ ] All acceptance criteria explicitly tested — not assumed
- [ ] Product gate: all criteria ✅ or fix loop complete
- [ ] Security gate: Bearer ran, no unresolved Critical/High findings
- [ ] Security gate: manual checklist complete (secrets, auth, input validation, HTTPS, deps)
- [ ] Agent governance checked (if agents built or called)
- [ ] Prompt injection checked (if skills/prompts shipped)
- [ ] Change requests received, classified, and queued — none silently absorbed into current sprint
- [ ] Sprint delta doc generated → `docs/sprint-[N]-delta.md`
- [ ] Progress report generated → `docs/sprint-[N]-report.md`
- [ ] Stakeholder section reviewed before any external send
- [ ] `crisp-state.json` updated

**Full execution complete:**
- [ ] All MVP sprints closed with passing gates
- [ ] All change requests either shipped or explicitly queued to post-MVP
- [ ] Full delta and report trail exists — one per sprint
- [ ] Human has approved final sprint
- [ ] Handoff to Phase P confirmed
