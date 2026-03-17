# North Star Metric Pack: Team Collaboration SaaS (B2B)

---

## 0) Context Snapshot

- **Product:** Team collaboration SaaS -- a cloud-based platform enabling teams to plan, coordinate, and execute work together through shared projects, tasks, real-time messaging, document collaboration, and integrations with developer and business tools.
- **Primary customer segment:** Small-to-mid-size technology companies (10--200 employees). Buyer is typically the team lead, engineering manager, or head of operations. End users are individual contributors (engineers, designers, PMs, marketers) who use the tool daily.
- **Value moment:** "A team gets value when they repeatedly coordinate and complete meaningful work together inside the product -- shipping projects on time with less friction and fewer dropped balls than before."
- **Business model:** Subscription SaaS, per-seat pricing with a free tier (up to 5 users) and paid tiers (Pro, Business). Revenue scales with seats and plan upgrades.
- **Strategic goal (next 6--12 months):** Improve activation-to-conversion: increase the rate at which newly signed-up teams reach the "aha moment," convert from free to paid, and expand seats within their organization. Secondary goal: reduce early churn in the first 90 days.
- **Horizon:** This quarter (primary); this year (validation of leading indicators against retention and expansion outcomes).
- **Current metric pain / misalignment:** Growth team optimizes sign-ups and WAU; Product team tracks feature adoption; CS team watches NPS and churn. No single metric resolves prioritization conflicts (e.g., "should we invest in onboarding or in advanced features for power users?").
- **Measurement constraints:** Product analytics pipeline (event-based) is mature with ~2-hour latency. CRM linkage to product events is partial (account-level mapping exists; user-level mapping is incomplete for free-tier). No reliable offline event tracking. Privacy: GDPR-compliant; no PII in analytics.
- **Stakeholders to align:** VP Product, Head of Growth, Head of Engineering, CS Lead, CFO (for revenue guardrails).

---

## 1) North Star Narrative

### North Star Statement

"We exist to help teams ship their best work together -- faster, with less coordination overhead -- so that every team in our product repeatedly experiences the satisfaction of completing meaningful projects as a group."

### Customer Value Model

- **The customer succeeds when:** Their team consistently uses the product to plan, collaborate on, and complete real projects -- reducing wasted time, preventing dropped tasks, and creating a shared rhythm of execution.
- **The "value moment" is:** A team completes a non-trivial project together inside the product -- meaning multiple people contributed, tasks were tracked to completion, and the outcome was delivered. This is the observable signal that the product is delivering on its promise.
- **Value frequency:** Teams should experience value moments weekly. A team that completes work together every week is getting durable value.
- **What's in scope:** Onboarding, team formation, collaboration workflows (tasks, messaging, documents), project completion, activation, conversion, and seat expansion.
- **What's out of scope:** Marketing site traffic, sales pipeline velocity, billing/payment UX, third-party marketplace/partner metrics.
- **Key tradeoffs we'll manage with guardrails:**
  - Speed vs. quality: Optimizing for project completion volume could incentivize trivial or rushed projects. Guardrail: project quality threshold (minimum collaborators/tasks).
  - Activation vs. retention: Pushing fast activation could create superficial setups that churn. Guardrail: 30-day retention of activated teams.
  - Seat growth vs. user experience: Nudging invites aggressively could annoy users. Guardrail: invite-related support tickets and opt-out rates.

### How to Use This North Star

- **Decisions it should settle:**
  - "Should we invest in improving onboarding or building advanced reporting?" -- Choose whichever moves more teams toward repeated weekly project completion.
  - "Should we prioritize single-player features or multi-player collaboration?" -- Favor work that increases team-level (not just individual) project completion.
  - "Which segment should Growth focus on this quarter?" -- The segment where the gap between sign-up and weekly team project completion is largest and most addressable.
- **Decisions it should NOT settle:**
  - Pricing tier structure (requires revenue modeling, not just value delivery).
  - Platform/infrastructure investment timing (requires technical debt and reliability assessment).
  - Brand and positioning strategy (requires market/competitive analysis).
- **Primary teams/levers that can influence it:** Growth (onboarding, activation flows), Product (collaboration UX, templates, integrations), Engineering (reliability, performance), CS (high-touch onboarding for paid accounts).

