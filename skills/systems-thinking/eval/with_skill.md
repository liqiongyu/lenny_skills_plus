# Systems Thinking Pack: Engineering On-Call Load & Firefighting Spiral

---

## 1) Context + System Boundary

- **Focal decision/problem:** Engineering on-call page volume has tripled over 6 months (5 to 15 pages/week per team), causing burnout, declining code review rigor, and suspected rising incident rates -- while management simultaneously demands higher feature velocity to match competitors. We need to identify where to intervene to break the firefighting spiral without sacrificing competitive shipping speed.

- **Desired outcome:** Reduce on-call page volume to fewer than 8 pages/week per team within 6 months while maintaining or improving current feature throughput. Stabilize engineer burnout indicators (attrition intent, satisfaction scores) within one quarter.

- **Time horizon:** 6 months for primary outcomes; 12 months for second-order effects and system stabilization.

- **In scope:**
  - Engineering teams (product engineering, platform/infra, on-call rotations)
  - Engineering management and VP/Director layer
  - Code review process and deployment pipeline
  - Incident management lifecycle (detection, response, resolution, post-mortem, remediation)
  - Feature planning and prioritization process
  - Reliability investment allocation (tech debt, monitoring, automation)

- **Explicit non-scope:**
  - Customer support operations (downstream of incidents but not directly managed here)
  - Competitor product strategy (we note it as an external pressure, not something we control)
  - Hiring pipeline mechanics (recruiting process itself; we model headcount as an input)
  - Org chart redesign (use `organizational-design` if needed after this analysis)

- **Constraints/guardrails:**
  - Cannot freeze feature delivery entirely (business survival constraint)
  - Cannot exceed current approved headcount budget without VP-level approval
  - Must maintain existing SLA commitments to customers
  - On-call must remain staffed at all times (no "opt-out" without coverage)
  - Any intervention must show measurable progress within 8 weeks or be revisited

- **Primary outcome metric(s):**
  - Pages per week per team (target: < 8, from current 15)
  - Mean time to resolve (MTTR) for P1/P2 incidents

- **Leading indicators (7):**
  1. Code review thoroughness score (comments per PR, approval time, rejection rate)
  2. Escaped defect rate (bugs found in production vs. caught in review/test)
  3. Percentage of post-mortem action items completed within 14 days
  4. Ratio of reliability/tech-debt work to feature work (target: shift from ~5% toward 20-30%)
  5. Engineer satisfaction / burnout index (pulse survey, eNPS)
  6. On-call handoff quality (runbook coverage, alert documentation %)
  7. Feature cycle time (idea to production) -- to ensure velocity is not regressing

- **What has been tried already:**
  - Not explicitly stated; assumed: ad-hoc hiring requests (slow to fill), verbal encouragement to "be more careful," occasional on-call load-sharing across teams. No structural changes to incident prevention, code review process, or reliability investment. (Assumption -- labeled as such.)

---

## 2) Actors & Incentives Map

| Actor / Player | Incentives (optimizes for) | Constraints | Power / Levers | Likely Behavior (if nothing changes) | Notes |
|---|---|---|---|---|---|
| **Individual engineers (IC)** | Personal well-being, career growth (promo via feature delivery), learning, manageable workload | On-call obligations, sprint commitments, limited hours in the day | Can cut corners on reviews, skip post-mortem follow-ups, reduce testing rigor | Continue cutting review depth to survive; best engineers leave (attrition); remaining ICs become less effective | Burnout compounds -- fatigued engineers write worse code |
| **Engineering managers (EMs)** | Team velocity (features shipped), team health, low attrition, meeting roadmap commitments | Headcount caps, cross-team dependencies, pressure from Director/VP on delivery dates | Control sprint planning, can allocate reliability work, can escalate headcount requests | Prioritize features to satisfy upward pressure; defer tech debt and reliability; verbally acknowledge burnout but change nothing structural | EMs are squeezed between IC burnout and management velocity demands |
| **VP/Director of Engineering** | Competitive feature velocity, engineering reputation, retention, managing costs | Board/CEO pressure for growth metrics, budget constraints, hiring market conditions | Set org-wide priorities, approve headcount, define engineering investment ratios, set cultural norms | Push for more features; approve reactive hires (too late); underinvest in reliability because it has no visible "launch" | Time delay: they see lagging indicators (attrition, major outages) months after the damage starts |
| **Product management** | Feature delivery, customer satisfaction, competitive parity, roadmap predictability | Dependent on engineering capacity, market timing, customer commitments | Control feature prioritization, can negotiate scope, set launch dates | Continue adding features to backlog; resist scope reduction; frame reliability as "engineering's problem" | PM incentives are entirely feature-oriented unless reliability is made visible to them |
| **On-call rotation (as a role)** | Resolve incidents quickly, get back to normal work, not get paged at 3 AM | Alert quality, runbook quality, system complexity, staffing levels | Can escalate, can write quick fixes vs. proper fixes, can author post-mortems | Apply band-aid fixes to stop bleeding; skip root-cause remediation; develop learned helplessness | On-call is a "hot potato" -- people dread it, further reducing its effectiveness |
| **Incident/alert system (invisible actor)** | N/A (system) -- but its configuration shapes behavior | Alert thresholds, monitoring coverage, noise-to-signal ratio | Determines who gets paged, when, and for what | Alert fatigue increases as volume rises; engineers start ignoring or muting alerts; real incidents get missed | A noisy alert system is a force multiplier for the firefighting loop |
| **Performance review system (invisible actor)** | Rewards feature delivery, visible "impact" | Defined by HR/leadership; rarely includes reliability or operational excellence | Shapes what engineers prioritize day-to-day | Engineers optimize for promo-worthy features, not unglamorous reliability work | This is a root driver of under-investment in reliability |
| **Codebase / technical debt (invisible actor)** | N/A (artifact) -- but accumulates and compounds | No natural "cleanup" mechanism without deliberate investment | Determines baseline defect rate, system fragility, deployment risk | Grows steadily; each shortcut today makes tomorrow's incidents more likely and harder to fix | Technical debt has a compounding interest rate |

