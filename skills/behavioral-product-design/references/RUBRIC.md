# Rubric (score 1–5)

Score the pack, then improve the lowest sections before finalizing.

## 1) Problem + behavior clarity
**1** Vague goal (“engagement”), no specific behavior or baseline.
**2** Target behavior is named but not observable or time-bounded; baseline is missing or “we think it's low.”
**3** Behavior and baseline exist but context/guardrails are weak.
**4** Behavior is observable and time-bounded with a baseline metric; guardrails are listed but thresholds are not specified.
**5** Clear behavior spec, baseline, success + guardrails, and user benefit.

## 2) Diagnosis quality
**1** Generic bias list with no link to the user journey.
**2** Some biases mapped to journey steps but evidence is absent; barriers are asserted without data or user signals.
**3** Some moments/barriers mapped, evidence is partial.
**4** Most friction points have a diagnosed mechanism with supporting evidence or explicitly labeled hypotheses; minor gaps in coverage.
**5** Clear moment-by-moment diagnosis with evidence and labeled hypotheses.

## 3) Intervention-mechanism fit
**1** UI ideas without mechanisms; “add reminders” everywhere.
**2** Some interventions reference a mechanism but the mapping is loose; only one barrier type (e.g., only forgetting) is addressed.
**3** Some mechanism alignment; gaps in feasibility or coverage.
**4** Interventions map to diagnosed mechanisms across multiple barrier types; minor feasibility or coverage gaps remain.
**5** Interventions clearly map to mechanisms and cover friction/uncertainty/motivation.

## 4) Ethics + user trust
**1** Manipulative/dark patterns or missing user control.
**2** Ethics acknowledged in principle but no concrete opt-out mechanisms, transparency measures, or harm mitigations specified.
**3** Mentions ethics but lacks concrete mitigations and controls.
**4** Transparency and opt-out are designed into interventions; harm mitigations exist but sensitive-context safeguards are incomplete.
**5** Explicit transparency, opt-out, harm mitigations, and safeguards for sensitive contexts.

## 5) Experimentation + measurement
**1** No instrumentation or decision rule.
**2** Primary metric identified but no event definitions, no guardrail metrics, or no rollout/rollback plan.
**3** Metrics exist but unclear evaluation plan.
**4** Events defined for primary and guardrail metrics; experiment design is feasible; rollout plan exists but rollback triggers are vague.
**5** Feasible experiment design, events defined, guardrails + rollout/rollback included.

## 6) Execution readiness
**1** Not actionable; no build-ready specs.
**2** Intervention concepts exist but lack UX/copy detail, states, or edge cases; an engineer cannot start without significant clarification.
**3** Some specs but missing states/edge cases.
**4** 1-3 specs have UX/copy, states, and most edge cases; minor decisions remain but an engineer could start implementation.
**5** 1-3 intervention specs are implementable in 1-2 sprints with clear checks.

