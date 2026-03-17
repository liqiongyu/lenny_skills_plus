# Showcase: Running Effective Meetings

> Demonstrates the value of the `running-effective-meetings` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `running-effective-meetings`. Design a 60-minute weekly product review meeting for a 12-person cross-functional team (PM, Eng leads, Design, Data, Marketing) at a Series B SaaS company. The current meeting devolves into status updates and runs over every week. The real need is to review metrics, make 1-2 decisions on experiment results, and surface blockers. Create a Meeting Pack with a meeting brief (purpose, attendees, decision owner), a pre-read template (metrics dashboard + decision memos), a timeboxed agenda, a facilitation script with transition cues, a notes + decision log template, and a follow-up email template with action items. Output: Meeting Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 6 sections + appendix: meeting brief, pre-read template, timeboxed agenda, facilitation script, notes + decision log, follow-up email, implementation playbook | 8-section canonical structure: meeting brief, pre-read template, timed agenda, facilitation script, notes + decision log, follow-up email, risks/open questions/next steps, and meeting hygiene recommendations |
| Completeness | All requested deliverables present; includes implementation playbook with week-by-week rollout and common failure modes table | All requested deliverables present; includes explicit Discover/Discuss/Decide separation framework, deep-dive off-ramp rule, and monthly hygiene retro design |
| Actionability | Facilitation script has word-for-word cues for each transition; implementation playbook covers weeks 0-4 and month 2+ with specific actions | Facilitation script has word-for-word cues plus "if stuck" branches for 6 specific scenarios (discussion stalls, new data introduced, someone repeats a point); off-ramp rule is non-negotiable |
| Specificity | Agenda allocates 18 min for decision #1 (3 present + 10 discuss + 5 decide) and 16 min for decision #2; pre-read due Monday EOD | Agenda allocates 18 min for decision #1 (1 present + 14 discuss + 3 decide) and 15 min for decision #2; pre-read has differentiated deadlines by role (Data by 10 AM, PMs by 10 AM, Eng by noon, all comments by 5 PM) |
| Quality gates | Meeting health check dimensions (5 items, rated 1-5) in the notes template; common failure modes table in appendix | 10-dimension rubric (20/20) plus 5-part checklist (meeting needed, pre-meeting, in-meeting, close-out, post-meeting); 5 identified risks with mitigations |

## Key Differences

1. **Discover/Discuss/Decide separation framework.** The skill output explicitly defines three phases (Discover = async pre-read, Discuss = live debate, Decide = live decisions) with a measurable target (67-75% of live time on discussion + decisions). The baseline achieves a similar structure in practice but does not name the framework or set a measurable threshold.

2. **Pre-read with differentiated role deadlines.** The with-skill output assigns different deadlines by role: Data Lead updates metrics by Monday 10 AM, PMs submit decision memos by Monday 10 AM, Eng Leads update the blocker log by noon, and all attendees add comments by 5 PM. The baseline uses a single Monday EOD deadline for the entire pre-read.

3. **Facilitation "if stuck" branches.** The skill output provides specific facilitator scripts for 6 scenarios: discussion stalls, someone introduces new data not in the pre-read, a topic goes off course, someone repeats a point, context questions that are answered in the pre-read, and the deep-dive off-ramp. The baseline provides transition cues and redirect scripts but with fewer scenario-specific branches.

4. **Decision numbering and traceability.** The baseline introduces a decision numbering convention (D-YYYY-WW-##) creating a searchable, persistent decision log. The skill output captures decisions with a simpler table format. Both are effective, but the baseline's numbering system is a notable operational detail.

5. **Implementation playbook.** The baseline includes a Week 0-Month 2+ implementation playbook with specific activities and a common failure modes table (7 modes with symptoms and fixes). The skill output addresses similar themes in its hygiene recommendations section but does not provide a phased rollout plan.

## Verdict

These two outputs are remarkably close in quality and completeness. The skill-guided output has a slight structural edge with its Discover/Discuss/Decide framework, differentiated deadlines, and more scenario-specific facilitation branches. The baseline has practical advantages in its implementation playbook, decision numbering system, and common failure modes table. Both would produce an effective meeting redesign. The skill output is better for a team that needs to understand the methodology behind the redesign; the baseline is better for a team that needs a step-by-step rollout guide.

## With Skill Output

<details>
<summary>Expand full output (~30k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~20k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
