# Showcase: Startup Pivoting

> Demonstrates the value of the `startup-pivoting` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `startup-pivoting`. We built an AI support copilot for e-commerce SMBs. We have 12 trial sign-ups, 3 converted to paid ($200/month each), but D30 retention is 40% and sales cycles average 6 weeks (too long for our price point). We have 5 months of runway ($180k remaining) and a team of 3 (2 engineers + 1 founder doing sales). We're seeing stronger pull from mid-market companies asking for our AI to handle returns/refunds specifically rather than general support. Should we pivot, and if so how? Create a Pivot Decision & Execution Pack with an exhaustion check (could we fix retention/sales cycle without pivoting?), a 4P pivot options grid (including narrowing to returns-only and moving upmarket), a recommended thesis with metrics and kill criteria, and a 4-week validation sprint plan. Output: Pivot Decision & Execution Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 7 sections: exhaustion check (retention + sales cycle analysis), 4P grid (4 options), recommended thesis, validation sprint, financial model, risk register, communication plan | 8-section pack: context snapshot, stuck diagnosis (symptoms + causes + evidence gaps), exhaustion check (6 levers evaluated), 4P grid (6 options), pivot thesis + metrics + kill criteria, validation plan with learning goals, 4-week execution plan, risks/open questions/next steps |
| Completeness | Includes a financial projection model showing path to break-even, competitive landscape comparison table, and ROI calculator for sales conversations | Includes a "stuck diagnosis" separating symptoms from causes, evidence tagging (fact vs. assumption), a "Butterfield Rule" exhaustion check with quality-of-attempt ratings per lever, and a shareable 1-page Pivot Decision Memo |
| Actionability | Sprint plan has specific weekly deliverables per role; design partner terms are spelled out ($500/month discounted rate); kill criteria use a scored checklist | Sprint plan has specific daily deliverables in Week 1 with gate checks at Week 2, 3, 4, and 8; kill criteria are binary decision gates with explicit "if no, then what" actions; cut list names 4 specific items being stopped |
| Specificity | Quantifies the LTV:CAC problem ($500 LTV vs. $3-5K CAC); provides a go/no-go scoring rubric (1-5 on 6 dimensions); estimates 12-week revenue trajectory by month | Quantifies evidence gaps (how many mid-market requests? why are churners leaving?); classifies each symptom as demand problem vs. execution problem; provides 5 learning goals mapped to specific decisions |
| Quality gates | Week 4 checkpoint with scored rubric (6 criteria, 1-5 scale, with thresholds for go/warn/kill) | 4 dated kill criteria gates with binary decisions; full 10-dimension self-assessment checklist + rubric; "what would change our mind" section per learning goal |

## Key Differences

1. **Diagnostic depth before prescribing.** The skill output separates symptoms from hypothesized causes, tags each piece of evidence as fact or assumption, and identifies 5 specific evidence gaps that must be filled. The baseline provides strong quantitative analysis (LTV:CAC math, retention modeling) but moves more quickly to the recommendation without a structured diagnostic framework.

2. **Exhaustion check methodology.** The skill output evaluates 6 non-pivot levers (ICP refinement, positioning, pricing, onboarding, distribution, reliability) with a quality-of-attempt rating and "best next attempt" for each, then provides a clear verdict on why the remaining levers are insufficient given runway. The baseline's exhaustion check reaches the same conclusion but evaluates fewer levers with less structured reasoning.

3. **Option set breadth.** The skill output evaluates 6 pivot options including two creative alternatives (Returns API/platform and refund fraud detection) and classifies each as a 10% or 200% pivot. The baseline evaluates 4 options which cover the core directions but miss the platform and fraud angles that could be valuable alternatives if the primary pivot fails.

4. **Kill criteria precision.** The skill output defines 4 dated gates with binary conditions and explicit fallback actions (e.g., "Gate 1, Week 2: Fewer than 5 qualified calls --> Pause, re-evaluate ICP reachability"). The baseline uses a scored checklist approach (6 dimensions rated 1-5) which provides nuance but may be harder to enforce objectively under pressure.

5. **Communication and transition planning.** Both outputs address team alignment and existing customer management. The baseline adds a detailed financial model showing month-by-month cash projections under the pivot scenario, which is valuable for investor conversations. The skill output includes a shareable 1-page Pivot Decision Memo designed for async review by advisors and investors.

## Verdict

Both outputs provide strong, actionable pivot analysis for a startup with limited runway. The skill-guided output is more rigorous in its diagnostic process -- the structured stuck diagnosis, evidence tagging, and exhaustion check methodology build a more defensible case for why pivoting is the right call. The baseline is more execution-ready in certain areas, particularly the financial model and competitive landscape analysis. For a founder making a high-stakes resource allocation decision, the skill output's diagnostic clarity and binary kill criteria provide more decisive guidance.

## With Skill Output

<details>
<summary>Expand full output (~40k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~29k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
