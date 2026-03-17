# Showcase: Conducting User Interviews

> Demonstrates the value of the `conducting-user-interviews` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> I'm a PM for a B2B SaaS product. Our activation rate dropped after we changed onboarding. I need to run 8 interviews with new trial users this week. Create a recruiting plan, screener, and a 45-minute discovery interview guide. Recording is allowed.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 3 parts (recruiting, screener, interview guide) with a post-interview debrief table and synthesis framework | 7 sections (context snapshot, recruiting + screener, interview guide + consent, note-taking template + tagging, synthesis report template, follow-up plan, risks/open questions/next steps) |
| Completeness | Covers recruiting, screener, interview guide, and a basic synthesis framework; missing structured note-taking and follow-up plan | Full end-to-end research operation: recruiting with outreach copy, screener, consent script, story-moment note-taking template, tagging scheme, synthesis report template, thank-you/panel plan, and risk mitigations |
| Actionability | Provides a section-by-section guide with probes and a post-interview debrief table; synthesis is a brief 4-point framework | Story-moment capture template with fields for triggers, goals, workarounds, and verbatim quotes; hypothesis-tracking in each debrief; synthesis template with evidence thresholds ("2+ interviews or labeled single anecdote") |
| Specificity | 18 questions across 6 sections with probes; includes a useful 1-10 ease rating; recruiting email template with incentive recommendations | 15 questions focused on story elicitation with moderator notes for handling common response patterns; outreach copy differentiated for activated vs. non-activated users; explicit recency requirements |
| Quality gates | No self-assessment | Full quality gate checklist (7 categories) plus rubric scoring 4.6/5 average |

## Key Differences

1. **Decision-anchored framing.** The skill output opens with a context snapshot that names the specific decision (fix, revert, or redesign onboarding by end of next week), three explicit hypotheses, and a "what will we do differently" statement. The baseline describes the goal but does not frame the research around a time-bounded decision.

2. **Story-first interview methodology.** The skill output structures the core 20 minutes around a single narrative thread ("Walk me through step by step") with follow-up probes, plus moderator notes for handling generic answers, feature requests, and overly positive responses. The baseline uses a more traditional section-by-section approach with more individual questions, which risks fragmenting the user's natural story.

3. **Structured evidence capture.** The skill output provides a note-taking template with story-moment fields (trigger, goal, steps taken, struggles, workarounds, verbatim quotes) and a 12-tag coding scheme. The baseline provides a simpler debrief table. The skill's approach makes cross-interview synthesis significantly easier.

4. **Hypothesis tracking across interviews.** The skill output's debrief template includes a section to update each hypothesis (supported/weakened/unchanged) after every interview, creating a running evidence tracker. The baseline has no mechanism to track how evidence accumulates across sessions.

5. **Participant follow-up and panel building.** The skill output includes a thank-you email template, a customer panel recruitment plan with cadence rules, and explicit guidance on sharing back what changed because of participant input. The baseline does not address post-interview relationship management.

## Verdict

The skill output delivers a complete user research operating system -- from recruiting through synthesis and follow-up -- designed for a PM who needs to run a tight research sprint and make a decision at the end. The baseline provides a solid interview guide that would work well for an experienced researcher, but the skill pack's structured note-taking, hypothesis tracking, and synthesis templates make it more reliable for teams running research under time pressure.

## With Skill Output

<details>
<summary>Expand full output (~27k)</summary>

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
