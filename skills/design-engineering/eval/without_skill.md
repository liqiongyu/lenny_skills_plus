# Design Engineering Execution Plan

## Context & Problem Statement

**Team:** 2 designers, 8 engineers (B2B SaaS web app)
**Core Problem:** Shipping slowly because UI polish and edge states get missed, leading to rework cycles.
**Goal:** Reduce rework and increase visual/interaction consistency.
**Constraints:** Accessibility (WCAG 2.1 AA minimum) is required; need initial measurable impact within 4 weeks.

---

## Root Cause Analysis

Before jumping to solutions, the rework and inconsistency issues likely stem from several interrelated causes:

1. **No single source of truth for UI.** Designers produce mockups, engineers interpret them differently, and there is no shared component library enforcing constraints.
2. **Edge states not designed upfront.** Happy-path mockups are handed off without loading, empty, error, partial-data, and permission-denied states being specified.
3. **Accessibility treated as afterthought.** A11y issues are caught in QA or by customers, causing rework.
4. **Review bottleneck.** 2 designers cannot review 8 engineers' output in real time, so polish issues slip through.
5. **No shared language for "done."** Engineers and designers have different definitions of what constitutes a finished UI.

---

## Execution Plan Overview

The plan is organized into three workstreams across four weeks, with a phased rollout:

| Week | Focus | Key Deliverable |
|------|-------|-----------------|
| 1 | Foundation & Audit | Component inventory, edge-state checklist, shared definition of done |
| 2 | Build Core System | Token system, 10 core components, accessibility baseline |
| 3 | Integrate & Adopt | Storybook deployment, PR workflow, first feature shipped with new system |
| 4 | Harden & Measure | Full coverage of top flows, metrics dashboard, retrospective |

---

## Week 1: Foundation & Audit

### 1.1 UI Component Inventory (Days 1-2)

**Owner:** 1 designer + 1 engineer (pair)

Audit the existing application and catalog every distinct UI element:

- Buttons (primary, secondary, tertiary, destructive, icon-only)
- Form inputs (text, select, multiselect, date picker, file upload)
- Feedback elements (toasts, banners, modals, inline errors)
- Navigation (sidebar, tabs, breadcrumbs, pagination)
- Data display (tables, cards, stat widgets, avatars, badges)
- Layout primitives (containers, grids, spacers, dividers)

**Output:** A spreadsheet or Notion database with columns: Component Name, Current Variants, Inconsistencies Found, Frequency of Use, Accessibility Issues Noted.

Prioritize the top 10 most-used components for Week 2 buildout.

### 1.2 Edge State Checklist (Days 2-3)

**Owner:** 1 designer

Create a canonical checklist of states every screen/component must address before being considered "designed." At minimum:

- **Empty state** - First use, no data yet
- **Loading state** - Skeleton or spinner while data fetches
- **Error state** - API failure, timeout, 403/404
- **Partial data** - Some fields missing or null
- **Overflow** - Long text, many items, large numbers
- **Permission-denied** - User lacks access
- **Offline / degraded** - Network interruption (if applicable)
- **Responsive breakpoints** - Mobile, tablet, desktop
- **Keyboard navigation** - Tab order, focus rings, escape-to-close
- **Screen reader** - Labels, roles, live regions

**Output:** A markdown checklist template that designers attach to every spec and engineers reference in PR self-review.

### 1.3 Definition of Done (Day 3)

**Owner:** Whole team (1-hour meeting)

Agree on a shared "UI Definition of Done" that a feature must satisfy before it can be merged:

1. All edge states from the checklist are implemented.
2. Component uses the shared design tokens (or documents why not).
3. Passes axe-core automated accessibility scan with zero critical/serious violations.
4. Keyboard navigable (Tab, Enter, Escape, Arrow keys where appropriate).
5. Tested at 200% browser zoom without layout breakage.
6. Designer has approved the implementation (async screenshot review or Storybook link).
7. No hardcoded colors, font sizes, or spacing values outside the token system.

### 1.4 Tooling Setup (Days 3-5)

**Owner:** 1 engineer

- Initialize a shared component library package (e.g., `@company/ui`), even if it starts nearly empty.
- Set up Storybook with:
  - Accessibility addon (`@storybook/addon-a11y`) running axe-core on every story.
  - Viewport addon for responsive testing.
  - Dark mode toggle (if applicable).
