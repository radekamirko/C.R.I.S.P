# Landing Page Brief

**Project:**
**Date:**
**Compiled from:** `docs/problem-statement.md`, `docs/value-proposition-canvas.md`, `docs/ux-discovery.md`, `docs/market-research.md`

---

> By the time you reach Phase S, everything needed for a landing page already exists in your docs.
> This brief compiles it into a ready-to-build page structure.
> Hand it to a developer or Claude Code and say: "Build this as a static landing page."

---

## Product Summary

**Product name:**
_(From project name)_

**One-sentence value prop:**
_(From `docs/value-proposition-canvas.md` — Pain Relievers + USP)_

**Who it's for:**
_(From `docs/stakeholder-register.md` — primary user, in plain language)_

**The problem it solves:**
_(From `docs/problem-statement.md` — one sentence, client-facing language)_

---

## Page Structure

### Hero Section

**Headline:**
_(Primary hook — the pain or the promise. Tension first. Product second.)_

> Draft:

**Subheadline:**
_(Who it's for + what it does for them — 1-2 sentences max)_

> Draft:

**Primary CTA:**
_(One action — sign up / get early access / book a demo / start free)_

> CTA text:
> CTA destination:

**Visual:**
_(What goes here — product screenshot, illustration, demo gif, none)_

---

### Problem Section

> Why this exists. Make the reader feel the pain before offering the solution.

**Section headline:**

**Pain points to show** _(from `docs/value-proposition-canvas.md` — Customer Pains)_:
1.
2.
3.

---

### Solution / Features Section

> 3-4 features max. Each one maps to a pain or a gain. No feature lists — benefits only.

**Section headline:**

| Feature | Benefit (what it does for the user) | Source doc |
|---|---|---|
| | | `docs/value-proposition-canvas.md` — Gain Creators |
| | | |
| | | |

---

### Social Proof / Trust Section

_(Leave blank until available — do not fake this)_

**Type:** Testimonials / logos / case study / metrics
**Content:**

---

### Target Audience Section _(optional)_

> Use if the product serves a specific niche that needs to self-identify.

**"Built for..." statement:**
_(From `docs/stakeholder-register.md` + `docs/market-research.md`)_

---

### Pricing / Access Section _(if applicable)_

**Model:** Free / Freemium / Paid / Early access / Waitlist

**Pricing tiers:**
_(If decided — or "Coming soon" / "Join the waitlist")_

---

### Final CTA Section

**Headline:**
**CTA text:**
**Supporting line:** _(e.g. "No credit card required" / "Free 14-day trial")_

---

## Visual Direction

_(From `docs/ux-discovery.md` — 3B Visual Direction)_

**Tone:** _(e.g. fast, warm, trustworthy, premium, minimal)_
**Non-negotiable feeling:**
**Reference apps/sites:**
**Avoid:**

**Color palette:**
_(From `docs/design-system.md` if complete — otherwise from ux-discovery)_

**Typography:**

---

## SEO Basics

**Primary keyword:**
**Page title tag:** _(max 60 chars)_
**Meta description:** _(max 155 chars)_

---

## Build Notes for Claude Code

- Static page — no backend required unless capturing emails/signups
- If capturing emails: use a form service (Mailchimp, ConvertKit, Loops, Resend) — do not build a custom backend for MVP
- Mobile-first — design and test at 375px before desktop
- Page must load under 3 seconds — no heavy libraries
- CTA above the fold on both mobile and desktop
- Analytics: fire `page_view` on load + `cta_clicked` on every CTA button — see `docs/analytics-spec.md`
