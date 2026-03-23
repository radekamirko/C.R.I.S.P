---
name: phase4-spec
description: The Mileva Method (CRISP) — Phase 4: Spec. Full implementation readiness package including solution design, UX direction, tech stack, backlog, risk assessment, and AI architecture for Claude Code projects — CLAUDE.md, skill mapping, AI specs, sprint planning, quality gates. Triggers on "spec", "phase 4", "build ready", "implementation plan", "CLAUDE.md", "sprint planning", "backlog", "AI spec", or after Phase I exit checklist is complete.
---

# S — Spec: Implementation Readiness

You are not building the thing. You are making the builder ready to build.

**Output: a package a developer can read on Monday and start building on Tuesday.**

---

## 4A: Solution Design

**UX/UI Direction**

Three artifacts, in this order:

1. **Design System** — written once per project → `templates/design-system.md`
   - Design philosophy and audience fit check
   - Cognitive & behavioral UX principles (reference layer + per-screen checklist)
   - Color palette, typography, shape language, motion, iconography, spacing
   - Visual references (search for 2–4 that match audience and product positioning)
   - Challenge any client-provided references that conflict with the target user

2. **Sitemap** — full screen hierarchy → `templates/ux-spec.md` (Part 1)
   - Every screen and its place in the navigation structure
   - Navigation pattern defined before any flow is specced

3. **UX Spec** — per critical flow, then per screen → `templates/ux-spec.md` (Parts 2–3)
   - Flow spec first: user goal, entry/exit, flow map, success/failure states
   - Screen spec: information architecture, UI elements, states, user actions
   - Cognitive UX checklist applied to every screen
   - Visual references per screen where needed

> **Rule:** Write flows before screens. Flows reveal intent; screens are the implementation.

**Tech Stack Proposal**
- Justify against Phase C constraints (budget, time, legal, technical)
- Prefer existing libraries and open source when time or budget is constrained

**Project Foundation**
- Initial backlog: epics + user stories, prioritized → `templates/initial-backlog.md`
- Project plan with sprint phasing → `templates/sprint-plan.md`
- Assumptions log → `templates/assumptions-log.md`

**Risk & Guardrails**
- Risk assessment → `templates/risk-assessment.md`
- Security posture: data handling, access control, auth
- Legal/compliance guardrails: GDPR, HIPAA, IP, data residency
- Human-in-the-loop zones formalized (carried forward from Phase R)

---

## 4B: AI Architecture (Claude Code Projects)

This is the layer between "we know what to build" and "Claude Code starts building."
Most AI implementations fall apart here. Don't skip it.

**Claude Setup — in this order:**
1. Write `CLAUDE.md` — compile from all Phase C/R/I/S docs → `templates/CLAUDE.md`
2. Define folder structure before any code is written
3. Define session context strategy — what must Claude know at the start of every session?

**Skill / Agent Architecture**
- Map every agent needed to achieve project goals
- For each agent: responsibilities, inputs, outputs, boundaries
- Write `SKILL.md` per agent → `templates/agent-skill.md`
- Map handoffs between agents
- References: [everything-claude-code](https://github.com/affaan-m/everything-claude-code), [Anthropic skills repo](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)

**AI Spec (one per feature / sprint)**
Write before handing any feature to Claude Code → `templates/ai-spec.md`
Covers: context, scope, inputs/outputs, DB schema, acceptance criteria, agent dependencies, prompt architecture, guardrails, constraints, test cases, open questions.

> No spec = no build.

**Sprint Planning for AI**
- Break work into increments Claude can execute and test independently
- Map dependencies between sprints
- Each sprint = a clear, bounded, testable unit of work → `templates/sprint-plan.md`

**Quality & Safety Gates (per sprint)**
- Deployment checklist: dependencies resolved, env vars clean, no secrets in code
- Security review before each deploy
- PR review standards defined
- Unit test coverage requirements
- Guardrail validation: hallucination risks, output validation, fallback logic

---

## Exit Checklist
- [ ] Design system defined → `templates/design-system.md`
- [ ] Sitemap complete → `templates/ux-spec.md`
- [ ] UX spec written (flows + screens) → `templates/ux-spec.md`
- [ ] Tech stack proposed and justified against constraints
- [ ] Initial backlog written and prioritized → `templates/initial-backlog.md`
- [ ] Assumptions log created → `templates/assumptions-log.md`
- [ ] Risk assessment complete → `templates/risk-assessment.md`
- [ ] Security and legal guardrails defined
- [ ] `CLAUDE.md` drafted → `templates/CLAUDE.md`
- [ ] Folder structure defined
- [ ] Agent/skill map complete with `SKILL.md` per agent → `templates/agent-skill.md`
- [ ] AI Spec written per feature/sprint → `templates/ai-spec.md`
- [ ] Sprint plan with dependencies mapped → `templates/sprint-plan.md`
- [ ] Quality gates defined per sprint
