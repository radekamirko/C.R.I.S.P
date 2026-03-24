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

Capture answers in the template. Mark everything as `[client-stated]` — assumptions until proven otherwise.

---

## Track 2: Independent Web Research

Do not skip this. Client assumptions are often wrong, outdated, or conveniently optimistic.

### 2a. TAM Sizing
- Search: "[industry] market size [year]" — find a credible number (Statista, McKinsey, industry reports)
- Find: total market → serviceable segment → realistic target
- Note the source and year — "it's a big market" is not a number

### 2b. Competitor Mapping
Search: "[problem space] software", "[problem space] tool", "[problem space] platform", "best [problem space] tools [year]"

For each competitor found:
- Category: Direct (same problem, same audience) / Indirect (same problem, different approach or audience)
- Role: Market Leader / Challenger / Niche Player / New Entrant
- Pricing model (if visible)
- Stated USP (what do they claim to be?)
- Feature set (scan their website, pricing page, feature list)

### 2c. Industry Feature Standards
From competitor feature lists — identify:
- **Must-have:** 3+ competitors have it → table stakes, users expect it, not having it is embarrassing
- **Differentiator:** 1-2 competitors have it → potential edge
- **Gap:** nobody does it well → opportunity worth exploring

### 2d. Review Mining
Sources to check (search: "site:reddit.com [competitor name]", "[competitor] review g2", etc.):
- Reddit (relevant subreddits, search competitor names — people are brutally honest here)
- G2 / Capterra (read the 1-star AND 3-star reviews — 5-stars are useless, 1-stars are emotional, 3-stars are gold)
- Product Hunt (comments section, not just vote count)
- Glassdoor (optional — internal chaos often shows up as product chaos)
- App Store / Play Store (if mobile)

What to look for:
- Repeated complaints = unmet need = your opportunity
- Features users rave about = match or beat them
- Onboarding/support complaints = often fixable with better UX or a well-placed AI agent

### 2e. Positioning Gap
After research: where is the white space nobody's standing in?
- What pain is underserved?
- What audience is being ignored?
- What approach hasn't been tried?
- What's the one sentence that positions this differently from everything else?

---

## Synthesis

Pre-fill `templates/market-research.md` with everything found.
Present to client. Don't ask open questions — give them something to react to:

> "Here's what I found. [X] is the clear market leader, [Y] is coming up fast, and the main gap nobody's closing is [Z]. Does that match your read, or am I missing something?"

Their corrections are signal. Write them down.

---

## Exit Checklist
- [ ] TAM estimated (with source — not a vibe)
- [ ] 3+ competitors mapped (direct + indirect)
- [ ] Market leader and challenger identified
- [ ] Industry feature standards documented (must-have vs differentiator vs gap)
- [ ] Review mining done (min 2 sources)
- [ ] At least one unmet need identified from reviews
- [ ] USP / positioning recommendation drafted
- [ ] Client has confirmed or corrected the research
- [ ] Output saved to `templates/market-research.md`

**Hand off to:** Phase C SWOT (`skills/phase1-clarify/swot.md`) — feed this research directly in.
