# Problem Definition Pack — B2B Analytics Activation Drop

## 1. Context snapshot

- **Product:** B2B analytics tool (SaaS)
- **Target user/segment:** Ops managers at companies with 50-500 employees who have recently signed up and connected at least one data source
- **Trigger signal (why now):** Activation rates drop sharply after users connect their data sources. Users complete the data-connection step but fail to reach the "aha moment" (first meaningful insight or report). This indicates a critical break in the onboarding funnel that is directly impacting new-user conversion.
- **Decision to make + deadline:** Decide whether to invest engineering and product resources in fixing the post-data-connection activation flow this quarter (next ~10 weeks). Alternatives: invest this quarter, defer to next quarter, or deprioritize entirely.
- **Constraints:**
  - Engineering capacity is shared with other roadmap commitments; a fix must be scoped to fit within a partial team allocation
  - Data integrations vary widely (warehouse, SaaS connectors, CSV); any solution must work across connector types
  - Customer data is sensitive (financial, operational); privacy and access-control requirements apply
  - Mid-market segment (50-500 employees) often lacks a dedicated data team, so the solution must not assume technical sophistication

## 2. Problem statement

**1-liner:** Ops managers at mid-market companies who connect data sources to our analytics tool fail to reach their first actionable insight, causing them to abandon the product before experiencing its value.

**Expanded:**

- **Symptoms (what we observe):**
  - Users complete account setup and data-source connection but do not create or view a report/dashboard within their first 7 days
  - Session frequency drops to near-zero within 3-5 days of connecting a source
  - Support tickets spike around "I connected my data, now what?" and "My dashboard is empty"
  - Trial-to-paid conversion for users who connect a source but don't activate is estimated to be significantly lower than for users who reach first insight

- **Likely root causes (hypotheses):**
  1. **Value gap after connection:** Connecting a data source feels like the hard part, but the product does not guide the user to a meaningful next step (e.g., a pre-built report, a suggested metric)
  2. **Data readiness delay:** After connecting, data may take time to sync or require transformation before it is usable; the user encounters a "cold start" with empty dashboards
  3. **Permissions/access confusion:** In mid-market orgs, the ops manager who connects the source may not have the right permissions to query certain tables, or needs IT involvement that stalls progress
  4. **Overwhelming interface:** Post-connection, the user lands in a blank workspace with too many options and no clear starting point
  5. **Misaligned expectations:** Marketing/sales promised quick insights, but the product requires manual configuration before delivering value

- **Impact:**
  - **User:** Ops managers waste time on setup without getting the operational visibility they need; they revert to spreadsheets or prior tools, losing the time invested in onboarding
  - **Business:** Low activation directly suppresses trial-to-paid conversion; each lost activation represents wasted acquisition spend and potential churn before revenue

- **Why now:**
  - The company has been investing in top-of-funnel growth (marketing, partnerships, new connectors), which means more users are entering the funnel -- but the activation leak means growth spend is increasingly inefficient
  - Recent connector improvements made it *easier* to connect sources, paradoxically surfacing the post-connection drop more clearly in the data
  - Competitors in the mid-market analytics space are shipping guided onboarding and time-to-value improvements, raising the bar for activation

## 3. JTBD (Jobs To Be Done)

**Primary job:** When I have just connected my company's data sources to the analytics tool, I want to quickly see a meaningful operational insight relevant to my role, so I can confirm the tool is worth my time and start making better decisions.

**Sub-jobs:**
1. **Understand what my data can tell me:** After connection, I need to know what reports or metrics are possible with the data I just connected, without manually exploring schemas or writing queries.
2. **Get a useful report without heavy configuration:** I want to see a pre-built or suggested dashboard that is relevant to my role (ops) and my industry, so I don't start from a blank slate.
3. **Share an early win with my team/manager:** I need to demonstrate value to justify continued use and potential upgrade, so I need a shareable artifact (report, chart, insight) quickly.
4. **Troubleshoot data issues without IT dependency:** If my data isn't showing up correctly or is incomplete, I need clear guidance on what's wrong and how to fix it myself.

**Success criteria (user POV):**
- Within 30 minutes of connecting a data source, I have viewed at least one insight or report that is relevant to my operational responsibilities
- I can explain to a colleague what the tool showed me and why it matters
- I do not need to contact support or IT to get from "data connected" to "first insight"

## 4. Current alternatives

