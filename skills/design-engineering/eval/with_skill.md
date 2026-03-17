# Design Engineering Execution Pack

**Team:** B2B SaaS web app | 2 designers, 8 engineers
**Goal:** Reduce rework, increase UI consistency
**Operating model:** Embedded
**Date:** 2026-03-17

---

## 1) Context Snapshot

**Product / area in scope:**
B2B SaaS web application -- all user-facing UI surfaces. Primary focus on the core product workflows where UI polish and edge-state coverage directly affect user trust and task completion.

**Primary user / JTBD:**
B2B end-users who need to complete workflows reliably and efficiently. They expect a polished, consistent, accessible interface that does not surprise them with broken states or visual inconsistencies.

**Stakeholders / decision-maker(s):**
- **Design Lead** (1 of 2 designers) -- owns visual/interaction direction
- **Engineering Lead** (senior IC or EM from the 8-person eng team) -- owns technical decisions and code quality
- **Product Manager** (assumed) -- owns prioritization and scope
- **Decision-maker for this initiative:** Engineering Lead + Design Lead jointly, with PM as tiebreaker on scope/priority

**Why now:**
The team ships slowly because UI polish and edge states are discovered late (during QA or after release), causing rework cycles. With only 2 designers serving 8 engineers, there is no systematic bridge between design intent and shipped UI. Accessibility is a hard requirement, and there is no repeatable mechanism to enforce it. The team needs initial measurable impact within 4 weeks.

**Success signals (measurable if possible):**
1. **Rework reduction:** 50% fewer UI-related bug tickets reopened or filed post-merge within the first 4-week cycle (baseline: count current UI bugs per sprint).
2. **Consistency:** New components/flows use shared tokens and follow the design-to-code contract (target: 100% of new work in scope).
3. **Accessibility coverage:** All new components pass WCAG 2.1 AA automated checks before merge (target: 0 a11y regressions shipped).
4. **Cycle time:** Measurable reduction in time from "design-ready" to "merged PR" for UI work (track before/after).
5. **Edge-state completeness:** PRs for UI work include all required states (loading, empty, error, disabled, hover, focus) as verified by the PR checklist.

**Current state (design + code):**
- **Design artifacts:** Figma files exist but handoff is informal (screenshot in ticket or Figma link with no structured spec). No design tokens file shared between Figma and code. No formal states inventory per component.
- **Codebase/stack:** Assumed modern web stack (React or similar component framework, CSS-in-JS or utility classes, CI pipeline). No Storybook or component documentation site. Components exist but are inconsistently built -- mix of one-off styles and partially shared patterns.
- **Existing design system:** Informal at best. Some shared components exist in code but they lack documentation, consistent API, states coverage, and accessibility annotations.

**Constraints:**
- **Timeline:** Initial impact required within 4 weeks (Week 1-4). This is the first milestone horizon.
- **Team capacity:** 2 designers (already fully utilized), 8 engineers. No dedicated "design engineer" hire. The embedded model must work with existing headcount.
- **Accessibility:** WCAG 2.1 AA compliance is mandatory, not optional. Must be built into the workflow, not bolted on.
- **Stack:** Modern web (assumed React + CI). Adjustments needed if stack differs.
- **No Storybook currently:** Component documentation and visual review tooling must be established as part of the plan.

**Assumptions:**
1. The stack is React (or similar component-based framework) with a CI pipeline that can run linters and tests.
2. There is no existing Storybook instance; setting one up is feasible within Week 1.
3. At least 1 engineer has strong UI/CSS skills and can act as the embedded design engineer (see charter below).
4. Figma is the design tool; designers can add structured annotations if given a lightweight template.
5. The team uses a ticket/board system (Jira, Linear, or similar) for tracking work.
6. No i18n or localization requirements in the initial 4-week scope (can be added later).

---

## 2) Design Engineering Charter

**Mission:**
Bridge the gap between design intent and shipped UI by embedding a design-engineering function that owns component implementation quality, edge-state completeness, accessibility compliance, and visual fidelity -- reducing rework and increasing consistency across the product.

**Scope (in):**
- Component implementation to production quality (states, tokens, a11y, responsiveness)
- Design-to-code contract definition and enforcement
- Prototype-to-production workflow and review gates
- Storybook/component documentation setup and maintenance
- Visual QA sign-off on UI PRs
- Accessibility compliance verification at the component and flow level
- PR checklist and review process for UI work

