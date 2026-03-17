# Showcase: Running Decision Processes

> Demonstrates the value of the `running-decision-processes` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `running-decision-processes`. Decision: sunset Feature X. Deadline: March 15. Context: support load is rising and adoption is falling. Constraints: no downtime; must notify top customers 30 days prior. Stakeholders: PM, Eng, Support, Sales, Legal. Options: keep as-is, invest to fix, sunset. Output: Decision Process Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 10 sections plus appendices: problem statement, decision framework, stakeholder roles, meeting agenda, constraints, execution plan, risk register, success metrics, decision record, post-review checklist | 9-section canonical structure: decision brief/pre-read, options + criteria matrix, decision rights (DACI), meeting agenda with facilitation script, curiosity loop, decision log entry, decision communication (internal + external), decision review plan, and risks/open questions/next steps |
| Completeness | Covers options analysis, stakeholder mapping, execution timeline, risk register, communication templates, and post-sunset checklists; missing curiosity loop, explicit assumption tracking, and pre-filled decision log | Includes all the above plus curiosity loop (outreach message, 12 suggested participants, input capture table), 5 testable assumptions with validation plans, pre-filled decision log with revisit triggers, and 17 milestones with owners and dates |
| Actionability | Execution timeline has 10 milestones from T-45 to T+30; decision record template is blank (to be filled) | 17 milestones from March 3 to June 10 with specific owners; decision log is pre-filled with the recommended decision, rationale, tradeoffs, assumptions, and review metrics |
| Specificity | Options analysis uses assessment tables with qualitative pros/cons; success metrics have targets (100% notification, 0 downtime, <2% churn) | Options matrix uses weighted criteria (25% customer impact, 20% support cost, 20% eng opportunity cost, 15% strategic alignment, 10% execution risk, 10% reversibility) with analysis per option; 5 assumptions each with testable signals |
| Quality gates | Post-sunset checklist in appendix; escalation path for stakeholder disagreement | 5 checklists (decision process quality, anti-hesitation, explicit assumptions, curiosity loop, post-decision follow-through) plus rubric scoring (12/12) |

## Key Differences

1. **Curiosity loop for structured input gathering.** The skill output includes a complete curiosity loop: an outreach message template with 3 specific prompts, a list of 12 suggested participants with reasons for inclusion, and an input capture table for recording responses. The baseline identifies stakeholder roles and action items but does not provide a structured mechanism for gathering diverse input before the decision meeting.

2. **Explicit assumptions with testable signals.** The with-skill output names 5 key assumptions (A1-A5), labels each as testable or unknown, and provides specific validation plans (e.g., "survey/call top 10 customers before finalizing"). It also defines "what would trigger a revisit" conditions. The baseline lists data to gather in an appendix but does not frame assumptions as testable statements with validation plans.

3. **One-way door classification drives process intensity.** The skill output explicitly classifies the decision as a "one-way door" and calibrates the process intensity accordingly (standard-to-heavy), including veto rights for Legal and Eng Lead. The baseline recognizes the decision's significance but does not use a reversibility framework to calibrate the process design.

4. **Pre-filled decision log vs. blank template.** The skill output provides a fully pre-filled decision log entry (decision, rationale, tradeoffs accepted, 4 testable assumptions with metrics, revisit triggers, and 7 post-decision milestones with owners). The baseline provides a blank decision record template to be completed during the meeting, which requires more facilitation effort.

5. **Internal and external communication drafts.** The skill output includes both an internal Slack/email announcement and a personalized external customer notification with specific messaging guidance. The baseline includes a customer email template and communication plan but does not draft the internal announcement.

## Verdict

The skill-guided output is a more complete decision process system. Its curiosity loop, assumption tracking, and pre-filled decision log transform the pack from a meeting preparation document into an end-to-end decision governance framework. The baseline is well-organized and includes strong execution planning (especially the technical deprecation plan and post-sunset checklists) but requires the decision-maker to build several process components from scratch. The most significant gap in the baseline is the absence of structured pre-meeting input gathering and explicit assumption management.

## With Skill Output

<details>
<summary>Expand full output (~33k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~12k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
