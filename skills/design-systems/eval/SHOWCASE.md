# Showcase: Design Systems

> Demonstrates the value of the `design-systems` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `design-systems`. Context: B2B SaaS web app. Current state: inconsistent UI, lots of one-off CSS, no shared tokens, and slow design-to-dev handoff. Goal: improve consistency and speed; first impact in 6 weeks. Constraints: accessibility required; small team (2 designers, 6 engineers). Output: a Design System Operating Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 15 sections covering executive summary, architecture, 6-week plan, handoff process, accessibility plan, migration strategy, governance, and tools | 9 sections: context snapshot, charter with principles and anti-goals, UI audit + operational blockers, blockframe-to-component map, token model + backlog, component inventory + roadmap with 4 milestones, documentation + enablement plan, governance + adoption plan, quality gate |
| Completeness | Very comprehensive: includes token architecture (3 tiers), component folder structure, CSS migration strategy, detailed accessibility testing matrix, and post-6-week governance lifecycle | Adds operational hook analysis, blockframe spec with component mapping, audience-specific enablement (non-designers, designers, engineers each with common mistakes and guardrails), champion plan with specific teams and asks |
| Actionability | 6-week plan with weekly checkboxes per function (design/engineering); migration strategy with per-screen checklist; handoff process before/after comparison with time savings estimates | Blockframe maps each UI element to a named component, tokens, required states, and accessibility requirements; champion plan names specific teams, what they get, what is asked of them, and support needed |
| Specificity | Names specific token values (hex codes, pixel values), component folder structure, and tool recommendations (Style Dictionary, Chromatic, jest-axe) | Token taxonomy includes 12 categories with usage rules and per-category a11y notes; component backlog assigns 31 items across 6 engineers with milestone targets and dependencies |
| Quality gates | No self-assessment | Full quality gate (8 checklists) plus rubric scoring 29/30 with top 3 improvements identified |

## Key Differences

1. **Operational hook and first slice.** The skill output identifies the primary operational blocker ("30-40% of feature time on UI infrastructure rather than product logic"), names the first slice to ship (Forms + Buttons + Typography + tokens + FormPage recipe), and explains why this slice was chosen (covers 60%+ of screens). The baseline starts building from a component priority list without the explicit business-case framing.

2. **Blockframe-to-component mapping.** The skill output includes an ASCII blockframe of the most common page pattern (Form Page), maps each block to a component, lists the tokens consumed, states required, and accessibility notes. The baseline jumps from audit to building components without an intermediate mapping step that ensures the component library matches real page structures.

3. **Audience-specific enablement.** The skill output defines common mistakes and guardrails for three distinct audiences: non-designers (using raw colors in specs), designers (detaching Figma components), and engineers (hardcoding values). The baseline provides documentation and onboarding but does not differentiate by audience or anticipate audience-specific failure modes.

4. **Champion-driven adoption plan.** The skill output names specific champion teams (Settings/Admin team for forms, Dashboard team for tables) with explicit asks ("rebuild 1 settings page using M1 components in Week 3-4"), what they get, and support needed. The baseline addresses adoption through migration rules and governance but without identifying specific early-adopter teams.

5. **Milestone rollback conditions.** Each skill output milestone includes an explicit stop condition (e.g., "If M1 adoption is below 50% of new screens, freeze M2 and focus on adoption/migration support"). The baseline's 6-week plan has weekly milestones but no off-ramps for when adoption does not follow delivery.

## Verdict

Both outputs are thorough and production-ready. The baseline excels in technical depth (architecture, folder structure, accessibility testing matrix, migration strategy). The skill output excels in organizational strategy (operational framing, audience enablement, champion-driven adoption, milestone stop conditions). The key insight is that design systems fail more often from adoption resistance than from technical shortcomings, and the skill pack's focus on enabling different audiences and driving adoption through champion teams addresses this directly.

## With Skill Output

<details>
<summary>Expand full output (~40k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~24k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
