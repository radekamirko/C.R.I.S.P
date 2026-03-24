# Design System

**Project:** Znam Coveka
**Date:** 2026-03-24

---

## Design Philosophy

Two users, two emotional registers — one platform.

- **Homeowner side:** Trustworthy and curated. The homeowner is anxious and has been burned before. Every design decision must reduce uncertainty and signal quality. Think Airbnb — clean, photography-led, confident.
- **Tradie side:** Fast and actionable. The tradie is practical and time-poor. Every screen must have one obvious action. Think Uber Driver — job card, accept/decline, done.

**Non-negotiable feeling:** Trustworthy + approachable. Neither is optional. The platform must feel like it was built by someone who understands both sides of this relationship.

---

## Cognitive & Behavioural UX Principles

Applied to every screen. These are constraints, not suggestions.

| Principle | Rule |
|---|---|
| Hick's Law | Never show more than 3 choices at the same level. Homeowner shortlist = max 3 tradies. |
| Miller's Law | Chunk information. Job posting = max 5 fields per step. Tradie profile = sections, not one long form. |
| Peak-End Rule | The shortlist screen (peak) and the job completion screen (end) define the memory of the experience. Design these with extra care. |
| Fitts's Law | Primary actions are large, thumb-reachable, and high-contrast. Nothing important is in a corner. |
| Progressive Disclosure | Show what's needed now. Details on demand — not all at once. |
| Trust signals | Show real photos, real ratings, real explanations. Avoid stock imagery. |
| Empty states | Never show a blank screen. Every empty state has a clear next action. |

---

## Colour Palette

| Role | Colour | Usage |
|---|---|---|
| Primary | Warm deep blue `#1B3A5C` | Primary buttons, headers, key UI elements |
| Accent | Amber `#E8A020` | CTAs on tradie side, highlights, success states |
| Background | Off-white `#F8F6F2` | Page backgrounds — warm, not clinical white |
| Surface | White `#FFFFFF` | Cards, modals, input fields |
| Text primary | Near-black `#1A1A1A` | Body text, headings |
| Text secondary | Slate `#6B7280` | Supporting text, labels, metadata |
| Success | Green `#16A34A` | Job confirmed, approved, completed |
| Warning | Amber `#D97706` | Availability conflict, expiring, pending |
| Error | Red `#DC2626` | Validation errors, rejected |
| Border | Light grey `#E5E7EB` | Card borders, dividers |

**Rationale:** Warm deep blue signals trustworthiness (banking, professional services). Amber accent is warm and approachable without being aggressive. Off-white background avoids the cold clinical feel of pure white.

---

## Typography

| Role | Font | Size | Weight |
|---|---|---|---|
| Display heading | Inter | 32px / 2rem | 700 |
| Section heading | Inter | 24px / 1.5rem | 600 |
| Card heading | Inter | 18px / 1.125rem | 600 |
| Body | Inter | 16px / 1rem | 400 |
| Small / label | Inter | 14px / 0.875rem | 400 |
| Micro / caption | Inter | 12px / 0.75rem | 400 |

**AI explanation text** (homeowner shortlist): Body size, 400 weight, but displayed with extra line-height (1.7) and slightly indented — this is the most important text on the platform and must be readable at a glance.

**Rationale:** Inter is clean, highly legible on screens, free, and widely trusted. No display font needed — the copy is the design.

---

## Shape Language

- **Border radius:** 12px for cards, 8px for inputs and buttons, 24px for pills/tags
- **Cards:** White surface, 1px `#E5E7EB` border, 8px shadow (`0 1px 3px rgba(0,0,0,0.08)`)
- **Elevation:** Used sparingly — modals and bottom sheets only. Not for cards.
- **Images:** Always rounded (12px radius). Tradie portfolio photos are the main visual element — give them space.

---

## Motion

- **Transitions:** 150ms ease-out for micro-interactions (button press, hover)
- **Page transitions:** 200ms fade. Nothing jarring.
- **Loading states:** Skeleton screens (not spinners) for shortlist and job feed loading — reduces perceived wait time
- **No animation for animation's sake.** Motion is used only to confirm actions and indicate state change.

---

## Iconography

- Library: Heroicons (MIT, open source, matches Tailwind ecosystem)
- Style: Outline icons for navigation and secondary actions. Solid icons for active states.
- Size: 20px inline, 24px in navigation tabs

---

## Spacing System (Tailwind defaults)

| Token | Value | Usage |
|---|---|---|
| xs | 4px | Tight internal padding |
| sm | 8px | Component internal spacing |
| md | 16px | Standard padding, card padding |
| lg | 24px | Section spacing |
| xl | 32px | Page section separators |
| 2xl | 48px | Major layout gaps |

---

## Component Rules

### Tradie Match Card (homeowner shortlist — most important component)
- Tradie photo (left, 64px circle) + Name + Trade + Rating (right-aligned)
- AI explanation text below — full width, readable, not truncated
- "Select" CTA button — full width, primary colour
- Never show more than 3 of these cards per job

### Job Card (tradie feed)
- Trade icon + Job title + Location + Distance
- Posted time + Budget range (if set)
- "View Job" and "Apply" inline actions
- Clear visual distinction between matched jobs (highlighted) and browseable jobs

### Navigation Tabs
- Bottom tab bar on mobile, top nav on desktop
- Active tab: primary colour icon + label
- Inactive tab: grey icon + label
- No badges unless there is an unread notification — avoid badge inflation

---

## Responsive Behaviour

- **Mobile-first** — design for 375px width upward
- **Breakpoints:** sm 640px, md 768px, lg 1024px (Tailwind defaults)
- Tradie profile photo upload must work natively on mobile camera
- Tab bar collapses to desktop nav at lg breakpoint
- Job posting form is single-column on mobile, two-column on desktop
