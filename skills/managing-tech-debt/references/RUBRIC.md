# Rubric (Score 1–4 per dimension)

Use this rubric to score the Tech Debt Management Pack. Target: **>= 20/28** with no 1s in “Safety & robustness”.

## 1) Decision clarity (1–4)
1 = Unclear what decision/action changes.
2 = Some decisions implied but not explicit.
3 = Decisions explicit; outputs aligned.
4 = Decisions explicit; trade-offs and stakeholders are aligned on next actions.

**0/1 boundary:** Score 1 if a reader cannot answer “what will we do differently after reading this?”
**1/2 boundary:** Score 2 if decisions are implied (e.g., “we should modernize”) but not stated as specific choices with owners.
**2/3 boundary:** Score 3 when each decision is a clear statement (“refactor service X”, “deprecate library Y”) tied to a deliverable.
**3/4 boundary:** Score 4 only when trade-offs for each decision are documented and stakeholders have a clear next action.

## 2) Evidence & signals (1–4)
1 = Pure opinion; no signals.
2 = Some anecdotes; weak linkage to symptoms.
3 = Symptoms and at least some measurable signals (or clear instrumentation plan).
4 = Clear baselines, confidence levels, and measurement plan for impact.

**0/1 boundary:** Score 1 if the only evidence is “engineers feel this is slow.”
**1/2 boundary:** Score 2 if anecdotes exist (e.g., “deploys are painful”) but no metric or signal is cited.
**2/3 boundary:** Score 3 when at least one symptom links to a measurable signal (incident count, p95 latency, cycle time) or an instrumentation plan to get it.
**3/4 boundary:** Score 4 only when baselines are numeric, confidence levels are labeled, and the measurement plan covers leading + lagging indicators.

## 3) Register completeness (1–4)
1 = List of items with missing owners/impact/effort.
2 = Register exists but inconsistent schema.
3 = Consistent schema; owners, impact, effort ranges, dependencies captured.
4 = Register enables immediate planning and can be maintained as an operating artifact.

**0/1 boundary:** Score 1 if the register is a bullet list of complaints without structure.
**1/2 boundary:** Score 2 if a table exists but columns vary across rows (some items have effort, others do not).
**2/3 boundary:** Score 3 when every row has the same columns (type, location, owner, impact, effort range, dependencies) and no field is blank.
**3/4 boundary:** Score 4 only when the register has a maintenance cadence, status tracking, and enough detail that a PM could plan sprints from it.

## 4) Prioritization quality (1–4)
1 = Ranked list with no rationale.
2 = Rationale exists but inconsistent or subjective.
3 = Transparent scoring and defensible top priorities.
4 = Prioritization accounts for sequencing and includes “enabler” work and stop conditions.

**0/1 boundary:** Score 1 if the list is ordered but no rationale accompanies any item.
**1/2 boundary:** Score 2 if rationale exists for some items but uses different criteria across items (impact for one, effort for another).
**2/3 boundary:** Score 3 when a consistent scoring model is applied and a skeptical reader would agree on the top 3.
**3/4 boundary:** Score 4 only when sequencing dependencies (“X must come before Y”), enabler work, and explicit stop conditions (“abandon if metric does not improve by milestone 2”) are included.

## 5) Strategy correctness (refactor vs rebuild) (1–4)
1 = Rebuild/refactor recommended without criteria.
2 = Options listed but incomplete criteria.
3 = Options + criteria + recommendation; acknowledges uncertainty.
4 = Includes migration phases, dual-run costs, cutover/decommission, rollback, and clear success metrics.

**0/1 boundary:** Score 1 if the recommendation is “rewrite it” with no options or criteria.
**1/2 boundary:** Score 2 if refactor and rebuild are both mentioned but the criteria for choosing are vague (“depends on complexity”).
**2/3 boundary:** Score 3 when explicit criteria (scope, risk, timeline, team capacity) lead to a stated recommendation with acknowledged uncertainty.
**3/4 boundary:** Score 4 only when migration phases, dual-run cost, decommission plan, rollback triggers, and success metrics are all present.

## 6) Execution feasibility (1–4)
1 = Plan is vague or unrealistic.
2 = Milestones exist but weak acceptance criteria.
3 = Incremental milestones with owners, acceptance criteria, capacity assumptions.
4 = Sequenced plan with measurable milestones, risks mitigations, and immediate next step.

**0/1 boundary:** Score 1 if the plan is “refactor over the next quarter” with no breakdown.
**1/2 boundary:** Score 2 if milestones exist but lack pass/fail acceptance criteria or capacity assumptions.
**2/3 boundary:** Score 3 when each milestone has an owner, a measurable acceptance criterion, and a capacity allocation (e.g., “20% of sprint”).
**3/4 boundary:** Score 4 only when milestones are sequenced with dependencies, risk mitigations are per-milestone, and the first milestone can start this week.

## 7) Safety & robustness (1–4)
1 = Encourages risky/irreversible actions without safeguards.
2 = Some safeguards but missing rollback/confirmation gates.
3 = Explicit safety gates; no secrets; rollback guidance included where relevant.
4 = Strong least-privilege posture, explicit human checkpoints for one-way-door actions, and clear rollback triggers.

**0/1 boundary:** Score 1 if the plan includes destructive actions (drop table, delete service) without any safeguard.
**1/2 boundary:** Score 2 if safeguards are mentioned generally (“be careful”) but no specific rollback or confirmation gate is defined.
**2/3 boundary:** Score 3 when every irreversible action has a named rollback step and no secrets/credentials appear in the plan.
**3/4 boundary:** Score 4 only when one-way-door actions have human approval gates, rollback triggers are quantified (e.g., “rollback if error rate > 1%”), and the plan follows least-privilege principles.

