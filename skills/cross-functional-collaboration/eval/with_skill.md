# Cross-Functional Collaboration Pack: Onboarding Revamp Initiative

**Prepared by:** Product Lead (DRI)
**Date:** 2026-03-17
**Version:** 1.0

---

## 1) Mission Charter

**Initiative:** Onboarding Revamp
**Why now (context):** Current onboarding flow has high drop-off, low activation rates, and inconsistent experiences across user segments. New competitors are shipping significantly better first-run experiences. We have a window to ship a revamped onboarding before the Q3 growth push.
**Timeframe:** 10 weeks (Week 1: Mar 17 -> Week 10: May 26, 2026)
**Collaboration mode:** Project team (finite, time-boxed)

**Mission (1-2 sentences):**
Redesign the end-to-end onboarding experience to increase new-user activation rate from 32% to 50%+ within the first 7 days, while reducing time-to-first-value from 4.2 days to under 2 days, across all primary user segments.

**Success metrics (top 3):**
- 7-day activation rate: 32% -> 50%+ (primary)
- Time-to-first-value: 4.2 days -> < 2 days (primary)
- Onboarding completion rate: 58% -> 75%+ (secondary)

**In-scope:**
- Full onboarding flow redesign (signup -> first value moment)
- Segmented onboarding paths (by persona / use case)
- In-app guidance, tooltips, and progressive disclosure
- Onboarding email/notification sequences (Marketing collaboration)
- Instrumentation and analytics for measuring activation funnel
- A/B testing infrastructure for rollout

**Out-of-scope:**
- Pricing or plan changes
- Core product feature development (beyond what onboarding exposes)
- Full redesign of post-onboarding retention flows (separate initiative)
- Internationalization / localization (follow-on)
- Changes to the signup page itself (owned by Growth team separately)

**Non-negotiables (guardrails):**
- **Timeline/deadlines:** Must ship initial rollout by Week 10 (May 26). Beta/internal dogfood by Week 7.
- **Quality bar:** No regression in existing activation for current user segments. Accessibility standards (WCAG 2.1 AA) must be met.
- **Policy/compliance/security:** GDPR-compliant data collection in onboarding forms. No PII in analytics events without consent.
- **Customer commitments:** Enterprise customers on custom onboarding flows must not be disrupted; their flows will be addressed in a follow-on phase.
- **Budget/headcount:** No new headcount; must ship with existing team allocation (partial allocation from each function).

**Key milestones (high level):**

| Week | Milestone |
|------|-----------|
| 1-2 | Discovery complete: user research synthesis, funnel analysis, segment definitions |
| 3 | Design concepts (2-3 directions) reviewed cross-functionally |
| 4 | Chosen direction locked; prototype built |
| 5-6 | Engineering build (Phase 1: core flow) |
| 7 | Internal dogfood / beta release |
| 8-9 | A/B test live; iterate on results |
| 10 | Full rollout decision + launch |

**Risks (early):**
- Partial allocation across all functions means competing priorities could cause delays.
- Eng capacity may be constrained by ongoing tech debt work mid-sprint.
- Segment definitions may require more research than 2 weeks allow.
- Marketing email sequences depend on a shared ESP (email service provider) with another team.
- Data instrumentation may surface gaps in current event tracking that take time to fix.

---

## 2) Stakeholder & Incentives Map

