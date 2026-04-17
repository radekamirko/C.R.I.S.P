# Agent Security Spec

**Project:**
**Agent name / description:**
**Date:**

---

> Use this template for every AI agent in scope.
> Agents have autonomy, system access, and persistent state.
> The same properties that make them valuable make them risky.
> If you don't define the permission boundary in the spec, Claude will make it up.
>
> Aligned with AIUC-1 enterprise AI agent security standard (aiuc-1.com).
> Required fields cover: Identity & Permissions, Data Handling, Failure Modes.

---

## 1. Identity & Permissions

### What this agent is allowed to do autonomously

> List every action the agent can take without human approval.
> If it's not listed here, it requires human approval.

| Action | Scope / Limits | Example |
|---|---|---|
| Read data | Which tables / APIs / files | Read orders table, read-only |
| Write data | Which tables / fields | Update status field only |
| Call external APIs | Which services | Send email via SendGrid |
| Trigger workflows | Which workflows | Start invoice generation job |
| | | |

### What this agent is explicitly NOT allowed to do

> Hard boundaries — the agent must never cross these, even if instructed.

- [ ] Delete records from the database
- [ ] Access tables / systems not listed above
- [ ] Expose raw user data in responses
- [ ] Call external APIs not listed above
- [ ] Make financial transactions autonomously
- _(add project-specific prohibitions)_

### Auth model

**How does the agent authenticate?**
_(Service account / API key / OAuth token / user session delegation)_

**Credential scope:**
_(Read-only / scoped write / admin — use least privilege)_

**Credential storage:**
_(Environment variable name — never hardcoded)_

**Token expiry and rotation:**
_(How often do credentials rotate? Who owns rotation?)_

### Human approval gates

> Pulled from `docs/stakeholder-register.md` HITL zones — expanded for agent context.

| Action | Approval required from | Trigger condition |
|---|---|---|
| | | e.g. value > €500 |
| | | e.g. affects >10 records |
| | | e.g. irreversible operation |

---

## 2. Data Handling

### Does this agent process PII?

- [ ] Yes — specify below
- [ ] No

**PII types in scope:**
_(Names / emails / phone numbers / addresses / financial data / health data / other)_

**PII handling rules:**
- Never log PII — mask or omit from all log entries
- Never include PII in agent reasoning traces or debug output
- Never send PII to external APIs unless explicitly required and documented
- PII stored only in fields defined in data schema — no free-text storage of PII

### Does this agent log conversations / interactions?

- [ ] Yes — specify retention period and access controls:
- [ ] No

**Retention period:**
**Who can access logs:**
**Is this disclosed to users?** Yes / No

### Does this agent train on user data?

- [ ] Yes — specify:
- [ ] No

### Data residency

**Where does agent-processed data live?**
_(Cloud provider, region — cross-check with `docs/problem-statement.md` constraints)_

---

## 3. Failure Modes

> What happens when the agent can't complete the task?
> Define this before building — a silent failure is worse than a loud one.

### Failure scenarios

| Scenario | Agent behaviour | Human notification | Fallback |
|---|---|---|---|
| External API unavailable | | | |
| DB write fails | | | |
| Input data malformed / missing | | | |
| Agent exceeds token / cost limit | | | |
| Agent produces low-confidence output | | | |
| Agent loop exceeds max steps | | | |

### Alerting

**Who gets notified on agent failure?**
**Notification channel:** _(email / Slack / webhook / log alert)_
**Severity threshold for alert:** _(every failure / repeated failure / critical only)_

### Human handoff

**When the agent fails, what does the human do?**
_(Specific fallback process — not "handle manually")_

**Is the fallback documented somewhere the human can find it?**
- [ ] Yes → location:
- [ ] No → document it before sprint starts

### Audit trail

**Are all agent actions logged with enough detail to reconstruct what happened?**
- [ ] Yes — every action logged with: timestamp, action type, input summary, output summary, actor (agent ID)
- [ ] No → add to sprint scope before build

---

## Open Questions

> All must be answered before the sprint that builds this agent starts.

- [ ]
- [ ]
- [ ]
