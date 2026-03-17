# Showcase: Problem Definition

> Demonstrates the value of the `problem-definition` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `problem-definition`. Product: B2B analytics tool. Segment: ops managers at 50-500 employee companies. Signal: activation drops after connecting data sources. Decision: decide whether to invest in fixing activation this quarter. Output: Problem Definition Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | General sections (problem, impact, hypotheses, next steps) loosely organized | 9-section canonical structure (context, problem statement, JTBD, alternatives, evidence log, success criteria, scope, prototype plan, risks/next steps) |
| Completeness | Covers problem, root causes, scope, and next steps; missing JTBD, alternatives analysis, evidence grading, and prototype/learning plan | Covers all dimensions including Jobs-To-Be-Done, 5 current alternatives with switching costs, 7 evidence items with confidence levels, success criteria with guardrails, and a 3-phase prototype plan |
| Actionability | Recommends 6 investigative next steps without owners, timelines, or success criteria | Provides 9 next steps with named owners, target dates, and a phased test plan (concierge, prototype, A/B) with explicit success criteria for each |
| Specificity | Metrics referenced directionally ("measurable drop," "significant portion") without baselines or targets | Quantified metrics with baselines and targets (activation rate: 30% to 50%, time-to-first-insight: >48h to <2h, empty-state encounters: <10%) |
| Quality gates | No self-assessment or verification checklist | Full 7-part checklist verification plus rubric scoring (16/16) confirming problem clarity, JTBD quality, evidence rigor, and scope boundaries |

## Key Differences

1. **Jobs-To-Be-Done and alternatives analysis.** The skill-guided output includes a structured JTBD section with a primary job statement and 4 sub-jobs, plus a 5-option alternatives table (including analog alternatives like spreadsheets and "do nothing") with explicit switching costs. The baseline omits JTBD entirely and does not systematically analyze what users do today.

2. **Evidence-graded assumptions with test plans.** The with-skill output separates 7 claims by confidence level (High/Medium/Low), names a "killer assumption," and assigns concrete validation tests to each. The baseline lists "What We Don't Yet Know" but does not grade confidence or propose specific tests for each hypothesis.

3. **Quantified success criteria with guardrails.** The skill output defines outcome metrics (activation rate from 30% to 50%), 3 leading indicators with targets, and 5 guardrails (support volume, data integrity, performance, privacy). The baseline mentions "sizing the opportunity" but provides no specific metric targets or guardrails.

4. **Phased prototype and learning plan.** The with-skill output designs a 3-phase test plan (concierge in weeks 1-2, clickable prototype in weeks 2-4, instrumented A/B in weeks 5-8) targeting the hardest assumptions first. The baseline recommends investigation but does not structure a progressive learning plan with go/no-go gates.

5. **Operational readiness with ownership.** The skill output includes a 9-row next steps table with named owner roles (Product analytics, CS lead, UX research, Engineering, Design lead) and target dates spanning weeks 1-10. The baseline lists 6 next steps without owners or timelines, making it harder to execute immediately.

## Verdict

The skill-guided output delivers a substantially more rigorous and actionable problem definition. It provides the analytical scaffolding (JTBD, alternatives, evidence grading, success criteria, prototype plan) that transforms a diagnostic document into a decision-ready brief. The baseline covers the problem space competently but would require significant additional work to become executable, particularly around quantified targets, assumption validation, and phased testing.

## With Skill Output

<details>
<summary>Expand full output (~22k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~10k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
