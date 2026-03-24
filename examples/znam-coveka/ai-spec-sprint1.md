# AI Spec — Sprint 1: Foundation

**Project:** Znam Coveka
**Feature / Sprint:** Sprint 1 — Foundation
**Date:** 2026-03-24
**Status:** Approved
**NFRs in scope:** Docker deployment, EU data residency (Railway EU + Supabase EU), encryption in transit (HTTPS), RLS on all tables, no secrets in Git

---

## Context

Sprint 1 builds the technical foundation everything else sits on. No user-facing features ship — but auth, the DB schema, role system, navigation shells, and deployment pipeline must all be working and correct before Sprint 2 begins. Getting the foundation wrong costs 3x to fix later.

**Goal served:** All goals — this sprint makes every subsequent sprint possible.

---

## Scope

**In:**
- Next.js 14 App Router project scaffold with TypeScript + Tailwind CSS
- Docker multi-stage build + docker-compose for local development
- Railway EU deployment pipeline (CI/CD from Git)
- Supabase project setup (EU region — Frankfurt)
- Google OAuth sign-in (Supabase Auth) — homeowner and tradie
- Role selection screen (homeowner / tradie) shown once after first sign-in
- Admin role: single admin account (Mirko) — set directly in Supabase DB, not self-service
- Session handling: Supabase default (1 hour + refresh token, auto-refresh)
- Role-gated routing: homeowner shell, tradie shell, /admin route
- Full DB schema with RLS policies
- Environment variables wired and verified — fail loudly if missing
- Basic navigation shells (homeowner tab bar + tradie tab bar + admin sidebar)

**Out:**
- Any user-facing feature beyond auth and role selection
- Apple Sign-In (Sprint 8 or later)
- Email/password auth for homeowners (Google only)
- Tradie-specific auth features (email auth is fine, covered in Sprint 2)
- Any AI calls
- Any third-party integrations beyond Supabase Auth + Google OAuth

---

## Version-Sensitive Dependencies

| Library | Pinned version | Breaking change to watch |
|---|---|---|
| Next.js | 14.2.x | App Router ONLY — never use Pages Router. `app/` directory, not `pages/`. |
| React | 18.3.x | Use `createRoot` — never `ReactDOM.render` |
| @supabase/supabase-js | 2.x | v2 auth API only. `createClient` not `createClient` from v1. `supabase.auth.getUser()` not `supabase.auth.user()`. |
| @supabase/ssr | latest stable | Required for Next.js server-side auth — use `createServerClient` and `createBrowserClient` |

---

## Environment Variables

| Variable | Purpose | Where to get it | Required? |
|---|---|---|---|
| NEXT_PUBLIC_SUPABASE_URL | Supabase project URL | Supabase dashboard → Project Settings → API | Yes |
| NEXT_PUBLIC_SUPABASE_ANON_KEY | Supabase public anon key | Supabase dashboard → Project Settings → API | Yes |
| SUPABASE_SERVICE_ROLE_KEY | Service role key — server-side only, never sent to client | Supabase dashboard → Project Settings → API | Yes |

---

## Database Schema

