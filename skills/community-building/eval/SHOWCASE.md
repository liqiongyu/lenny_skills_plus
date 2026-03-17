# Showcase: Community Building

> Demonstrates the value of the `community-building` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `community-building`. Product: open-source observability SDK for TypeScript. ICP: senior full-stack engineers at 10-200 person SaaS startups. Goal: accelerate activation and word-of-mouth adoption. We're considering Discord as our home base, with GitHub Discussions as a secondary channel. Resources: 1 community lead (10 hrs/week), 2 engineer SMEs (2 hrs/week each), $500/month budget. We have 400 GitHub stars and an email list of 1,200 developers. Create a Community Building Pack with a platform plan, member journey map, 6-week programming calendar, ambassador program v1, and governance/moderation rules. Output: Community Building Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Platform plan, member journey map, 6-week calendar, ambassador program, governance/moderation, appendix with metrics | Context snapshot with success metrics, member lifecycle with personas, activation rituals, seed cohort strategy, 6-week calendar with week themes, ambassador program with selection rubric, governance with escalation ladder, measurement plan with health indicators |
| Completeness | Discord channel architecture, GitHub Discussions categories, budget allocation, CoC, moderation escalation ladder | Adds "first win" definition with 14-day target, seed cohort strategy (hand-picked 15-20 members), activation rituals (show-and-tell, office hours, "first trace" challenge), knowledge base seeding plan, and friction audits |
| Actionability | Day-by-day calendar for 6 weeks with specific activities, owners, and channels; recurring weekly cadence defined | Each ritual has a facilitator guide with prompts, activation has a step-by-step flow (join -> DM -> intro post -> first win -> role badge), and the seed cohort has specific outreach templates |
| Specificity | Ambassador criteria (3 of 5 must-haves), monthly activity menu with time estimates, benefits including conference reimbursement | Primary success metric defined numerically (50% of seed cohort complete "first win" within 14 days), member-generated content target (3+ unique members/week by week 6), referral signal (10%+ cite friend as join source by week 8) |
| Quality gates | 6-week and 90-day metric targets in appendix | Health indicators mapped to community lifecycle stages, friction audit at week 4, "community energy" qualitative check, and explicit adapt/kill criteria for programs |

## Key Differences

1. **Activation-first design.** The skill output defines a specific "first win" (ship a working alert or trace and share a screenshot) with a 14-day completion target, and designs the entire community around driving members to that moment. The baseline defines a 5-stage journey map (Discoverer through Evangelist) with clear touchpoints but does not anchor the community design around a single measurable activation event.

2. **Seed cohort strategy.** The skill output includes a detailed plan for hand-picking 15-20 seed members, onboarding them before public launch, and using them to establish norms and generate initial content. The baseline launches publicly from week 1, which is faster but risks an empty-room feeling if early members do not engage.

3. **Ritual facilitator guides.** The skill output provides facilitator guides for key rituals (show-and-tell, office hours) with specific prompts, time allocations, and what "good" looks like. The baseline specifies activities and owners on a daily calendar but does not include facilitation scripts.

4. **Governance depth.** The baseline provides a more detailed governance section with a 6-level moderation escalation ladder, content guidelines per channel type, a decision-making framework (minor/moderate/major), and emergency procedures (raid, security disclosure, moderator misconduct). The skill output covers governance but with less procedural detail.

5. **Budget and tooling specificity.** The baseline provides a line-item budget breakdown ($500/month across 5 categories) and a tech stack recommendation (Discord bots, community analytics tools). The skill output allocates the budget at a higher level and focuses more on community programs than tooling infrastructure.

## Verdict

The skill output is stronger on community strategy -- its activation-first design, seed cohort approach, and measurable "first win" metric create a focused growth engine. The baseline is stronger on community operations -- its detailed channel architecture, governance procedures, budget allocation, and ambassador program mechanics provide the infrastructure to run a community day-to-day. A community lead would benefit from the skill output's strategic framework combined with the baseline's operational playbook.

## With Skill Output

<details>
<summary>Expand full output (~45k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~25k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
