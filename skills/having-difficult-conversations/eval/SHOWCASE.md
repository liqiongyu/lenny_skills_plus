# Showcase: Having Difficult Conversations

> Demonstrates the value of the `having-difficult-conversations` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `having-difficult-conversations`. I'm an Engineering Manager with a senior engineer who has missed 3 consecutive sprint commitments, shows up late to standups, and has started pushing back on code review feedback from peers. The team morale is suffering and two other engineers have mentioned it to me privately. I need to have a direct performance conversation this week. The engineer was a top performer 6 months ago and I suspect burnout or personal issues. Prepare a Difficult Conversation Pack with an evidence-based conversation brief, a talk track/script (direct but empathetic), a plan for handling defensiveness or emotional reactions, and a follow-up note template with a 4-week improvement plan and check-in schedule. Output: Difficult Conversation Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 6-section format covering talk track, defensiveness handling, follow-up note, quick-reference card, and additional considerations | 7-section pack with conversation brief, message map, full talk track, objection/emotion handling table, follow-up note, documentation note, and risks/open questions |
| Completeness | Covers core elements but lacks a formal conversation brief, documentation template, and explicit quality gate | Includes every requested artifact plus a documentation note for manager records, explicit non-negotiables, and a self-assessment rubric scoring 4.83/5 |
| Actionability | Provides a usable script with good inline coaching ("stop talking, count to 10") and a follow-up template with a 4-week plan | Delivers calendar-ready artifacts: a conversation brief with pre-meeting prep, a message map spine, word-for-word scripts with pauses, and a structured follow-up with measurable weekly milestones |
| Specificity | Good use of the scenario details (Sprints 14-16, specific behaviors) with helpful follow-up table | Deeply scenario-specific with 3 time-bounded examples, explicit "what good looks like" expectations, support menu, boundaries with consequences, and risks/sensitivities section |
| Quality gates | No formal quality checks or self-assessment | Full checklist (prep, script, follow-up) plus a 6-dimension rubric with scores and a pass/fail threshold |

## Key Differences

1. **Systematic conversation architecture.** The skill output separates the conversation into a brief (context, facts, expectations), a message map (conversational spine), and a full talk track. This three-layer structure lets the manager prepare at different altitudes -- strategic (brief), structural (map), and tactical (script) -- whereas the baseline merges everything into a single narrative flow.

2. **Objection handling as a decision matrix.** The skill version provides a 6-row table mapping likely reactions (shock, defensiveness, anger, sadness, disclosure, negotiation) to specific response moves, exact language, and explicit anti-patterns. The baseline covers defensiveness and emotions in prose, which is helpful but harder to reference in the moment.

3. **Documentation and legal-awareness.** The skill output includes a separate documentation note template for manager records (participants, facts discussed, agreements, employee response) and flags HR briefing as a pre-conversation action item. The baseline mentions documentation in passing but provides no template or process.

4. **Explicit risk analysis and open questions.** The skill version dedicates a full section to risks (root cause unknown, perception of unfairness, flight risk, team dynamics) and open questions that could change the plan. The baseline addresses some of these inline but lacks a structured risk register.

5. **Quality gate and self-assessment.** The skill output includes a multi-dimension rubric with numerical scores and a pass/fail threshold, which serves as both a quality check and a teaching tool. The baseline has no equivalent mechanism for evaluating the output's completeness.

## Verdict

Both outputs are competent and usable, but the skill-guided version is significantly more thorough and operationally ready. Its layered architecture (brief, map, script), structured objection-handling matrix, documentation template, and quality gate transform a good conversation guide into a complete management toolkit. The baseline provides solid advice but requires more manager judgment to fill structural gaps.

## With Skill Output

<details>
<summary>Expand full output (~27k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~15k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
