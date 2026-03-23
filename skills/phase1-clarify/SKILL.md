---
name: phase1-clarify
description: The Mileva Method (CRISP) — Phase 1: Clarify. Problem definition, eliciting, painkiller test, buy vs build, Go/No-Go. Use at the start of any AI implementation project. Triggers on "clarify", "phase 1", "start discovery", "define the problem", "what problem are we solving", or at the beginning of a new client engagement.
---

# C — Clarify: Problem Definition

Do not discuss technology, solutions, or tools until this phase is complete.

## The 3 Moves

**Move 1: Business Mirroring**
Reconstruct their core business or idea back at them until confirmed correct.
> "So just to make sure we're on the same page — you do X, which is similar to Y and Z, right?"

**Move 2: Eliciting**
Suggest the ideal state — let them correct you into the real need.
> "So ideally you'd want X to happen automatically, then Y follows — is that right?"
People react better than they originate. Corrections surface real pain faster than open questions.

**Move 3: Roleplay / Process Walkthrough**
Act as the user living the current process. Narrate it out loud step by step.
> "So the underwriter asks 12 questions, fills the form, submits it, does the math manually — is that right?"
Exposes friction they've become blind to.

---

## Key Assessments

**Painkiller vs Multivitamin**
- Painkiller = costs them daily in time/money/risk → proceed
- Multivitamin = nice to have, life slightly better → deprioritize or kill

**Internal vs External**
- Internal: stakeholders, ROI measurement, employee ideal state
- External: competitors, TAM, USP, Value Proposition Canvas

**Constraints Capture**
- Budget, Time, Legal/Compliance, Scope, Technical stack
- Constraints direct architecture — capture before any solution talk

**Buy vs Build**
- Tool solves it for $50/month? → Buy it
- Needs config on top of existing tools? → Configure it
- Genuinely needs custom? → Build it
- Deliverable: one-page matrix → `templates/buy-vs-build-matrix.md`

---

## The One Sentence
> "Currently, [who] are spending [cost/time/money] doing [thing] because [root cause]."

Both sides must agree on this sentence before Phase C closes.

---

## Exit Checklist
- [ ] One-sentence problem statement agreed → `templates/problem-statement.md`
- [ ] Business context mirrored and confirmed
- [ ] Ideal desired state defined
- [ ] ROI / gains identified
- [ ] Internal vs external decided → VPC if external: `templates/value-proposition-canvas.md`
- [ ] Constraints captured (budget, time, legal, scope, tech)
- [ ] Buy vs Build evaluated → `templates/buy-vs-build-matrix.md`
- [ ] Go / No-Go called

**No-Go is a feature.** If a free tool solves it, say so. Lose the project, win the trust.
