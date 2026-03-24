---
name: phase2-results
description: The Mileva Method (CRISP) — Phase 2: Results. Outcome alignment, stakeholder register, baseline measurement, success metrics, tradeoff negotiation. Use after problem definition is complete. Triggers on "results", "phase 2", "define success", "success metrics", "what does done look like", or after Phase C exit checklist is complete.
---

# R — Results: Outcome Alignment

> "We don't know if we succeeded unless we defined what success looks like before we started."

Do not discuss solutions or architecture until this phase is complete.

## Step 1: Stakeholder Register — Pre-fill, Elicit, Confirm

Do not open a blank register and ask "who are the stakeholders?" — you already have what you need to start.

**Pre-fill from existing docs:**

| Register section | Source |
|---|---|
| Primary users | `docs/problem-statement.md` — who the problem belongs to |
| Adjacent teams / employees | `docs/problem-statement.md` — business context, who touches the process |
| External users / customers | `docs/value-proposition-canvas.md` — customer profile (external projects) |
| Impact per stakeholder | `docs/problem-statement.md` — what changes for each group when the problem is solved |
| Human-in-the-loop zones | `docs/problem-statement.md` — constraints; `docs/swot.md` — threats (external) |

Draft the register, then work through it with three elicitation moves before confirming:

**Move 1 — Surface the hidden stakeholders**
> "Here's everyone I see being affected. [Primary user], [adjacent team], [sponsor]. Before we go further — who else touches this process, even occasionally? The person who only shows up when something goes wrong. The team that gets the output but has no say in the input."

People forget about downstream consumers, compliance reviewers, support staff. Get them on the register now.

**Move 2 — Challenge the impact ratings**
For each stakeholder, name the impact and let them push back:
> "I've marked [team X] as neutral — they're not doing the work differently, just receiving better output. Does that feel right, or are there ways this actually makes their life harder before it gets better?"

Neutral is often wrong. Changes create transition friction even when the end state is better. Flush that out.

**Move 3 — Elicit the HITL zones**
> "For each of these groups — where in this process would you be uncomfortable with a fully automated decision? Where does a human need to stay in the loop, even if the AI could technically handle it?"

Don't pre-fill HITL zones — let the client name them. Their discomfort is the signal, not your inference.

Confirm the completed register:
> "Here's the full picture. Does anything feel wrong before we lock this and move to baselines?"

Save to `docs/stakeholder-register.md`

---

## Step 2: Baseline Measurement

Measure the current state before anything is built. This is the "before" that Phase P will measure against.

- Time to complete the action
- Cost / money spent on process
- Error rate / rework frequency
- Frustration level (survey or 1-10 interview score)
- Tools used, open tabs, manual steps — the "friction inventory"

Pre-fill what you can from Phase C process walkthrough and constraints. Ask the client to fill any gaps:
> "I've estimated the current baseline at [X time / Y cost / Z errors]. Does that match your experience, or are you seeing different numbers?"

> If you can't measure the baseline, you can't prove the outcome.

---

## Step 3: Desired Projection

Define where metrics should land post-implementation.

Pre-fill with reasonable targets derived from:
- Phase C ROI / gains identified
- Market research benchmarks (external projects)
- Industry standards for the problem type

Then present:
> "Based on what you told me in Phase C, I'd expect this to get us to [X% improvement / Y time / Z cost]. Does that feel ambitious enough, or are you aiming higher?"

- Prefer relative metrics (% improvement) over absolute values
- Map second-order effects — one metric often has downstream impact
  > "Checkout <1min" → reduces cart abandonment → increases revenue
- Set both quantitative and qualitative targets

---

## Alignment Negotiation

Client sponsor speaks money and risk — use that language.
- Present tradeoffs explicitly: metric target ↑ = scope/budget/timeline ↑
- Flag human-in-the-loop zones proactively (legal, security, high-stakes)
- *"Everything is possible. Not everything is worth it. Here's what each option costs."*
- Iterate until aligned — do not proceed without sign-off

---

## Phase 2 Outputs

> Save before closing Phase R. These files are inputs to Phases I and S.

| File | Contents | Required? |
|---|---|---|
| `docs/stakeholder-register.md` | All impacted parties, their stakes, baseline metrics, success targets, HITL zones | Always |

> Baseline measurements and desired projections are captured inside `docs/stakeholder-register.md` — no separate file needed unless the project warrants a standalone metrics doc.

---

## Exit Checklist
- [ ] Stakeholder register pre-filled, elicited (3 moves), confirmed → `docs/stakeholder-register.md`
- [ ] Hidden stakeholders surfaced (downstream consumers, compliance, support)
- [ ] Impact ratings challenged — neutral validated, not assumed
- [ ] HITL zones elicited from client, not inferred
- [ ] Baseline measured across all key dimensions
- [ ] Desired projections defined — relative where possible
- [ ] Second-order impacts identified
- [ ] Tradeoffs presented and discussed
- [ ] Quant and qual success criteria agreed and signed off by client sponsor
