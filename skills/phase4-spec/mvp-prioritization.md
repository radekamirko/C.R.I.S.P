---
name: mvp-prioritization
description: CRISP Phase 4 (Spec) — MVP vs Post-MVP feature prioritization using HVLE (High Value Low Effort) scoring. Defines MVP baseline, scores all other features against weighted business value criteria, applies effort sizing, and draws the MVP line. Triggers on "MVP", "prioritization", "what goes in MVP", "feature list", "HVLE", or after the initial backlog is drafted.
---

# MVP Prioritization — Phase S

Run this after the initial backlog is drafted and market research is complete.
Input required: competitor feature standards, USP, problem statement, project goals, stakeholder register.

---

## Step 1: MVP Baseline (Non-Negotiable)

Before any scoring, lock the baseline. These features bypass HVLE entirely — they're not up for debate.

**MVP Baseline = Must-Haves + USP**

### Must-Haves (table stakes)
Pull from `templates/market-research.md` → Feature Standards → Must-Have column.
Every competitor has these. Users expect them. Not having them isn't bold — it's just incomplete.

> "These are the things every player in this space has. We're not getting points for building them, but we'll lose points for missing them. They go in MVP, full stop."

### USP Features
Pull from `templates/market-research.md` → USP Recommendation.
This is the reason someone picks you over the alternative. If it's not in MVP, what exactly are you launching?

> "Our edge is [USP]. Anything that directly delivers that goes in MVP — that's the whole point."

Lock these. Do not score them. Mark as `MVP-BASELINE` in the template.

---

## Step 2: Business Value Criteria

Elicit up to 5 criteria that define what "valuable" means for this specific project.

**For external SaaS / products:**
- Customer acquisition
- User activation / adoption
- Retention / engagement
- Revenue generation
- Referral / virality

**For internal tools:**
- Cross-company process adoption
- Time saved per user per week
- Error / rework reduction
- Employee satisfaction
- Compliance / risk reduction

Pre-fill 3-4 based on context, then:
> "I've assumed the outcomes that matter most here are [X, Y, Z]. Does that feel right, or am I optimizing for the wrong thing?"

**Max 5 criteria. If they want more, help them consolidate — more than 5 and everything starts scoring the same.**

### Weighting
Once criteria are agreed:
> "Now give each one a weight from 1 to 3. Think of it as: 3 = if we nail this, everything else follows. 1 = nice to track, but it's not what this lives or dies on."

Record the weights. They multiply every score — so getting them right matters.

---

## Step 3: Feature Scoring

For each feature in the backlog (excluding MVP-BASELINE items):

**Business Value Score:**
- Score each feature against every criterion: 1–5
  - 5 = this directly and strongly drives the outcome
  - 3 = it contributes, but it's not the whole story
  - 1 = barely connected, we're reaching
- Weighted score per criterion = score × weight
- Total Business Value Score = Σ(weighted scores)

**Effort (T-shirt sizing):**

| Size | Days | Effort Value |
|---|---|---|
| XS | < 1 day | 0.5 |
| S | 1–2 days | 1.5 |
| M | 3–5 days | 4 |
| L | 7–10 days | 8.5 |
| XL | 10+ days | 12 |

**Priority Score = Business Value Score ÷ Effort Value**
Higher = do it sooner.

---

## Step 4: Dependency Overrides

After scoring, check for dependencies — scoring alone doesn't know that B can't exist without A.

> "Feature [X] scored lower on its own, but [Y] sits on top of it — so [X] moves into MVP as a dependency. We don't get a choice here."

Mark blockers explicitly. Adjust the MVP line to include all required foundations.

---

## Step 5: Draw the MVP Line

Sort features by Priority Score (descending). Layer in: MVP-BASELINE first, then scored features high→low, with dependencies resolved.

> "Here's the ranked list. I'd draw the line here — everything above ships in MVP. Before you agree, ask yourself: can someone actually use this and get value from it? Does it deliver our USP? Can we build it in the time we have?"

If the answer to any of those is no — something's either missing or the scope is too big.

**The three questions before confirming the line:**
- Can a user complete the core job-to-be-done with MVP features only?
- Does MVP deliver the USP?
- Is MVP buildable within the agreed timeline?

All three must be yes. Otherwise, adjust.

---

## Step 6: Tag and Hand Off

Tag every feature:
- `MVP-BASELINE` — table stakes or USP, non-negotiable
- `MVP` — scored, above the line
- `POST-MVP` — scored, below the line (not never — just not now)
- `DEPENDENCY` — lower score but required by an MVP feature

Hand off to:
- `templates/mvp-prioritization.md` — scoring output
- `templates/initial-backlog.md` — update with tags
- `templates/sprint-plan.md` — MVP features drive sprint 1+

---

## Exit Checklist
- [ ] MVP baseline locked (must-haves + USP features identified)
- [ ] Business value criteria defined (max 5) and weighted (1–3)
- [ ] All backlog features scored (1–5 per criterion)
- [ ] Effort sized for every feature (XS/S/M/L/XL)
- [ ] Priority scores calculated
- [ ] Dependencies mapped and overrides applied
- [ ] MVP line drawn and validated with client (all 3 questions answered yes)
- [ ] Backlog updated with MVP / Post-MVP / Dependency tags
- [ ] Output saved to `templates/mvp-prioritization.md`
