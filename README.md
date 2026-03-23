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
├── CLAUDE.md                  — project context for Claude
├── skills/
│   ├── phase1-clarify/        — C: Problem definition
│   ├── phase2-results/        — R: Outcome alignment
│   ├── phase3-investigate/    — I: Process mapping
│   ├── phase4-spec/           — S: Build ready
│   └── phase5-prove/          — P: Success validation
└── templates/
    ├── problem-statement.md
    ├── buy-vs-build-matrix.md
    ├── value-proposition-canvas.md
    ├── stakeholder-register.md
    ├── user-journey-map.md
    ├── process-flow.md
    ├── project-goals.md
    ├── initial-backlog.md
    ├── assumptions-log.md
    ├── risk-assessment.md
    ├── sprint-plan.md
    ├── ai-spec.md
    └── CLAUDE.md
```

---

Built by [Mirko Radeka](https://mileva.io) — AI agency builder, Serbia.
*Outcome first. Always.*