- Set up a CI step that runs `axe-core` on Storybook stories and fails the build on critical violations.
- Configure a Chromatic or Percy account for visual regression testing (even a free tier is fine to start).

---

## Week 2: Build Core System

### 2.1 Design Token System (Days 1-2)

**Owner:** 1 designer + 1 engineer

Define and implement a token system covering:

**Color tokens:**
```
--color-primary-500: #2563EB;
--color-primary-600: #1D4ED8;  /* hover */
--color-primary-700: #1E40AF;  /* active */
--color-neutral-50 through --color-neutral-900
--color-success-500, --color-warning-500, --color-error-500
--color-focus-ring: #2563EB;   /* 3:1 contrast minimum against background */
```

**Spacing scale:**
```
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-6: 24px;
--space-8: 32px;
--space-12: 48px;
--space-16: 64px;
```

**Typography scale:**
```
--text-xs: 12px / 16px
--text-sm: 14px / 20px
--text-base: 16px / 24px
--text-lg: 18px / 28px
--text-xl: 20px / 28px
--text-2xl: 24px / 32px
```

**Other tokens:** border-radius (sm/md/lg/full), shadow (sm/md/lg), transition durations, z-index scale.

All colors must meet WCAG 2.1 AA contrast ratios (4.5:1 for normal text, 3:1 for large text and UI components).

**Output:** A CSS custom properties file (or Tailwind config extension) plus a Figma style library synced to the same values.

### 2.2 Core Component Library (Days 2-5)

**Owner:** 2 engineers (pair programming), 1 designer reviewing

Build the top 10 prioritized components from the Week 1 audit. Each component must include:

**Accessibility requirements per component type:**

| Component | A11y Requirements |
|-----------|-------------------|
| Button | `role="button"`, visible focus ring, `aria-disabled` not just `disabled`, loading state announced |
| TextInput | Associated `<label>`, `aria-describedby` for help text, `aria-invalid` + `aria-errormessage` for errors |
| Select | Keyboard operable (arrow keys, type-ahead), `aria-expanded`, `aria-activedescendant` |
| Modal | Focus trap, `role="dialog"`, `aria-labelledby`, return focus on close, Escape to dismiss |
| Toast | `role="alert"` or `aria-live="polite"`, auto-dismiss with pause-on-hover, not blocking content |
| Table | `<caption>`, `scope` attributes on headers, sortable columns announced |
| Tabs | `role="tablist/tab/tabpanel"`, arrow key navigation, `aria-selected` |
| Dropdown Menu | `role="menu/menuitem"`, arrow key navigation, Escape to close, `aria-haspopup` |
| Checkbox/Radio | Native elements or correct ARIA roles, group labels with `fieldset/legend` |
| Alert/Banner | `role="alert"` for urgent, `role="status"` for informational, dismissible with keyboard |

**Each component ships with:**
- TypeScript props interface with JSDoc
- Default, hover, active, focus, disabled, loading, and error visual states
- Storybook stories covering all states
- Unit tests for keyboard interaction
- axe-core passing in Storybook

### 2.3 Figma Component Sync (Days 3-5)

**Owner:** 2 designers

Rebuild the top 10 components in Figma to match the coded versions exactly:
- Use auto-layout and Figma variables mapped to the token system.
- Include all states as variants.
- Add usage guidelines and do/don't examples in Figma.
- Name layers to match code prop names (so handoff is unambiguous).

---

## Week 3: Integrate & Adopt

### 3.1 Migration Pattern (Day 1)

**Owner:** 1 engineer

Create a migration guide and codemod (or find-and-replace script) for the most common replacements:

- Replace hardcoded hex colors with token variables.
- Replace inline styles with component library imports.
- Replace custom button implementations with `<Button>` from the library.

The goal is NOT to migrate the entire app in one week. The goal is to establish the pattern and migrate the top 3 most-trafficked pages/flows.

### 3.2 PR Review Workflow (Days 1-2)

**Owner:** 1 designer + 1 engineer lead

Establish a lightweight but enforced review process:

**For every PR that touches UI:**

1. **Self-review:** Engineer runs through the edge-state checklist before requesting review.
2. **Automated checks (CI):**
   - axe-core scan on affected Storybook stories (zero critical/serious violations).
   - Visual regression test (Chromatic/Percy) flags any unintended pixel changes.
   - Lint rule: no hardcoded color/spacing values outside tokens.