| Stakeholder | Function | Role | Optimizes for | Concerns / Risks | What they need | Comms |
|---|---|---|---|---|---|---|
| Product Lead (you) | Product | DRI | Activation metrics; shipping on time; cross-functional alignment | Scope creep; teams getting pulled to other priorities | Clear decisions; partner accountability; exec air cover | All channels; drives sync |
| Eng Lead | Engineering | Co-owner (build) | Technical quality; manageable scope; no last-minute changes | Unclear specs leading to rework; unrealistic timelines | Locked specs by Week 4; clear priority vs. tech debt | Slack #onboarding-revamp; weekly sync |
| Design Lead | Design | Co-owner (UX) | User experience quality; research-backed decisions; design craft | Being handed solutions instead of problems; rushed research | Early involvement in discovery; time for user testing | Slack; Figma comments; weekly sync |
| Data Analyst | Data/Analytics | Contributor | Accurate measurement; clean instrumentation; statistical rigor | Being asked to "prove it worked" without proper instrumentation upfront | Instrumentation plan locked early; access to event schemas | Slack; async updates; weekly sync |
| Marketing Lead | Marketing | Contributor | Messaging coherence; email sequence performance; brand consistency | Late involvement; onboarding messaging conflicting with lifecycle campaigns | Messaging brief by Week 4; access to in-app copy decisions | Slack; biweekly touchpoint |
| VP Product | Product (exec) | Approver | Portfolio-level impact; resource allocation justified | Initiative under-delivers or delays other roadmap items | Biweekly async update; escalation path for resource conflicts |  Async written update biweekly |
| Head of Engineering | Engineering (exec) | Approver | Eng team utilization; technical architecture alignment | New tech debt introduced; scope expansion mid-build | Approval on technical approach (Week 3); escalation path | Async written update biweekly |
| CS/Support Lead | Customer Success | Informed + Contributor | Customer satisfaction; reduced support tickets on onboarding | Changes break existing enterprise flows; support not prepped for launch | Heads-up on UX changes 2 weeks before launch; FAQ doc | Email updates at milestones |
| QA Lead | Engineering (QA) | Contributor | Test coverage; regression-free launch | Compressed testing window | Test plan input by Week 5; stable build for testing by Week 7 | Slack; sync as needed |

**Missing seats (likely needed):**
- **Growth/Lifecycle team:** If they own the signup page or lifecycle emails, they need to be informed or consulted to avoid conflicting changes.
- **Legal/Privacy:** If onboarding collects new data fields or changes consent flows, a brief review is needed by Week 3.
- **Infra/Platform team:** If A/B testing infrastructure needs changes, their capacity should be checked by Week 2.

---

## 3) Roles & Expectations Contract

**Primary driver/DRI:** Product Lead
**Decision model:** DACI (Driver, Approver, Contributor, Informed)

### A) Expectations matrix

**PM expects Eng to:**
- Provide realistic effort estimates by Week 3 so scope can be locked early.
- Flag technical risks and constraints proactively (not at the last minute).
- Build to spec without re-negotiating UX decisions that were already decided cross-functionally.
- Participate in design reviews and speak up on feasibility before specs are locked.

**PM expects Design to:**
- Deliver research-backed concepts (not just aesthetic preferences) by Week 3.
- Provide specs at sufficient fidelity for Eng (no "figure it out" handoffs).
- Be willing to simplify designs when Eng raises genuine feasibility concerns.
- Participate actively in prototype testing (Week 4-5).

**PM expects Data to:**
- Define the instrumentation plan and event taxonomy by Week 3.
- Flag gaps in current tracking early so Eng can plan instrumentation work.
- Provide clear measurement criteria for A/B tests before they launch.
- Deliver activation metric dashboards by Week 7 (dogfood).

**PM expects Marketing to:**
- Align onboarding email copy with in-app messaging by Week 5.
- Flag conflicts with existing lifecycle campaigns early.
- Have email sequences ready for A/B test by Week 8.

**Eng expects PM to:**
- Lock scope by Week 4 and not introduce new features after that point without a formal tradeoff discussion.
- Prioritize ruthlessly when scope pressure arises (cut features, not quality).
- Shield the team from ad-hoc exec requests that aren't aligned with the charter.
- Provide clear acceptance criteria for every user story.

**Eng expects Design to:**
- Deliver final specs (not "WIP") before Eng sprint planning for each phase.
- Be available for quick clarifications during build (< 24h turnaround on Slack questions).
- Provide assets (icons, illustrations) in the agreed format and timeline.

