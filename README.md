# CRISP — The Mileva Method

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

A BA/PM framework for AI implementors. 5 phases that take you from a vague client request to a fully specced, ready-to-build implementation brief — before Claude Code writes a single line.

| Phase | Name | What it does |
|---|---|---|
| **C** | Clarify | Problem statement, painkiller test, constraints, buy vs build, Go/No-Go |
| **R** | Results | Stakeholder register, baseline measurement, success metrics, tradeoff negotiation |
| **I** | Investigate | Process mapping (existing or greenfield), user journey maps |
| **S** | Spec | Solution design, AI architecture, CLAUDE.md, skill mapping, sprint planning, quality gates |
| **P** | Prove | Did the needle move? |

---

## How to use

1. Drop the `/skills` folder into your Claude Code project
2. Use `/templates` as your deliverable starting points
3. Run phases in order — do not skip
4. Check the exit checklist before moving to the next phase
5. Write one AI Spec per sprint before building anything

## The rule

> No spec = no build.

Never discuss technology before the problem is defined.
Never design a solution before the finish line is set.
Never hand a feature to Claude Code without an AI Spec.

---

## File structure

```
crisp/
├── CLAUDE.md                  — project context for Claude (includes env vars master list)
├── skills/
│   ├── phase1-clarify/        — C: Problem definition
│   ├── phase2-results/        — R: Outcome alignment
│   ├── phase3-investigate/    — I: Process mapping
│   ├── phase4-spec/           — S: Build ready
│   └── phase5-prove/          — P: Success validation
└── templates/
    ├── problem-statement.md   — Phase C: one-sentence problem + constraints + Go/No-Go
    ├── buy-vs-build-matrix.md — Phase C: evaluate existing tools before committing to build
    ├── value-proposition-canvas.md — Phase C: external products only
    ├── stakeholder-register.md — Phase R: who is impacted and how
    ├── user-journey-map.md    — Phase I: per user type, needs/feelings/actions/pain points
    ├── process-flow.md        — Phase I: step-by-step process map
    ├── project-goals.md       — Phase I→S: goals linked to success metrics
    ├── design-system.md       — Phase S: design philosophy, cognitive UX principles, color/type/motion
    ├── ux-spec.md             — Phase S: sitemap + flow specs + screen specs
    ├── initial-backlog.md     — Phase S: epics + user stories, prioritized
    ├── assumptions-log.md     — Phase S: what we're taking as true until proven otherwise
    ├── risk-assessment.md     — Phase S: what could go wrong, likelihood, mitigation
    ├── sprint-plan.md         — Phase S: sprint phasing with dependencies
    ├── ai-spec.md             — Phase S: per-sprint build brief for Claude Code (includes env vars + DB schema)
    ├── agent-skill.md         — Phase S: template for each project agent SKILL.md
    └── CLAUDE.md              — Phase S: compiled project context for Claude (master env vars table)
```

---

Built by [Mirko Radeka](https://mileva.io) — AI agency builder, Serbia.
*Outcome first. Always.*
