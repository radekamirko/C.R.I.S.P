---
name: phase3-investigate
description: The Mileva Method (CRISP) — Phase 3: Investigate. Process mapping for existing or greenfield processes, user journey mapping, UX discovery, project goals. Use after outcome alignment. Triggers on "investigate", "phase 3", "map the process", "process mapping", "user journey", "as-is process", or after Phase R exit checklist is complete.
---

# I — Investigate: Process Understanding

Map what exists (or what should exist) before designing a solution.

## Two Tracks

### Track A: Existing Process (Automation)
Shadow the actual person doing the work. Step by step, no skipping.
- What tool is open at each step?
- What is copied, pasted, where does it go?
- What decisions are made manually and why?
- Where do errors happen? Where do things slow down?
- Every tab, every click, every "and then I just..."

> Goal: expose the real process, not the documented one. They are always different.

### Track B: New Process (Greenfield)
Design one step at a time:
- Input parameters — what comes in?
- Goal of the step — what is it trying to achieve?
- Output parameters — what comes out?
- Big picture first → zoom into each step

---

## Deliverable 1: Process / Flow Diagram

Map every step visually. Tool doesn't matter — draw.io, Figma, Miro, pen and paper.
Save to `docs/process-flow.md`.

---

## Deliverable 2: User Journey Map — Pre-fill and Confirm

Do not build this from scratch in the client session. Pre-fill from what you already know, then walk through it together.

**Pre-fill from existing docs:**

| Journey section | Source |
|---|---|
| User types | `docs/stakeholder-register.md` — primary and secondary users |
| Core steps | `docs/problem-statement.md` — the process being changed; Phase C process walkthrough |
| Needs per step | `docs/problem-statement.md` — desired outcome, ideal state |
| Pain points | `docs/problem-statement.md` — root cause, friction inventory from Phase C walkthrough |
| Feelings | Infer from pain points and context — frustration where friction is high, relief at resolution |
| Moments of delight | `docs/value-proposition-canvas.md` — gain creators (external); implied by what the solution fixes |

Draft a complete journey map per user type, then walk it with the client step by step:
> "I've mapped the [user type] journey based on what we've discussed. Step 1 is [X] — they're trying to [goal], and right now the friction is [pain]. Does that match what you see?"

Move through each step. Correct where they push back. Add steps they identify. Mark delight moments explicitly — they become design priorities.

Save to `docs/user-journey-map.md`

---

## Deliverable 3: Project Goals — Pre-fill and Confirm

Goals are not invented in Phase I — they are derived from what's already been agreed. Pre-fill everything, then confirm.

**Pre-fill from existing docs:**

| Goals section | Source |
|---|---|
| Goals | `docs/stakeholder-register.md` — success targets and desired projections |
| Non-goals | `docs/problem-statement.md` — scope constraints, what was explicitly ruled out |
| Success criteria | `docs/stakeholder-register.md` — quant and qual metrics agreed at Phase R sign-off |

Draft the full goals doc, then present it:
> "Based on everything we've aligned on, I see three things this project must achieve: [1], [2], [3]. Non-goals are [X and Y] — we agreed those are out of scope. And success looks like [metric] by [timeframe]. Does that capture it, or is something missing?"

Do not reopen the negotiation on success criteria — that was Phase R. If they want to change a metric now, note it, surface the tradeoff, and ask for explicit sign-off before updating.

Save to `docs/project-goals.md`

---

## UX Discovery — Mandatory for External Products (UI/Mobile/Web)

> Run this after user journey maps are complete, before closing Phase I.
> Phase S will write the UX spec and design system from these inputs. If you skip this, Phase S has nothing to work from and will either guess or stall.

This is a conversation, not a form. Pre-fill what you can from context, then let the client correct.

---

### 3A: Audience & Mental Model

You already have user types from `docs/stakeholder-register.md`. Now go one level deeper.

For each primary user type, ask:
> "When [user type] opens this app for the first time — what's the app they think of? What does familiar feel like to them?"

You're not asking what they want to copy. You're mapping the mental model the design must meet or consciously break.