**Design expects PM/Eng to:**
- Include Design in problem framing (not just solution execution).
- Respect research findings even when they challenge assumptions.
- Not ship visual changes without Design review.
- Give Design enough lead time (at least 1 week ahead of Eng build).

**Data/Analytics expects PM/Eng/Design to:**
- Include Data in defining success metrics and segment definitions upfront.
- Implement event tracking per the agreed instrumentation plan (no ad-hoc events).
- Allow sufficient A/B test duration for statistical significance (min 1 week per test).

**Marketing expects PM/Design to:**
- Provide a messaging brief and value props by Week 4.
- Share final in-app copy so email sequences can reinforce (not contradict) the in-app experience.
- Give 2 weeks notice before any launch date changes.

### B) Responsibility map (who owns what)

- **Product:** Overall initiative ownership; scope decisions; milestone tracking; stakeholder communication; rollout strategy.
- **Engineering:** Technical architecture; build execution; instrumentation implementation; A/B test infrastructure; QA coordination; performance/reliability.
- **Design:** User research; UX flows; visual design; prototypes; user testing; design QA.
- **Data/Analytics:** Instrumentation plan; event taxonomy; dashboards; A/B test analysis; activation metric reporting.
- **Marketing:** Onboarding email sequences; in-app messaging copy support; launch comms to existing users (if needed).
- **CS/Support:** Feedback on common onboarding pain points; FAQ and support doc updates pre-launch.

### C) Decision rights + escalation triggers

**Decisions this group can make (no escalation needed):**
- UX flow and interaction design choices (Design lead decides, with PM + Eng input)
- Technical implementation approach (Eng lead decides, with PM awareness)
- Instrumentation and event naming (Data lead decides, with Eng input)
- Email sequence structure and copy (Marketing lead decides, with PM input on messaging)
- A/B test variants and duration (PM decides, with Data input on statistical requirements)
- Scope tradeoffs within the approved feature set (PM decides, with Eng + Design input)

**Decisions that require escalation/approval:**
- Shipping without meeting the 50% activation target threshold (VP Product)
- Adding more than 1 week to the timeline (VP Product + Head of Eng)
- Changing the primary success metric definition (VP Product)
- Architectural decisions that affect other product areas (Head of Eng)
- Collecting new PII in onboarding forms (Legal/Privacy review)

**Escalation triggers (specific thresholds):**
- Any milestone slips by more than 3 business days -> PM escalates to VP Product + Head of Eng with options.
- A cross-functional disagreement is unresolved after 48 hours -> Escalate using the Conflict Protocol (Section 6).
- Eng estimates exceed 120% of planned capacity for any sprint -> PM + Eng Lead jointly escalate for scope or resource adjustment.
- A/B test results show activation regression (statistically significant) -> Halt rollout; PM + Data escalate to VP Product.

### D) Review cadence (how the contract stays alive)

- **Revisit cadence:** At Week 5 (mid-point) and Week 8 (pre-launch), plus any phase change.
- **Artifact used for review:** Decision log + retro notes from mid-point check-in.
- **Trigger for ad-hoc review:** Any escalation trigger is hit, or a function raises a concern about the working agreement.

---

## 4) Shared Artifacts & Source of Truth

### Artifact plan

