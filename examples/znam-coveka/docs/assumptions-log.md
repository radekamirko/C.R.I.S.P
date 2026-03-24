# Assumptions Log

**Project:** Znam Coveka
**Date:** 2026-03-24

_Rating: High = wrong → project fails or pivots. Medium = wrong → rework. Low = wrong → minor adjustment._

---

| ID | Assumption | Source | Risk Rating | Status | Resolution |
|---|---|---|---|---|---|
| AS-01 | Homeowners in Belgrade will post jobs on a web platform rather than calling or asking friends | docs/problem-statement.md — behaviour change required | High | Unvalidated | Validate with 5 homeowner interviews before sprint 3 |
| AS-02 | Painters and plumbers in Belgrade will pay a subscription fee for access to a pre-qualified job pipeline | docs/problem-statement.md — monetisation model | High | Unvalidated | Validate by manually onboarding 10 tradies before billing sprint |
| AS-03 | Claude API can generate a convincing, specific match explanation from job description + tradie profile data alone | docs/process-flow.md — matching engine | High | Unvalidated | Build and test explanation quality in Sprint 2 before committing to it as the USP |
| AS-04 | Tradie websites and Google My Business pages contain enough structured data for Claude API to auto-fill a useful profile | docs/ux-discovery.md — URL auto-fill feature | Medium | Unvalidated | Test with 10 real Belgrade tradie URLs before making auto-fill the primary path |
| AS-05 | Google Maps API autocomplete returns accurate results for Belgrade addresses | docs/buy-vs-build-matrix.md | Low | Unvalidated | Test during Sprint 1 setup |
| AS-06 | Supabase EU region is available and sufficient for Serbian ZZPL compliance | docs/problem-statement.md — legal constraints | Medium | Assumed | Confirm Supabase EU region availability before data model build |
| AS-07 | Railway EU region deployment is stable and meets latency requirements for Belgrade users | docs/buy-vs-build-matrix.md | Low | Assumed | Test latency from Belgrade post-deployment |
| AS-08 | Homeowners are willing to share their job location (map pin) as part of posting | docs/process-flow.md — job posting flow | Medium | Unvalidated | Monitor drop-off at location step in job posting form |
| AS-09 | Tradies will have availability to respond to matched jobs within 24 hours | docs/stakeholder-register.md — 1-week job start target | Medium | Unvalidated | Add availability response SLA to tradie onboarding expectation-setting |
| AS-10 | A solo admin (Mirko) can vet tradies manually within 24 hours at MVP scale | docs/stakeholder-register.md — admin load | Medium | Assumed | Holds for first 50 tradies. Flag when volume exceeds 10 applications/week |
| AS-11 | Resend free tier (3,000 emails/month) is sufficient for MVP notification volume | docs/buy-vs-build-matrix.md | Low | Assumed | Monitor — upgrade to paid tier when 200+ active users |
| AS-12 | Homeowners will complete the 3-question preference onboarding without dropping off | docs/ux-discovery.md — onboarding design | Medium | Unvalidated | A/B test with 2 vs 3 questions if drop-off is observed |
| AS-13 | The hybrid matching model (AI push + tradie pull) will not create confusion about which shortlist is "official" | docs/process-flow.md — hybrid matching | Medium | Unvalidated | UX solution: AI shortlist is primary, applications are secondary — monitor homeowner behaviour |
| AS-14 | Supabase Realtime is sufficient for in-platform messaging at MVP scale | docs/buy-vs-build-matrix.md | Low | Assumed | Holds for < 500 concurrent users. Revisit if scale demands it |
