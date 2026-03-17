# Showcase: Writing Specs Designs

> Demonstrates the value of the `writing-specs-designs` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `writing-specs-designs`. We're a consumer iOS app. Add an 'invite friends' flow. Goal: increase successful invites. Constraint: ship in 4 weeks. Please optimize taps to first value.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 13 sections covering overview, user flows, entry points, deep linking, share messages, invitee onboarding, technical architecture, edge cases, privacy, delivery plan, A/B testing, post-launch monitoring | 10 sections following a structured spec methodology: context snapshot, goals/non-goals, assumptions/dependencies, tap economy worksheet, low-fi diagram, user flows, states per screen, prototype brief, requirements with acceptance criteria, measurement plan |
| Completeness | Covers sender flow, invitee flow, entry points with frequency rules, deep link architecture (Universal Links, App Clips), share message templates, invitee onboarding comparison table, full backend data model, and A/B testing plan | Covers tap economy analysis, Mermaid flow diagram with backend components, two happy paths with edge cases, state tables for three screens (six states each), prototype brief with three scenarios, 15 requirements with MoSCoW priority, and measurement plan with 10 metrics |
| Actionability | 4-week delivery plan with weekly milestones; A/B testing plan with 3 experiments (sample sizes specified); post-launch dashboard requirements; technical architecture with API endpoints and iOS components | Requirements have testable acceptance criteria; prototype brief has a 3-day timebox with specific success criteria; next steps table has 9 actions with owners and day-by-day timeline; each risk has likelihood/impact/mitigation |
| Specificity | Deep link URL structure with HMAC signature; invitee onboarding differences table (organic vs. invited); rate limiting at 50/day; 11 analytics events named; iOS component names specified | Tap economy worksheet with per-step friction risk and removal ideas; per-screen state tables with UI content, system behavior, and analytics events; P95 latency targets (<500ms for link generation); contacts permission pre-frame explainer specified |
| Quality gates | No formal quality gate | Six-item checklist plus a six-dimension rubric self-score (29/30) |

## Key Differences

1. **Tap economy methodology.** The skill output includes a dedicated tap economy worksheet that budgets 3 taps from entry to first invite sent, with per-step friction risk assessment and specific tap-removal decisions (e.g., combining contact selection + message preview into one screen). The baseline output achieves a 2-tap goal but presents it as a design outcome rather than a structured analysis with trade-off reasoning.

2. **Screen state coverage.** The skill output provides state tables for three key screens (Invite Picker, Pre-composed Message, Success Screen), documenting six states each (loading, empty, populated, permission denied, permission not determined, error) with specific UI content, system behavior, and analytics events per state. The baseline output handles edge cases in a separate table but does not systematically enumerate states per screen.

3. **Prototype brief as a validation tool.** The skill output includes a prototype brief that identifies two critical interaction uncertainties to validate (permission prompt timing and post-send celebration effect), specifies three prototype scenarios, sets fidelity requirements (hi-fi, on-device), and defines measurable success criteria (>70% permission grant rate, >50% "Invite More" taps). The baseline output does not include a prototyping phase.

4. **Technical architecture depth.** The baseline output provides significantly more technical detail: a full backend data model (Invite entity with all fields), five iOS client components by name (InviteManager, InviteDeepLinkHandler, etc.), infrastructure decisions (Branch.io evaluation, OG image generation via serverless), deep link URL structure with HMAC signatures, and App Clip integration. The skill output stays at the spec level, leaving technical design to engineering.

5. **A/B testing and post-launch plan.** The baseline output includes three defined A/B experiments with control/variant descriptions, primary metrics, and sample sizes, plus post-launch dashboard requirements and Phase 2 candidates. The skill output focuses more on pre-build validation (prototype brief) and measurement instrumentation, deferring experimentation to the post-launch phase.

## Verdict

The skill-guided output is a more methodical spec document that guides the team through structured decision-making: tap economy analysis, state enumeration, prototype validation, and testable requirements. The baseline output is more implementation-comprehensive, covering technical architecture, deep linking details, A/B testing plans, and iOS component design. The skill output reduces risk before building (through the prototype brief and tap economy worksheet); the baseline output accelerates building once the decision to proceed is made.

## With Skill Output

<details>
<summary>Expand full output (~30k)</summary>

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
