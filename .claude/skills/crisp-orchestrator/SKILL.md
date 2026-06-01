---
name: crisp-orchestrator
description: CRISP session manager — detects project state and routes to the right entry point. Use /crisp to start or resume any CRISP engagement. Handles new projects (discovery), existing codebases (archaeology), active sprints (execute), and validation (prove). Reads docs/crisp-state.json to know where you are.
---

# CRISP — Session Orchestrator

Before doing anything else, output this exact text verbatim:

  C — Clarify  ·  R — Results  ·  I — Investigate
        S — Spec  ·  P — Prove  ·  E — Execute

        Outcome first. Always.

---

## Step 1: Detect project state

Check if `docs/crisp-state.json` exists.

---

### If `docs/crisp-state.json` does NOT exist → Ask what we're starting

Do not assume. Ask:

> "Starting fresh — two quick questions:
> 1. Do you have an existing codebase, or are we starting from scratch?
> 2. What's the project?"

**If starting from scratch** (no existing code):
- Copy `templates/crisp-state.json` to `docs/crisp-state.json`, set `mode: "discovery"`
- Read `.claude/skills/phase1-clarify/SKILL.md`
- Begin Phase C with: "Tell me about the project — what are you trying to solve, or what did the client brief say?"
- Do not explain the methodology. Just ask.

**If existing codebase** (has code, no docs):
- Copy `templates/crisp-state.json` to `docs/crisp-state.json`, set `mode: "archaeology"`
- Inform the user: "Got it — I'll run CRISP Archaeology to reverse-engineer your codebase into docs. This requires the crisp-archaeology skill. Open your codebase project in Claude Code and say: 'run archaeology on [path]'."
- Do not attempt to run archaeology here — it runs in the target project, not in this repo.

---

### If `docs/crisp-state.json` EXISTS → Read it and route

Read `docs/crisp-state.json`. Check `mode` first, then route.

---

#### Mode: `"discovery"` (standard CRISP phases)

**1. Report current status**

```
Project: [project.name] · Client: [project.client]
Mode: Discovery
─────────────────────────────────────────
Phases complete: [phases.complete joined with " · " — or "None"]
Current phase:   [phases.current]
─────────────────────────────────────────
```

Summarise the current phase state in 2–3 lines:
- Phase C: "Problem defined as [oneSentence]. Go/No-Go: [goNoGo]. Type: [type]."
- Phase R: "Baseline: [baseline]. Target: [successTarget]. [N] HITL zones defined."
- Phase I: "Process track: [processTrack]. User types: [userTypes]. Data mapping: [dataMappingRequired]."
- Phase S: "[sprintCount] sprints planned. Stack: [stack.layers summary]."
- Phase P: "Outcome: [outcome]."

If open questions exist in the current phase, list them before asking what to do next.

**2. Check if ready for Execute**

If `phases.S.complete: true` and `handoffs.ready_for_execute: false`:
> "Phase S is complete. Ready to start building? Say 'Start Sprint 1' to hand off to CRISP Execute."

If the user confirms → update `handoffs.ready_for_execute: true` in `crisp-state.json`.

**3. Route**

| User says | Action |
|---|---|
| Continue / yes / Phase [X] | Load phase SKILL.md and proceed |
| Start Sprint 1 / execute / build | Set `handoffs.ready_for_execute: true`. Route to Execute (see Execute routing below). |
| New project | Ask: overwrite state or new docs/ folder? |
| Show full state | Print crisp-state.json in readable format |
| What's left | List incomplete phases and open questions |

---

#### Mode: `"archaeology"`

**1. Report status**

```
Project: [project.name]
Mode: Archaeology
─────────────────────────────────────────
Recon:       [phases.recon.status]
Strawman:    [phases.strawman.status]
Elicitation: [phases.elicitation.status] ([artifacts.confidence_summary.confirmed] confirmed · [artifacts.confidence_summary.open] open)
Output:      [phases.output.status]
─────────────────────────────────────────
```

**2. Route**

If `handoffs.archaeology_complete: false`:
> "Archaeology is in progress. Open the target codebase in Claude Code and continue with the crisp-archaeology skill."

If `handoffs.archaeology_complete: true` and `handoffs.entry_point_after: "phase-s"`:
> "Archaeology is complete. [N] open questions remain (see docs/open-questions.md). Ready to run Phase S to spec the next phase?"
> Route to Phase S on confirmation.

If `handoffs.archaeology_complete: true` and `handoffs.entry_point_after: "crisp-execute"`:
> "Archaeology is complete. Sprint plan exists. Ready to start building?"
> Route to Execute on confirmation.

---

#### Mode: `"execute"`

**1. Report status**

```
Project: [project.name]
Mode: Execute
─────────────────────────────────────────
Current sprint:   [execute.current_sprint]
Sprints complete: [execute.sprints_complete]
Change requests:  [execute.change_requests.length] queued
─────────────────────────────────────────
```

Show gate status for the current sprint if available:
- Product gate: [execute.gates.sprint_N.product]
- Security gate: [execute.gates.sprint_N.security]

**2. Route**

| User says | Action |
|---|---|
| Continue / start sprint / build | Load `.claude/skills/crisp-execute/SKILL.md` and proceed |
| New requirement: [X] | Route to Execute change request intake |
| Close sprint [N] | Route to Execute sprint close sequence |
| Show change requests | List `execute.change_requests` |
| Go to Phase P / prove | Check all sprints complete, then route to Phase P |

---

#### Mode: `"prove"`

Route to `.claude/skills/phase5-prove/SKILL.md`.

---

## Phase routing table

| Phase / Mode | Skill to load |
|---|---|
| C — Clarify | `.claude/skills/phase1-clarify/SKILL.md` |
| R — Results | `.claude/skills/phase2-results/SKILL.md` |
| I — Investigate | `.claude/skills/phase3-investigate/SKILL.md` |
| S — Spec | `.claude/skills/phase4-spec/SKILL.md` |
| E — Execute | `.claude/skills/crisp-execute/SKILL.md` |
| P — Prove | `.claude/skills/phase5-prove/SKILL.md` |
| Archaeology | Runs in target project via `crisp-archaeology` skill (separate repo) |

---

## crisp-state.json handoff signals

The orchestrator reads and writes these fields to coordinate between modes:

| Field | Set by | Meaning |
|---|---|---|
| `mode` | Orchestrator on create | Which system is active |
| `handoffs.discovery_complete` | Phase S exit | All phases done, ready for execute |
| `handoffs.archaeology_complete` | Archaeology skill | Archaeology finished, ready to proceed |
| `handoffs.ready_for_execute` | Orchestrator | Spec is locked, execute can start |
| `handoffs.execute_complete` | Execute skill | All sprints done, ready for prove |
| `execute.current_sprint` | Execute skill | Which sprint is active |
| `execute.gates.sprint_N` | Execute skill | Gate results per sprint |
| `execute.change_requests` | Execute skill | Queued change requests |

---

## Rules

- Never skip a phase without explicit user instruction.
- If a phase is marked complete but the user wants to re-run it — allow it, flag: *"Phase [X] is marked complete. Running again won't reset state automatically."*
- If `crisp-state.json` has open questions — surface them before starting the next phase.
- If phases are out of order — flag it: *"Phase R isn't marked complete. Running Phase S without it means some pre-fills will be missing. Continue anyway?"*
- If `execute.change_requests` has queued items when a sprint opens — surface them: *"[N] change requests are queued. Review before sprint starts?"*
- Keep responses tight. Status reporting is a tool, not a presentation.
