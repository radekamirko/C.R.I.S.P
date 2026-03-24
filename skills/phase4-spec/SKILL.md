---
name: phase4-spec
description: The Mileva Method (CRISP) — Phase 4: Spec. Full implementation readiness package including solution design, UX direction, tech stack, backlog, MVP prioritization, risk assessment, and AI architecture for Claude Code projects — CLAUDE.md, skill mapping, AI specs, sprint planning, quality gates. Triggers on "spec", "phase 4", "build ready", "implementation plan", "CLAUDE.md", "sprint planning", "backlog", "AI spec", or after Phase I exit checklist is complete.
---

# S — Spec: Implementation Readiness

You are not building the thing. You are making the builder ready to build.

**Output: a package a developer can read on Monday and start building on Tuesday.**

---

## Before You Start — Read These

All filled project documents live in `docs/`. Read from there, not from the blank `/templates/` folder.

| File | What to extract |
|---|---|
| `docs/problem-statement.md` | Core problem, constraints, Go/No-Go rationale |
| `docs/stakeholder-register.md` | Who is impacted, what they need, human-in-the-loop zones |
| `docs/market-research.md` | Competitor must-haves, USP, feature gaps (external projects only) |
| `docs/swot.md` | Strengths to lean into, threats to design around (external projects only) |
| `docs/buy-vs-build-matrix.md` | Which tools are bought/configured vs built — informs tech stack |
| `docs/value-proposition-canvas.md` | USP and positioning — shapes UX and feature priority |
| `docs/user-journey-map.md` | Flows per user type — feeds UX spec directly |
| `docs/ux-discovery.md` | Visual direction, navigation pattern, high-stakes screens, friction/delight — **mandatory for UI/Mobile/Web; if missing, return to Phase I** |
| `docs/process-flow.md` | Step-by-step logic — feeds agent architecture |
| `docs/project-goals.md` | Goals and success criteria — every epic must link to one |

> **If `docs/ux-discovery.md` does not exist and this is a UI/Mobile/Web project: stop. Go back to Phase I and run the UX Discovery section (3A–3E) before continuing.**

Nothing in Phase S should contradict what was agreed in Phases C, R, and I. If a conflict arises — surface it, resolve it, update the source file.

---

## 4A: Solution Design

**UX/UI Direction**

Three artifacts, in this order:

1. **Design System** → `docs/design-system.md`
   - Pull design philosophy and audience fit from `docs/ux-discovery.md` (3A: mental models, use context)
   - Pull visual direction and references from `docs/ux-discovery.md` (3B: proposed direction, client refs, non-negotiable feeling)
   - Cognitive & behavioral UX principles (reference layer + per-screen checklist)
   - Color palette, typography, shape language, motion, iconography, spacing — grounded in 3B
   - Challenge any client-provided references that conflict with the target user (use 3A mental model as the test)

2. **Sitemap** → `docs/ux-spec.md` (Part 1)
   - Pull navigation pattern decision from `docs/ux-discovery.md` (3C) — this is already decided, do not re-open it
   - Pull user types from `docs/stakeholder-register.md`
   - Every screen and its place in the navigation structure

3. **UX Spec** → `docs/ux-spec.md` (Parts 2–3)
   - Pull flows directly from `docs/user-journey-map.md`
   - Flow spec first: user goal, entry/exit, flow map, success/failure states
   - For high-stakes screens (from `docs/ux-discovery.md` 3D): lead with the target emotion and primary action before speccing UI elements
   - For friction points (from `docs/ux-discovery.md` 3E): the design response is the spec direction — use it
   - Screen spec: information architecture, UI elements, states, user actions
   - Cognitive UX checklist applied to every screen

> **Rule:** Write flows before screens. Flows reveal intent; screens are the implementation.

---

## 4B: Tech Stack + 3rd Party Integration Trigger

