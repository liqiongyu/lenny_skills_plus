# Delegation Pack: Improve Onboarding Activation

**Skill used:** `delegating-work`

---

## Assumptions (intake gaps)

The user provided: the work item ("Improve onboarding activation"), the delegatee role (PM), and the timeline (6 weeks). The following details were not provided and are filled with reasonable assumptions, clearly labeled.

- **Owner identity:** A mid-level PM on the Growth team with 2+ years of product experience; currently at moderate workload; growth goal of leading cross-functional projects end-to-end. *(Assumed)*
- **Success metric:** Onboarding activation rate (defined as the percentage of new sign-ups who complete the core "aha moment" action within their first 7 days). Current baseline assumed to be ~30%; target improvement of +5 pp (to ~35%) or a data-backed recommendation with validated experiment plan if the 6-week window is discovery-focused. *(Assumed)*
- **Budget / headcount:** No incremental headcount; PM can pull from existing Eng + Design resources within the Growth pod. *(Assumed)*
- **Autonomy preference:** "Decide with guardrails" -- the PM decides research approach, experiment design, and cross-functional sequencing; escalates scope changes, timeline slips > 1 week, and anything touching pricing or core signup flow logic. *(Assumed)*
- **Stakeholders:** Growth team lead (approver), Engineering lead (consulted), Design lead (consulted), Marketing (informed on messaging changes), Data/Analytics (consulted). *(Assumed)*

---

## Step 1 -- Frame the Delegation Decision

### 1) Delegation Brief

**Work item:** Improve onboarding activation -- diagnose the current onboarding funnel, identify the highest-leverage opportunities, design and (if feasible) run experiments to lift the activation rate.

**Owner:** [PM Name] -- Product Manager, Growth Team

**Why now (context):**
Onboarding activation is the single largest lever for improving retention and revenue growth. Recent cohort analysis shows that users who do not reach the "aha moment" within the first 7 days churn at 3x the rate of activated users. The executive team has flagged activation as a top-3 company priority this quarter, and there is a window to ship improvements before the next major acquisition push. Waiting longer compounds the loss: every month of delay means thousands of new sign-ups fall through the funnel without activation.

**Outcome / Definition of done:**
- **Primary deliverable(s):**
  1. A diagnostic memo: root-cause analysis of where and why users drop off during onboarding (funnel data, qualitative insights, segment breakdowns).
  2. An experiment plan: 2-3 prioritized experiment concepts with hypotheses, expected impact, effort estimates, and success criteria.
  3. At least one experiment launched (or launch-ready with eng signoff) by end of Week 6.
  4. A final learning memo summarizing results, recommendations, and next steps.
- **Acceptance criteria / success metrics:**
  - Diagnostic memo reviewed and accepted by Growth lead by end of Week 2.
  - Experiment plan reviewed and approved by end of Week 3.
  - At least one experiment live (or launch-ready) by end of Week 6.
  - Final learning memo delivered by end of Week 6.
  - Activation rate measurement framework is in place and baseline is validated.

**Non-negotiables (guardrails):**
- **Timeline / milestones:** 6 weeks total. Diagnostic complete by Week 2; experiment plan approved by Week 3; first experiment live by Week 5; wrap-up and learning memo by Week 6.
- **Quality bar:** Recommendations must be grounded in data (quantitative funnel analysis + at least 5 qualitative user interviews or session replays). No "gut feel only" proposals.
- **Budget / headcount:** Work within existing Growth pod resources. No new tool purchases > $500 without approval.
- **Policy / compliance / security:** No changes to authentication flows, data collection practices, or privacy consent without Legal/Security review. No dark patterns.
- **Customer impact constraints:** No degradation of existing onboarding experience for active users. Experiments must have rollback plans.

**Scope**
- **In-scope:** New user onboarding flow (signup through activation moment); experiment design and execution; cross-functional coordination with Eng, Design, Data, Marketing.
- **Out-of-scope:** Retention beyond the first 7 days (separate initiative); pricing/packaging changes; mobile app onboarding (web only for this cycle); fundamental product strategy pivots.