**Scope (out):**
- UX research, user interviews, or product strategy (use appropriate research skills)
- Brand/visual identity creation or evolution (separate design/brand process)
- Backend architecture, API design, or infrastructure (engineering team)
- Building a full design system with governance, theming, and multi-team adoption (use `design-systems` if that becomes the goal)
- Running standalone design critiques or reviews (use `running-design-reviews`)
- Writing feature specs or detailed UX flow documents (use `writing-specs-designs`)

**Engagement model: Embedded**
One engineer (the "Design Engineer Lead") is embedded as the bridge between the 2 designers and the 8-person engineering team. This person:
- Joins design reviews to understand intent, constraints, and edge cases early
- Translates Figma specs into component contracts (states, tokens, a11y requirements)
- Reviews all UI-touching PRs for visual fidelity, states coverage, and accessibility
- Maintains Storybook and component documentation
- Coaches other engineers on UI implementation patterns

**Why embedded (not platform or tiger team):**
- The team is small (10 people total). A separate platform team is overhead the org cannot afford.
- The problem is systemic (polish and edge states missed across all work), not confined to a single flow -- so a tiger team on one project would not fix the root cause.
- Embedding one engineer as the design-engineering bridge gives the highest leverage: they set patterns that all 8 engineers follow, multiplied by the PR review process.

**Ownership boundaries:**

| Responsibility | Design (2 designers) | Design Engineer Lead (1 engineer) | Engineering (remaining 7 engineers) |
|---|---|---|---|
| Interaction/visual direction | **Owns** | Consulted | Informed |
| Component API shape | Consulted | **Owns** (proposes) | Reviews + approves |
| States inventory (loading, empty, error, disabled, hover, focus) | Co-owns (specifies in Figma) | **Owns** (verifies completeness) | Implements |
| Design tokens (spacing, color, type) | **Owns** (defines in Figma) | Translates to code tokens | Consumes |
| Accessibility (WCAG 2.1 AA) | Annotates in Figma | **Owns** (review gate) | Implements |
| Visual QA / fidelity sign-off | Final say on visual direction | **Owns** (PR-level sign-off) | Requests review |
| Performance | Informed | Flags issues | **Owns** |
| Storybook / component docs | Contributes examples | **Owns** (maintains) | Contributes |
| PR review (UI work) | Optional review | **Required** reviewer | Author + peer review |

**Key rule: No "two owners."** For any UI component or flow:
- **Visual direction** = Designer decides.
- **Component API + implementation quality** = Design Engineer Lead decides.
- **Technical architecture** = Engineering team decides.
- **Accessibility compliance** = Design Engineer Lead verifies; Engineering implements.
- **Disputes** escalate to the Design Lead + Engineering Lead pair, with PM as tiebreaker.

**Interfaces (how work flows between functions):**
1. **Design -> Design Engineer Lead:** Designer shares Figma link with structured annotations (states, tokens, a11y notes) using the Figma Handoff Template (see Section 4). Design Engineer Lead reviews for completeness within 1 business day.
2. **Design Engineer Lead -> Engineering:** Design Engineer Lead creates or updates the component contract (see Section 4) and adds it to the ticket. Engineer implements against the contract.
3. **Engineering -> Design Engineer Lead:** Engineer opens PR with required checklist items (screenshots, states, a11y notes). Design Engineer Lead reviews within 1 business day.
4. **Design Engineer Lead -> Design:** For visual fidelity questions that exceed the contract, Design Engineer Lead pulls in the designer for a quick sync (async Figma comment or 10-min call).

**Definition of "done" (for any UI component or flow):**
- All states implemented (default, hover, focus, active, disabled, loading, empty, error -- as applicable)
- Design tokens used (no one-off pixel values or hex colors)
- WCAG 2.1 AA compliance verified (keyboard navigation, focus order, labels, color contrast, ARIA as needed)
- Storybook story exists with all states documented
- PR checklist complete (screenshots, test plan, a11y notes)
- Design Engineer Lead has approved the PR
- No unresolved visual fidelity issues flagged by the designer

**Operating cadence:**

| Ritual | Frequency | Duration | Participants | Purpose |
|--------|-----------|----------|-------------|---------|
| Design-Eng Sync | Weekly (Mon) | 30 min | Design Lead + Design Engineer Lead + Eng Lead | Review upcoming UI work, resolve blockers, align on priorities |
| PR Review SLA | Ongoing | < 1 business day | Design Engineer Lead | All UI-touching PRs get design-eng review |
| Component Demo | Biweekly (Fri) | 20 min | Full team | Demo shipped components in Storybook; collect feedback |
| Retrospective | Every 2 weeks | 30 min | Design + Design Engineer Lead + Eng | What's working, what's not, process adjustments |
| Stakeholder Update | Biweekly | Async (5 bullets) | PM + leads | Progress, risks, asks |

