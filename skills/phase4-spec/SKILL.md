---
name: phase4-spec
description: The Mileva Method (CRISP) — Phase 4: Spec. Full implementation readiness package including solution design, UX direction, tech stack, backlog, MVP prioritization, risk assessment, and AI architecture for Claude Code projects — CLAUDE.md, skill mapping, AI specs, sprint planning, quality gates. Triggers on "spec", "phase 4", "build ready", "implementation plan", "CLAUDE.md", "sprint planning", "backlog", "AI spec", or after Phase I exit checklist is complete.
---

# S — Spec: Implementation Readiness

You are not building the thing. You are making the builder ready to build.

**Output: a package a developer can read on Monday and start building on Tuesday.**

---

## Before You Start — Read These

Pull context from every previous phase before writing a single spec:

| File | What to extract |
|---|---|
| `templates/problem-statement.md` | Core problem, constraints, Go/No-Go rationale |
| `templates/stakeholder-register.md` | Who is impacted, what they need, human-in-the-loop zones |
| `templates/market-research.md` | Competitor must-haves, USP, feature gaps (external projects only) |
| `templates/swot.md` | Strengths to lean into, threats to design around (external projects only) |
| `templates/buy-vs-build-matrix.md` | Which tools are bought/configured vs built — informs tech stack |
| `templates/value-proposition-canvas.md` | USP and positioning — shapes UX and feature priority |
| `templates/stakeholder-register.md` | User types for UX spec and user stories |
| `templates/user-journey-map.md` | Flows per user type — feeds UX spec directly |
| `templates/process-flow.md` | Step-by-step logic — feeds agent architecture |
| `templates/project-goals.md` | Goals and success criteria — every epic must link to one |

Nothing in Phase S should contradict what was agreed in Phases C, R, and I. If a conflict arises — surface it, resolve it, update the source template.

---

## 4A: Solution Design

**UX/UI Direction**

Three artifacts, in this order:

1. **Design System** — written once per project → `templates/design-system.md`
   - Design philosophy and audience fit (pull from stakeholder-register + market-research)
   - Cognitive & behavioral UX principles (reference layer + per-screen checklist)
   - Color palette, typography, shape language, motion, iconography, spacing
   - Visual references (search for 2–4 that match audience and product positioning)
   - Challenge any client-provided references that conflict with the target user

2. **Sitemap** — full screen hierarchy → `templates/ux-spec.md` (Part 1)
   - Pull user types from `templates/stakeholder-register.md`
   - Every screen and its place in the navigation structure
   - Navigation pattern defined before any flow is specced

3. **UX Spec** — per critical flow, then per screen → `templates/ux-spec.md` (Parts 2–3)
   - Pull flows directly from `templates/user-journey-map.md`
   - Flow spec first: user goal, entry/exit, flow map, success/failure states
   - Screen spec: information architecture, UI elements, states, user actions
   - Cognitive UX checklist applied to every screen

> **Rule:** Write flows before screens. Flows reveal intent; screens are the implementation.

---

## 4B: Tech Stack + 3rd Party Integration Trigger

**Tech Stack Proposal**
- Justify every choice against constraints in `templates/problem-statement.md` (budget, time, legal, tech)
- Cross-check `templates/buy-vs-build-matrix.md` — already-decided tools go here, not up for debate again
- Prefer existing libraries and open source when time or budget is constrained

**3rd Party Integration Identification — mandatory step**

> Every 3rd party service in the tech stack = a required integration AI Spec.

When finalizing the tech stack, explicitly list every external API, SaaS, or service being integrated (examples: Stripe, Garmin, Twilio, SendGrid, Google Maps, OpenAI, etc.).

For each one:
1. Flag it in the tech stack table with tag `[INTEGRATION REQUIRED]`
2. Create a dedicated AI Spec for it using the **3rd Party Integrations** section in `templates/ai-spec.md`
3. Run the **Web Research Protocol** from that template — browse the official dev docs, extract auth, endpoints, payloads, response shapes, DB mapping
4. Only ask the client for what docs don't provide (credentials, account-specific config, sandbox access)

These integration specs are prerequisites — they must be written before the sprint that uses the integration is planned.

---

## 4C: Project Foundation

**Initial Backlog** → `templates/initial-backlog.md`
- Pull user types from `templates/stakeholder-register.md` for user story format
- Every epic must link to a goal in `templates/project-goals.md`
- Every goal in `templates/project-goals.md` must have at least one epic
- Leave MVP tag column blank at this stage — filled in 4D

**Assumptions Log** → `templates/assumptions-log.md`

