# OKR & Goals Pack — Growth Team, Q2

> **Prompt:** "Set quarterly OKRs for Growth. Teams keep arguing about conversion rate vs volume."

---

## 0) Context Snapshot

- **Cycle + horizon:** Q2 (April 1 -- June 30)
- **Team(s) in scope:** Growth team (acquisition, activation, monetization sub-teams)
- **Strategy anchor (company goal):** Accelerate sustainable user growth -- increase the number of users who activate and retain, not just top-of-funnel volume or isolated conversion rate improvements
- **Baselines + data sources:** Product analytics platform (e.g., Amplitude/Mixpanel); weekly refresh; marketing attribution system; revenue system of record. See KR table for per-metric baselines.
- **Constraints:**
  - Engineering capacity: ~12 engineers across 3 sub-teams; no net-new headcount this quarter
  - Must-do commitments: GDPR consent flow migration (ships mid-April, ~2 eng-weeks)
  - Dependencies: Data Engineering owns the event pipeline; Marketing owns paid spend budget
  - Risk tolerance: Moderate -- willing to run bold experiments but not willing to degrade product quality or trust
- **Stakeholders:**
  - Decider: VP Growth
  - Contributors: Growth PM leads (Acquisition, Activation, Monetization), Data Lead, Eng Manager
  - Approvers: CPO (reviews final OKRs), CFO (reviews monetization guardrails)
  - Review cadence participants: Growth leadership + Data Lead (weekly); CPO (mid-cycle + end-of-cycle)
- **Non-goals:**
  - Not optimizing brand marketing or awareness campaigns (owned by Brand team)
  - Not redesigning the core product experience (owned by Core Product team)
  - Not setting individual performance targets tied to these OKRs
- **Notes / assumptions:**
  - *Assumption 1:* The "conversion rate vs. volume" debate stems from sub-teams optimizing different parts of the funnel in isolation. Acquisition cares about sign-up volume; Activation cares about conversion rate. Neither alone captures the outcome that matters: more activated, retained users.
  - *Assumption 2:* Baselines below are illustrative but realistic for a mid-stage SaaS/product-led company. Actual numbers should be confirmed with the Data Lead in the first week.
  - *Assumption 3:* "Activated user" has an agreed definition (completed core action within 7 days of sign-up). If not, defining this is the first open question.
  - **OKR intent:** OKRs are for focus + learning, not performance evaluation.

---

## 1) Alignment Map

| Company Goal | Team Objective | Why This Is "One Step Away" | Primary Metric(s) It Should Influence | Notes |
|---|---|---|---|---|
| Accelerate sustainable user growth | **O1:** More new users activate and retain (the whole funnel, not just one stage) | Activated + retained users is the direct output of the Growth team's full-funnel ownership; it moves the company's user growth number within the quarter | Activated users/quarter; retained users at Day 30 | Resolves the rate-vs-volume debate by anchoring on absolute activated users |
| Accelerate sustainable user growth | **O2:** Improve the efficiency of growth spend so we can invest more without diminishing returns | Spend efficiency determines whether growth is sustainable and scalable; directly enables the company to invest more confidently | Activated users per $1K spend; payback period | Prevents "growth at any cost" |

---

## 2) OKRs (Objectives + Key Results)

### Objective 1: More new users activate and retain through a healthier full funnel

**Why now:**
- Sub-teams are optimizing in silos: Acquisition pushes volume, Activation pushes conversion rate. Neither is accountable for the combined outcome (absolute activated users).
- Conversion rate improvements are meaningless if they come from narrowing the top of funnel. Volume gains are meaningless if new users churn in week 1.
- This quarter is the highest-leverage moment to align the teams before annual planning locks in budgets.
- Early data shows activation drop-off at setup completion is the single largest leak (58% of sign-ups never complete setup).

**How this supports the company goal:** More activated, retained users directly increases the company's sustainable user growth number. By measuring absolute counts (not just rates), we ensure real user-level impact.

**Primary owner:** VP Growth (accountable); Growth PM -- Activation (day-to-day lead)