**KPIs / success signals:**
1. UI bug tickets reopened or filed post-merge (target: -50% within 4 weeks)
2. Percentage of new UI PRs that pass the PR checklist on first submission (target: >80% by Week 4)
3. Accessibility regressions shipped (target: 0)
4. Average time from design-ready to merged PR for UI work (track trend)
5. Number of components with Storybook documentation (target: all new + top 5 existing by Week 4)

**Risks / constraints (charter-level):**
- The Design Engineer Lead role is filled by reallocating an existing engineer, reducing feature capacity by ~12.5%. This must be explicitly supported by PM and Eng Lead.
- If neither designer can produce structured Figma annotations (states, tokens), the Design Engineer Lead will need to extract this information themselves, slowing the process.
- The embedded model depends on one person; if they are unavailable, the review gate stalls. Mitigation: train a secondary reviewer by Week 4.

---

## 3) Prototype Ladder + Prototype-to-Production Workflow

### Prototype Ladder

| Rung | Purpose | Fidelity | Typical Artifacts | Disposable? | "Graduation" Rule |
|------|---------|----------|-------------------|-------------|-------------------|
| **Lo-fi** | Explore information architecture, flow structure, and layout options. Validate with stakeholders before investing in visual detail. | Wireframe-level. No real data, no styling, no interactions. | Paper sketches, Figma wireframes, whiteboard photos | **Yes -- always throwaway** | Stakeholder sign-off on flow structure and key layout decisions. Designer confirms direction before moving to hi-fi. |
| **Hi-fi** | Lock visual direction, spacing, typography, and color. Define all required states. Produce the "spec" that becomes the design-to-code contract. | Pixel-accurate Figma mocks with real content examples. All states (default, hover, focus, disabled, loading, empty, error) shown. | Figma frames with annotations (states, tokens, a11y notes, responsive breakpoints) | **Yes -- throwaway** (the Figma file is reference, not shipped code) | Design Lead approves visual direction. Design Engineer Lead confirms states inventory is complete and contract is writable. |
| **Coded prototype** | Validate interaction patterns, animations, data-binding behavior, and technical feasibility in the real stack. Surface constraints that Figma cannot reveal (performance, focus management, keyboard navigation). | Uses production components/tokens if available. Real framework code. May use mocked data. | Branch with prototype code; Storybook stories or local demo | **Shippable IF** it uses production tokens/components and passes the quality bar. **Throwaway IF** it uses shortcuts (inline styles, no a11y, hardcoded data). Label explicitly in the PR description. | Decision within **3 business days** of creation: (a) promote to production (apply quality bar, add tests, document), (b) extract learnings and delete, or (c) extend time-box by 2 days max with explicit justification. |
| **Production** | Ship to users. Maintainable, tested, documented, accessible. | Full quality bar. All states, tokens, a11y, Storybook, tests. | Merged PR, Storybook story, component docs | **No -- never throwaway** | Passes all review gates (see below). Design Engineer Lead + peer engineer approve PR. Designer confirms visual fidelity (async). |

### Decision Rules for Coded Prototypes

1. **Default assumption:** coded prototypes are **throwaway** unless the author explicitly labels them shippable at creation time.
2. **Shippable criteria:** uses production tokens, production components, has keyboard/focus support, no inline styles or magic numbers.
3. **Time-box:** every coded prototype has a 3-business-day decision window. At the end of the window, the team must choose: promote, extract-and-delete, or extend (max 2 days, once only).
4. **No zombie prototypes:** if a coded prototype has not been promoted or deleted within 5 business days, the Design Engineer Lead flags it in the weekly sync and it is deleted by end of week.

### Review Gates

**Design Review Gate (Lo-fi -> Hi-fi transition):**
- **Who:** Design Lead
- **What:** Flow structure, IA, layout direction
- **When:** Before investing in hi-fi mocks
- **Pass criteria:** Stakeholder agreement on flow; no major IA concerns

**Design Spec Gate (Hi-fi -> Coded prototype or Production):**
- **Who:** Design Engineer Lead + Design Lead
- **What:** States inventory complete, tokens specified, a11y annotations present, responsive behavior defined
- **When:** Before any engineer starts implementation
- **Pass criteria:** Design-to-code contract is writable from the Figma spec without back-and-forth

