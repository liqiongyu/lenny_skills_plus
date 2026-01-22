# PRD Quality Rubric (0/1/2 per item)

0 = missing, 1 = present but weak, 2 = clear and testable.

## 1) Problem clarity (0–2)
- Target user is explicit
- Problem is stated without embedding the solution
- Evidence exists (data, quotes, examples) or assumptions are labeled

## 2) Why now (0–2)
- Urgency / window / risk is explicit
- Opportunity cost vs alternatives is acknowledged

## 3) Scope discipline (0–2)
- Goals are measurable
- Non-goals are explicit
- Out of scope is concrete (not just “later”)

## 4) Requirements are executable (0–2)
- Requirements are numbered (R1…)
- Each requirement is testable (acceptance criteria or measurable behavior)

## 5) Success metrics & instrumentation (0–2)
- Success metric(s) defined
- Guardrails defined (what must not get worse)
- Instrumentation plan exists (events/dashboards/owners)

## 6) Rollout & reversibility (0–2)
- Rollout plan (flag, phased release, QA)
- Rollback plan

## 7) Risks & dependencies (0–2)
- Risks enumerated + mitigations
- Dependencies/assumptions listed with owners

## 8) AI-only: evals & prompt set (0–2)
(Only score if AI/LLM feature.)
- Non-negotiables translated into evals
- Test set covers golden + adversarial + regression
- Judge rubric + threshold defined
- Prompt set includes guardrails + expected output shape

Suggested pass bar: 12/16 for non-AI PRDs, 14/18 for AI PRDs.
