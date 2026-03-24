# Initial Backlog

**Project:** Znam Coveka
**Date:** 2026-03-24

_MVP tags applied in docs/mvp-prioritization.md. Tags shown here are final after HVLE scoring._

---

## Epics and User Stories

---

### Epic 1: Authentication & Onboarding

**Goal link:** Goal 1 (homeowner shortlist in < 5 min), Goal 2 (tradie pipeline access)

| ID | User Story | MVP Tag |
|---|---|---|
| A1 | As a homeowner, I want to sign in with Google or Apple in one tap so that I can start using the platform without creating a password | MVP-BASELINE |
| A2 | As a tradie, I want to sign up with email so that I can create an account and submit my profile | MVP-BASELINE |
| A3 | As a homeowner, I want to set my tradie preferences during onboarding (3 questions) so that the platform learns what matters to me from the start | MVP-BASELINE |
| A4 | As a tradie, I want to paste my website or Google My Business URL so that my profile is auto-filled without manually entering every field | MVP-BASELINE |
| A5 | As a tradie, I want to review and edit my auto-filled profile before submitting so that I can correct any errors from the import | MVP-BASELINE |
| A6 | As a user, I want to receive a confirmation when my profile is submitted so that I know what happens next | MVP-BASELINE |

---

### Epic 2: Tradie Profile & Vetting

**Goal link:** Goal 2 (tradie pipeline), Goal 4 (job funnel health)

| ID | User Story | MVP Tag |
|---|---|---|
| B1 | As a tradie, I want to set my trade type(s), service area, and availability so that I am matched to relevant jobs | MVP-BASELINE |
| B2 | As a tradie, I want to upload portfolio photos so that homeowners can see my work quality | MVP-BASELINE |
| B3 | As an admin, I want to see an AI pre-screen summary of each tradie application so that I can make vetting decisions faster | MVP-BASELINE |
| B4 | As an admin, I want to approve or reject a tradie profile with one action so that the vetting queue stays manageable | MVP-BASELINE |
| B5 | As a tradie, I want to receive an email notification when my profile is approved or rejected so that I know when I can start getting jobs | MVP-BASELINE |
| B6 | As a tradie, I want to update my availability at any time so that I only receive matched jobs I can actually take | MVP |
| B7 | As a tradie, I want to update my portfolio photos after approval so that my profile stays current | MVP |

---

### Epic 3: Job Posting

**Goal link:** Goal 1 (shortlist in < 5 min), Goal 4 (20+ jobs/week)

| ID | User Story | MVP Tag |
|---|---|---|
| C1 | As a homeowner, I want to select a trade type and describe my job so that the platform knows what I need | MVP-BASELINE |
| C2 | As a homeowner, I want to pin my job location on a map so that tradies in my area are matched | MVP-BASELINE |
| C3 | As a homeowner, I want to set my availability window so that I am only matched to tradies who can come when I'm free | MVP-BASELINE |
| C4 | As a homeowner, I want to specify my budget range and urgency so that the matching reflects my priorities | MVP-BASELINE |
| C5 | As a homeowner, I want to attach photos to my job post so that the tradie understands the scope before arriving | MVP |
| C6 | As a homeowner, I want to see a confirmation that my job is live and matching is running so that I'm not left wondering | MVP-BASELINE |

---

### Epic 4: AI Matching Engine

**Goal link:** Goal 1 (shortlist < 5 min), Goal 5 (preference learning)

| ID | User Story | MVP Tag |
|---|---|---|
| D1 | As a homeowner, I want to receive a shortlist of 2-3 matched tradies within 60 seconds of posting a job so that I can make a decision quickly | MVP-BASELINE |
| D2 | As a homeowner, I want each matched tradie to come with an AI-generated explanation of why they fit my job so that I can make a confident decision | MVP-BASELINE |
| D3 | As the system, I want to filter tradies by trade type, location, and availability before ranking so that shortlists only contain tradies who can actually do the job | MVP-BASELINE |
| D4 | As the system, I want to rank tradies by rating, job fit, and homeowner preferences so that the best match appears first | MVP-BASELINE |
| D5 | As the system, I want to record implicit signals (who was selected, rating given, repeat bookings) so that matching improves over time | MVP |
| D6 | As the system, I want to weight homeowner preference data in the ranking algorithm so that matches get more personalised over time | POST-MVP |

---

### Epic 5: Tradie Job Feed (Pull)

**Goal link:** Goal 2 (tradie pipeline), Goal 4 (job funnel)

