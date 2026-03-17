# Onboarding & Activation Pack

## B2B Team Analytics Tool -- Admin Onboarding Redesign

---

## 1) Context Snapshot (Onboarding Brief)

**Product:** B2B team analytics tool (SaaS)
**Segment(s):** New self-serve admins (primary buyer/setup persona). Secondary: invited team members (out of scope for this pack; focus is on admin activation).
**Stage:** Early PMF / growth (established product with 5,000 signups/month but low activation)
**Platform(s):** Web (primary)
**FTUE entry point:** Marketing site / signup form -> email verification -> in-app setup wizard

**Goal (baseline -> target by date):**
Increase 7-day activation rate from **12% to 18%** (50% relative improvement) by end of quarter (~12 weeks). This means moving from ~600 activated admins/month to ~900 activated admins/month.

**Primary metric:** 7-day activation rate (defined below in Section 3)
**Guardrails:**
- Signup completion rate must not decrease (currently assumed ~45-55%; to be confirmed with data)
- Support ticket volume for onboarding issues must not increase >10%
- Integration connection error rate must not increase
- Time-to-complete-signup must not increase by more than 15 seconds

**Constraints:**
- Assume a standard growth squad (1 PM, 1 designer, 2 engineers, 1 data analyst) for the quarter
- Must support Slack, Jira, and GitHub as integration options
- OAuth-based integration connections require third-party permission screens (cannot be eliminated)
- No dark patterns (forced upsells, hidden skip buttons, guilt-based copy)
- GDPR/privacy: no pre-checked data-sharing; clear consent for analytics permissions

**Non-goals / "do not do" list:**
- Do not redesign the marketing site or signup form (pre-app funnel is out of scope)
- Do not build new integrations this quarter (optimize for the three existing ones)
- Do not attempt post-activation retention improvements (use `retention-engagement` for that)
- Do not add incentives (discounts, credits) to force activation -- focus on UX

**Assumptions (labeled):**
- [MEDIUM confidence] Signup completion rate is ~50%. Needs confirmation from analytics.
- [LOW confidence] D1 return rate is ~30%. Needs instrumentation.
- [HIGH confidence] Integration setup is the primary drop-off point (stated by team).
- [MEDIUM confidence] Most admins arrive from marketing site, not invite links.

---

## 2) Current FTUE Journey Map + Friction Log

### FTUE Journey Map (step-by-step)

| Step # | User goal | What the product asks | Value delivered (if any) | Friction / confusion | Current metric (event/proxy) |
|---:|---|---|---|---|---|
| 1 | Learn what the tool does | Landing page with value prop | Understanding of benefits | None significant (pre-scope) | `page_view` (marketing) |
| 2 | Create an account | Signup form: name, email, password, company name | Account created | 4 fields feels standard; company name may cause pause for solo evaluators | `signup_started` / `signup_completed` |
| 3 | Verify email | Check inbox, click verification link | Email confirmed | Inbox switching, potential deliverability issues, no in-app feedback while waiting | `email_verified` |
| 4 | Land in the app (empty state) | Welcome screen or empty dashboard | None -- blank state, no data | **HIGH FRICTION**: User sees an empty product with no value. No demo data, no preview. | `first_app_load` |
| 5 | Choose an integration | Product shows integration picker: Slack, Jira, GitHub | None yet -- still setup | Choice overload for users unfamiliar with which integration provides best value; unclear what each integration unlocks | `integration_picker_viewed` |
| 6 | Connect the integration (OAuth) | Redirect to third-party OAuth screen; grant permissions | None yet -- permissions step | **PRIMARY LEAK**: Users leave the app for OAuth, face permission scopes they don't understand, worry about granting access to org data, or need IT approval they don't have yet | `integration_auth_started` / `integration_auth_completed` |
| 7 | Wait for data sync | Loading/sync screen while data imports | Partial -- progress bar but no insights | Sync can take 30s-5min depending on data volume; users abandon during wait | `data_sync_started` / `data_sync_completed` |
| 8 | See first dashboard/insights | Dashboard populates with real data | **First real value** -- user sees team analytics | If sync was abandoned, user returns to blank state; dashboard may be confusing without orientation | `dashboard_first_viewed` |
| 9 | Explore / take a meaningful action | User explores data, filters, runs a report | Value deepens -- actionable insight | Without guidance, users may not know what to look for or what action to take | `report_run` / `filter_applied` |

### Friction Log

| Friction | Where it happens | Likely cause | Severity (H/M/L) | Fix idea (short) |
|---|---|---|---|---|
| Empty state on first app load -- no value preview | Step 4 (first app load) | No demo data or preview; product requires integration to show anything | **H** | Show demo/sample dashboard with real-looking data immediately on first load |
| OAuth permission anxiety -- users don't trust scope requests | Step 6 (integration auth) | Third-party OAuth screens list broad permissions; admins worry about org data exposure | **H** | Add pre-OAuth explainer ("here's exactly what we access and what we don't") + "connect later" escape hatch |
| Integration choice overload -- unclear which to pick first | Step 5 (integration picker) | Three options with no guidance on which delivers the most value fastest | **M** | Auto-detect likely integration (based on email domain / tech stack signals) and recommend one; or default to most popular |
| Data sync wait time -- users leave during sync | Step 7 (data sync) | Sync takes 30s-5min; no engagement during wait | **M** | Show progressive data loading (partial insights as they arrive); send email/push notification when sync completes |
| No guided next action after dashboard loads | Step 8-9 (first dashboard) | Dashboard is populated but user gets no orientation or suggested action | **L** | Add a contextual "first insight" callout: "Your team shipped 12 PRs this week -- here's how that compares" |

