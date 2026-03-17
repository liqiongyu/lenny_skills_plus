# Rubric (Score 1–5)

Score the pack across the dimensions below. Use this to decide whether the evaluation is decision-ready.

## Scoring guidance
- **1 = Weak:** vague, untestable, missing key info, not actionable.
- **3 = Acceptable:** mostly complete, some assumptions, decision possible with caution.
- **5 = Strong:** specific, testable, evidence-driven, operationally ready, risks owned.

## Dimensions

1) **Problem clarity**
- 1: Tool-led framing; no clear workflow or user.
- 2: Problem mentioned but framed around the tool (“we should use X”) rather than the job-to-be-done; no non-goals.
- 3: Clear workflow + user; some ambiguity remains.
- 4: Crisp problem statement with non-goals; stakeholders identified but not all aligned.
- 5: Crisp problem statement + non-goals; stakeholders agree on the job-to-be-done.

**0/1 boundary:** Score 1 if you cannot explain the decision without naming the candidate tool.
**1/2 boundary:** Score 2 if a problem exists but the framing is “should we adopt X?” rather than “how do we solve Y?”
**2/3 boundary:** Score 3 when the workflow and user are clear but some scope boundaries are missing.
**4/5 boundary:** Score 5 only when non-goals are explicit and all stakeholders can restate the problem independently.

2) **Criteria quality**
- 1: Criteria are a feature checklist; no weights or measures.
- 2: Criteria exist but are subjective (“easy to use”, “powerful”); no weights or deal-breakers.
- 3: Criteria relate to workflows/ROI; some measures are soft.
- 4: Most criteria are measurable; weights assigned; deal-breakers identified but not all falsifiable.
- 5: Criteria are measurable/falsifiable; weights and deal breakers are explicit.

**0/1 boundary:** Score 1 if criteria are just a vendor feature comparison table.
**2/3 boundary:** Score 3 when criteria reference real workflows but at least one key criterion lacks a measurement method.
**4/5 boundary:** Score 5 only when every criterion could be validated in a pilot and deal-breakers have pass/fail thresholds.

3) **Options coverage**
- 1: Only one option considered; status quo ignored.
- 2: Two options considered but status quo (“do nothing / improve current”) is missing.
- 3: Multiple options considered; trade-offs captured.
- 4: Status quo + 2+ alternatives with trade-offs; build option acknowledged but not deeply analyzed.
- 5: Status quo + credible alternatives + build/hybrid considered where appropriate.

**0/1 boundary:** Score 1 if the pack evaluates a single vendor with no alternatives.
**2/3 boundary:** Score 3 when alternatives exist but the status-quo baseline is missing or hand-waved.
**4/5 boundary:** Score 5 only when build/hybrid is explicitly considered (even if rejected) and status quo is a real option.

4) **Evidence strength**
- 1: Mostly opinions; no pilot or validation plan.
- 2: Some references (blog posts, vendor claims) cited but no first-party evidence or pilot design.
- 3: Some evidence (demo/spike/reference) and a reasonable pilot plan.
- 4: Pilot plan with hypotheses, metrics, and timeline; some first-party evidence from a spike or demo.
- 5: Pilot evidence (or strong rationale to skip) ties directly to criteria and metrics.

**0/1 boundary:** Score 1 if the recommendation rests on vendor marketing or team opinion alone.
**2/3 boundary:** Score 3 when a pilot plan exists but hypotheses are vague (“see if it works”).
**4/5 boundary:** Score 5 only when pilot results (or a documented rationale to skip) map to specific criteria scores.

5) **Build vs buy reasoning**
- 1: Focused on sticker price only.
- 2: License cost compared to build cost, but maintenance, on-call, and upgrade burden are ignored.
- 3: Includes some maintenance/bandwidth considerations.
- 4: TCO + bandwidth + opportunity cost addressed; lock-in acknowledged but exit plan is vague.
- 5: Includes bandwidth/TCO + opportunity cost + core competency and lock-in/exit plan.

**0/1 boundary:** Score 1 if the comparison is “vendor costs $X/yr vs. N engineer-months to build.”
**2/3 boundary:** Score 3 when maintenance cost is mentioned but opportunity cost of engineering time is absent.
**4/5 boundary:** Score 5 only when the analysis includes who maintains the system at 12 months, exit/migration cost, and core-competency alignment.

6) **Risk management**
- 1: Risks are generic or missing.
- 2: Risks listed (e.g., “security,” “vendor lock-in”) but no mitigations or owners.
- 3: Risks identified with partial mitigations.
- 4: Top risks have owners and mitigations; blocker vs. monitor labeling present; AI-specific claims partially tested.
- 5: Top risks have owners, mitigations, and clear “blocker vs monitor” labeling; AI guardrails assumptions are tested.

**0/1 boundary:** Score 1 if no risks section exists or it says “low risk.”
**2/3 boundary:** Score 3 when risks are named but at least one top risk lacks an owner or mitigation.
**4/5 boundary:** Score 5 only when every top risk has an owner, a mitigation, a blocker/monitor label, and any vendor “safety” claims are independently verified.

7) **Decision readiness**
- 1: No clear recommendation or next actions.
- 2: Recommendation stated but no rationale, timeline, or next actions.
- 3: Recommendation exists; adoption steps are rough.
- 4: Clear recommendation with rationale and trade-offs; adoption plan exists but rollback plan is incomplete.
- 5: Clear decision, owner, timeline, adoption + rollback plan; next steps are concrete.

**0/1 boundary:** Score 1 if the pack ends without a recommendation.
**2/3 boundary:** Score 3 when a recommendation exists but you cannot answer “what happens Monday morning?”
**4/5 boundary:** Score 5 only when the memo names the decision-maker, adoption timeline, rollback trigger, and immediate next actions.

## Suggested pass thresholds
- **Low-risk/internal tooling:** average score >= 3.5
- **Customer-facing or sensitive data:** average score >= 4.0 and **Risk management >= 4**

