# Stakeholder Register

**Project:** Znam Coveka
**Date:** 2026-03-24

---

| Stakeholder | Role | Impact | Change for them | Notes |
|---|---|---|---|---|
| Homeowner | Posts jobs, receives shortlist, selects tradie, confirms completion | High positive | Better — faster, confident decision, no cold calls, no waiting months | Primary demand side. Behaviour change required: post a job instead of Googling or asking friends. |
| Tradie (painter / plumber) | Receives matched jobs, completes work, builds reputation, pays subscription | High positive (long-term) / friction on entry | Better overall, but initial trust barrier before first matched job arrives | Risk: early churn if first job takes too long to arrive. Availability must be a first-class profile field. |
| Founder / Admin (Mirko) | Vets tradies, approves profiles, handles disputes, seeds Belgrade supply | High operational load | More work before automation is possible | Manual vetting does not scale past ~100 tradies without process investment. Flag this before Series A sprint. |

---

## Human-in-the-Loop Zones

| Zone | Who decides | AI role | Human role |
|---|---|---|---|
| Tradie selection | Homeowner | Generates shortlist of 3 + explanation of fit | Final pick always human — AI never auto-assigns |
| Tradie vetting / approval | Admin (Mirko) | Pre-screens profile completeness, portfolio, flags inconsistencies | Human approves every tradie before they go live on platform |
| Dispute resolution | Admin (Mirko) | N/A at MVP | Human handles all homeowner / tradie disputes manually |

---

## Baseline Measurements

| Metric | Current value | Source | Notes |
|---|---|---|---|
| Time for homeowner to find a tradie | Hours to days of searching | Client-stated, validated by market research | Google + word of mouth + cold calls |
| Time from search to job start | Days searching + 4-6 week wait | Client-stated | Availability is the primary bottleneck, not discovery |
| Tradie bid win rate (on lead platforms) | ~10-20% | Industry benchmarks (Thumbtack/Bark review mining) | 30-60 mins wasted per bid, lose primarily on price |
| Homeowner frustration score | 8/10 | Inferred from client context and review mining | High frustration, low confidence in outcome |
| Manual steps (homeowner) | Google → call 3-5 numbers → wait for callbacks → compare with no real info → book → wait weeks | Process walkthrough | 5-7 manual steps, high drop-off risk at each |

---

## Success Targets (Month 6, Belgrade)

| Metric | Baseline | Target | Type |
|---|---|---|---|
| Time to receive shortlist | Hours to days | < 5 minutes | Absolute |
| Time from job posted to job started | Days + 4-6 weeks | < 1 week | Absolute |
| Active tradies on platform | 0 | 50 | Absolute |
| Jobs posted per week | 0 | 20+ | Absolute |
| Jobs matched (shortlist sent) | 0 | > 80% of posted jobs | % of funnel |
| Jobs completed (confirmed by homeowner) | 0 | > 60% of matched jobs | % of funnel |
| Match acceptance rate (tradie accepts) | N/A | > 60% | % |
| Tradie subscription retention (month 2+) | N/A | > 70% | % |
| Homeowner repeat usage | N/A | > 40% | % |

### Job Funnel (North Star)
```
Jobs posted → Jobs matched → Jobs accepted → Jobs completed
    20+/wk       > 80%           > 60%           > 60%
```
Jobs posted per week is the primary health metric. Everything else flows from it.

---

## Second-Order Effects

| Primary metric improves | Second-order effect |
|---|---|
| Tradie retention high → tradies get consistent work | Word of mouth brings more tradies — supply grows without paid acquisition |
| Homeowner repeat usage high | Average jobs per tradie increases → subscription value goes up → justifies price increase |
| Jobs completed rate high | Trust signal builds → homeowners refer platform to friends → demand grows organically |
| Availability as first-class field | Matching quality improves → acceptance rate goes up → tradies see faster ROI on subscription → retention improves |