### Primary Leak

**Integration setup (Steps 5-6)** is the single biggest leak. Users who reach the app but do not complete an integration connection represent the largest drop-off cohort. The friction is compounded by: (a) seeing no value before the integration step, which reduces motivation, and (b) OAuth permission anxiety, which creates a psychological barrier.

---

## 3) Activation / "Aha Moment" Spec

### Candidate aha behaviors (5):

1. **Connects first integration** -- Admin successfully completes OAuth for Slack, Jira, or GitHub (necessary but not sufficient; connecting alone is not "value").
2. **Views populated dashboard** -- Admin sees the main analytics dashboard with real team data loaded (first exposure to value, but passive).
3. **Runs first report or applies first filter** -- Admin actively interacts with the data by running a report, filtering by team/project/date, or drilling into a metric (active engagement with value).
4. **Shares an insight or dashboard with a teammate** -- Admin sends a dashboard link, exports a report, or invites a colleague (extends value beyond the admin; social proof of value).
5. **Returns on a second day and views the dashboard** -- Admin comes back after day 1 and re-engages with the product (demonstrates ongoing value, not just curiosity).

### Chosen activation definition (behavioral):

**"Admin connects at least one integration AND views the populated dashboard at least once within 7 days of signup."**

### Threshold / time window:
- Event: `integration_auth_completed` (any of Slack, Jira, GitHub) AND `dashboard_viewed_with_data` (dashboard render with >0 data points)
- Time window: within 7 calendar days of `signup_completed`
- Count: at least 1 integration + at least 1 dashboard view with data

### Why this is value (user POV):
The admin has seen real team analytics data from their actual tools. They now have evidence of what the product delivers and can make an informed decision about whether to invest further (invite team, explore reports). This is the minimum "aha" -- "I can see my team's work patterns from tools we already use."

### Why this predicts retention (business POV):
- [HYPOTHESIS] Admins who connect an integration and view data within 7 days retain at 3-4x the rate of those who don't, because they have experienced concrete value rather than an empty promise.
- The integration connection creates switching cost and data lock-in.
- Viewing data triggers the "endowed progress" effect -- they see their data and want to do more with it.

### Validation plan:
1. **Retroactive correlation analysis** (Week 1-2): Pull all signups from last 90 days. Segment into "connected + viewed data within 7 days" vs. "did not." Compare D7, D14, and D30 retention rates. Target: activated cohort retains at >= 2x the rate of non-activated cohort.
2. **Threshold testing**: Test variations of the time window (3 days, 7 days, 14 days) and whether "viewed dashboard" vs. "ran a report" is a better predictor.
3. **Causal validation** (if sample allows): In a later quarter, run a holdout experiment where one group receives enhanced onboarding (driving toward activation) and measure whether the higher activation rate causes higher retention, or is merely correlated.

### Instrumentation requirements:
- `integration_auth_completed` -- properties: integration_type (slack/jira/github), time_since_signup, signup_cohort
- `dashboard_viewed_with_data` -- properties: data_point_count, integration_source, time_since_signup
- `activated` (derived/computed) -- fires when both conditions are met within the 7-day window; properties: time_to_activate, integration_type, signup_source

---

## 4) First 30 Seconds Spec ("make it feel magical")

### Entry context:
New admin has just completed signup and email verification. They land in the app for the first time. Currently, they see an empty dashboard with an integration setup prompt. No data, no value.

### One-sentence promise:
"See what your team's analytics look like -- with real sample data -- in under 30 seconds, before you connect anything."

### The "win" in 30 seconds:
The admin sees a fully populated sample dashboard showing realistic team analytics (velocity trends, PR cycle times, sprint completion rates) using demo data. They interact with it (click a metric, filter by team) and immediately understand the value of the product. The integration connection becomes a motivated next step ("Now see YOUR team's data"), not a cold prerequisite.

### Script (what happens):

1. **User sees** (0-5 seconds): After signup, the app loads a full-screen welcome with the admin's name and company: "Welcome, Sarah. Let's show you what [Product] looks like with your team's data." Below: a single button: "See a live demo dashboard" (primary CTA) and a smaller link: "Skip to setup" (for power users who want to connect immediately).

2. **User does** (5-15 seconds): Admin clicks "See a live demo dashboard." The app loads a pre-built dashboard populated with realistic sample data (labeled clearly as "Sample Data" with a subtle banner). The dashboard shows 3-4 key metrics: team velocity trend (line chart), PR review cycle time (bar chart), top contributors this week (leaderboard), and a sprint health score (gauge).