**Tech Stack Proposal**
- Justify every choice against constraints in `docs/problem-statement.md` (budget, time, legal, tech)
- Cross-check `docs/buy-vs-build-matrix.md` — already-decided tools go here, not up for debate again
- Prefer existing libraries and open source when time or budget is constrained

**3rd Party Integration Identification — mandatory step**

> Every 3rd party service in the tech stack = a required integration AI Spec.

When finalizing the tech stack, explicitly list every external API, SaaS, or service being integrated (examples: Stripe, Garmin, Twilio, SendGrid, Google Maps, OpenAI, etc.).

For each one:
1. Flag it in the tech stack table with tag `[INTEGRATION REQUIRED]`
2. Create a dedicated AI Spec for it → `docs/ai-spec-[service-name].md`
3. Run the **Web Research Protocol** from `templates/ai-spec.md` — browse the official dev docs, extract auth, endpoints, payloads, response shapes, DB mapping
4. Only ask the client for what docs don't provide (credentials, account-specific config, sandbox access)

These integration specs are prerequisites — they must be written before the sprint that uses the integration is planned.

---

## 4C: Project Foundation

**Initial Backlog** → `docs/initial-backlog.md`
- Pull user types from `docs/stakeholder-register.md` for user story format
- Every epic must link to a goal in `docs/project-goals.md`
- Every goal in `docs/project-goals.md` must have at least one epic
- Leave MVP tag column blank at this stage — filled in 4D

**Assumptions Log** → `docs/assumptions-log.md`

**Risk Assessment** → `docs/risk-assessment.md`
- Pull known threats from `docs/swot.md` (external projects)
- Security posture: data handling, access control, auth
- Legal/compliance: GDPR, HIPAA, IP, data residency
- Human-in-the-loop zones formalized (carried forward from Phase R)

---

## 4D: MVP Prioritization — HVLE Conversation

> **Stop. Do not write sprint plans yet. This step requires a live conversation with the client.**
> The HVLE scoring is not a background calculation — it is a structured elicitation. Run it now.
> Full scoring logic lives in `skills/phase4-spec/mvp-prioritization.md` — read it before starting.

---

### Step 1: Lock MVP-BASELINE (no scoring needed)

Before any HVLE scoring, identify the non-negotiables. These bypass the scoring model entirely.

Pull from `docs/market-research.md`:
- **Must-haves** — features every competitor has; users expect them as table stakes
- **USP features** — the thing that makes this product worth choosing over alternatives

Present them to the client:
> "Before we score anything, let me lock the floor. These features go in MVP regardless of score — every competitor has them, and our USP lives here. Does this list look right, or is anything missing?"

Get confirmation. Mark these `MVP-BASELINE` in `docs/initial-backlog.md`. Do not re-debate them.

---

### Step 2: Elicit Business Value Criteria

Pre-fill 3–4 criteria based on project context (pull from `docs/project-goals.md` and `docs/stakeholder-register.md`), then present them for correction — don't ask open-ended questions.

For **external products**, default criteria are:
- Customer acquisition
- User activation / adoption
- Retention / engagement
- Revenue generation
- Referral / virality

For **internal tools**, default criteria are:
- Cross-company process adoption
- Time saved per user per week
- Error / rework reduction
- Employee satisfaction
- Compliance / risk reduction

Say this:
> "I've assumed the outcomes that matter most here are [X, Y, Z]. Does that feel right, or am I optimizing for the wrong thing? We need max 5 — if you want to add one, we cut one."

**Hard limit: 5 criteria.** If they want more, help them consolidate. More than 5 and everything starts scoring the same.

---

### Step 3: Weight the Criteria

Once criteria are agreed, get weights. Do not skip this — unweighted scoring treats every criterion as equal, which is almost never true.

> "Now give each one a weight from 1 to 3. Think of it as: 3 = if we nail this, everything else follows. 1 = nice to track, but it's not what this lives or dies on."

Present the weighted criteria back for confirmation before scoring.

---

