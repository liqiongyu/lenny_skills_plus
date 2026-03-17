# Design Review Pack: Web Onboarding Flow (Flow A vs. Flow B)

**Review Type:** Live Design Review (45 minutes)
**Date:** 2026-03-17
**Decision:** Choose between Flow A and Flow B for next sprint
**Target User:** First-time admin setting up a team
**Constraints:** WCAG AA accessibility, limited engineering bandwidth

---

## 1. Review Agenda (45 Minutes)

| Time | Activity | Owner |
|------|----------|-------|
| 0:00 - 0:05 | Context setting: problem statement, user persona, constraints | Facilitator |
| 0:05 - 0:15 | Walkthrough of Flow A | Designer |
| 0:15 - 0:25 | Walkthrough of Flow B | Designer |
| 0:25 - 0:35 | Comparative evaluation against criteria | All |
| 0:35 - 0:40 | Decision and rationale | Decision-maker |
| 0:40 - 0:45 | Action items, owners, next steps | Facilitator |

---

## 2. Review Attendees and Roles

| Role | Responsibility | Name |
|------|---------------|------|
| **Facilitator** | Keep time, enforce ground rules, capture decisions | |
| **Designer / Presenter** | Walk through both flows, explain design rationale | |
| **Product Manager** | Represent user and business priorities, make final call | |
| **Engineering Lead** | Assess feasibility, complexity, and bandwidth fit | |
| **Accessibility Specialist** (if available) | Evaluate WCAG AA compliance for both flows | |
| **Note-taker** | Document discussion, decisions, and action items | |

---

## 3. Ground Rules

1. Critique the design, not the designer.
2. Frame feedback as questions or suggestions ("Have we considered...?" rather than "This is wrong").
3. Stay focused on the target user (first-time admin) and stated constraints.
4. Reserve opinions on scope or timeline for the structured discussion block.
5. The facilitator may table tangential topics to a parking lot list.

---

## 4. Context and Problem Statement

### The Problem

First-time admins who sign up for our product need to set up their team (invite members, configure roles, establish basic settings) before they can derive value. Today this process is unguided, leading to drop-off during setup and an elevated volume of support tickets. We need a structured onboarding flow that gets admins to a fully configured team quickly and confidently.

### Target User: First-Time Admin

- **Who they are:** Someone (likely a team lead, manager, or IT coordinator) who has just signed up or been granted admin access and needs to configure the product for their team.
- **Mental state:** A mix of motivation (they chose the product or were tasked with setting it up) and anxiety (unfamiliar interface, pressure to get it right for the team, possibly evaluating the product).
- **Core jobs to be done:**
  1. Create or name the workspace/organization
  2. Invite team members
  3. Assign roles and basic permissions
  4. Configure foundational settings (timezone, notifications, defaults)
  5. Understand what happens next (the first team experience)
- **Key concerns:** "Am I doing this right?", "Can I change this later?", "How long will this take?"
- **Technical sophistication:** Varies widely. Must design for the least technical admin who could reasonably hold this role.

### Success Metrics

- Onboarding completion rate (target: >80%)
- Time to first team invite sent
- Time to fully functional team workspace
- Support ticket volume related to setup (target: measurable reduction)
- WCAG AA audit pass rate

### Hard Constraints

- **WCAG AA compliance** -- all interactive elements must meet contrast ratios, keyboard navigability, screen reader compatibility, and focus management standards. This is non-negotiable.
- **Limited engineering bandwidth** -- the chosen flow must be buildable within a single sprint by the available team. Prefer reuse of existing design system components.

---

## 5. Evaluation Criteria

Each flow should be evaluated against the following criteria, weighted by importance given the constraints.

### 5.1 Usability (Weight: High)