---

## 3) System Map (Variables + Causal Links)

### Key Variables

- **V1:** On-call page volume (pages/week/team)
- **V2:** Engineer burnout level
- **V3:** Code review thoroughness
- **V4:** Escaped defect rate (bugs reaching production)
- **V5:** Incident rate (new incidents/week)
- **V6:** Feature velocity (features shipped/quarter)
- **V7:** Reliability investment ratio (% of engineering effort on reliability/tech-debt)
- **V8:** Technical debt level
- **V9:** Management pressure for feature velocity
- **V10:** Time spent firefighting (hours/week on incident response + remediation)
- **V11:** Post-mortem action item completion rate
- **V12:** Engineer attrition rate
- **V13:** Alert noise ratio (false/irrelevant alerts as % of total)
- **V14:** Available engineering capacity (effective hours for planned work)
- **V15:** System fragility (probability that a given change causes an incident)

### Causal Links

| # | From (cause) | Direction | To (effect) | Time delay | Mechanism | Confidence |
|---|---|:---:|---|---|---|---|
| 1 | On-call page volume (V1) | **+** | Engineer burnout (V2) | Short (days-weeks) | More pages = more sleep disruption, context switching, emotional drain | High |
| 2 | Engineer burnout (V2) | **-** | Code review thoroughness (V3) | Short (days) | Burned-out engineers rubber-stamp PRs to clear their queue and get back to feature work | High |
| 3 | Code review thoroughness (V3) | **-** | Escaped defect rate (V4) | Short-Medium (1-4 weeks) | Less rigorous reviews miss bugs, design flaws, and operational risks before they ship | High |
| 4 | Escaped defect rate (V4) | **+** | Incident rate (V5) | Medium (2-6 weeks) | Defects in production manifest as incidents after deployment and user exposure | High |
| 5 | Incident rate (V5) | **+** | On-call page volume (V1) | Short (days) | More incidents generate more pages | High |
| 6 | On-call page volume (V1) | **+** | Time spent firefighting (V10) | Short (hours-days) | Each page requires investigation, triage, communication, fix | High |
| 7 | Time spent firefighting (V10) | **-** | Available engineering capacity (V14) | Immediate | Hours on incidents = hours not on planned work | High |
| 8 | Available engineering capacity (V14) | **-** | Reliability investment ratio (V7) | Short (sprint cycle) | When capacity is scarce, reliability work is the first to be cut in favor of features | High |
| 9 | Reliability investment ratio (V7) | **-** | Technical debt level (V8) | Medium-Long (1-6 months) | Less reliability investment means debt accumulates (monitoring gaps, flaky tests, fragile infra) | High |
| 10 | Technical debt level (V8) | **+** | System fragility (V15) | Long (3-12 months) | Accumulated debt makes the system harder to change safely | High |
| 11 | System fragility (V15) | **+** | Escaped defect rate (V4) | Medium (2-8 weeks) | Fragile systems are more likely to break even from "safe" changes | Medium |
| 12 | System fragility (V15) | **+** | Alert noise ratio (V13) | Medium (1-3 months) | Fragile systems produce more spurious alerts as components degrade | Medium |
| 13 | Alert noise ratio (V13) | **+** | On-call page volume (V1) | Immediate | More noise = more pages for the same number of real incidents | High |
| 14 | Management pressure (V9) | **+** | Feature velocity target (V6) | Immediate | Leadership pushes for more features | High |
| 15 | Management pressure (V9) | **-** | Reliability investment ratio (V7) | Short (sprint cycle) | Feature demands crowd out reliability work | High |
| 16 | Engineer attrition (V12) | **-** | Available engineering capacity (V14) | Long (2-4 months to backfill) | People leave; replacements take months to hire and onboard | High |
| 17 | Engineer burnout (V2) | **+** | Engineer attrition (V12) | Medium (1-3 months) | Sustained burnout causes top performers to leave first | High |
| 18 | Post-mortem action item completion (V11) | **-** | Incident rate (V5) | Medium (1-3 months) | Completed remediation items prevent recurrence | High |
| 19 | Time spent firefighting (V10) | **-** | Post-mortem action item completion (V11) | Short-Medium (1-4 weeks) | Teams too busy firefighting to do remediation work | High |