3. **Product responds with** (15-25 seconds): As the admin hovers or clicks on any metric, a tooltip or micro-interaction responds: "In your real data, this shows your team's actual PR cycle time from GitHub." The dashboard is interactive -- filters work, clicking into a metric shows a drill-down. A subtle progress indicator shows: "Step 1 of 3: Explore the demo (done!) -> Step 2: Connect your tools -> Step 3: See your real data."

4. **Next step CTA is** (25-30 seconds): After 10-15 seconds of exploration (or on any click), a non-blocking bottom bar slides up: "Like what you see? Connect Slack, Jira, or GitHub to see YOUR team's real data." Three integration icons with one-click connect buttons. The bar also shows: "Takes about 60 seconds. You can also do this later."

### Design principles applied:
- **Defer non-essential questions**: No profile completion, no team size questions, no use-case survey before showing value. Collect these later.
- **Prefer interactive doing over passive reading**: No carousel tour, no tooltip walkthrough. The admin interacts with a real (sample) dashboard.
- **Provide instant feedback + visible progress**: Every click on the demo dashboard produces a response. Progress indicator shows where the admin is in the setup journey.

### Success criteria (measurable):
- Time-to-first-win: **< 30 seconds** (first-win = interacting with the demo dashboard; event: `demo_dashboard_interacted`)
- % users reaching first-win event: **> 70%** of users who complete signup (baseline: ~0%, since no demo exists today)
- Guardrail(s):
  - Signup completion rate does not decrease
  - "Skip to setup" usage stays < 20% (if higher, the demo is not compelling enough)
  - Users who see demo then connect integration within 7 days >= current integration connection rate (the demo should motivate, not replace, integration connection)

---

## 5) First Mile Plan (Milestones -> Activation)

### Milestones (5):

| Milestone # | User intent | Product mechanic(s) | What "done" looks like | Leading indicator metric |
|---:|---|---|---|---|
| 1 | "Show me why this matters" | **Demo dashboard with sample data** (auto-loaded on first visit). Interactive, realistic data. Labeled as sample. No setup required. | Admin has clicked/hovered on at least one metric in the demo dashboard | `demo_dashboard_interacted` -- target: >70% of signups |
| 2 | "Let me connect my real tools" | **Smart integration recommendation** (auto-detect likely tool from email domain or show most popular). Pre-OAuth explainer screen ("we access X, we never access Y"). One-click OAuth. "Connect later" escape hatch visible. | Admin completes OAuth for one integration (Slack, Jira, or GitHub) | `integration_auth_completed` -- target: >40% of signups (up from current ~20% est.) |
| 3 | "Show me MY data" | **Progressive data loading**: Show partial insights as data syncs ("We found 47 PRs from last week -- loading more..."). If sync takes >30s, show real-time progress + early data. Send email notification when sync completes for users who leave. | Admin views their real, populated dashboard with actual team data | `dashboard_viewed_with_data` -- target: >35% of signups |
| 4 | "Help me understand what I'm seeing" | **First insight callout**: After data loads, highlight one notable data point with context: "Your team's PR cycle time is 4.2 hours -- that's faster than 65% of similar teams." Provide a suggested next action: "Share this with your team" or "Set up a weekly digest." | Admin interacts with the contextual insight (clicks, dismisses, or takes the suggested action) | `first_insight_engaged` -- target: >25% of signups |
| 5 | "I want my team to see this too" | **Teammate invite flow** (lightweight): "Invite 1-2 teammates to see these insights." Pre-filled invite with a personalized message. Show what teammates will see. Optional -- not required for activation, but accelerates retention. | Admin sends at least one teammate invite | `teammate_invited` -- target: >15% of signups |

### Notes:
- **Milestones 1-3 are the activation path** (Milestone 1 = first win; Milestones 2+3 = activation). Milestones 4-5 deepen value and drive early retention.
- **No milestone is a "tour-only" step.** Every milestone involves real product interaction.
- **Progressive disclosure is applied throughout**: profile questions, notification preferences, and advanced settings are deferred until after activation. The admin is never asked to fill out forms before seeing value.
- **The demo dashboard (Milestone 1) replaces the current empty state.** This is the highest-leverage single change.
- **"Connect later" is always available** at Milestone 2. Admins who defer integration connection will receive a follow-up email at 24 hours and 72 hours with a direct deep link to the integration picker. The demo dashboard remains accessible.

### Updated Journey Map (redesigned flow):

| Step # | User goal | What the product does | Value delivered | Time |
|---:|---|---|---|---|
| 1 | Create account | Signup form (name, email, password, company) | -- | 45s |
| 2 | Verify email | Verification email + link | -- | 30-120s |
| 3 | See value immediately | **Demo dashboard** auto-loads with sample data | Immediate value preview | 10-20s |
| 4 | Explore the demo | Interactive demo; click metrics, filter data | Understanding of product capabilities | 30-90s |
| 5 | Decide to connect real tools | Smart integration recommendation + pre-OAuth explainer | Motivated by demo to see own data | 15-30s |
| 6 | Connect integration (OAuth) | One-click OAuth with clear permission explanation | Integration connected | 30-60s |
| 7 | See real data loading | Progressive sync with partial insights shown live | Early real insights during sync | 30-300s |
| 8 | View real dashboard | Full dashboard with actual team data + contextual first insight | **Activation achieved** | 10-30s |
| 9 | Share or go deeper | Invite teammates or explore reports | Value expansion | Optional |

