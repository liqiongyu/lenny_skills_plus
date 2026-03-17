# Showcase: Writing Job Descriptions

> Demonstrates the value of the `writing-job-descriptions` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `writing-job-descriptions`. Write a job description for a founding Product Designer at a seed-stage B2B AI startup (6 people, $3M raised) building an AI-powered contract review tool for legal teams. The designer will be the first design hire, working directly with the CEO (former lawyer) and 3 engineers. They need to ship end-to-end (research through pixel-perfect UI) in high ambiguity with no design system yet. Include 12-month success outcomes, a clear design-major spike (information-dense UI + legal workflow), an honest 'what's hard here' section (no design peers, fast pace, ambiguous requirements), and filters that self-select wrong-fit candidates out. Create both a role scorecard and a public job posting. Output: Job Description Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Three-part pack: internal scorecard (detailed), public posting, and appendix with sourcing strategy/red flags | Seven-section pack: context snapshot, role scorecard with 30/60/90, competency spike map with anti-signals, public JD, filters summary, iteration plan with version log, risks/open questions/next steps |
| Completeness | Covers 10 competencies with weights, knockout criteria, anti-patterns, interview process with design exercise prompt, sourcing strategy, and compensation benchmarking | Covers 6 outcomes, 3 spikes (1 major + 2 minor) with evidence criteria, public JD with all sections, self-selection filters, iteration triggers tied to specific JD sections, and quality gate checklist |
| Actionability | Scorecard provides 1-5 rating dimensions and minimum thresholds; interview stages have evaluators and focus areas; sourcing strategy names specific companies to recruit from | Iteration plan specifies what to test (attract/filter/alignment), which JD section to adjust, and how to detect failure; next steps have numbered action items; quality gate provides pass/fail checklists |
| Specificity | 12-month outcomes broken into quarterly milestones with measurable targets (20% improvement in task completion, SUS score of 75+, 30+ research sessions); compensation range with equity specifics | 12-month outcomes are outcome-based with evidence/artifacts and metrics; spike map includes "what strong looks like" and "common anti-signals" columns; 30/60/90 sketch is concise and milestone-driven |
| Quality gates | No formal quality gate or checklist | Six checklists (role clarity, 12-month outcomes, spike specificity, high-signal filtering, inclusivity/compliance, iteration readiness) plus a six-dimension rubric self-score |

## Key Differences

1. **Spike map methodology.** The skill output uses a formal major/minor spike framework, identifying one major spike (information-dense UI for expert users) and two minor spikes (end-to-end product design, domain curiosity), each with "what strong looks like," evidence criteria, and anti-signals. The baseline output lists 10 competencies with weights (Critical/High/Medium), which is more granular but less sharply differentiated for screening.

2. **Self-selection filtering depth.** Both outputs include "who should not apply" sections that are candid and specific. The skill output additionally includes a "What's Hard Here" section with 7 specific hard-truth statements and a "Who Will Thrive Here" section with 6 positive signals, creating a two-sided filter. The baseline output achieves a similar effect with 6 "should not apply" items and an honest "What's hard here" section.

3. **Iteration and learning system.** The skill output includes a dedicated iteration plan with a signal-to-section mapping (e.g., "low volume of applicants with information-dense experience" maps to adjusting the opening paragraphs), review triggers (after 15 applications or 5 portfolio reviews), and a version log template. The baseline output does not include an iteration framework, treating the JD as a final artifact rather than a living document.

4. **Internal vs. external separation.** The baseline output more clearly separates the internal scorecard (with knockout criteria, anti-patterns, and hiring manager notes) from the public posting, and includes a sourcing strategy appendix naming specific target companies (Palantir, Everlaw, Bloomberg). The skill output has an internal context snapshot and scorecard but blends more of the internal guidance into the public JD structure.

5. **Compensation and logistics transparency.** Both outputs include compensation ranges and equity details in the public posting. The baseline output provides slightly more specificity on equity (0.5%-1.25%, common stock) and benefits (including dollar amounts for learning budget and home office stipend). The skill output notes the range needs CEO confirmation and flags it as an open question.

## Verdict

Both outputs produce high-quality job description packs that would attract the right candidates. The skill-guided output excels at providing a repeatable methodology -- the spike map framework, iteration triggers, and quality gate checklist make it a system for writing JDs, not just a single JD. The baseline output excels at practical hiring execution -- the detailed competency scorecard, sourcing strategy with named target companies, and red-flag patterns give a hiring manager more immediately actionable tools for evaluating candidates.

## With Skill Output

<details>
<summary>Expand full output (~31k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~21k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
