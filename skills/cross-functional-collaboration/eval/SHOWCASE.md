# Showcase: Cross Functional Collaboration

> Demonstrates the value of the `cross-functional-collaboration` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `cross-functional-collaboration`. You're a Product Lead running a 10-week onboarding revamp with Product/Eng/Design/Data/Marketing.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 10 sections: RACI matrix, phase breakdown with weekly tasks, communication framework, dependency map, risk management, quality gates, resource allocation | 8 sections: mission charter, stakeholder incentives map, roles/expectations contract with bilateral expectations, shared artifacts, operating cadence, decision log, collaboration norms with conflict protocol and credit plan, risks/open questions/next steps |
| Completeness | Thorough project management plan with daily task tables, resource allocation percentages, and quality gate checklists per phase | Focuses on the collaboration operating system: incentives mapping, bilateral expectations, decision rights with escalation triggers, conflict resolution protocol, and credit/recognition plan |
| Actionability | Detailed weekly deliverables and daily task assignments; clear go/no-go checklists at phase boundaries | Decision log seeded with 5 pending decisions (criteria, options, owners, due dates); expectations contract defines what each function expects from every other function; escalation triggers have specific numeric thresholds |
| Specificity | RACI matrix for 10 activities; dependency map with critical path items; resource allocation down to percentage per person per week | Stakeholder map captures what each person optimizes for and their concerns/fears; expectations are bilateral (PM expects Eng to..., Eng expects PM to...); conflict protocol is a 5-step worked example |
| Quality gates | Phase-level quality gate checklists (end of discovery, design, build, launch) | Full quality gate checklist (11 items) plus rubric scoring 29/30 with identified gap (missing seats to confirm) |

## Key Differences

1. **Incentives and concerns mapping.** The skill output maps what each stakeholder optimizes for and what they fear (e.g., "Eng Lead optimizes for technical quality; concerns: unclear specs leading to rework"). The baseline assigns RACI roles but does not surface the underlying incentive tensions that drive collaboration friction.

2. **Bilateral expectations contract.** The skill output defines expectations in both directions (PM expects Eng to provide estimates by Week 3; Eng expects PM to lock scope by Week 4 and not introduce new features). The baseline assigns responsibilities to functions but does not make cross-functional promises explicit.

3. **Conflict resolution protocol.** The skill output includes a 5-step conflict protocol with a worked example ("Design is optimizing for polish; Eng is optimizing for shipping in 10 weeks. Both are valid.") and norms for healthy disagreement. The baseline addresses decision-making escalation paths but without a structured conflict resolution methodology.

4. **Credit and recognition plan.** The skill output includes specific mechanics for sharing credit: rotating presenters at demos, named contributors in exec updates, weekly shout-outs, and anti-patterns to avoid (PM monopolizing the narrative, invisible infrastructure work). The baseline does not address recognition, which is a common source of cross-functional resentment.

5. **Decision velocity focus.** The skill output seeds a decision log with 5 specific pending decisions, each with owner, due date, criteria, and options. Operating cadence meetings are structured around "decisions needed" rather than status updates. The baseline includes decision-making protocols but without pre-seeded decisions or decision-first meeting agendas.

## Verdict

The baseline provides a stronger project management plan with detailed task breakdowns, resource allocations, and phase gates. The skill output provides a stronger collaboration operating system that addresses the human dynamics (incentives, expectations, conflict, credit) that typically cause cross-functional projects to fail. The two outputs are complementary -- the skill pack's collaboration norms would make the baseline's project plan more likely to succeed.

## With Skill Output

<details>
<summary>Expand full output (~29k)</summary>

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