- **Clarity of progression:** Does the user always know where they are, what step they are on, and how many steps remain?
- **Cognitive load:** How many decisions does each screen require? Are choices presented clearly without overwhelming?
- **Error prevention and recovery:** Does the flow prevent common mistakes? Can the user go back without losing data?
- **Time to completion:** Estimated time from start to a functional team setup.
- **Flexibility:** Can the user skip optional steps and return later?
- **Reversibility messaging:** Does the UI communicate what can be changed later?

### 5.2 Accessibility -- WCAG AA Compliance (Weight: High)

- **Color contrast:** All text meets minimum 4.5:1 ratio (3:1 for large text). Non-text UI components meet 3:1.
- **Keyboard navigation:** Entire flow is completable via keyboard alone. Logical tab order, visible focus indicators on all interactive elements. No keyboard traps.
- **Screen reader compatibility:** All interactive elements have proper labels, ARIA attributes where needed, meaningful heading hierarchy (h1 > h2 > h3, no skipped levels).
- **Form design:** Labels are visibly and programmatically associated with inputs. Error messages are specific and linked via `aria-describedby`. Required fields indicated by more than color alone.
- **Motion and animation:** Any transitions respect `prefers-reduced-motion`. No content dependent solely on animation.
- **Touch targets / interactive element sizing:** Minimum 44x44px for interactive elements.
- **Zoom:** Flow works correctly at 200% browser zoom without horizontal scrolling or content loss.

### 5.3 Engineering Feasibility (Weight: High)

- **Component reuse:** How much of the flow can be built with existing design system components?
- **New components needed:** Each new component adds design, build, and test overhead.
- **API complexity:** How many backend endpoints does the flow require? Are they already built?
- **State management:** Multi-step flows with branching or partial-save requirements are harder to implement than simpler patterns.
- **Testing surface area:** Simpler flows are easier to test thoroughly within limited bandwidth.
- **Sprint fit:** Can the entire flow be completed in one sprint, including accessibility testing?

### 5.4 Business Impact (Weight: Medium)

- **Activation rate impact:** Which flow is more likely to get users to a meaningful "aha moment" (team is configured and functional)?
- **Drop-off risk:** Where are the likely abandonment points in each flow?
- **Support burden:** Which flow will generate fewer support tickets?
- **Scalability:** Does the flow accommodate future features (SSO, SCIM, billing setup, role-based access) without a full redesign?

### 5.5 Design Quality (Weight: Medium)

- **Visual consistency:** Does the flow align with the existing design system and brand guidelines?
- **Information hierarchy:** Is the most important information and primary action prominent on each screen?
- **Empty states and edge cases:** What happens with zero team members? Very long organization names? Slow network connections? Browser back button?
- **Copy and microcopy:** Is the language clear, concise, and encouraging? Does it avoid jargon?

---

## 6. Comparative Scorecard

Use the following scorecard during the live review. Each reviewer scores 1-5 per criterion (1 = poor, 5 = excellent).

| Criterion | Flow A (1-5) | Flow A Notes | Flow B (1-5) | Flow B Notes |
|-----------|-------------|--------------|-------------|--------------|
| Clarity of progression | | | | |
| Cognitive load per screen | | | | |
| Error prevention / recovery | | | | |
| Estimated time to complete | | | | |
| Skip / defer flexibility | | | | |
| Color contrast (WCAG AA) | | | | |
| Keyboard navigability | | | | |
| Screen reader compatibility | | | | |
| Form accessibility | | | | |
| Focus management | | | | |
| Component reuse (existing DS) | | | | |
| New components needed | | | | |
| API / backend complexity | | | | |
| State management complexity | | | | |
| Activation likelihood | | | | |
| Drop-off risk (lower = better) | | | | |
| Visual consistency with DS | | | | |
| Edge case handling | | | | |
| Copy / microcopy quality | | | | |
| Future extensibility | | | | |
| **Total** | **___/100** | | **___/100** | |

---

## 7. Accessibility Audit Checklist

Before shipping, the selected flow must pass all items in the "Must-Have" section.

### Must-Have (WCAG AA -- Sprint Blocker)

