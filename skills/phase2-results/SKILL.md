---
name: phase2-results
description: The Mileva Method (CRISP) — Phase 2: Results. Outcome alignment, stakeholder register, baseline measurement, success metrics, tradeoff negotiation. Use after problem definition is complete. Triggers on "results", "phase 2", "define success", "success metrics", "what does done look like", or after Phase C exit checklist is complete.
---

# R — Results: Outcome Alignment

> "We don't know if we succeeded unless we defined what success looks like before we started."

Do not discuss solutions or architecture until this phase is complete.

## Step 1: Stakeholder Register — Pre-fill and Confirm

Do not open a blank register and ask "who are the stakeholders?" — you already have what you need.

**Pre-fill from existing docs:**

| Register section | Source |
|---|---|
| Primary users | `docs/problem-statement.md` — who the problem belongs to |
| Adjacent teams / employees | `docs/problem-statement.md` — business context, who touches the process |
| External users / customers | `docs/value-proposition-canvas.md` — customer profile (external projects) |
| Impact per stakeholder | `docs/problem-statement.md` — what changes for each group when the problem is solved |
| Human-in-the-loop zones | `docs/problem-statement.md` — constraints; `docs/swot.md` — threats (external) |

Pre-fill the full register, then present it:
> "Here's everyone I see being affected by this. [Primary user] is the main one — this changes [X] for them. [Adjacent team] gets [better/worse/neutral] because [Y]. Does this feel complete, or is there a group I'm missing?"

Add anyone they flag. If they struggle to think of more — good, the list is probably right.

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
- [ ] Stakeholder register pre-filled from Phase C docs, confirmed with client → `docs/stakeholder-register.md`
- [ ] Baseline measured across all key dimensions
- [ ] Desired projections defined — relative where possible
- [ ] Second-order impacts identified
- [ ] Human-in-the-loop zones flagged
- [ ] Tradeoffs presented and discussed
- [ ] Quant and qual success criteria agreed and signed off by client sponsor
