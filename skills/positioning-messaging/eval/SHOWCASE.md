# Showcase: Positioning Messaging

> Demonstrates the value of the `positioning-messaging` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `positioning-messaging`. Product: an audit-ready AI assistant for SOC2 evidence collection. ICP: security leaders at 200-2,000 employee SaaS companies. Alternative: spreadsheets + GRC consultants. Proof: 'cut audit prep time by 40%' + 3 case studies. Surfaces: homepage hero + sales talk track. Output: a Positioning & Messaging Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 7-section document covering positioning statement, messaging framework, homepage hero, sales talk track, messaging hierarchy, persona messaging, and channel adaptations | 7-section Pack following a prescribed methodology (Context Snapshot, Positioning Brief, Messaging Hierarchy, Copy Set, Consistency Enablement, Validation Plan, Risks/Open Questions) with quality-gate self-assessment |
| Completeness | Covers a wide range of output surfaces: homepage, sales talk track, LinkedIn ads, email subject lines, conference pitch, financial modeling (ROI calculator), and competitive differentiation table | Additionally includes a positioning brief with 3 category frame options and selection rationale, a "say this / not that" table for consistency, internal description scripts at 15s/30s/60s, a sales "reset" script for confused prospects, and a formal validation plan with decision rules |
| Actionability | Full sales talk track with opening, discovery questions, pain amplification scripts, objection handling (5 objections), and a closing script; homepage includes full below-the-fold copy | Copy set provides 3 one-liner options, a 30-second elevator pitch, 10 taglines, and 5 homepage hero variants each with headline/subhead/CTA; sales talk track is structured as a 5-step framework (problem, category, differentiation, proof, next step) |
| Specificity | Persona-specific messaging for 3 roles (CISO, Head of Compliance, CFO) with specific lead messages and proof points; competitive positioning table against 4 alternative categories | Positioning brief includes explicit tradeoffs/non-goals (not a GRC platform, SOC 2 only, does not replace auditor) and an objection-response table; 3 pillar messaging has "what we mean" and "what we don't mean" clarifiers to prevent misinterpretation |
| Quality gates | No self-assessment or validation methodology | Includes a validation plan with 8 specific test questions, quantified decision rules (70% comprehension threshold, 70% recall at 24 hours), an A/B test design for homepage variants, and a next-iteration loop |

## Key Differences

1. **Category frame selection with rationale.** The skill-guided output evaluates 3 category frame options ("Automated SOC 2 evidence collection platform," "AI-powered compliance assistant," "Continuous audit-readiness platform") and explains why option A was chosen (most concrete, immediately understandable, avoids confusion with chatbots or risk scorers). The baseline uses "AI-powered audit readiness platform" without considering alternatives.

2. **"Say this / not that" consistency table.** The with-skill output includes a 6-row table mapping common communication goals (category, differentiation, outcome, alternative, scope, AI role) to preferred language and language to avoid, with reasons for each. The baseline provides a messaging hierarchy but does not formalize what should and should not be said.

3. **Validation plan with decision rules.** The skill-guided output defines a test plan (5 moderated calls + landing page A/B test), 8 specific questions to ask, and quantified decision rules (keep if 70%+ can restate the category unprompted; revise if fewer than 70%). The baseline does not include a validation methodology.

4. **Explicit tradeoffs and non-goals.** The with-skill output states 4 positioning tradeoffs: not a full GRC platform, not for SOC 1/HIPAA/ISO (yet), does not replace the auditor, and chooses depth in SOC 2 over breadth across frameworks. The baseline mentions GRC differentiation in objection handling but does not formalize non-goals as part of the positioning architecture.

5. **Sales content breadth vs. depth.** The baseline provides notably more sales content: full discovery questions, pain amplification scripts tailored to 3 buyer situations (spreadsheets, consultants, legacy GRC), 5 objection responses, a closing script, and persona-specific messaging for a CFO audience (ROI framing). The skill-guided output provides a more compact sales framework but with less situational adaptation.

## Verdict

The baseline excels in sales enablement depth -- its discovery questions, situational pain amplification scripts, and CFO-specific messaging provide richer material for a sales team. The skill-guided output is stronger as a positioning architecture: the category frame selection, consistency enablement artifacts, explicit non-goals, and validation plan with decision rules ensure the messaging holds together across surfaces and teams. The ideal outcome for this product would combine the skill-guided output's positioning discipline with the baseline's sales talk track depth.

## With Skill Output

<details>
<summary>Expand full output (~28k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~15k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
