# Showcase: Delegating Work

> Demonstrates the value of the `delegating-work` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `delegating-work`. Delegate "Improve onboarding activation" to a PM in 6 weeks.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 13 sections: overview, objective, background, scope, success criteria, authority, resources, 6-week plan, communication, risk, feedback/growth, handoff checklist, post-initiative wrap-up | 8 steps following a deliberate delegation workflow: frame the delegation, pick owner + autonomy level, context handoff pack, decision rights + guardrails, owner-led plan, execution cadence, review plan, debrief plan, plus risks/open questions/next steps |
| Completeness | Covers scope, resources, weekly plan, communication, risk, and a growth/development plan; success criteria use placeholder variables (X%, Y%, Z%) | Fills assumed values where user did not provide them (baseline ~30%, target +5pp), includes prior decision rationale (Q3 tooltip experiment killed), known gotchas (bot traffic in funnel data), and example outputs ("what good looks like") |
| Actionability | 6-week plan with weekly activities and deliverables; weekly check-ins and escalation protocol defined | Decision rights table per area (research approach: PM decides; scope changes: PM recommends, manager approves); 4 scheduled review points with specific artifacts and quality criteria; debrief agenda with "what worked/what didn't" structure |
| Specificity | Resources listed with bracket placeholders ([X] engineers, [Designer name]); authority section uses general categories | Autonomy level explicitly set to "Decide with guardrails" with a decision-area-by-decision-area table; escalation triggers are specific thresholds (timeline > 1 week, spend > $500, auth flow changes); prior decisions cited with rationale |
| Quality gates | No self-assessment | Full quality gate (2 checklists: delegation quality + anti-micromanagement) plus rubric scoring 12/12 |

## Key Differences

1. **Explicit autonomy calibration.** The skill output defines a specific autonomy level ("Decide with guardrails") and maps it to a decision-area table showing exactly what the PM can decide independently vs. what requires escalation. The baseline grants "full authority" in general categories without the granular calibration that prevents both micromanagement and miscommunication.

2. **Context handoff with prior decisions.** The skill output includes 10 background bullets, 3 prior decisions with rationale (e.g., "Q3 tooltip experiment was killed: no stat-sig lift, high eng cost"), and known gotchas (e.g., "Eng lead prefers PRDs, not slide decks"). The baseline lists types of context to share but uses bracket placeholders rather than filling in realistic details.

3. **Anti-micromanagement guardrails.** The skill output includes a dedicated "what the manager will NOT do" section: will not dictate methodology, override in-guardrail decisions, rewrite artifacts, or rescue the PM from productive struggle. The baseline's feedback section is growth-oriented but does not explicitly constrain the manager's behavior.

4. **Debrief as a learning mechanism.** The skill output includes a structured 45-60 minute debrief agenda covering what worked, what didn't, ownership durability ("does ownership snap back to manager?"), and template improvements. The baseline includes a post-initiative retrospective as a bullet in Week 6 but without the structured debrief methodology.

5. **Criteria-based review.** The skill output defines quality criteria for each deliverable (diagnostic memo must be "grounded in data, includes segment analysis, identifies root causes not just symptoms") and specifies how the manager reviews ("frame feedback as criteria gaps, not personal preferences"). The baseline defines success criteria but without the review methodology that prevents managers from substituting their own judgment for the PM's.

## Verdict

The baseline provides a solid project delegation plan that any manager could use. The skill pack produces a delegation operating system that explicitly addresses the human dynamics of delegation -- autonomy calibration, context transfer, anti-micromanagement discipline, and structured debriefing. The skill output is particularly valuable for managers who tend to either under-delegate (micromanage) or over-delegate (abdicate), as it provides explicit guardrails for both failure modes.

## With Skill Output

<details>
<summary>Expand full output (~26k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~10k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
