# Showcase: Building Team Culture

> Demonstrates the value of the `building-team-culture` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `building-team-culture`. I'm a new Head of Product joining a fully remote product team of 12 (3 PMs, 4 designers, 5 researchers) across US and EU time zones at a Series B developer tools company. Culture feels low-trust: decisions get relitigated in Slack after meetings, people avoid giving candid feedback in retros, and two senior ICs are checked out. I want to build psychological safety and faster decision-making within 8 weeks. Create a culture snapshot, a culture code with 5 principles and explicit behaviors, decision-making and meeting norms, a 30/60/90 rollout plan, and a measurement plan with pulse questions. Output: Team Culture Operating System Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Diagnosis, guiding principles, 8-week plan, anti-patterns, success metrics, weekly cadence | Culture snapshot with behavior-reward analysis, 5-principle culture code with do/don't/decision rules/anti-patterns/signals, team norms, rituals map, 30/60/90 rollout plan, measurement plan with 6 leading indicators and 6 pulse questions, risks/open questions/next steps |
| Completeness | Covers listening tour, decision framework, IC re-engagement, psychological safety, working agreement, health check | Adds behavior-reward evidence table, sacred cows to examine, explicit escalation norms, cross-function problem-framing ritual, hiring/onboarding hooks, recognition/reward integration, and quarterly culture retro |
| Actionability | Week-by-week activities with clear goals; retro redesign with anonymous pre-survey | Each principle has observable signals (healthy vs. anti-pattern), rituals map specifies purpose/cadence/owner/agenda/outputs, listening tour includes 7 specific prompts, rollout plan has dated milestones |
| Specificity | DACI framework with decision doc template; 8 success metrics with numeric targets | DRI model with 24-hour documentation rule, Slack thread >10 messages rule, 4-business-hour response SLA, and per-principle decision rules (e.g., "if a PM wants to skip research input, document the tradeoff and get sign-off") |
| Quality gates | Health check survey questions at week 8 | 6 leading indicators tracked continuously, 6 monthly pulse questions mapped to specific principles, trigger-based intervention (score <3.0 triggers focused retro), versioned culture code with changelog |

## Key Differences

1. **Behavior-reward analysis.** The skill output includes an evidence table analyzing what behaviors are currently rewarded and punished (e.g., "meeting decisions are punished/undermined; Slack behavior is rewarded"), creating a diagnostic foundation for the culture code. The baseline identifies symptoms and root causes effectively but does not frame them through a reward/punishment lens.

2. **Principle depth.** Each of the skill output's 5 principles includes do/don't lists, decision rules for edge cases, named anti-patterns, and observable healthy signals. The baseline's 5 guiding principles are stated concisely and then operationalized through the weekly plan, but the principles themselves lack the same depth of behavioral specification.

3. **Cross-function equity.** The skill output dedicates a full principle ("Every Function Is a Partner, Not a Service Desk") to ensuring PMs, designers, and researchers have equal standing, with specific decision rules about when functions can be bypassed. The baseline addresses this indirectly through role-based onboarding paths and inclusive meeting practices.

4. **Measurement sophistication.** The skill output defines 6 leading indicators (decision cycle time, relitigating rate, retro action completion, WIP demo participation, cross-function involvement, pulse response rate) with 8-week targets, plus 6 pulse questions each mapped to a specific principle. The baseline uses a health check survey with 6 questions and qualitative targets, which is simpler but less trackable over time.

5. **Sustainability hooks.** The skill output includes hiring interview questions aligned to culture principles, onboarding additions (culture code walkthrough, WIP demo attendance, cross-function 1:1s), and a quarterly culture retro for evolving the code. The baseline coaches direct reports to cascade norms but does not define hiring or onboarding integration.

## Verdict

The skill output is a more complete operating system -- the culture code, norms, rituals, and measurement plan form an interconnected system that can sustain and evolve beyond the initial 8 weeks. The baseline is a strong coaching playbook for a new leader, particularly good on the human dynamics of re-engaging checked-out ICs and building informal connection in remote teams. The skill output's main advantage is that it creates artifacts (culture code, decision log, pulse surveys) that persist after the initial transformation period.

## With Skill Output

<details>
<summary>Expand full output (~37k)</summary>

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
