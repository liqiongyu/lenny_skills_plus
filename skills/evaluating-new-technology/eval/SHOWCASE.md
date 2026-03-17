# Showcase: Evaluating New Technology

> Demonstrates the value of the `evaluating-new-technology` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `evaluating-new-technology`. Candidate: an AI 'guardrails' vendor that claims to block prompt injection. Problem: we're launching a customer-facing support agent and need safer tool use. Current stack: Zendesk + internal KB. Constraints: SOC2 required, PII present, SSO required, budget $50k/yr, decision in 3 weeks. Output: Technology Evaluation Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 14 sections organized as a comprehensive vendor evaluation report with detailed per-vendor assessments | 7 numbered sections following a decision pipeline: Evaluation Brief, Options Matrix, Build vs Buy, Pilot Plan, Risk Review, Decision Memo, Next Steps |
| Completeness | Detailed vendor landscape (6 vendors scored individually), architectural design, 3-year TCO, and Go/No-Go criteria | 4 options (status quo, buy, build, hybrid) with weighted criteria matrix, build-vs-buy TCO ledger, pilot with 3 testable hypotheses, 8-layer defense-in-depth architecture, and rollback plan |
| Actionability | Vendor comparison matrix with scores; PoC plan testing top 2 vendors in parallel over 5 days | 9-step next-steps table with owners and deadlines by day; pilot with binary exit criteria (adopt/iterate/reject) |
| Specificity | Scores 6 vendors across 5 weighted categories with per-vendor assessments; specific pricing estimates | Weighted criteria matrix with 1-5 scores across 4 options; explicit deal-breakers list; defense-in-depth architecture with 8 named layers and owners |
| Quality gates | Go/No-Go threshold table with escalation path if no vendor qualifies | 11-item checklist plus rubric self-score averaging 4.4/5 across 7 dimensions |

## Key Differences

1. **Problem-first vs. vendor-first framing.** The skill output starts with a tool-agnostic problem statement, explicitly lists 5 non-goals, and defines success metrics before considering any vendor. The baseline opens with a vendor landscape, which risks anchoring the evaluation to available solutions rather than the actual problem.

2. **Build vs. buy analysis with opportunity cost.** The skill output includes a detailed TCO ledger comparing build and buy across 6 cost areas (initial, maintenance, on-call, compliance, procurement, opportunity cost), concluding that buy is 40-60% cheaper in year one. The baseline estimates 3-year TCO for the buy option but does not systematically compare it to a build alternative.

3. **AI-specific skepticism and defense-in-depth.** The skill output explicitly warns against relying on vendor guardrails as the sole security layer and defines an 8-layer defense-in-depth architecture (input filtering through continuous evaluation) with owners per layer. The baseline mentions layering defenses but does not formalize the multi-layer architecture or assign ownership.

4. **Pilot with testable hypotheses.** The skill output defines 3 specific hypotheses (95% block rate, <300ms latency, <2% false positives) with measurement methods and binary exit criteria. The baseline provides a PoC plan with similar metrics but frames them as objectives rather than falsifiable hypotheses.

5. **Vendor assessment depth vs. breadth.** The baseline evaluates 6 individual vendors with per-vendor scorecards, making a specific recommendation (Lakera Guard). The skill output evaluates 4 strategic options without naming a specific vendor, deferring vendor selection to the pilot phase. This is a genuine trade-off: the baseline gives an immediate vendor recommendation while the skill output gives a more rigorous decision framework.

## Verdict

The skill output produces a decision framework that would hold up under executive scrutiny: problem-agnostic evaluation criteria, explicit build-vs-buy reasoning, defense-in-depth requirements regardless of vendor choice, and a pilot with pass/fail criteria. The baseline is more immediately useful for someone who wants a vendor recommendation today, with detailed per-vendor scores and a specific pick. The skill pack's strength is ensuring the right decision gets made; the baseline's strength is speed to a vendor shortlist.

## With Skill Output

<details>
<summary>Expand full output (~15k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~18k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
