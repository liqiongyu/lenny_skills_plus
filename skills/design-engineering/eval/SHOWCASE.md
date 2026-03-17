# Showcase: Design Engineering

> Demonstrates the value of the `design-engineering` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `design-engineering`. Context: B2B SaaS web app. 2 designers, 8 engineers. We ship slowly because UI polish and edge states get missed. Goal: reduce rework and increase consistency. Constraints: accessibility is required; need initial impact in 4 weeks. Output: a Design Engineering Execution Pack with an embedded model.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 4-week execution plan (foundation, build, integrate, measure) plus an embedded operating model with roles, cadence, and component lifecycle | 8 sections: context snapshot, design engineering charter with ownership matrix, prototype ladder with review gates, design-to-code contract (Figma template + component spec + PR checklist), component backlog with milestones, quality bar checklists, stakeholder cadence + decision log, risks/open questions/next steps |
| Completeness | Covers token system with specific CSS values, 10 core components with per-component a11y specs, PR workflow, migration pattern, and Week 4 metrics dashboard | Adds a prototype ladder (lo-fi through production) with graduation rules, a Figma handoff template, a component/flow spec template, explicit "definition of done" for UI work, and a decision log with initial entries |
| Actionability | Provides concrete token values (hex codes, spacing scale) and per-component ARIA requirements; PR workflow has 4 steps including visual regression testing | PR checklist is copy-paste ready; design-to-code contract defines 8 required states per component; prototype decision rules require a 3-day promote-or-delete window with a 5-day kill rule for zombie prototypes |
| Specificity | Names specific tools (axe-core, Chromatic/Percy); provides TypeScript interface requirement; gives accessibility specs per component type (10 components) | Ownership boundaries table maps 10 responsibilities across 3 roles (Design, Design Engineer Lead, Engineering) with clear "owns/consulted/informed" designations; milestones have rollback/stop conditions |
| Quality gates | Week 4 retrospective with discussion questions; success criteria checklist | Full quality bar with 7 checklists plus rubric scoring 30/30 with self-assessment caveat about real-world execution |

## Key Differences

1. **Embedded role definition.** The skill output defines a specific "Design Engineer Lead" role with ownership boundaries across 10 responsibility areas, interface protocols with designers and engineers, and an explicit engagement model justification (why embedded, not platform or tiger team). The baseline distributes responsibilities across existing roles without creating a dedicated bridge function.

2. **Prototype-to-production workflow.** The skill output includes a 4-rung prototype ladder (lo-fi, hi-fi, coded prototype, production) with explicit graduation rules, throwaway/shippable labels, and a 3-day decision window for coded prototypes. The baseline moves directly from design to build without a structured prototype lifecycle that prevents prototype debt.

3. **Design-to-code contract.** The skill output provides three ready-to-use templates: a Figma handoff template (6 required elements), a component/flow spec template (states, responsive behavior, accessibility, tokens, acceptance criteria), and a PR checklist. The baseline defines a PR review workflow but without the upstream contract that ensures designers deliver specs at the right level of detail.

4. **Milestone rollback conditions.** Each skill output milestone includes explicit rollback/stop conditions (e.g., "If Storybook setup takes >3 days, descope to local-only and ship CI integration in M2"). The baseline has a 4-week plan with weekly deliverables but without defined off-ramps when individual milestones take longer than expected.

5. **Decision log with initial entries.** The skill output seeds a decision log with 5 decisions made during planning (embedded model chosen, WCAG 2.1 AA as standard, axe-core as tool, Button as first golden-path component, top-10 token scope) with rationale and revisit triggers. The baseline makes similar decisions but does not capture them in a referenceable log.

## Verdict

The baseline provides a more immediately executable plan with specific token values, component ARIA specs, and a concrete 4-week weekly breakdown. The skill output provides a more sustainable operating model with clearer ownership, stronger process guardrails (prototype ladder, design-to-code contract, PR checklist), and explicit mechanisms to prevent the two most common failure modes: prototype debt and rework from underspecified handoffs. For a team with only 2 designers serving 8 engineers, the skill pack's structured handoff templates are particularly valuable.

## With Skill Output

<details>
<summary>Expand full output (~39k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~18k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