```sql
-- users (extends Supabase auth.users)
CREATE TABLE public.profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  role TEXT NOT NULL CHECK (role IN ('homeowner', 'tradie', 'admin')),
  full_name TEXT,
  avatar_url TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- tradies (extended profile for tradie role)
CREATE TABLE public.tradies (
  id UUID PRIMARY KEY REFERENCES public.profiles(id) ON DELETE CASCADE,
  trade_types TEXT[] NOT NULL DEFAULT '{}', -- ['painter', 'plumber']
  service_areas TEXT[] NOT NULL DEFAULT '{}', -- Belgrade zones
  bio TEXT,
  years_experience INT,
  availability JSONB, -- { mon_am: true, mon_pm: false, ... }
  pricing_indication TEXT,
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected')),
  rejection_reason TEXT,
  website_url TEXT,
  google_my_business_url TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- tradie_portfolio_photos
CREATE TABLE public.tradie_portfolio_photos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tradie_id UUID NOT NULL REFERENCES public.tradies(id) ON DELETE CASCADE,
  storage_path TEXT NOT NULL,
  display_order INT DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- jobs
CREATE TABLE public.jobs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  homeowner_id UUID NOT NULL REFERENCES public.profiles(id),
  trade_type TEXT NOT NULL CHECK (trade_type IN ('painter', 'plumber')),
  description TEXT NOT NULL,
  location_address TEXT NOT NULL,
  location_lat DECIMAL(10, 8),
  location_lng DECIMAL(11, 8),
  availability_from DATE NOT NULL,
  availability_to DATE NOT NULL,
  budget_range TEXT CHECK (budget_range IN ('under_5k', '5k_15k', '15k_50k', '50k_plus')),
  urgency TEXT CHECK (urgency IN ('this_week', 'this_month', 'flexible')),
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'matched', 'in_progress', 'completed', 'cancelled')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- job_photos
CREATE TABLE public.job_photos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  job_id UUID NOT NULL REFERENCES public.jobs(id) ON DELETE CASCADE,
  storage_path TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- matches (AI-generated shortlist)
CREATE TABLE public.matches (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  job_id UUID NOT NULL REFERENCES public.jobs(id) ON DELETE CASCADE,
  tradie_id UUID NOT NULL REFERENCES public.tradies(id),
  match_type TEXT NOT NULL CHECK (match_type IN ('ai_shortlist', 'tradie_applied')),
  ai_explanation TEXT, -- populated for ai_shortlist type only
  rank_position INT, -- 1, 2, 3 for AI shortlist
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'selected', 'declined', 'expired')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- messages
CREATE TABLE public.messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  job_id UUID NOT NULL REFERENCES public.jobs(id) ON DELETE CASCADE,
  sender_id UUID NOT NULL REFERENCES public.profiles(id),
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- reviews
CREATE TABLE public.reviews (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  job_id UUID NOT NULL REFERENCES public.jobs(id),
  homeowner_id UUID NOT NULL REFERENCES public.profiles(id),
  tradie_id UUID NOT NULL REFERENCES public.tradies(id),
  rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  content TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- implicit_signals (preference learning)
CREATE TABLE public.implicit_signals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  homeowner_id UUID NOT NULL REFERENCES public.profiles(id),
  job_id UUID NOT NULL REFERENCES public.jobs(id),
  selected_tradie_id UUID REFERENCES public.tradies(id),
  rating_given INT CHECK (rating_given BETWEEN 1 AND 5),
  rebooked BOOLEAN DEFAULT FALSE,
  shortlist_response_time_minutes INT, -- how long homeowner took to pick
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- homeowner_preferences
CREATE TABLE public.homeowner_preferences (
  id UUID PRIMARY KEY REFERENCES public.profiles(id) ON DELETE CASCADE,
  priority TEXT CHECK (priority IN ('speed', 'price', 'reviews', 'experience')),
  max_distance_km INT DEFAULT 10,
  urgency_profile TEXT CHECK (urgency_profile IN ('same_week', 'within_month', 'flexible')),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

**RLS Policies (enforce on every table):**

```sql
-- profiles: users can only read/update their own profile
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can view own profile" ON public.profiles FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users can update own profile" ON public.profiles FOR UPDATE USING (auth.uid() = id);
-- Admin can view all (use service role key server-side for admin operations)

-- jobs: homeowners own their jobs; tradies can read active jobs
ALTER TABLE public.jobs ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Homeowners manage own jobs" ON public.jobs FOR ALL USING (auth.uid() = homeowner_id);
CREATE POLICY "Tradies can read active jobs" ON public.jobs FOR SELECT USING (
  status = 'active' AND EXISTS (SELECT 1 FROM public.tradies WHERE id = auth.uid() AND status = 'approved')
);

-- matches: homeowners see matches for their jobs; tradies see their own matches
ALTER TABLE public.matches ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Homeowners see their job matches" ON public.matches FOR SELECT USING (
  EXISTS (SELECT 1 FROM public.jobs WHERE id = job_id AND homeowner_id = auth.uid())
);
CREATE POLICY "Tradies see own matches" ON public.matches FOR SELECT USING (tradie_id = auth.uid());

-- messages: only parties on the job can see messages
ALTER TABLE public.messages ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Job parties can read messages" ON public.messages FOR SELECT USING (
  EXISTS (
    SELECT 1 FROM public.jobs j
    LEFT JOIN public.matches m ON m.job_id = j.id AND m.status = 'selected'
    WHERE j.id = job_id AND (j.homeowner_id = auth.uid() OR m.tradie_id = auth.uid())
  )
);
CREATE POLICY "Job parties can send messages" ON public.messages FOR INSERT WITH CHECK (
  auth.uid() = sender_id AND EXISTS (
    SELECT 1 FROM public.jobs j
    LEFT JOIN public.matches m ON m.job_id = j.id AND m.status = 'selected'
    WHERE j.id = job_id AND (j.homeowner_id = auth.uid() OR m.tradie_id = auth.uid())
  )
);

