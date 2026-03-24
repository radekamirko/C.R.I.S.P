# MVP Prioritization

**Project:** Znam Coveka
**Date:** 2026-03-24
**Method:** HVLE (High Value, Low Effort)

---

## Business Value Criteria & Weights

| Criterion | Weight | Reasoning |
|---|---|---|
| Job volume | 3 | North star metric — no jobs, no platform |
| Revenue | 2 | Tradie subscriptions — deferred at MVP but shapes feature value |
| Tradie retention | 2 | Subscription model lives or dies here |
| Match quality | 3 | The USP — bad matches kill trust fastest |
| Homeowner repeat | 1 | Lagging indicator — follows from match quality |

---

## Effort Sizing Key

| Size | Days | Effort Value |
|---|---|---|
| XS | < 1 day | 0.5 |
| S | 1–2 days | 1.5 |
| M | 3–5 days | 4 |
| L | 7–10 days | 8.5 |
| XL | 10+ days | 12 |

---

## MVP-BASELINE Features (locked — no scoring needed)

These bypass scoring. Either table stakes (every competitor has them) or they are the USP.

| ID | Feature | Reason |
|---|---|---|
| A1–A6 | Auth & onboarding | Table stakes |
| B1–B5 | Tradie profile & vetting | Table stakes + quality gate |
| C1–C4, C6 | Job posting (core) | Table stakes |
| D1–D4 | AI matching engine + explanation | **USP** |
| E1–E4 | Tradie job feed (push + pull) | USP enabler |
| F1, F2, F4 | Selection + confirmation | Core flow |
| G1–G3 | In-platform messaging | Table stakes |
| H1–H3 | Job completion + reviews | Table stakes + trust signal |
| J1, J2 | Admin vetting queue + funnel | Operational requirement |
| K1–K3, K5 | Core notifications | Table stakes |

---

## HVLE Scoring (non-baseline features)

| ID | Feature | Job vol ×3 | Revenue ×2 | Tradie ret ×2 | Match qual ×3 | HO repeat ×1 | Total | Effort | Priority Score | Tag |
|---|---|---|---|---|---|---|---|---|---|---|
| F3 | Tradie notified when not selected | 1 | 1 | 3 | 1 | 1 | 15 | XS (0.5) | 30.0 | **MVP** |
| K4 | HO email when tradie applies | 2 | 1 | 1 | 1 | 2 | 15 | XS (0.5) | 30.0 | **MVP** |
| E5 | Tradie sees jobs they applied to | 1 | 1 | 2 | 1 | 1 | 13 | XS (0.5) | 26.0 | **MVP** |
| B6 | Tradie updates availability | 3 | 2 | 4 | 4 | 1 | 34 | S (1.5) | 22.7 | **MVP** |
| H4 | Rebook same tradie | 3 | 2 | 3 | 1 | 4 | 26 | S (1.5) | 17.3 | **MVP** |
| C5 | Photos on job post | 2 | 1 | 2 | 3 | 2 | 23 | S (1.5) | 15.3 | **MVP** |
| B7 | Tradie updates portfolio | 2 | 1 | 3 | 2 | 1 | 21 | S (1.5) | 14.0 | **MVP** |
| D5/I1 | Record implicit signals | 2 | 1 | 2 | 4 | 2 | 26 | M (4) | 6.5 | **MVP** |
| J3 | Admin platform metrics | 2 | 1 | 1 | 1 | 1 | 14 | M (4) | 3.5 | POST-MVP |
| D6 | Weight preferences in ranking | 2 | 1 | 2 | 5 | 3 | 30 | L (8.5) | 3.5 | POST-MVP |
| I2 | Personalised matching weights | 1 | 1 | 2 | 5 | 3 | 28 | L (8.5) | 3.3 | POST-MVP |

---

## MVP Line

**Above the line → MVP:** F3, K4, E5, B6, H4, C5, B7, D5/I1

**Below the line → POST-MVP:** J3, D6, I2

**Validation:**
- Can someone get real value with only MVP features? ✅ Yes
- Does it deliver the USP (AI matching + explanation)? ✅ Yes
- Can it be built before autumn 2026? ✅ Yes — all MVP items are XS/S/M effort

---

## Dependency Map

| Feature | Depends on | Status |
|---|---|---|
| F3 (not-selected notification) | F1 (homeowner selects) | MVP-BASELINE ✓ |
| K4 (HO email when tradie applies) | E2 (tradie applies) | MVP-BASELINE ✓ |
| E5 (sees applied jobs) | E2 (apply action) | MVP-BASELINE ✓ |
| B6 (update availability) | B1 (set availability) | MVP-BASELINE ✓ |
| H4 (rebook) | H1–H3 (completion + review) | MVP-BASELINE ✓ |
| C5 (photos on job post) | C1 (job posting form) | MVP-BASELINE ✓ |
| B7 (update portfolio) | B2 (photo upload) | MVP-BASELINE ✓ |
| D5/I1 (implicit signals) | D1–D4, H1–H3 | MVP-BASELINE ✓ |

No dependency overrides needed — all dependencies are MVP-BASELINE.