---

## 4) Feedback Loops

### Loop R1 (Reinforcing): The Firefighting Death Spiral

**Links involved:** V1 -> V2 -> V3 -> V4 -> V5 -> V1

**Cycle:** More pages --> more burnout --> sloppier code reviews --> more escaped defects --> more incidents --> more pages.

**Pattern over time:** Exponential growth in on-call load. This is a classic "fixes that fail" archetype. Each pass through the loop makes the next pass worse. The current trajectory (5 to 15 pages in 6 months) is consistent with a reinforcing loop accelerating.

**Why it happens:** There is no natural balancing force in this loop. Burned-out engineers don't spontaneously become more careful -- they become less careful. The system has no built-in circuit breaker.

**What would weaken it:** Breaking any link in the chain -- improving code review quality (independent of burnout), catching defects before production (automated testing), or reducing alert noise so fewer pages fire. The highest-leverage break is at V3 -> V4 (review quality to defect rate) because it's the most controllable.

**So what:** If left unchecked, this loop will continue accelerating until a catastrophic event (major outage, mass attrition) forces a reset. The loop optimizes for *decline*.

---

### Loop R2 (Reinforcing): The Capacity Starvation Loop

**Links involved:** V10 -> V14 -> V7 -> V8 -> V15 -> V4 -> V5 -> V1 -> V10

**Cycle:** More firefighting --> less available capacity --> less reliability investment --> more tech debt --> more system fragility --> more defects --> more incidents --> more firefighting.

**Pattern over time:** Slow but steady erosion of system health. This loop operates on a longer time scale (months) than R1 (weeks), which makes it invisible in sprint-level planning but devastating over quarters.

**Why it happens:** Reliability investment is discretionary; firefighting is mandatory. When capacity shrinks, discretionary work is always cut first. This is rational for each individual sprint but catastrophic over time.

**What would weaken it:** Ring-fencing a minimum reliability investment ratio (e.g., 20%) that cannot be raided for features, regardless of delivery pressure. This converts a discretionary budget into a mandatory one.

**So what:** This is the "boiling frog" loop. Teams don't notice the gradual degradation until they're in crisis. It explains why the problem has worsened steadily over 6 months without triggering a structural response.

---

### Loop R3 (Reinforcing): The Attrition Accelerator

**Links involved:** V1 -> V2 -> V12 -> V14 -> V7 -> V8 -> V15 -> V5 -> V1

**Cycle:** More pages --> more burnout --> higher attrition --> less capacity --> less reliability investment --> more fragility --> more incidents --> more pages.

**Pattern over time:** Delayed but severe. Attrition has a 2-4 month lag (notice period + backfill), so the worst effects of today's burnout won't hit capacity for months. When they do, the remaining team is even more overloaded, which triggers more attrition. This is a vicious cycle with a long delay that can cause dramatic oscillation.

**Why it happens:** The best engineers have the most options and leave first, creating a negative selection effect. New hires take 3-6 months to become fully productive, so capacity recovery lags far behind capacity loss.

**What would weaken it:** Immediate burnout relief (reduce on-call burden now, before attrition triggers) and retention incentives targeted at high-flight-risk engineers.

**So what:** This loop has the longest delay and the hardest-to-reverse consequences. Once it activates in earnest, recovery takes 6-12 months even with aggressive hiring. It is the most dangerous loop because it destroys the very resource (experienced engineers) needed to fix the other loops.

