# Process Flow

**Project:** Znam Coveka
**Date:** 2026-03-24
**Track:** B — Greenfield (new product)

---

## Overview

Three parallel tracks that converge at the job matching layer:
1. Homeowner track — post job, receive matches, select tradie, confirm completion
2. Tradie track — apply, get vetted, browse jobs or receive matches, complete work
3. Admin track — vet tradies, monitor job funnel, handle disputes

---

## Track 1: Homeowner

```
[Sign up]
    └─ OAuth (Google / Apple) — frictionless, no password
    └─ Collect tradie preferences during onboarding:
       - What matters most? (speed / price / reviews / experience)
       - Implicit signals begin accumulating from first job

[Post a job]
    └─ Trade type (painter / plumber / etc.)
    └─ Job description (free text)
    └─ Location (Belgrade address or area)
    └─ Availability window (when can the tradie come?)
    └─ Photos (optional)
    └─ Job preferences collected here:
       - Budget range
       - Urgency
       - Disruption tolerance

[Receive shortlist]
    └─ AI matching engine runs (see Matching Engine below)
    └─ Homeowner receives 2-3 curated matches
    └─ Each match includes: tradie profile + AI-generated explanation of fit
    └─ Also visible: any tradie applications (pull track) for this job

[Select tradie]
    └─ Homeowner picks one (human decision — never auto-assigned)
    └─ Selected tradie notified
    └─ Unselected tradies notified (job filled)

[Job in progress]
    └─ In-platform messaging (no personal contact exchanged)
    └─ Start date/time agreed via platform

[Confirm completion]
    └─ Homeowner marks job complete
    └─ Leaves review + rating for tradie
    └─ Implicit signal recorded: who was picked, rating given, repeat booking indicator
```

---

## Track 2: Tradie

```
[Sign up + profile]
    └─ Trade type(s)
    └─ Service area (Belgrade zones)
    └─ Availability (calendar / general availability)
    └─ Portfolio (past work photos)
    └─ Bio + years of experience
    └─ Pricing indication (optional)

[Vetting — Admin]
    └─ AI pre-screens: profile completeness, portfolio quality, flags inconsistencies
    └─ Human (Admin) reviews and approves or rejects
    └─ Approved → goes live on platform

[Receive matched jobs — Push]
    └─ AI matching engine selects tradie for a job
    └─ Tradie notified of match (email + in-app)
    └─ Tradie accepts or declines

[Browse open jobs — Pull]
    └─ Tradie sees job feed (filtered by their trade + location)
    └─ Tradie applies to a job
    └─ Application visible to homeowner alongside AI shortlist

[Complete job]
    └─ Job confirmed, start date agreed
    └─ Job completed
    └─ Homeowner confirms + reviews
    └─ Tradie rating updated → feeds future matching rank
```

---

## Track 3: Admin (Mirko)

```
[Tradie application received]
    └─ AI pre-screen flags summary presented to admin
    └─ Admin reviews profile + portfolio
    └─ Approves → tradie goes live
    └─ Rejects → tradie notified with reason

[Monitor job funnel]
    └─ Jobs posted / matched / accepted / completed (dashboard)
    └─ Flag stalled jobs (posted but not matched, matched but not accepted)

[Dispute resolution]
    └─ Homeowner or tradie raises issue
    └─ Admin reviews, mediates, resolves manually
    └─ Resolution logged on job record
```

---

## Matching Engine

```
INPUT
    └─ Job: trade type, location, description, availability window, homeowner preferences

FILTER
    └─ Trade type matches tradie's registered trade(s)
    └─ Location within tradie's service area
    └─ Tradie availability overlaps with homeowner's window
    └─ Tradie is approved and active on platform

RANK
    └─ Rating / review score
    └─ Job fit (description vs portfolio + past job types)
    └─ Homeowner preference alignment (speed / price / experience weighting)
    └─ Implicit signals from homeowner's past picks

SELECT
    └─ Top 2-3 tradies selected

EXPLAIN
    └─ Claude API generates a personalised explanation per tradie:
       "We matched Marko because he's completed 8 bathroom plumbing jobs in Vračar,
        has a 4.9 rating, and is available from Thursday."

OUTPUT
    └─ Shortlist of 2-3 tradies with explanations → presented to homeowner
```

---

## Preference Learning Loop

```
Homeowner onboarding  →  explicit tradie preferences captured
Job posting           →  explicit job preferences captured
Job completion        →  implicit signals recorded:
                          - which tradie selected
                          - rating given
                          - repeat booking with same tradie
                          - response time to shortlist
Matching engine       →  weights adjusted per homeowner over time
```
