# Showcase: Content Marketing

> Demonstrates the value of the `content-marketing` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `content-marketing`. Product: payroll automation for multi-state restaurants. ICP: finance ops managers at 20-200 locations. Goal: increase qualified demo requests from organic search by 20% in 10 weeks. Constraints: 1 marketer, 1 SME (tax), compliance review needed. Output: a Content Marketing Plan Pack with a demand-validated topic map, 6-week calendar, and 3 briefs.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 7 parts: topic map with 4 clusters and 14 topics, 6-week calendar with daily tasks, 3 briefs with SEO specs, measurement framework, risk mitigation, and production workflow | 11 sections: context snapshot, content market fit brief (anxieties/JTBD/myths), channel + voice strategy, demand-validated topic map with "to validate" separation, prioritized backlog with scoring, 6-week editorial calendar, 3 content briefs, flagship draft outline, AI content SOP, measurement plan with decision rules, risks/open questions/next steps |
| Completeness | Strong tactical execution plan with 14 topics, daily task breakdowns, and detailed SEO specs per brief; includes internal linking strategy and production workflow appendix | Adds audience psychology layer (anxieties, JTBD, myths, objections), voice rules ("say this / not that"), explicit demand validation separation (approved vs. to-validate topics), AI content SOP, and measurement decision rules |
| Actionability | Calendar breaks down to daily tasks per person per week; briefs include complete SEO specs and word counts; production workflow defines a 5-day per-article cycle | Calendar includes review dates and compliance sign-off windows; briefs include "information gain" commitments and fact/claim check lists; measurement plan has if/then decision rules for content performance |
| Specificity | Provides estimated search volumes, keyword difficulty scores, and specific SERP targets for all 14 topics; briefs include URL slugs and meta descriptions | Topics cite demand evidence sources (autocomplete patterns, competitor pages) rather than estimated volumes; briefs require 2+ "information gain" commitments (artifacts, teardowns, original data) to differentiate from existing SERP content |
| Quality gates | No self-assessment | Full quality gate checklist (10 items) plus rubric scoring 12/12 |

## Key Differences

1. **Audience psychology vs. keyword-first planning.** The skill output starts with a Content Market Fit Brief that maps ICP anxieties, jobs-to-be-done, misconceptions, and objections before any topic planning. The baseline starts with keyword research and search volumes. The skill's approach ensures content addresses real buyer psychology, not just search demand.

2. **Demand validation rigor.** The skill output separates topics into "Approved SEO" (with documented demand signals) and "To Validate" (with concrete next steps and deadlines). The baseline lists all 14 topics with estimated search volumes but does not distinguish between validated and speculative demand.

3. **Information gain as a content standard.** Every skill brief requires 2+ specific "information gain" commitments: original frameworks, concrete examples/teardowns, reusable artifacts, or unique data. The baseline provides thorough outlines but without an explicit differentiation standard against existing SERP content.

4. **AI content governance.** The skill output includes a dedicated AI-Assisted Content SOP with allowed/disallowed uses, mandatory human review gates, and a versioning workflow (v0 AI draft through v3 compliance-approved). The baseline includes a production workflow but does not address AI-specific quality controls.

5. **Measurement decision rules.** The skill output provides explicit if/then decision rules (e.g., "if a piece ranks 11-20 after 3 weeks, refresh and add depth"). The baseline includes measurement targets and a Week 4 decision gate but without the granular decision rules for individual content pieces.

## Verdict

Both outputs are strong, production-ready content marketing plans. The baseline excels in tactical detail (daily tasks, SEO specifications, production workflow). The skill pack adds strategic layers -- audience psychology, demand validation discipline, information gain standards, and AI governance -- that make the plan more durable and defensible. For a 1-marketer team with compliance constraints, the skill output's structured review gates and decision rules provide more guardrails against common content marketing pitfalls.

## With Skill Output

<details>
<summary>Expand full output (~46k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~31k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
