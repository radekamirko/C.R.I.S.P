# UX Discovery

**Project:** Znam Coveka
**Date:** 2026-03-24

---

## 3A: Audience & Mental Models

### Homeowner
- **Profile:** Belgrade resident, needs a painter or plumber. Uses apps daily. Opens platform on mobile or laptop, typically in a moment of frustration after a failed search or bad experience.
- **Mental model reference:** Airbnb — curated shortlist with context, you pick from a small number of well-explained options. Not Booking.com (browse hundreds, filter yourself). Not Google (open search).
- **What they need most on first open:** Trust and speed. They've been burned before. The product must signal quality before they post a single job.

### Tradie
- **Profile:** Experienced painter or plumber in Belgrade. Not a "form person." Likely signs up on mobile. Sceptical of platforms — has lost money to fake leads or race-to-the-bottom pricing before.
- **Mental model reference:** Uber Driver — job feed, accept or decline, clear status, fast action. Not LinkedIn (passive profile). Not a dashboard.
- **What they need most on first open:** To see real jobs immediately after approval. The feed must feel alive.

### Admin (Mirko)
- **Profile:** Solo founder managing vetting and disputes manually at MVP. Needs a lean, fast interface — not a full CRM.
- **Mental model reference:** A simple approval queue. Think Airtable or a stripped-down inbox.

---

## 3B: Visual Direction

**Emotional register:** Trustworthy + approachable. Both are non-negotiable — neither can be sacrificed for the other.

- Trustworthy: clean layout, generous white space, real photography (tradie portfolio photos do heavy lifting), no clutter
- Approachable: warm typography, human tone in copy, not corporate or cold

**Reference apps:**
- Homeowner side: Airbnb (curated, confidence-inspiring, photography-led)
- Tradie side: Uber Driver (action-first, status-clear, nothing decorative)

**What to avoid:**
- Dark, aggressive UI (signals hustle culture, not trust)
- Cheap directory aesthetic (the thing we are explicitly not)
- Over-engineered dashboards (tradies don't want analytics, they want jobs)

**Colour / tone direction:** Warm neutrals, one strong accent colour. Friendly but professional. Serbian market — avoid anything that feels imported or generic Western tech.

---

## 3C: Navigation Pattern

Two distinct user types. Separate navigation shells — homeowners and tradies never share the same nav.

### Homeowner — Tab Bar (bottom nav, 3 tabs)
| Tab | Content |
|---|---|
| Post a Job | Job posting flow — primary action |
| My Jobs | Active + past jobs, shortlists, status |
| Profile | Account settings, preferences |

### Tradie — Tab Bar (bottom nav, 4 tabs)
| Tab | Content |
|---|---|
| Jobs | Feed of open jobs (filtered by trade + location) + matched jobs |
| My Work | Active jobs, past completed jobs, reviews received |
| Profile | Portfolio, availability, bio, settings |
| Earnings | Subscription status, jobs completed, estimated earnings via platform |

### Admin — Standalone lightweight dashboard (separate URL/route)
| Section | Content |
|---|---|
| Approvals | Tradie applications queue — AI pre-screen summary + approve/reject |
| Job Funnel | Posted → matched → accepted → completed pipeline view |
| Disputes | Open disputes, job history, message trail |

---

## 3D: High-Stakes Screens

### Screen 1: Homeowner Shortlist
**Why it matters:** This is where the platform wins or loses. The AI explanation either earns trust or the homeowner bounces.

| Dimension | Detail |
|---|---|
| Emotion the user should feel | Confident — "I know why this person was recommended for my job" |
| Primary action | Select a tradie |
| Secondary action | View tradie profile in full |
| Biggest risk | Generic explanation ("Marko is a great plumber") = distrust. Explanation must be specific to the job. |
| UX note | AI explanation is the hero element. Tradie photo + name + explanation card. Rating visible but secondary. Applications (pull) shown below AI shortlist — never above. |

### Screen 2: Tradie Profile Setup
**Why it matters:** If this feels like a long form, tradies abandon. Quality of profile directly determines matching quality — so dropout here degrades the whole platform.

| Dimension | Detail |
|---|---|
| Emotion the user should feel | Invested — "this is my shop window, I want it to look good" |
| Primary action | Complete profile (trade, area, availability, portfolio photos) |
| Biggest risk | Long form → abandonment → low profile quality → poor matches → tradie churn |
| UX note | **URL auto-fill feature:** Tradie pastes their website URL or Google My Business link → Claude API scrapes and pre-fills trade type, bio, service area, and photos where available → tradie reviews and confirms. Turns 10-minute form into 2-minute review. This is the key friction-reduction feature for this screen. |
| Mobile-first | Tradies will set up on mobile. Photo upload must work natively on mobile. |

---

## 3E: Friction & Delight Inventory

### Friction Points → Design Actions

| Friction point | Where | Design action |
|---|---|---|
| "Another directory" scepticism | Homeowner landing page | Lead with the mechanic, not the category: "Post a job. Get 3 matched tradies with a reason why. Pick one." |
| Homeowner anxiety during matching | After job posted | Loading state with reassuring message: "Finding your best matches — usually under 60 seconds" |
| Tradie profile form abandonment | Profile setup | URL auto-fill (website / Google My Business) — Claude pre-fills, tradie confirms |
| Tradie vetting silence | After profile submitted | Immediate email: "Profile received — we review within 24h" |
| Dead job feed on first tradie login | After approval | Show open jobs in area immediately — never an empty state on first login |
| Homeowner unsure what to do after selecting tradie | Post-selection | Clear confirmation: "Marko has been notified — expect contact within 24h" |
| Tradie subscription renewal doubt | Month 2 renewal | Show "You completed X jobs through Znam Coveka this month" before renewal prompt |

### Delight Moments → Amplify

| Delight moment | Where | How to amplify |
|---|---|---|
| One-tap Google/Apple sign-in | Homeowner onboarding | No friction at all — land on preferences immediately after tap |
| Reading "We matched Marko because..." | Shortlist screen | Typography and layout give the explanation room to breathe — not a footnote, the headline |
| Seeing own profile looking professional | Tradie post-setup | Profile preview before going live — "Here's how homeowners will see you" |
| First job matched | Tradie feed | Notification copy: "You've been matched to your first job — a homeowner in Vračar needs a painter" |
| Rebooking same tradie | Homeowner post-completion | One-tap rebook button on job completion screen |