| ID | User Story | MVP Tag |
|---|---|---|
| E1 | As a tradie, I want to see a feed of open jobs filtered to my trade and service area so that I can find jobs to apply for | MVP-BASELINE |
| E2 | As a tradie, I want to apply to an open job with one tap so that I can express interest quickly | MVP-BASELINE |
| E3 | As a tradie, I want to see my matched jobs (push) at the top of the feed so that I can respond to the best opportunities first | MVP-BASELINE |
| E4 | As a tradie, I want to receive a notification when I am matched to a job so that I can respond before another tradie applies | MVP-BASELINE |
| E5 | As a tradie, I want to see which jobs I've already applied to so that I don't apply twice | MVP |

---

### Epic 6: Selection & Confirmation

**Goal link:** Goal 1 (job start < 1 week), Goal 4 (job funnel)

| ID | User Story | MVP Tag |
|---|---|---|
| F1 | As a homeowner, I want to select a tradie from my shortlist so that the job is assigned | MVP-BASELINE |
| F2 | As a tradie, I want to receive a notification when a homeowner selects me so that I can prepare for the job | MVP-BASELINE |
| F3 | As a tradie, I want to see notifications when I am not selected so that I know the job is filled | MVP |
| F4 | As a homeowner, I want to see a clear confirmation after selecting a tradie so that I know what happens next | MVP-BASELINE |

---

### Epic 7: In-Platform Messaging

**Goal link:** Goal 1 (job start < 1 week)

| ID | User Story | MVP Tag |
|---|---|---|
| G1 | As a homeowner and tradie, I want to message each other within the platform so that we can arrange the job without sharing personal contact details | MVP-BASELINE |
| G2 | As a user, I want to receive a notification when I have a new message so that I respond promptly | MVP-BASELINE |
| G3 | As a user, I want to see the full message history for each job so that context is never lost | MVP-BASELINE |

---

### Epic 8: Job Completion & Reviews

**Goal link:** Goal 4 (completion rate), Goal 5 (preference learning)

| ID | User Story | MVP Tag |
|---|---|---|
| H1 | As a homeowner, I want to mark a job as complete so that the tradie can receive their reputation credit | MVP-BASELINE |
| H2 | As a homeowner, I want to leave a star rating and optional review for the tradie so that future homeowners can benefit | MVP-BASELINE |
| H3 | As a tradie, I want to see new reviews appear on my profile immediately so that my reputation is up to date | MVP-BASELINE |
| H4 | As a homeowner, I want to rebook the same tradie with one tap after a completed job so that good relationships are easy to continue | MVP |

---

### Epic 9: Preference Learning

**Goal link:** Goal 5 (smarter matching over time)

| ID | User Story | MVP Tag |
|---|---|---|
| I1 | As the system, I want to record which tradie was selected, the rating given, and whether rebooking occurred after each job so that implicit signals accumulate | MVP |
| I2 | As the system, I want to adjust matching weights per homeowner based on accumulated signals so that recommendations improve without asking for extra input | POST-MVP |

---

### Epic 10: Admin Dashboard

**Goal link:** Goal 4 (job funnel monitoring)

| ID | User Story | MVP Tag |
|---|---|---|
| J1 | As an admin, I want to see the job funnel (posted → matched → accepted → completed) so that I can spot problems early | MVP-BASELINE |
| J2 | As an admin, I want to access a dispute resolution view with full job history and message trail so that I can mediate fairly | MVP-BASELINE |
| J3 | As an admin, I want to see platform-wide metrics (active tradies, jobs this week, completion rate) so that I can track health | MVP |

---

### Epic 11: Notifications

**Goal link:** All goals — notifications connect all flows

| ID | User Story | MVP Tag |
|---|---|---|
| K1 | As a homeowner, I want an email when my shortlist is ready so that I don't have to keep checking the app | MVP-BASELINE |
| K2 | As a tradie, I want an email when I am matched to a job so that I can respond quickly | MVP-BASELINE |
| K3 | As a tradie, I want an email when a homeowner selects me so that I can prepare | MVP-BASELINE |
| K4 | As a homeowner, I want an email when a tradie applies to my job so that I know there is interest | MVP |
| K5 | As a user, I want an email when I receive a new message so that I respond promptly | MVP-BASELINE |

---

## Out of Scope (POST-MVP)

- Native mobile app (iOS / Android)
- Tradie leaderboard / reputation gamification
- Subscription billing and payment processing (Stripe)
- B2B / enterprise accounts
- Fraud detection automation
- Analytics dashboard for sponsors
- Multi-language (Serbian / English toggle)
- Expansion beyond Belgrade
- Trade types beyond painters and plumbers
- Personalised matching weight adjustment (D6, I2)
