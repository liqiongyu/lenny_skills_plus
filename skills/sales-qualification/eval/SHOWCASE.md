# Showcase: Sales Qualification

> Demonstrates the value of the `sales-qualification` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `sales-qualification`. We sell B2B SaaS to operations teams at 50-500 employee companies. Inbound is high volume, but AEs say meetings are low quality. ACV $12k, cycle ~45 days. We have SDRs qualifying and handing off to AEs. Output: Sales Qualification Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Linear sections covering diagnosis, ICP, framework, handoff, lead scoring, disqualification, comp, feedback, channel analysis, and implementation | 7-section pack with context snapshot, qualification charter, weighted scorecard, call script, CRM artifacts, rollout plan, and risks/open questions |
| Completeness | Covers broad ground including lead scoring, comp alignment, and channel quality analysis, but lacks a unified scoring mechanism and CRM enforcement | Complete end-to-end system: ICP segments with triggers, hard disqualifiers, weighted scorecard with must-pass criteria, CRM templates, pipeline hygiene rules, and rollout plan |
| Actionability | Provides BANT+ criteria and handoff brief template but scoring is binary (4/5 = book, 3/5 = nurture); no weighted prioritization | Highly actionable: 7-criterion weighted scorecard with 0-3 anchors, threshold math (accept/nurture/reject), 3 worked scoring examples, and copy-paste CRM note template |
| Specificity | Uses generic BANT framework adapted for the scenario; lead scoring model uses arbitrary point values without calibration data | Tailored to the $12k ACV / SDR-to-AE motion: 15-20 min call script mapped to scorecard criteria, specific disqualifier detection windows (e.g., "first 2 minutes"), and max stage ages |
| Quality gates | No self-assessment; no explicit quality checks on the qualification system itself | Full 8-item checklist + 7-dimension rubric self-score; includes pipeline hygiene rules with automated enforcement triggers |

## Key Differences

1. **Scoring precision and calibration.** The skill output produces a 7-criterion weighted scorecard with concrete 0-3 anchors (not vague labels) and three fully worked scoring examples showing accept, nurture, and reject outcomes. The baseline uses a simpler 4-of-5-met threshold that doesn't distinguish between strong and weak signals within each criterion.

2. **Operational CRM integration.** The skill output includes a structured CRM notes template with specific required fields, stage exit criteria, and "no next step, no stage" enforcement rules. The baseline provides a handoff brief template but lacks the pipeline hygiene rules and automated enforcement mechanisms that prevent deals from stalling invisibly.

3. **Disqualification rigor.** The skill output defines 6 hard disqualifiers with specific detection windows ("minutes 5-8") and a graceful close-out talk track, plus nurture triggers for re-engagement. The baseline lists disqualifiers but treats them as static rules without timing guidance or re-engagement protocols.

4. **Call script design.** The skill output maps every question block directly to scorecard criteria with explicit disqualifier checkpoints throughout the call flow. The baseline provides 5 standalone discovery questions without connecting them to the scoring mechanism or building in decision points during the conversation.

5. **Rollout and iteration planning.** The skill output includes a 2-week day-by-day rollout plan with calibration sessions, live call reviews, and an explicit iteration loop after 20-30 calls. The baseline proposes a 90-day implementation plan that is broader but less prescriptive about calibration and inter-rater consistency.

## Verdict

Both outputs are substantive and demonstrate strong domain knowledge. The skill-guided output is meaningfully superior in operational precision: it produces a tighter, more integrated system where the scorecard, call script, CRM artifacts, and pipeline rules all reinforce each other. The baseline covers more peripheral topics (comp alignment, channel analysis, lead scoring) but lacks the internal consistency and calibration mechanisms that make a qualification system work in practice.

## With Skill Output

<details>
<summary>Expand full output (~34k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~17k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