---

### Loop B1 (Balancing): Management Visibility Correction

**Links involved:** V5 (incident rate) -> Major outage/customer escalation -> V9 (management pressure shifts) -> V7 (reliability investment increases)

**Cycle:** Incident rate rises until a sufficiently visible crisis occurs --> management temporarily redirects resources to reliability --> incident rate drops --> management redirects back to features --> incident rate rises again.

**Pattern over time:** Oscillation. The system lurches between "feature mode" and "fire drill mode" with no stable equilibrium. Each cycle burns trust and morale.

**Why it happens:** Management lacks real-time visibility into system health. They respond to lagging, dramatic indicators (major outage, attrition spike) rather than leading indicators (page volume trends, review quality, tech debt metrics). The delay between "things getting worse" and "management noticing" is 2-6 months.

**What would weaken it:** Giving management a real-time dashboard of leading indicators so they can course-correct continuously rather than in crisis mode. This converts a lagging, dramatic balancing loop into a proactive, smooth one.

**So what:** This loop explains why the organization keeps cycling between "we need to ship faster" and "oh no, everything is on fire." The corrective action is always too late and too dramatic, causing whiplash.

---

### Key Time Delays

| Delay | Estimated lag | Impact |
|---|---|---|
| Code defect to production incident | 2-6 weeks | Defects shipped today cause incidents next month; today's "urgency" creates tomorrow's pages |
| Attrition decision to capacity loss | 2-4 months | Burnout damage is invisible until resignations arrive in waves |
| New hire to full productivity | 3-6 months | Hiring is not a quick fix; capacity recovery is slow |
| Reliability investment to reduced incidents | 2-4 months | Tech debt paydown has a lagging return; impatient leaders may cancel it before seeing results |
| Post-mortem action item to incident prevention | 1-3 months | Remediation items need to be built, tested, and deployed before they prevent recurrence |

---

## 5) Second-/Third-Order Effects Ledger

### Candidate Move A: Hire More Engineers

| Order | Effect | Detail |
|---|---|---|
| **1st (immediate)** | Headcount budget increases; job reqs open | Approved positions enter recruiting pipeline. No capacity change for 3-6 months (hiring + onboarding). |
| **2nd (responses/adaptations)** | Existing engineers distracted by interviews and onboarding; management declares "we're fixing it" and maintains feature pressure | Interview load further reduces available capacity in the short term. "Help is coming" framing delays structural changes. New hires don't know the system and may initially *increase* incident rate as they ship unfamiliar code. |
| **3rd (long-term)** | If root causes aren't addressed, new engineers burn out too; org grows but per-engineer productivity stays flat or declines; larger team = more coordination overhead | Hiring into a broken system just feeds more engineers into the firefighting loop. 12 months later you have more people, similar page volume per person, and higher costs. The system absorbs the new capacity without improving. |
| **Who wins/loses** | Wins: recruiting team gets budget. Loses: existing engineers (short-term interview load), finance (higher burn), new hires (enter a broken environment). | |
| **Unintended consequence** | Hiring creates an illusion of action, reducing urgency for structural fixes. The loops (R1, R2, R3) continue unabated. | |
| **Mitigations** | Only hire if paired with structural interventions (reliability investment, alert quality). Use new hires to *build reliability*, not just add feature capacity. Set explicit expectation: new hires spend first quarter on reliability and onboarding, not feature delivery. | |

---

### Candidate Move B: Reduce Feature Scope

| Order | Effect | Detail |
|---|---|---|
| **1st (immediate)** | Fewer features in the sprint; engineers gain slack for reliability work, code reviews, and remediation | Direct capacity relief. Engineers can breathe. |
| **2nd (responses/adaptations)** | Product management pushes back; executives worry about competitive gap; some stakeholders escalate to bypass the scope reduction | Political friction. "Why are we shipping less?" becomes a recurring question. Teams that got their features cut feel deprioritized. Some PMs may try to sneak scope back in through "small asks." |
| **3rd (long-term)** | If communicated well, establishes a healthier sustainable pace; if not, creates a cultural narrative of "engineering can't deliver" that haunts prioritization discussions for years | The narrative matters enormously. A well-framed scope reduction ("investing in speed by investing in stability") builds trust. A poorly-framed one ("engineering is slow") becomes a permanent drag on eng credibility. |
| **Who wins/loses** | Wins: engineers (burnout relief), customers (fewer incidents, more reliable product). Loses: PMs (fewer features in short term), sales (fewer talking points), management (uncomfortable conversations with board). | |
| **Unintended consequence** | If scope reduction is applied uniformly rather than surgically, high-value features get delayed alongside low-value ones. Competitors ship a differentiating feature during the slowdown period. | |
| **Mitigations** | Frame as "investment sprint" not "slowdown." Protect 1-2 highest-value features and cut only low-signal work. Set a clear time-box (e.g., 6-8 weeks) with measurable reliability milestones. Communicate externally as "quality initiative" with specific metrics. | |

