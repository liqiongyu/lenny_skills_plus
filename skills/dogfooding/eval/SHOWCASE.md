# Showcase: Dogfooding

> Demonstrates the value of the `dogfooding` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `dogfooding`. We're building an AI-powered meeting notes tool for remote teams. The core workflow is: join meeting -> auto-record -> generate summary -> extract action items -> share to Slack/Notion. Set up a 2-week dogfooding sprint where our 8-person product team uses the tool for every internal meeting (standup, 1:1s, planning). Each PM must share at least 3 meeting summaries/week externally with stakeholders. Environment: production app, real meetings, Slack integration. Create a Dogfooding Pack with scenario map, daily routines, creator commitments, a log + triage board spec in Linear, a weekly report template, and a ship/no-ship gate. Output: Dogfooding Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 7 sections organized by topic (scenarios, routines, reporting); reasonable flow but loosely connected | 8 numbered sections following a strict workflow (Context Snapshot through Ship Gate) with cross-references between sections |
| Completeness | Covers scenarios, routines, commitments, logging, triage, reporting, and ship gate; adds appendices with calendar and survey | All required deliverables plus a Dogfooding Charter, explicit success criteria, severity scale, triage rules, and a quality self-assessment |
| Actionability | Provides templates and checklists but many fields are generic placeholders | Every field ties to a specific scenario, step, and owner; creator commitments have precise tracking mechanisms |
| Specificity | 10 stress-test scenarios plus 5 integration scenarios; detailed log schema with 23 fields | 6 focused end-to-end scenarios with explicit edge cases; log schema maps each issue to a scenario and step |
| Quality gates | 12 mandatory pass criteria plus 7 soft criteria with a decision flowchart | 10 gate criteria with a decision matrix (ship / ship-with-known-issues / no-ship) and explicit evidence requirements |

## Key Differences

1. **Structured methodology vs. broad coverage.** The skill output follows a deliberate progression from context snapshot through ship gate, where each section builds on the previous one. The baseline covers more ground (10 scenarios, 5 integrations, an end-of-sprint survey) but the sections are more loosely coupled.

2. **Creator commitments with accountability.** The skill output defines a dedicated Slack channel for external shares, requires PMs to self-report editing status, and tracks stakeholder feedback per share. The baseline lists commitments in a table but lacks the granular tracking and accountability loop.

3. **Severity scale with triage rules.** The skill output provides a 4-level severity scale (S0-S3) with explicit triage rules such as "data going to the wrong place is automatically S0." The baseline uses P0-P3 with time-based response SLAs but fewer decision rules for classification.

4. **Ship gate decision framework.** The skill output maps gate outcomes to specific actions (extend sprint, investigate root causes) with clear thresholds. The baseline uses a more elaborate flowchart (Ship / Conditional Ship / No-Ship) but the criteria are more numerous and potentially harder to evaluate cleanly.

5. **Quality self-assessment.** The skill output includes a rubric self-score and checklist verification against its own reference materials, making the pack auditable. The baseline has no self-assessment mechanism.

## Verdict

Both outputs are strong and comprehensive. The skill output excels at internal consistency -- every scenario links to the charter, every log entry maps to a scenario, and the ship gate directly references the success criteria. The baseline is broader (more scenarios, more integrations, an end-of-sprint survey) but lacks the tight connective tissue. For a team that needs a ready-to-execute pack, the skill output is more immediately actionable.

## With Skill Output

<details>
<summary>Expand full output (~17k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~19k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