**Risk Assessment** → `templates/risk-assessment.md`
- Pull known threats from `templates/swot.md` (external projects)
- Security posture: data handling, access control, auth
- Legal/compliance: GDPR, HIPAA, IP, data residency
- Human-in-the-loop zones formalized (carried forward from Phase R)

---

## 4D: MVP Prioritization → `skills/phase4-spec/mvp-prioritization.md`

Run this after the initial backlog is drafted. Mandatory — do not plan sprints without it.

**Inputs — pull from:**
- `templates/market-research.md` → competitor must-haves and USP (external only)
- `templates/problem-statement.md` → problem context and constraints
- `templates/project-goals.md` → goals that features must link back to
- `templates/stakeholder-register.md` → who benefits, informs business value criteria
- `templates/initial-backlog.md` → full feature list to score

**Output:**
- Every feature tagged: `MVP-BASELINE` / `MVP` / `POST-MVP` / `DEPENDENCY`
- Priority scores and dependency map
- MVP line validated with client

Update `templates/initial-backlog.md` with tags immediately after.

---

## 4E: AI Architecture (Claude Code Projects)

This is the layer between "we know what to build" and "Claude Code starts building."
Most AI implementations fall apart here. Don't skip it.

**Claude Setup — in this order:**
1. Write `CLAUDE.md` — compile context from ALL previous templates → `templates/CLAUDE.md`
   - Problem statement, constraints, goals, success metrics, tech stack, agent map, env vars master list
   - This is what Claude reads at the start of every session — make it complete
2. Define folder structure before any code is written
3. Define session context strategy — what must Claude know at the start of every session?

**Skill / Agent Architecture**
- Pull process steps from `templates/process-flow.md` — each major step is a candidate agent
- For each agent: responsibilities, inputs, outputs, boundaries
- Map handoffs between agents
- Write `SKILL.md` per agent → `templates/agent-skill.md`

**AI Spec (one per feature / sprint)**
Write before handing any feature to Claude Code → `templates/ai-spec.md`
- If the feature involves a 3rd party integration: complete the **3rd Party Integrations** section
- Integration specs must be written before the sprint that depends on them

> No spec = no build.

**Sprint Planning**
- MVP-tagged features feed Sprint 1+. Post-MVP feeds later sprints.
- Use dependency map from `templates/mvp-prioritization.md` to sequence sprints correctly
- Each sprint = a clear, bounded, testable unit of work → `templates/sprint-plan.md`
- Integration AI specs must be complete before any sprint that calls that API

**Quality & Safety Gates (per sprint)**
- Deployment checklist: dependencies resolved, env vars clean, no secrets in code
- Security review before each deploy
- PR review standards defined
- Unit test coverage requirements
- Guardrail validation: hallucination risks, output validation, fallback logic

---

## Exit Checklist

**Solution Design**
- [ ] Design system defined → `templates/design-system.md`
- [ ] Sitemap complete → `templates/ux-spec.md`
- [ ] UX spec written (flows + screens) → `templates/ux-spec.md`
- [ ] Tech stack proposed and justified against constraints in `templates/problem-statement.md`

**3rd Party Integrations**
- [ ] Every 3rd party service in tech stack identified and tagged `[INTEGRATION REQUIRED]`
- [ ] Integration AI Spec written per service → `templates/ai-spec.md` (3rd Party section)
- [ ] Auth, endpoints, payloads, DB mapping documented for each

**Foundation**
- [ ] Initial backlog written, every epic linked to a goal → `templates/initial-backlog.md`
- [ ] Every goal in `templates/project-goals.md` has at least one epic
- [ ] Assumptions log created → `templates/assumptions-log.md`
- [ ] Risk assessment complete (threats from SWOT included) → `templates/risk-assessment.md`
- [ ] Security and legal guardrails defined

**MVP Prioritization**
- [ ] Business value criteria defined and weighted
- [ ] All features scored and sized
- [ ] MVP line drawn and client-validated → `templates/mvp-prioritization.md`
- [ ] Backlog updated with MVP / Post-MVP / Dependency tags → `templates/initial-backlog.md`

**AI Architecture**
- [ ] `CLAUDE.md` compiled from all phase outputs → `templates/CLAUDE.md`
- [ ] Folder structure defined
- [ ] Agent/skill map complete → `templates/agent-skill.md` per agent
- [ ] AI Spec written per feature/sprint → `templates/ai-spec.md`
- [ ] Sprint plan sequenced using MVP prioritization + dependency map → `templates/sprint-plan.md`
- [ ] Quality gates defined per sprint
- [ ] Integration specs completed before sprints that depend on them
