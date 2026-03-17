# Showcase: Giving Presentations

> Demonstrates the value of the `giving-presentations` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `giving-presentations`. Create a 7-minute all-hands presentation: what we shipped this quarter, what's next, and what help we need from other teams. Audience is the whole company. I have bullets and a few metrics. Output: Presentation Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 8 slides in a standard presentation outline format with timing breakdown, tips, and a content-filling appendix | 7 sections following a presentation system: Brief, Narrative Outline (Contrast Spine), Slide-by-Slide with Talk Track, Q&A Bank, Stakeholder Pre-Brief Plan, Rehearsal + Delivery Plan, Risks/Next Steps |
| Completeness | Slide deck structure with timing, general tips, and a pre-presentation checklist | All slide content plus a narrative contrast table, 10 anticipated Q&A responses with proof and fallbacks, a stakeholder pre-brief plan with change log, and a 4-day rehearsal plan |
| Actionability | Slide templates with layout suggestions and speaker note prompts; appendix lists what to plug in | Speaker notes written as near-final scripts per slide; delivery cues for pauses, pacing, and eye contact; rehearsal plan with specific day-by-day activities |
| Specificity | General frameworks ("lead with impact, not process"); timing per slide | Contrast spine with "What Is" vs "What Could Be" columns; Q&A answers structured as short answer + proof + fallback; second-by-second time budget totaling 360 of 420 seconds |
| Quality gates | 6-item pre-presentation checklist | 6-category checklist plus 7-dimension rubric scoring 13/14 |

## Key Differences

1. **Narrative contrast spine.** The skill output builds the entire presentation around a "What Is / What Could Be" contrast: Q1 results and honest gaps versus Q2 outcomes achievable with cross-team support. This creates narrative tension and makes the asks feel earned rather than appended. The baseline provides a logical flow (shipped, next, needs) but without an explicit narrative arc.

2. **Q&A bank with structured responses.** The skill output prepares 10 likely questions, each with a short answer, supporting proof, an "if pressed" response, and a fallback commitment. Questions range from "Why should my team prioritize your ask?" to "What didn't you ship that was planned?" The baseline suggests preparing 1-sentence answers but does not provide a question bank.

3. **Stakeholder pre-brief plan.** The skill output includes a table of 4-5 stakeholders to brief before the all-hands (each ask-receiving team lead plus the exec sponsor), with their likely concerns and the goal of each pre-brief. It includes a change log template for tracking adjustments made based on pre-brief feedback. The baseline recommends sharing the deck 24 hours before but does not formalize pre-briefing.

4. **Rehearsal and delivery plan.** The skill output provides a 4-day rehearsal schedule (visualization, timed run #1, record-and-review, timed run #2, hard-mode Q&A role-play) with specific delivery cues: where to pause, when to slow down, and a "think up" reminder for Zoom. The baseline says "rehearse to time" and "run through at least twice" without a structured plan.

5. **Time budget with buffer analysis.** The skill output budgets each slide to the second (totaling 360 seconds of content with a 60-second buffer in a 420-second slot), explicitly noting the 14% buffer. The baseline provides per-slide timing that totals 6 minutes with 1 minute buffer, which is similar in outcome but less precisely managed.

## Verdict

The skill output treats the all-hands not as a slide deck to fill in but as a communication event to manage end-to-end: pre-briefs to prevent surprises, a narrative arc to earn the asks, rehearsals to nail the delivery, and Q&A prep to handle the aftermath. The baseline provides a solid, practical slide template that would get anyone to a decent presentation. The skill pack's value is in the 80% of presentation work that happens outside the slides.

## With Skill Output

<details>
<summary>Expand full output (~15k)</summary>

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