| Artifact | Owner | Tool/Location | Purpose |
|---|---|---|---|
| Collaboration Pack (this doc) | Product Lead | Notion: /Onboarding-Revamp/Collaboration-Pack | Operating agreement and decision rights |
| PRD / Spec | Product Lead | Notion: /Onboarding-Revamp/PRD | Requirements, scope, acceptance criteria |
| Design Files | Design Lead | Figma: Onboarding Revamp project | Mockups, prototypes, design specs |
| Instrumentation Plan | Data Analyst | Notion: /Onboarding-Revamp/Instrumentation | Event taxonomy, tracking plan |
| Decision Log | Product Lead | Notion: /Onboarding-Revamp/Decision-Log | All cross-functional decisions + rationale |
| Sprint Board | Eng Lead | Jira/Linear: Onboarding Revamp board | Eng tasks, status, blockers |
| Activation Dashboard | Data Analyst | Looker/Amplitude: Onboarding Metrics | Live metrics, funnel, A/B results |
| Email Sequence Spec | Marketing Lead | Notion: /Onboarding-Revamp/Email-Sequences | Drip campaign copy, triggers, segmentation |
| Launch Checklist | Product Lead | Notion: /Onboarding-Revamp/Launch-Checklist | Pre-launch go/no-go items |

### Source of truth rules

- **Notion** is the single source of truth for all written decisions, specs, and plans.
- **Figma** is the source of truth for design (not screenshots in Slack).
- **Jira/Linear** is the source of truth for engineering task status.
- If Slack contradicts a Notion doc, the Notion doc wins. Update the doc if the Slack discussion changes a decision.

### Prototype / working-slice milestone

- **Week 4:** Clickable Figma prototype of the primary onboarding flow (happy path for top 2 segments). This prototype is the shared artifact that aligns PM, Eng, Design, and Data on the target experience before any code is written.
- **Week 7:** Internal dogfood build (working code, limited to team + internal users). This is the first "real" artifact that surfaces instrumentation gaps, edge cases, and performance issues.

---

## 5) Operating Cadence & Communication Plan

**Doc hub / source of truth:** Notion workspace -> /Onboarding-Revamp/
**Primary channels:**
- **Slack:** #onboarding-revamp (working channel); #onboarding-revamp-decisions (decisions only, low noise)
- **Figma comments:** Design feedback
- **Jira/Linear:** Eng task tracking
- **Email:** Exec/stakeholder updates only

### Meetings (minimal)

| Meeting | Frequency | Duration | Attendees | Focus |
|---|---|---|---|---|
| Cross-functional sync | Weekly (Tuesdays) | 45 min | PM, Eng Lead, Design Lead, Data Analyst, Marketing Lead | Decisions needed; blockers; risks; next-week priorities. NOT status (status is async). |
| Design review | Weekly (Thursdays, Weeks 2-6) | 30 min | PM, Eng Lead, Design Lead | Review design progress; flag feasibility; align on UX direction. |
| Working session | As needed | 60 min max | Varies (2-3 people) | Deep-dive on a specific problem (e.g., segmentation logic, instrumentation). Scheduled ad-hoc, not recurring. |
| Stakeholder update | Biweekly (Weeks 2, 4, 6, 8, 10) | Async (written) | VP Product, Head of Eng, CS Lead | Progress vs. outcome; decisions made; risks; asks. |

### Weekly sync agenda (standard)

1. **Decisions needed this week** (5 min) - review decision log; make or assign.
2. **Blockers and risks** (10 min) - each function names top blocker; assign owner + resolution date.
3. **Progress vs. milestones** (10 min) - are we on track? If not, what's the tradeoff proposal?
4. **Cross-functional handoffs this week** (10 min) - what's being handed off, to whom, in what state?
5. **Upcoming decisions** (5 min) - seed next week's decision log entries.
6. **Shout-outs** (5 min) - recognize a cross-functional contribution from the past week.

### Default async update format

Posted to Slack #onboarding-revamp every Friday by each function lead:
- **Progress vs. outcome:** Where we are against the current milestone.
- **Decisions made / needed:** Decisions finalized this week + decisions needed next week.
- **Risks + mitigations:** Top risk and what we're doing about it.
- **Asks / blockers:** What I need from another function.
- **Next milestone + ETA:** What's coming and whether it's on track.

### Decision logging protocol

- Every meaningful cross-functional decision gets logged in the Decision Log (Notion) within 24 hours.
- Each entry includes: decision, owner, date, options considered, criteria, rationale, and follow-ups.
- Decisions can only be re-opened with **new information or changed constraints** -- not because someone wasn't in the room.
- The #onboarding-revamp-decisions Slack channel is a mirror (post a one-liner + link to the log entry).