#### Key Results -- Objective 1

| KR | Metric Definition (Unambiguous) | Baseline | Target | Window | Owner | Data Source | Type | Anti-Gaming Note | Guardrails |
|---|---|---:|---:|---|---|---|---|---|---|
| **KR 1.1** Increase activated users | Count of unique users who complete the core action within 7 days of sign-up, measured quarterly | 18,000/qtr | 24,000/qtr (+33%) | Q2 | PM -- Activation | Amplitude (event: `core_action_completed`, filter: within 7d of `account_created`) | Absolute | Cannot be gamed by narrowing sign-up criteria -- sign-up volume is tracked separately as a guardrail | **Guardrail:** New sign-ups must stay >= 60,000/qtr (current baseline); activation quality score (see KR 1.3) must not decline |
| **KR 1.2** Increase Day-30 retained users | Count of unique users who return and perform any qualifying action on Day 28-30 after sign-up, measured quarterly | 7,200/qtr | 9,600/qtr (+33%) | Q2 | PM -- Activation | Amplitude (event: any qualifying action, filter: Day 28-30 window post sign-up) | Absolute | Could be inflated by sending aggressive re-engagement emails that drive low-quality sessions | **Guardrail:** Unsubscribe rate on growth emails must stay < 1.2% (current: 0.8%); support ticket rate per retained user must not increase |
| **KR 1.3** Improve setup completion rate (ratio -- with safeguards) | % of new sign-ups who complete the full setup checklist within 48 hours | 42% | 52% | Q2 | PM -- Activation | Amplitude (event: `setup_complete`, filter: within 48h of `account_created`) | Ratio | **Ratio risk:** Could be gamed by (a) making the setup checklist shorter/easier, removing meaningful steps, or (b) reducing sign-up volume so only high-intent users remain. | **Denominator guardrail:** New sign-ups >= 60,000/qtr. **Numerator guardrail:** Setup checklist must retain all current steps (any removal requires VP Growth approval and KR re-baseline). Also tracked as absolute: target >= 31,200 completions/qtr (52% x 60K). |
| **KR 1.4** Reduce time-to-activation | Median calendar hours from `account_created` to `core_action_completed` for users who activate within 7 days | 62 hours | 40 hours | Q2 | Eng -- Activation | Amplitude (median of time delta) | Absolute | Could be gamed by auto-completing steps or pre-filling data that users should configure themselves | **Guardrail:** User-reported "setup was easy" NPS question score must not decline below 7.5 (current: 7.8) |

---

### Objective 2: Improve growth spend efficiency so we can invest more sustainably

**Why now:**
- CAC has risen 18% YoY while activation rates for paid-acquired users lag organic by 15 percentage points.
- The CFO has flagged that Q3 budget expansion depends on proving payback period improvement this quarter.
- Without efficiency gains, more spend just means more waste, not more growth.

**How this supports the company goal:** Sustainable growth requires not just more users but cost-effective acquisition. Improving efficiency unlocks budget for the second half of the year.

**Primary owner:** VP Growth (accountable); Growth PM -- Acquisition (day-to-day lead)

#### Key Results -- Objective 2