### Step 4: Score the Backlog Together

Take every feature from `docs/initial-backlog.md` (excluding MVP-BASELINE items) and score them against each criterion (1–5). For each feature:
- 5 = directly and strongly drives this outcome
- 3 = contributes, but not the whole story
- 1 = barely connected — we're reaching

Walk the client through scores for any non-obvious features. Don't silently assign scores — show your reasoning and invite correction.

**Priority Score = Business Value Score ÷ Effort Value**

Effort sizing (T-shirt):
| Size | Days | Effort Value |
|---|---|---|
| XS | < 1 day | 0.5 |
| S | 1–2 days | 1.5 |
| M | 3–5 days | 4 |
| L | 7–10 days | 8.5 |
| XL | 10+ days | 12 |

---

### Step 5: Apply Dependency Overrides

After scoring, check for features that scored low but are required by high-scoring ones.

> "Feature [X] scored lower on its own, but [Y] sits on top of it — so [X] moves into MVP as a dependency. We don't get a choice here."

Mark blockers as `DEPENDENCY`. Adjust the MVP line to include all required foundations.

---

### Step 6: Draw the MVP Line with the Client

Sort features by Priority Score (descending): MVP-BASELINE first, then scored features high→low, dependencies resolved.

Present the ranked list and propose where to draw the line:
> "Here's the ranked list. I'd draw the line here — everything above ships in MVP. Before you agree, ask yourself three things: Can someone actually use this and get value from it with only these features? Does it deliver our USP? Can we build it in the time we have?"

All three must be yes. If not — something's missing or the scope is too big. Adjust together.

---

### Step 7: Tag and Save

Tag every feature:
- `MVP-BASELINE` — table stakes or USP, non-negotiable
- `MVP` — scored, above the line
- `POST-MVP` — scored, below the line (not never — just not now)
- `DEPENDENCY` — required by an MVP feature, regardless of own score

Save scoring output → `docs/mvp-prioritization.md`
Update tags in → `docs/initial-backlog.md`

Only after this is complete: proceed to 4E and sprint planning.

---

## 4E: AI Architecture (Claude Code Projects)

This is the layer between "we know what to build" and "Claude Code starts building."
Most AI implementations fall apart here. Don't skip it.

**Claude Setup — in this order:**
1. Write `CLAUDE.md` in the project root — compile context from ALL `docs/` files
   - Problem statement, constraints, goals, success metrics, tech stack, agent map, env vars master list
   - Include the CRISP Output Manifest (see Phase 4 Outputs below) so Claude always knows what docs exist
   - This is what Claude reads at the start of every session — make it complete
2. Define folder structure before any code is written
3. Define session context strategy — what must Claude know at the start of every session?

**Skill / Agent Architecture**
- Pull process steps from `docs/process-flow.md` — each major step is a candidate agent
- For each agent: responsibilities, inputs, outputs, boundaries
- Map handoffs between agents
- Write `SKILL.md` per agent into the project's `skills/` folder

**AI Spec (one per feature / sprint)**
Write before handing any feature to Claude Code → `docs/ai-spec-[feature-or-sprint].md`
- Use `templates/ai-spec.md` as the blank starting point
- If the feature involves a 3rd party integration: complete the **3rd Party Integrations** section
- Integration specs must be written before the sprint that depends on them

> No spec = no build.

**Sprint Planning** → `docs/sprint-plan.md`
- MVP-tagged features feed Sprint 1+. Post-MVP feeds later sprints.
- Use dependency map from `docs/mvp-prioritization.md` to sequence sprints correctly
- Each sprint = a clear, bounded, testable unit of work
- Integration AI specs must be complete before any sprint that calls that API

**Quality & Safety Gates (per sprint)**
- Deployment checklist: dependencies resolved, env vars clean, no secrets in code
- Security review before each deploy
- PR review standards defined
- Unit test coverage requirements
- Guardrail validation: hallucination risks, output validation, fallback logic

