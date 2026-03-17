# Rubric (Score the AI Evals Pack)

Score each category from 1 (poor) to 5 (excellent). A “ship-ready” pack typically averages ≥4 with no category below 3.

## 1) Clarity of decision + scope
1: Vague goal; no decision or non-goals.
2: Decision exists ("ship or not") but scope is unbounded; non-goals absent; target behaviors not listed.
3: Decision is stated; scope mostly clear; a few ambiguities remain.
4: Decision, scope, non-goals, and target behaviors all present; minor gaps in acceptance thresholds.
5: Decision, scope, and non-goals are crisp; stakeholders can act immediately.

## 2) Test set quality (representativeness + coverage)
1: Mostly happy paths; little tagging/coverage logic.
2: Some edge cases included but no tagging schema; coverage is ad hoc with no plan for safety/adversarial inputs.
3: Covers main scenarios; some tagging and edge cases; gaps remain.
4: Strong coverage with tagging; safety/adversarial cases included; minor gaps in long-tail or cross-segment coverage.
5: High-signal cases with clear schema and strong coverage across critical segments/risks.

## 3) Taxonomy usefulness
1: Generic categories; not actionable.
2: Categories exist but overlap or lack severity; no mapping to fixes or new tests.
3: Reasonable categories; some actionable guidance.
4: Categories are specific and severity-weighted; most map to fixes; 1-2 categories need refinement.
5: Clear, specific, severity-weighted categories that map to fixes and new tests.

## 4) Rubric executability
1: Subjective/vibes; judges cannot apply consistently.
2: Scoring dimensions defined but descriptions are abstract; no examples or tie-breakers; judges would disagree frequently.
3: Mostly clear; still some ambiguity.
4: Behaviorally anchored with examples; tie-breakers exist for most dimensions; minor ambiguity in 1 dimension.
5: Behaviorally anchored; clear scoring, examples, tie-breakers; high judge agreement expected.

## 5) Judge + harness repeatability
1: No runbook; not reproducible.
2: Judge type chosen but no calibration plan; prompts/models not versioned; cost/time unknown.
3: Repeatable at a basic level; some versioning/cost gaps.
4: Repeatable with versioned artifacts and calibration; cost estimates present; minor data handling gaps.
5: Fully repeatable and auditable: versioned artifacts, calibration, cost/time estimates, clear data handling.

## 6) Reporting + iteration loop actionability
1: Results don’t translate into action.
2: Results presented (pass rate) but no regression rules; no process for turning failures into new tests.
3: Results are interpretable; next steps exist.
4: Decision-ready reporting with thresholds; regression rules defined; iteration loop exists but informal.
5: Decision-ready reporting with regression rules; iteration loop turns failures into prioritized work.

## Required final section
The pack must include: **Risks**, **Open questions**, **Next steps**.

## Required final section
The pack must include: **Risks**, **Open questions**, **Next steps**.

