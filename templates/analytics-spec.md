# Analytics Spec — GA4

**Project:**
**Date:**
**Sprint:**

---

> Analytics are not a post-launch task.
> If you don't define what to measure before you build, you'll build the wrong thing and never know it.
> Every success metric from Phase R needs a GA4 event that fires when it happens.

---

## GA4 Setup

**Measurement ID:** `G-XXXXXXXXXX`
_(Add to `CLAUDE.md` environment variables once issued)_

**Implementation method:**
- [ ] gtag.js (script tag)
- [ ] Google Tag Manager
- [ ] GA4 SDK (mobile — Firebase)

**Data stream:** Web / iOS / Android / All

**Environments:**
| Environment | Tracking | Measurement ID |
|---|---|---|
| Development | Disabled (or separate property) | |
| Staging | Separate GA4 property | |
| Production | Live property | `G-XXXXXXXXXX` |

---

## Conversion Goals

> Pulled from `docs/success-metrics.md` — every success target needs a corresponding GA4 conversion event.

| Success metric (Phase R) | GA4 conversion event | Description |
|---|---|---|
| | | |
| | | |

---

## Event Map

> One row per event. Be specific — vague events produce useless data.
> Event names: lowercase, underscores, max 40 chars. No spaces.

### Authentication & Onboarding

| Event name | Trigger | Parameters | Sprint |
|---|---|---|---|
| `sign_up` | User completes registration | `method` (email/google/etc) | |
| `login` | User successfully authenticates | `method` | |
| `onboarding_step_complete` | User completes an onboarding step | `step_name`, `step_number` | |
| `onboarding_complete` | User completes full onboarding flow | | |

### Core Product Actions

_(Add events specific to your product here)_

| Event name | Trigger | Parameters | Sprint |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### Engagement

| Event name | Trigger | Parameters | Sprint |
|---|---|---|---|
| `feature_used` | User interacts with a key feature | `feature_name` | |
| `search_performed` | User submits a search | `search_term` (if not PII) | |

### Errors & Friction

| Event name | Trigger | Parameters | Sprint |
|---|---|---|---|
| `form_error` | Form submission fails validation | `form_name`, `error_type` | |
| `api_error_shown` | User sees an error message | `error_code`, `screen` | |

### Conversion / Monetisation

| Event name | Trigger | Parameters | Sprint |
|---|---|---|---|
| `purchase` | _(GA4 standard — do not rename)_ | `value`, `currency`, `items` | |
| `begin_checkout` | User enters checkout flow | `value`, `currency` | |

---

## Custom Dimensions & Metrics

> Needed when you want to segment reports beyond GA4 defaults.

| Name | Scope | Type | Description |
|---|---|---|---|
| `user_plan` | User | String | Free / Pro / Enterprise |
| `user_id` | User | String | Internal user ID (not PII — use hashed or internal ref) |
| | | | |

---

## PII Rules — Non-Negotiable

- **Never send PII to GA4.** No names, emails, phone numbers, addresses.
- User IDs must be hashed or use an internal reference — never raw.
- Search terms: only track if confirmed non-PII for this product.
- Form field values: never tracked, even on error events.
- If in doubt: omit the parameter, not the event.

---

## Implementation Rules for Claude Code

Add to `CLAUDE.md` and reference in every sprint's AI Spec:

- Every new feature in scope must implement its events from this spec before the sprint is complete.
- No analytics code in components — use a centralised `analytics.ts` / `analytics.js` utility.
- All `gtag()` / `logEvent()` calls go through the utility. Never call GA4 directly from UI components.
- Test every event in GA4 DebugView before marking the sprint done.
- Events not in this spec require sign-off before implementation.

---

## Sprint Quality Gate

Before a sprint is marked complete:
- [ ] All events listed for this sprint are implemented
- [ ] All events verified firing in GA4 DebugView
- [ ] No PII in any event parameters — confirmed by code review
- [ ] Conversion events verified as goals in GA4 property settings
