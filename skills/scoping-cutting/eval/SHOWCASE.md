# Showcase: Scoping Cutting

> Demonstrates the value of the `scoping-cutting` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> We're building bulk CSV import for admins. We have 4 weeks. Cut scope so we can ship something useful; include a Wizard-of-Oz validation plan for risky parts.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Feature wish list, scope cut table, week-by-week plan, risk register, WoZ plan, technical decisions, success metrics, open questions | 8-section pack: context snapshot, outcome + hypothesis, appetite + success bar, MLS spec, 20-item cut list, validation plan, delivery plan with scope-change guardrails, risks/open questions |
| Completeness | Covers the essentials well with clear in/out scope, WoZ tests for mapping and validation UX, and technical pre-decisions | Comprehensive: explicit hypotheses (value, usability, trust), measurable success criteria with guardrails, 20-item cut list with revisit triggers, scope-change policy with trade-off rules |
| Actionability | Week-by-week plan with deliverables; WoZ tests have clear protocols; pre-decided technical choices reduce ambiguity | Highly actionable: each cut item has a "revisit when" trigger, validation tests have success/failure/pivot criteria, and a formal "trade, don't add" scope-change policy prevents creep |
| Specificity | Specific technical choices (5K row cap, UTF-8, comma-only); WoZ tests target column mapping and error resolution with concrete protocols | More specific on outcomes: 3 named hypotheses with measurable thresholds (60% task completion, <5 min import, 30% adoption), per-item risk impact assessments in the cut list |
| Quality gates | Success metrics table with targets; risk register with mitigations | Full self-assessment checklist (7 categories) + 8-dimension rubric; "done means" definition with non-negotiables; milestone gates per week |

## Key Differences

1. **Hypothesis-driven framing.** The skill output anchors the entire scope in three falsifiable hypotheses (value, usability, trust) with measurable success thresholds. The baseline jumps directly to features and scope cuts without articulating what the MVP is designed to test, making it harder to evaluate whether the right things were kept.

2. **Cut list depth and rigor.** The skill output evaluates 20 individual items with keep/cut/defer decisions, each justified against the outcome and appetite, with risk impact assessments and concrete "revisit when" triggers. The baseline has a shorter out-of-scope table with rationale and revisit dates but lacks the per-item risk analysis and triggering conditions.

3. **Scope-change governance.** The skill output includes a formal "trade, don't add" policy with a decision owner, escalation path, default trade-off order, and a single intake channel for requests. The baseline has no equivalent mechanism, leaving scope management to ad hoc negotiation.

4. **Validation plan structure.** Both outputs include WoZ tests, but the skill output ranks assumptions by risk and ties each test to specific success/failure criteria with pivot plans. The baseline's WoZ tests are well-designed but structured more as standalone experiments than as a risk-mitigation hierarchy.

5. **Guardrails and non-negotiables.** The skill output defines explicit guardrails (zero silent data corruption, <5% support tickets, <10% latency impact, PII file purge within 24h) that cannot be traded away. The baseline lists similar requirements as technical decisions but without framing them as hard constraints that survive scope negotiations.

## Verdict

Both outputs are high quality and would serve a team well. The skill-guided output adds meaningful structure through its hypothesis-first approach, richer cut-list analysis, and formal scope-change policy -- all of which reduce the risk of unmanaged scope creep during a tight 4-week build. The baseline is more opinionated on technical choices upfront, which has practical value, but lacks the governance and evaluation framework that makes scope decisions durable under pressure.

## With Skill Output

<details>
<summary>Expand full output (~27k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~14k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