---

## 6) Decision Log (Initial)

| # | Decision | Owner | Due | Options | Criteria | Decision | Rationale | Follow-ups |
|---|---|---|---|---|---|---|---|---|
| D1 | Which user segments to prioritize for onboarding paths? | PM + Data | Week 2 | (a) Top 2 by volume, (b) Top 2 by revenue potential, (c) Highest-drop-off segments | Impact on activation metric; data availability; build complexity | PENDING | -- | Data to pull segment analysis by end of Week 1 |
| D2 | Onboarding UX direction: guided wizard vs. contextual tooltips vs. hybrid? | Design Lead (with PM + Eng input) | Week 3 | (a) Step-by-step wizard, (b) Contextual tooltips, (c) Hybrid approach | User research findings; Eng feasibility; time-to-first-value impact | PENDING | -- | Design to present 2-3 concepts at Week 3 design review |
| D3 | A/B test rollout strategy: % rollout vs. segment-based rollout? | PM (with Data + Eng input) | Week 7 | (a) 10% -> 50% -> 100% gradual rollout, (b) Rollout by segment, (c) Feature flag per-org | Statistical power requirements; risk tolerance; rollback ease | PENDING | -- | Data to model required sample sizes; Eng to confirm feature flag capability |
| D4 | Instrumentation approach: extend existing events or new event schema? | Data + Eng | Week 3 | (a) Extend current schema, (b) New dedicated onboarding event schema | Backward compatibility; analysis flexibility; Eng effort | PENDING | -- | Data to draft event taxonomy by Week 2; Eng to review |
| D5 | Email sequence trigger logic: time-based vs. behavior-based vs. hybrid? | Marketing + PM | Week 5 | (a) Time-based drip, (b) Behavior-triggered, (c) Hybrid | ESP capabilities; personalization impact on activation; build effort | PENDING | -- | Marketing to audit current ESP capabilities by Week 4 |

---

## 7) Collaboration Norms

### Conflict Protocol

Use this when cross-functional partners disagree and progress stalls.

**Step 1 -- Name the conflict (neutral language):**
State the tension explicitly: "We seem to be optimizing for X vs. Y."
Example: "Design is optimizing for a polished, research-validated flow, and Eng is optimizing for shipping within the 10-week window. Both are valid."

**Step 2 -- Validate both goals (Yes, and):**
Acknowledge both sides before proposing a resolution.
Example: "Yes, a polished UX matters because it directly drives activation, AND shipping on time matters because we have a Q3 growth dependency."

**Step 3 -- Make constraints explicit:**
- **Non-negotiables:** 10-week timeline; no activation regression; accessibility standards.
- **What can flex:** Number of segments in V1; depth of personalization; number of email sequences at launch.

**Step 4 -- Propose options + tradeoffs:**
- Option A: Ship the full design for 2 segments (high quality, narrower reach).
- Option B: Ship a simplified design for 4 segments (broader reach, less polish).
- Option C: Ship full design for 2 segments + simplified fallback for remaining segments.

**Step 5 -- Decide (or escalate via trigger):**
- The decision owner (per the Decision Rights in Section 3C) makes the call.
- If the decision owner can't resolve within 48 hours, escalate to VP Product with: (a) the question, (b) options and tradeoffs, (c) the team's recommendation.
- Once decided, log it. No re-litigation without new information.

**Norms for healthy disagreement:**
- Disagree in the room (or the thread), not in side channels.
- Critique the approach, not the person or function.
- If you feel unheard, say "I don't think my concern was addressed" -- the group pauses to listen.
- "I disagree and commit" is an acceptable and respected outcome. Log the dissent in the decision rationale.

### Credit & Recognition Plan