- [ ] All text meets 4.5:1 contrast ratio against its background
- [ ] All large text (18px+ regular or 14px+ bold) meets 3:1 contrast ratio
- [ ] Non-text UI components (icons, borders, focus rings) meet 3:1 contrast ratio
- [ ] Every form input has a visible, programmatically associated `<label>`
- [ ] Required fields are indicated by more than color alone (e.g., text or icon)
- [ ] Error messages are specific, visible, and linked to the field via `aria-describedby`
- [ ] All interactive elements are reachable and operable by keyboard
- [ ] Focus order follows logical reading/interaction order
- [ ] Focus indicator is clearly visible on all interactive elements
- [ ] No keyboard traps exist in modals, dropdowns, or multi-step components
- [ ] Page has a logical heading hierarchy (h1 > h2 > h3, no skipped levels)
- [ ] All images and icons have appropriate alt text (or `aria-hidden="true"` if decorative)
- [ ] Progress indicator (stepper / progress bar) conveys current step to screen readers
- [ ] Page works at 200% browser zoom without horizontal scrolling or content loss
- [ ] No information is conveyed by color alone
- [ ] Status changes (e.g., "Step completed") are announced to assistive technology

### Should-Have (Best Practice -- Ship If Bandwidth Allows)

- [ ] `prefers-reduced-motion` is respected for all transitions and animations
- [ ] Loading states announce to screen readers via `aria-live` regions
- [ ] Inline validation provides immediate, accessible feedback
- [ ] Skip navigation link is available if header/nav is present during onboarding
- [ ] Autocomplete attributes are set on relevant fields (name, email)
- [ ] Touch targets are minimum 44x44px on mobile viewports
- [ ] Error summary at top of form with links to each invalid field

---

## 8. Discussion Prompts

Use these to structure the 10-minute comparative discussion block:

1. **User fit:** Given that our target is a first-time admin with unknown technical ability, which flow reduces the chance they get stuck, confused, or overwhelmed?
2. **Accessibility cost:** Which flow can we ship at WCAG AA with less custom ARIA work and fewer edge cases? Where are the accessibility pitfalls in each?
3. **Bandwidth reality check:** Engineering lead -- given current capacity, which flow is realistically shippable in one sprint? Are there hidden costs (state persistence, partial-save, email integration) in either approach?
4. **Drop-off and resumability:** Which flow is more forgiving if the admin leaves mid-setup and returns later? What does the partial-completion state look like?
5. **Future-proofing:** We may add SSO configuration, billing setup, and SCIM provisioning later. Which pattern extends more gracefully?
6. **Copy and guidance:** Does either flow rely on copy/microcopy that we have not yet written? Is a content/UX writing pass needed before sprint?

---

## 9. Engineering Scoping Questions

These questions should be answered during or immediately after the review to inform sprint planning:

1. How many unique screens/routes does each flow require?
2. Which steps involve new API endpoints vs. existing ones?
3. Does either flow require new backend logic (e.g., invite system, permission setup, email sending)?
4. What percentage of UI components already exist in the design system? List any net-new components needed.
5. Does either flow involve conditional/branching logic? (Branching adds significant state management complexity.)
6. What is the data persistence model? Can a user close the browser mid-flow and resume?
7. Are there third-party integrations in either flow? (Email delivery, SSO providers, calendar)
8. What analytics events need to be instrumented for funnel tracking?
9. What is the estimated engineering effort for each flow? (T-shirt size or story points)
10. What can be deferred to a fast-follow iteration without degrading the core experience?

---

## 10. Decision Framework

After scoring, use this framework to make the final call.

### Priority Order for Tiebreakers

1. **Buildable in one sprint?** If only one flow fits the bandwidth, that is the answer. A well-executed simple flow beats a rushed complex one.
2. **WCAG AA achievable without extensive custom workarounds?** Prefer the flow with a simpler, more reliable accessibility story.
3. **Higher predicted completion rate for first-time admins?** Prefer the flow that better serves the target user and reduces drop-off.

