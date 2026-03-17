# Showcase: Personal Productivity

> Demonstrates the value of the `personal-productivity` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> I'm a product lead with 25-30 hours/week of meetings and I advise a startup. Build me a personal productivity system that protects deep work and stops tasks from slipping.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 10-section advice guide covering time architecture, task capture, meeting hygiene, weekly review, advisory management, communication protocols, tools, habits, and red flags | 8-section system pack following a diagnostic methodology (Context Snapshot, Commitment Inventory, Weekly Timebox Plan, Capture + To-Do System Spec, Daily Plan + Shutdown Ritual, Weekly Review Ritual, 7-Day Rollout Plan, Risks/Open Questions) |
| Completeness | Covers all major productivity areas with practical advice; includes advisory work management as a separate section and "saying no" scripts | Produces a complete system with explicit constraints analysis, hour-by-hour default week calendar, copy-paste checklists for daily shutdown and weekly review, and a staged 7-day rollout with specific daily tasks and success criteria |
| Actionability | Provides general frameworks ("block deep work time," "batch Slack/email") with suggested weekly layout but leaves specific implementation to the user | Prescribes exact time blocks (e.g., "Mon 9:00-11:30 FOCUS"), concrete booking rules to share with the team (25/50 minute defaults, agenda required, 24-hour lead time), and a weekend spillover hard cap with an explicit escalation trigger |
| Specificity | Advisory work gets its own section with sensible advice; tools section recommends specific products; "red flags" section is a useful addition | Quantifies the constraint problem (25-30 hours meetings + advising = 10-20 hours remaining, much fragmented); defines 3 measurable success signals (dropped tasks per week, deep-work blocks completed, weekend hours); includes specific "if X for 2 consecutive weeks then Y" adjustment rules |
| Quality gates | No self-assessment; notes that the system is "deliberately low-tech and low-overhead" | Includes a full quality-gate checklist across 5 dimensions (inputs completeness, timebox plan, capture/to-do, rituals, testability) plus a rubric self-score |

## Key Differences

1. **Diagnostic before prescription.** The skill-guided output begins with a context snapshot that identifies explicit constraints (25-30 hours of meetings, advising commitment), flags unknowns (meeting distribution, energy patterns, current tools), and calculates the available time budget. The baseline jumps directly to recommendations without diagnosing the specific constraint landscape.

2. **Measurable success signals.** The with-skill output defines 3 concrete, time-bound success signals: dropped tasks per week (target: 0-1), deep-work blocks completed per week (target: 3+), and weekend work (target: zero or one 2-hour block). The baseline mentions "red flags to watch for" but frames them as qualitative warning signs rather than measurable targets.

3. **Copy-paste ritual checklists.** The skill-guided output provides literal copy-paste checklists for both the daily shutdown ritual (6 steps, ~13 minutes) and the weekly review (13 steps, ~35 minutes) with precise time budgets for each section. The baseline provides review checklists but without the step-level time estimates or the copy-paste formatting.

4. **Staged rollout plan.** The with-skill output includes a 7-day rollout plan that introduces one practice per day (Day 1: inbox setup, Day 2: list creation, Day 3: shutdown ritual, etc.) with specific "what to measure" for each day and Week 1 success criteria. The baseline provides a 6-item quick-start list but expects all changes to begin in the first two days.

5. **Adjustment triggers.** The skill-guided output defines explicit "if X for 2 consecutive weeks, then Y" rules: if dropped tasks exceed 2 for two weeks, fix the capture system; if deep-work blocks fall below 3 for two weeks, renegotiate meeting load; if weekend work exceeds the cap for two weeks, have a workload conversation. The baseline notes red flags but does not pre-commit to specific corrective actions.

## Verdict

The baseline provides solid, broadly applicable productivity advice that covers more surface area (communication protocols, "saying no" scripts, tool recommendations). The skill-guided output is significantly more prescriptive and testable: it diagnoses constraints quantitatively, produces an hour-by-hour default calendar, defines measurable success signals, and stages adoption over 7 days with built-in adjustment triggers. For someone who needs a system they can implement tomorrow and evaluate in two weeks, the skill-guided output is substantially more actionable.

## With Skill Output

<details>
<summary>Expand full output (~27k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~9k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
