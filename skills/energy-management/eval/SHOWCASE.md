# Showcase: Energy Management

> Demonstrates the value of the `energy-management` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `energy-management`. A product leader is in back-to-back meetings and feels constant decision fatigue.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 6-part framework (Diagnosis, Framework, Tactics, Longer-term, Emergency, Metrics) organized as a general guide | 8 numbered sections following a personal operating-system format: Context Snapshot through Risks/Next Steps, tailored to the specific leader |
| Completeness | Covers energy theory, calendar tactics, delegation principles, renewal rituals, and success metrics | All of the above plus a full energy drivers/drains map, calendar audit with time-bucket math, a default week schedule, delegation briefs with escalation triggers, and a 2-week experiment tracker |
| Actionability | Offers general advice ("implement time blocking") with a monthly metric table | Provides a day-by-day default week, 4 named experiments each with keep/modify/stop decision rules, a daily tracking table, and a stakeholder boundary message ready to copy-paste |
| Specificity | References generic energy zones and a 3-month rollout plan | Calculates specific hours (zone-of-genius from 15% to 35%), names 5 top offenders with deletion/redesign plans, and estimates 8-10 hrs/week recovery |
| Quality gates | Monthly self-assessment with 6 metrics (1-10 scale) | Checklist covering 5 categories (pack completeness, actionability, energy-quality, measurement, safety) plus a rubric self-score of 10/10 |

## Key Differences

1. **Personalized diagnosis vs. general framework.** The skill output creates a specific energy drivers/drains map with 5 drivers and 8 drains, each with controllability assessment and concrete levers. The baseline identifies 5 root causes at a conceptual level without mapping them to the individual's calendar.

2. **Calendar redesign with real constraints.** The skill output builds a full default week around non-negotiable meetings (Tue 10AM leadership, Thu 2PM hiring committee) and the 5:30PM caregiving hard stop. The baseline provides a generic time-block template that does not account for specific constraints.

3. **Experiment tracker with decision rules.** The skill output defines 4 experiments (async status meetings, 25/50-min defaults, decision office hours, Wednesday no-meeting morning), each with a hypothesis, specific measures, and a keep/modify/stop rule at day 14. The baseline suggests monthly audits but lacks structured experimentation.

4. **Delegation briefs with guardrails.** The skill output includes 2 detailed delegation briefs (cross-team sync, hiring logistics) with decision rights, escalation triggers, and review cadence. The baseline describes a "70% rule" for delegation but provides no specific handoff documentation.

5. **Low-energy-day protocol.** The skill output includes a "Minimum Viable Day" protocol with a copy-paste stakeholder message and explicit recovery actions. The baseline has an "Emergency Protocol" section but it focuses on crisis days rather than sustainable low-energy management.

## Verdict

The skill output transforms a generic energy-management problem into a personal operating system with scheduled experiments, measurable targets, and ready-to-use artifacts (stakeholder message, delegation briefs, daily tracker). The baseline provides sound principles and a solid long-term plan, but requires significant additional work to translate into action. The skill pack's main advantage is turning advice into a system.

## With Skill Output

<details>
<summary>Expand full output (~13k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~7k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
