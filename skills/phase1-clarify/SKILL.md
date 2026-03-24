---
name: phase1-clarify
description: The Mileva Method (CRISP) — Phase 1: Clarify. Problem definition, eliciting, painkiller test, buy vs build, Go/No-Go. Use at the start of any AI implementation project. Triggers on "clarify", "phase 1", "start discovery", "define the problem", "what problem are we solving", or at the beginning of a new client engagement.
---

# C — Clarify: Problem Definition

Do not discuss technology, solutions, or tools until this phase is complete.

## The 3 Moves

**Move 1: Business Mirroring**
Reconstruct their core business or idea back at them until confirmed correct.
> "Okay, let me make sure I'm not about to solve the wrong problem — you do X, it works kind of like Y and Z, right? Tell me where I'm off."

**Move 2: Eliciting**
Suggest the ideal state — let them correct you into the real need.
> "So in a perfect world, X happens automatically, Y follows, nobody has to touch it — is that roughly the dream? Or am I undershooting?"
People react better than they originate. Corrections surface real pain faster than open questions.

**Move 3: Roleplay / Process Walkthrough**
Act as the user living the current process. Narrate it out loud step by step.
> "Walk me through it like I'm the new hire on day one. The underwriter opens what, clicks where, copies what into where... go."
Exposes friction they've become blind to.

**Move 4: Magic Wand**
Remove all constraints — budget, time, tech, team — and ask what they'd actually want.
> "Forget what's possible for a second. If you had a magic wand and could fix one thing in this business tomorrow, what would it be?"
Use this early, before they've started self-editing. The answer is almost always the real problem — or points directly at it. Then bring constraints back in and work backwards from there.

---

## Key Assessments

**Painkiller vs Multivitamin**
- Painkiller = costs them daily in time/money/risk → proceed
- Multivitamin = nice to have, life slightly better → deprioritize or kill

**Internal vs External**
- Internal: stakeholders, ROI measurement, employee ideal state
- External: competitors, TAM, USP → run Market Research + SWOT (see below)

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

Both sides must agree on this sentence before Phase C closes. If they can't agree on the sentence, they definitely can't agree on the solution.

---

## External Product Extensions (run after Internal vs External decision)

If the project is an **external product**, two additional steps are mandatory before Phase C closes:

### 1. Market Research → `skills/phase1-clarify/market-research.md`
Run full market research: TAM sizing, competitor mapping, feature standards (must-have vs differentiator vs gap), review mining (Reddit, G2, Product Hunt), USP gap analysis.
Output → `templates/market-research.md`

This feeds directly into:
- Phase R: success metrics (market context shapes what "good" looks like)
- Phase S: MVP baseline (competitor must-haves), backlog, USP

### 2. SWOT → `skills/phase1-clarify/swot.md`
Run after market research. Pre-fill S/W from problem statement and constraints. Pre-fill O/T from market research findings, competitor intelligence, and industry trends.
Elicit client input — let them correct, not originate.
Output → `templates/swot.md`

This feeds directly into:
- Phase R: risk flags, opportunity prioritization
- Phase S: positioning, MVP decisions

---

## Exit Checklist
- [ ] One-sentence problem statement agreed → `templates/problem-statement.md`
- [ ] Business context mirrored and confirmed
- [ ] Ideal desired state defined
- [ ] ROI / gains identified
- [ ] Internal vs external decided
- [ ] Constraints captured (budget, time, legal, scope, tech)
- [ ] Buy vs Build evaluated → `templates/buy-vs-build-matrix.md`
- [ ] **[External only]** Market research complete → `templates/market-research.md`
- [ ] **[External only]** Value Proposition Canvas → `templates/value-proposition-canvas.md`
- [ ] **[External only]** SWOT complete → `templates/swot.md`
- [ ] Go / No-Go called

**No-Go is a feature.** If a free tool solves it, say so. Lose the project, win the trust.