| Alternative | Who uses it | Why it works today | Gaps / pain | Switching costs |
|---|---|---|---|---|
| **Spreadsheets (Excel/Google Sheets) with manual data exports** | Most ops managers in this segment | Familiar tool; full control; no permissions issues; works offline | Time-consuming manual updates; error-prone; no real-time visibility; hard to share live dashboards | Very low -- already the default; switching *away* from spreadsheets requires proving speed and reliability advantage |
| **Ask IT/data team to pull reports** | Ops managers at companies with a small data team | Accurate data; someone else does the work | Slow turnaround (days/weeks); ops manager depends on another team's priorities; limited to pre-defined reports | Low -- no new tool to learn; cost is waiting time and lack of self-service |
| **Existing BI tool (Looker, Metabase, Power BI)** | Companies that already invested in BI infrastructure | Established workflows; integrated with other systems | Requires technical skill to configure; ops managers often can't self-serve; expensive at scale | High -- data pipelines, dashboards, training, and organizational habits are already built around the incumbent |
| **Do nothing / gut feel** | Smaller companies or early-stage ops functions | Zero effort; no tool to maintain | Poor decisions; invisible inefficiencies; reactive instead of proactive | Zero -- but the cost of inaction grows as the company scales |
| **Competitor analytics tools with guided onboarding** | Ops managers evaluating alternatives | Some competitors offer templates and guided setup that reduce time-to-first-insight | May lack depth, specific integrations, or pricing fit for mid-market | Medium -- requires re-evaluating, re-connecting data, and re-training the team |

**Why would a user switch from their current alternative?**
The core promise is self-service operational insights without waiting for IT or manually wrangling spreadsheets. If the tool delivers a relevant insight within minutes of connecting data -- faster and more reliably than the alternatives -- the switching cost is justified. But right now, the product fails to deliver on that promise at the critical moment (post-connection), so users have no reason to switch away from their current workflow.

## 5. Evidence & assumptions log

