# Showcase: Running Effective 1:1s

> Demonstrates the value of the `running-effective-1-1s` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `running-effective-1-1s`. I'm a new product lead managing 5 direct reports (3 PMs, 1 designer, 1 data analyst) across PST and EST time zones. Two reports are senior and low-maintenance, one is a new hire (week 3), one is struggling with prioritization, and one just got passed over for promotion. My calendar is already at 85% utilization. Design a 1:1 Operating System Pack with a tiered cadence plan (not everyone needs weekly), a shared 1:1 doc template, a coaching question bank organized by situation type, a career conversation plan for the passed-over report, and a 4-week pilot schedule. Output: 1:1 Operating System Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 6 sections: team assessment + cadence, shared doc template, coaching question bank, career conversation plan (8-week), 4-week pilot, operating principles | 8-section canonical structure: intake + context snapshot, purpose + "what goes where" map, tiered cadence plan, shared doc template, coaching toolkit with decision tree, career conversation plan (4-phase), wellbeing/recovery + special situations, and quality gate + pilot schedule |
| Completeness | 3-tier cadence plan, doc template with private manager notes, question bank (8 categories, ~80 questions), 8-week career recovery plan, 4-week pilot with weekly retrospective prompts | Tiered cadence with barbell approach (relationship catch-ups + urgent topicals), doc template with working agreements, 7-category question bank (~50 questions) with coaching script, 4-phase career plan with dedicated listening session, wellbeing check-in pattern, 3 special-situation playbooks, and full pilot schedule |
| Actionability | 4-week pilot has day-by-day schedules with focus areas per report; post-pilot decision matrix for tier transitions | 4-week pilot has day-by-day schedules with specific session types (listening session, life story, future dreams, action plan); pilot review questions on 8 dimensions |
| Specificity | Career plan spans 8 weeks with weekly goals, manager prep items, and growth plan template with gap analysis; includes promotion narrative building | Career plan has 4 dedicated 45-60 min sessions across 4 weeks; listening session has a minute-by-minute agenda with critical guidelines (don't promise, don't minimize); growth bet table with practice loops |
| Quality gates | Success metrics table (7 signals with healthy/warning indicators); 6 operating principles with anti-patterns | 6-part quality checklist (pack completeness, 1:1 system quality, coaching quality, career development, wellbeing/safety, skip-level) plus rubric (30/30); boundary checks for escalation |

## Key Differences

1. **"What goes where" map and anti-pattern guard.** The skill output explicitly maps 5 communication channels (async, team standup, standing 1:1, urgent topical, career conversation) with their topics and cadences, plus an anti-pattern guard ("Could this be a Slack message?"). The baseline addresses the status-update trap in operating principles but does not provide a formal channel-routing map.

2. **Coaching decision tree with directive-mode exceptions.** The with-skill output includes a coach-vs-advisor decision tree that specifies 5 conditions for switching to directive mode (safety, legal, time-critical, repeated pattern, new hire lacking context) and a 6-step coaching conversation script. The baseline provides coaching questions and principles ("coaching over solving") but does not formalize when to stop coaching and give the answer.

3. **Wellbeing check-in pattern with escalation boundaries.** The skill output includes a structured wellbeing check-in (energy 1-10, joy, biggest drain, activation), specific manager behavioral activations (adjust scope, protect calendar), and explicit escalation rules (EAP referral language, "you are not a therapist" boundary). The baseline does not include a wellbeing protocol or escalation guidance.

4. **Special-situation playbooks.** The skill output provides 3 special-situation playbooks: post-crisis listening session (60 min, no-laptop format with a listening-first script), urgent topical meeting (trigger, SLA, format), and skip-level template (for future use). The baseline does not address crisis or urgent meeting scenarios.

5. **Career conversation as dedicated sessions vs. embedded plan.** The skill output separates career conversations into dedicated 45-60 minute sessions (listening, life story, future dreams, career action plan) that are distinct from standing 1:1s and cannot be "squeezed into the last 10 minutes." The baseline embeds career work into the first 15 minutes of regular 1:1s during weeks 4-6 of the recovery plan, which may compete with tactical topics.

## Verdict

Both outputs are comprehensive 1:1 operating systems. The baseline is notably strong, with a deeper career recovery plan (8 weeks with promotion narrative building) and more coaching questions (~80 vs ~50). The skill-guided output excels in system design: the channel-routing map, coaching decision tree, wellbeing protocol, and special-situation playbooks create a more resilient operating system that handles edge cases and prevents common failure modes. The outputs are complementary -- a practitioner would benefit from the baseline's depth of coaching questions combined with the skill output's structural guardrails.

## With Skill Output

<details>
<summary>Expand full output (~38k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~33k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