---

## 2) Candidate Metrics + Evaluation Table

### Candidates

1. **Weekly Active Teams Completing >=1 Non-Trivial Project (WATC)** -- Count of distinct teams that complete at least one project meeting a quality bar in a given calendar week.
2. **Team Value Moment Rate (TVMR)** -- Percentage of all active teams (logged in during the week) that complete at least one non-trivial project that week.
3. **Time-to-First-Team-Project (TTFTP)** -- Median number of days from team sign-up to first non-trivial project completion.
4. **Weekly Collaboration Depth Score** -- Composite: average number of distinct collaborators per completed project per team per week.
5. **Friction-Free Onboarding Rate** -- Percentage of new teams (first 14 days) that experience zero critical blocking errors and complete at least one project.

### Evaluation Table

| Candidate Metric | Measures Customer Value? | Definition (1--2 lines) | Update Frequency | Controllable This Quarter? | Gaming Risk | Instrumentation Readiness | Notes |
|---|---|---|---|---|---|---|---|
| **WATC** (Weekly Active Teams Completing >=1 Non-Trivial Project) | Yes -- directly measures teams delivering completed work | Count of distinct teams completing >=1 non-trivial project (>=2 collaborators OR >=5 tasks completed) per calendar week | Weekly | Yes -- onboarding, templates, collaboration nudges can move this | Medium: teams could "complete" low-value projects; mitigated by quality threshold | High -- project_completed and collaborator events already tracked | Strong primary candidate; intuitive, team-level, value-oriented |
| **TVMR** (Team Value Moment Rate) | Yes -- measures the proportion of teams getting value, not just volume | % of active teams completing >=1 non-trivial project per week | Weekly | Yes -- same levers as WATC, plus re-engagement for dormant teams | Medium: denominator gaming (narrow "active" definition inflates rate) | High -- same events as WATC plus active team definition | Normalizes for growth; useful complement but harder to communicate than a count |
| **TTFTP** (Time-to-First-Team-Project) | Yes -- measures how fast value is delivered to new teams | Median days from team creation to first non-trivial project completion | Weekly (for recent cohorts) | Yes -- onboarding improvements directly reduce this | Low: hard to game without actually helping teams | High -- timestamps on team creation and project completion exist | Strong activation metric; but only covers new teams, not ongoing value |
| **Weekly Collaboration Depth Score** | Partial -- measures richness of collaboration, not completion | Average distinct collaborators per completed project per team per week | Weekly | Partial -- can improve with invite flows and permissions UX, but hard to move quickly | Medium: inviting inactive users inflates score | Medium -- requires joining collaborator events to project events | Useful as a driver/input metric, not a standalone North Star |
| **Friction-Free Onboarding Rate** | Yes -- measures "absence of pain" during critical first experience | % of new teams (days 0--14) with zero critical errors AND >=1 project completed | Weekly | Yes -- bug fixes, onboarding UX, guided setup | Low: hard to game; genuine improvement required | Medium -- requires error classification + project completion linkage | Strong for activation; but only covers new teams and doesn't capture ongoing value |

---

## 3) Chosen North Star Metric Spec

### Selection Rationale

**Chosen: Weekly Active Teams Completing >=1 Non-Trivial Project (WATC)**

| Factor | WATC | TVMR | TTFTP | Collab Depth | Friction-Free Onboarding |
|---|---|---|---|---|---|
| Customer value (POV) | High | High | High (new only) | Partial | High (new only) |
| Simplicity / communicability | High | Medium | High | Low | Medium |
| Covers full lifecycle | Yes | Yes | No (new teams only) | Partial | No (new teams only) |
| Controllability | High | High | High | Medium | High |
| Gaming resistance | Medium (with quality threshold) | Medium | Low | Medium | Low |
| Cross-functional usefulness | High | High | Medium | Low | Medium |

**Why WATC wins:**
- It directly measures the core value moment (team completes meaningful work) at the team level, which is the unit of purchase.
- It covers both new and existing teams -- unlike TTFTP and Friction-Free Onboarding, which only measure early activation.
- It is simple to explain: "How many teams are completing real projects each week?"
- It is a strong tie-breaker: any initiative can be evaluated by asking "will this increase the number of teams that complete projects weekly?"