| # | Claim / assumption | Evidence we have | Confidence | Test to validate | Owner |
|---|---|---|---|---|---|
| 1 | Activation drops sharply after data-source connection | Funnel data showing step-over-step drop (stated signal) | **High** | Confirm exact drop rate and segment breakdown from analytics dashboard | Product analytics |
| 2 | The primary cause is a "cold start" experience (empty state, no guidance post-connection) | Support tickets mentioning "now what?" and "empty dashboard"; anecdotal feedback from CS | **Medium** | Session replay analysis of first 10 minutes post-connection for 30+ users; categorize where users get stuck | UX research |
| 3 | Ops managers in 50-500 employee companies lack technical skill to self-configure dashboards | Segment assumption based on company size and role; no direct measurement | **Medium** | Survey or interview 10-15 recently churned users in segment to assess technical comfort and setup experience | Product + UX research |
| 4 | Data sync delays contribute to the drop (users see empty dashboards because data isn't ready) | Engineering knows some connectors have 15-60 min sync times; no user-facing data on impact | **Medium** | Correlate activation rates with connector type and sync duration; identify whether fast-sync connectors have better activation | Data engineering + analytics |
| 5 | Providing a pre-built, role-relevant report immediately post-connection would improve activation | Hypothesis -- no direct evidence yet | **Low** | Prototype test (see Section 8) with ops manager participants | Product + design |
| 6 | Permissions and access issues block a meaningful subset of users | CS reports some tickets about permissions, but volume is unclear | **Low** | Quantify permission-related support tickets as % of total post-connection tickets; interview 5 affected users | CS + engineering |
| 7 | Users who reach first insight within 24 hours convert to paid at a significantly higher rate than those who don't | Directional belief based on general SaaS activation patterns; not yet validated for this product | **Medium** | Cohort analysis: compare conversion rates for users who view a report within 24h vs those who don't | Product analytics |

**Key "killer assumption":** If assumption #5 is wrong (i.e., the problem is not about guidance/cold start but about fundamental data quality or product-market fit), then investing in activation UX this quarter would not move the needle.

## 6. Success criteria + guardrails

**Outcome metric(s):**
- **Activation rate (primary):** % of users who connect a data source AND view/interact with a meaningful report or dashboard within 7 days. Current estimated baseline: ~30%. Target: 50%+ within one quarter of shipping the fix.
- **Trial-to-paid conversion for activated users:** Confirm that improving activation correlates with higher conversion (expected but needs validation).

**Leading indicators (movable in weeks):**
- **Time-to-first-insight:** Median time from data-source connection to first report view. Target: reduce from estimated >48 hours to <2 hours.
- **Post-connection session return rate:** % of users who return to the product within 48 hours of connecting a source. Target: increase by 20% relative.
- **"Empty state" encounter rate:** % of post-connection sessions where the user sees a blank/empty dashboard. Target: reduce to <10%.

**Guardrails (must not worsen):**
- **Support ticket volume:** Post-connection support contacts per new user must not increase (should decrease)
- **Data integrity / trust:** Any pre-built reports or auto-generated insights must be accurate; showing incorrect data would destroy trust and accelerate churn
- **Onboarding completion rate for data connection step:** Fixing post-connection must not make the connection step itself harder or longer
- **System performance:** Auto-generated reports must load within acceptable latency (<5 seconds); slow reports are worse than no reports
- **Privacy/access controls:** Pre-built reports must respect existing data permissions; no user should see data they shouldn't have access to

## 7. Scope boundaries

**In scope:**
- The experience from "data source successfully connected" to "first meaningful insight viewed" for the primary segment (ops managers, 50-500 employees)
- Diagnosis of root causes for the activation drop (analytics, session replays, user interviews)
- Design and prototype of post-connection guidance (e.g., suggested reports, templates, onboarding checklist)
- Evaluation of data-sync timing and its impact on activation
- Definition of activation metric and instrumentation to track it

**Out of scope / non-goals:**
- Redesigning the data-connection flow itself (pre-connection steps are working; this quarter focuses on post-connection)
- Building new data connectors or expanding connector coverage
- Addressing activation for segments outside ops managers at 50-500 employee companies (enterprise and SMB segments are deferred)
- Full BI feature parity with incumbent tools (Looker, Power BI); the goal is first insight, not advanced analytics
- Pricing or packaging changes
- Marketing/sales messaging changes (may be a follow-up, but not part of this problem definition)

**Dependencies:**
- **Data engineering:** Need connector-level sync time data and the ability to surface sync status to users
- **Design:** Need design capacity for prototype exploration (estimated 2-3 weeks of design time)
- **Analytics instrumentation:** Need to define and instrument the activation event if not already tracked
- **CS/support:** Need access to post-connection support ticket data and willingness to participate in user identification for research

## 8. Prototype / learning plan

**Hardest assumptions to test (top 3):**
1. The primary blocker is lack of guidance post-connection (not data quality, not permissions, not product-market fit)
2. A pre-built, role-relevant report delivered immediately post-connection will meaningfully increase activation
3. Ops managers in this segment can self-serve from a suggested starting point without technical support

**Prototype/test approach:**

### Test A: Concierge onboarding (Week 1-2)
- **Type:** Concierge / high-touch manual
- **Audience:** 15-20 new users in the target segment who just connected a data source
- **Method:** CS team manually reaches out within 1 hour of connection, walks the user through creating their first report using a standardized script, and observes where they get stuck
- **Key questions:** Where do users get stuck? Is the blocker guidance, data readiness, permissions, or something else? Do users who receive this help activate and return?
- **Success criteria:** 70%+ of concierge users reach first insight within the session; qualitative feedback confirms the problem was "didn't know what to do next" (not "data wasn't useful")
- **Timeline:** 2 weeks

### Test B: Clickable prototype of guided post-connection flow (Week 2-4)
- **Type:** Clickable prototype (Figma)
- **Audience:** 8-10 ops managers in target segment (mix of existing users and prospects)
- **Method:** Show a prototype that presents 2-3 suggested reports immediately after data connection, with a "your data is loading" state and estimated time. Observe comprehension, interest, and click behavior.
- **Key questions:** Do users understand the suggested reports? Do they find them relevant? Does the loading state manage expectations or frustrate?
- **Success criteria:** 80%+ of participants say they would use at least one suggested report; average comprehension score of 4+/5
- **Timeline:** 2 weeks (overlaps with Test A analysis)

### Test C: Instrumented A/B (if Tests A+B are positive) (Week 5-8)
- **Type:** Live A/B test with minimal viable implementation
- **Audience:** All new users in target segment (50/50 split)
- **Method:** Ship a lightweight version of the top-performing prototype direction; measure activation rate, time-to-first-insight, and 7-day retention
- **Key questions:** Does the intervention move activation rate meaningfully? What is the effect on downstream conversion?
- **Success criteria:** Statistically significant improvement in activation rate (target: +10 percentage points or more vs control)
- **Timeline:** 3-4 weeks of runtime for statistical significance

## 9. Risks / Open questions / Next steps

**Risks:**
- **Root cause misdiagnosis:** If the activation drop is primarily caused by data quality issues or product-market fit problems (not UX/guidance), the prototype approach will not move the metric. Mitigation: Test A (concierge) is designed to surface the real blocker before committing to a build.
- **Connector heterogeneity:** The post-connection experience varies significantly by connector type (e.g., warehouse vs SaaS API vs CSV). A one-size-fits-all solution may not work. Mitigation: Segment analysis in Week 1 to identify if certain connector types have dramatically different activation rates.
- **Capacity competition:** If the team cannot allocate sufficient design + engineering time this quarter, the prototype/A/B timeline will slip. Mitigation: Scope Test A (concierge) to require zero engineering; use results to make the investment case for engineering time.
- **Pre-built report relevance:** Suggested reports may not be relevant across industries and ops functions in the segment. Mitigation: Start with 3-5 universally relevant operational metrics (e.g., throughput over time, anomaly detection, trend comparison) rather than industry-specific reports.
- **Data privacy exposure:** Auto-generating reports could inadvertently surface sensitive data to users who shouldn't see it. Mitigation: Reports must inherit existing permission model; include a privacy review in the design sprint.

**Open questions:**
1. What is the exact current activation rate by segment and connector type? (Need analytics pull -- this number is critical to size the opportunity.)
2. How long does data sync take for each major connector type, and what % of users encounter >30 min sync delays?
3. Do we have session replay data for the post-connection experience, or do we need to instrument it?
4. Is there an existing definition of "activation" in the product, or do we need to define and instrument it from scratch?
5. What is the revenue impact per percentage point of activation improvement? (Needed to justify the investment vs other roadmap items.)
6. Are there contractual or compliance constraints on auto-generating reports from customer data?

**Next steps (owners + dates):**

| # | Action | Owner | Target date |
|---|---|---|---|
| 1 | Pull activation funnel data by segment and connector type; establish baseline | Product analytics | Week 1 |
| 2 | Audit post-connection support tickets (last 90 days); categorize root causes | CS lead | Week 1 |
| 3 | Set up session replay tracking for post-connection flow (if not already instrumented) | Engineering | Week 1 |
| 4 | Launch concierge onboarding test (Test A) with 15-20 target-segment users | CS + Product | Week 1-2 |
| 5 | Design clickable prototype for guided post-connection experience (Test B) | Design lead | Week 2-3 |
| 6 | Conduct prototype usability sessions (Test B) | UX research | Week 3-4 |
| 7 | Synthesize Test A + B findings; make go/no-go decision on A/B test investment | Product lead (DRI) | Week 4 |
| 8 | If go: implement and launch A/B test (Test C) | Engineering + Product | Week 5-8 |
| 9 | Final readout and quarter decision (invest further / scale / deprioritize) | Product lead (DRI) | Week 8-10 |

---

## Quality gate

### Checklist verification

**1) Problem statement checklist**
- [x] 1-liner identifies who, context, pain, and impact
- [x] Avoids embedding a solution or technology choice
- [x] Includes why now (trigger/event)
- [x] Defines the problem in terms that could be proven wrong (testable)