**Stakeholders**
- **Approvers (must sign off):** Growth team lead (diagnostic memo, experiment plan, final memo).
- **Consulted (input):** Engineering lead, Design lead, Data/Analytics, Customer Support (for qualitative signal).
- **Informed (visibility):** Marketing (if messaging changes are part of experiments), VP Product (end-of-project summary).

**Known risks / landmines:**
- Eng capacity may be constrained in Weeks 4-5 due to a platform release; plan experiments that can flex on timing.
- Previous onboarding experiments (Q3 last year) showed that tooltip-heavy approaches did not move the needle; avoid retreading without new evidence.
- The "aha moment" definition may need re-validation -- if the current proxy metric is wrong, the first week should surface this.

**Links / references:**
- Current onboarding funnel dashboard: [link]
- Q3 experiment retrospective doc: [link]
- User research repository (onboarding tag): [link]
- Company activation metric definition: [link]

---

## Step 2 -- Pick the Owner + Autonomy Level

**Owner:** [PM Name] -- Mid-level PM, Growth Team

**Autonomy level:** Decide with guardrails

**What this means in practice:**

| Decision area | Autonomy | Notes |
|---|---|---|
| Research approach (surveys, interviews, data analysis methods) | PM decides | Inform manager of approach in Week 1 update |
| Experiment design (hypotheses, variants, targeting) | PM decides within guardrails | Must meet quality bar (data-grounded, rollback plan) |
| Cross-functional prioritization within Growth pod | PM decides | Coordinate directly with Eng/Design leads |
| Scope changes (adding/removing experiment concepts) | PM recommends, manager approves | Escalate before committing to scope changes |
| Timeline adjustments > 1 week | Escalate to manager | Bring options + tradeoffs, not just the problem |
| Changes to auth flow, data collection, privacy | Escalate to manager + Legal/Security | Non-negotiable review gate |
| External customer communication changes | PM recommends, manager approves | Marketing must be consulted |
| Tool/vendor spend > $500 | Escalate to manager | Bring ROI justification |

