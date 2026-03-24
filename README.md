# CRISP — The Mileva Method

**A BA/PM framework for AI implementors. Go from vague client brief to Claude Code-ready spec — without building the wrong thing.**

> Most AI implementations fail before a single line of code is written.
> Not because the model was wrong. Not because the tools weren't good enough.
> Because nobody defined the problem. Nobody measured the baseline. Nobody asked *why* before asking *how*.
>
> You're an AI implementor. You know how to build. You probably even know which tools to use.
> What you might not have — yet — is the methodology to make sure you're building the right thing.
>
> This is that methodology.

---

## What is CRISP?

CRISP is an open-source **AI project management framework** for builders, consultants, and AI agencies. It's a structured 5-phase methodology that takes you from a vague client request to a fully specced, Claude Code-ready implementation brief — before a single line of code gets written.

Built for:
- **AI agency owners** running client implementations
- **Solo builders** using Claude Code, Cursor, or similar agentic tools
- **Consultants** who need a repeatable discovery-to-spec process
- **Product managers** working on AI-native products

| Phase | Name | What it does |
|---|---|---|
| **C** | Clarify | Problem statement, painkiller test, magic wand, constraints, buy vs build, market research (external), SWOT (external), Go/No-Go |
| **R** | Results | Stakeholder register, baseline measurement, success metrics, tradeoff negotiation |
| **I** | Investigate | Process mapping (existing or greenfield), user journey maps, project goals |
| **S** | Spec | Solution design, MVP prioritization (HVLE scoring), 3rd party integration specs, AI architecture, CLAUDE.md, skill mapping, sprint planning, quality gates |
| **P** | Prove | Did the needle move? |

---

## Why CRISP exists

Every AI project failure I've seen had the same root cause.

Builder gets a brief → skips straight to the stack → builds something technically impressive → delivers it → client says *"this isn't what I meant."*

Six weeks. Wasted.

The gap isn't in the build. It's in everything before it. CRISP fills that gap with a repeatable, client-tested process — from problem definition to sprint-ready AI specs.

---

## How to use

1. Drop the `/skills` folder into your Claude Code project
2. Use `/templates` as your deliverable starting points
3. Run phases in order — do not skip
4. Check the exit checklist before moving to the next phase
5. Write one AI Spec per sprint before building anything

## The rules

> No spec = no build.

- Never discuss technology before the problem is defined
- Never design a solution before the finish line is set
- Never hand a feature to Claude Code without an AI Spec
- Never plan a sprint that calls an external API without an integration spec

---

## How it connects

Every phase feeds the next. Nothing lives in isolation.

```
C — Clarify
  problem-statement ──────────────────────────────────────────┐
  buy-vs-build-matrix ────────────────────────────────────┐   │
  market-research (external) ─────────────────────────┐   │   │
  swot (external) ─────────────────────────────────┐  │   │   │
                                                   │  │   │   │
R — Results                                        │  │   │   │
  stakeholder-register ────────────────────────┐  │  │   │   │
                                               │  │  │   │   │
I — Investigate                                │  │  │   │   │
  user-journey-map ────────────────────────┐  │  │  │   │   │
  process-flow ─────────────────────────┐  │  │  │  │   │   │
  project-goals ──────────────────────┐ │  │  │  │  │   │   │
                                      ↓ ↓  ↓  ↓  ↓  ↓   ↓   ↓
S — Spec
  tech stack → [INTEGRATION REQUIRED] tags → integration ai-specs
  initial-backlog (epics linked to goals)
  mvp-prioritization (HVLE scored, tagged, dependencies mapped)
  initial-backlog updated with MVP / Post-MVP tags
  sprint-plan (sequenced by tags + dependency map)
  ai-spec per sprint (integration specs before sprints that need them)
  CLAUDE.md (compiled from everything above)
```

---

## File structure

```
crisp/
├── CLAUDE.md                        — project context for Claude (env vars master list)
├── skills/
│   ├── phase1-clarify/
│   │   ├── SKILL.md                 — C: Problem definition, elicitation moves, Go/No-Go
│   │   ├── market-research.md       — C: TAM, competitor map, review mining, USP gap (external only)
│   │   └── swot.md                  — C: Pre-filled SWOT, client confirms (external only)
│   ├── phase2-results/              — R: Outcome alignment, baseline, success metrics
│   ├── phase3-investigate/          — I: Process mapping, user journeys, project goals
│   ├── phase4-spec/
│   │   ├── SKILL.md                 — S: Full spec process, reads all previous phase outputs
│   │   └── mvp-prioritization.md   — S: HVLE scoring, MVP line, dependency overrides
│   └── phase5-prove/                — P: Success validation against Phase R baseline
└── templates/
    ├── problem-statement.md         — Phase C: one-sentence problem + constraints + Go/No-Go
    ├── buy-vs-build-matrix.md       — Phase C: evaluate existing tools before committing to build
    ├── value-proposition-canvas.md  — Phase C: external products only
    ├── market-research.md           — Phase C: TAM, competitors, feature standards, review insights, USP
    ├── swot.md                      — Phase C: strengths, weaknesses, opportunities, threats + strategy matrix
    ├── stakeholder-register.md      — Phase R: who is impacted and how
    ├── user-journey-map.md          — Phase I: per user type, needs/feelings/actions/pain points
    ├── process-flow.md              — Phase I: step-by-step process map
    ├── project-goals.md             — Phase I→S: goals linked to success metrics
    ├── design-system.md             — Phase S: design philosophy, cognitive UX principles, color/type/motion
    ├── ux-spec.md                   — Phase S: sitemap + flow specs + screen specs
    ├── initial-backlog.md           — Phase S: epics linked to goals, user stories with MVP tags
    ├── mvp-prioritization.md        — Phase S: HVLE scoring table, dependency map, MVP line
    ├── assumptions-log.md           — Phase S: what we're taking as true until proven otherwise
    ├── risk-assessment.md           — Phase S: what could go wrong, likelihood, mitigation
    ├── sprint-plan.md               — Phase S: sprint sequencing from MVP tags + dependency map
    ├── ai-spec.md                   — Phase S: per-sprint build brief + 3rd party integration specs
    ├── agent-skill.md               — Phase S: template for each project agent SKILL.md
    └── CLAUDE.md                    — Phase S: compiled project context for Claude (master env vars table)
```

---

## Built by Mileva

CRISP is the methodology behind [Mileva](https://mileva.io) — an AI automation agency that builds workflow systems replacing entire operational teams.

If you're a business owner looking to implement AI without wasting six weeks building the wrong thing, or an agency that wants to productise your discovery process — [mileva.io](https://mileva.io) is where this gets applied in the real world.

**Questions, PRs, or war stories from using CRISP in the wild:** open an issue or find me on [X @radekamirko](https://x.com/radekamirko).

---

*Outcome first. Always.*
