# Showcase: Managing Timelines

> Demonstrates the value of the `managing-timelines` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `managing-timelines`. We're launching a new enterprise SSO integration at our B2B SaaS company at the AWS re:Invent conference on December 3. The project involves 2 backend engineers, 1 frontend engineer, 1 designer, and requires security review and SOC 2 documentation updates. We're 10 weeks out and haven't started the security review yet. Create a Timeline Management Pack with a milestone plan working backward from Dec 3, a RAG status cadence (weekly), scope control rules (what gets cut if we slip), stakeholder comms templates for Sales/Marketing/Execs, and escalation triggers for when to negotiate the date vs cut scope. Output: Timeline Management Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 5 sections: milestone plan (5 phases), RAG cadence, scope control rules, stakeholder comms templates (4 templates), and escalation triggers with risk watchlist | 8 sections: deadline + commitment model, phase plan with decision gates, milestone tracker + RAG, governance cadence, scope + change control, stakeholder comms pack (5 templates), escalation decision framework, and risks/open questions |
| Completeness | Covers all requested elements with a detailed milestone table, scope freeze rules, and pre-approved scope cuts | Covers all elements plus a commitment ladder (commit vs forecast vs target), explicit decision gates between phases, a "trade don't add" change control rule, and a structured escalation decision process |
| Actionability | Each milestone has an owner, due date, and deliverable; scope control includes 6 rules and 4 pre-approved cuts | Each milestone has owner, target date, confidence level, RAG status, dependencies, and notes; scope control includes an ordered cut list (cut first / cut next / never cut) with estimated time savings per item |
| Specificity | Detailed meeting cadence (daily standup, weekly status, bi-weekly stakeholder, weekly security sync, go/no-go review) with attendees and durations | Detailed governance with specific escalation trigger table (7 triggers with status and actions), a decision log template, and weekly review agenda with time allocations |
| Quality gates | No formal quality assessment | 10-dimension rubric scoring 18/18 with per-dimension notes |

## Key Differences

1. **Commitment ladder methodology.** The skill output introduces a three-tier commitment model (commitment, forecast, target) where early phases are committed and later phases remain forecasts until decision gates are passed. This prevents premature over-commitment. The baseline treats all milestones as equal, with no distinction between committed and forecasted dates.

2. **Decision gates between phases.** The skill version defines explicit gates between Discovery, Solutioning, Build, and Launch phases, each with specific criteria that must be true before proceeding. The baseline has a go/no-go meeting at Week 9 but no intermediate gates to catch problems earlier.

3. **Escalation decision framework.** The skill output provides a structured framework for when to cut scope vs. negotiate the date, with specific conditions for each (e.g., "Cut scope when the slip is 5 days or less and a cut-list item can absorb it" vs. "Negotiate the date when security review reveals P0 vulnerabilities requiring 2+ weeks of remediation"). The baseline has an escalation matrix with severity and response SLAs but no decision framework for the cut-vs-delay tradeoff.

4. **Stakeholder-specific comms templates.** The skill version provides five distinct templates (weekly update, Sales-specific, Marketing-specific, executive briefing, and escalation note), each tailored to the audience's needs and language. The baseline provides four templates (kickoff, escalation, go/no-go, post-launch) that are more milestone-oriented than audience-oriented.

5. **Ordered cut list with savings estimates.** The skill output pre-orders scope cuts from lowest to highest user impact, with specific time savings per item (e.g., "SCIM provisioning: saves ~1 week," "Google Workspace: saves ~3 days"). This makes the scope-cutting conversation actionable under pressure. The baseline lists pre-approved cuts but without quantified savings or a recommended cutting order.

## Verdict

Both outputs produce comprehensive, professional timeline management plans. The skill-guided version adds methodological rigor through its commitment ladder, phase gates, and structured escalation framework, which are particularly valuable for a high-stakes external deadline like a conference launch. The baseline is more prescriptive about meeting cadences and includes a useful critical-path warning section. Overall, the skill version better equips a PM to navigate the inevitable surprises of a complex, deadline-driven project.

## With Skill Output

<details>
<summary>Expand full output (~28k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~18k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
