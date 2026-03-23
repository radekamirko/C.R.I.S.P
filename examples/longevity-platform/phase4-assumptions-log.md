# Assumptions Log

**Project:** Longevity Intelligence Platform
**Date:** 2026-03-23

> Assumptions are things we believe to be true but haven't verified yet.
> Track them — wrong assumptions are the #1 cause of project failure.

---

| # | Assumption | Category | Risk if wrong | How to validate | Status |
|---|---|---|---|---|---|
| A1 | Garmin Health API is accessible to individual developers without enterprise agreement | Technical | High — core data source blocked | Check Garmin developer portal and apply for access immediately | Unvalidated |
| A2 | Apple HealthKit can be accessed via Expo without a full native build | Technical | High — may need ejecting from Expo managed workflow | Build a minimal HealthKit test in Expo and verify read access | Unvalidated |
| A3 | Open-Meteo provides sufficient weather accuracy for the user's location | Technical | Low — can swap to another provider | Test Open-Meteo against known location for 3 days | Unvalidated |
| A4 | Claude vision (or GPT-4o vision) can identify common meal items with >80% accuracy | Technical | High — core UX of nutrition loop depends on this | Run 20 test meal photos through the model and measure accuracy | Unvalidated |
| A5 | Target users (35-50+) are willing to complete a 5-minute onboarding including baseline indicators | User | Medium — drop-off at onboarding kills activation | User interview with 3-5 people matching profile before Sprint 1 ships | Unvalidated |
| A6 | The "information not advice" framing is sufficient to stay outside FTC health claim enforcement | Legal | High — product could require significant reframing or legal review | Brief a US-based health/consumer law attorney before public launch | Unvalidated |
| A7 | Supabase free tier is sufficient for POC data volumes | Technical | Low — cost, not blocking | Monitor usage during Sprint 1; upgrade plan is straightforward | Unvalidated |
| A8 | Users will perceive the longevity score as motivating rather than anxiety-inducing | User | Medium — wrong framing could cause harm or churn | User test the score UI with 3 beta users before Sprint 5 ships | Unvalidated |
| A9 | The glycemic index and inflammation data embedded in the science layer is sufficiently accurate and current | Technical | High — core science credibility of the platform | Curate RAG content from peer-reviewed sources only (PubMed, etc.) and have reviewed by a qualified nutritionist | Unvalidated |
| A10 | React Native (Expo) camera API is sufficient for meal photo capture quality | Technical | Low — standard use case | Test camera + vision model pipeline in Sprint 4 spike | Unvalidated |

---

## Invalidated Assumptions

_(Move here when proven wrong — and update the plan)_

| # | Assumption | Impact | Action taken |
|---|---|---|---|
| — | — | — | — |
