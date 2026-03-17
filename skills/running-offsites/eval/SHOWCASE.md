# Showcase: Running Offsites

> Demonstrates the value of the `running-offsites` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Plan a 1-day strategy offsite for a 10-person product team (remote-first). We need to decide Q2 priorities and reset working agreements. Budget is moderate; location is NYC. Output the full Offsite Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 10 sections: goals, logistics, pre-work, detailed agenda, facilitation notes, outputs/follow-up, budget, risk mitigation, packing list, communication templates | 8-section canonical structure: intake + boundary check, offsite brief (1-pager), format recommendation, agenda + session output map, prework pack, facilitation run-of-show, logistics plan + checklist, and post-offsite output pack |
| Completeness | Detailed agenda with 14 session blocks, facilitation notes (energy management, dominant voices), venue options, restaurant recommendations, pre/post email templates, packing list | Boundary check, offsite brief with 5 target outputs and success measures (immediate + 2-4 weeks), format recommendation with rationale, session-level facilitation scripts with disagreement protocol, decision capture protocol (6 fields), 7 contingency plans, and 3 review checkpoints |
| Actionability | Pre-work has 3 reflection prompts; agenda has time blocks with goals; follow-up cadence spans Day+2 through Q2 end | Prework has 5 prompts plus top-3 bet submissions with deadlines; each agenda session has explicit input, output artifact, and facilitator; follow-up has 10 action items with owners and dates |
| Specificity | Working agreements template requires agreements to be specific, observable, and revisable; commitment ritual includes personal commitment sharing | Decision principles session includes stress-testing against 2-3 scenarios; convergence session explicitly applies principles to bets before voting; anti-bets (explicit no-gos) are a required output |
| Quality gates | Risk mitigation table (7 risks) | 10-criterion rubric (20/20) plus 6-part checklist (brief, agenda, prework, facilitation, logistics, post-offsite); 5 risks with mitigations; 6 open questions |

## Key Differences

1. **Boundary check and format recommendation.** The skill output opens with a boundary check (is an offsite appropriate for these goals?) and provides a format recommendation with rationale (laptops-down whiteboard day chosen over retreat or hybrid formats). The baseline proceeds directly to planning without assessing whether an offsite is the right intervention.

2. **Decision principles before priority-setting.** The with-skill output schedules a Decision Principles session (10:45-11:30) before the Q2 bets divergence session, so the team has agreed-upon criteria for evaluating priorities before they start debating them. The baseline runs the Q1 retrospective and then moves directly into priority generation without establishing decision criteria first.

3. **Anti-bets as a required output.** The skill output explicitly requires the team to define 3-5 "anti-bets" (things they are NOT doing in Q2) as a separate session output during convergence. The baseline does not produce explicit anti-bets, which means the team may leave without clarity on what they said no to.

4. **Decision capture protocol with 6 fields.** The skill output specifies a structured decision capture format (decision, rationale, tradeoffs accepted, owner, next step + date, review trigger/date) that the scribe uses for every decision throughout the day. The baseline captures decisions in a simpler format (priority list with owners) without documenting tradeoffs or review triggers.

5. **Contingency plans.** The skill output provides 7 specific contingency plans (key person absent, venue falls through, energy crash, heated debate, prework not done, AV failure, bad weather for walk). The baseline has a risk mitigation table with 7 items but at a higher level of abstraction.

## Verdict

The skill-guided output is a more methodologically rigorous offsite plan, with its boundary check, decision principles framework, anti-bets output, and structured decision capture. The baseline is a more practical event-planning document, with venue recommendations, restaurant suggestions, a packing list, and communication templates that are immediately useful for logistics. The key structural difference is that the skill output designs the offsite around producing specific artifacts (5 target outputs, each traceable to a session), while the baseline designs it around running productive sessions. Both approaches work; the skill output better ensures the offsite produces durable decisions.

## With Skill Output

<details>
<summary>Expand full output (~41k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~23k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