| KR | Metric Definition (Unambiguous) | Baseline | Target | Window | Owner | Data Source | Type | Anti-Gaming Note | Guardrails |
|---|---|---:|---:|---|---|---|---|---|---|
| **KR 2.1** Increase activated users per $1K of growth spend | Count of activated users (KR 1.1 definition) divided by total growth spend in $1K increments, measured monthly and rolled up quarterly | 12 activated users/$1K | 16 activated users/$1K (+33%) | Q2 | PM -- Acquisition | Amplitude + Finance spend tracker | Ratio | **Ratio risk:** Could be gamed by cutting spend entirely (denominator shrinks). Could also be gamed by shifting spend to cheap-but-low-quality channels. | **Denominator guardrail:** Total growth spend must stay >= $1.4M/qtr (current baseline). **Quality guardrail:** Day-30 retention rate for paid-acquired users must be >= 35% (current: 32%). |
| **KR 2.2** Increase absolute activated users from paid channels | Count of activated users (KR 1.1 definition) attributed to paid acquisition channels | 6,000/qtr | 8,500/qtr (+42%) | Q2 | PM -- Acquisition | Amplitude + attribution system | Absolute | Attribution model must not change mid-quarter without VP Growth approval; prevents inflating numbers via model tweaks | **Guardrail:** Attribution methodology frozen for Q2; any changes require sign-off and KR re-baseline |
| **KR 2.3** Reduce blended payback period | Median months to recover CAC based on user revenue contribution, measured for Q2 sign-up cohort | 9 months | 7 months | Q2 (measured on Q2 cohort, read at end of Q3 for full data; leading indicator tracked weekly via modeled payback) | PM -- Monetization | Revenue system + Finance model | Absolute | Could be gamed by focusing only on enterprise/high-ARPU segments, ignoring self-serve | **Guardrail:** Self-serve sign-up volume must stay >= 80% of total sign-ups (current: 84%) |

---

## 3) Metric Robustness + Guardrails Summary

### The Conversion Rate vs. Volume Resolution

The core design principle of this OKR set: **lead with absolute counts, use rates only as supporting/diagnostic metrics, and always pair a rate with its denominator guardrail.**

| Metric Type | How We Use It | Safeguard |
|---|---|---|
| Absolute count (e.g., activated users) | **Primary KR** -- this is what we optimize for | Volume guardrails ensure we are not shrinking the funnel to hit targets |
| Ratio/rate (e.g., setup completion %) | **Supporting KR** -- useful for diagnosing where in the funnel we are improving | Always paired with (a) absolute numerator target, (b) denominator floor, and (c) checklist integrity rule |
| Efficiency ratio (e.g., activated users/$1K) | **Primary KR for spend objectives** -- ensures sustainability | Denominator (spend) floor prevents gaming; quality guardrail (retention rate for paid users) prevents channel quality degradation |

### Per-KR Failure Modes and Detection

| KR | Failure Mode 1 | Detection | Failure Mode 2 | Detection |
|---|---|---|---|---|
| KR 1.1 (activated users) | Team narrows sign-up criteria to boost activation rate artificially | Weekly sign-up volume monitoring; alert if < 4,500/week | Team counts low-quality "activations" (e.g., accidental triggers) | Quarterly audit of activation event definition; spot-check 50 random activations |
| KR 1.2 (Day-30 retained) | Aggressive re-engagement spam inflates return visits | Track email unsubscribe rate weekly; alert if > 1.2% | "Qualifying action" definition is too broad (e.g., just opening the app) | Definition frozen for Q2; any change requires Data Lead sign-off |
| KR 1.3 (setup completion %) | Setup checklist simplified to boost completion rate | Checklist change log; VP Growth approval required for any step removal | Denominator (sign-ups) shrinks | Weekly sign-up volume alert; >= 4,500/week |
| KR 1.4 (time-to-activation) | Auto-completing setup steps for users | User satisfaction survey check; NPS question must stay >= 7.5 | Measuring only fast activators (survivorship bias) | Metric includes all activators, not just fastest quartile |
| KR 2.1 (activated users/$1K) | Cutting spend to improve ratio | Spend floor: >= $1.4M/qtr | Shifting to cheap, low-quality channels | Retention rate guardrail for paid users >= 35% |
| KR 2.2 (paid activated users) | Attribution model manipulation | Model frozen for Q2 | Organic users miscounted as paid | Monthly attribution audit by Data team |
| KR 2.3 (payback period) | Cherry-picking high-ARPU segments | Self-serve volume guardrail >= 80% of sign-ups | Modeled payback diverges from actuals | Reconcile model vs. actuals monthly once revenue data matures |

---

## 4) Systems & Habits Plan ("Default-On")

