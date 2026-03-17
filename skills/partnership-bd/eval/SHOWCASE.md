# Showcase: Partnership BD

> Demonstrates the value of the `partnership-bd` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> We're a B2B SaaS product that helps companies automate employee onboarding workflows. We want to grow pipeline through integration partnerships with HRIS and ATS vendors, but we only have 1.5 engineers to allocate to integrations. Our ICP is mid-market companies (200-2000 employees). We currently have 3 integrations live but believe expanding to 10-15 could 2x our pipeline in 6 months. Please build the full partnership execution pack: prioritized partner shortlist with decision-maker hypotheses and warm-path plans, tiered offer structure that protects our limited engineering capacity, partner pitch framework, and an outreach sequence we can start running in the next 2 weeks.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 7-section plan covering partner shortlist through quick-start action plan | 9-section Execution Pack with Context Snapshot, Deal Math, Partner Shortlist, Outreach Sequence, Pitch Framework, Negotiation Playbook, Partner Scorecard, Risk Log, and full quality-gate self-assessment |
| Completeness | Covers partner prioritization, tiered offers, pitch framework, outreach sequence, and metrics; engineering capacity plan is well done | Additionally includes a deal-math section with pipeline economics, a negotiation playbook with term sheets and walk-away criteria, a partner health scorecard, warm-path identification per partner, and decision-maker hypotheses with contact strategies |
| Actionability | 4-week quick-start plan with weekly checkboxes; outreach sequence is a detailed 8-touch multi-channel campaign with full email copy | Context snapshot makes explicit assumptions about unknowns; outreach sequence includes 8 touches with full scripts; pitch framework uses the BRIDGE methodology (Business, Relevant pain, Integration value, Data/proof, Go-to-market, Easy next step) with preparation checklists |
| Specificity | Names 15 specific partner companies across 3 tiers with ICP overlap ratings, engineering effort estimates, and rationale for each | Similarly names specific partners with tiering but adds decision-maker role hypotheses, warm-path plans per partner, and maps mutual customer overlap as a concrete outreach lever |
| Quality gates | Includes a risk mitigation table and monthly tracking dashboard | Includes risk log plus a quality-gate self-assessment rubric scoring the pack across multiple dimensions |

## Key Differences

1. **Deal math and pipeline economics.** The skill-guided output opens with a context snapshot that calculates the pipeline economics: how many partners at what conversion rates produce the target 2x pipeline. The baseline assumes the 2x target is achievable with 10-15 integrations but does not model the underlying math to validate the assumption.

2. **Decision-maker mapping and warm paths.** The with-skill output identifies specific roles (Head of Partnerships, Director of Ecosystem) at each target partner and proposes warm-path strategies (mutual customers, investor connections, industry peers) for getting introductions. The baseline lists partners and suggests multi-threaded outreach but does not map specific decision-maker roles or warm-path tactics per partner.

3. **Negotiation playbook.** The skill-guided output includes a negotiation section with term structures, walk-away criteria, and escalation strategies for partnership discussions. The baseline provides a tiered offer structure (revenue share percentages, co-marketing commitments) but does not address how to handle the negotiation process itself.

4. **Pitch framework methodology.** The with-skill output uses a structured BRIDGE framework with specific time allocations per section (30s for context, 60s for pain point, 90s for integration value, etc.) and a pre-conversation preparation checklist. The baseline's pitch approach is embedded in the outreach emails and partner tier descriptions but is not formalized into a repeatable methodology.

5. **Partner health scorecard.** The skill-guided output includes a quarterly partner health scorecard rating partners on 5 dimensions (adoption, lead flow, co-marketing engagement, technical health, relationship strength) with a deprioritization threshold. The baseline includes a monthly tracking dashboard with pipeline metrics but lacks a per-partner health evaluation framework.

## Verdict

Both outputs produce substantive partnership execution plans with specific partner names, tiered offer structures, and detailed outreach sequences. The baseline is notably strong on outreach copy (full multi-touch email scripts) and engineering capacity planning. The skill-guided output adds layers of strategic depth -- deal math validation, decision-maker mapping, a negotiation playbook, and a partner health scorecard -- that would be particularly valuable for a resource-constrained team needing to prioritize ruthlessly across 15 potential partners.

## With Skill Output

<details>
<summary>Expand full output (~46k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~23k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
