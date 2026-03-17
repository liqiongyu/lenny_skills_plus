# Showcase: Post-Mortems Retrospectives

> Demonstrates the value of the `post-mortems-retrospectives` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `post-mortems-retrospectives`. Yesterday we had a 90-minute outage in our payments processing API that affected ~2,000 transactions. The root cause was a database migration that passed staging but failed in production due to a data volume difference (staging has 1% of prod data). The on-call engineer escalated after 30 minutes, but the incident commander role was unclear and the rollback playbook was outdated. Run a blameless postmortem and produce the full Pack: evidence-backed timeline, 5-whys contributing factors analysis, a systems-level root cause summary (not individual blame), an action tracker with owners and due dates, and a shareout plan for engineering + leadership. Output: Post-mortem Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 9-section blameless postmortem following a standard incident review format (executive summary, impact, timeline, 5-whys, root cause summary, action tracker, lessons learned, shareout plan, metadata) | 8-section Post-mortem Pack following a prescribed methodology (Retro Brief + Agenda, Facts + Timeline, Contributing Factors + Root Cause Hypotheses, Learnings + Decisions, Action Tracker, Kill Criteria/Triggers, Dissemination Plan, Risks/Open Questions) with quality-gate self-assessment |
| Completeness | Includes "what went well" and "where we got lucky" sections that provide balanced perspective; executive summary suitable for leadership consumption | Additionally includes a retro brief with explicit ground rules and pre-reads list, contributing factors clustered by category (Tech/Process/People/Comms/Environment) with "why it made sense at the time" column, and kill criteria with committed future actions if the same class of issue recurs |
| Actionability | Action tracker organized into immediate (1 week), short-term (30 days), and long-term (90 days) tiers with specific IDs, owners, due dates, and status tracking | Action tracker includes success signals and follow-up dates for each action; kill criteria define 5 observable signals with thresholds and pre-committed responses (e.g., "another production migration failure within 90 days -> halt all non-critical migrations") |
| Specificity | Timeline is more granular (2-minute increments in places) with evidence sources mapped to each entry; 5-whys analysis follows 2 threads with clear causal chains | Timeline explicitly labels each entry as "Fact" or "Hypothesis" to distinguish confirmed evidence from assumptions needing validation; contributing factors include a "why it made sense at the time" column that supports blameless analysis |
| Quality gates | No self-assessment; metadata section provides standard postmortem fields | Includes a rubric self-assessment scoring 6 dimensions (scope/safety, evidence quality, systems thinking, actionability, dissemination, kill criteria) plus a prep and output quality checklist |

## Key Differences

1. **Fact vs. hypothesis labeling.** The skill-guided output explicitly tags each timeline entry as "Fact" or "Hypothesis," making it clear which entries need further validation. This is methodologically important for a postmortem: it prevents the team from building corrective actions on unverified assumptions. The baseline provides evidence sources but does not distinguish confirmed facts from assumptions.

2. **Contributing factors with "why it made sense" framing.** The with-skill output clusters contributing factors by category (Tech, Process, People, Comms, Environment) and includes a column for "why it made sense at the time" -- reinforcing blameless analysis by contextualizing each factor. The baseline achieves blamelessness through its framing principles but does not structurally encode this perspective into the factor analysis.

3. **Kill criteria with pre-committed responses.** The skill-guided output defines 5 kill criteria -- observable future signals (e.g., "critical playbooks found outdated during an incident") with specific thresholds and pre-committed organizational responses (e.g., "freeze deploys for the affected system until playbook is updated"). The baseline does not include kill criteria, which means future recurrence would require a new analysis rather than triggering a pre-agreed action.

4. **Dissemination plan with recurring review.** The with-skill output includes a dissemination plan with a 1-page TL;DR shareout format and a biweekly "Impact & Learnings Review" ritual with specific agenda, attendees, and inputs. The baseline's shareout plan maps audiences to formats and dates but does not establish a recurring follow-up mechanism to track whether actions are completed.

5. **Balanced perspective sections.** The baseline includes "What Went Well" and "Where We Got Lucky" sections that provide valuable balance -- acknowledging that the monitoring fired promptly, no data was corrupted, and a senior engineer happened to be available. The skill-guided output focuses on what to fix and does not include these positive-signal sections, which can be important for team morale in a postmortem setting.

## Verdict

Both outputs produce high-quality blameless postmortems. The baseline is notably stronger in balanced framing (what went well, where we got lucky) and timeline granularity (2-minute increments with specific evidence sources). The skill-guided output adds methodological rigor through fact/hypothesis labeling, categorized contributing factors with "why it made sense" framing, kill criteria with pre-committed responses, and a recurring review cadence. For organizations looking to build a postmortem culture that prevents recurrence, the kill criteria and dissemination rituals in the skill-guided output are the most distinctive additions.

## With Skill Output

<details>
<summary>Expand full output (~27k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~14k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
