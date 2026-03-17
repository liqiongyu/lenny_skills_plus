# Showcase: Platform Strategy

> Demonstrates the value of the `platform-strategy` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `platform-strategy`. Internal ML platform used by 40 engineers. Biggest pain is shipping models reliably and quickly. PII present; SOC2. Two platform engineers.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 10-section strategy document covering executive summary, current state, principles, architecture, SOC 2, roadmap, org model, metrics, risks, and recommendations with a technology appendix | 8-section Platform Strategy Pack following a prescribed methodology (Product Charter, Surface & Interface Map, Lifecycle Stage & Open/Close Strategy, Moat & Ecosystem Model, Governance & Policy Plan, AI System Defensibility, Metrics & Operating Model, 12-Month Roadmap) with quality-gate self-assessment |
| Completeness | Covers the technical strategy comprehensively with architecture recommendations, SOC 2 mapping, platform champions program, and technology vendor recommendations | Additionally includes a platform product charter with user promise, explicit non-goals, lifecycle stage diagnosis (Step 0) with evidence, open/close decisions for the quarter, compounding flywheel loops with leading indicators, and AI-system-specific guardrails |
| Actionability | 4-phase roadmap (6-week increments) with deliverables per phase; success metrics table with current/6-month/12-month targets; "this week" immediate next steps | Surface inventory maps each capability to status (to build now/next), SLOs, consumers, and interface type; 3 investment gates with specific adoption signals that unlock additional resources; rollback/exit paths for each major risk |
| Specificity | Names specific technology options (MLflow, BentoML, Presidio, etc.) per category; platform champions program is a distinctive practical addition | Defines exact role-based access model (4 roles with specific capabilities), quota/limit policies, deprecation timelines (4-week notice, 2-release-cycle support), and versioning semantics for platform CLI and APIs |
| Quality gates | No self-assessment; mentions risk and mitigations | Includes quality-gate checklist across 7 dimensions plus a rubric self-assessment scoring 8 categories (scope clarity, platform-as-product, surface area, lifecycle, ecosystem, governance, AI defensibility, roadmap realism) |

## Key Differences

1. **Platform-as-product framing.** The skill-guided output treats the internal platform as a product with an explicit user promise ("Any ML engineer can take a validated model from experiment to monitored production in under 2 hours"), 5 non-goals, and 5 explicit assumptions. The baseline frames it as a strategy and architecture plan, which is thorough but does not adopt the product-thinking lens that clarifies what the platform is and is not.

2. **Lifecycle stage diagnosis.** The with-skill output explicitly diagnoses the platform as "Step 0 -- Conditions met" with 4 evidence points and prescribes what to do at this stage vs. what to avoid (premature marketplace thinking, building for hypothetical scale). The baseline proceeds directly to architecture recommendations without positioning the platform in a lifecycle framework.

3. **Open/close decisions.** The skill-guided output makes 3 explicit quarter-level decisions (standardize model packaging format, platform-managed tokenization for PII, opt-in then mandate adoption) with options evaluated, rationale, and risk mitigations for each. The baseline covers similar ground in its architecture sections but frames these as recommendations rather than explicit decisions with tradeoff analysis.

4. **Compounding loops with investment gates.** The with-skill output defines two flywheel loops (internal productivity, data governance) with measurable leading indicators and 3 investment gates that tie adoption signals to resource unlocks (e.g., "Gate 2: >50% paved-road adoption unlocks request for monitoring layer and part-time PM"). The baseline does not model compounding dynamics or formalize the relationship between adoption evidence and investment decisions.

5. **AI system defensibility section.** The skill-guided output includes a dedicated section on AI-system-specific concerns: context sources mapped by PII status, context storage and retrieval architecture, guardrails (least privilege, audit logs, human approval points), and evaluation/monitoring strategy. The baseline covers PII and compliance thoroughly but does not frame these through an AI-system-specific lens that addresses model lifecycle concerns.

## Verdict

The baseline provides a notably practical strategy with specific technology vendor recommendations and a platform champions program that the skill-guided output does not include. The skill-guided output is stronger as a strategic artifact: its platform-as-product framing, lifecycle stage diagnosis, explicit open/close decisions, compounding loop analysis, and investment gates create a more complete strategic foundation. For a 2-person platform team that needs to demonstrate value and earn investment, the investment-gate structure in the skill-guided output is particularly valuable.

## With Skill Output

<details>
<summary>Expand full output (~39k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~15k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
