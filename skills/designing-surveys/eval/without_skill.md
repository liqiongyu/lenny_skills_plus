# Onboarding Profiling Survey — B2B Analytics Tool

## Overview

This is an in-product profiling survey designed to run during a new user's first session. It routes signups to the correct onboarding path and flags whether the account is a potential buyer or a non-commercial user (so sales doesn't waste time on non-buyers). Target completion time: under 2 minutes (6 questions, progressive disclosure).

---

## Survey Flow

### Screen 1 — Welcome & Role

**Header:** "Let's personalize your experience"
**Subtext:** "4 quick questions so we can get you to value faster."

**Q1. What best describes your role?**
_(Single select)_

- Executive / C-suite
- VP / Director
- Manager
- Individual Contributor / Analyst
- Engineer / Developer
- Other: ___________

**Routing logic:**
- Executive / C-suite / VP / Director → flag as `decision_maker = true`
- All others → `decision_maker = false`

---

### Screen 2 — Company Size & Use Case

**Q2. How large is your company?**
_(Single select)_

- 1–10 employees
- 11–50
- 51–200
- 201–1,000
- 1,001–10,000
- 10,000+

**Q3. What's your primary goal with [Product]?**
_(Single select)_

- Track product/feature usage
- Build dashboards & reports for stakeholders
- Run experiments / A/B tests
- Monitor business KPIs
- Explore data / ad-hoc analysis
- Other: ___________

**Routing logic:**
- Company size 1–10 → `segment = self_serve`
- Company size 11–200 → `segment = mid_market`
- Company size 201+ → `segment = enterprise`

---

### Screen 3 — Current Stack & Buyer Intent

**Q4. What analytics tools are you using today?**
_(Multi-select, pick all that apply)_

- Google Analytics
- Mixpanel
- Amplitude
- Heap
- Looker / Tableau / Power BI
- Internal / custom-built
- None — this is our first analytics tool
- Other: ___________

**Q5. What best describes your situation?**
_(Single select)_

- Evaluating tools — have budget and timeline
- Exploring options — no active buying process
- Already purchased — setting up my account
- Using a free/community tier for personal or side project

**Routing logic for sales filtering:**
- "Evaluating tools — have budget and timeline" AND `decision_maker = true` AND `segment ∈ {mid_market, enterprise}` → **Sales-Qualified Lead (SQL).** Route to sales-assisted onboarding.
- "Already purchased" → **Customer.** Route to implementation onboarding.
- "Exploring options" or "Using free tier for personal project" OR `segment = self_serve` → **Non-buyer.** Suppress sales outreach; route to self-serve onboarding.

---

### Screen 4 — Team Context (conditional)

_Only shown if company size ≥ 51 (mid-market or enterprise)._

**Q6. How many people on your team will use [Product]?**
_(Single select)_

- Just me
- 2–5
- 6–20
- 20+

**Routing logic:**
- "Just me" → self-serve onboarding (even if mid-market company)
- 2–5 → guided onboarding with templates
- 6+ → team onboarding with workspace setup flow

---

## Onboarding Path Mapping

| Segment | Buyer Signal | Path | First-Session Experience |
|---|---|---|---|
| Self-serve (1–10 employees) | Any | **Self-serve** | Interactive setup wizard → sample dataset → first chart in 5 min |
| Mid-market, non-buyer | Exploring / free tier | **Self-serve plus** | Setup wizard + pre-built templates for their use case |
| Mid-market, active buyer | Evaluating + budget | **Sales-assisted** | Setup wizard + calendar invite from AE within 24 hrs |
| Enterprise, non-buyer | Exploring / free tier | **Self-serve plus** | Setup wizard + templates; sales suppressed |
| Enterprise, active buyer | Evaluating + budget | **Sales-assisted (high-touch)** | Dedicated onboarding call scheduled; CSM assigned |
| Any, already purchased | Already purchased | **Implementation** | Technical setup guide + data-source connection flow |

---

## Sales Suppression Rules

To prevent sales from contacting non-buyers:

1. **Do not pass to sales** any signup where `buyer_intent` ∈ {"Exploring options", "Using free tier for personal project"}.
2. **Do not pass to sales** any signup where `segment = self_serve` (1–10 employees), regardless of buyer intent.
3. **Do not pass to sales** any signup where `decision_maker = false`, unless the account already has a separate SQL flag from another user at the same company domain.
4. Leads flagged as SQL get a 48-hour enrichment window (Clearbit/ZoomInfo) before AE outreach to confirm fit.

---

## Implementation Notes

- **Progress indicator:** Show a simple step counter ("1 of 4") to set expectations and reduce drop-off.
- **Skip option:** Allow "Skip for now" on every screen. Skipped users go to a generic self-serve path; sales is suppressed until they complete the survey or trigger a PQL event.
- **Persistence:** Save answers progressively (don't wait for completion). If a user drops at Q3, you still have role + company size for basic routing.
- **Revisit:** Let users update answers from Settings → Profile. Changes re-evaluate routing logic.
- **Analytics on the survey itself:** Track completion rate, drop-off by screen, and time-to-complete. Target: >70% completion, <90 seconds median.
- **Privacy:** Add a one-liner under the first question: "We use this to personalize your setup — never shared with third parties."

---

## Estimated Timing

| Screen | Questions | Est. Time |
|---|---|---|
| 1 — Role | 1 | 10 sec |
| 2 — Company size & goal | 2 | 20 sec |
| 3 — Stack & intent | 2 | 30 sec |
| 4 — Team size (conditional) | 1 | 10 sec |
| **Total** | **5–6** | **~70 sec** |

Well under the 2-minute target.
