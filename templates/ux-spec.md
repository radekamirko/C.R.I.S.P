# UX Spec

**Project:** 
**Date:** 
**Author:** 
**Status:** Draft / Review / Approved
**Linked to:** design-system.md · phase3-user-journey-map.md · phase4-ai-spec.md

---

## Part 1 — Sitemap

> Full screen hierarchy for the product. Define every screen and its place in the navigation structure before speccing individual flows.

```
App
├── Auth
│   ├── Login
│   └── Sign Up
├── Onboarding
│   ├── Screen 1
│   ├── Screen 2
│   └── ...
├── [Tab / Section 1]
│   ├── Screen
│   └── Screen
├── [Tab / Section 2]
│   └── ...
└── [Settings / Profile]
    └── ...
```

**Navigation pattern:**
- [ ] Tab bar (bottom nav)
- [ ] Drawer / sidebar
- [ ] Stack only
- [ ] Hybrid — _(describe)_

---

## Part 2 — Flow Specs

> One section per critical user flow. A flow is a sequence of screens the user moves through to complete a goal.
> Write flows before individual screens — flows reveal the intent; screens are the implementation.

---

### Flow: [Name]

**User goal:** _(What is the user trying to accomplish?)_
**Entry point:** _(Where does this flow start?)_
**Exit point:** _(Where does it end — what has changed for the user?)_
**Trigger:** _(What causes the user to enter this flow?)_

**Flow map:**
```
[Entry] → Screen A → Screen B → Screen C → [Exit / outcome]
         ↓ (error)
         Screen A (error state)
```

**Success state:** _(What does success look like for the user at the end?)_
**Failure / fallback:** _(What happens if something goes wrong mid-flow?)_

**Cognitive UX notes for this flow:**
- _(e.g. "Serial Position: put the goal reminder at step 1 and the confirmation at the final step")_
- _(e.g. "Zeigarnik: show a progress bar — 3 of 5 steps complete")_
- _(e.g. "Paradox of the Active User: step 1 must have one obvious action, no intro text walls")_

---

## Part 3 — Screen Specs

> One section per screen. Only write screen specs for screens that need design direction.
> Simple screens (e.g. a success confirmation) can be noted briefly.

---

### Screen: [Name]

**Parent flow:** _(Which flow does this screen belong to?)_
**Purpose:** _(One sentence — what does this screen do for the user?)_
**Entry from:** _(Previous screen or trigger)_
**Exit to:** _(Next screen(s) — including edge cases)_

---

**Information Architecture**

| Priority | Content element | Type | Notes |
|---|---|---|---|
| 1 (hero) | | Heading / data / image / CTA | The dominant element — one per screen |
| 2 | | | |
| 3 | | | |
| Supporting | | | Secondary info, labels, metadata |

**Layout notes:**
_(Describe the visual hierarchy — what is at the top, middle, bottom? What is dominant? What is de-emphasized?)_

---

**UI Elements**

| Element | Type | Label / content | Action on tap/interact | Notes |
|---|---|---|---|---|
| | Button / input / card / list / toggle / nav | | | |
| | | | | |

---

**States**

| State | Trigger | What changes |
|---|---|---|
| Default | Screen loads | _(normal state)_ |
| Loading | Data fetch in progress | _(skeleton / spinner)_ |
| Empty | No data yet | _(empty state message + CTA)_ |
| Error | API fail / validation fail | _(error message + retry)_ |
| Success | Action completed | _(confirmation / transition)_ |

---

**User Actions**

| Action | Trigger | Result |
|---|---|---|
| Primary | Tap [CTA] | _(what happens)_ |
| Secondary | Tap [secondary action] | _(what happens)_ |
| Dismiss / back | Swipe / back button | _(where does user go)_ |
| Edge case | _(describe)_ | _(what happens)_ |

---

**Cognitive UX checklist for this screen**
- [ ] One dominant action (Von Restorff — primary CTA is visually unique)
- [ ] Fewer than 5 choices visible (Hick's Law)
- [ ] Related elements grouped (Proximity)
- [ ] Progress visible if part of a flow (Zeigarnik)
- [ ] Loading state defined — no blank screen (Doherty ≤400ms)
- [ ] Matches user's mental model — familiar pattern (Jakob's Law)
- [ ] No complexity pushed onto the user (Tesler's Law)

---

**Visual references**
_(Links to specific screens from products that capture the right direction for this screen)_

| Reference | URL | What to take from it |
|---|---|---|
| | | |

---

**Notes for Claude Code**
_(Component names, specific implementation notes, library references)_

---

_[Duplicate Part 3 section for each additional screen]_

---

## Open Questions

- [ ] 
- [ ] 