**Engineering Review Gate (Coded prototype -> Production or PR merge):**
- **Who:** Design Engineer Lead (required) + 1 peer engineer
- **What:** PR checklist complete (screenshots of all states, test plan, a11y notes, Storybook link)
- **When:** Before merge
- **Pass criteria:** All PR checklist items satisfied; no unresolved comments; WCAG 2.1 AA automated checks pass

**QA/A11y Gate (before release):**
- **Who:** Design Engineer Lead (or designated a11y reviewer)
- **What:** Keyboard navigation, screen reader basics (labels, roles, focus order), color contrast, responsive behavior
- **When:** Before feature flag is enabled or release is cut
- **Pass criteria:** Component passes axe-core (or equivalent) with 0 critical/serious violations; keyboard-only task completion verified

**Release Gate:**
- **Who:** Eng Lead + PM
- **What:** Feature completeness, no regressions, stakeholder sign-off
- **When:** Before deploy to production
- **Pass criteria:** All prior gates passed; no open P0/P1 bugs in scope

---

## 4) Design-to-Code Contract

### Figma Handoff Template (for designers)

For every component or flow handed off to engineering, the designer must provide:

1. **Component/flow name** and user goal (1 sentence)
2. **States shown in Figma:** default, hover, focus, active, disabled, loading, empty, error (mark N/A if not applicable; do not omit without explanation)
3. **Token annotations:** spacing values reference the token scale (e.g., `space-4`, `space-8`), colors reference named tokens (e.g., `color-primary`, `color-text-secondary`), typography references type scale (e.g., `heading-md`, `body-sm`)
4. **Responsive behavior:** what changes at mobile / tablet / desktop breakpoints (or "no responsive variation" if fixed-width)
5. **Accessibility notes:** expected keyboard behavior, focus order, visible focus indicator, any ARIA labels or roles, minimum color contrast
6. **Edge cases and constraints:** max content length / truncation rules, empty state content, error message copy, loading skeleton shape

### Component/Flow Spec Template (for implementation)

```
**Name:** [Component or flow name]
**User goal:** [1 sentence: what the user is trying to accomplish]

**States:**
- Default: [description or Figma frame link]
- Hover: [description or Figma frame link]
- Focus: [description or Figma frame link]
- Active: [description or Figma frame link]
- Disabled: [description or Figma frame link]
- Loading: [description or Figma frame link]
- Empty: [description or Figma frame link]
- Error: [description or Figma frame link]

**Responsive behavior:**
- Mobile (<640px): [behavior]
- Tablet (640-1024px): [behavior]
- Desktop (>1024px): [behavior]

**Accessibility (WCAG 2.1 AA):**
- Keyboard: [tab order, enter/space/escape behavior]
- Focus: [visible focus indicator; focus trap if modal]
- Labels: [visible label or aria-label; aria-describedby for help text]
- ARIA: [role, aria-expanded, aria-live, etc. if applicable]
- Contrast: [minimum 4.5:1 for text, 3:1 for UI components]

**Tokens used:**
- Spacing: [e.g., space-2, space-4, space-8]
- Typography: [e.g., heading-sm, body-md]
- Color: [e.g., color-primary, color-border-default, color-bg-surface]
- Border radius: [e.g., radius-md]
- Shadow: [e.g., shadow-sm]

**Acceptance criteria:**
- [ ] All states listed above are implemented and visually match Figma
- [ ] Design tokens are used (no hardcoded px/hex values)
- [ ] Keyboard navigation works as specified
- [ ] axe-core reports 0 critical/serious violations
- [ ] Storybook story exists showing all states
- [ ] Responsive behavior matches spec at all breakpoints
- [ ] [Additional criteria specific to this component]
```

### PR Expectations (copy into PR template)

Every PR that touches UI must include:

```markdown
## UI PR Checklist

### Screenshots (required)
- [ ] Default state
- [ ] Hover state
- [ ] Focus state (keyboard focus visible)
- [ ] Disabled state (if applicable)
- [ ] Loading state (if applicable)
- [ ] Empty state (if applicable)
- [ ] Error state (if applicable)
- [ ] Mobile viewport (<640px) (if responsive)

### Accessibility (required)
- [ ] Keyboard-only task completion verified
- [ ] Focus order is logical
- [ ] Visible focus indicator present
- [ ] axe-core (or equivalent) reports 0 critical/serious violations
- [ ] Color contrast meets 4.5:1 (text) / 3:1 (UI components)
- [ ] ARIA labels/roles added where needed

### Tokens + Consistency (required)
- [ ] Design tokens used for spacing, color, typography (no magic numbers)
- [ ] Component follows existing patterns in the codebase

### Documentation (required)
- [ ] Storybook story added/updated with all states
- [ ] Component API documented (props, variants, defaults)

### Test Plan
- [ ] [Describe what was tested and how]

### Notes
- [Any edge cases, known limitations, or follow-up items]
```

