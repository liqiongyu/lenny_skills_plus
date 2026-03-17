# Showcase: Building Sales Team

> Demonstrates the value of the `building-sales-team` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `building-sales-team`. We're seed-stage B2B SaaS. Founder has done 70 first meetings, closed 16, lost 40 (rest pending). Win rate ~23% (first meeting to closed-won). ACV $12k, cycle 30-45 days. We have 2,000 signups/month but upgrades are inconsistent. Budget: hire 2 AEs. Output: Sales Team Build Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Situational assessment, pre-hire groundwork, hiring plan, onboarding, lead allocation, sales process, tech stack, metrics, comp, expansion strategy, risks, timeline | Readiness gate with hire/no-hire decision, sales motion spec, team design with A/B plan, role scorecard, 6-stage interview loop with exercises, onboarding with coaching cadence, risks with mitigations, open questions, next steps |
| Completeness | Covers PQL definition, tech stack recommendations, comp/quota design, and expansion strategy | Covers readiness gate criteria, pricing guardrails, objection responses, interview scorecard with 1-5 anchors, and process-vs-person diagnostic framework |
| Actionability | Recommends completing closed-lost analysis and ICP refinement before hiring; provides a detailed 12-section plan | Provides a complete interview loop with mock discovery scoring rubric, pre-start checklist, day-by-day onboarding schedule, and weekly coaching sessions with specific agendas |
| Specificity | Comp benchmarks ($120-140k OTE), quota math ($600k ARR), PQL trigger examples, tech stack with pricing | At-bat definition (Stage 1 discovery completed), demo/pilot criteria with 14-day success metrics, pricing concession authority (AE vs. founder), and discovery call agenda with minute-by-minute breakdown |
| Quality gates | None explicit | 7-dimension checklist (readiness gate, motion spec, team design, scorecards, interview loop, onboarding, execution) plus 14/14 rubric score |

## Key Differences

1. **Readiness gate decision.** The skill output opens with an explicit hire/no-hire decision framework tied to specific metrics (70+ at-bats, 23% win rate, 30-45 day cycle) and states "hire now (pilot)" with rationale. The baseline argues for completing a closed-lost analysis before hiring, which is a valid alternative view -- it prioritizes diagnosis over speed.

2. **A/B test humans.** The skill output frames hiring two AEs simultaneously as an A/B test with comparable conditions (alternating lead assignment, identical onboarding), metrics to compare, and a diagnostic rule ("if both underperform, it's the process, not the reps"). The baseline recommends staggering hires to iterate on the playbook, which reduces risk but sacrifices the A/B learning advantage.

3. **Interview loop depth.** The skill output provides a 6-stage interview loop with 4 practical exercises (mock discovery, product deep-dive, written follow-up, coachability round), a 1-5 scoring rubric with anchored descriptions per dimension, and explicit hire/no-hire thresholds. The baseline describes a 5-stage process with reasonable structure but without scored rubrics or decision rules.

4. **Sales motion spec.** The skill output defines the complete sales motion: at-bat definition, stage exit criteria, first-meeting agenda with minute allocation, demo/pilot criteria, pricing guardrails with AE vs. founder authority, and a 5-objection response bank. The baseline recommends documenting the founder playbook but provides the framework rather than the content.

5. **Coaching and diagnostic cadence.** The skill output specifies a weekly coaching rhythm (Monday pipeline review, Wednesday call coaching, Friday experiment review) with a process-vs-person diagnostic framework. The baseline recommends weekly 1:1s and transitions the founder role over time but does not define the coaching session structure.

## Verdict

The skill output is more prescriptive and execution-ready -- a founder could follow it step by step from "hire decision" through "day 90 assessment" without additional planning. The baseline offers valuable strategic cautions (diagnose closed-lost before hiring, stagger hires, fix PQL pipeline first) that the skill output addresses but does not emphasize as strongly. The ideal approach combines the skill output's execution framework with the baseline's diagnostic caution about the 40 lost deals.

## With Skill Output

<details>
<summary>Expand full output (~34k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~16k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
