# PM Coaching Pack — Growth Team PM: From Shipping to Choosing Better Bets

---

## Context Snapshot

| Dimension | Detail |
|---|---|
| **Coach role** | PM Manager / Product Lead (Growth) |
| **Product / team** | Growth team; consumer or SaaS growth loop (acquisition, activation, retention) |
| **Stage** | Growth-stage product with weekly release cadence |
| **PM level** | Mid-level PM (assumed IC3/IC4 equivalent; owns a surface area with moderate autonomy) |
| **Tenure** | Established on the team (ships reliably, knows the codebase and release process) |
| **Strengths** | Execution & delivery — ships on time, manages releases consistently, dependable |
| **Challenges** | Struggles to frame the right problems; does not make crisp tradeoffs; defaults to building the next obvious thing rather than asking "why this, why now?" |
| **Coaching goal** | In 8 weeks, the PM consistently frames problems with evidence, articulates explicit tradeoffs in decisions, and independently selects higher-leverage bets for the growth team |
| **Coaching type** | Development coaching (NOT performance management / PIP) |

**Assumptions (to validate with coach):**
- No formal PM ladder exists; we will define "good PM" for this role below.
- The PM has decision rights over weekly experiment/feature scope but not quarterly strategy.
- Peer/eng feedback themes: "great at getting things done, but we're not sure we're building the right things."
- No authority or mandate gaps blocking the PM; this is a skill gap, not a constraint gap.

---

## 1) Definition of "Good PM" (Growth Team, Mid-Level)

**PM role context:**
- Team/product: Growth team (funnel optimization, activation, retention loops)
- Stage: Growth (iterating on existing product with weekly releases)
- Scope + decision rights: Owns weekly release scope, experiment design, and feature specs within a quarterly theme set by leadership. Proposes but does not unilaterally set quarterly bets.

### Competency Model

| Competency | What "good" looks like (observable behaviors) | Bloom Depth Ladder |
|---|---|---|
| **Problem framing & insight** | Identifies the highest-leverage funnel drop-off or user pain point using data + qualitative evidence. Writes a 1-page opportunity assessment with segments, root causes, and sizing before proposing solutions. Distinguishes symptoms from causes. | **Knowledge:** Can name common growth frameworks (pirate metrics, JTBD). **Comprehension:** Can explain why a metric moved. **Application:** Can write an opportunity assessment with data for a known problem. **Analysis:** Can break down a funnel stage into competing root causes and recommend which to pursue with explicit tradeoffs. **Synthesis:** Can create a novel growth thesis connecting multiple signals. **Evaluation:** Can judge competing opportunity assessments and teach the framework. |
| **Strategy & prioritization** | Produces a decision brief for every significant prioritization call. Articulates 2-3 options with tradeoffs, rejected alternatives, and a clear recommendation tied to the quarterly goal. Says "no" with rationale. | **Knowledge:** Can list prioritization frameworks (RICE, ICE, cost of delay). **Comprehension:** Can explain why one bet was chosen over another. **Application:** Can score items using a framework with support. **Analysis:** Can compare options across multiple dimensions and surface hidden tradeoffs. **Synthesis:** Can build a sequenced roadmap slice with rationale under constraints. **Evaluation:** Can judge and defend a prioritization decision to leadership with evidence. |
| **Execution & delivery** | Ships weekly with quality; manages scope, risk, and stakeholder expectations. Runs experiments with clear hypotheses and success criteria. | **Knowledge:** Can describe the team's release process. **Comprehension:** Can explain scope/timeline tradeoffs. **Application:** Can run the release process end-to-end. **Analysis:** Can diagnose execution risks and proactively mitigate. **Synthesis:** Can redesign the release process for a new context. **Evaluation:** Can judge whether an experiment result is valid and recommend next steps. |
| **Stakeholder leadership** | Communicates decisions proactively with rationale. Seeks input early, not after the fact. Manages up clearly (status, asks, risks). | **Knowledge:** Can identify key stakeholders. **Comprehension:** Can explain stakeholder incentives. **Application:** Can write a status update with asks. **Analysis:** Can map stakeholder conflicts and propose alignment plans. **Synthesis:** Can design a communication strategy for a complex initiative. **Evaluation:** Can judge communication effectiveness and coach others. |
| **Product craft (docs, UX, edge cases)** | Writes clear specs with success criteria, edge cases, and acceptance criteria. Reviews designs with user-centric judgment. | (Not a primary coaching focus this cycle; preserve current level.) |
| **Business acumen (metrics, GTM, economics)** | Understands unit economics of the growth loop; can explain how a feature change affects CAC, LTV, or activation rate. | (Not a primary coaching focus this cycle; preserve current level.) |