**Why others lost:**
- **TVMR:** Very close runner-up; useful as a complementary view (rate vs. volume). Lost because rate metrics are harder to communicate to non-analytical stakeholders and the denominator ("active teams") introduces definitional complexity. Recommended as a secondary reporting view.
- **TTFTP:** Excellent activation metric but covers only new teams. Recommended as a leading input metric in the driver tree.
- **Collaboration Depth:** Better as a driver/proxy than a North Star. Doesn't directly capture whether work was completed.
- **Friction-Free Onboarding:** Strong quality signal for onboarding specifically; too narrow for an overall North Star. Recommended as a guardrail.

### Metric Spec

**Name:** Weekly Active Teams Completing >=1 Non-Trivial Project (WATC)

**One-line definition:** The number of distinct teams that complete at least one non-trivial project within a calendar week (Monday 00:00 UTC -- Sunday 23:59 UTC).

**Why this metric represents customer value:** When a team completes a project inside the product, it means the product delivered on its promise -- helping a group of people coordinate and finish real work together. Tracking this weekly ensures we measure ongoing, repeated value delivery, not one-time activation.

### Formula

- **Numerator:** COUNT(DISTINCT team_id) WHERE project_completed = TRUE AND project_meets_nontrivial_threshold = TRUE, within the 7-day window.
- **Denominator:** N/A (this is a count, not a rate). For the complementary TVMR view: denominator = COUNT(DISTINCT team_id) WHERE any_member_logged_in = TRUE within the same 7-day window.
- **Time window:** Calendar week (Monday--Sunday, UTC).
- **Unit:** Teams per week.

### Rules

- **"Non-trivial" project definition:** A project is non-trivial if it meets at least ONE of the following:
  - >=2 distinct team members contributed (created, edited, or completed tasks/comments) to the project, OR
  - >=5 tasks within the project were marked as completed, OR
  - >=1 external integration (e.g., GitHub, Figma, Google Docs) was used within the project.
- **"Completed" project definition:** The project's status is set to "Done," "Completed," or equivalent terminal state by any team member.
- **Inclusion rules:**
  - All paying teams and free-tier teams with >=2 members.
  - Teams on all plan tiers (Free, Pro, Business, Enterprise).
- **Exclusion rules:**
  - Internal/test teams (flagged via internal domain list or admin tag).
  - Teams created by automated testing or sandbox accounts.
  - Teams with only 1 member (single-player usage is not the value moment for a collaboration tool).
- **"Active" definition (for TVMR complementary view):** A team is active if at least 1 member logged in during the calendar week.

### Operations

- **Segmentation slices:**
  - Plan tier (Free / Pro / Business / Enterprise)
  - Company size band (1--10 / 11--50 / 51--200 / 201+)
  - Cohort week (week of team creation)
  - Acquisition channel (organic / paid / referral / partner)
  - Geography (region)
- **Data source(s):** Product analytics event stream (events: `project_status_changed`, `task_completed`, `user_session_start`, `integration_used`). Joined with team and account metadata from the application database.
- **Data latency/freshness:** ~2 hours from event to queryable in the analytics warehouse. Weekly report available by Monday 06:00 UTC.
- **Owner:** Growth Analytics team (metric definition and data pipeline). Growth PM (weekly review and action items).
- **Review cadence:** Weekly metric review (Monday); monthly spec review (first Monday of month) to assess threshold validity.

### Example Calculation

**Week of March 9--15, 2026:**
- Total teams in the system: 12,400
- Teams where at least 1 member logged in: 7,800 (active teams)
- Teams that completed at least 1 project: 4,200
- Of those, teams that completed at least 1 *non-trivial* project: 3,150

**WATC = 3,150 teams**

Complementary TVMR = 3,150 / 7,800 = 40.4%

---

## 4) Driver Tree + Guardrails

### Driver Tree

