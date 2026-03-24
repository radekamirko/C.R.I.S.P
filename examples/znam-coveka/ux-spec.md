# UX Spec

**Project:** Znam Coveka
**Date:** 2026-03-24

---

# Part 1: Sitemap

## Homeowner Shell

```
/ (root)
├── /login               — OAuth sign-in (Google / Apple)
├── /onboarding          — Tradie preference setup (3 questions, post-signup)
├── /dashboard           — Tab: Post a Job (default landing after onboarding)
│   ├── /jobs/new        — Job posting flow (multi-step)
│   ├── /jobs            — Tab: My Jobs (active + past)
│   │   └── /jobs/[id]   — Job detail: shortlist, applications, status, messaging
│   └── /profile         — Tab: Profile + preferences + account settings
```

## Tradie Shell

```
/ (root — tradie)
├── /login               — OAuth or email sign-in
├── /onboarding/tradie   — Profile setup (URL auto-fill → review + confirm)
├── /pending             — Waiting for admin approval (holding screen)
├── /feed                — Tab: Jobs (matched + open job feed)
│   └── /feed/[jobId]    — Job detail + apply action
├── /my-work             — Tab: Active jobs + completed jobs
│   └── /my-work/[jobId] — Job detail, messaging, status
├── /profile             — Tab: Portfolio, availability, bio, settings
└── /earnings            — Tab: Subscription status, jobs completed, earnings
```

## Admin Shell (separate route)

```
/admin
├── /admin/approvals     — Tradie application queue
│   └── /admin/approvals/[tradieId] — Profile review + approve/reject
├── /admin/funnel        — Job pipeline: posted → matched → accepted → completed
└── /admin/disputes      — Open disputes, job history, message trail
```

---

# Part 2: Flow Specs

## Flow 1: Homeowner Sign-Up + Onboarding

**User goal:** Get onto the platform and set preferences — in under 2 minutes.
**Entry:** Landing page CTA / referral link
**Exit:** Dashboard — /jobs/new

```
Landing page
  → "Continue with Google" / "Continue with Apple"
  → OAuth completes
  → Onboarding: 3 preference questions
      Q1: What matters most to you? (Speed / Price / Reviews / Experience) — single select
      Q2: How far can your tradie travel? (My area / Up to 5km / Up to 10km) — single select
      Q3: How urgently do you usually need a tradie? (Same week / Within a month / No rush) — single select
  → "Done — let's find you a tradie" → /jobs/new
```

**Success state:** User lands on job posting screen, preferences saved.
**Failure state:** OAuth fails → show error + retry. Never drop to a blank screen.

---

## Flow 2: Homeowner Posts a Job

**User goal:** Post a job in under 2 minutes.
**Entry:** /jobs/new (tab or CTA)
**Exit:** Job submitted → matching in progress screen

```
Step 1: What do you need?
  → Trade type (Painter / Plumber) — large tap targets, icons
  → Job description (free text, max 500 chars)
  → [Next]

Step 2: Where and when?
  → Location (Google Maps autocomplete — Belgrade addresses)
  → Availability window (date range picker: "From / To")
  → Photos (optional — mobile camera or gallery)
  → [Next]

Step 3: Job preferences
  → Budget range (slider: "Under 5,000 RSD / 5k–15k / 15k–50k / 50k+")
  → Urgency (This week / This month / Flexible)
  → [Post Job]

Confirmation screen:
  → "Finding your best matches — usually under 60 seconds"
  → Skeleton loading cards (3 cards placeholder)
  → Redirect to /jobs/[id] when shortlist ready
```

**Success state:** Shortlist ready, user redirected to job detail.
**Failure state:** No tradies available in area → "No matches right now — we'll notify you when a match is found."

---

## Flow 3: Homeowner Views Shortlist and Selects Tradie

**User goal:** Understand the recommendations and pick one confidently.
**Entry:** /jobs/[id] — shortlist ready notification
**Exit:** Tradie selected → messaging opens

```
Job detail screen
  → Job summary (trade, description, location, status)
  → "Your Matches" section — 3 tradie cards (AI shortlist)
      Each card:
        - Tradie photo + name + trade + rating
        - AI explanation: "We matched [name] because [specific reason]"
        - "View Profile" / "Select" actions
  → "Also applied" section — pull applications (below AI shortlist)
      Each application: tradie card, same format, no AI explanation
  → Selecting a tradie:
      Confirmation modal: "Confirm [name] for this job?"
      → Confirm → tradie notified → messaging channel opens
      → Other tradies notified: "This job has been filled"
```

**High-stakes screen rules:**
- AI explanation is the hero element — full width, not truncated, readable font size
- "Select" button is primary, full-width within each card
- Applications section is clearly secondary — label: "Others who applied"

---

## Flow 4: Tradie Onboarding + Profile Setup

**User goal:** Get approved and live on the platform.
**Entry:** /login → /onboarding/tradie
**Exit:** Approval pending → /pending

