# Logging Spec

**Project:**
**Date:**
**Sprint:**

---

> Logging is what tells you what happened when production breaks at 2am.
> Define it here, before the build. Not after.

---

## Log Levels

| Level | When to use | Examples |
|---|---|---|
| `ERROR` | Something failed — user impact likely | DB write failed, API call returned 5xx, unhandled exception |
| `WARN` | Something unexpected — no user impact yet | Retry attempted, fallback triggered, deprecated usage |
| `INFO` | Normal significant events | User authenticated, job started/completed, record created |
| `DEBUG` | Developer detail — not in production by default | Function inputs/outputs, query parameters, state changes |

**Default production log level:** `INFO` (DEBUG disabled unless explicitly turned on)

---

## What Gets Logged

### Always log
- [ ] Every API request — method, endpoint, status code, response time (no body — see PII rules)
- [ ] Every authentication event — login, logout, token refresh, failed attempt
- [ ] Every background job — start, completion, failure (with job ID)
- [ ] Every unhandled exception — full stack trace + context
- [ ] Every 3rd party API call — service name, endpoint, status (no keys or secrets in logs)
- [ ] Every DB write operation that modifies critical data — record ID, operation type, actor

### Never log
- [ ] Passwords, tokens, API keys, secrets — ever
- [ ] PII unless explicitly required by compliance and masked/hashed (name, email, phone, address)
- [ ] Full request/response bodies containing user data
- [ ] Credit card numbers, financial data, health records

### Log with care (mask or hash if included)
- User IDs — OK to log as reference
- Email addresses — mask to `u***@domain.com` format if needed for debugging
- Session tokens — log only the last 6 characters for tracing

---

## Log Format

**Structured JSON — mandatory for production:**

```json
{
  "timestamp": "2026-04-16T14:23:01.000Z",
  "level": "INFO",
  "service": "[service-name]",
  "event": "[event-name]",
  "message": "Human-readable description",
  "requestId": "uuid-per-request",
  "userId": "optional-user-ref",
  "durationMs": 142,
  "metadata": {}
}
```

- Every request gets a `requestId` — generated at entry point, passed through all downstream calls
- `userId` is optional — include when an authenticated user is the actor
- `metadata` is for event-specific context — keep it flat, no nested PII

---

## Log Destination

- [ ] **Local development:** Console / stdout
- [ ] **Staging:** File (`logs/app.log`) + console
- [ ] **Production:** _(choose one or both)_
  - [ ] Log aggregation service: _(e.g. Datadog, Logtail, Papertrail, CloudWatch)_
  - [ ] File with rotation: max size ___MB, retain ___ days

**Log rotation rules (if file-based):**
- Rotate daily or at ___MB — whichever comes first
- Retain for ___ days
- Compress rotated files

---

## Alerting

| Condition | Alert channel | Severity |
|---|---|---|
| ERROR rate > ___/min | | 🔴 Critical |
| 3rd party API failure | | 🟠 High |
| Background job failed | | 🟠 High |
| Auth failure spike | | 🟠 High |
| Warn rate > ___/min | | 🟡 Medium |

---

## Sprint Quality Gate

Before a sprint is marked complete, confirm:
- [ ] Logging implemented for all new API endpoints
- [ ] Logging implemented for all new background jobs
- [ ] No PII in logs — verified by code review
- [ ] No secrets or keys in logs — verified by code review
- [ ] Log destination configured for the target environment
- [ ] At least one ERROR-level log with test trigger exists and outputs correctly
