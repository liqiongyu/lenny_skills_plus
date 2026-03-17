# Showcase: Launch Marketing

> Demonstrates the value of the `launch-marketing` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `launch-marketing`. We're launching a developer tool (private beta to waitlist). Goal: 1,000 waitlist signups in 14 days. Audience: platform engineers at mid-size SaaS companies. Constraints: no customer logos, only product screenshots + demo. Channels: PR, LinkedIn, founder network, community. Output: Launch Marketing Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Linear plan organized by phases (pre-launch, launch week, sustained push) with channel-specific strategies and a budget section | 8-section pack: context snapshot, launch brief, motion + sequencing, channel plan, PR outreach kit, asset checklist, internal readiness kit, and measurement + experiment plan |
| Completeness | Comprehensive tactical playbook with daily targets, budget allocation, and post-campaign steps but no internal readiness kit, FAQ, or formal go/no-go criteria | Includes all tactical elements plus an internal readiness kit (30-second talk track, FAQ, objections, escalation paths), day-of runbook with backup plans, and a 7-experiment backlog with explicit "double down" and "cut" rules |
| Actionability | Highly tactical with specific daily signup targets (Day 1: 150, Day 5: 100 for PH, etc.) and channel-specific signup goals adding to 1,000 | Equally tactical with a sequenced timeline, but adds go/no-go criteria before launch, explicit decision rules for budget reallocation, and experiment-level success thresholds |
| Specificity | Provides concrete budget allocation ($3-5K), daily signup projections, and channel-by-channel expected impact | Provides UTM plan per channel, experiment hypotheses with measurable thresholds, and a complete pitch email draft for PR exclusive |
| Quality gates | No formal quality check; relies on implicit completeness | Full 6-category checklist (brief, PR, channel, internal readiness, measurement, day-of) plus a 7-dimension rubric scoring 14/14 |

## Key Differences

1. **Message architecture vs. tactical playbook.** The skill output begins with a structured launch brief that defines the core message ("steak"), four hook options with rationale for selection, and audience segments with tailored message angles. The baseline jumps directly into channel tactics and asset lists, assuming the messaging is self-evident.

2. **Internal readiness and team enablement.** The skill version includes a complete internal readiness kit with a 30-second talk track, 10-item FAQ, 5 objection-and-response pairs, known limitations/guardrails, escalation paths, and a day-of runbook. The baseline has no equivalent, which means team members fielding questions on launch day would be improvising.

3. **Experimentation framework.** The skill output defines 7 structured experiments with hypotheses, success thresholds, and explicit "double down" (3x average signup rate) and "cut" (<10 signups after 72 hours) rules. The baseline includes decision rules but they are less systematic and lack per-experiment structure.

4. **PR strategy depth.** The skill version provides a complete PR outreach kit with an exclusive decision and rationale, a full pitch email draft, a follow-up email, a press blurb, and a timeline with fallback plan. The baseline lists target outlets and a pitch structure but does not draft the actual emails.

5. **Assumptions and TBDs made explicit.** The skill output systematically labels every unknown (product name, value proposition, team owners, pricing) as a TBD and lists 10 open questions. The baseline assumes many of these are resolved, which could lead to gaps during execution.

## Verdict

The baseline produces a strong, action-oriented launch plan with daily targets and budget math. The skill-guided output matches that tactical depth while adding substantial strategic scaffolding: a message framework, internal readiness kit, structured experimentation plan, and complete PR outreach drafts. For a team executing their first major launch, the skill version significantly reduces the risk of miscommunication, misalignment, and wasted effort.

## With Skill Output

<details>
<summary>Expand full output (~36k)</summary>

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
