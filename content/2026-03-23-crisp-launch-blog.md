---
title: I built a PM framework specifically for AI implementors. Here's why existing ones fail.
date: 2026-03-23
status: ready
type: blog
project: CRISP
url: https://github.com/radekamirko/C.R.I.S.P
---

# I built a PM framework specifically for AI implementors. Here's why existing ones fail.

Every AI project I've seen go wrong had the same root cause.

Not a bad model. Not the wrong stack. Not Claude hallucinating.

Someone started building before they understood the problem.

They jumped from "client wants AI" to "let me set up the repo" in the same conversation. And six weeks later, they're delivering something technically impressive that solves the wrong thing.

I've done it. I've watched other builders do it. And it's completely avoidable.

---

## The gap nobody talks about

There are great frameworks for traditional software delivery. JIRA, agile, scrum, shape-up — they all have their place.

But none of them were designed for what an AI implementor actually does: take a vague brief, figure out what the AI should actually automate, design agent architecture, and hand it to Claude Code in a way it can act on without breaking things.

That gap is where most AI projects fall apart.

---

## So I built CRISP

CRISP is a 5-phase BA/PM methodology for AI builders. Five phases, one rule: no spec, no build.

- **C — Clarify:** What problem are we actually solving? Painkiller or multivitamin? Go or no-go?
- **R — Results:** What does solved look like? Baseline the current state. Define success before touching a keyboard.
- **I — Investigate:** Map the process — existing or greenfield. Every step, every tool, every handoff.
- **S — Spec:** Build the implementation package. Design system, UX spec, tech stack, backlog, agent architecture, CLAUDE.md, AI specs per sprint.
- **P — Prove:** Did the needle move? Close the loop back to the baseline you set in R.

Each phase has a skill file, templates, and an exit checklist. You don't move to the next phase until the checklist is clean.

---

## What it produces

The Spec phase alone outputs: a design system with cognitive UX principles baked in, a full UX spec (sitemap → flows → screens), a prioritized backlog, risk assessment, a `CLAUDE.md` that Claude reads at the start of every session, an agent map with SKILL.md per agent, and an AI Spec per sprint that Claude Code can execute without ambiguity.

I tested it end-to-end on a real project — a longevity intelligence platform — and the output is in the repo as an example. Every template, filled in, ready to build.

---

## The rule that changes everything

> Never discuss technology before the problem is defined.
> Never design a solution before the finish line is set.
> Never hand a feature to Claude Code without an AI Spec.

That's it. If you follow those three rules, you'll ship the right thing.

CRISP is open source. The repo is here: https://github.com/radekamirko/C.R.I.S.P

Clone it. Drop the `/skills` folder into your Claude Code project. Run the phases. Tell me what breaks.