---

## Phase 4 Outputs

> All files go to `docs/` in the project root. Save as you go — do not batch at the end.
> The CLAUDE.md output manifest lists all expected files so nothing gets silently dropped.

| File | Contents | Required? |
|---|---|---|
| `docs/design-system.md` | Design philosophy, visual direction, color, type, motion, references | External UI/Mobile/Web only |
| `docs/ux-spec.md` | Sitemap + flow specs + screen specs with cognitive UX | External UI/Mobile/Web only |
| `docs/initial-backlog.md` | Full feature list with user stories, epic-to-goal links, MVP tags | Always |
| `docs/assumptions-log.md` | Logged assumptions and resolution status | Always |
| `docs/risk-assessment.md` | Risks, mitigations, security posture, legal/compliance, HITL zones | Always |
| `docs/mvp-prioritization.md` | HVLE scoring table, weighted criteria, priority scores, MVP line | Always |
| `docs/ai-spec-[name].md` | One per feature/sprint — inputs, outputs, logic, edge cases | Always (one per sprint) |
| `docs/ai-spec-[service].md` | Integration spec per 3rd party service | Per integration |
| `docs/sprint-plan.md` | Sprint sequence, goals, features per sprint, quality gates | Always |
| `CLAUDE.md` | Compiled project context — lives in project root, not docs/ | Always |

---

## Exit Checklist

**Solution Design**
- [ ] UX discovery inputs read from `docs/ux-discovery.md` before any design work started
- [ ] Design system defined, visual direction grounded in ux-discovery → `docs/design-system.md`
- [ ] Sitemap complete, navigation pattern taken from ux-discovery (not re-decided) → `docs/ux-spec.md`
- [ ] UX spec written (flows + screens), high-stakes screens and friction points addressed → `docs/ux-spec.md`
- [ ] Tech stack proposed and justified against constraints in `docs/problem-statement.md`

**3rd Party Integrations**
- [ ] Every 3rd party service in tech stack identified and tagged `[INTEGRATION REQUIRED]`
- [ ] Integration AI Spec written per service → `docs/ai-spec-[service-name].md`
- [ ] Auth, endpoints, payloads, DB mapping documented for each

**Foundation**
- [ ] Initial backlog written, every epic linked to a goal → `docs/initial-backlog.md`
- [ ] Every goal in `docs/project-goals.md` has at least one epic
- [ ] Assumptions log created → `docs/assumptions-log.md`
- [ ] Risk assessment complete (threats from SWOT included) → `docs/risk-assessment.md`
- [ ] Security and legal guardrails defined

**MVP Prioritization (HVLE)**
- [ ] MVP-BASELINE features locked (must-haves + USP) and confirmed with client
- [ ] Business value criteria defined (max 5) and confirmed with client
- [ ] Criteria weighted (1–3) by client
- [ ] All backlog features scored (1–5 per criterion) — reasoning shown to client
- [ ] Effort sized for every feature (XS/S/M/L/XL)
- [ ] Priority scores calculated (Business Value ÷ Effort)
- [ ] Dependencies mapped and overrides applied
- [ ] MVP line drawn and validated with client (all 3 questions answered yes)
- [ ] Scoring output saved → `docs/mvp-prioritization.md`
- [ ] Backlog updated with MVP / Post-MVP / Dependency tags → `docs/initial-backlog.md`

**AI Architecture**
- [ ] `CLAUDE.md` compiled from all `docs/` outputs — includes output manifest
- [ ] Folder structure defined
- [ ] Agent/skill map complete — one `SKILL.md` per agent in project `skills/` folder
- [ ] AI Spec written per feature/sprint → `docs/ai-spec-[name].md`
- [ ] Sprint plan sequenced using MVP prioritization + dependency map → `docs/sprint-plan.md`
- [ ] Quality gates defined per sprint
- [ ] Integration specs completed before sprints that depend on them
