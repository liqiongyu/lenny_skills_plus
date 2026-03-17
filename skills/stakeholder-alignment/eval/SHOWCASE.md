# Showcase: Stakeholder Alignment

> Demonstrates the value of the `stakeholder-alignment` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `stakeholder-alignment`. We need exec alignment to pause our new analytics dashboard feature (6 weeks into a 12-week build) to address a critical reliability issue: our core data pipeline has had 3 outages in the past month, causing customer escalations from 2 enterprise accounts worth $400k ARR combined. The CTO is concerned about engineering morale from context-switching, the CRO is worried about the Q3 pipeline impact of delaying the dashboard (it was promised to 5 prospects), and the CEO wants a recommendation by Friday. Create a Stakeholder Alignment Pack with an alignment brief, a stakeholder map capturing each exec's principles and evidence preferences, a pre-brief sequence plan (who to talk to first), a 30-minute decision meeting plan, and a follow-up comms draft. Output: Stakeholder Alignment Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 5-section document: alignment brief (SCR format), stakeholder map, pre-brief sequence, 30-minute meeting plan, follow-up comms (4 drafts: exec email, eng announcement, customer outreach, prospect guidance) | 7-section pack: alignment brief (1-pager), stakeholder map with "how they think" notes, alignment plan with pre-brief sequence + timeline, pre-brief notes templates, decision meeting plan with evaluation criteria, decision summary + comms draft, risks/open questions/next steps |
| Completeness | Covers the full arc from brief to meeting to follow-up; includes 4 ready-to-send communication drafts for different audiences | Covers the same arc plus adds: pre-brief notes templates with "eyes lit up / dead eyes" signal capture, options scored against weighted criteria, change log for tracking what shifts after pre-briefs, and a "what would trigger a revisit" clause |
| Actionability | Strong on communication templates -- the engineering team announcement and customer outreach drafts are ready to adapt and send | Strong on meeting design -- evaluation criteria mapped to stakeholder principles, facilitation notes for specific objection scenarios, and a live decision-capture template |
| Specificity | Stakeholder map includes detailed win conditions, influence approaches, and specific objection handling per exec; phased plan with tiger team model | Stakeholder map includes decision principles ("how they think"), evidence preferences per person, and a "silent veto / surprise risks" section identifying overlooked stakeholders (PM, Board) |
| Quality gates | Risk register and decision log template in appendix | Full 7-dimension checklist + rubric self-score; pre-brief change log to track how the brief evolves through conversations |

## Key Differences

1. **Decision principles vs. stakeholder profiles.** The skill output extracts cross-stakeholder decision principles (5 named principles like "don't ship broken things" and "one clear priority for engineering") and uses them to design evaluation criteria for the meeting. The baseline profiles each stakeholder thoroughly but doesn't synthesize the principles into a shared evaluation framework for the decision itself.

2. **Pre-brief as a structured feedback loop.** The skill output provides per-stakeholder pre-brief notes templates with fields for "what landed," "dead eyes moments," verbatim quotes, and commitments secured, plus a change log to track how the alignment brief evolves. The baseline describes the pre-brief sequence and conversation framework well but treats it as a one-way communication rather than a structured learning process.

3. **Meeting facilitation design.** The skill output includes specific facilitation notes for predictable objection scenarios ("if the CRO pushes for Option 2," "if the CTO raises morale concerns") with prepared responses anchored to the vital question. The baseline also handles objections but embeds them in general facilitation notes rather than tying each to a specific evaluation criterion.

4. **Communication drafts breadth.** The baseline provides 4 fully drafted communications (exec summary, engineering announcement, customer outreach, prospect guidance) that are nearly ready to send. The skill output provides a single comprehensive decision summary with owners and dates but doesn't draft the engineering or customer communications in the same detail.

5. **Silent veto identification.** The skill output explicitly calls out two potential surprise stakeholders (the dashboard PM whose project is being paused, and board/investors who may have Q3 expectations) and recommends addressing them before Friday. The baseline does not surface these latent risks.

## Verdict

Both outputs demonstrate sophisticated stakeholder management thinking. The skill-guided output is stronger on decision architecture -- extracting principles, designing evaluation criteria, and building a feedback loop through pre-briefs. The baseline is stronger on communication execution -- providing polished, audience-specific drafts that could be sent with minimal editing. For the stated goal (getting a decision by Friday), the skill output's structured decision-making machinery is the more valuable contribution, while the baseline's communication templates would complement it well.

## With Skill Output

<details>
<summary>Expand full output (~33k)</summary>

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