**Where we will share credit (moments):**
- **Weekly sync shout-outs:** Dedicate 5 min at the end of every sync to name a specific cross-functional contribution. The DRI (PM) is responsible for teeing this up but anyone can nominate.
- **Exec/stakeholder updates:** Every biweekly update explicitly names contributors from each function. No update goes out with only PM's name on it.
- **Demo days / reviews:** Rotate who presents. Eng demos the build. Design walks through the UX rationale. Data presents the metrics story. Marketing presents the messaging approach. PM facilitates but does not monopolize the stage.
- **Launch moment:** Launch announcement credits all contributing functions and names individuals.

**How we will share credit (mechanics):**
- Biweekly async updates include a "Contributors this cycle" section with specific names and contributions.
- Slack #onboarding-revamp channel: PM posts a "this week's MVPs" message every Friday.
- If an exec asks "who did this?", the default answer is the team and the specific individuals, not just "Product."
- Design, Eng, and Data leads are invited to present at the exec review in Week 10.

**Anti-patterns to avoid:**
- PM "owns the narrative" and others feel invisible. Mitigation: rotating presenters; named contributors in all written artifacts.
- Recognition only for the "visible" work (design, demos) while "invisible" work (instrumentation, QA, data pipelines) gets overlooked. Mitigation: explicitly call out infrastructure and quality work in shout-outs and updates.
- Credit given only at launch, not during the journey. Mitigation: weekly shout-outs start in Week 1.

---

## 8) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Competing priorities pull team members off the initiative mid-sprint | High | High | Lock commitments with functional leads in Week 1; escalate early if allocation drops below 50% for any function | PM + functional leads |
| Segment definitions require more research than 2 weeks | Medium | Medium | Start with existing data; use "good enough" segments for V1; refine post-launch | Data + PM |
| Email sequences depend on shared ESP with another team | Medium | Medium | Marketing to confirm ESP availability by Week 2; identify backup plan (in-app only for V1 if ESP blocked) | Marketing Lead |
| Instrumentation gaps in current tracking delay measurement | Medium | High | Data to audit existing events in Week 1; Eng to prioritize instrumentation alongside feature work (not as afterthought) | Data + Eng |
| Design and Eng disagree on feasibility of preferred UX direction | Medium | Medium | Prototype milestone at Week 4 forces early alignment; conflict protocol in place | Design + Eng + PM |
| Enterprise customer onboarding flows accidentally disrupted | Low | High | Enterprise flows explicitly out of scope; feature flags isolate new onboarding; QA regression suite includes enterprise paths | Eng + QA |
| A/B test doesn't reach statistical significance in time | Medium | Medium | Data to model required sample sizes by Week 6; PM to decide if rollout proceeds on directional data | Data + PM |

### Open Questions

1. **Growth team alignment:** Does the Growth team have any overlapping signup page changes planned for the same period? (Check by Week 1)
2. **Legal review:** Are we collecting any new data fields in the revamped onboarding? If so, do we need a Legal/Privacy review? (Confirm by Week 2)
3. **Infra/Platform capacity:** Does the A/B testing infrastructure need updates to support this initiative? (Eng to confirm by Week 2)
4. **Support readiness:** What's the current top-5 list of onboarding support tickets? Can CS/Support provide this input for discovery? (Ask in Week 1)
5. **Post-launch ownership:** After launch, who owns ongoing optimization of the onboarding flow? Is this the same team or a handoff? (Decide by Week 8)

### Next Steps (Week 1)

| Action | Owner | Due |
|---|---|---|
| Schedule kickoff meeting (all functions) to review this Collaboration Pack | PM | Day 1 |
| Each function lead confirms team member allocation (names + % time) | All function leads | Day 2 |
| Data pulls segment analysis and current funnel metrics | Data Analyst | End of Week 1 |
| Design begins user research synthesis (existing research + 3-5 user interviews) | Design Lead | End of Week 1 |
| Marketing audits ESP availability and current lifecycle campaign calendar | Marketing Lead | End of Week 1 |
| Eng confirms A/B test infrastructure readiness | Eng Lead | End of Week 1 |
| PM checks with Growth team and Legal on open questions 1 and 2 | PM | End of Week 1 |
| CS/Support provides top onboarding support ticket themes | CS Lead | End of Week 1 |
| PM creates Notion workspace and seeds all artifact templates | PM | Day 1 |