3. **Designer review (async):**
   - Engineer posts a Storybook link or screenshots (all states) in the PR.
   - Designer approves or requests changes. Target: review within 4 hours.
   - For small changes (copy, spacing), designer approval can be post-merge with a follow-up ticket.
4. **Accessibility spot-check:** For complex interactive components, manual keyboard + VoiceOver/NVDA test (rotate this duty among engineers weekly).

**Key rule:** No PR merges with a "TODO: add loading state" comment. If the state is in the checklist, it ships or the PR doesn't merge.

### 3.3 First Feature with New System (Days 2-5)

**Owner:** Full team

Pick one upcoming feature (ideally medium complexity, customer-facing) and build it entirely with the new system:

- Designer specs in Figma using the new component library, with all edge states annotated.
- Engineers build using only shared components and tokens.
- Track: time to design, time to implement, number of review rounds, number of bugs found in QA.

This is the proof-of-concept that demonstrates the new workflow end-to-end.

---

## Week 4: Harden & Measure

### 4.1 Expand Component Coverage (Days 1-3)

**Owner:** 2 engineers

Based on what was learned in Week 3, build the next tier of components (the ones that came up as missing during the feature build). Typical candidates:

- Data table with sorting, filtering, pagination
- Form validation patterns (inline errors, summary errors)
- Empty state illustrations/templates
- Skeleton loaders for each major content type
- Confirmation dialogs (destructive action pattern)

### 4.2 Accessibility Audit of Top 5 Flows (Days 2-4)

**Owner:** 1 engineer + 1 designer

Conduct a manual accessibility audit of the five most-used user flows:

1. Sign up / onboarding
2. Core workflow (whatever the main JTBD is)
3. Settings / account management
4. Search / filtering
5. Data export / reporting

For each flow, test:
- Keyboard-only navigation (can complete the flow without a mouse?)
- Screen reader (VoiceOver on Mac, NVDA on Windows): are all elements announced correctly?
- Zoom to 200%: does layout hold?
- Color contrast: run axe-core and fix remaining issues.
- Motion: does `prefers-reduced-motion` disable animations?

**Output:** A prioritized list of accessibility fixes, categorized as P0 (blocking, legal risk), P1 (significant usability impact), P2 (improvement).

### 4.3 Metrics Dashboard (Days 3-4)

**Owner:** 1 engineer

Set up tracking for the metrics that matter:

| Metric | How to Measure | Baseline (Week 1) | Target (Week 8) |
|--------|---------------|-------------------|-----------------|
| UI-related bug tickets per sprint | Jira/Linear label | Count current | 50% reduction |
| Avg review rounds per UI PR | GitHub PR data | Count current | < 2 rounds |
| axe-core violations in CI | CI logs | Count current | Zero critical/serious |
| Time from design handoff to PR merge | Ticket timestamps | Measure current | 30% reduction |
| Component library adoption | % of UI PRs importing from `@company/ui` | 0% | > 60% |
| Visual regression catches | Chromatic/Percy alerts | N/A | Tracking started |

### 4.4 Retrospective (Day 5)

**Owner:** Whole team (1-hour meeting)

Discuss:
- What worked? What didn't?
- Where did the new system save time? Where did it add friction?
- Which components are still missing?
- Is the designer review workflow sustainable at current velocity?
- What should the next 4-week cycle focus on?

---

## Embedded Operating Model

The plan above gets you through the first 4 weeks. Below is the ongoing operating model that sustains and scales the system.

### Roles & Responsibilities

| Role | Person(s) | Ongoing Responsibilities |
|------|-----------|------------------------|
| **Design System Owner** | 1 designer (designated) | Maintains Figma library, reviews all new component proposals, owns token system, publishes changelog |
| **Component Library Maintainer** | 1 engineer (designated) | Maintains `@company/ui` package, reviews component PRs, manages versioning and releases |
| **Accessibility Champion** | 1 engineer (rotating monthly) | Runs weekly spot-check on one flow, triages axe-core CI failures, mentors team on a11y patterns |
| **All Engineers** | 8 engineers | Use shared components, follow edge-state checklist, self-review against Definition of Done |
| **All Designers** | 2 designers | Design with the component library, annotate edge states, review UI PRs within 4 hours |

### Cadence