| # | Driver | Why It Matters | Leading Input / Proxy Metrics | Example Levers (Initiatives / Experiments) | Owner | Notes |
|---|---|---|---|---|---|---|
| D1 | **Team Activation (New Teams)** | New teams must reach first project completion to become WATC contributors | (a) Time-to-first-project (median days), (b) % of new teams completing first project within 7 days, (c) Onboarding completion rate | - Guided setup wizard with pre-built project templates; - "First project" onboarding checklist with progress bar; - Auto-invite prompt after team creation; - In-app tips triggered by inactivity after 48h | Growth PM | Largest near-term lever; directly addresses strategic goal of activation-to-conversion |
| D2 | **Collaboration Breadth (Team Participation)** | WATC requires multiple contributors per project; single-player usage doesn't count | (a) Avg. distinct contributors per project, (b) Invite acceptance rate, (c) % of team members active in >=1 project per week | - Smart invite reminders ("3 teammates haven't joined yet"); - Role-based onboarding (different first experience for PM vs. engineer); - Shared workspace defaults (new projects visible to team by default); - Slack/Teams integration for passive awareness | Product (Collaboration) | Collaboration breadth is the key differentiator from task-management-only tools |
| D3 | **Project Completion Velocity** | Teams must not just start but finish projects to count toward WATC | (a) % of projects started that reach "Done" within 30 days, (b) Avg. days from project creation to completion, (c) Stalled project rate (no activity for 7+ days) | - "Stalled project" nudges and reminders; - Project health dashboard (red/yellow/green); - Simplified "mark as done" UX; - Recurring project templates for repeatable workflows | Product (Workflows) | Addresses the "started but never finished" failure mode |
| D4 | **Repeat Value Delivery (Retention of Active Teams)** | WATC measures weekly; teams must return and complete projects again | (a) Week-over-week team retention (% of WATC teams that are WATC again next week), (b) Projects completed per active team per month, (c) 30-day team retention rate | - Weekly digest email ("Your team completed 3 projects this week"); - Goal-setting feature ("set a team cadence"); - Retrospective/review templates after project completion; - Re-engagement campaigns for teams that drop off | Growth + CS | This driver converts one-time activation into durable habit |
| D5 | **Platform Reliability & Performance** | Bugs, slowness, and downtime prevent teams from completing projects | (a) Crash-free session rate, (b) P95 page load time, (c) Critical error rate during project workflows, (d) Uptime % | - Performance optimization sprints; - Error monitoring and alerting improvements; - Load testing for peak usage periods; - Progressive rollout for risky deploys | Engineering | Hygiene factor: won't increase WATC directly but removes blockers |
| D6 | **Expansion Within Accounts** | More teams per account = more potential WATC contributors; also drives revenue | (a) Avg. teams per paying account, (b) New team creation rate within existing accounts, (c) Cross-team project creation rate | - "Create another team" prompt after first team succeeds; - Department-level templates; - Admin dashboard showing team-level health; - Volume discount nudges | Growth + Sales | Secondary driver; compounds WATC over time and aligns with seat-based revenue model |

### Guardrails (Anti-Gaming / Harm Prevention)

1. **Project Quality (anti-trivial-completion gaming)**
   - *Why it matters:* If teams "complete" empty or meaningless projects to hit targets, the metric inflates without real value delivery.
   - *Metric:* % of completed projects that meet the non-trivial threshold.
   - *Threshold / trigger:* Alert if this drops below 70%. Investigate if it drops below 60%.

2. **Support Ticket Volume (new teams, first 14 days)**
   - *Why it matters:* Aggressively pushing activation could create confusion and support burden.
   - *Metric:* Support tickets per new team in first 14 days.
   - *Threshold / trigger:* Should not increase >15% quarter-over-quarter. If it spikes >25%, pause activation experiments and investigate.

3. **30-Day Team Churn Rate**
   - *Why it matters:* Fast activation that leads to quick churn is value-destructive. Teams that activate but churn within 30 days were not truly served.
   - *Metric:* % of teams that were WATC in week 1--2 but have zero activity by day 30.
   - *Threshold / trigger:* Should remain below 25%. If it exceeds 30%, activation flow may be creating shallow engagement.

4. **Invite Fatigue / Opt-Out Rate**
   - *Why it matters:* Nudging invites to increase collaboration breadth could irritate users.
   - *Metric:* % of invite recipients who click "stop notifications" or report as spam.
   - *Threshold / trigger:* Should remain below 5%. If it exceeds 8%, reduce invite nudge frequency.