### If Scores Are Close (Within 10%)

Choose the flow with lower engineering complexity, given the bandwidth constraint. A simpler flow shipped with polish and full accessibility beats a complex flow shipped with gaps.

### If One Flow Wins on Usability but Loses on Feasibility

Explore whether a scoped-down version of the better-designed flow can fit within sprint capacity. Identify which features or steps can be deferred to a fast-follow.

### If Accessibility Compliance Differs Significantly

Accessibility is non-negotiable. If one flow has fundamental accessibility issues that cannot be resolved within the sprint, it cannot be selected regardless of other scores.

### Decision Options

- **Ship Flow A** -- proceed with this pattern as designed
- **Ship Flow B** -- proceed with this pattern as designed
- **Ship Flow [A/B] with modifications** -- specify exact changes and confirm they fit in sprint
- **Hybrid** -- combine elements from both (only if engineering and design confirm feasibility within sprint)
- **Defer** -- neither flow is ready; specify what must change before re-review

---

## 11. Decision Record

*To be completed during the review meeting:*

**Decision:** ___________________________

**Rationale (2-5 sentences):**

___________________________

___________________________

___________________________

**Key trade-offs accepted:**

1. ___________________________
2. ___________________________
3. ___________________________

**Dissenting views (if any):**

___________________________

**Deferred items (fast-follow backlog):**

1. ___________________________
2. ___________________________
3. ___________________________

**Accessibility risk items requiring follow-up:**

1. ___________________________
2. ___________________________

---

## 12. Action Items

| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 | Finalize high-fidelity designs for selected flow | Design | | |
| 2 | Complete accessibility annotation pass on final designs | Design | | |
| 3 | Break flow into engineering stories with estimates | Eng Lead | | |
| 4 | Write acceptance criteria for each story (include a11y) | PM + Design | | |
| 5 | Set up analytics events and funnel tracking plan | Eng + PM | | |
| 6 | Conduct screen reader testing on prototype | QA / A11y | | |
| 7 | Finalize onboarding copy and microcopy | Content / PM | | |
| 8 | Create fast-follow tickets for deferred items | PM | | |
| 9 | Schedule mid-sprint check-in on accessibility progress | Facilitator | | |
| 10 | Circulate this decision record to all stakeholders | Note-taker | Within 24h | |

---

## 13. Pre-Read Checklist (Send to Attendees 24h Before Review)

- [ ] Review this Design Review Pack document
- [ ] Walk through the Figma prototype for Flow A and Flow B (links to be attached by designer)
- [ ] Note your top concern or question for the discussion block
- [ ] Engineering: prepare a rough effort estimate for each flow (T-shirt size)
- [ ] Accessibility: do a preliminary scan of both flows for obvious WCAG issues

---

## 14. Post-Review Checklist

- [ ] Decision record completed and circulated to all attendees within 24 hours
- [ ] Figma file annotated: selected flow marked "Approved," rejected flow marked "Not selected"
- [ ] Engineering stories created in sprint backlog
- [ ] Accessibility acceptance criteria added to every engineering ticket
- [ ] QA informed of WCAG AA testing requirements and provided with testing checklist
- [ ] Parking lot items assigned owners and target dates
- [ ] Fast-follow items added to product backlog with priority

---

## 15. Post-Launch Metrics to Track

Once the selected flow ships, track these metrics to validate the decision and inform iteration:

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| Onboarding completion rate | >80% | Analytics funnel |
| Step-by-step drop-off | Identify top drop-off step | Funnel analysis per step |
| Time to complete setup | <10 minutes median | Event timestamps |
| Invite acceptance rate | >60% within 7 days | Invite tracking |
| Setup-related support tickets | Measurable reduction vs. baseline | Support system tagging |
| Return-to-settings rate | Track within 48h | Analytics |
| Keyboard-only completion | Functional | Manual QA + usability testing |
| Screen reader completion | Functional | Manual QA + usability testing |