| Frequency | Activity | Participants |
|-----------|----------|-------------|
| **Every PR** | Edge-state checklist self-review, CI accessibility scan, designer async review | PR author + reviewer |
| **Weekly (30 min)** | Design system sync: review new component requests, discuss inconsistencies, triage a11y backlog | Design System Owner + Component Library Maintainer + Accessibility Champion |
| **Bi-weekly** | Component library release (semver, changelog, migration notes if breaking) | Component Library Maintainer |
| **Monthly** | Accessibility audit of 2-3 flows (rotating) | Accessibility Champion + 1 designer |
| **Quarterly** | Full design system review: usage metrics, component coverage, deprecation of unused components, roadmap for next quarter | Whole team |

### Component Lifecycle

```
Proposal --> Review --> Build --> Document --> Release --> Maintain --> Deprecate
```

1. **Proposal:** Anyone files a "New Component" request (template: use case, states needed, a11y requirements, existing alternatives considered).
2. **Review:** Design System Owner + Component Library Maintainer approve or suggest alternatives (< 2 days).
3. **Build:** Designer creates Figma component; engineer implements in code. Pair ideally.
4. **Document:** Storybook stories for all states, JSDoc on props, usage guidelines.
5. **Release:** Included in next bi-weekly release with changelog entry.
6. **Maintain:** Bug fixes, new variants as needed.
7. **Deprecate:** When replaced or unused, mark deprecated for one release cycle, then remove.

### Decision Framework: Build vs. Skip

Not everything needs a shared component. Use this decision tree:

- **Used in 3+ places?** Yes -> shared component. No -> continue.
- **Complex interaction or accessibility pattern?** Yes -> shared component (even if used in 1 place, to get the a11y right once). No -> continue.
- **Likely to be reused in the next 3 months?** Yes -> shared component. No -> local implementation is fine.

### Escalation Path

- **Disagreement on component design:** Design System Owner makes final call.
- **Accessibility severity dispute:** Default to stricter interpretation. When in doubt, fix it.
- **Timeline pressure to skip edge states:** Not negotiable. The edge-state checklist is the minimum bar. If the feature is too large, cut scope on functionality, not on polish.
- **Token system doesn't accommodate a need:** Add a new token (with approval) rather than hardcoding a value.

### How to Onboard New Engineers

1. Read the Definition of Done document (30 min).
2. Browse Storybook and build a sample form using shared components (1 hour).
3. Pair with the Accessibility Champion on one keyboard navigation test (30 min).
4. First UI PR gets extra review from the Component Library Maintainer.

### How to Scale Beyond 4 Weeks

**Weeks 5-8:** Migrate the next 5 most-trafficked pages to the component library. Target 80% component coverage on new features.

**Weeks 9-12:** Introduce theming support (dark mode, customer branding). Add automated visual regression to all critical flows. Conduct first external accessibility audit.

**Quarter 2:** Evaluate headless UI approach for complex components (Radix, React Aria) to get robust accessibility primitives. Establish contribution model where any engineer can propose and build components. Consider design-to-code tooling (Figma dev mode, Anima, etc.) to reduce handoff friction.

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Designers become bottleneck reviewing 8 engineers' PRs | High | Medium | Async screenshot reviews, trust engineers on minor spacing/color (they have tokens), only require designer review for new patterns |
| Engineers resist using shared components ("faster to write my own") | Medium | High | Make the library genuinely faster to use than custom code. Measure and share time savings. Lead by example. |
| Token system is too rigid for edge cases | Medium | Low | Allow escape hatches with a lint warning (not error) and a required comment explaining why |
| Accessibility CI is too noisy (false positives) | Medium | Medium | Curate axe-core rules; disable rules that generate false positives in your stack; review quarterly |
| Week 1-4 investment delays feature work | High | Medium | Communicate to stakeholders: this is a one-time investment that pays back in reduced rework. Show metrics from Week 4 retrospective |

---

## Success Criteria at Week 4

The initiative is successful if, by end of Week 4:

1. A design token system is in production use.
2. 10+ shared components are built, documented in Storybook, and passing accessibility CI.
3. At least one feature has been shipped end-to-end using the new system.
4. The edge-state checklist is being used on every UI PR (verified by PR template).
5. axe-core CI is running and blocking on critical/serious violations.
6. Baseline metrics are captured for all KPIs listed above.
7. The team has conducted a retrospective and has a plan for Weeks 5-8.

The initiative is *not* successful if the system exists but nobody uses it. Adoption is the measure, not creation.