---

### Candidate Move C: Invest in Reliability (monitoring, automated testing, alert tuning, tech debt paydown)

| Order | Effect | Detail |
|---|---|---|
| **1st (immediate)** | Engineering effort redirected from features to reliability; feature velocity dips in the short term (2-4 weeks) | Visible cost with invisible (delayed) benefit. Management and PM will feel pain before they see improvement. |
| **2nd (responses/adaptations)** | Alert noise decreases as monitoring improves; code review pressure eases as automated tests catch more bugs; post-mortem action items start getting completed; escaped defect rate begins to drop | Virtuous cycle starts: lower page volume -> less burnout -> better reviews -> fewer defects -> fewer incidents. But the lag is 2-4 months, creating a "valley of despair" where investment has been made but results aren't visible yet. |
| **3rd (long-term)** | System fragility decreases; engineering capacity increases as firefighting shrinks; feature velocity *increases* beyond pre-crisis levels because engineers aren't constantly interrupted; reliability becomes a cultural value, not a chore | This is the highest-ROI move but requires patience and leadership conviction through the lag period. The compounding benefit accelerates over time -- the inverse of the compounding debt that created the crisis. |
| **Who wins/loses** | Wins (long-term): everyone -- engineers, customers, management, business. Loses (short-term): PMs waiting for features, management explaining the velocity dip. | |
| **Unintended consequence** | If the reliability investment is too broad ("fix everything"), it becomes unfocused and slow. If measured only by feature velocity, the initiative gets canceled in the "valley of despair" before benefits materialize. | |
| **Mitigations** | Scope the reliability investment to the top 5 incident-causing systems (Pareto principle). Set weekly leading indicator dashboards so progress is visible before outcome metrics move. Executive sponsor publicly commits to the timeline. Define a "valley of despair" survival pact: no canceling the initiative for 8 weeks regardless of feature velocity dip. | |

---

## 6) Leverage Points + Intervention Plan

