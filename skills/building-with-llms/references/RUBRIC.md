# Rubric (score 1–5 per category)

Suggested bar for “ship-ready”: average ≥ 4.0 and no category below 3.

## 1) Problem framing and boundaries
1 = Vague goal; no non-goals; no success definition
2 = Goal exists but is unmeasurable (e.g., “make it smarter”); non-goals absent or trivial; no guardrails defined
3 = Clear job statement; some constraints; partial success/guardrails
4 = Job statement + non-goals + measurable success criteria present; guardrails listed but not all quantified
5 = Crisp job + non-goals; measurable success + guardrails; top failure modes named

**0/1 boundary:** Score 1 if you cannot answer “what does the LLM do and not do?” after reading the brief.
**1/2 boundary:** Score 2 if a goal exists but lacks any measurable success metric or guardrail.
**2/3 boundary:** Score 3 when someone could build against the spec but would need to guess at some acceptance thresholds.
**4/5 boundary:** Score 5 only when every success metric has a numeric target and top 3 failure modes are explicitly named.

## 2) Prompt + tool contract quality
1 = Prompt is generic; tools undefined; output format unclear
2 = Prompt has a role/persona but no DO/DO NOT rules; tools listed but schemas missing; no examples
3 = Prompt has rules; tools described; some examples
4 = Prompt + tools + output schema complete; examples for happy path; safety constraints present but uncertainty behavior not specified
5 = Contract is testable: DO/DO NOT rules, uncertainty behavior, schema, examples, and safety constraints for each tool

**0/1 boundary:** Score 1 if the prompt is a single sentence with no structure.
**2/3 boundary:** Score 3 when a developer could implement the contract but would guess at edge-case behavior.
**4/5 boundary:** Score 5 only when the contract specifies what the model does when it does not know, encounters conflicting instructions, or receives adversarial input.

## 3) Context strategy correctness
1 = “Just stuff context”; no source-of-truth concept
2 = Context sources listed but no retrieval strategy, no authority ranking, no freshness policy
3 = Some retrieval/tool plan; partial conflict handling
4 = Clear retrieval pipeline with source-of-truth defined; freshness and authority partially addressed; grounding expectations stated
5 = Clear context pipeline with authority, freshness, conflict handling, and grounding expectations

**0/1 boundary:** Score 1 if context approach is “put everything in the prompt” with no discussion of limits.
**2/3 boundary:** Score 3 when retrieval exists but you cannot answer “what happens when two sources disagree?”
**4/5 boundary:** Score 5 only when authority hierarchy, staleness policy, and grounding verification are all explicit.

## 4) Evaluation rigor (offline)
1 = No evals; only ad hoc manual testing
2 = A few manual test cases exist; no rubric or acceptance threshold defined
3 = Basic test set and rubric; thresholds unclear
4 = Test set covers happy path + key failure modes; rubric with thresholds; some automated checks; red-team cases mentioned but incomplete
5 = Test set covers failure modes + red team; rubric + thresholds + automated checks; bugs become tests

**0/1 boundary:** Score 1 if quality assurance is “we’ll try it and see.”
**2/3 boundary:** Score 3 when a test set exists but you could not re-run it and get a pass/fail number.
**4/5 boundary:** Score 5 only when red-team cases exist, thresholds are numeric, and the plan states “every production bug becomes a test case.”

## 5) Production readiness
1 = No budgets/monitoring; no fallback
2 = Monitoring mentioned but no specific metrics, thresholds, or fallback mechanism
3 = Some monitoring; partial budgets; basic rollback
4 = Cost + latency budgets defined; logging fields specified; rollback plan exists; prompt versioning mentioned but not operationalized
5 = Budgets + monitoring + fallbacks + logging are complete; prompt versioning and incident hooks exist

**0/1 boundary:** Score 1 if there is no mention of what happens when the model is slow, wrong, or expensive.
**2/3 boundary:** Score 3 when monitoring exists but you cannot answer “what alert fires and who responds?”
**4/5 boundary:** Score 5 only when prompt versions are tracked, incident playbook hooks are named, and fallback behavior is tested.

## 6) Iteration loop and engineering plan
1 = “We’ll iterate” without a loop
2 = Plan mentions iteration but no concrete loop (no reproduce/label/test/fix/measure steps)
3 = Basic prototype and feedback plan
4 = Prototype slice defined; feedback loop with evals; coding agent usage mentioned with some guardrails
5 = Tight loop: reproduce→label→test→fix→measure; safe use of coding agents with review gates and rollback

**0/1 boundary:** Score 1 if “iteration” appears but no process is described.
**2/3 boundary:** Score 3 when a prototype plan exists but the feedback-to-improvement loop is vague.
**4/5 boundary:** Score 5 only when every step of reproduce→label→test→fix→measure is explicit and coding-agent safety constraints are documented.

