# Risk Assessment

**Project:** Znam Coveka
**Date:** 2026-03-24

_Likelihood: H/M/L. Impact: H/M/L. Priority = Likelihood × Impact._

---

## Business Risks

| Risk | Likelihood | Impact | Priority | Mitigation | Owner |
|---|---|---|---|---|---|
| Cold start — no tradies at launch, so no matches, so no homeowners post | H | H | Critical | Founder manually seeds 20+ tradies from Belgrade network before any homeowner marketing. Launch supply before demand. | Mirko |
| Homeowners don't change behaviour — keep calling tradies directly instead of posting | H | H | Critical | Make posting faster than calling. 5-field form, 60 seconds to shortlist. Word-of-mouth from first successful matches is the acquisition channel. | Mirko |
| Toolly adds AI matching — closes the USP gap | M | H | High | Move fast. First-mover advantage in Belgrade is real but time-limited. Get to 50 tradies before Toolly notices the niche. | Mirko |
| Tradie subscription churn — not enough jobs to justify cost | M | H | High | Don't charge until job volume is proven. Manual onboarding at MVP. Only introduce billing after 20+ jobs/week sustained. | Mirko |
| Znam Majstora invests in matching features — brand advantage | L | M | Medium | Their strength is directory scale, not curation. Build reputation for quality before they can react. | Mirko |
| Bad match incident (homeowner unhappy with tradie work quality) | M | M | Medium | Vetting + reviews as quality gates. Admin dispute resolution. Clear expectation-setting in onboarding: "vetted tradies, not guaranteed outcomes." | Mirko |

---

## Technical Risks

| Risk | Likelihood | Impact | Priority | Mitigation | Owner |
|---|---|---|---|---|---|
| Claude API explanation quality is too generic to be the USP | M | H | High | Prompt engineering is critical — test with 20+ real job/tradie pairs before sprint 2 ships. Define quality threshold. | Claude Code |
| URL auto-fill (tradie profile import) fails for most Belgrade tradies (no website / bad GMB) | H | M | High | Treat auto-fill as enhancement, not requirement. Manual profile entry must always work. Auto-fill is the fast path, not the only path. | Claude Code |
| Supabase Realtime messaging drops under load or has high latency | L | M | Medium | Acceptable at MVP scale (<100 concurrent users). Add monitoring. Revisit if messaging becomes unreliable. | Claude Code |
| Google Maps API costs spike unexpectedly | L | M | Medium | Set billing alert at $50/month. MVP volume is well within free tier (28k map loads/month). | Mirko |
| Docker build fails on Railway EU region | L | L | Low | Test deployment pipeline in Sprint 1 before any feature work. | Claude Code |
| Next.js App Router behaviour differs from client expectations (SSR/hydration edge cases) | M | M | Medium | All routes using App Router conventions from sprint 1. No Pages Router patterns allowed — flag immediately if introduced. | Claude Code |

---

## Legal & Compliance Risks

| Risk | Likelihood | Impact | Priority | Mitigation | Owner |
|---|---|---|---|---|---|
| ZZPL (Serbia GDPR-equivalent) violation — user data stored outside EU | L | H | High | Supabase EU region (Frankfurt). Railway EU region. Explicitly documented. No exceptions. | Mirko |
| Personal contact details exchanged between homeowner and tradie outside platform | M | M | Medium | In-platform messaging only. Remind users in onboarding. No phone number / email fields in any user-facing form. | Claude Code |
| No privacy policy / terms of service at launch | H | H | Critical | Draft basic privacy policy before any public launch. Consult a Serbian lawyer. Not a technical task — flagged for Mirko to action. | Mirko |

---

## Security Risks

| Risk | Likelihood | Impact | Priority | Mitigation | Owner |
|---|---|---|---|---|---|
| Unauthorised access to another user's job or message data | L | H | High | Row-level security (RLS) enforced at Supabase level — every query scoped to authenticated user ID. Never rely on client-side checks alone. | Claude Code |
| Admin route accessible to non-admin users | M | H | High | /admin routes protected by server-side role check. Admin role stored in Supabase, not in JWT claims alone. | Claude Code |
| API keys / secrets committed to Git | M | H | High | All secrets in .env.local (never committed). .gitignore verified before first commit. Claude Code must never hardcode secrets. | Claude Code |
| Claude API prompt injection via job description or tradie bio | L | M | Medium | Sanitise all user input before passing to Claude API. System prompt instructs Claude to ignore instructions in user content. | Claude Code |

---

## People & Adoption Risks

| Risk | Likelihood | Impact | Priority | Mitigation | Owner |
|---|---|---|---|---|---|
| Tradies drop off during profile setup (form too long) | H | M | High | URL auto-fill is the primary path. Manual form is chunked into short steps with progress indicator. Max 5 fields visible at once. | Claude Code |
| Homeowner drops off during job posting (form feels like effort) | M | M | Medium | 3-step form, no more than 5 fields per step. Optional fields clearly marked. Progress bar visible throughout. | Claude Code |
| Admin bottleneck — vetting queue backs up | M | M | Medium | AI pre-screen summary reduces review time to < 5 minutes per tradie. Flag if queue exceeds 10 pending. | Mirko |

---

## Human-in-the-Loop Zones (from Phase R)

| Zone | Decision | Why human stays in loop |
|---|---|---|
| Homeowner selects tradie | Homeowner picks from AI shortlist | Trust — homeowner must feel in control. Auto-assignment would destroy trust. |
| Tradie vetting / approval | Admin approves every tradie | Quality gate — AI pre-screens but never approves autonomously. Bad approval = bad match = platform reputation damage. |
| Dispute resolution | Admin mediates | Nuance — disputes involve context AI cannot fully evaluate. Manual at MVP. |
