# User Journey Map

**Project:** Znam Coveka
**Date:** 2026-03-24

---

## Journey 1: Homeowner

**Persona:** Homeowner in Belgrade who needs a painter or plumber. Currently relies on Google search and word of mouth. Technically comfortable — uses apps daily. Opens Znam Coveka on their phone or laptop, probably in a moment of frustration after a bad experience or a failed search.

---

| Step | Action | Need | Feeling | Pain Point | Delight Moment |
|---|---|---|---|---|---|
| 1. Discovery | Hears about Znam Coveka (word of mouth / social) | Reason to trust it before trying | Sceptical — "another directory?" | Has been burned by directories before | — |
| 2. Sign up | Taps Google / Apple sign-in — one tap, done | Zero friction, no forms | Relieved — faster than expected | Password fatigue from other platforms | One-tap sign-in is the first delight |
| 3. Preference onboarding | Quick 2-3 question setup: what matters most to you in a tradie? | Feel like the platform is learning about them | Mildly curious | Feels like a survey if too long — must be max 3 questions, feel like a preference not a form | "Tell us what matters — we'll do the rest" |
| 4. Post a job | Fills in trade type, description, location, timing, photos (optional), budget/urgency | Fast, low friction — under 2 minutes | Focused, slightly anxious (will anyone respond?) | Long forms kill this moment — must be minimal | Progress indicator, clear "your job is live" confirmation |
| 5. Wait for shortlist | Platform processes matches — ideally < 60 seconds | Confidence something is happening | Anticipation / mild anxiety | Dead silence is terrifying — need feedback that matching is running | Loading state with a reassuring message |
| 6. Receive shortlist | Sees 2-3 tradies with photos, ratings, and AI explanation | Understand why each person was recommended | Curious → increasingly confident | Generic "we found 3 tradies" with no context is useless | Reading "We matched Marko because..." is the core delight of the product |
| 7. Review applications | Sees any additional tradie applications (pull track) | Compare options with context | Considered, in control | Too many options causes decision paralysis — AI shortlist must be primary | AI shortlist anchors decision, applications are supplementary |
| 8. Select tradie | Taps to select | Confirmation their choice was registered | Decisive, slightly hopeful | Uncertainty about next steps after selecting | Clear "Marko has been notified — expect contact within 24h" |
| 9. Agree start date | Communicates via in-platform messaging | Arrange job logistics without sharing personal contact | Practical | Messaging feels clunky if UX is poor | Smooth messaging flow = trust signal |
| 10. Job completed | Marks job as done, leaves review | Closure, feel heard | Satisfied (if job went well) | Review prompt feels like admin — must be one tap | Option to rebook same tradie immediately is a delight |

**Moment where they stay or leave:** Step 6 — the shortlist. If the AI explanation is generic or unconvincing, trust collapses. This screen earns or loses the platform.

---

## Journey 2: Tradie (Painter / Plumber)

**Persona:** Experienced painter or plumber in Belgrade. Has tried Oglasi.rs, word of mouth, maybe Znam Majstora. Wastes time writing quotes that go nowhere. Earns inconsistently. Sceptical of platforms — has been burned by fake leads or race-to-the-bottom pricing. Signs up during summer downtime when work is slow and they're open to trying something new.

---

| Step | Action | Need | Feeling | Pain Point | Delight Moment |
|---|---|---|---|---|---|
| 1. Discovery | Hears about platform (founder seeding, word of mouth in tradie community) | Understand the model quickly — is this another lead trap? | Sceptical, cautious | "I've tried these before and paid for nothing" | Clear "no bidding, no per-lead fees" message on landing page |
| 2. Sign up | Creates account — email or OAuth | Simple, not corporate-feeling | Neutral | Long onboarding kills this — tradies are not form people | Progress bar, estimated time: "Takes 5 minutes" |
| 3. Build profile | Trade type, service area, availability, portfolio photos, bio | Show their quality — this is their shop window | Invested — care about how they look | No photo upload on mobile is a deal-breaker. Must be mobile-first for tradies. | Seeing their own profile looking professional after setup |
| 4. Vetting wait | Waits for admin approval | Know what happens next and when | Uncertain, slightly frustrated if it takes long | Silence after submitting = drop-off. Send confirmation email immediately with timeline. | "Profile received — we'll review within 24h" |
| 5. Approved — goes live | Receives approval notification | Excitement, want to see jobs immediately | Motivated | If no jobs appear immediately, disappointment sets in | "You're live — here are the open jobs in your area right now" |
| 6a. Receive matched job (push) | Notification: "New job matched to you" | Understand the job quickly and decide | Interested, assessing | Notification without enough context = wasted click | Notification includes trade type, area, rough budget — enough to decide |
| 6b. Browse open jobs (pull) | Opens job feed, filtered by trade + location | Find jobs worth applying to | Active, hunting | Unfiltered feed wastes their time | Pre-filtered to their trade and area by default |
| 7. Accept / apply | Accepts matched job or applies to open job | Confirmation their action registered | Hopeful | Uncertainty about whether homeowner will respond | "Application sent — homeowner typically responds within Xh" |
| 8. Job confirmed | Homeowner selects them | Validation, practical next steps | Pleased, motivated | Unclear next steps after selection | Clear job brief, messaging channel opens automatically |
| 9. Complete job | Does the work, job confirmed by homeowner | Recognition, review | Proud (if job went well) | Bad review with no context is demoralising | Good review = visible on profile immediately |
| 10. Subscription renewal | Monthly renewal prompt | Feel the ROI was worth it | Calculating — did I earn enough to justify this? | If jobs were sparse, this is churn risk | Show "You completed X jobs, earned approx. X EUR through platform" |

**Moment where they stay or leave:** Step 10 — subscription renewal. If the job volume wasn't there, they leave. The platform's job is to make sure the ROI is visible and real before renewal.

---

## Journey 3: Admin (Mirko — Founder)

**Persona:** Solo founder, building and running the platform simultaneously. Handles tradie vetting, onboarding, and dispute resolution personally at MVP stage. Needs to be able to do this fast without a dedicated tool — lean admin interface is enough.

---

| Step | Action | Need | Feeling | Pain Point | Delight Moment |
|---|---|---|---|---|---|
| 1. Tradie application arrives | Receives notification of new tradie application | See profile + portfolio quickly, make a fast decision | Efficient, businesslike | No notification = applications pile up unreviewed | Email notification with direct link to profile review |
| 2. Review profile | Scans trade type, portfolio photos, bio, AI pre-screen summary | Enough signal to approve or reject in < 5 minutes | Analytical | Poorly structured profile makes the decision harder | AI pre-screen summary saves time — flags missing fields or inconsistencies |
| 3. Approve / reject | One-click decision with optional rejection note | Fast action, clear outcome | Decisive | Multi-step approval flows are friction | Single button, optional note field, done |
| 4. Monitor job funnel | Reviews dashboard: posted → matched → accepted → completed | Spot problems before they become churn signals | Alert, scanning | No dashboard = flying blind | Job funnel health visible at a glance |
| 5. Handle dispute | Homeowner or tradie raises issue | Context on what happened, fast resolution | Calm, fair | No job history = can't mediate fairly | Full job record, message history, review trail accessible in one view |
