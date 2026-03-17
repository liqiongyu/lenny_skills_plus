# Showcase: Systems Thinking

> Demonstrates the value of the `systems-thinking` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `systems-thinking`. Our engineering on-call load has been rising for 6 months straight (now averaging 15 pages/week per team, up from 5). Teams are burned out and starting to cut corners on code reviews to ship faster, which we suspect is creating more incidents. Meanwhile, management is pushing for higher feature velocity because competitors are shipping faster. Map the system dynamics: identify actors and incentives, feedback loops (especially the firefighting-creates-more-fires loop), second-order effects of proposed interventions (hiring more engineers vs reducing scope vs investing in reliability), and propose 2-3 leverage points with an intervention plan and guardrails. Output: Systems Thinking Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 12-section document: system boundary, actor maps, 5 feedback loops (text + ASCII diagram), quantitative projection, 3 intervention analyses, 3 leverage points, integrated intervention plan, guardrails, expected trajectory, mental models, executive summary | 8-section pack: context + boundary, actors + incentives map, system map (15 variables, 19 causal links), 4 feedback loops with "so what" narratives, second-order effects ledger (3 moves), 6 leverage points with intervention plan, 4 system-build opportunities, risks/open questions/next steps |
| Completeness | Covers the system dynamics thoroughly with quantitative projections (pages/week extrapolated through month 9), 5 guardrails with enforcement mechanisms, and a reference to Donella Meadows' leverage point hierarchy | Covers system dynamics with more formal structure: 15 named variables with 19 directional causal links, explicit time delays (5 delays with estimated lags), 3 "invisible actors" (alert system, performance review system, codebase/debt), and 4 automation/standardization opportunities |
| Actionability | 3-phase intervention plan (Emergency Stabilization, Instrument/Diagnose, Structural Changes) with specific owners and metrics per action; expected trajectory table through month 12 | 6 leverage points each with owner, sequencing (Now/Next/Later), leading indicators, guardrails, and rollback/stop conditions; week-by-week execution timeline |
| Specificity | Names specific interventions (circuit breaker policy with 8-page threshold, 20% reliability budget, mandatory review standards); quantifies current capacity loss (12.5%) | Names specific variables and links with confidence ratings; specifies rollback conditions for each intervention (e.g., "If page volume increases after alert changes, immediately revert"); provides a detailed sequencing diagram |
| Quality gates | 5 guardrails with specific enforcement and override mechanisms (e.g., circuit breaker override requires VP-level written approval, max 2 overrides/quarter) | 10-dimension self-assessment checklist + rubric; each leverage point has leading indicators, guardrails, and explicit rollback conditions |

## Key Differences

1. **System model formalization.** The skill output defines 15 named variables with 19 directional causal links, each annotated with time delay estimates and confidence ratings. The baseline describes the same dynamics using narrative feedback loops and an ASCII causal diagram. Both approaches are valid, but the formal variable-and-link structure makes it easier to trace exactly how interventions propagate through the system.

2. **Invisible actors.** The skill output identifies 3 "invisible actors" that shape behavior without being human participants: the alert/incident system (configuration shapes who gets paged), the performance review system (rewards features over reliability), and the codebase itself (debt compounds). The baseline covers these dynamics within its actor profiles and loop descriptions but doesn't elevate them as distinct system actors.

3. **Second-order effects analysis.** The skill output provides a structured 3-order effects ledger for each candidate move (hire, reduce scope, invest in reliability) including who wins/loses, unintended consequences, and specific mitigations. The baseline analyzes the same 3 interventions with similar depth but organizes the analysis differently (1st, 2nd, 3rd order effects in tables vs. narrative sections).

4. **System-build opportunities.** The skill output includes 4 concrete automation/standardization proposals (automated alert enrichment, post-mortem action item tracker, automated code quality gates, work categorization taxonomy) each with a "first small step" and expected outcome. The baseline proposes similar interventions within its plan but doesn't separate the system-building opportunities as a distinct deliverable.

5. **Quantitative projection.** The baseline provides a month-by-month projection of pages/week, capacity lost, and effective velocity both with and without intervention -- including the "wall" at month 6-9 where capacity collapses. The skill output describes these dynamics qualitatively but doesn't produce the same numerical forecast. The quantitative approach is more compelling for executive audiences.

## Verdict

Both outputs demonstrate strong systems thinking and reach similar conclusions about the core dynamics and interventions. The skill-guided output is more formally structured (explicit variables, links, time delays, confidence ratings) and more operationally detailed (rollback conditions for each intervention, system-build opportunities). The baseline is more persuasive for leadership audiences through its quantitative projections, Meadows leverage point framework references, and the circuit breaker policy design with override governance. The two approaches are complementary rather than clearly superior in one direction.

## With Skill Output

<details>
<summary>Expand full output (~40k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~27k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
