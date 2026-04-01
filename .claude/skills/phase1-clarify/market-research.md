---
name: market-research
description: CRISP Phase 1 (Clarify) — Market Research. TAM sizing, competitor mapping, review mining, USP gap analysis. Run this when the project is an external product. Triggers on "market research", "competitors", "TAM", "who else does this", "find the edge", or when Phase C identifies the project as external-facing.
---

# Market Research — Phase C Extension

Run this only for **external products**. Internal tooling → skip.

Two tracks. Run both. Neither replaces the other.

---

## Track 1: Client Elicitation

Elicit what they already know. Treat their answers as hypotheses, not facts — you'll validate everything independently.

> "Before I go digging myself — who do you think your main competitors are? And be honest, not just the ones you like to compare yourself to."

> "If someone is solving this problem today without you, what are they using? Even if it's a spreadsheet and a prayer."

> "Who's the market leader right now — the one everyone defaults to? And who's the scrappy one coming up behind them?"

> "What do you think you do better than all of them? And don't say 'customer service' — everyone says that."

> "Have you read any reviews of competitors — G2, Reddit, App Store? Anything that stuck with you?"

> "What do you think customers hate most about existing solutions? That's usually where the money is."

Also establish the target geography early — it shapes the entire research pass:
> "Who are we building this for, geographically? Is this a global product, or are we focused on a specific country or region first?"

Capture answers in the template. Mark everything as `[client-stated]` — assumptions until proven otherwise.

---

## Track 2: Independent Web Research

Do not skip this. Client assumptions are often wrong, outdated, or conveniently optimistic.

### 2a. TAM Sizing
- Search: "[industry] market size [year]" — find a credible number (Statista, McKinsey, industry reports)
- Find: total market → serviceable segment → realistic target
- Note the source and year — "it's a big market" is not a number
- If the target market is regional, find regional market size too — "global TAM = €50B" is useless if you're launching in Italy

### 2b. Global Competitor Mapping
Search: "[problem space] software", "[problem space] tool", "[problem space] platform", "best [problem space] tools [year]"

For each competitor found:
- Category: Direct (same problem, same audience) / Indirect (same problem, different approach or audience)
- Role: Market Leader / Challenger / Niche Player / New Entrant
- Pricing model (if visible)
- Stated USP (what do they claim to be?)
- Feature set (scan their website, pricing page, feature list)
- Geographic presence — do they operate in the target region? Local language support? Local pricing?

### 2b-ii. Regional / Local Competitor Pass

> Run this whenever the target market is a specific country or region. A product launching in Italy competes with Italian alternatives first — Salesforce is a threat, but the local CRM used by 60% of Italian SMBs is a bigger one.

**Step 1 — Establish the target region**
If not already confirmed in Track 1, lock it now:
> "Before I go deeper — are we thinking global from day one, or is there a primary country or region we're targeting first? I want to make sure I'm finding the right competitors."

**Step 2 — Local competitor search**
Search: "[problem space] [country/region]", "best [problem space] [country] [year]", "[problem space] software [language of target market]"

Also search in the local language if applicable — many regional competitors don't rank in English.

For each local competitor found, capture the same fields as 2b, plus:
- Local market share or name recognition (if findable)
- Language and localisation quality
- Local integrations (local payment providers, local ERPs, local government APIs if relevant)
- Regulatory compliance specific to that region (GDPR, local tax rules, etc.)

**Step 3 — Check global players for local presence**
For every global competitor identified in 2b, check:
- Do they have a [country] landing page or pricing in local currency?
- Do they have local language support?
- Are they actively marketed in that region?

A global player with no local presence, no local language, and no regional pricing is a much weaker competitor than their brand suggests. Note this — it's often your opening.

**Step 4 — Synthesise regional vs global competitive landscape**

| Competitor | Type | Global / Local | Local presence? | Main threat |
|---|---|---|---|---|
| | Direct/Indirect | Global/Local | Yes/No/Partial | |

> The question isn't just "who exists?" — it's "who does the customer in [region] actually know about and trust?"

### 2c. Industry Feature Standards
From competitor feature lists — identify:
- **Must-have:** 3+ competitors have it → table stakes, users expect it, not having it is embarrassing
- **Differentiator:** 1-2 competitors have it → potential edge
- **Gap:** nobody does it well → opportunity worth exploring

Note if any must-have features differ between global and local competitors — regional products sometimes skip features that global tools treat as table stakes, or add region-specific ones (e.g. local invoice formats, specific payment rails).

### 2d. Review Mining
Sources to check (search: "site:reddit.com [competitor name]", "[competitor] review g2", etc.):
- Reddit (relevant subreddits, search competitor names — people are brutally honest here)
- G2 / Capterra (read the 1-star AND 3-star reviews — 5-stars are useless, 1-stars are emotional, 3-stars are gold)
- Product Hunt (comments section, not just vote count)
- Glassdoor (optional — internal chaos often shows up as product chaos)
- App Store / Play Store (if mobile)
- **Local review sources** — Trustpilot local, local tech forums, Facebook groups in the target language

What to look for:
- Repeated complaints = unmet need = your opportunity
- Features users rave about = match or beat them
- Onboarding/support complaints = often fixable with better UX or a well-placed AI agent
- **Regional complaints** — "doesn't support [local payment method]", "no [language] support", "pricing doesn't work for [country] businesses" — these are gifts

### 2e. Positioning Gap
After research: where is the white space nobody's standing in?
- What pain is underserved?
- What audience is being ignored?
- What approach hasn't been tried?
- What's the one sentence that positions this differently from everything else?
- **Is there a regional gap?** Global tools often ignore local nuance. Local tools are often outdated. The gap between "built for everyone" and "built for [region]" is frequently wide open.

---

## Synthesis

Pre-fill `templates/market-research.md` with everything found.
Present to client. Don't ask open questions — give them something to react to:

> "Here's what I found. Globally, [X] is the clear market leader and [Y] is coming up fast. Locally in [region], [Z] dominates — but they're [weakness]. The gap nobody's closing is [specific opportunity]. Does that match your read, or am I missing something?"

Their corrections are signal. Write them down.

---

## Exit Checklist
- [ ] TAM estimated (with source — not a vibe)
- [ ] Target geography confirmed with client
- [ ] 3+ global competitors mapped (direct + indirect)
- [ ] Market leader and challenger identified
- [ ] **[Regional target]** Local competitor pass done — searched in local language if applicable
- [ ] **[Regional target]** Global competitors checked for local presence
- [ ] **[Regional target]** Regional vs global competitive landscape synthesised
- [ ] Industry feature standards documented (must-have vs differentiator vs gap)
- [ ] Review mining done (min 2 sources — include local sources if regional)
- [ ] At least one unmet need identified from reviews
- [ ] USP / positioning recommendation drafted — regional angle considered
- [ ] Client has confirmed or corrected the research
- [ ] Output saved to `docs/market-research.md`

**Hand off to:** Phase C SWOT (`swot.md`) — feed this research directly in.