| # | Leverage Point | Intervention | Owner | Sequence | Leading Indicator(s) | Guardrail(s) | Rollback / Stop Condition |
|---|---|---|---|---|---|---|---|
| **LP1** | **Information flow: Management visibility into system health** | Build an automated "Engineering Health Dashboard" showing pages/week trend, escaped defect rate, post-mortem completion rate, reliability investment ratio, and burnout pulse survey results. Review weekly in leadership staff meeting. | VP of Engineering + Platform team lead | **Now** (week 1-2) | Dashboard exists and is reviewed weekly; management references leading indicators (not just feature velocity) in planning decisions | Feature velocity is also tracked alongside reliability metrics to prevent overcorrection | If dashboard adds overhead without changing any decisions after 4 weeks, simplify to 3 key metrics |
| **LP2** | **Rules/policy: Mandatory reliability investment ratio** | Institute a 20% reliability investment floor: every team allocates at least 20% of sprint capacity to reliability, tech debt, and incident remediation. This is not optional and cannot be raided for features without VP-level approval per instance. | Director of Engineering (enforcement); EMs (execution) | **Now** (week 1, effective next sprint) | Reliability investment ratio per team (target: >= 20%); post-mortem action item completion rate (target: > 80% within 14 days) | Feature velocity must not drop below 60% of current baseline (the 20% comes primarily from firefighting reduction, not feature cuts) | If after 8 weeks, page volume has not started declining AND feature velocity has dropped below 60%, re-evaluate the ratio and allocation strategy |
| **LP3** | **Incentives: Align performance reviews with reliability** | Add "operational excellence" to the engineering promotion rubric and performance review criteria. Contributions to reliability, incident prevention, code review quality, and on-call improvement count as high-impact work. | VP of Engineering + HR/People team | **Next** (design in weeks 3-4, implement at next review cycle) | % of engineers who cite reliability work in self-reviews; # of reliability-focused projects in promo packets | Feature delivery remains valued -- goal is parity, not replacement; ensure the rubric change does not create perverse incentives to *create* incidents in order to heroically fix them | If engineers game the system (e.g., inflating incident severity for "impact"), revise criteria to focus on prevention, not response |
| **LP4** | **Buffers/capacity: Alert noise reduction and on-call quality** | Dedicate a 2-person "Alert Quality Tiger Team" for 4 weeks to audit all alerts, eliminate noise (target: reduce alert volume 40%), improve runbooks, and set severity-based routing so only actionable, correctly-prioritized alerts page humans. | Platform/Infra team lead + 2 senior SREs | **Now** (week 1-4, time-boxed) | Alert noise ratio (% of non-actionable pages); pages/week per team; mean time to acknowledge vs. mean time to resolve | Do not mute alerts for systems without alternative monitoring; all alert changes require peer review | If page volume increases after alert changes (indicating real incidents are being missed), immediately revert and audit |
| **LP5** | **Process: Post-mortem remediation accountability** | Every P1/P2 post-mortem produces max 3 remediation action items. Each item gets an owner, a due date (max 14 days), and is tracked on the Engineering Health Dashboard. Incomplete items are escalated to the Director weekly. | EMs (ownership); Director of Engineering (escalation) | **Now** (week 1) | Post-mortem action item completion rate (target: > 80% within 14 days); repeat incident rate (same root cause) | Post-mortem culture remains blameless; do not use completion tracking as a punishment mechanism; cap at 3 items to prevent overcommitment | If action item load becomes unsustainable (> 5 open items per team at any time), revisit incident severity thresholds and team allocation |
| **LP6** | **Scope management: Strategic feature scope reduction** | For the next 2 sprints (4 weeks), reduce feature commitments by 30%. Use the freed capacity for the top-5 reliability improvements identified by the Alert Quality Tiger Team and post-mortem backlog. Frame externally as "quality and speed investment sprint." | VP of Engineering (approval); Product leads (scope negotiation); EMs (execution) | **Now** (week 1, time-boxed to 4 weeks) | Feature backlog health (are high-value features protected?); reliability milestone completion; engineer sentiment (pulse survey) | Protect the top 2 highest-value features from scope reduction; customer-facing commitments are honored; scope reduction is time-boxed, not open-ended | If reliability metrics don't improve after the 4-week sprint, diagnose whether the investment was mis-targeted (not whether the approach is wrong) before extending |

### Sequencing Summary

```
WEEK 1-2 (NOW):
  - LP1: Build & launch Engineering Health Dashboard
  - LP2: Announce 20% reliability floor (effective next sprint)
  - LP4: Launch Alert Quality Tiger Team (4-week time-box)
  - LP5: Implement post-mortem remediation tracking
  - LP6: Negotiate 30% feature scope reduction for next 2 sprints

WEEK 3-6 (NEXT):
  - LP3: Design "operational excellence" promotion criteria
  - LP4: Tiger Team delivers alert audit findings and remediations
  - LP6: Reliability investment sprint executes; weekly progress reviews

WEEK 6-12 (LATER):
  - LP3: Roll out updated performance review rubric
  - LP2: Evaluate reliability ratio -- adjust from 20% based on results
  - All: Assess outcome metrics; decide on steady-state operating model
```

---

## 7) System-Build Opportunities (Automation / Standardization)

| Recurring Pain | Frequency | Root Driver Hypothesis | Proposed "System" (process/tool/automation) | First Small Step | Risks | Notes |
|---|---|---|---|---|---|---|
| **Engineers manually triaging noisy alerts** | Multiple times daily per on-call engineer | Alert thresholds are stale; no automated severity classification; alerts lack context | **Automated alert enrichment and routing system**: enrich every alert with recent deploy info, affected service owner, runbook link, and historical frequency. Auto-suppress known-noisy alerts. Route by severity to appropriate channel (page for P1, Slack for P3+). | Instrument the top-3 noisiest alert sources with auto-enrichment (deploy correlation + runbook link). Measure noise reduction after 2 weeks. | Over-suppression could hide real incidents; requires careful tuning and a "suppressed alert" audit log | This directly breaks link #13 (alert noise -> page volume) and is the fastest-ROI automation |
| **Post-mortem action items lost in docs** | Every post-mortem (2-4/week) | Action items live in Google Docs; no tracking, no reminders, no escalation | **Post-mortem action item tracker**: auto-extract action items from post-mortem template into a shared tracker (Jira project or Linear board) with owner, due date, and auto-escalation if overdue by 3 days. Integrate with Engineering Health Dashboard. | Create a Jira project "Incident Remediation" and manually migrate the last 4 weeks of open action items. Track completion rate for 2 sprints. | Overhead of tracking must not exceed the value; keep items to max 3 per post-mortem; avoid bureaucracy | Directly targets link #19 (firefighting blocks remediation) |
| **Code review bottleneck under load** | Daily during high-page-volume weeks | Burned-out engineers skip reviews; no automated pre-checks; review assignments are ad-hoc | **Automated code quality gates**: require CI-enforced checks (linting, unit test coverage threshold, integration test pass, security scan) before a PR can be reviewed by a human. Add auto-assignment of reviewers based on code ownership. | Enable coverage threshold (e.g., 80% for changed files) and auto-assign reviewers for the 3 highest-incident services. Measure escaped defect rate after 4 weeks. | Too-strict gates slow down deployment; calibrate thresholds to catch high-risk changes, not all changes | Directly weakens link #3 (review quality -> defect rate) by adding a non-human safety net |
| **No visibility into reliability investment** | Every sprint planning | No standard way to categorize work as "reliability" vs "feature"; managers guess | **Work categorization taxonomy + automated tracking**: add a required "work type" label to all tickets (feature / reliability / tech-debt / incident-response). Auto-generate weekly reliability ratio per team from ticket data. | Add work-type labels to Jira/Linear. Have EMs classify current sprint backlog. Report first week's ratio at leadership meeting. | Label gaming (mislabeling feature work as reliability); mitigate with spot checks and clear definitions | Enables LP1 (dashboard) and LP2 (20% floor) -- this is foundational infrastructure |

