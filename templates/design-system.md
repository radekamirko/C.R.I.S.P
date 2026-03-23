# Design System

**Project:** 
**Date:** 
**Author:** 
**Status:** Draft / Review / Approved
**Linked to:** phase1-problem-statement.md · phase3-user-journey-map.md

---

## Audience Fit Check

> Before any design decision is made, CRISP validates choices against the target user defined in Phase 1.
> If a design direction conflicts with the audience profile, flag it explicitly.

**Target user (from Phase 1):**  
_(e.g. "Health-conscious, late 30s+, already using wearables, data-literate, motivated by longevity")_

**Audience-design alignment check:**
- [ ] Visual style matches the emotional register of the target user (not too playful, not too clinical)
- [ ] Complexity level is appropriate — not dumbed down, not overwhelming
- [ ] References feel native to this user's world (tools they already use and trust)
- [ ] Tone of design supports the product's positioning (from Phase 1 problem statement)

> **Challenge rule:** If the client proposes a design direction that conflicts with the audience profile, surface the conflict explicitly before proceeding.
> e.g. "Your target user is a data-literate professional in their late 30s. The proposed playful, high-animation style is more typical of consumer wellness apps targeting 20s. Is that intentional?"

---

## Design Philosophy

_(One paragraph. What is the emotional and functional intent of this interface? How should it feel?)_

> Example: "The interface should feel like a trusted instrument — precise, calm, and intelligent. It earns attention through clarity, not decoration."

---

## Cognitive & Behavioral UX Principles

These principles govern every design decision in this project. Use as both a reference layer when making decisions and a checklist when reviewing screens.

### Cognitive Load & Efficiency

| Principle | What it means | How to apply |
|---|---|---|
| **Aesthetic-Usability Effect** | Visually pleasing = perceived as more usable | Invest in polish — it directly affects trust |
| **Fitts's Law** | Frequently-used actions should be large and close to interaction point | Primary CTAs are thumb-reachable and prominent |
| **Hick's Law** | More choices = slower decisions | Max 3–5 options per screen; hide secondary actions |
| **Miller's Law** | Working memory holds ~7 items (±2) | Chunk content into groups of 5–9 elements |
| **Tesler's Law** | Complexity must live somewhere — push it into the system | Never make the user do what the system can do |
| **Occam's Razor** | Simplest solution that achieves the goal | No feature or element without a job |
| **Doherty Threshold** | Respond within 400ms to sustain engagement | Show skeleton/loading state instantly; never blank |
| **Postel's Law** | Flexible inputs, strict outputs | Accept multiple input formats; output is always consistent |
| **Paradox of the Active User** | Users prefer action over reading instructions | Make first action obvious; skip onboarding walls |

### Visual Perception & Layout

| Principle | What it means | How to apply |
|---|---|---|
| **Jakob's Law** | Users expect familiar patterns | Match conventions of tools users already know |
| **Law of Proximity** | Close = related | Group related elements spatially |
| **Law of Similarity** | Same style = same category | Use consistent shape/color to reinforce grouping |
| **Law of Prägnanz** | The mind prefers simple, clear, symmetrical | Favor clean layouts; avoid visual noise |
| **Law of Uniform Connectedness** | Visually link related elements | Use lines, containers, or color to connect related UI |

### Behavior, Memory & Motivation

| Principle | What it means | How to apply |
|---|---|---|
| **Serial Position Effect** | First and last items are most memorable | Put key actions/info at start and end of flows |
| **Von Restorff Effect** | Distinctive elements are remembered | Make primary CTA visually unique — one per screen |
| **Zeigarnik Effect** | Unfinished tasks stick in memory | Show progress indicators, streaks, incomplete states |
| **Peak-End Rule** | Users judge an experience by its peak and its end | Design emotional high points and exit moments carefully |
| **Selective Attention** | Users notice what stands out | Use hierarchy, contrast, and whitespace to direct focus |
| **Working Memory** | Dense interfaces overwhelm | Progressive disclosure; show only what's needed now |
| **Mental Models** | Users apply prior expectations | Structure interactions the way users intuitively expect |
| **Pareto Principle** | 20% of features = 80% of value | Ruthlessly prioritize; surface the core loop first |
| **Parkinson's Law** | Work expands to fill time available | Use clear workflows and pacing cues to drive action |

---

## Screen Review Checklist

Use this for every screen before marking it complete.

