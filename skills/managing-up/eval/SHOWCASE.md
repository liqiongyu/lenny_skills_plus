# Showcase: Managing Up

> Demonstrates the value of the `managing-up` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `managing-up`. I just started as a Senior PM reporting to a VP of Product who manages 8 PMs and is known for changing priorities frequently. We're 3 weeks into a quarterly roadmap and she's already suggested pivoting to a different initiative twice. I need a system to manage up effectively: understand her decision-making style, keep her informed without overwhelming her, and push back on priority changes constructively. Create a Managing Up Operating System Pack with a manager profile template (filled in with what I know), a weekly async update format optimized for a context-switching exec, a trade-off memo template for escalating priority conflicts, and a 4-week pilot cadence for establishing the relationship. Output: Managing Up Operating System Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 6 parts: manager profile template, weekly update format, trade-off memo, 4-week pilot, pilot scorecard, and quick-reference phrases appendix | 10 sections: context snapshot, manager profile, communication cadence map, weekly update template with filled example, trade-off memo template, escalation triggers + ask ladder, working agreement + boundary scripts, influence/seat-at-the-table plan, 4-week pilot cadence, and risks/open questions |
| Completeness | Covers all requested elements thoroughly; adds a pilot scorecard and quick-reference phrases for common situations | Covers all elements plus a communication channel architecture, a 5-level "ask ladder," leader leverage map, boundary scripts for 5 specific situations, an influence plan with target forums and pre-wire loops, and formal risks/open questions |
| Actionability | 4-week pilot has day-by-day actions per week; weekly update template is well-structured with explicit guidelines | 4-week pilot has action tables per week with specific deliverables; weekly update includes a filled-in example showing exactly how to use it; working agreement includes specific commitments with proposed cadence |
| Specificity | Manager profile includes hypothesis tracking table and 3 behavioral hypotheses about the VP's patterns | Manager profile includes validation questions for the next 1:1, common failure mode predictions, and 3 specific commitments; the influence plan names target forums and defines success signals |
| Quality gates | Pilot scorecard with 7 dimensions and a grading scale (30-35 points = working; below 20 = misalignment) | Full checklist (9 items) plus a 5-dimension rubric scoring 24/25 |

## Key Differences

1. **Communication channel architecture.** The skill output defines a "what goes where" map specifying four channels (async weekly update, 1:1, trade-off memo, urgent escalation) with explicit rules for what does and does not belong in each. It also explains the design rationale for a context-switching exec. The baseline provides a weekly update format and trade-off memo but does not systematically map communication channels.

2. **Ask ladder and leader leverage map.** The skill version introduces a 5-level ask ladder (FYI, Nudge, Unblock, Sponsor, Decision) with example language for each, plus a leader leverage map showing what the VP can uniquely do and how to request it. The baseline addresses escalation through the trade-off memo but does not provide a graduated framework for different types of asks.

3. **Boundary scripts for priority-change situations.** The skill output provides 5 specific scripts for common scenarios: VP suggests a pivot mid-sprint, VP suggests a second pivot before resolving the first, urgency is inflated, scope creeps, and insufficient prep time. Each script is 2-3 sentences of ready-to-use language. The baseline includes quick-reference phrases but they are more general.

4. **Influence and seat-at-the-table plan.** The skill version includes a 30-day plan for moving from "new PM executing a roadmap" to "PM who helps the VP make better priority decisions," with specific tactics (weekly strategic observations, pre-wire loops, QBR contributions) and success signals. The baseline does not address the influence dimension.

5. **Working agreement with reciprocal commitments.** The skill output proposes a working agreement where the PM commits to specific behaviors (weekly updates by 10am, trade-off memos within 24 hours) and asks the VP for reciprocal commitments (48-hour decision turnaround, context with pivot suggestions). The baseline captures similar ideas but does not frame them as a formal bilateral agreement.

## Verdict

The baseline produces a well-structured, practical system with a strong pilot scorecard and useful quick-reference phrases. The skill-guided version builds on this foundation with significantly more depth in communication design (channel map, ask ladder), boundary-setting (5 scenario-specific scripts), and strategic influence (30-day plan with pre-wiring and forum targeting). For a new PM navigating a complex relationship with a high-context-switching VP, the skill version provides a more complete operating system.

## With Skill Output

<details>
<summary>Expand full output (~32k)</summary>

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