| System/Habit (Default-On) | Cadence | Owner | What It Changes | Evidence/Output Captured |
|---|---|---|---|---|
| **Full-funnel metrics review** | Weekly (Tuesdays, 45 min) | VP Growth + all PM leads + Data Lead | Forces cross-team visibility; prevents silo optimization; surfaces rate vs. volume tensions in real time | Updated dashboard screenshot + 3-bullet decision log posted to #growth-okrs Slack channel |
| **Experiment pipeline review + prioritization** | Weekly (Thursdays, 30 min) | Growth PM leads (rotating chair) | Ensures experiments are ranked by expected impact on absolute activated users, not just local conversion lifts | Ranked experiment backlog + next 2 experiments selected with hypothesis documented |
| **New-user session recordings review** | Weekly (Fridays, 30 min) | PM -- Activation + Design lead | Builds qualitative empathy for activation friction; catches issues dashboards miss | Top 3 friction points documented; filed as improvement candidates |
| **Paid channel quality audit** | Biweekly | PM -- Acquisition + Data Lead | Prevents spend from drifting to cheap-but-low-quality channels | Channel scorecard (volume, activation rate, Day-30 retention) shared with VP Growth |
| **Cross-team activation standup** | Weekly (Mondays, 15 min, async-first) | PM -- Activation | Ensures Acquisition and Activation teams share learnings; prevents "throw users over the wall" dynamic | Async update in shared doc; sync only if blockers exist |
| **Monthly growth spend reconciliation** | Monthly | PM -- Acquisition + Finance | Keeps spend tracking accurate; early warning on CAC drift | Spend report with variance analysis vs. plan |

---

## 5) Review + Grading Plan (Learning Loop)

### Weekly OKR Review (45 min, Tuesdays)

**Attendees:** VP Growth, Growth PM leads (Acquisition, Activation, Monetization), Data Lead, Eng Manager

**Agenda:**
1. **Metric check** (15 min) -- Review all KRs: current value vs. target trajectory. Flag any KR that is > 10% off trajectory as "off-track." Use the shared dashboard (not ad hoc queries).
2. **What changed in the world** (10 min) -- New signals, competitor moves, incidents, experiment results from the past week.
3. **Decide: stop / start / adjust** (15 min) -- Based on data, pick the 1-2 highest-leverage actions for the coming week. Explicitly state what we are *not* doing this week.
4. **Risks / blocks + owners** (5 min) -- Name blockers, assign owners, set deadlines (not "we'll look into it").

**Artifacts produced:**
- Updated KR status: on-track / at-risk / off-track (color-coded in dashboard)
- Decision log: 1-3 bullets posted to #growth-okrs

### Mid-Cycle Checkpoint (90 min, Week 6 -- mid-May)

**Attendees:** VP Growth, Growth PM leads, Data Lead, CPO (invited)

**Decisions allowed:**
- Drop or replace a KR if the metric is proven unmeasurable or irrelevant (document the reason)
- Adjust a target if the baseline was materially wrong (document the original, the new baseline, and the new target)
- Add a guardrail if a new gaming vector or harm pattern is detected
- Reallocate up to 20% of engineering capacity between sub-teams based on where the biggest leverage is

**Decisions NOT allowed:**
- Adding new objectives (scope creep)
- Removing guardrails without CPO approval

**Artifacts produced:**
- Mid-cycle memo (1 page): what is working, what is not, what we are changing and why
- Updated KR targets (if any) with change log

### End-of-Cycle Grading (90 min, final week of June)

**Attendees:** VP Growth, Growth PM leads, Data Lead, Eng Manager, CPO

**Scoring method (per KR):**
| Score | Meaning |
|---|---|
| 0.0 | No progress vs. baseline |
| 0.3 | Some progress but well short of target |
| 0.7 | Meaningful progress; close to target or strong trajectory |
| 1.0 | Target achieved or exceeded |

**Scoring norm:** A 0.7 average across KRs is a good quarter. Consistently scoring 1.0 means targets were too easy. Consistently scoring 0.3 means either targets were unrealistic or execution was blocked.