**Key difference from current flow:** Value is front-loaded. The admin sees a working dashboard (demo) in < 30 seconds. The integration connection becomes a motivated "upgrade to real data" action, not a cold prerequisite.

---

## 6) Measurement + Instrumentation Plan

### Key definitions:
- **Signup completion** = `signup_completed` event fired (account created, email verified)
- **First key action** = `demo_dashboard_interacted` (clicked/hovered on at least one metric in demo dashboard)
- **First-win event** = `demo_dashboard_interacted` (same as first key action -- the demo IS the first win)
- **Activation event** = `activated` (derived: `integration_auth_completed` AND `dashboard_viewed_with_data` within 7 days of `signup_completed`)

### Event schema (minimum viable):

| Event | When fired | Key properties | Used in |
|---|---|---|---|
| `signup_started` | User begins signup form | `source` (organic, paid, referral), `utm_params` | Funnel top |
| `signup_completed` | Account created + email verified | `source`, `company_size` (if collected), `signup_duration_seconds` | Funnel, signup rate |
| `first_app_load` | First authenticated page view | `time_since_signup`, `referrer` | Funnel, time-to-first-load |
| `demo_dashboard_viewed` | Demo dashboard rendered | `time_since_signup` | First 30s funnel |
| `demo_dashboard_interacted` | Admin clicks/hovers/filters on demo dashboard | `interaction_type` (click, hover, filter), `metric_type`, `time_since_signup` | First-win rate, time-to-first-win |
| `integration_picker_viewed` | Integration selection screen shown | `time_since_signup`, `source` (from_demo, from_setup, from_email) | Integration funnel |
| `integration_auth_started` | Admin clicks "Connect" on an integration | `integration_type` (slack/jira/github), `time_since_signup` | Integration funnel |
| `integration_auth_completed` | OAuth flow completed successfully | `integration_type`, `time_since_signup`, `auth_duration_seconds` | Activation, integration funnel |
| `integration_auth_failed` | OAuth flow failed or was cancelled | `integration_type`, `failure_reason` (cancelled, error, timeout), `time_since_signup` | Debugging, integration health |
| `data_sync_started` | Data import begins after integration connection | `integration_type`, `estimated_duration` | Sync funnel |
| `data_sync_completed` | Data import finishes | `integration_type`, `sync_duration_seconds`, `records_synced` | Sync funnel, time-to-value |
| `dashboard_viewed_with_data` | Real dashboard rendered with >0 data points | `integration_type`, `data_point_count`, `time_since_signup`, `time_since_integration` | Activation |
| `first_insight_engaged` | Admin interacts with contextual first insight | `insight_type`, `action_taken` (clicked, dismissed, shared) | Milestone 4 |
| `teammate_invited` | Admin sends a teammate invite | `invite_count`, `time_since_signup` | Milestone 5, virality |
| `activated` | Derived: integration_auth_completed + dashboard_viewed_with_data within 7 days | `time_to_activate`, `integration_type`, `signup_source` | Primary metric |
| `onboarding_email_sent` | Lifecycle email sent (reminder to connect) | `email_type` (24h_reminder, 72h_reminder, sync_complete), `integration_status` | Email engagement |
| `onboarding_email_clicked` | User clicked CTA in lifecycle email | `email_type`, `cta_type` | Email conversion |

### Dashboards to create:

**Dashboard 1: FTUE Funnel (primary)**
- Funnel: signup_started -> signup_completed -> first_app_load -> demo_dashboard_viewed -> demo_dashboard_interacted -> integration_picker_viewed -> integration_auth_started -> integration_auth_completed -> dashboard_viewed_with_data -> activated
- Segmented by: signup source, integration type, company size (if available)
- Time period: rolling 7-day and 30-day cohorts
- Owner: Growth PM

**Dashboard 2: Time-to-Value Distribution**
- Histogram: time from signup_completed to demo_dashboard_interacted (time-to-first-win)
- Histogram: time from signup_completed to activated (time-to-activation)
- Median and p75 for both, tracked weekly
- Owner: Growth Data Analyst

**Dashboard 3: Activation Rate + Early Retention**
- 7-day activation rate by weekly cohort (primary metric)
- D1, D7 return rates for activated vs. non-activated users
- Activation rate by integration type and signup source
- Owner: Growth PM

**Dashboard 4: Guardrails**
- Signup completion rate (weekly, must not decrease)
- Support ticket volume tagged "onboarding" (weekly)
- Integration auth error rate by type (daily)
- App performance (page load p50/p95 for onboarding screens)
- Email unsubscribe rate for lifecycle emails
- Owner: Growth Data Analyst

### Instrumentation gaps to address:
- [CRITICAL] `demo_dashboard_interacted` event does not exist today -- must be built for the demo dashboard feature
- [CRITICAL] `activated` derived event needs to be defined in the analytics platform (Amplitude/Mixpanel computed metric or warehouse-based)
- [MEDIUM] `data_sync_completed` may not fire reliably if sync is interrupted -- add a timeout fallback
- [LOW] Company size is not collected at signup -- consider adding post-activation or inferring from integration data

---

