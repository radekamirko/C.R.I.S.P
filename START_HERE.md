# START HERE — CRISP

Most AI projects fail before a single line of code is written.
Not because the tools were wrong. Because nobody defined the problem.

CRISP fixes that. Five phases, in order, no skipping.

---

## Setup

**Option A — New client project (recommended)**

Create a folder for your project, clone CRISP directly into it, then start Claude:

```bash
mkdir my-project
cd my-project
git clone https://github.com/radekamirko/C.R.I.S.P .
claude
```

The `.` at the end is important — it clones the contents directly into your folder instead of creating a `C.R.I.S.P/` subfolder. Your project folder *is* CRISP. All your discovery docs (`docs/`) will live here alongside the framework.

**Option B — Standalone / demo**

```bash
git clone https://github.com/radekamirko/C.R.I.S.P
cd C.R.I.S.P
claude
```

Just make sure you `cd` into the folder before starting Claude — `/crisp-start` won't work from the parent directory.

---

## Start

Once Claude is running from the right folder:

**Claude Code:**
```
/crisp-start
```

**Any Claude (no slash commands):**
```
Read .claude/skills/phase1-clarify/SKILL.md and begin Phase C.
Don't explain anything. Just ask me about the project.
```

---

## The five phases

| | | |
|---|---|---|
| **C** | Clarify | What problem are we actually solving? |
| **R** | Results | What does success look like? |
| **I** | Investigate | How does the work actually flow? |
| **S** | Spec | What exactly are we building? |
| **P** | Prove | Did the needle move? |

C → R → I → S → P. Each phase has an exit checklist.
If you can't check every box, you're not done.

One rule: never hand a sprint to Claude Code without a locked AI Spec.

---

*Outcome first. Always.*