**Retrospective prompts:**
1. What got in the way of progress? (Be specific: was it capacity, wrong bets, data issues, external factors?)
2. Which "default-on" systems helped most? Which were unused or ineffective?
3. What would we do differently next cycle knowing what we know now?
4. What did we learn about our strategy assumptions? (Was the "rate vs. volume" tension real? Did absolute-count framing help?)
5. What open questions should feed into Q3 OKR planning?

**Artifacts produced:**
- Completed scorecard with per-KR scores + commentary
- Retro summary (1 page): top 3 learnings, top 3 changes for next cycle
- Input doc for Q3 OKR planning

---

## 6) Risks / Open Questions / Next Steps

### Risks

1. **Baseline uncertainty.** The baselines in this pack are assumed, not confirmed. If actual baselines differ by > 15%, targets need re-calibration at the mid-cycle checkpoint. *Mitigation:* Data Lead confirms all baselines by end of Week 1.
2. **GDPR migration steals capacity.** The must-do GDPR consent flow migration could expand beyond the estimated 2 eng-weeks if scope creeps. *Mitigation:* Hard scope cap agreed with Legal; any expansion requires VP Growth + CPO trade-off discussion.
3. **Attribution model fragility.** Paid-channel KRs depend on accurate attribution. If the attribution model has known blind spots (e.g., cross-device, view-through), KR 2.1 and KR 2.2 could be noisy. *Mitigation:* Attribution model frozen for Q2; known limitations documented; monthly audit by Data team.
4. **Silo behavior resurfaces.** Despite the full-funnel framing, sub-teams may revert to optimizing their local metrics. *Mitigation:* The primary KR (activated users) is shared across sub-teams; the weekly full-funnel review creates joint accountability; VP Growth is explicitly the tie-breaker.
5. **Rate vs. volume debate is a symptom of a deeper strategy disagreement.** If the team fundamentally disagrees on whether to grow the top of funnel or deepen conversion, these OKRs may not fully resolve the tension. *Mitigation:* The OKR framing explicitly says "absolute activated users is the North Star for Q2" -- this is a strategic bet that should be named and owned by the VP Growth.

### Open Questions

1. **Is "activated user" well-defined?** Does the team have a shared, instrumented definition of the core action? If not, defining this is the most urgent pre-work before Q2 starts.
2. **What is the actual paid spend budget for Q2?** The $1.4M/qtr floor is assumed. CFO confirmation is needed.
3. **Should we include a monetization KR?** This pack focuses on activation and efficiency. If monetization (e.g., trial-to-paid conversion) is in scope, a third objective may be needed -- but that risks violating the "1-3 objectives" rule. Recommend keeping it out of scope for Q2 and revisiting for Q3.
4. **Are there inter-team dependencies beyond Data Engineering?** If the Activation team depends on Core Product for specific feature work, those dependencies need to be surfaced and committed to.
5. **What happened last quarter?** Understanding what was tried and what failed is critical context for target-setting. The retro from Q1 should be reviewed before finalizing targets.

### Next Steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Confirm all metric baselines with actual data; update KR table | Data Lead | End of Week 1 (Apr 4) |
| 2 | Confirm "activated user" definition is instrumented and agreed | PM -- Activation + Data Lead | End of Week 1 (Apr 4) |
| 3 | Get CFO sign-off on Q2 paid spend budget floor ($1.4M) | VP Growth | End of Week 1 (Apr 4) |
| 4 | Review Q1 retro and incorporate learnings into target calibration | VP Growth + PM leads | End of Week 1 (Apr 4) |
| 5 | Share this OKR pack with CPO for approval | VP Growth | Week 2 (Apr 7) |
| 6 | Freeze attribution model for Q2; document known limitations | Data Lead + PM -- Acquisition | Week 2 (Apr 7) |
| 7 | Set up shared dashboard with all KRs, guardrails, and traffic lights | Data Lead | Week 2 (Apr 7) |
| 8 | First weekly OKR review (inaugural) | VP Growth | Week 2 Tuesday (Apr 8) |

---

## Quality Gate: Checklist Verification

