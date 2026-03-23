# Buy vs Build Matrix

**Project:** Longevity Intelligence Platform
**Date:** 2026-03-23

---

| Tool / Solution | What it covers | Gap | Cost | Decision |
|---|---|---|---|---|
| Whoop | HRV, recovery, sleep | Hardware-locked, no AI memory, no multi-source, no longevity science layer | $239/yr + hardware | Don't buy — competitor reference |
| Oura Ring | Sleep, readiness, HRV | Hardware-locked, single metric focus, no longevity intelligence layer | $99/yr + hardware | Don't buy — competitor reference |
| Levels | CGM / glucose | Single metric, no wearable integration, no memory | $199+/mo | Don't buy — too narrow |
| ChatGPT / Claude (raw) | AI Q&A on longevity topics | No long-term memory, no wearable data integration, no personalization | Free–$20/mo | Configure — use as LLM backbone, build intelligence layer on top |
| Garmin Connect API | Garmin wearable data | Raw data only, no intelligence | Free | Configure — integrate as data source |
| Apple HealthKit | Apple Watch data | Raw data only, no intelligence | Free | Configure — integrate as data source |
| Custom intelligence layer | Memory, context, longevity science curation, personalization | Does not exist as a product | Build cost | **Build** |

## Recommendation

**Build** — configured on top of existing APIs (Garmin, Apple HealthKit, LLM), with a custom intelligence layer that provides long-term memory, context, and longevity science personalization.

## Justification

No existing tool solves the core problem: connecting multi-source wearable data to longevity science with persistent user memory. The data APIs and LLM infrastructure exist and are affordable. The intelligence layer — the thing that makes it personal, continuous, and science-backed — must be built. This is the core differentiator and cannot be bought.
