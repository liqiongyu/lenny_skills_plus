# Showcase: Working Backwards

> Demonstrates the value of the `working-backwards` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> We're a B2B analytics platform used by enterprise admins and department leads. The problem: admins can't tailor dashboards by role, so teams see irrelevant data and adoption stalls after initial rollout. Enterprise expansion requires governance and least-privilege views. We're targeting a beta in 8 weeks. Please run the full Working Backwards process: generate 2-3 divergent PR/FAQ options (e.g., role-based default dashboards vs. dashboard packs by department vs. permissioned saved views), select and write the full PR/FAQ for the strongest option, and produce a backcasting plan that includes security review, permissions model, analytics instrumentation, documentation, and support enablement.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | Three phases (divergent options, full PR/FAQ, backcasting) in a linear document | Four phases: context snapshot, divergent options with evaluation matrix, full PR/FAQ with 15 FAQs (external + internal), and a week-by-week backcasting plan across five parallel tracks |
| Completeness | Evaluates 3 options, writes a PR/FAQ for the chosen option, and provides a backcasting plan with a critical-path dependency map | Includes weighted evaluation matrix, full press release, 8 external FAQs + 7 internal FAQs, week-by-week plan for 5 tracks (permissions, product/UX, analytics, docs, support), resource requirements, success criteria, and deferred-items roadmap |
| Actionability | Backcasting plan provides week-by-week deliverables with owners and dependencies per track; critical path is identified | Each week has a table with specific deliverables, owners, and dependencies per track; resource requirements quantified by role and weeks; beta success criteria have named metrics with targets |
| Specificity | PR/FAQ covers data scopes, saved views, governance console; FAQs address SSO/SCIM, API impact, pricing; backcasting identifies shadow mode as a de-risking technique | Similar product design choices with additional detail: shadow mode validation process, performance benchmarks (<50ms p99), SCIM sync latency handling (5-min cache with push invalidation), API token scoping with deprecation header, and penetration testing |
| Quality gates | No formal quality gate or self-assessment | No formal quality gate or self-assessment (both outputs lack this) |

## Key Differences

1. **Divergent options evaluation rigor.** The skill output includes a weighted evaluation matrix scoring each option across five criteria (least-privilege, adoption, security readiness, feasibility, platform leverage) with numerical scores and a weighted total. The baseline output provides prose-based strengths/weaknesses analysis without quantitative comparison, making the selection rationale less transparent.

2. **Internal vs. external FAQ separation.** The skill output explicitly separates customer-facing FAQs (8) from internal stakeholder FAQs (7), addressing questions like "Can we really ship in 8 weeks?" and "What are the biggest technical risks?" that a team needs answered internally. The baseline output mixes customer and internal concerns in a single FAQ section.

3. **Backcasting plan granularity.** The skill output organizes the 8-week plan into five parallel tracks (permissions/security, product/UX, analytics, documentation, support) with specific deliverables and dependencies per track per week, plus a critical-path diagram. The baseline output similarly covers these tracks but with less per-week, per-track specificity.

4. **Resource quantification.** The skill output includes a detailed resource requirements table listing 13 roles with headcount, weeks of involvement, and notes. The baseline output does not quantify the team size or effort required, making it harder to assess feasibility against the stated constraint of "1 PM, 1 designer, 4 engineers, 0.5 data engineer."

5. **Risk de-risking approach.** Both outputs identify shadow mode as a key de-risking technique for the permissions engine. The skill output adds specific mitigation details: benchmarking against top-10 customer datasets, session-level scope refresh with 5-minute cache, and SCIM push event triggering immediate invalidation. The baseline output covers similar ground but with slightly less operational detail.

## Verdict

Both outputs demonstrate strong Working Backwards methodology and arrive at the same product recommendation (Permissioned Saved Views). The skill-guided output provides a more rigorous option evaluation (weighted matrix), better-organized FAQ structure (internal vs. external), and a more detailed resource plan. The baseline output is still quite thorough and includes elements like a dependency map diagram. The primary advantage of the skill output is its execution-readiness: the backcasting plan with per-track, per-week deliverables and quantified resource needs gives a team what they need to start sprint planning.

## With Skill Output

<details>
<summary>Expand full output (~55k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~36k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