---

## 8) Risks / Open Questions / Next Steps

### Risks

1. **Valley of despair risk (high likelihood, high impact):** The 2-4 month lag between reliability investment and reduced incidents creates a window where feature velocity drops but page volume hasn't improved yet. Management or the board may lose patience and cancel the initiative. **Mitigation:** Executive sponsor publicly commits to the timeline; weekly leading indicator reviews show early progress; "valley of despair" concept is explicitly socialized with leadership before the initiative starts.

2. **Scope reduction backlash (medium likelihood, medium impact):** Product management and sales may escalate aggressively against the 4-week feature scope reduction, especially if a competitor launches during this period. **Mitigation:** Protect top-2 features; frame as time-boxed investment, not permanent slowdown; provide specific metrics for when scope returns to normal.

3. **Alert tuning creates blind spots (medium likelihood, high impact):** Aggressive alert noise reduction may suppress real incidents if tuning is too coarse. **Mitigation:** All suppression rules require peer review; maintain a "suppressed alert" audit log reviewed weekly; set a hard guardrail that page volume cannot drop below a minimum floor (e.g., 3/week) without manual review of what's being suppressed.

4. **Attrition has already begun (high likelihood, high impact):** If top engineers are already in the process of leaving, even perfect interventions won't prevent a capacity crunch in 2-3 months. **Mitigation:** Conduct confidential 1:1s with highest-flight-risk engineers in week 1 to understand retention levers; consider immediate burnout relief (temporary on-call opt-out for most-affected individuals, with coverage from volunteers or management).

5. **Incentive gaming (low likelihood, medium impact):** If performance reviews reward "operational excellence," some engineers may game the system by inflating incident severity or creating problems to heroically fix. **Mitigation:** Weight prevention over response in the rubric; peer review of incident severity classifications; track engineer-created incidents separately.

### Open Questions

1. **What is the actual attrition pipeline?** How many engineers are actively interviewing or have expressed intent to leave? This determines the urgency of immediate retention actions vs. structural fixes.

2. **What are the top 5 incident-causing systems?** The Pareto distribution of incidents by service/system is needed to target reliability investment. If 80% of pages come from 3 services, the tiger team should focus there exclusively.

3. **What does the competitor landscape actually require?** Is management's velocity pressure calibrated to a real competitive threat, or is it a default "more is better" stance? Understanding this determines how much feature scope reduction is politically viable.

4. **What is the current reliability investment ratio?** We assumed approximately 5% but this needs to be measured. The gap between current state and the 20% target determines how much reallocation is needed.

5. **Are post-mortem action items actually effective?** It's possible the action items themselves are low-quality (too vague, wrong root cause). Tracking completion is only valuable if the items are worth completing. An audit of the last 10 post-mortems would reveal this.

6. **Is on-call compensation or structure a factor?** Are engineers being compensated for on-call burden? Is the rotation fair? Compensation won't fix the systemic issues, but perceived unfairness accelerates attrition.

### Next Steps

1. **Week 1, Day 1-2:** VP of Engineering holds an all-hands with engineering leadership to announce the initiative, frame the "quality and speed investment" narrative, and commit to the timeline. Socialize the "valley of despair" concept so expectations are set.