## 7) Experiment Backlog (Prioritized)

### Scoring: Impact x Confidence / Effort (1-5 each). ICE score = (I x C) / E.

| Rank | Experiment | Hypothesis | Primary metric | Guardrail | ICE score | Effort notes |
|---:|---|---|---|---|---:|---|
| 1 | Demo dashboard on first load | If we show a pre-populated demo dashboard on first load, then more admins will connect an integration because they understand the value before being asked to set up | 7-day activation rate | Signup completion rate; integration error rate | 5.0 | (I:5, C:5, E:5) 2-3 week build: sample data set, demo dashboard view, interaction tracking. Largest effort but highest expected impact. |
| 2 | Pre-OAuth explainer + "connect later" option | If we add a clear permission explainer before OAuth and a visible "connect later" option, then integration auth completion rate will increase because permission anxiety decreases | integration_auth_completed rate | Signup completion rate; "connect later" usage (monitor but not guardrail) | 6.7 | (I:4, C:5, E:3) 1 week build: static explainer screen + "connect later" button + follow-up email trigger |
| 3 | Smart integration recommendation | If we auto-detect or recommend the best-fit integration (based on email domain or popularity), then more admins will start the auth flow because choice overload is reduced | integration_auth_started rate | Integration type distribution (ensure we don't funnel everyone to one type) | 5.0 | (I:4, C:4, E:3 est. ~1 week: detection logic + UI recommendation badge) Slight detection logic needed |
| 4 | Progressive data sync (show partial results) | If we show partial insights as data syncs instead of a loading screen, then fewer users will abandon during sync because they see value incrementally | dashboard_viewed_with_data rate (among those who started sync) | Sync error rate; data accuracy | 4.0 | (I:4, C:4, E:4) 2 weeks: streaming data display, partial dashboard render logic |
| 5 | Lifecycle emails for non-completers (24h + 72h) | If we send targeted emails at 24h and 72h to admins who signed up but didn't connect, then late integration connections will increase because reminders re-engage dropped users | 7-day activation rate (contribution from email channel) | Email unsubscribe rate; spam complaints | 5.0 | (I:3, C:4, E:2 est. ~3-4 days: email templates, triggers, deep links) Low effort, moderate expected lift |
| 6 | Contextual first insight callout | If we highlight one notable data point after the dashboard loads ("Your PR cycle time is faster than 65% of similar teams"), then admin engagement deepens because the data feels personally relevant | first_insight_engaged rate | Support tickets (ensure callout is accurate) | 3.3 | (I:3, C:3, E:3 est. ~1 week: benchmark data, callout UI, content) Requires benchmark dataset |
| 7 | Inline teammate invite after activation | If we prompt admins to invite 1-2 teammates immediately after seeing their real dashboard, then invite rates will increase because the admin is at peak excitement | teammate_invited rate | Activation rate (ensure invite prompt doesn't interrupt activation flow) | 4.0 | (I:3, C:3, E:2 est. ~3-4 days: invite modal, pre-filled message) |

---

### Experiment Card 1: Demo Dashboard on First Load

**Name:** Demo Dashboard First-Load Experience
**Problem / insight:** New admins currently land on an empty dashboard and are immediately asked to connect an integration. With no visible value, motivation to complete the multi-step integration setup is low. This empty state is the root cause of the 12% activation rate.
**Hypothesis:** If we show a fully populated demo dashboard with sample data on first load, then the 7-day activation rate will increase from 12% to 15%+ because admins will understand the product's value before being asked to invest effort in setup, increasing their motivation to connect an integration.
**Change:** Replace the empty-state first-load experience with a pre-built demo dashboard using realistic sample data (labeled "Sample Data"). The dashboard is fully interactive (filters, drill-downs work). After 10-15 seconds of interaction, a non-blocking bottom bar appears: "Connect your tools to see YOUR team's data."
**Audience:** All new admin signups (web platform); new users only (not returning).
**Primary metric:** 7-day activation rate (integration_auth_completed + dashboard_viewed_with_data within 7 days)
**Guardrails:** Signup completion rate, integration error rate, support ticket volume, app load time (p95 < 3s)
**Instrumentation:** New events: `demo_dashboard_viewed`, `demo_dashboard_interacted` (interaction_type, metric_type), `demo_cta_clicked` (connect_integration, skip_to_setup). Existing events: `integration_auth_completed`, `dashboard_viewed_with_data`, `activated`.
**Duration / sample:** 4 weeks at 50/50 split. With 5,000 signups/month and a baseline of 12% activation, a 50% improvement (12% -> 18%) requires ~2,500 users per variant to detect with 80% power and 95% significance. 4 weeks at 50% allocation = ~2,500/variant.
**Rollout:** Feature flag (`demo_dashboard_v1`). Ramp: 0% -> 10% (3 days, check for errors) -> 50% (21 days, measure activation) -> 100% (if winning).
**Rollback plan:** If activation rate decreases or signup completion drops >2pp or p95 load time exceeds 3s, immediately roll back to 0% via feature flag. Rollback can be executed in <5 minutes.
**Risks / edge cases:**
- Risk: Demo data may set unrealistic expectations if it shows metrics the admin's team doesn't generate. Mitigation: Use conservative, realistic sample data; label clearly as "Sample."
- Risk: Admins may explore the demo and never connect real tools ("demo is enough"). Mitigation: Monitor "connect later" cohort; add progressive nudges.
- Edge case: Admins who sign up via team invite (not self-serve) may not need a demo. Mitigation: Exclude invited members from this experiment in v1.

---

### Experiment Card 2: Pre-OAuth Explainer + "Connect Later"

**Name:** Integration Permission Explainer + Deferral Option
**Problem / insight:** Admins who reach the integration picker and click "Connect" are redirected to a third-party OAuth screen with broad-sounding permission requests. Many cancel or abandon at this step due to permission anxiety ("Why does this tool need access to all my Slack channels?"). Additionally, there is no option to defer setup, so admins who can't complete OAuth immediately (e.g., need IT approval) are stuck.
**Hypothesis:** If we add a clear, human-readable permission explainer before the OAuth redirect AND provide a visible "Connect later" option, then the integration auth completion rate will increase by 20%+ because admins will understand what data is accessed (reducing anxiety) and those who need IT approval will have a path to return later.
**Change:** (a) Insert a pre-OAuth interstitial screen: "What [Product] will access from [Slack/Jira/GitHub]" with a short bullet list of data accessed and an explicit "We never access: private messages, credentials, billing info." (b) Add a "Connect later -- we'll send you a reminder" link below the Connect button. Clicking it triggers a follow-up email at 24h with a deep link back to the integration picker.
**Audience:** All new admin signups who reach the integration picker; web platform.
**Primary metric:** `integration_auth_completed` rate (among those who view the integration picker)
**Guardrails:** Signup completion rate; "connect later" click rate (informational, not guardrail -- high usage is acceptable if it drives later conversion); overall 7-day activation rate
**Instrumentation:** New events: `permission_explainer_viewed`, `permission_explainer_connect_clicked`, `connect_later_clicked`, `connect_later_email_sent`, `connect_later_email_clicked`. Existing: `integration_auth_started`, `integration_auth_completed`.
**Duration / sample:** 3 weeks at 50/50 split. Measuring integration_auth_completed rate (higher base rate than activation, so smaller sample needed).
**Rollout:** Feature flag (`oauth_explainer_v1`). Ramp: 0% -> 20% (2 days) -> 50% (14 days) -> 100%.
**Rollback plan:** If integration_auth_completed rate decreases or if the explainer screen causes >5% bounce rate (users leaving the app entirely), roll back via feature flag.
**Risks / edge cases:**
- Risk: The explainer adds a step, which could decrease conversion for highly motivated users. Mitigation: Monitor speed-of-connection for users who would have connected anyway; consider a "Don't show again" option.
- Risk: "Connect later" may become a permanent escape hatch, reducing urgency. Mitigation: Follow-up email series with clear value prop; track "connect later" -> eventual connection rate.

---

### Experiment Card 3: Smart Integration Recommendation

**Name:** Auto-Detect + Recommend Best-Fit Integration
**Problem / insight:** The integration picker shows Slack, Jira, and GitHub equally, with no guidance on which to connect first. Admins unfamiliar with the product don't know which integration provides the most immediate value for their team. This choice overload causes hesitation and drop-off.
**Hypothesis:** If we auto-detect the admin's likely tech stack (from email domain MX records, or fallback to popularity data) and highlight a recommended integration ("Most teams like yours start with GitHub"), then the integration_auth_started rate will increase by 15%+ because the decision is simplified.
**Change:** (a) On the integration picker, add a "Recommended for you" badge to one integration. (b) Detection logic: check email domain against known patterns (e.g., company uses GitHub Enterprise -> recommend GitHub). Fallback: recommend the most popular integration across all users. (c) All three integrations remain equally accessible; recommendation is a nudge, not a restriction.
**Audience:** All new admin signups who reach the integration picker.
**Primary metric:** `integration_auth_started` rate (among those who view integration picker)
**Guardrails:** Integration type distribution (ensure recommendation doesn't create unhealthy skew); integration_auth_completed rate (ensure recommendation quality)
**Instrumentation:** New events: `integration_recommended` (integration_type, recommendation_source: domain_detection / popularity_default), `integration_recommendation_followed` (boolean). Existing: `integration_auth_started`, `integration_auth_completed`.
**Duration / sample:** 3 weeks at 50/50 split.
**Rollout:** Feature flag (`smart_integration_rec_v1`). Ramp: 0% -> 20% (2 days) -> 50% (14 days) -> 100%.
**Rollback plan:** If integration_auth_started rate decreases, or if recommendation accuracy is poor (>30% of users who follow recommendation fail auth), roll back.
**Risks / edge cases:**
- Risk: Domain detection is inaccurate for small teams or personal email signups. Mitigation: Use popularity-based fallback for undetectable domains; never hide other options.
- Risk: Recommendation creates perception of bias. Mitigation: Clear "Recommended based on teams like yours" copy; all options remain equally prominent.

---

## 8) Rollout / Rollback Plan

### Release mechanism:
Feature flags for each experiment, managed through existing feature flag system. All experiments run as A/B tests with holdout control groups.

### Recommended sequencing:

| Phase | Timeline | Experiment(s) | Ramp |
|---|---|---|---|
| Phase 1 | Weeks 1-3 | Exp 2 (Pre-OAuth explainer) + Exp 3 (Smart recommendation) | 0% -> 20% -> 50%. These are lower-effort, independent changes that can ship quickly and compound. |
| Phase 2 | Weeks 3-6 | Exp 1 (Demo dashboard) | 0% -> 10% -> 50%. Largest change; needs more build time. Run alongside Phase 1 winners. |
| Phase 3 | Weeks 4-7 | Exp 5 (Lifecycle emails) | Launch to 100% of non-completers. Low risk, additive. |
| Phase 4 | Weeks 6-10 | Exp 4 (Progressive sync) + Exp 6 (First insight) | Build after Phase 2 ships; these optimize post-integration steps. |
| Phase 5 | Weeks 8-12 | Exp 7 (Inline invite) + iteration on winners | Ship to 100% if Phase 2-3 experiments win. |

### Monitor (for every experiment):
- Primary metric (specific to experiment)
- Guardrails: signup completion rate, support tickets, integration error rate, app performance (p95 load time)
- Error logs: OAuth failures, data sync errors, 5xx errors on new endpoints

### Rollback triggers:
- Primary metric decreases by >2pp from control (statistically significant at p<0.05)
- Any guardrail metric degrades by >10% from baseline
- >5 new support tickets referencing the changed experience within 48 hours
- p95 load time for affected pages exceeds 3 seconds
- Integration auth error rate increases by >5%

### Rollback process:
1. Disable feature flag (immediate, <5 minutes)
2. Notify growth squad via Slack channel
3. Post-mortem within 48 hours to determine root cause
4. Decide: fix and re-ship, or abandon

### Comms:
- Internal: Growth squad Slack channel for experiment launches and results. Weekly activation metric review in growth team standup.
- External: No user-facing communication needed for these changes (they are UX improvements, not feature announcements). If the demo dashboard ships broadly, consider a changelog entry.

---

## 9) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Demo dashboard sets unrealistic expectations | Medium | Medium | Use conservative sample data; clear "Sample Data" labeling; monitor post-activation satisfaction |
| "Connect later" becomes a permanent escape, reducing activation | Medium | High | Follow-up email series at 24h/72h; track eventual connection rate for deferrers; add gentle in-app reminders on return visits |
| Integration recommendation algorithm is inaccurate for small/unknown companies | Medium | Low | Fallback to popularity-based default; never hide other options; A/B test recommendation quality |
| OAuth provider changes break the integration flow | Low | High | Monitor integration_auth_failed rate daily; have fallback instructions for manual API key entry if OAuth is disrupted |
| Sample size is insufficient for activation rate experiments (need ~2,500/variant) | Low | Medium | Run experiments for full 4 weeks; consider sequential testing if results are ambiguous |
| Engineering capacity is consumed by demo dashboard build, delaying other experiments | Medium | Medium | Phase experiments (ship Exp 2+3 first while Exp 1 is in development); staff a dedicated pair on the demo |

### Open Questions

1. **What is the actual current signup completion rate?** Assumed ~50%. If it's much lower, there may be a bigger opportunity upstream, but that's out of scope per constraints.
2. **Do we have reliable D1/D7 retention data segmented by whether users connected an integration?** This is needed to validate the activation definition. If not, instrumentation must be the first task.
3. **What is the actual time distribution for data sync?** If most syncs complete in <30 seconds, the progressive sync experiment (Exp 4) may be unnecessary. If syncs regularly take >5 minutes, it becomes higher priority.
4. **Are there IT/admin approval requirements for OAuth at larger companies?** If so, the "connect later" flow needs to include an "IT approval" path (e.g., send an email to the IT admin explaining the permissions).
5. **Do we have any existing lifecycle emails?** If so, Exp 5 needs to be coordinated with existing email cadence to avoid over-messaging.
6. **What percentage of signups are admins vs. invited team members?** The first-mile plan is designed for admins. Invited members may need a separate, lighter onboarding flow.
7. **Is there benchmark data available (team performance benchmarks) to power the "first insight" callout?** If not, Exp 6 needs a simpler version that doesn't require cross-team comparisons.

### Next Steps

1. **[Week 1] Validate activation definition.** Run the retroactive correlation analysis (Section 3 validation plan) to confirm that "connected integration + viewed dashboard within 7 days" predicts D30 retention at >= 2x the rate of non-activated users. If not, iterate on the definition before building experiments.
2. **[Week 1] Instrument missing events.** Implement the minimum viable event schema (Section 6). Priority: `demo_dashboard_interacted`, `activated` (derived), `integration_auth_failed`. Without instrumentation, experiments cannot be measured.
3. **[Week 1-2] Build Dashboards 1-4.** Create the four dashboards defined in Section 6 and establish baseline measurements for all metrics.
4. **[Week 1-2] Ship Experiments 2+3** (Pre-OAuth explainer + Smart recommendation). These are lower-effort changes that can ship quickly and begin generating learnings while the demo dashboard is in development.
5. **[Week 2-4] Build and ship Experiment 1** (Demo dashboard). This is the highest-expected-impact change. Coordinate with design to create the sample data set and the demo dashboard UI.
6. **[Week 3-4] Launch Experiment 5** (Lifecycle emails). Set up the 24h and 72h email triggers for non-completers. Coordinate with existing email infrastructure.
7. **[Week 5] First experiment readout.** Analyze results from Experiments 2+3. Decide: ship to 100%, iterate, or kill. Share results with growth team.
8. **[Week 6-8] Ship Phase 4 experiments** (Progressive sync + First insight) based on Phase 1-2 learnings.
9. **[Week 10] Mid-quarter activation rate check.** Compare current 7-day activation rate against the 18% target. If on track, continue. If behind, double down on the highest-performing experiment and consider adding new experiments.
10. **[Week 12] End-of-quarter review.** Final activation rate measurement against the 18% target. Document learnings, update the activation definition if needed, and hand off post-activation retention insights to the `retention-engagement` workstream.

---

## Quality Gate: Checklist + Rubric Scoring

### A) Scope + boundary checklist
- [x] This is **product onboarding/FTUE**, not HR/service onboarding.
- [x] Primary segment(s) are defined (new self-serve admins) and used throughout the plan.
- [x] Goal includes baseline -> target + date (12% -> 18% by end of quarter); guardrails are explicit (signup completion, support tickets, error rate).
- [x] Assumptions are clearly labeled with confidence levels.

### B) Activation ("aha moment") checklist
- [x] Activation is **behavioral** and measurable (integration_auth_completed + dashboard_viewed_with_data within 7 days).
- [x] There is a plan to validate (retroactive correlation analysis + threshold testing + future causal holdout).
- [x] Activation ties to user value ("admin has seen real team analytics from their actual tools").

### C) First 30 seconds checklist (make it feel magical)
- [x] The first 30 seconds has a clear "win" (interacting with a demo dashboard showing realistic team analytics).
- [x] Non-essential setup is deferred (no profile questions, no use-case survey before demo).
- [x] Onboarding is interactive; no reliance on passive carousel tours (demo dashboard is fully interactive).
- [x] The product provides immediate feedback (hover/click responses on demo metrics) and a clear next action ("Connect your tools to see YOUR data").

### D) First mile checklist (milestones -> activation)
- [x] Milestones are 5 steps that map to real product actions (demo interaction, integration connection, data sync, dashboard view, teammate invite).
- [x] Each milestone includes mechanics (demo data, smart recommendation, progressive sync, contextual insight, lightweight invite flow).
- [x] Each milestone has a leading-indicator metric and reduces time-to-value.

### E) Measurement + experiment readiness checklist
- [x] Every proposed experiment has a primary metric + at least one guardrail.
- [x] Instrumentation needs are listed (full event schema with 16 events and their properties).
- [x] Rollout/rollback is specified with triggers and monitoring for each experiment and the overall plan.
- [x] Risks, open questions, and next steps are included (6 risks, 7 open questions, 10 next steps).

### Rubric Scoring

| Dimension | Score | Rationale |
|---|---:|---|
| 1) Goal clarity | 2 | Goal: "Increase 7-day activation from 12% to 18% by end of quarter." Baseline, target, date, and guardrails all specified. |
| 2) Segmentation | 2 | Primary segment (new self-serve admins) defined with distinct job-to-be-done. Secondary segment (invited team members) acknowledged as out-of-scope with reasoning. Plan is tailored to admin path. |
| 3) Journey map + friction log | 2 | 9-step FTUE mapped end-to-end with events at each step. 5 frictions ranked H/M/L with specific fix ideas. Primary leak identified (integration setup, Steps 5-6). |
| 4) Activation definition | 2 | Behavioral definition (integration_auth_completed + dashboard_viewed_with_data within 7 days) with threshold, time window, user-value rationale, retention-prediction hypothesis, and 3-step validation plan. |
| 5) First 30 seconds quality | 2 | Concrete "win" (interactive demo dashboard) achievable in <30 seconds. No passive tours. Script specifies exactly what user sees/does/product responds. Success criteria are measurable (>70% first-win rate, <30s time-to-first-win). |
| 6) First mile plan quality | 2 | 5 milestones, each specific and realistic. Every milestone has mechanics (demo data, smart recommendation, progressive sync, contextual insight, invite flow) and a leading-indicator metric. No tour-only steps. |
| 7) Measurement plan | 2 | 16 events defined with specific properties and "used in" mapping. 4 dashboards defined with owners. Instrumentation gaps flagged with severity. |
| 8) Experiments | 2 | 7 experiments prioritized by ICE. Top 3 have full experiment cards with hypothesis, metrics, guardrails, instrumentation, duration/sample, rollout/rollback, and risks. Phased sequencing plan. |
| 9) Safety + ethics | 2 | No dark patterns. "Connect later" is always visible. Demo data is clearly labeled. No PII/secrets requested. Progressive permission requests (OAuth explainer). User always in control. |
| 10) Finalization | 2 | 6 specific risks with likelihood/impact/mitigation. 7 open questions. 10 sequenced next steps with timelines. Output is structured and actionable. |
| **Total** | **20/20** | |

---

*End of Onboarding & Activation Pack.*