Also establish:
- Age range and tech comfort level
- Use context: on the move, desktop, low attention, high stress?
- Is speed the priority, or clarity, or trust?

Pre-fill a hypothesis, then:
> "I'm picturing [user type] as someone who [context]. Does that match who you're building for, or am I off?"

---

### 3B: Visual Direction

Do not ask "what should it look like?" — that gets you nothing useful. Use references and reactions instead.

**Step 1: Propose a direction**
Based on the product category and user type, name 2–3 apps or products the design should feel adjacent to — not copy, but share the emotional register of.

> "For the [user type] flow — given it's [context] and needs to feel [quality] — I'm thinking something in the direction of [App A] or [App B]. Does that resonate, or does it feel wrong?"

**Step 2: Capture any client-provided references**
If they have references, take them. Then ask:
> "These are great starting points. Is there anything about these you'd specifically want to avoid — a vibe, a colour, a layout pattern that doesn't feel right for your audience?"

**Step 3: Identify one non-negotiable**
> "If there's one thing the design absolutely must feel — fast, warm, trustworthy, premium, approachable — what is it? Pick one."

Record all of this. It will feed `docs/design-system.md` directly.

---

### 3C: Navigation Pattern

Establish the navigation model before any screens are drawn.

Present the options with context:
> "There are a few standard patterns here. Tab bar (bottom nav) works well when users switch between 2–4 core areas frequently. Stack-only works for linear flows — think onboarding or checkout. Drawer/sidebar suits apps with many sections. Which one fits how users will actually move through this?"

If the product has distinct user roles, ask:
> "Do these user types see different navigation entirely, or the same shell with different content?"

Record the decision. This is the navigation contract — Phase S builds the sitemap from it.

---

### 3D: Key Screen Identification

You already have the critical flows from the user journey map. Now identify which screens carry the most weight.

> "Looking at the journey map — which 2 or 3 screens does everything hinge on? The one where users decide to stay or leave. The one where the product either earns trust or loses it."

For each high-stakes screen identified:
- What emotion should the user feel here?
- What is the single most important action on this screen?
- What's the biggest risk of getting it wrong?

This feeds the cognitive UX prioritisation in Phase S screen specs.

---

### 3E: Friction & Delight Inventory

Pull from the user journey map — moments of pain and moments of delight are already mapped.

Now make them design-actionable:

For each pain point:
> "This step causes friction. What would make it disappear — simplification, automation, better feedback, trust signal?"

For each delight moment:
> "This is where users feel good. How do we amplify it — animation, confirmation, a small reward moment?"

Record the answers. They become UX notes in the screen specs.

---

## Phase 3 Outputs

> Save all of these to `docs/` before closing Phase I.

| File | Contents | Required? |
|---|---|---|
| `docs/process-flow.md` | Full process map — every step, tool, input, output, decision | Always |
| `docs/user-journey-map.md` | Journey per user type — steps, needs, feelings, pain points, delights | Always |
| `docs/project-goals.md` | Goals, non-goals, success criteria linked to Phase R metrics | Always |
| `docs/ux-discovery.md` | Audience mental models, visual direction, navigation pattern, high-stakes screens, friction/delight | External UI/Mobile/Web only |

---

## Exit Checklist
- [ ] Process fully mapped (Track A or B) → `docs/process-flow.md`
- [ ] Every tool, input, output, and decision point documented
- [ ] User journey map pre-filled from prior phases, confirmed with client → `docs/user-journey-map.md`
- [ ] Needs / feelings / actions mapped across journey
- [ ] Project goals pre-filled from Phase R outputs, confirmed with client → `docs/project-goals.md`
- [ ] Diagrams drawn and shared with client for confirmation
- [ ] **[External UI/Mobile/Web]** UX Discovery complete → `docs/ux-discovery.md`
  - [ ] Audience mental model confirmed per user type (3A)
  - [ ] Visual direction agreed — references captured, non-negotiable identified (3B)
  - [ ] Navigation pattern decided (3C)
  - [ ] High-stakes screens identified with emotion + primary action (3D)
  - [ ] Friction and delight moments made design-actionable (3E)