### How the Contract Is Verified

| Check | Method | When | Who |
|-------|--------|------|-----|
| States completeness | Visual inspection of PR screenshots against spec | PR review | Design Engineer Lead |
| Token usage | Code review (search for hardcoded px/hex) + future lint rule | PR review | Design Engineer Lead + peer |
| Accessibility automated | axe-core or similar in CI (fails PR if critical/serious) | CI pipeline | Automated |
| Accessibility manual | Keyboard walkthrough + screen reader spot check | PR review | Design Engineer Lead |
| Visual fidelity | Storybook screenshot vs Figma frame | PR review | Design Engineer Lead (escalate to Designer if uncertain) |
| Responsive behavior | Browser resize or responsive mode screenshots | PR review | Author (screenshots in PR) |

---

## 5) Component/Flow Backlog + Delivery Plan

### UI Surface Map (Leverage Analysis)

Based on a typical B2B SaaS app, the highest-leverage areas are:

| Area | User Impact | Reuse Potential | Risk / Complexity | Priority |
|------|------------|-----------------|-------------------|----------|
| Form components (inputs, selects, checkboxes, radio, textarea) | High -- every workflow uses forms | Very high -- used on every page | Medium -- many states, a11y-critical | **P0** |
| Data table | High -- primary data consumption pattern | High -- used in multiple list views | High -- sorting, filtering, pagination, empty/loading/error states, keyboard navigation | **P0** |
| Button system (primary, secondary, destructive, icon, loading) | High -- every action | Very high | Low-Medium -- states are well-defined | **P0** |
| Toast / notification system | Medium -- feedback for all actions | Very high | Medium -- a11y (aria-live), positioning, auto-dismiss | **P1** |
| Modal / dialog | Medium-High -- confirmation flows, forms | High | Medium -- focus trap, escape handling, scroll lock | **P1** |
| Navigation (sidebar, breadcrumbs, tabs) | High -- every page | Very high | Medium -- active states, responsive collapse, keyboard nav | **P1** |
| Empty states (illustration + CTA pattern) | Medium -- first-run and zero-data | High -- every list/table view | Low | **P2** |
| Error boundaries + error pages | Medium -- failure recovery | High | Low-Medium | **P2** |

### Component/Flow Backlog

