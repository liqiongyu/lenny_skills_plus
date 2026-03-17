# Showcase: Onboarding New Hires

> Demonstrates the value of the `onboarding-new-hires` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `onboarding-new-hires`. We're onboarding a new Senior PM starting April 7 at our Series C B2B collaboration SaaS company (250 people, fully remote across US/EU). She'll own the enterprise integrations product line and report to the VP of Product. The team has had 2 PM turnovers in the past year and morale is fragile. Create a full Onboarding Pack: preboarding checklist (equipment, access, welcome), a first-week schedule with key meetings and stakeholder intros, a listening tour guide (who to talk to, what to ask), a working agreement template for her and her manager, and a 30/60/90-day + 1-year success plan with concrete milestones. Output: New Hire Onboarding Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 5 sections: preboarding checklist, first-week schedule, listening tour guide, working agreement template, and 30/60/90-day plan with risk mitigation and metrics appendix | 9 sections: onboarding brief, preboarding checklist, first-week plan, context pack outline, listening tour kit, working agreement, 30/60/90-day + 1-year plan, 30-day state-of-the-union memo template, and risks/open questions |
| Completeness | Covers all requested elements thoroughly; adds team preparation steps ("what I wish the PM knew" anonymous notes) and a key metrics appendix | Covers all elements plus a context pack / team operating manual outline, a "first pair" pairing assignment, a state-of-the-union memo template, and a detailed risk register with 5 risks, 7 open questions, and 9 immediate next steps |
| Actionability | First-week schedule is time-blocked with meeting purpose; listening tour has 25-30 conversations with a note template; 30/60/90 has specific checklists and anti-goals | First-week schedule is time-blocked with detailed notes per session; listening tour has a stakeholder map with 15+ roles, priority levels, and "meet by" dates; 30/60/90 has deliverables, metrics/checks, stakeholder checkpoints, and explicit guardrails |
| Specificity | Working agreement is team-oriented (mission, communication norms, meeting cadence, decision-making, feedback, work/life balance); listening tour has 11 internal + 5 customer questions | Working agreement is manager-PM focused (decision rights matrix, communication channels with response time norms, disagreement protocol, feedback preferences); listening tour has 14 questions organized by type (universal, diagnostic, relationship, forward-looking) |
| Quality gates | No formal quality assessment; includes a practical "this plan is a starting framework" disclaimer | 6-dimension rubric scoring 30/30 |

## Key Differences

1. **Onboarding brief with success definition.** The skill output opens with an onboarding brief that defines why this hire exists, what success looks like at 30/60/90 days and 1 year, constraints and context, and 5 risks to watch. This strategic framing gives both the manager and the new hire a shared understanding of the role's purpose. The baseline starts directly with the preboarding checklist.

2. **"First pair" and belonging design.** The skill version introduces a "first pair" concept -- a PM peer assigned to collaborate on a real task in week 1 -- alongside the traditional buddy. The first-week schedule explicitly designs for belonging with principles stated upfront ("no 'sit alone and read docs' days") and a "first contribution" artifact. The baseline includes a virtual team coffee and buddy but does not structure collaborative work in week 1.

3. **Context pack / team operating manual outline.** The skill output provides an 8-section outline for the context pack (team mission, decision-making, product philosophy, "what good looks like," metrics, cadence, stakeholders, glossary) that the manager should prepare before day 1. This is particularly valuable given the PM turnover context where institutional knowledge may have been lost. The baseline mentions a "state of the product" briefing document but does not specify its structure.

4. **Working agreement scope.** The skill version frames the working agreement as a bilateral manager-PM contract with a decision rights matrix (PM decides / PM + VP decide / VP decides), communication channel specifications with response time norms, a disagreement protocol, and explicit expectations in both directions. The baseline frames the working agreement as a team document covering broader norms (meetings, feedback, work/life balance), which is useful but serves a different purpose.

5. **30-day state-of-the-union memo template.** The skill output includes a complete template for the new PM's first major deliverable: a structured memo covering what she did, what she heard (themes with evidence and tensions), her current understanding, proposed focus areas, open questions, risks, and next steps. This artifact makes the listening tour's output tangible and actionable. The baseline mentions a "What I Heard" document synthesis but does not template it.

## Verdict

Both outputs are thorough and demonstrate genuine understanding of onboarding challenges, particularly in the context of PM turnover and fragile team morale. The baseline adds practical value through its team-oriented working agreement and metrics appendix. The skill-guided version differentiates through its strategic framing (onboarding brief), belonging design (first pair + first contribution), context pack structure, bilateral working agreement, and state-of-the-union memo template. For a VP of Product preparing to onboard a critical hire into a sensitive team situation, the skill version provides a more complete system.

## With Skill Output

<details>
<summary>Expand full output (~44k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~26k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
