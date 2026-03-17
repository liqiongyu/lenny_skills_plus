# Showcase: Defining Product Vision

> Demonstrates the value of the `defining-product-vision` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `defining-product-vision`. We're a workflow automation platform for IT and Security teams. Problem: complex approvals and fragmented tooling slow down releases and increase risk. Horizon: 5-7 years. Constraints: compliance-first; do not degrade reliability or auditability. Output: a Product Vision Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 13 sections: executive summary, problem, vision, principles, target customer, 3-horizon strategy, use cases, competitive landscape, architecture, risks, metrics, "what this is NOT," call to action | 6 sections following the skill workflow: context snapshot, problem anchor, vision statement + narrative, vision pillars + experience principles, strategy bridge (choices + non-goals + wedge), rollout + alignment plan, risks/open questions/next steps |
| Completeness | Very comprehensive: includes 3-horizon product strategy with specific capabilities, 4 use cases, competitive landscape table, technical architecture principles, and 5-year business metrics | Focuses on vision clarity: potent user problem, pillars with invest/say-no implications, 5 strategic choices, 7 non-goals, near-term wedge, rollout workshop agenda, and anticipated objections with responses |
| Actionability | Provides detailed H1/H2/H3 roadmap with specific features and success metrics per horizon; includes architecture principles and technology decisions | Strategy bridge settles 3 named debates (platform vs. point-solution, build vs. partner GRC, regulated vs. horizontal); rollout plan includes a 75-minute workshop agenda with specific discussion blocks and pre-read instructions |
| Specificity | Names specific competitor categories and tools; provides 5-year ARR targets ($10M-$100M); specifies architecture patterns (event-driven, immutable log) | Each pillar has explicit "invest in" and "say no to" implications; experience principles include example behaviors; wedge describes a specific form factor with time-to-value target (under 1 hour) |
| Quality gates | No self-assessment | Full quality gate (6 checklists) plus rubric scoring 20/20 |

## Key Differences

1. **Problem anchor vs. problem description.** The skill output anchors the vision in a specific, potent user problem statement ("IT and Security leads struggle to approve, track, and audit changes across fragmented toolchains...") and defines what success looks like from the customer's perspective. The baseline describes the problem thoroughly but across multiple sections without a single anchoring formulation.

2. **Pillars with decision implications.** The skill output defines 5 vision pillars, each with explicit "invest in" and "say no to" guidance. For example, Pillar 2 says "invest in deep integrations with top 30 tools; say no to shallow notification-only integrations." The baseline has strategic principles but without the explicit investment tradeoffs that make a vision decision-useful.

3. **Strategy bridge with non-goals.** The skill output includes 7 explicit non-goals (e.g., "we will NOT build a general-purpose workflow automation tool") that sharpen the vision by defining what the product will not become. The baseline has a "What This Vision Is NOT" section with 6 items, but the skill output ties non-goals directly to strategic choices and pillar implications.

4. **Near-term wedge and path to vision.** The skill output describes a specific near-term form factor ("change-management control plane") with 3 first product bets that progress toward the full vision. The baseline uses a 3-horizon framework with detailed feature lists, which is more comprehensive but less focused on the critical bridge between today's product and the 5-7 year vision.

5. **Alignment and adoption plan.** The skill output includes a detailed rollout plan: 75-minute workshop agenda, pre-read instructions, anticipated objections with pre-built responses, and iteration cadence. The baseline does not address how to communicate, debate, or align stakeholders around the vision.

## Verdict

The baseline produces a more comprehensive strategic document with detailed roadmap, architecture, and business metrics -- suitable for a board or investor audience. The skill output produces a more focused vision alignment tool designed to settle specific debates, guide daily product decisions, and build shared understanding across a leadership team. The skill pack's emphasis on decision-useful pillars, explicit non-goals, and rollout planning makes it better suited for internal alignment, while the baseline's breadth makes it better suited for external communication.

## With Skill Output

<details>
<summary>Expand full output (~27k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~20k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