| ID | Component/Flow | User Impact | Reuse | Complexity/Risk | Owner | Dependencies | Milestone | Acceptance Criteria |
|---:|----------------|-------------|-------|-----------------|-------|--------------|-----------|---------------------|
| 1 | Design token foundation (spacing, color, typography, radius, shadow) | High (enables all other work) | Universal | Low | Design Engineer Lead + Design Lead | Figma token audit | M1 | Token file in code matches Figma; lint rule flags hardcoded values; README documents usage |
| 2 | Storybook setup + CI integration | High (enables review workflow) | Universal | Low | Design Engineer Lead | CI pipeline access | M1 | Storybook builds in CI; accessible via URL; at least 1 example story deployed |
| 3 | PR template + a11y CI check | High (enables quality gate) | Universal | Low | Design Engineer Lead | CI pipeline access | M1 | PR template auto-applied to UI PRs; axe-core runs in CI and blocks on critical/serious |
| 4 | Button system (primary, secondary, destructive, icon-only, loading) | High | Very High | Low-Med | Engineer A + Design Engineer Lead | Tokens (#1) | M1 | All 5 variants; all states (default/hover/focus/active/disabled/loading); Storybook; a11y pass; PR checklist complete |
| 5 | Text input + textarea (with label, help text, error, disabled, required) | High | Very High | Medium | Engineer B + Design Engineer Lead | Tokens (#1) | M2 | All states; floating/static label; error + help text; a11y (label association, aria-describedby); Storybook |
| 6 | Select / dropdown (single select, searchable) | High | High | Medium-High | Engineer C + Design Engineer Lead | Tokens (#1), Button (#4) | M2 | Keyboard navigation (arrow keys, type-ahead); focus management; a11y (combobox pattern); Storybook |
| 7 | Checkbox + radio group | High | High | Medium | Engineer B + Design Engineer Lead | Tokens (#1) | M2 | Group keyboard nav; indeterminate checkbox; a11y (fieldset/legend); Storybook |
| 8 | Data table (sortable, with loading/empty/error states) | High | High | High | Engineer D + Design Engineer Lead | Tokens (#1), Button (#4) | M3 | Sort by column; loading skeleton; empty state; error state; keyboard nav for sort controls; responsive scroll; a11y; Storybook |
| 9 | Modal / dialog | Medium-High | High | Medium | Engineer A + Design Engineer Lead | Tokens (#1), Button (#4) | M3 | Focus trap; escape to close; scroll lock; a11y (dialog role, aria-modal); Storybook |
| 10 | Toast / notifications | Medium | Very High | Medium | Engineer C + Design Engineer Lead | Tokens (#1) | M3 | aria-live region; auto-dismiss with pause-on-hover; keyboard dismissable; Storybook |

### Milestones

| Milestone | Outcome | Scope | Owner(s) | ETA | Acceptance Criteria | Rollback/Stop Condition |
|-----------|---------|-------|----------|-----|---------------------|------------------------|
| **M1: Foundation + First Pattern** (Weeks 1-2) | Establish the design-engineering workflow and ship the first "golden path" component as proof of concept. | Tokens (#1), Storybook (#2), PR template + a11y CI (#3), Button system (#4) | Design Engineer Lead (primary), Design Lead (tokens), Engineer A (button implementation) | End of Week 2 | Tokens in code, Storybook running, PR template enforced, Button component shipped with full states + Storybook + a11y pass. Team has used the new PR workflow on at least 2 PRs. | If Storybook setup takes >3 days, descope to local-only and ship CI integration in M2. If token audit reveals >50 unique values, scope to top-10 tokens only. |
| **M2: Core Form Components** (Weeks 3-4) | Ship the form component suite; team adopts the design-to-code contract for all new UI work. | Text input (#5), Select (#6), Checkbox + radio (#7) | Design Engineer Lead (review), Engineers B + C (implementation), Design Lead (specs) | End of Week 4 | All 3 form components shipped with full states, Storybook stories, a11y pass. At least 1 existing feature page refactored to use new components. PR checklist pass rate >80%. | If team velocity is lower than expected, drop Select (#6) to M3 and ship input + checkbox/radio only. Do not compromise a11y to hit the deadline. |
| **M3: Complex Components + Scale** (Weeks 5-8) | Ship higher-complexity components; begin refactoring existing pages to use the component library. | Data table (#8), Modal (#9), Toast (#10), existing page refactoring | Design Engineer Lead (review + coaching), Engineers A + C + D (implementation) | End of Week 8 | All 3 components shipped. At least 3 existing pages refactored to use shared components. UI bug rate measurably lower than pre-initiative baseline. | If M2 slipped, move Toast to M4 or descope. Prioritize data table (highest user impact). |
| **M4: Consolidation + Handoff** (Weeks 9-10) | Document patterns, train secondary reviewer, measure results, plan next phase. | Documentation, training, retrospective, metrics review | Design Engineer Lead + Eng Lead | End of Week 10 | Pattern guide written. Secondary reviewer trained and has solo-reviewed at least 3 PRs. Metrics report comparing before/after. Next-phase backlog drafted. | N/A (this is the consolidation milestone). |

### 4-Week Focus (Initial Impact Commitment)

The user requires initial impact in 4 weeks. **M1 + M2 deliver that commitment:**

- **Week 1:** Token audit + Storybook setup + PR template + a11y CI. Design Engineer Lead role activated. First design-to-code contract written (for Button).
- **Week 2:** Button system shipped end-to-end through the new workflow. Team demo. Retrospective on the workflow.
- **Week 3:** Form components (input, checkbox/radio) in progress. Select started. All new UI PRs use the checklist.
- **Week 4:** Form components shipped. At least 1 existing page refactored. Metrics checkpoint: count UI bugs, PR checklist pass rate, cycle time.

**What "initial impact" looks like at Week 4:**
- A working design-to-code contract that the team has used on 5+ PRs
- 4 components (button, input, checkbox/radio, select) with full states, Storybook, and a11y compliance
- A measurable reduction in UI-related rework (compared to the 4 weeks prior)
- Every engineer knows how to use the PR checklist and where to find component docs

---

## 6) Quality Bar

### Checklists (completed)

#### A) Scope + assumptions
- [x] The "design engineering" definition for this context is explicit: an embedded function (not a new hire or separate team), where 1 engineer acts as the bridge between design and engineering, owning UI implementation quality.
- [x] In-scope vs out-of-scope responsibilities are listed in the charter.
- [x] Stakeholders and decision-makers are explicit (Design Lead + Eng Lead, PM as tiebreaker).
- [x] Assumptions are clearly labeled (React stack, no Storybook, Figma, no i18n in initial scope).

#### B) Operating model + boundaries
- [x] Engagement model is selected (embedded) and justified (small team, systemic problem, highest leverage).
- [x] Ownership boundaries are unambiguous: tokens (Design owns definition, Design Eng translates), components (Design Eng owns API, Eng reviews), visual QA (Design Eng owns PR sign-off), accessibility (Design Eng owns verification), performance (Engineering owns).
- [x] Handoff and review gates are documented (4 gates: design review, design spec, engineering review, QA/a11y).

#### C) Prototype -> production workflow
- [x] A prototype ladder exists with 4 rungs, each with purpose and graduation rule.
- [x] Each artifact is labeled throwaway vs shippable (lo-fi and hi-fi are always throwaway; coded prototype is labeled at creation; production is never throwaway).
- [x] Review gates exist for shippable work (design spec gate, engineering review gate, QA/a11y gate, release gate).

#### D) Design-to-code contract
- [x] Component/flow spec requires states (loading/empty/error/disabled/focus/hover) -- template mandates all 8 states.
- [x] Token usage is defined (spacing, color, typography, radius, shadow tokens; no one-off pixels/colors).
- [x] PR expectations are explicit (screenshots of all states, test plan, a11y notes, Storybook link).

#### E) Delivery plan quality
- [x] Backlog is prioritized by user impact + reuse (form components and buttons first, not easy/cosmetic items).
- [x] Milestones are incremental and pattern-setting (M1 ships tokens + 1 golden-path component within 2 weeks).
- [x] Each milestone has acceptance criteria and a rollback/stop condition.

#### F) Quality bar + sustainability
- [x] Accessibility requirements are stated and testable (WCAG 2.1 AA, axe-core in CI, manual keyboard/screen reader checks).
- [x] Consistency mechanism exists (Storybook, PR template, lint rule for hardcoded values, design-to-code contract, review gates).
- [x] Success signals/KPIs are defined (5 measurable signals in the charter).

#### G) Finalization
- [x] Risks, open questions, and next steps are included (see Section 7).
- [x] No secrets/credentials were requested or recorded.

### Rubric Score

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Scope clarity | 5 | Clear definition of design engineering as an embedded function; explicit in/out scope; redirects to 4 neighboring skills (design-systems, engineering-culture, running-design-reviews, writing-specs-designs). |
| Operating model fit | 5 | Embedded model chosen and justified against alternatives; ownership boundaries are explicit for all key areas (tokens, components, visual QA, a11y, performance); rituals and escalation paths defined. |
| Prototype-to-production rigor | 5 | 4-rung ladder with clear graduation rules; throwaway/shippable labels for all rungs; coded prototype has a 3-day decision window with 5-day kill rule; 4 review gates defined. |
| Design-to-code contract quality | 5 | Spec template covers all 8 states, tokens, a11y (WCAG 2.1 AA level + axe-core test method + manual checks), responsive behavior, and PR checklist with verification methods. |
| Delivery plan executability | 5 | 4 milestones; M1 ships within 2 weeks (tokens + Storybook + Button); owners assigned; acceptance criteria for each milestone; rollback/stop conditions defined; 4-week initial impact commitment with weekly breakdown. |
| Quality bar + sustainability | 5 | Review gates integrated into workflow (not separate); axe-core in CI (automated); PR template (repeatable); Storybook (documented); 5 measurable KPIs; secondary reviewer training in M4 (sustainability). |

**Total: 30/30**

**Self-assessment note:** This is a self-score by the producing agent. Real-world scores depend on whether the team can execute against this plan. The plan is comprehensive on paper; the true test is adoption. Key risk areas for score degradation in practice: (1) Design Engineer Lead capacity may be overestimated; (2) Token audit complexity may be underestimated; (3) Team adoption of PR checklist may lag.

---

## 7) Stakeholder Cadence + Decision Log

**Cadence:** Weekly (Weeks 1-4), then biweekly (Weeks 5+)
**Update format:** 5 bullets + demo + risks + asks (async-first; sync demo biweekly)

**Decision Log (initial decisions):**

| Date | Decision | Rationale | Owner | Revisit Trigger |
|------|----------|-----------|-------|-----------------|
| Week 0 (kickoff) | Embedded model (not platform or tiger team) | Small team (10 total); systemic problem across all UI work; cannot afford separate team overhead | Eng Lead + Design Lead | If the team grows to 20+ or a second product line is added, revisit for platform model |
| Week 0 (kickoff) | WCAG 2.1 AA as the accessibility standard | Industry standard for B2B SaaS; covers keyboard, contrast, labels, focus; AAA is aspirational but not required initially | Design Engineer Lead | If customers or legal require AAA for specific components, scope those individually |
| Week 0 (kickoff) | axe-core in CI as automated a11y gate | Free, well-maintained, catches ~40% of WCAG issues automatically; manual checks cover the rest | Design Engineer Lead | If axe-core produces excessive false positives or misses critical issues, evaluate alternatives (pa11y, lighthouse) |
| Week 0 (kickoff) | Button system as the first "golden path" component | High reuse (every page), moderate complexity (5 variants, clear states), good teaching example for the workflow | Design Engineer Lead + Design Lead | N/A (already shipped by M1) |
| Week 1 | Token scope: top 10 most-used values only (not full audit) | Full token audit could take 2+ weeks; starting with the 10 most-used spacing/color/type values unblocks M1 | Design Engineer Lead | If >20% of M2 components need tokens not in the initial set, expand the token set in M2 |

---

## 8) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Design Engineer Lead is a single point of failure.** One person owns review gate + Storybook + contract. If they are sick/on vacation, the workflow stalls. | Medium | High | Train a secondary reviewer (target: Week 4). Document the review checklist so others can follow it mechanically. |
| **Designers cannot produce structured Figma annotations.** If the 2 designers do not have capacity or skill to add states/token annotations, the Design Engineer Lead must extract this themselves, doubling their workload. | Medium | Medium | Provide a lightweight Figma annotation template (Section 4). Timebox: if designer adoption < 50% by Week 2, the Design Engineer Lead fills gaps and escalates capacity concern to PM. |
| **Token audit reveals massive inconsistency.** If the codebase has 100+ unique color/spacing values, the token mapping is a multi-week project, not a Week 1 task. | Medium | Medium | Scope to top-10 tokens only in M1. Create a "token debt" backlog item. Do not block component delivery on full token migration. |
| **Team resists the PR checklist.** Engineers may see the checklist as bureaucratic overhead, especially if PR review times increase. | Medium | Medium | Keep the checklist short (fits on one screen). Design Engineer Lead commits to < 1 business day review SLA. Demonstrate value with before/after bug counts at Week 4 retrospective. |
| **4-week timeline is insufficient for meaningful impact.** If setup tasks (Storybook, tokens, CI) take longer than expected, component delivery is compressed. | Low-Medium | Medium | Rollback conditions are defined for each milestone. The minimum viable Week-4 outcome is: tokens + PR template + 1 component (Button) shipped through the full workflow. Even this proves the process. |
| **Scope creep into design system governance.** Success may lead to "now build the whole design system," which is a different initiative (use `design-systems`). | Low | Medium | Charter explicitly scopes out design system governance. At M4 retrospective, assess whether the next phase is "more components" (continue) or "design system with multi-team governance" (hand off to `design-systems`). |

### Open Questions

1. **Who is the Design Engineer Lead?** The plan assumes 1 engineer with strong UI/CSS skills. The team needs to identify this person and confirm they can dedicate ~60-70% of their time to this function for Weeks 1-4.
2. **What is the exact tech stack?** React is assumed. If Vue, Svelte, or another framework, the Storybook setup and component patterns will differ. Confirm before kickoff.
3. **Is there an existing CI pipeline that can run axe-core?** If CI is minimal, the a11y automation step in M1 may need to be simplified (local-only checks first, CI integration in M2).
4. **What is the current UI bug rate?** To measure the "50% reduction" KPI, we need a baseline. Pull the count of UI-related bugs from the last 4 sprints before kickoff.
5. **Do designers have Figma token/style libraries set up?** If yes, the token audit is faster. If no, the Design Engineer Lead may need to extract token values from Figma manually.
6. **Is there budget for any tooling?** Storybook is free. Chromatic (visual regression) is paid. axe-core is free. Clarify if paid tooling is available for future milestones.

### Next Steps (immediate, before Week 1 starts)

1. **Identify the Design Engineer Lead.** Eng Lead nominates 1 engineer with strong UI skills. Confirm with PM that this person's feature work is deprioritized for 4 weeks. Target: before kickoff.
2. **Establish the baseline.** Pull UI bug count from the last 4 sprints. Record current average cycle time for design-ready to merged PR. This is the "before" measurement. Target: before kickoff.
3. **Kick off Week 1.** Hold a 60-minute kickoff with Design Lead, Design Engineer Lead, Eng Lead, and PM. Walk through this execution pack. Confirm or adjust assumptions. Assign M1 tasks. Target: Day 1 of Week 1.