### A) Scope + Alignment
- [x] Cycle, horizon, and team scope are explicit -- Q2, Apr-Jun, Growth team
- [x] A clear strategy anchor exists -- "Accelerate sustainable user growth"
- [x] Each team objective is no more than one step away from the company goal -- verified in alignment map
- [x] Non-goals are explicit -- brand marketing, core product redesign, individual performance targets

### B) Objective Quality
- [x] 1-3 objectives total -- 2 objectives
- [x] Objectives are outcomes, not project lists -- "more users activate and retain" / "improve spend efficiency"
- [x] "Why now" is documented -- per objective
- [x] Each objective is understandable without reading the KRs -- yes

### C) KR Quality
- [x] 2-5 KRs per objective -- 4 for O1, 3 for O2
- [x] Each KR has: definition, baseline, target, time window -- verified in tables
- [x] Each KR has an owner and data source -- verified in tables
- [x] Targets are ambitious enough to change behavior, but not obviously impossible -- +33% is stretch but achievable with system changes

### D) Anti-Gaming + Metric Robustness
- [x] Prefer absolute metrics over ratios -- 5 of 7 KRs are absolute; the 2 ratio KRs have denominator guardrails
- [x] Any ratio KR includes numerator/denominator checks -- KR 1.3 and KR 2.1 both have explicit safeguards
- [x] Each KR includes "how this could be gamed" notes -- verified in per-KR failure modes table
- [x] Guardrails exist to prevent obvious harm -- sign-up volume floors, email unsubscribe limits, attribution freeze, quality checks

### E) Systems & Habits
- [x] At least one default-on system/habit exists per objective -- 6 systems covering both objectives
- [x] Each system has a cadence + owner -- verified in table
- [x] Evidence/artifacts from the system are defined -- verified in table

### F) Review + Grading (Learning Loop)
- [x] Weekly review cadence and agenda are defined -- Tuesdays, 45 min, 4-part agenda
- [x] Mid-cycle checkpoint rules are defined -- Week 6, with explicit allowed/not-allowed decisions
- [x] End-of-cycle grading method and retro prompts exist -- 0.0-1.0 scale + 5 retro prompts
- [x] The grading framing is explicitly for learning, not punishment -- "0.7 average is a good quarter"

### G) Final Pack Completeness
- [x] Context snapshot
- [x] Alignment map
- [x] OKRs (objectives + KR tables)
- [x] Guardrails + anti-gaming notes
- [x] Systems & habits plan
- [x] Review + grading plan
- [x] Risks
- [x] Open questions
- [x] Next steps

---

## Quality Gate: Rubric Self-Score

| # | Dimension | Score | Rationale |
|---|---|---:|---|
| 1 | Discovery + triggering | 2 | Directly addresses the "set quarterly OKRs for Growth" prompt; conversion-vs-volume tension is the central design challenge |
| 2 | Boundaries | 2 | Non-goals stated; pack does not bleed into vision, roadmap, or sprint planning |
| 3 | Input contract | 2 | Assumptions are explicitly labeled; missing info (baselines, budget) flagged in open questions with owners and deadlines |
| 4 | Output contract | 2 | All 7 required deliverable sections present in order |
| 5 | Alignment quality | 2 | Both objectives trace directly to the company goal with documented rationale |
| 6 | Objective quality | 2 | 2 outcome-oriented objectives; "why now" documented; changes weekly prioritization |
| 7 | KR quality | 2 | 7 KRs with definitions, baselines, targets, owners, data sources; two analysts would compute the same number |
| 8 | Anti-gaming + guardrails | 2 | Per-KR failure modes table; ratio KRs have denominator checks; absolute counts are primary |
| 9 | Systems + cadence | 2 | 6 default-on systems with owners + cadence; full learning loop (weekly + mid-cycle + end-of-cycle) |
| 10 | Shareability | 2 | Pack is self-contained; assumptions labeled; next steps have owners and dates |
| | **Total** | **20/20** | |

---

*This OKR & Goals Pack is ready to share with the VP Growth and CPO for review. The most critical pre-work before Q2 starts is confirming baselines and the "activated user" definition (Next Steps 1-2).*