---

## 2) Current Assessment (Evidence-Based)

**PM:** [Name redacted] — Mid-level PM, Growth Team
**Timeframe assessed:** Last 4-6 weeks of shipped work
**Evidence sources:**
- Recent PRDs / feature specs (weekly releases)
- Peer and engineering feedback summaries
- Roadmap / backlog prioritization artifacts
- Sprint retrospectives and launch postmortems

### Assessment Table

| Competency | Current Bloom Level | Target Bloom Level | Evidence (2-3 bullets) | Gap Type | Coaching Priority |
|---|---|---|---|---|---|
| **Problem framing & insight** | Application | Analysis | - PRDs start with a solution, not a problem statement; "why this problem" section is thin or absent. - When asked "why this drop-off matters more than others," PM defers to intuition or what's next on the backlog. - Can pull data and describe what happened, but does not break down competing root causes. | Skill gap | **H** |
| **Strategy & prioritization** | Application | Analysis | - Prioritization is implicit; no written decision brief or rejected-alternatives log. - When challenged on tradeoffs, PM struggles to articulate what was considered and why alternatives were rejected. - Defaults to the "most obvious next thing" rather than the highest-leverage bet. | Skill gap | **H** |
| **Execution & delivery** | Analysis | Analysis (maintain) | - Ships weekly, reliably. Manages scope and risk well. - Runs experiments with hypotheses and success criteria. - Occasionally over-scopes when problem framing is weak (builds more than needed because the problem wasn't narrowed). | N/A (strength) | L |
| **Stakeholder leadership** | Application | Application (maintain) | - Communicates status clearly. Manages up on timelines. - Does not yet proactively frame decisions for stakeholders with tradeoffs — this will improve as a second-order effect of the primary bets. | Minor skill gap (will improve via primary bets) | M |
| **Product craft** | Application | Application (maintain) | - Specs are clear and complete. Edge cases are covered. - Quality bar is solid for weekly releases. | N/A (strength) | L |
| **Business acumen** | Comprehension | Application | - Understands growth metrics at a high level. - Does not yet connect feature bets to unit economics in opportunity assessments. | Skill gap (secondary) | M |

### Strengths to Compound
1. **Execution & delivery** — Reliable weekly shipping is a rare and valuable asset. Use it as the vehicle for practicing new skills (each release becomes a coaching rep).
2. **Product craft** — Clean specs and attention to edge cases. Build on this by adding "problem framing" and "tradeoff" sections to existing spec templates.
3. **Dependability and trust** — The team trusts this PM to deliver. This trust creates room to experiment with new approaches without risking team confidence.

### Constraints to Remove (if any)
- **Assumption:** No authority, mandate, or data access constraints are blocking this PM. If quarterly goals are unclear or shifting, that is a leadership input problem to address separately.
- **Open question:** Does the PM have access to analytics / data tooling to do self-serve funnel analysis? If not, this is a constraint, not a skill gap.

---

## 3) Shared Vision — Growth Bets

| Growth Bet | Why It Matters (Business + PM) | Target Behavior / Artifact | Success Signals | Timeframe |
|---|---|---|---|---|
| **1. Problem framing & insight** (Application --> Analysis) | The growth team's impact is capped by picking the right problems. Better framing means higher-leverage experiments and less wasted build time. For the PM, this is the bridge from "reliable shipper" to "strategic contributor." | Produces a 1-page opportunity assessment for every significant initiative: problem statement, evidence, segments, root causes, sizing, and recommendation. | - 3 out of 4 weekly opportunity assessments include explicit competing root causes and a defended recommendation. - Eng lead confirms: "We understand why we're building this." - At least one initiative is killed or re-scoped based on the assessment (evidence of "no" decisions). | Weeks 1-8 |
| **2. Strategy & prioritization** (Application --> Analysis) | Crisp tradeoffs prevent scope creep and wasted cycles. The team needs a PM who can say "we're doing X because Y, and we're not doing Z because W." For the PM, this builds the muscle for roadmap ownership. | Produces a decision brief for every significant prioritization call: 2-3 options, tradeoffs, rejected alternatives, recommendation with rationale. | - Decision briefs are used in at least 2 planning conversations per month. - Stakeholders report: "I understand the tradeoffs and why we chose this path." - PM can articulate rejected alternatives without prompting. | Weeks 2-8 |

**Why these 2 bets (and not more):**
- Problem framing and prioritization are deeply connected — better problem framing feeds better prioritization. Coaching both simultaneously creates a reinforcing loop.
- These are the highest-leverage gaps: they affect everything downstream (what gets built, how scope is managed, what gets communicated to stakeholders).
- Limiting to 2 bets keeps focus tight on a weekly release cadence where coaching time is constrained.

---

## 4) Development Plan

### Growth Bet 1: Problem Framing & Insight

**Hypothesis:** If the PM practices writing structured opportunity assessments with explicit root cause analysis and tradeoffs, then the quality of problems the team works on will improve because the PM will develop the habit of asking "why this problem" before "what should we build."

**Current --> Target Bloom level:** Application --> Analysis

#### Weekly Reps (30-60 min each)

- **Rep #1 — Opportunity Assessment (weekly):** For the top candidate initiative each week, write a 1-page opportunity assessment before writing a spec. Structure: (a) Problem statement in one sentence, (b) Evidence (quantitative + qualitative), (c) Affected segments, (d) 2-3 competing root causes, (e) Sizing / impact estimate, (f) Recommendation with rationale. Submit to coach 24 hours before 1:1 for async review.

- **Rep #2 — "Kill or Continue" Review (biweekly, starting week 3):** Review a recently shipped feature or experiment. Write a half-page retrospective: (a) What problem were we solving? (b) Did the evidence support the root cause we targeted? (c) What would we do differently? (d) Should we double down, iterate, or move on? This rep develops the habit of evaluating problem framing quality retroactively.

#### Stretch Assignment (Real Work)

- **Own an 8-week growth initiative end-to-end with a clear hypothesis.** The PM selects or is assigned a funnel stage (e.g., activation drop-off between signup and first value moment). They own the full arc: opportunity assessment --> hypothesis --> experiment design --> weekly decision briefs --> mid-point tradeoff review (week 4) --> final retrospective (week 8). This is real work with real stakes, not a simulation.

#### Required Artifacts (What They Produce)

- 6-8 opportunity assessments (one per week)
- 3-4 "kill or continue" retrospectives (biweekly from week 3)
- 1 mid-point tradeoff review (week 4)
- 1 final initiative retrospective (week 8)

#### Coach Commitments (What You Will Do)

- **Review cadence:** Written feedback on each opportunity assessment within 24 hours (async). Focus feedback on: Is the problem clearly stated? Are root causes competing or just listed? Is the recommendation defended?
- **Shadow/observe:** Sit in on 1 planning meeting per week (weeks 1-4) to observe how the PM frames problems live. Debrief in 1:1.
- **Introductions/unblocking:** Connect PM with data/analytics support if self-serve analysis is a gap. Share 2-3 exemplar opportunity assessments from the org or industry.

#### Measurement (How We'll Know)

- **Rubric dimensions:** Opportunity assessments are scored on: (1) problem clarity, (2) evidence quality, (3) root cause depth, (4) recommendation defensibility. Use a simple 0-1-2 scale per dimension.
- **Evidence to collect:** Artifacts (opportunity assessments, retrospectives); peer feedback at week 4 and week 8 ("Do you understand why we're building what we're building?"); initiative outcomes.

#### Timeline + Checkpoints

- **Week 1:** First opportunity assessment. Coach provides detailed written feedback + modeling in 1:1.
- **Week 2:** Second assessment. Coach feedback focuses on root cause depth. Introduce "competing hypotheses" frame.
- **Week 4:** Mid-point review. PM presents the stretch initiative tradeoff review to coach (and optionally to the team). Assess: Are assessments improving? Adjust reps if needed.
- **Week 8:** Final retrospective on stretch initiative. Score all artifacts against rubric. Decide: continue bet, shift focus, or graduate.

---

### Growth Bet 2: Strategy & Prioritization

**Hypothesis:** If the PM practices writing decision briefs with explicit options, tradeoffs, and rejected alternatives, then prioritization quality will improve because the PM will develop the habit of making tradeoffs visible and defensible rather than implicit.

**Current --> Target Bloom level:** Application --> Analysis

#### Weekly Reps (30-60 min each)

- **Rep #1 — Decision Brief (weekly, starting week 2):** For every significant scope or prioritization decision, write a 1-page decision brief before the decision is made. Structure: (a) Decision to make (one sentence), (b) Context and constraints, (c) 2-3 options with tradeoffs, (d) Rejected alternatives and why, (e) Recommendation with rationale tied to the quarterly goal. Submit to coach before the planning conversation.

- **Rep #2 — "Tradeoff Log" Entry (weekly):** Maintain a running log of tradeoffs made each week. For each entry: what was traded off, what was gained, what was the rationale. Review the log in 1:1 every 2 weeks to spot patterns (e.g., always trading off long-term for short-term, or always avoiding a particular tradeoff).

#### Stretch Assignment (Real Work)

- **Integrated with Bet 1's stretch initiative.** The PM uses decision briefs as the primary decision-making tool for their 8-week initiative. At the mid-point (week 4), the PM presents a tradeoff review: what was prioritized, what was deprioritized, what changed, and why. This forces the prioritization muscle in a real, high-stakes context.

#### Required Artifacts (What They Produce)

- 5-6 decision briefs (weekly from week 2)
- 1 running tradeoff log (updated weekly)
- 1 mid-point tradeoff review presentation (week 4, combined with Bet 1)

#### Coach Commitments (What You Will Do)

- **Review cadence:** Written feedback on each decision brief within 24 hours. Focus feedback on: Are options genuinely different? Are tradeoffs explicit? Is the recommendation tied to a goal or just a preference?
- **Shadow/observe:** Observe 1 prioritization conversation per week (weeks 2-4) to see how the PM uses the brief in practice. Debrief: Did the brief change the conversation?
- **Introductions/unblocking:** Share the team's quarterly goals in writing (if not already documented) so the PM can anchor recommendations.

#### Measurement (How We'll Know)

- **Rubric dimensions:** Decision briefs scored on: (1) option quality (genuinely different choices), (2) tradeoff explicitness, (3) recommendation defensibility, (4) connection to quarterly goal. 0-1-2 scale.
- **Evidence to collect:** Artifacts (decision briefs, tradeoff log); stakeholder feedback at week 4 and week 8 ("Do you understand why we chose this over that?"); count of decisions where alternatives were explicitly rejected.

#### Timeline + Checkpoints

- **Week 2:** First decision brief. Coach provides detailed written feedback + models a "good" decision brief in 1:1.
- **Week 3:** Second brief. Focus feedback on tradeoff depth.
- **Week 4:** Mid-point tradeoff review (combined with Bet 1). Assess brief quality trend. Adjust if needed.
- **Week 8:** Final review. Score all briefs against rubric. Review tradeoff log for patterns. Decide: continue bet, shift focus, or graduate.

---

## 5) Coaching Cadence + Session Toolkit

**Cadence:** Weekly 1:1 (45 min) + async artifact reviews (24-hour turnaround)
**Format:** 1:1 (in-person or video) + shared doc for artifact submissions and feedback

### Default 1:1 Agenda

| Block | Time | What happens |
|---|---|---|
| 1. Wins + energy check | 5 min | What went well this week? How are you feeling about the work? (Build trust; surface blockers early.) |
| 2. Artifact review deep-dive | 20 min | Review this week's opportunity assessment or decision brief together. Coach asks questions; PM defends and iterates. Focus on ONE artifact per session (depth over breadth). |
| 3. Live coaching on a current decision | 10 min | PM brings one real decision or problem they're facing. Coach uses coaching prompts (below) to develop the PM's reasoning — does NOT give the answer. |
| 4. Tradeoff log review (biweekly) | 5 min | Every other week: review the tradeoff log. Spot patterns. Discuss: "What tradeoff are you avoiding?" |
| 5. Next reps + commitments | 5 min | Confirm next week's reps, artifact deadlines, and any shadow/observe sessions. Both sides state commitments. |

### Coaching Prompts (Use in Blocks 2 and 3)

1. "What problem are we solving, and for whom? What's the evidence that this is the right problem?"
2. "What options did you consider? What did you reject, and why?"
3. "What's the strongest argument against your recommendation?"
4. "If this fails, why will it fail? What's the riskiest assumption?"
5. "What would you do if you had half the time? What would you cut?"
6. "How does this connect to our quarterly goal? If it doesn't, why are we doing it?"
7. "What would you need to see in the data to change your mind?"

**Coaching stance:** Default to questions. Let the PM arrive at the answer. Provide your own view only after the PM has articulated theirs. Frame feedback as criteria-based ("The opportunity assessment is missing competing root causes, which means we can't evaluate whether we're targeting the right cause") rather than opinion-based ("I think you should do X").

### Artifact Review Points (Scheduled)

| Week | Artifact | Review format |
|---|---|---|
| 1 | Opportunity assessment #1 | Deep-dive in 1:1 + written feedback |
| 2 | Opportunity assessment #2 + Decision brief #1 | Async written feedback + 1:1 discussion |
| 3 | Opportunity assessment #3 + Decision brief #2 + Kill-or-continue #1 | 1:1 deep-dive on one artifact; async on the rest |
| 4 | **Mid-point tradeoff review** | Dedicated 1:1 (or small group presentation); formal assessment checkpoint |
| 5-7 | Weekly artifacts | Async feedback + 1:1 coaching as needed |
| 8 | **Final retrospective + all artifacts** | Formal review session; updated assessment; decide next cycle |

### When to Be Directive (Exceptions)

- **Safety / compliance risk:** If a decision could cause user harm, data loss, or compliance violation, give the answer directly. Debrief afterward.
- **Major customer impact:** If a shipping decision will negatively affect a large customer segment and the PM hasn't identified the risk, intervene.
- **Time-critical decisions:** If the weekly release deadline requires an immediate call and there's no time for coaching, make the call together and use it as a teaching moment in the next 1:1.
- **Repeated blind spots:** If the same gap appears in 3+ consecutive artifacts after feedback, shift from coaching to structured modeling — walk through your thinking process explicitly, then have the PM replicate it.

---

## 6) Follow-up Tracker + Review Plan

### Progress Tracker

| Week | Growth Bet | Rep / Artifact Completed | Coach Feedback (1-3 bullets) | Next Rep | Progress |
|---|---|---|---|---|---|
| 1 | Problem framing | Opportunity assessment #1 | (To be filled after review) | OA #2; begin stretch initiative scoping | -- |
| 2 | Problem framing + Prioritization | OA #2 + Decision brief #1 | | OA #3 + DB #2 | -- |
| 3 | Problem framing + Prioritization | OA #3 + DB #2 + Kill-or-continue #1 | | OA #4 + DB #3 | -- |
| 4 | **Both (mid-point)** | **Mid-point tradeoff review** + OA #4 + DB #3 | **Formal checkpoint: score artifacts, assess Bloom progression, adjust plan if needed** | OA #5 + DB #4 + K/C #2 | -- |
| 5 | Problem framing + Prioritization | OA #5 + DB #4 + K/C #2 | | OA #6 + DB #5 | -- |
| 6 | Problem framing + Prioritization | OA #6 + DB #5 + K/C #3 | | OA #7 + DB #6 | -- |
| 7 | Problem framing + Prioritization | OA #7 + DB #6 + Tradeoff log review | | OA #8 + final retro prep | -- |
| 8 | **Both (final)** | **Final retrospective + all artifacts** | **Formal review: score all artifacts, updated assessment, decide next cycle** | (Next cycle planning) | -- |

### Review Checkpoints

**Week 4 — Mid-point Review:**
- Score all opportunity assessments and decision briefs against rubric (0-1-2 per dimension).
- Compare week 1 artifacts to week 4 artifacts: is there visible progression?
- Collect peer feedback: "Do you understand why we're building what we're building?"
- Decision: Keep both bets? Adjust intensity? Add/remove a rep? Address a constraint?

**Week 8 — Final Review:**
- Score all artifacts against rubric. Calculate trend (are scores improving?).
- Collect peer and eng feedback again. Compare to week 4.
- Updated assessment: re-map the PM against the competency model. Has Bloom level shifted?
- Decision: Graduate both bets (move to maintenance)? Continue one bet for another cycle? Introduce a new bet?

### How to Adjust the Plan

| Signal | Action |
|---|---|
| Artifacts improving steadily; PM is self-correcting | Reduce coach review intensity; increase PM autonomy (review every other artifact instead of every one) |
| Artifacts plateau after week 3-4 | Diagnose: Is this a skill ceiling or a constraint? If skill, introduce modeling (coach writes an exemplar, PM compares). If constraint, remove it. |
| PM is overwhelmed (energy check signals burnout) | Drop one rep (keep the higher-leverage one). Reduce artifact requirements. Re-scope stretch assignment. |
| External disruption (reorg, goal change, fire drill) | Pause non-essential reps. Keep the stretch initiative if possible (it provides the most learning). Resume after disruption clears. |
| PM is ahead of plan (artifacts are consistently strong by week 4) | Graduate early. Introduce a new bet (e.g., stakeholder leadership or business acumen) or increase the Bloom target (Analysis --> Synthesis). |

---

## 7) Risks / Open Questions / Next Steps

### Risks

1. **Coaching time competes with delivery pressure.** Weekly releases create constant urgency. Risk: the PM (or coach) skips artifact creation or 1:1 deep-dives because "there's a release to ship." Mitigation: Embed reps into existing workflow (opportunity assessments replace the "why are we building this" section of existing specs; decision briefs replace ad hoc Slack prioritization discussions).

2. **Artifacts become checkbox exercises.** Risk: the PM writes assessments and briefs to satisfy the coach, not to improve thinking. Mitigation: Coach evaluates whether artifacts actually changed decisions (not just whether they were produced). Ask: "Did this brief change anything? If not, why did you write it?"

3. **Coach defaults to telling, not coaching.** Under time pressure, the coach gives answers instead of asking questions. Mitigation: The coaching prompts list is a forcing function. In each 1:1, the coach tracks how many times they gave a directive answer vs. asked a question. Target: 80% questions in blocks 2-3.

4. **Peer feedback is unavailable or vague.** If eng/design peers can't articulate whether problem framing has improved, the measurement signal is weak. Mitigation: Use specific questions ("In the last 2 weeks, did you understand why we were building what we were building? Can you give an example?") rather than open-ended "how's the PM doing?"

### Open Questions

1. Does the PM have self-serve access to analytics / data tooling for funnel analysis? If not, this is a constraint to remove before Bet 1 can succeed.
2. Are the quarterly goals clearly documented and accessible? If the PM can't anchor decision briefs to a goal, Bet 2 is harder.
3. What is the PM's own aspiration? Do they want to grow toward senior PM / strategy roles, or is reliable execution their preferred mode? This affects motivation and bet selection.
4. Is there an existing spec or PRD template on the team? If so, can we modify it to include "problem framing" and "tradeoff" sections (lowering friction for reps)?
5. Does the coach have 45 min/week for the 1:1 plus 15-20 min/week for async artifact review? If not, cadence needs adjustment.

### Next Steps (Next 1-2 Weeks)

1. **Validate this coaching pack with the PM.** Share the Definition of Good PM and Assessment with the PM. Get their input: Do they agree with the strengths and gaps? Do the growth bets feel right? This must be a shared vision, not a top-down mandate.
2. **Confirm logistics.** Lock the weekly 1:1 slot (45 min). Set up the shared doc for artifact submissions and feedback. Confirm data/analytics access.
3. **Start Bet 1 in week 1.** The PM writes their first opportunity assessment for the top initiative candidate. Coach provides detailed written feedback + 1:1 deep-dive.
4. **Start Bet 2 in week 2.** Introduce the decision brief rep once the opportunity assessment cadence is established.
5. **Scope the stretch initiative.** By end of week 1, coach and PM agree on the 8-week growth initiative the PM will own end-to-end.

---

## Quality Gate — Rubric Self-Score

| Dimension | Score | Rationale |
|---|---|---|
| 1. Definition clarity | **2** | Observable behaviors tied to role scope (Growth team, mid-level PM). Bloom depth ladder included for each competency. Context-specific, not generic. |
| 2. Evidence-based assessment | **2** | Evidence mapped to competencies with specific artifact references (PRDs, specs, planning conversations). Skill gaps separated from constraints. Uncertainty labeled (data access, quarterly goals). |
| 3. Growth bet selection | **2** | 2 high-leverage bets with clear success signals, timeframe (8 weeks), and rationale tied to business priorities (growth team impact) and PM development arc. |
| 4. Development plan specificity | **2** | Weekly reps + stretch assignment + required artifacts + measurable signals (rubric scoring) + explicit coach commitments (review cadence, shadowing, unblocking) + timeline with checkpoints. |
| 5. Coaching cadence & toolkit | **2** | Sustainable weekly cadence with async reviews. Coaching prompts that develop independent reasoning. Artifact review schedule. Explicit "when to be directive" exceptions. |
| 6. Follow-up & adaptation | **2** | Tracker with weekly entries. Week 4 and week 8 formal checkpoints. Explicit adjustment criteria (plateau, overwhelm, ahead of plan, disruption). |
| **Total** | **12 / 12** | Ship as-is. |

### Checklist Verification

**A) PM Coaching Pack quality checklist:**
- [x] Clear boundary: coaching vs HR/performance management
- [x] Defines "good PM" in-context with observable behaviors
- [x] Uses Bloom depth ladder for skill depth
- [x] Assessment is evidence-based; separates skill vs constraints
- [x] 1-3 growth bets with success signals and timeframe
- [x] Development plan contains weekly reps + stretch work + artifacts
- [x] Coaching cadence is sustainable with artifact review points
- [x] Follow-up tracker + review checkpoints included
- [x] Risks / Open questions / Next steps included

**B) Evidence quality checklist:**
- [x] Each gap claim has at least 1 concrete example
- [x] Evidence references decisions/artifacts, not personality judgments
- [x] Uncertainty is labeled

**C) Coaching (not rescuing) checklist:**
- [x] Plan is built around asking questions and reviewing artifacts, not giving answers
- [x] Feedback is criteria-based
- [x] Building independent reasoning, not dependency

**D) Follow-up checklist (to be used at monthly review):**
- [ ] Updated assessment using new evidence (week 4, week 8)
- [ ] Kept/changed growth bets based on constraints and results
- [ ] Celebrated visible progress and increased autonomy
