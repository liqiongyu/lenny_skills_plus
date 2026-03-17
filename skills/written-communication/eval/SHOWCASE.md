# Showcase: Written Communication

> Demonstrates the value of the `written-communication` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `written-communication`. Artifact: email. Audience: exec stakeholders. Context: launch is slipping 2 weeks due to dependency delays. Ask: approve scope cut (drop Feature B) by Friday. Tone: direct, calm.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Email with TL;DR, Situation, Impact, Recommendation (with trade-off table), What I Need, Consequence of Inaction, Next Steps; followed by a "Notes on Approach" explainer | Eight-step communication pack: intake/artifact selection, outcome/ask sentence, actionable next steps, outline, draft email, clarity pass ("letter to yourself"), canonical doc check, quality gate with checklists and rubric |
| Completeness | Complete email draft with all essential elements; includes a trade-off comparison table and a meta-commentary explaining structural choices | Full process from intake through quality gate; includes the draft email plus surrounding methodology: what changes vs. what stays, dependencies/risks, canonical doc update recommendation, and post-decision logging template |
| Actionability | Email has numbered next steps (4 items) with owners implied; trade-off table enables quick decision comparison; includes offer-to-discuss close | Email has 5 numbered next steps with explicit owners and dates; post-decision next steps (Slack-ping nudge, canonical doc logging) extend beyond the email itself; "if I do not hear back" default action path removes ambiguity |
| Specificity | Revenue impact, team cost, and credibility risk called out in Impact section; Feature B affects ~15% of initial users; trade-off table compares "Feature B In" vs. "Feature B Out" across 4 factors | Fast-follow target specified (3 weeks post-launch); delay risk quantified (4+ weeks of uncertainty); next steps dated (Monday, next Wednesday, next Friday); response path specifies Thursday EOD for concerns vs. Friday EOD for approval |
| Quality gates | "Notes on Approach" section explains 8 structural decisions (TL;DR up front, consequence of inaction, tone choices) but no formal checklist | Universal checklist (9 items) + decision-request checklist (4 items) + six-dimension rubric scoring 12/12; clarity pass confirms the through-line; canonical doc check ensures the decision is logged |

## Key Differences

1. **Process vs. product.** The skill output delivers not just an email but a full communication workflow: intake brief, outcome sentence, "how" specification, structured outline, draft, clarity pass, and canonical doc check. This teaches the reader how to write effective exec communication, not just what to write. The baseline output delivers a polished email and explains its reasoning in a "Notes on Approach" section, but treats the email as a standalone artifact.

2. **Clarity pass and self-editing.** The skill output includes a "Letter to Yourself" step where the writer restates their message in plain internal language ("We hit a dependency delay. Feature B is blocked. The cleanest move is to cut it now.") and checks whether the draft matches this intent. The baseline output achieves the same clarity through careful writing but does not make the self-editing process visible or repeatable.

3. **Post-email follow-through.** The skill output extends beyond the email with a canonical doc check (recommending the decision be logged in the project doc with date and rationale), a Slack-ping nudge on Thursday if no reply, and a risks section addressing fast-follow feasibility and customer impact. The baseline output ends at the email signature, treating the communication as complete upon sending.

4. **Trade-off presentation.** The baseline output includes a comparison table ("Feature B In" vs. "Feature B Out") across four factors (launch date, revenue exposure, customer impact, engineering risk) with specific assessments. The skill output uses a simpler "changing vs. not changing" table. The baseline's trade-off table is more persuasive for an exec audience making a binary decision.

5. **Tone and persuasion craft.** The baseline output is arguably the stronger standalone email: it includes an "Impact" section with revenue/team/credibility framing, a "Consequence of Inaction" section that creates urgency, and an offer-to-discuss close. The skill output's email is more concise and procedural, optimizing for clarity over persuasion. Both maintain the requested direct, calm tone.

## Verdict

The skill-guided output's primary value is methodological: it provides a repeatable 8-step process for crafting exec communications, with quality gates that catch common failure modes (buried ask, missing deadline, no source-of-truth link). The baseline output produces a slightly more polished and persuasive standalone email, with a stronger impact framing and trade-off table. For a one-time email, the baseline may be more effective; for building an organizational capability in written communication, the skill output's process is more valuable.

## With Skill Output

<details>
<summary>Expand full output (~11k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~6k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