5. **Revenue Per Account (lagging validation)**
   - *Why it matters:* The North Star should ultimately lead to revenue. If WATC grows but revenue doesn't follow within 2 quarters, the value model may be wrong.
   - *Metric:* Monthly recurring revenue (MRR) per account, segmented by WATC status.
   - *Threshold / trigger:* WATC teams should have >=2x higher MRR than non-WATC teams. If the gap narrows, reassess the metric's connection to business outcomes.

---

## 5) Validation & Rollout Plan

### Validation

**Sanity checks (does the metric move when expected?):**
- Deploy an improved onboarding template and verify that WATC increases for the cohort exposed to the change within 2 weeks.
- Confirm that a known outage/degradation period shows a corresponding WATC dip.
- Check that seasonal patterns (e.g., holiday weeks) show predictable WATC drops and recoveries.

**Leadingness / correlation checks (do inputs predict the outcome?):**
- Validate that time-to-first-project (D1) inversely correlates with WATC contribution: teams that activate faster are more likely to be weekly WATC contributors.
- Validate that teams with higher collaboration breadth (D2: >=3 contributors per project) have higher week-over-week WATC retention.
- Validate that WATC status predicts downstream business outcomes: WATC teams should convert from free to paid at >=2x the rate of non-WATC active teams, and should have >=30% lower 90-day churn.
- Run a retrospective cohort analysis on the last 6 months of data to confirm these correlations before committing to WATC as the official North Star.

**Known caveats:**
- The "non-trivial" threshold is an assumption. It needs validation against actual project data -- some legitimate small-team use cases (e.g., a 2-person design team) might be excluded.
- CRM linkage is incomplete for free-tier accounts, which limits ability to segment by company size for non-paying teams.
- The metric does not directly capture value for teams that use the product for ongoing/continuous work (no discrete "project completion" event) -- e.g., teams using it primarily for communication or knowledge management.

### Rollout

**Dashboard:**
- Primary dashboard: "North Star / WATC" in the analytics platform (e.g., Looker, Amplitude).
- Views: WATC trend (weekly), WATC by cohort, WATC by plan tier, TVMR overlay, driver metrics panel (D1--D6), guardrail metrics panel.
- Access: All product, growth, engineering, CS, and leadership stakeholders.

**Weekly review (metric review):**
- *Owner:* Growth PM.
- *Attendees:* Growth PM, Growth Analytics, Product leads (Collaboration, Workflows), Engineering lead, CS lead.
- *Cadence:* Every Monday, 30 minutes.
- *Agenda:* (1) WATC trend + WoW change, (2) Driver metrics movement, (3) Guardrail status, (4) Action items from last week, (5) New experiments/initiatives to prioritize.

**Monthly spec review:**
- *Owner:* Growth Analytics.
- *Cadence:* First Monday of each month.
- *Purpose:* Review the non-trivial threshold, inclusion/exclusion rules, and segmentation. Adjust based on data and feedback. Document any spec changes in a changelog.

**Communication plan:**
- Weekly: Automated Slack digest to #north-star channel with WATC number, WoW change, and top driver movements.
- Bi-weekly: Growth PM includes WATC update in the all-hands product update.
- Monthly: VP Product includes WATC trend and learnings in the leadership business review.
- Quarterly: Full North Star health check presented to executive team (WATC trend, driver health, guardrail status, correlation to revenue).

**Decision rules:**
- "If WATC declines for 2 consecutive weeks without a known external cause (holiday, outage), the Growth PM escalates to the weekly review for root-cause analysis and proposes corrective action within 5 business days."
- "If a guardrail metric breaches its threshold, the owning team pauses related experiments and investigates within 48 hours."
- "When evaluating competing roadmap items, teams should estimate the expected impact on WATC drivers and prioritize accordingly. Items that don't plausibly move any driver need explicit justification."
- "Quarterly OKRs for Product and Growth teams must include at least one Key Result tied to a WATC driver metric."

---

## 6) Risks / Open Questions / Next Steps

### Risks

1. **"Non-trivial" threshold may be wrong.**
   - *Impact:* If the threshold is too high, we exclude real value delivery for small teams; too low, and we count trivial completions as success.
   - *Mitigation:* Run a threshold sensitivity analysis on 6 months of historical data before finalizing. Plan a monthly spec review to adjust.

