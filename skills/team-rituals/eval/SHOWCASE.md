# Showcase: Team Rituals

> Demonstrates the value of the `team-rituals` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `team-rituals`. Remote cross-functional team (reduce chaos, increase decision velocity): - Team: 12 people (PM, Design, Eng, Data)

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 8-section document: core principles, rhythm of rituals (8 rituals), detailed ritual specs, communication norms, anti-chaos mechanisms, implementation plan, success metrics, common pitfalls | 7-step pack: context snapshot + outcome definition, ritual inventory audit (keep/change/kill), design rules + time budget, golden rituals shortlist (5 rituals), full ritual specs with templates, onboarding primer + rollout plan, governance plan + quality gate |
| Completeness | Covers 8 rituals including cross-functional pair syncs, random coffee chats, and a monthly strategy review; adds communication norms (response times, DRI framework, documentation standards) and anti-chaos mechanisms | Covers 5 rituals with greater depth per ritual: full copy-paste templates, anti-pattern + fix pairs (2-3 per ritual), async fallback for every sync ritual, explicit decision rules, and a governance plan with retirement criteria |
| Actionability | Provides detailed moderator scripts for each ritual and a 4-phase implementation plan; communication norms table with response-time expectations is immediately adoptable | Provides complete copy-paste templates (agenda + notes format) for every ritual, a phased rollout plan (weeks 0-6), and a "Known by First Friday" onboarding primer that a new hire could use on day one |
| Specificity | Names specific tools (Donut for Slack, Miro, FigJam); sets meeting-hour caps; proposes standing pair syncs (PM+Design Monday, Design+Eng Tuesday, etc.) | Names each ritual with memorable alliterative names (Monday Map, Decision Drop, Async Daily Pulse, Retro Rewind, Demo & Donuts); calculates exact time budget (2h50m vs 4h cap); maps each ritual to specific outcomes |
| Quality gates | 7 success metrics with targets (decision cycle time <5 days, async completion >90%, retro action completion >80%); common pitfalls section with 6 anti-patterns | 6-dimension rubric self-score; quarterly ritual review with keep/change/kill criteria and retirement rules; hard cap of 7 rituals max; annual reset mechanism |

## Key Differences

1. **Ritual inventory audit before design.** The skill output starts by auditing the team's probable existing rituals (7 items) with explicit keep/change/kill decisions and rationale, establishing a net reduction in meeting load (killing 2 status meetings, saving ~2.5 hrs/week). The baseline designs rituals from scratch without accounting for what exists, which could lead to additive meeting burden.

2. **Template completeness.** The skill output provides full, copy-paste-ready Markdown templates for every ritual (Monday Map, Decision Drop log, Retro Rewind, Demo & Donuts, Daily Pulse Slack message). The baseline describes each ritual with agendas and scripts but doesn't provide ready-to-use artifact templates, requiring the team to create their own.

3. **Anti-pattern + fix pairs.** The skill output identifies 2-3 specific anti-patterns per ritual with corresponding fixes (e.g., Monday Map becomes a status meeting -- fix: facilitator redirects with "That's in the doc -- what decision or trade-off do you need?"). The baseline lists 6 common pitfalls at the end but doesn't tie them to specific rituals.

4. **Governance and ritual lifecycle.** The skill output includes a quarterly ritual review process with explicit keep/change/kill criteria (participation >75%, team rating 3+/5), retirement rules (archiving, communication), and a hard cap of 7 rituals to prevent sprawl. The baseline mentions quarterly auditing as a pitfall to avoid but doesn't provide the governance structure.

5. **Scope breadth.** The baseline covers more ground: 8 rituals including cross-functional pair syncs, random coffee chats, and a monthly strategy review; communication norms with response-time expectations; and 5 anti-chaos mechanisms (two-pizza rule, 24-hour decision expiry, office hours, no-meeting blocks, "propose don't ask" norm). The skill output is narrower (5 rituals) but deeper per ritual.

## Verdict

The skill-guided output is the stronger operational system for a team implementing ritual changes: the inventory audit, copy-paste templates, anti-pattern playbook, and governance mechanism make it adoptable with minimal additional work. The baseline provides a broader toolkit of practices (especially the communication norms, anti-chaos mechanisms, and pair syncs) that a more mature team could layer on top. For a 12-person team starting from chaos, the skill output's focused, governable system is more likely to stick.

## With Skill Output

<details>
<summary>Expand full output (~42k)</summary>

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