-- reviews: public read, homeowner write
ALTER TABLE public.reviews ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Reviews are public" ON public.reviews FOR SELECT USING (TRUE);
CREATE POLICY "Homeowners write reviews" ON public.reviews FOR INSERT WITH CHECK (auth.uid() = homeowner_id);
```

**Indexes:**
```sql
CREATE INDEX idx_jobs_homeowner ON public.jobs(homeowner_id);
CREATE INDEX idx_jobs_status ON public.jobs(status);
CREATE INDEX idx_jobs_trade_type ON public.jobs(trade_type);
CREATE INDEX idx_matches_job ON public.matches(job_id);
CREATE INDEX idx_matches_tradie ON public.matches(tradie_id);
CREATE INDEX idx_messages_job ON public.messages(job_id, created_at);
CREATE INDEX idx_tradies_status ON public.tradies(status);
```

---

## Business Logic & Rules

- After Google OAuth, check if `profiles` row exists for the user. If not → show role selection screen. If yes → route to appropriate shell.
- Role selection is one-time only. Once set, it cannot be changed by the user (admin only).
- Admin role is set directly in the DB (INSERT into profiles with role='admin'). There is no self-service admin sign-up. Mirko's account is seeded manually.
- /admin routes must check role='admin' server-side on every request — not client-side only.
- SUPABASE_SERVICE_ROLE_KEY must never be exposed to the client. All admin DB operations use server-side API routes only.

---

## Acceptance Criteria

- [ ] Given a new user, when they sign in with Google, then they see a role selection screen (Homeowner / Tradie)
- [ ] Given a returning user, when they sign in with Google, then they are routed directly to their role's shell (no role selection)
- [ ] Given a homeowner user, when they visit /admin, then they receive a 403 or redirect to /dashboard
- [ ] Given an admin user, when they visit /admin, then they see the admin dashboard shell
- [ ] Given a tradie user, when they visit the homeowner shell, then they are redirected to the tradie shell
- [ ] Given any unauthenticated user, when they visit any protected route, then they are redirected to /login
- [ ] Given the app is running, when an environment variable is missing, then the app throws a clear error at startup — not a silent failure
- [ ] Given the Docker container is built and run locally, when `docker-compose up` is run, then the app starts and auth works
- [ ] Given the app is deployed to Railway EU, when a user signs in, then the session works correctly in production
- [ ] Given all DB tables are created, when a user tries to read another user's private data via direct Supabase query, then RLS blocks the request

---

## Constraints & Rules

- **Security:** SUPABASE_SERVICE_ROLE_KEY never sent to client. Admin role checked server-side. RLS on all tables.
- **Data handling:** No PII logged. User IDs are UUIDs. No personal data in error messages.
- **Error handling:** Missing env vars → throw at startup with clear message listing which var is missing. Auth failure → redirect to /login with error query param.
- **Fallback:** If Google OAuth fails → show error state with retry button. Never a blank screen.

---

## Test Cases

| # | Scenario | Input | Expected output | Type |
|---|---|---|---|---|
| T1 | New user Google sign-in | Valid Google account | Role selection screen | Functional |
| T2 | Returning homeowner sign-in | Existing homeowner account | Routed to homeowner dashboard | Functional |
| T3 | Returning tradie sign-in | Existing tradie account | Routed to tradie shell | Functional |
| T4 | Homeowner visits /admin | Authenticated homeowner | 403 / redirect | Security |
| T5 | Unauthenticated visits /jobs | No session | Redirect to /login | Security |
| T6 | Missing env var | ANTHROPIC_API_KEY missing | Clear startup error (not a runtime crash) | Edge |
| T7 | RLS check | User A queries User B's job via Supabase client | Empty result / RLS error | Security |
| T8 | Docker build | `docker-compose up` | App starts, auth works on localhost | Functional |

---

## Notes for Claude Code

- Use `@supabase/ssr` for all server-side auth (Server Components, API routes, middleware). Use `createBrowserClient` for client components.
- Middleware (`middleware.ts`) should handle session refresh on every request — follow Supabase SSR docs exactly.
- The `profiles` table uses the same UUID as `auth.users`. Use a Supabase trigger or handle in the sign-up flow to create the profiles row automatically on first sign-in.
- Do not use `supabase.auth.user()` (v1). Use `supabase.auth.getUser()` (v2).
- Navigation shells are layout files (`app/(homeowner)/layout.tsx`, `app/(tradie)/layout.tsx`). Role check happens in the layout server component.
- `/admin` is a separate route group — not inside homeowner or tradie groups.
- Docker multi-stage build: builder stage (npm install + build), runner stage (production image). Use Node 20 Alpine base image.
- All secrets must be injected as environment variables in Railway — never baked into the Docker image.
