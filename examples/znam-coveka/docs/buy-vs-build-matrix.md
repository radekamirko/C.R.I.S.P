# Buy vs Build Matrix

**Project:** Znam Coveka
**Date:** 2026-03-24

---

| Tool / Solution | What it covers | Gap | Cost | Decision |
|---|---|---|---|---|
| Supabase | Auth (email/Google/Apple), database, storage, realtime | None for MVP | Free tier → ~$25/mo | Buy / Configure |
| Claude API (Anthropic) | AI-generated match explanations, tradie ranking logic | None | Pay per use (~$0.01-0.05 per match generation) | Buy / Configure |
| Next.js + Vercel | Web frontend, SSR, responsive layout | None | Free tier sufficient for MVP | Configure / Build UI |
| Google Maps API | Location input, map pin for job, tradie proximity | None | Pay per use (free tier: 28k map loads/mo) | Buy / Configure |
| Resend | Transactional email (job notifications, account events) | None | Free tier: 3k emails/mo | Buy / Configure |
| Stripe | Tradie subscription billing | Not needed at MVP — manual onboarding first | Free until live payments | Buy (defer to post-MVP) |
| Custom matching engine | Job-to-tradie matching logic (trade type, location, availability, rating) | Must be built — no off-the-shelf tool does this | 0 (code) | Build |
| Custom vetting workflow | Tradie onboarding: portfolio review, ID check, rating system | Must be built | 0 (code) | Build |
| Custom job posting flow | Homeowner posts job with details, location, photos | Must be built | 0 (code) | Build |

## Recommendation

Buy and configure infrastructure (Supabase, Claude API, Vercel, Google Maps, Resend). Build the product logic: matching engine, tradie vetting workflow, job posting flow, and AI explanation generation.

## Justification

No off-the-shelf tool does curated tradie matching with AI explanation — that is the core differentiator and must be built. All infrastructure layers have mature, affordable SaaS options that would take weeks to replicate. The build cost is code only (bootstrapped), and the SaaS costs are negligible at MVP scale (sub-$100/month total until meaningful user volume).

Stripe deferred: at MVP, tradie access can be managed manually (whitelist onboarding) while the product is validated. Add payments in the sprint after product-market fit signals appear.