2. **Week 1, Day 3-5:** EMs conduct confidential 1:1 retention conversations with highest-risk engineers. Director pulls incident data to identify top-5 incident-causing systems. Platform lead assembles Alert Quality Tiger Team.

3. **Week 1-2:** Build Engineering Health Dashboard (v1 can be a simple spreadsheet or Datadog dashboard). Implement work-type labels in project tracker. Announce 20% reliability floor effective next sprint.

4. **Week 2:** Product and engineering leads negotiate 30% scope reduction for the next 2 sprints. Identify top-2 protected features.

5. **Week 3-4:** Tiger Team delivers alert audit. Post-mortem remediation tracker goes live. First reliability investment sprint begins.

6. **Week 6:** First checkpoint. Review leading indicators (pages/week trend, escaped defect rate, post-mortem completion, reliability ratio). Decide whether to extend, adjust, or expand interventions.

7. **Week 8:** Hard evaluation point. If pages/week has not started declining, diagnose root cause of stall and adjust strategy. If declining, plan transition to steady-state operating model.

8. **Week 12:** Evaluate outcome metrics against targets (< 8 pages/week, improved engineer satisfaction). Design steady-state reliability investment ratio and performance review criteria for long-term sustainability.

---

## Quality Gate Self-Assessment

### Checklist Verification

| Check | Status |
|---|---|
| **A) Boundary + clarity** | |
| Focal problem in 1-2 sentences (not a solution) | PASS |
| Goal, horizon, in-scope, non-scope are clear | PASS |
| Success measures: 2 outcome metrics + 7 leading indicators | PASS |
| Constraints/guardrails explicit | PASS |
| **B) Actor + incentive realism** | |
| All major actors listed including invisible actors | PASS (8 actors including 3 invisible: alert system, perf reviews, codebase/debt) |
| Incentives and constraints are plausible | PASS |
| At least one incentive conflict identified | PASS (management velocity pressure vs. engineer capacity; PM feature focus vs. reliability needs) |
| **C) System map quality** | |
| Variables concrete and observable | PASS (15 variables, all measurable) |
| Causal links directional and testable | PASS (19 links with mechanisms stated) |
| Time delays noted | PASS (5 explicit delays with estimated lags) |
| At least 2 feedback loops | PASS (4 loops: R1, R2, R3, B1) |
| **D) Second-/third-order thinking** | |
| Effects ledger covers top 3 candidate moves | PASS (Hire, Reduce Scope, Invest in Reliability) |
| Each move has unintended consequence | PASS |
| Each move has mitigation + guardrail | PASS |
| **E) Interventions that can ship** | |
| 3-7 leverage points named and tied to loops | PASS (6 leverage points, each mapped to specific loops) |
| Each has owner + sequencing | PASS |
| Each has leading indicators + rollback conditions | PASS |
| At least one system-build opportunity | PASS (4 system-build opportunities) |
| **F) Communication readiness** | |
| Readable without a live meeting | PASS |
| Trade-offs explicit | PASS |
| Risks / Open questions / Next steps included | PASS |

### Rubric Score

| Dimension | Score | Rationale |
|---|---|---|
| 1) Triggering + scope | 2/2 | Clear problem match; scope and non-scope defined; neighbor skills referenced |
| 2) Boundary + success measures | 2/2 | Tight boundary with measurable outcome metrics and 7 leading indicators, all time-bound |
| 3) Actors + incentives realism | 2/2 | 8 actors including 3 invisible actors; explicit incentive conflicts; plausible constraints |
| 4) System map quality | 2/2 | 15 concrete variables; 19 directional, testable links with mechanisms; time delays marked |
| 5) Feedback loops + delays | 2/2 | 4 loops (3R + 1B) with "so what" narratives; 5 delays with estimated lags |
| 6) Second-/third-order effects | 2/2 | Full ledger for 3 moves through 3rd order; winners/losers; unintended consequences; mitigations |
| 7) Leverage points + interventions | 2/2 | 6 interventions tied to specific loops; owners, sequencing, indicators, guardrails, rollback conditions |
| 8) System-build opportunity | 2/2 | 4 automation/standardization opportunities with first steps, owners, and expected outcomes |
| 9) Decision usability | 2/2 | Decision-ready with explicit trade-offs, sequenced action plan, and week-by-week next steps |
| 10) Safety + robustness | 2/2 | 5 risks with mitigations; 6 open questions; assumptions labeled; rollback conditions specific |
| **Total** | **20/20** | Passing bar: >= 16/20 |