**Cognitive load:**
- [ ] Fewer than 5 primary choices visible at once (Hick's Law)
- [ ] Related elements chunked — no isolated orphan items (Miller's Law)
- [ ] System handles complexity — user never has to hold state in their head (Tesler's Law)
- [ ] Every element has a clear job — nothing decorative for decoration's sake (Occam's Razor)

**Visual:**
- [ ] Primary action is visually dominant — one Von Restorff moment per screen
- [ ] Related elements are spatially grouped (Proximity)
- [ ] Visual consistency is maintained — same type of element looks the same (Similarity)
- [ ] Layout is clean, balanced, symmetrical (Prägnanz)

**Behavior:**
- [ ] Progress is visible if this is part of a flow (Zeigarnik)
- [ ] The first and last elements carry the most important content (Serial Position)
- [ ] Loading/response states exist — no blank screens (Doherty)
- [ ] Pattern matches what this user already knows from similar tools (Jakob)

---

## Design Language

### Visual Style
_(Describe the overall aesthetic direction)_

- **Mood:** _(e.g. precise, warm, clinical, calm, energetic)_
- **Reference tools/apps:** _(Tools or products this should feel adjacent to)_
- **What to avoid:** _(Styles that would conflict with the audience or positioning)_

### Color Palette

| Role | Name | Hex | Usage |
|---|---|---|---|
| Background | | | Primary canvas |
| Surface | | | Cards, panels |
| Primary | | | Key actions, highlights |
| Secondary | | | Supporting elements |
| Text primary | | | Body, headings |
| Text secondary | | | Labels, captions |
| Success | | | Confirmation states |
| Warning | | | Flags, caution |
| Error | | | Failures, alerts |
| Border | | | Dividers, containers |

**Dark mode:**
- [ ] Dark mode is required
- [ ] Light mode only
- [ ] Both

### Typography

| Role | Typeface | Weight | Size | Notes |
|---|---|---|---|---|
| Heading 1 | | | | |
| Heading 2 | | | | |
| Heading 3 | | | | |
| Body | | | | |
| Caption | | | | |
| Data/numbers | | | Prominent | _(if data-heavy product)_ |
| CTA / button | | | | |

**Typography principles:**
- _(e.g. "Numbers are the hero — large, high-contrast, dominant")_
- _(e.g. "Body text is always readable at arm's length — minimum 16sp")_

### Shape Language

- [ ] Rounded (approachable, consumer)
- [ ] Sharp (technical, precise)
- [ ] Hybrid — _(describe)_

**Border radius standard:** _(e.g. 8px cards, 24px buttons, fully rounded pills for tags)_

### Motion & Animation

- [ ] Static — no animation
- [ ] Micro-interactions only (feedback on tap, state changes)
- [ ] Expressive transitions (screen changes, loading moments)

**Motion principles:**
- _(e.g. "Fast and functional — max 200ms for feedback, 300ms for transitions")_
- _(e.g. "No animation that delays access to content")_
- _(e.g. "Respect reduce-motion OS setting")_

### Iconography

- **Style:** _(e.g. outline, filled, duotone)_
- **Library:** _(e.g. Lucide, SF Symbols, Phosphor, custom)_

### Spacing & Grid

- **Base unit:** _(e.g. 8px)_
- **Screen margins:** _(e.g. 16px / 24px)_
- **Card padding:** _(e.g. 16px)_
- **Section spacing:** _(e.g. 32px)_

---

## Visual References

> CRISP: Search for 2–4 visual references that match the design direction and audience profile defined above. Link them here. Challenge any client-provided references that conflict with the target user or product positioning.

| Reference | URL | What to take from it |
|---|---|---|
| | | |
| | | |
| | | |

**Client-provided references:**
_(Paste any references the client has suggested. Flag conflicts with audience below.)_

**Conflicts / challenges:**
_(Any references that don't fit the audience or positioning — explain why and suggest alternatives.)_

---

## Platform & Deliverables

**Platform:**
- [ ] iOS
- [ ] Android
- [ ] Web (responsive)
- [ ] Desktop
- [ ] Other: ___

**Deliverable format:**
- [ ] Figma file (hi-fi, tokenized)
- [ ] Described in this doc only (for AI builder)
- [ ] Lo-fi sketches / wireframes
- [ ] Other: ___

---

## Open Questions

- [ ] 
- [ ] 

---

## Notes for Claude Code
_(Specific implementation notes — token names, component conventions, library choices)_