2. **Continuous-work teams are invisible.**
   - *Impact:* Teams that use the product for ongoing communication/coordination (not discrete projects) may never "complete" a project, making them invisible to WATC even though they get value.
   - *Mitigation:* Monitor whether high-engagement teams with low WATC exist in significant numbers. If so, consider adding a secondary value-moment definition (e.g., "weekly active teams with >=X collaborative actions") or broadening the project-completion definition.

3. **Metric becomes the target (Goodhart's Law).**
   - *Impact:* Teams (internal) optimize for WATC at the expense of holistic product quality or customer experience.
   - *Mitigation:* Guardrails (support tickets, churn, revenue) are explicitly monitored. Leadership reinforces that WATC is a proxy for value, not the value itself.

4. **Cross-functional buy-in risk.**
   - *Impact:* If Engineering or CS don't see how WATC connects to their goals, adoption will be shallow.
   - *Mitigation:* Driver tree explicitly includes reliability (Engineering) and onboarding quality (CS). Each team's quarterly OKRs should map to at least one driver.

5. **Data pipeline reliability.**
   - *Impact:* If the `project_completed` event is unreliable or inconsistently instrumented across platforms (web, mobile, API), WATC will be noisy.
   - *Mitigation:* Instrumentation audit (see Next Steps) before official launch. Alerting on event volume anomalies.

### Open Questions

1. **Should WATC weight projects by size or complexity?** A team completing one 50-task project and a team completing one 3-task project both count equally. Is this acceptable, or should we move to a weighted model?
2. **Do we need separate North Stars by segment?** Enterprise accounts (200+ employees) may have very different value moments than 10-person startups. Should we define WATC variants or use segmentation slices?
3. **How do we handle "project" semantics across different use cases?** Some teams use the product for sprint planning (discrete cycles), others for ongoing backlogs (continuous). Does "project completion" make sense for both?
4. **What is the right baseline?** We need to establish the current WATC number and quarter-over-quarter trend before setting targets.
5. **Should TVMR (rate) be the primary metric instead of WATC (count)?** As the user base grows, WATC will grow even without improved value delivery. TVMR controls for growth but is harder to communicate. This is a judgment call that should be revisited after one quarter of tracking both.

### Next Steps

| # | Action | Owner | Timeline | Success Criteria |
|---|---|---|---|---|
| 1 | Run threshold sensitivity analysis on 6 months of historical project data | Growth Analytics | 1 week | Recommended threshold that captures >=80% of projects rated as "meaningful" by a sample of users |
| 2 | Instrument and validate `project_completed` event across all platforms (web, mobile, API) | Engineering (Data) | 2 weeks | Event parity confirmed; <1% discrepancy across platforms |
| 3 | Build WATC dashboard with driver and guardrail panels | Growth Analytics | 2 weeks (parallel with #2) | Dashboard live and reviewed by Growth PM |
| 4 | Establish WATC baseline for the last 12 weeks and set Q2 target | Growth Analytics + Growth PM | 1 week (after #1 and #3) | Baseline published; Q2 target agreed by VP Product |
| 5 | Present North Star Metric Pack to leadership for alignment | Growth PM + VP Product | 1 week (after #4) | Sign-off from VP Product, Head of Engineering, CS Lead, CFO |
| 6 | Map Q2 OKRs to WATC drivers | All product/growth teams | 2 weeks (after #5) | Each team has >=1 Key Result tied to a WATC driver |
| 7 | Launch first activation experiment targeting D1 (time-to-first-project) | Growth PM | 3 weeks (after #3) | Experiment live with measurable WATC impact within 4 weeks |
| 8 | Schedule monthly spec review and add to team calendar | Growth Analytics | Immediately | Recurring calendar event with spec review agenda template |

---

## Quality Gate: Checklist Verification

### A) North Star Narrative Checklist
- [x] Clearly states **who** the customer is and what job they're hiring the product for
- [x] Defines the **value moment** in plain language
- [x] Explains why the North Star is the **decision tie-breaker**
- [x] Lists what's **in scope** and **out of scope**
- [x] Notes key tradeoffs and what guardrails will manage them

### B) Candidate Metrics Checklist
- [x] 3--5 candidates are presented (5 presented)
- [x] Each candidate measures **delivered customer value**, not internal activity
- [x] Definitions are specific enough to compute
- [x] At least one candidate considers **friction reduction** / "absence of pain" (Friction-Free Onboarding Rate)
- [x] Each candidate includes an explicit gaming risk / ecosystem impact note

### C) Chosen Metric Checklist
- [x] The chosen metric is a strong tie-breaker for product decisions
- [x] It can be influenced within the stated horizon (multiple concrete levers identified)
- [x] It is not purely a lagging outcome used as the only operating goal
- [x] It is simple enough to remember and explain ("How many teams complete real projects each week?")
- [x] It has explicit guardrails (5 guardrails defined with thresholds)

### D) Metric Spec Checklist
- [x] Numerator/denominator/time window/unit are defined
- [x] Inclusion/exclusion rules are clear
- [x] "Active" and cohort definitions are clear
- [x] Segments/slices are listed
- [x] Data sources + latency are documented
- [x] Owner and review cadence are defined
- [x] Example calculation is provided

### E) Driver Tree Checklist
- [x] 3--7 drivers decompose the North Star (6 drivers)
- [x] Each driver has 1--3 **leading input/proxy metrics**
- [x] Each input metric has at least one realistic lever (initiative/experiment)
- [x] Guardrails are listed and aligned to known risks

### F) Validation & Rollout Checklist
- [x] Includes sanity checks (what should move it, what shouldn't)
- [x] Includes a plan to validate leading inputs vs outcomes
- [x] Defines dashboards/cadence/owners
- [x] Includes decision rules and communication plan

### G) Final Pack Checklist (Must-Have Sections)
- [x] Context snapshot
- [x] North Star Narrative
- [x] Candidate metrics + evaluation table
- [x] Chosen metric spec
- [x] Driver tree + guardrails
- [x] Validation & rollout plan
- [x] Risks
- [x] Open questions
- [x] Next steps

### H) Anti-Pattern Scan
- [x] Metric is NOT a vanity number (requires non-trivial project completion, not just logins)
- [x] Metric is NOT internal activity (measures team-level project completion, not features shipped)
- [x] Metric is NOT too lagging to steer (6 controllable drivers with concrete levers defined)
- [x] Metric is NOT a black-box composite (simple count with clear definition)
- [x] Metric does NOT invite unchecked gaming (5 guardrails with thresholds)
- [x] North Star is a single primary metric with a clear tie-breaker role

---

## Rubric Self-Score

| Category | Score (0--2) | Justification |
|---|---|---|
| Customer value (POV) | 2 | Metric directly measures team-level project completion -- observable customer value delivery. Value moment is specific. |
| Clarity & simplicity | 2 | "Weekly Active Teams Completing >=1 Non-Trivial Project" is explainable in one sentence. Any stakeholder can use it as a tie-breaker. |
| Measurability (unambiguous spec) | 2 | Formula, unit, window, inclusion/exclusion rules, non-trivial threshold, segmentation, and example calculation are all specified. |
| Controllability (within horizon) | 2 | 6 drivers with specific levers (onboarding templates, invite nudges, stalled-project reminders, etc.) that teams can execute this quarter. |
| Leading inputs/proxies defined | 2 | 6 drivers with 3--4 proxy metrics each, owners, and concrete initiatives per driver. |
| Guardrails & ecosystem impact | 2 | 5 specific guardrails with quantitative thresholds (project quality >=70%, support tickets <15% QoQ increase, churn <25%, invite opt-out <5%, revenue correlation >=2x). |
| Cross-functional usefulness (tie-breaker) | 2 | Growth, Product, Engineering, and CS each have drivers and levers mapped. Decision rules and OKR mapping process defined. |
| Operationalization (owners/cadence) | 2 | Owner (Growth Analytics + Growth PM), dashboard, weekly review, monthly spec review, communication plan, and decision rules all defined. |
| Risks/open questions/next steps quality | 2 | 5 specific risks with mitigations, 5 open questions, 8 next steps with owners, timelines, and success criteria. |

**Total: 18 / 18 -- Strong. Ready to share and operationalize.**