**2) JTBD checklist**
- [x] Primary job is written as When... I want... so I can...
- [x] Sub-jobs cover major steps (not features)
- [x] Success criteria are from the user's perspective (not internal KPIs)

**3) Alternatives + switching checklist**
- [x] Includes what users do today (including "do nothing")
- [x] Includes at least one analog/non-digital alternative (spreadsheets, ask IT)
- [x] Explains why current alternatives work (not just why they're bad)
- [x] Calls out switching costs
- [x] Answers "Why would a user give this the time of day?"

**4) Evidence & assumptions checklist**
- [x] Separates knowns from hypotheses
- [x] Each key claim has evidence or an explicit "unknown" label
- [x] Top 1-3 riskiest assumptions have a concrete test plan
- [x] Avoids the "shiny object trap" (no specific tech prescribed)

**5) Success + guardrails checklist**
- [x] Outcome metric(s) reflect user value delivered
- [x] Leading indicators are controllable in weeks/months
- [x] Guardrails protect against harm (trust, quality, cost, support load, latency)
- [x] Metrics are defined unambiguously

**6) Prototype/learning plan checklist**
- [x] The team can describe the end state
- [x] Prototype is the fastest path to learning (concierge before build)
- [x] Success criteria for the test are defined in advance
- [x] Includes timeline, audience, and key questions

**7) Finalization checklist**
- [x] Includes Risks / Open questions / Next steps with owners
- [x] Assumptions are labeled and reviewable
- [x] A stakeholder can decide "proceed/pause/stop" async

### Rubric scoring

| Category | Score | Rationale |
|---|---|---|
| 1) Clarity of problem | 2 | 1-liner is specific and solution-free; expanded statement includes impact, hypothesized causes, and why now |
| 2) Target segment + context | 2 | Segment is recruitable (ops managers, 50-500 employees, recently connected a data source); situation and stakes are described |
| 3) JTBD quality | 2 | Primary job + 4 sub-jobs are outcome-oriented; user success criteria are defined and distinct from product metrics |
| 4) Alternatives + differentiation | 2 | 5 alternatives including analog (spreadsheets, ask IT) and "do nothing"; switching costs and "why switch" are explicit |
| 5) Evidence + assumptions | 2 | 7 claims with evidence levels and confidence ratings; top assumptions have concrete test plans; killer assumption identified |
| 6) Metrics + guardrails | 2 | Outcome metric (activation rate) with baseline and target; 3 leading indicators; 5 guardrails with specifics |
| 7) Scope boundaries | 2 | In/out and non-goals are explicit; 4 dependencies with owners identified |
| 8) Prototype/learning plan | 2 | 3-phase test plan targeting hardest assumptions first; concierge before build; clear success criteria and timeline |
| **Total** | **16/16** | |