```
Option A — URL auto-fill (primary path):
  → "Paste your website or Google My Business URL"
  → Claude API scrapes: trade type, bio, service area, photos
  → Review screen: pre-filled profile — tradie edits if needed
  → Add availability (calendar / general pattern)
  → Submit for review

Option B — Manual (fallback):
  → Trade type (multi-select: Painter / Plumber / Both)
  → Service area (Belgrade zones — multi-select)
  → Bio (free text)
  → Portfolio photos (upload — mobile camera supported)
  → Availability
  → Submit for review

/pending screen:
  → "Profile received — we review within 24 hours"
  → Email sent immediately on submission
```

---

## Flow 5: Tradie Browses and Applies to Jobs

**User goal:** Find relevant open jobs and apply.
**Entry:** /feed (tab)
**Exit:** Application submitted

```
/feed — default view:
  → Filter: pre-set to tradie's trade + service area
  → "Matched for you" section (top) — AI-pushed jobs
  → "Open jobs" section (below) — pull feed
  → Each job card: trade icon + description + area + budget + posted time
  → Tap job card → /feed/[jobId]

Job detail:
  → Full description, location (map), budget, homeowner preferences
  → "Apply" CTA (primary button)
  → Apply → confirmation: "Application sent"
  → Job card marked as "Applied" in feed
```

---

## Flow 6: Job Completion + Review

**User goal:** Confirm the job is done, leave a review.
**Entry:** /my-work/[jobId] or /jobs/[id] — job in progress
**Exit:** Review submitted → option to rebook

```
Homeowner confirms completion:
  → "Mark job as complete" button on job detail
  → One-tap confirmation modal
  → Review prompt: star rating (1–5) + optional text (max 200 chars)
  → Submit → "Thanks! [tradie name]'s profile has been updated."
  → Rebook CTA: "Book [name] again?" — one tap

Tradie sees:
  → Review appears on profile immediately
  → Job moves to completed in /my-work
  → Earnings screen updated
```

---

# Part 3: Screen Specs

## Screen: Homeowner Shortlist (/jobs/[id])

**Target emotion:** Confident — "I know why this person was recommended."
**Primary action:** Select a tradie.

| Element | Spec |
|---|---|
| Header | Job summary (trade type + short description) — collapsible |
| Section label | "Your Matches" — 16px semibold, primary colour |
| Tradie card | White card, 12px radius, photo (64px circle) left, name + trade + rating right |
| AI explanation | Full-width below tradie info, 16px body, 1.7 line-height, `#1A1A1A` — NOT grey |
| Select button | Full-width inside card, primary colour, 48px height |
| Applications section | Below shortlist, label "Others who applied", secondary styling |
| Empty state | If no matches: "We're looking for matches — check back soon" |

**Cognitive UX checklist for this screen:**
- [ ] Max 3 cards (Hick's Law)
- [ ] AI explanation is never truncated
- [ ] Select button is visually dominant over "View Profile"
- [ ] Applications section is clearly secondary — never competes with AI shortlist

---

## Screen: Tradie Job Feed (/feed)

**Target emotion:** Active — "There are real jobs here for me."
**Primary action:** Tap a job to view and apply.

| Element | Spec |
|---|---|
| "Matched for you" | Top section, amber accent label, highlighted card background |
| "Open jobs" | Below, standard card styling |
| Job card | Trade icon + job title + area + distance + budget + time posted |
| Applied badge | Green "Applied" pill on cards already applied to |
| Empty state | "No open jobs in your area right now — we'll notify you when one appears" |
| Filter bar | Sticky at top: trade filter + area filter (pre-filled to tradie's settings) |

---

## Screen: Tradie Profile Setup (/onboarding/tradie)

**Target emotion:** Invested — "This is my shop window."
**Primary action:** Submit profile for review.

| Element | Spec |
|---|---|
| URL auto-fill input | Prominent, top of screen, label: "Paste your website or Google My Business URL" |
| Auto-fill button | "Import profile" — primary CTA |
| Pre-filled review | Each field shows pre-filled value + edit icon — review mode, not a blank form |
| Portfolio photos | Grid upload — 2 columns, add button in last cell, mobile camera supported |
| Availability | Simple toggle pattern: Mon–Sun, AM/PM — not a full calendar at this stage |
| Submit button | "Submit for review" — primary, full-width, bottom of screen |
| Progress indicator | Step 1 of 2 (Profile → Review) shown at top |

---

## Screen: Admin Approval Queue (/admin/approvals)

**Target emotion:** Efficient — "I can process this in under 5 minutes."
**Primary action:** Approve or reject.

| Element | Spec |
|---|---|
| Queue list | Sorted by submission date (oldest first) |
| AI pre-screen summary | At top of each profile: "Profile complete / Missing: [fields] / Flags: [issues]" |
| Portfolio grid | Photos displayed inline — no separate download |
| Approve button | Green, prominent |
| Reject button | Red, secondary — requires optional rejection note |
| Bulk view | Show 10 per page — no pagination needed at MVP scale |