---

## Quality Gate: Checklist & Rubric Score

### Checklist (Pre-flight)

- [x] Mission is explicit (1-2 sentences) and tied to measurable success metrics.
- [x] Timeframe and collaboration mode are named (project team, 10 weeks).
- [x] Stakeholder map includes all execution dependencies and approvers ("no surprise veto").
- [x] Incentives/concerns are captured (what each function optimizes for + fears).
- [x] Roles & expectations contract includes decision rights and escalation triggers.
- [x] Artifact plan defines a source of truth and avoids doc sprawl.
- [x] Operating cadence is sustainable and outcome/decision/risk oriented.
- [x] Decision log exists and is seeded with the next 5 decisions.
- [x] Conflict protocol is explicit and usable in a real disagreement.
- [x] Credit/recognition plan prevents credit hoarding and creates shared ownership.
- [x] Risks / Open questions / Next steps are included.

### Decision Clarity Checklist

- [x] Every seeded decision has: owner, due date, criteria, and space for rationale.
- [x] The team has a standard for "what would change the decision" (new info thresholds).
- [x] Disagreements map to decision rights (decide vs. escalate).

### Rubric Self-Assessment

| Dimension | Score | Rationale |
|---|---|---|
| 1. Mission clarity + success metrics | 5 | Mission is explicit and testable; 3 metrics with current baselines and targets; 10-week timeframe with milestones. |
| 2. Stakeholder completeness + incentives | 4 | All executing and approving stakeholders identified; incentives captured; 3 "missing seats" flagged for resolution in Week 1-2. |
| 3. Roles, expectations, and decision rights | 5 | Expectations matrix covers all function pairs; responsibility map is explicit; decision rights and escalation triggers have specific thresholds; review cadence defined. |
| 4. Shared artifacts and source of truth | 5 | Artifact set is defined with clear owners and tools; single source of truth rules established; prototype milestone at Week 4 and dogfood at Week 7 reduce ambiguity. |
| 5. Operating cadence + decision velocity | 5 | Minimal meeting cadence (1 weekly sync + 1 design review); async-first updates; decision log seeded with 5 decisions; decision protocol prevents re-litigation. |
| 6. Collaboration norms (conflict + credit) | 5 | Conflict protocol is step-by-step with a worked example; credit plan includes specific mechanics (rotating presenters, named contributors, weekly shout-outs). |
| **Total** | **29 / 30** | Ship as-is. Minor gap: "missing seats" (Growth, Legal, Infra) should be confirmed in Week 1. |

### Interpretation

Score of 29/30 falls in the "ship as-is" range (26-30). The pack is ready for the kickoff meeting. The one area to strengthen in Week 1 is confirming the three "missing seats" (Growth team, Legal/Privacy, Infra/Platform) and adding them to the stakeholder map if needed.

---

## Appendix: Health Check Schedule

| Check | When | What to evaluate |
|---|---|---|
| Week 3 health check | End of Week 3 | Are decisions D1-D4 made? Is the expectations contract working? Any function feeling unheard? |
| Week 5 mid-point retro | End of Week 5 | Review the Roles & Expectations Contract; is rework trending down? Are meetings useful? Update the contract if needed. |
| Week 8 pre-launch check | End of Week 8 | Are A/B tests running? Is the launch checklist on track? Any escalation triggers hit? Final contract review. |
| Week 10 post-launch retro | End of Week 10 | What worked? What broke? Capture process improvements. Close the credit loop (recognize all contributors). Hand off to ongoing owner. |
