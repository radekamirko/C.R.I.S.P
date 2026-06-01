# Sprint [N] Delta — [Date]

**Project:** 
**Sprint goal:** 
**Date range:** [start → close]

---

## What was specced vs what shipped

| US ID | Story | Specced | Shipped | Delta |
|---|---|---|---|---|
| US-01 | | ✅ | ✅ | None |
| US-02 | | ✅ | ❌ | [reason — slipped to Sprint N+X] |

---

## Scope that slipped

| US ID | Story | Reason | New sprint |
|---|---|---|---|
| | | | |

_(If nothing slipped, write: None.)_

---

## Change requests received this sprint

| ID | Description | Classification | Slotted to | Notes |
|---|---|---|---|---|
| CR-001 | | New feature / Scope change / Bug fix | Sprint N+X | |

_(If none received, write: None.)_

---

## Product gate result

**Result:** ✅ Passed / ❌ Failed

| US ID | Acceptance Criteria | Result | Notes |
|---|---|---|---|
| US-01 | | ✅ | |
| US-02 | | ❌ | [what failed] |

---

## Security gate result

**Result:** ✅ Passed / ❌ Failed

**Bearer scan:**
- Critical findings: [N] — [list or "None"]
- High findings: [N] — [list or "None"]
- Medium findings: [N] — [list or acknowledged mitigation]

**Manual security checklist:**
- [ ] No secrets/API keys on client side
- [ ] All credential-bearing calls server-side
- [ ] No sensitive data logged
- [ ] Input validation on all backend-facing inputs
- [ ] Auth checks on all protected routes built this sprint
- [ ] HTTPS enforced for all external calls
- [ ] New dependencies checked for CVEs

**Agent governance (if applicable):**
- [ ] Agent permissions scoped to minimum required
- [ ] Sensitive operations require explicit confirmation
- [ ] Agent outputs validated before acting on them
- [ ] Failure modes documented
- [ ] Audit trail exists

**Prompt injection (if applicable):**
- [ ] No raw user input injected into system prompts
- [ ] Prompt boundaries clearly defined

---

## Open items going into Sprint [N+1]

| Item | Type | Owner | Notes |
|---|---|---|---|
| | Slipped story / Unresolved finding / Blocked dep | | |

_(If none, write: None.)_

---

## Notes

_(Anything worth remembering that doesn't fit above.)_