**Boundaries:**
- **"On assignment" (less flexibility):** The diagnostic memo format, the milestone dates, the quality bar (data-grounded), and the non-negotiables above.
- **"High flexibility" (PM's call):** How to conduct research, which experiments to prioritize, how to structure cross-functional collaboration, the experiment implementation approach.

**Check:** Both manager and PM should be able to clearly answer: "What decisions are mine vs yours?" If there is any ambiguity after the kickoff conversation, clarify immediately.

---

## Step 3 -- Context Handoff Pack

**Background summary (10 bullets):**
1. Onboarding activation is defined as completing the core "aha moment" action within 7 days of sign-up.
2. Current activation rate is approximately 30% (validated against the last full-quarter cohort).
3. The executive team has identified activation as a top-3 company priority for this quarter.
4. Users who do not activate within 7 days churn at 3x the rate of activated users, making this the highest-leverage retention lever.
5. The Growth pod (Eng + Design + PM + Data) has capacity allocated for this initiative.
6. Previous experiments (Q3 last year) tested tooltip overlays and guided tours; neither produced statistically significant activation lifts. The retro concluded that the interventions addressed symptom (confusion) but not root cause (unclear value proposition in the first session).
7. Qualitative research from Q2 suggested that users who connected their first integration or completed their first workflow activated at 2x the base rate -- but the sample size was small.
8. The onboarding funnel has not been instrumented below the page level; event-level tracking may need to be added in Week 1.
9. Marketing is planning a new acquisition campaign in 8 weeks -- improvements to activation will compound the ROI of that spend.
10. There is an existing onboarding funnel dashboard, but it has not been updated since Q3; data validation is a Week 1 task.

**Prior decisions + rationale:**
- Q3 tooltip experiment was killed after 3 weeks: no stat-sig lift, high eng cost. Decision: "Do not retry tooltip-heavy approaches without new root-cause evidence."
- The "aha moment" was defined 18 months ago as [core action]. It has not been re-validated since the product expanded scope. Decision: "Re-validate the activation proxy as part of this initiative."
- A proposal to overhaul the entire signup flow was deprioritized in Q1 due to eng cost. Decision: "Focus on post-signup experience for this cycle; signup flow changes are out of scope."

**Constraints explained (why they exist):**
- The 6-week timeline aligns with the quarterly planning cycle; findings will feed into next quarter's roadmap.
- No auth flow changes because the Identity team has a security audit in progress; any changes would require a full re-audit.
- Web-only scope because the mobile app has a separate team and codebase; cross-platform changes would double coordination cost.

**Known gotchas / pitfalls:**
- The funnel dashboard may show misleading numbers if bot traffic is not filtered (validate data source in Week 1).
- The Eng lead prefers experiment proposals as PRDs, not slide decks; match their format expectations.
- Design capacity is shared with the Retention squad in Weeks 3-4; book design time early.
- Customer Support has a backlog of onboarding-related tickets that could be a goldmine for qualitative insights -- but the tickets are not tagged consistently.

**Example outputs ("what good looks like"):**
- A diagnostic memo that is 3-5 pages, includes a funnel visualization, segment analysis, qualitative themes, and a clear "so what" section with prioritized opportunity areas.
- An experiment plan that uses a hypothesis-driven format: "We believe [change] will [outcome] because [evidence]. We will measure [metric]. Success = [threshold]."
- A final learning memo that captures what was learned regardless of whether the experiment "won."

**Evidence / data sources:**
- Product analytics platform (Amplitude/Mixpanel): funnel events, cohort analysis
- User research repository: tagged interviews, session replays
- Customer Support tickets: onboarding-related tag
- Q3 experiment retro doc
- Company metric definitions wiki

---

## Step 4 -- Decision Rights + Guardrails

**Autonomy level:** Decide with guardrails (see Step 2 table for detail)

**Owner can decide:**
- Research methodology and sequencing (quantitative analysis, user interviews, surveys, session replays)
- Which experiment concepts to pursue (within the approved experiment plan)
- How to structure cross-functional collaboration and meetings
- Day-to-day prioritization within the Growth pod's allocated capacity
- Experiment targeting, variant design, and rollout percentage (within guardrails)
- Communication approach with consulted stakeholders

**Escalation triggers (pull manager in):**
- Any proposed scope change to the initiative (adding/removing major workstreams)
- Timeline slip > 1 week on any milestone
- Eng capacity conflict that cannot be resolved within the Growth pod
- Any change that touches authentication, data collection, or privacy consent
- Any customer-facing communication change (email, in-app messaging copy changes that go beyond the experiment)
- Experiment results that suggest a fundamental product strategy question (e.g., "our aha moment is wrong")
- Spend > $500 on tools or vendors
- Disagreement with a stakeholder that cannot be resolved peer-to-peer

**Required review points (artifacts + timing):**

| Review | Artifact | Timing | Reviewer |
|---|---|---|---|
| Review 1 | Diagnostic memo (draft) | End of Week 2 | Manager + Growth lead |
| Review 2 | Experiment plan (2-3 concepts) | End of Week 3 | Manager + Eng lead |
| Review 3 | Experiment launch checklist (rollback plan, success criteria, monitoring) | Week 5 (pre-launch) | Manager + Eng lead |
| Review 4 | Final learning memo + recommendations | End of Week 6 | Manager + Growth lead |

**Quality criteria (how we judge output):**
- Diagnostic memo: grounded in data (quantitative + qualitative); includes segment analysis; identifies root causes, not just symptoms; has a clear "so what" with prioritized opportunities.
- Experiment plan: hypothesis-driven; each concept has expected impact, effort, and success criteria; risks and rollback plans are included.
- Final memo: honest assessment of results regardless of outcome; clear next steps; learnings are actionable.

---

## Step 5 -- Plan + Milestones (Owner-Led)

The following is a starting-point plan. The PM should review, adjust, and propose their own version. The manager's role is to ask questions, not prescribe the path.

**Suggested milestone plan:**

| Week | Milestone | Key outcome |
|---|---|---|
| Week 1 | Kickoff + data foundation | Validate funnel data, instrument missing events, review prior research, schedule 5+ user interviews. PM restates problem and proposed approach in own words. |
| Week 2 | Diagnostic memo delivered | Root-cause analysis complete. Funnel analysis, qualitative themes, and prioritized opportunity areas. Reviewed and accepted by Growth lead. |
| Week 3 | Experiment plan approved | 2-3 experiment concepts with hypotheses, expected impact, effort, success criteria. Reviewed and approved by manager + Eng lead. |
| Week 4 | Build + prep | Experiments built/configured. Design assets ready. QA complete. |
| Week 5 | First experiment launched | Experiment live with monitoring, rollback plan confirmed, success criteria dashboard set up. |
| Week 6 | Results + learning memo | Preliminary results analyzed. Final learning memo delivered with recommendations for next cycle. |

**First-week plan (PM to refine):**
- Day 1-2: Review all existing docs (prior retro, funnel dashboard, user research). Validate data sources. Identify instrumentation gaps.
- Day 3-4: Schedule and begin user interviews / session replay reviews. Pull cohort data for segment analysis.
- Day 5: Draft initial hypotheses. Share a brief async update with manager (what you've found, what's surprising, what's missing).

**Questions for the manager to ask (thought-partner mode):**
- "What's your hypothesis for the biggest drop-off point, and what would change your mind?"
- "Which user segments do you think are most worth focusing on, and why?"
- "What's the riskiest assumption in this plan?"

---

## Step 6 -- Execution Cadence

**Cadence:** Weekly synchronous check-in (30 min) + mid-week async update

**Medium:**
- Weekly check-in: 1:1 meeting (calendar invite)
- Mid-week async: Slack thread or short doc update (3-5 bullets)

**Weekly check-in agenda (default):**
1. Progress vs. outcome (where are we relative to the milestone?)
2. Decisions made since last check-in (for visibility, not approval)
3. Decisions needed (framed as options + tradeoffs)
4. Top 1-3 risks + mitigations
5. Asks / blockers
6. Next milestone + ETA + confidence level

**Mid-week async update format (copy/paste):**
```
**Progress vs outcome:** [1-2 sentences]
**Decisions made / needed:** [bullets]
**Risks + mitigations:** [bullets]
**Asks / blockers:** [bullets]
**Next milestone + ETA:** [date + confidence: green/yellow/red]
```

**Rules of engagement:**
- Manager will "refuse to rule" unless an escalation trigger fires or the work drifts from the outcome/guardrails. If the PM asks "what should I do?", the manager's default response is: "What are your options, and what do you recommend?"
- Owner brings options and tradeoffs, not just status or problems.
- If an escalation trigger fires between check-ins, use Slack DM for immediate resolution; do not wait for the weekly sync.
- The weekly check-in can be shortened to 15 min or canceled if the async update is clean and no decisions are needed.

**Cadence adjustments:**
- Weeks 1-2 (discovery phase): consider 2x weekly check-ins if the PM is new to this type of initiative or if data validation surfaces unexpected issues.
- Weeks 4-5 (build + launch): add a brief pre-launch sync with Eng lead to confirm rollback readiness.

---

## Step 7 -- Review Plan

**What the manager reviews (artifacts):**

| Artifact | When | What to look for |
|---|---|---|
| Diagnostic memo | End of Week 2 | Data quality, root-cause depth (not just symptoms), segment analysis, clear "so what" |
| Experiment plan | End of Week 3 | Hypothesis rigor, expected impact sizing, effort realism, success criteria specificity, rollback plans |
| Launch checklist | Week 5 | Monitoring in place, rollback plan tested, success criteria dashboard live |
| Final learning memo | End of Week 6 | Honest results assessment, actionable learnings, clear next steps |

**How the manager reviews (criteria-based):**
- Compare each artifact against the quality criteria defined in Step 4.
- Frame feedback as: "This doesn't meet the quality bar because [specific criterion]. Here's the gap: [what's missing]. How would you close it?"
- If the artifact meets the bar, say so explicitly and move on. Do not add polish for polish's sake.
- When multiple valid approaches exist, ask "what are the tradeoffs?" rather than picking the one you would have chosen.

**What the manager will NOT do:**
- Dictate the research methodology, experiment design, or implementation approach when multiple valid options exist.
- Override decisions that are inside the PM's guardrails without new constraints or evidence.
- Rewrite the PM's artifacts; instead, provide criteria-based feedback and let the PM revise.
- Request task-level status updates ("did you send that email?"); focus on outcomes, risks, and decisions.
- Rescue the PM from productive struggle -- if they are wrestling with the right problem (e.g., which experiment to prioritize), let them work through it.

---

## Step 8 -- Debrief Plan

**Debrief meeting:** Scheduled for Week 6, Day 5 (or the first available slot after the final memo is delivered). 45-60 minutes.

**Debrief agenda:**

1. **What happened (PM presents, 10 min):** Summary of what was delivered, key results, and how they compare to the original outcome/acceptance criteria.

2. **What worked (joint discussion, 10 min):**
   - Which parts of the delegation setup (brief, guardrails, cadence) were most helpful?
   - Where did the PM feel most empowered?
   - What decisions did the PM make well independently?

3. **What didn't work (joint discussion, 10 min):**
   - Where did ambiguity cause friction or rework?
   - Were any guardrails too tight or too loose?
   - Were any escalation triggers missing?
   - Did any "snap-back" moments occur (manager unconsciously taking back control)?

4. **What we learned / will change next time (joint, 10 min):**
   - What assumptions were wrong?
   - What should we add to the delegation template for next time?
   - What guardrails or escalation triggers should be adjusted?

5. **Ownership updates (5 min):**
   - Who owns onboarding activation going forward? (Default: the PM retains ownership for the next cycle.)
   - What ongoing responsibilities transfer with this ownership? (Monitoring experiment results, iterating on findings, presenting to leadership.)
   - Is the ownership durable, or does it snap back to the manager? (Must be explicitly durable.)

6. **Next steps (5 min):**
   - File the learning memo in the team knowledge base.
   - Update the delegation template with any improvements.
   - Identify the next delegation candidate (another project or another team member to develop).

**Debrief Note (template, to be filled at the meeting):**

**What happened:** [PM fills in 1 paragraph summary of results vs. goals]

**What worked:** [Bullets from discussion]

**What didn't:** [Bullets from discussion]

**What we learned / will change next time:** [Bullets -- at least one template/guardrail improvement]

**Ownership updates ("who owns what now"):** [PM Name] retains ownership of onboarding activation for Q[X+1], including: monitoring experiment results, iterating on findings, presenting quarterly update to Growth lead and VP Product.

**Next steps:** [Bullets]

---

## Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Funnel data is unreliable (bot traffic, missing events) | Medium | High -- diagnostic memo built on bad data | Week 1: validate data sources before analysis; add instrumentation if needed |
| Eng capacity conflict in Weeks 4-5 (platform release) | Medium | Medium -- experiment launch delayed | Book eng time early; have a backup experiment that requires minimal eng effort |
| "Aha moment" definition is wrong | Low-Medium | High -- optimizing the wrong metric | Re-validate activation proxy in Week 1 diagnostic; escalate if evidence suggests redefinition needed |
| Design capacity shared with Retention squad | Medium | Low-Medium -- design assets delayed | Book design time in Week 1; have a "design-light" experiment option ready |
| PM is new to this level of autonomy and struggles with ambiguity | Low | Medium -- slower progress, need more coaching | Increase check-in frequency in Weeks 1-2; use thought-partner questions rather than giving answers |
| Stakeholder misalignment surfaces mid-project | Low | Medium -- scope creep or rework | Share delegation brief with all stakeholders in Week 1; flag disagreements early |

### Open Questions

1. What is the exact current activation rate, and has it been validated recently? (PM to answer in Week 1)
2. Is the current "aha moment" proxy metric still the right one, or does it need re-validation? (PM to assess in diagnostic)
3. What is the Eng team's actual capacity in Weeks 4-5 given the platform release? (PM to confirm with Eng lead in Week 1)
4. Are there any upcoming product changes (from other teams) that could affect the onboarding flow? (PM to check in Week 1)
5. Does the PM have experience running A/B experiments end-to-end, or is coaching needed on experiment design? (Manager to assess in kickoff)

### Next Steps

1. **Manager:** Share this Delegation Pack with the PM. Schedule a 60-minute kickoff meeting for Day 1.
2. **Manager:** Send the Context Handoff Pack (Step 3) with all relevant links and docs before the kickoff.
3. **PM (at kickoff):** Restate the problem, outcome, and constraints in their own words. Confirm understanding of decision rights and escalation triggers.
4. **PM (Week 1):** Propose a refined plan and first-week priorities. Share the first async update by mid-Week 1.
5. **Manager:** Set up the recurring weekly check-in calendar invite and the Slack channel/thread for async updates.
6. **Manager:** Brief stakeholders (Growth lead, Eng lead, Design lead) on the delegation and the PM's ownership.

---

## Quality Gate -- Self-Assessment

### Checklist A: Delegation Pack quality (pre-flight)

- [x] Outcome/definition of done is explicit and testable.
- [x] "Why now" context is included (so the owner can make tradeoffs).
- [x] Non-negotiables are listed (timeline, quality, policy/security, customer impact).
- [x] Autonomy level is explicit (decide with guardrails).
- [x] Decision rights are clear (owner decisions vs manager decisions).
- [x] Escalation triggers are specific thresholds (not vibes).
- [x] Context handoff includes prior decisions + rationale + known pitfalls.
- [x] Cadence focuses on outcomes/risks/decisions (not task micromanagement).
- [x] Review points are artifact-based and scheduled.
- [x] Risks / Open questions / Next steps are included.

### Checklist B: "Context, not control" (anti-micromanagement)

- [x] Communicated the why, constraints, and success criteria -- not a task list.
- [x] Asks for options/tradeoffs before giving an answer.
- [x] Feedback is framed as criterion/constraint, not "do it my way."
- [x] Owner is expected to struggle with the right problems without being rescued.

### Rubric Score

| Dimension | Score | Rationale |
|---|---|---|
| 1. Outcome clarity | 2 | Outcome + acceptance criteria are explicit and testable (diagnostic memo, experiment plan, launched experiment, learning memo -- each with clear acceptance criteria). |
| 2. Context transfer | 2 | Full context pack with background, prior decisions (Q3 retro, aha moment definition), known pitfalls, stakeholder map, and example outputs. |
| 3. Decision rights + guardrails | 2 | Explicit autonomy level per decision area, specific escalation triggers (scope changes, timeline > 1 week, auth/privacy, spend > $500), scheduled review points. |
| 4. Empowerment vs micromanagement | 2 | Criteria-based review; manager reviews artifacts against quality bar; explicit "will NOT do" list; "refuse to rule" principle; owner-led planning. |
| 5. Operating cadence | 2 | Weekly sync + mid-week async; outcome/decision/risk oriented; defined update format; cadence adjustment guidance. |
| 6. Closure + learning | 2 | Debrief meeting planned with structured agenda; ownership explicitly made durable; template improvement captured. |
| **Total** | **12 / 12** | **Ship as-is.** |
