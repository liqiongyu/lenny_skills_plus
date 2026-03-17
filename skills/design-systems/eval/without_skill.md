# Design System Operating Plan

## B2B SaaS Web Application — Comprehensive Design System Initiative

---

## 1. Executive Summary

This plan establishes a design system to resolve inconsistent UI, eliminate one-off CSS, introduce shared design tokens, and accelerate design-to-dev handoff. The system will be built incrementally by a small team (2 designers, 6 engineers) with first measurable impact targeted within 6 weeks. Accessibility (WCAG 2.1 AA minimum) is a non-negotiable requirement throughout.

---

## 2. Current State Assessment

### Problems Identified

- **Inconsistent UI**: Screens use different spacing, typography, colors, and component patterns for the same interactions.
- **One-off CSS**: Duplicated and conflicting styles scattered across the codebase, increasing maintenance burden and regression risk.
- **No shared tokens**: Color values, font sizes, spacing units, and breakpoints are hardcoded in individual files rather than centralized.
- **Slow design-to-dev handoff**: Designers specify intent in Figma; engineers re-interpret from scratch each time, leading to drift and rework.

### Impact of Current State

- Higher bug rate on visual/layout issues
- Longer cycle time for new features (each screen is designed/built from zero)
- Accessibility gaps: no systematic color contrast enforcement, inconsistent focus states, missing ARIA patterns
- Onboarding friction for new team members

---

## 3. Design System Vision and Principles

### Vision

A single source of truth — shared tokens, documented components, and usage guidelines — that lets any designer or engineer ship consistent, accessible UI without re-inventing patterns.

### Guiding Principles

1. **Adopt, don't invent**: Start from what already exists in the product. Extract and standardize the best current patterns before creating anything new.
2. **Tokens first**: Every visual decision (color, spacing, typography, elevation, motion) flows from a token. No magic numbers.
3. **Accessible by default**: Components ship with correct contrast ratios, focus management, keyboard navigation, and ARIA attributes baked in. Accessibility is not a post-hoc audit.
4. **Small surface, high coverage**: Prioritize the 15-20 components that cover 80%+ of screens. Resist scope creep.
5. **Living system**: The design system is a product, not a project. It ships continuously alongside the application.
6. **Documentation is the UI**: If it's not documented, it doesn't exist in the system.

---

## 4. Team Structure and Roles

### Dedicated Roles (Part-Time Allocation)

| Role | Person(s) | Allocation | Responsibilities |
|------|-----------|------------|-----------------|
| Design System Lead | 1 senior engineer | ~50% | Architecture, token structure, component API design, code review |
| Design Lead | 1 designer | ~40% | Token definitions in Figma, component specs, documentation |
| Component Contributors | 3-4 engineers (rotating) | ~20% each | Build and test individual components |
| Design Contributor | 1 designer | ~20% | Audit existing screens, create migration specs |
| QA/Accessibility Champion | 1 engineer | ~15% | Automated a11y testing, manual screen reader testing |

### Governance

- **Weekly sync** (30 min): Review progress, unblock issues, triage requests.
- **Bi-weekly design review** (45 min): Walk through new components, get feedback from full team.
- **RFC process for new components**: Any team member can propose; requires sign-off from Design Lead + System Lead before work begins.

---

## 5. Technical Architecture

### 5.1 Design Tokens

**Format**: Define tokens in a platform-agnostic format (JSON or YAML) and transform to CSS custom properties, SCSS variables, and JavaScript constants via a build step (e.g., Style Dictionary or a lightweight custom script).

**Token Tiers**:

```
Global Tokens (primitive)
├── color.blue.500: #2563EB
├── color.neutral.100: #F5F5F5
├── spacing.4: 16px
├── font.size.md: 16px
└── ...

Semantic Tokens (alias)
├── color.text.primary → color.neutral.900
├── color.text.secondary → color.neutral.600
├── color.action.primary → color.blue.600
├── color.action.primary.hover → color.blue.700
├── color.border.default → color.neutral.200
├── spacing.component.padding → spacing.4
└── ...

Component Tokens (scoped)
├── button.color.background → color.action.primary
├── button.color.text → color.neutral.white
├── input.border.color → color.border.default
├── input.border.color.focus → color.action.primary
└── ...
```

**Accessibility Enforcement at Token Level**:
- All foreground/background token pairings must meet WCAG AA contrast (4.5:1 for normal text, 3:1 for large text).
- Focus indicator tokens must produce visible outlines meeting 3:1 contrast against adjacent colors.
- Automated contrast checks run in the token build pipeline.

### 5.2 Component Library

**Technology**: Build as a shared package within the existing monorepo (or as an internal npm package if using a multi-repo setup). Use the same framework as the application (React assumed here; adjust if Vue/Angular/Svelte).

**Component API Conventions**:
- Props use semantic names, not visual ones (`variant="primary"` not `color="blue"`)
- All interactive components accept standard HTML attributes via spread/rest props
- Every component forwards refs
- Every component supports a `className` escape hatch for edge cases (but discouraged in docs)
- TypeScript interfaces for all props

**Accessibility Requirements per Component**:
- Correct semantic HTML element (button is `<button>`, not `<div>`)
- ARIA roles/attributes where native semantics are insufficient
- Keyboard interaction pattern matching WAI-ARIA Authoring Practices
- Visible focus indicator using the system focus token
- Color is never the sole means of conveying information
- Motion respects `prefers-reduced-motion`

**Component Folder Structure**:

```
src/design-system/
├── tokens/
│   ├── global.json
│   ├── semantic.json
│   └── build.js
├── components/
│   ├── Button/
│   │   ├── Button.tsx
│   │   ├── Button.styles.ts (or .module.css)
│   │   ├── Button.test.tsx
│   │   ├── Button.a11y.test.tsx
│   │   ├── Button.stories.tsx
│   │   └── index.ts
│   ├── Input/
│   ├── Select/
│   ├── Modal/
│   └── ...
├── hooks/
│   ├── useFocusTrap.ts
│   ├── useKeyboardNavigation.ts
│   └── ...
├── utils/
│   └── a11y.ts
└── index.ts (barrel export)
```

### 5.3 Styling Strategy

**Approach**: Replace one-off CSS with token-based styles. Recommended migration path:

1. Introduce CSS custom properties derived from tokens at the `:root` level.
2. New components use only token-based custom properties (no hardcoded values).
3. Existing screens migrate incrementally: when a feature touches a screen, swap hardcoded values for tokens.
4. Add a stylelint rule to warn/error on raw color hex values and pixel values outside the token scale.

### 5.4 Documentation Site

Use Storybook as the documentation and development environment:

- **Stories for every component**: Default state, all variants, edge cases (long text, empty state, loading state).
- **Accessibility tab**: Integrated axe-core addon showing live violations.
- **Design token page**: Visual display of all tokens (color swatches, type scale, spacing scale).
- **Usage guidelines**: When to use, when not to use, do/don't examples.
- **Code snippets**: Copy-pasteable usage examples.

---

## 6. Component Prioritization

### Tier 1 — Foundation (Weeks 1-3)

These are the atomic building blocks that everything else depends on:

| Component | Rationale |
|-----------|-----------|
| Design Tokens (full set) | Everything depends on tokens existing |
| Button | Most common interactive element |
| Input (text) | Core of every form |
| Typography (headings, body, labels) | Used on every screen |
| Icon system | Referenced by buttons, inputs, nav |
| Layout primitives (Stack, Flex, Grid) | Replaces most one-off spacing CSS |

### Tier 2 — Core Patterns (Weeks 3-5)

| Component | Rationale |
|-----------|-----------|
| Select / Dropdown | Second most common form element |
| Checkbox / Radio | Form completion |
| Modal / Dialog | High-frequency pattern, critical a11y needs (focus trap) |
| Table | B2B SaaS bread and butter |
| Toast / Alert | Feedback patterns |
| Card | Common content container |
| Badge / Tag | Status indicators throughout the app |

### Tier 3 — Composite (Weeks 5-6+)

| Component | Rationale |
|-----------|-----------|
| Form (composed) | Wires together inputs with validation and error states |
| Navigation (sidebar, topbar) | App shell consistency |
| Pagination | Table companion |
| Tabs | Common content organization |
| Tooltip / Popover | Progressive disclosure |

---

## 7. Six-Week Execution Plan

### Week 1: Foundation and Audit

**Design**:
- [ ] Audit top 10 most-visited screens: screenshot, annotate every unique color, font size, spacing value, and component variant
- [ ] Propose consolidated token set: colors (8-12 semantic colors), type scale (6 sizes), spacing scale (8 values), border radii, shadows
- [ ] Set up Figma token library using proposed values

**Engineering**:
- [ ] Set up design system directory structure in repo
- [ ] Implement token build pipeline (JSON source -> CSS custom properties + JS constants)
- [ ] Inject token CSS custom properties into app root
- [ ] Configure Storybook with accessibility addon (axe-core)
- [ ] Add stylelint rule to flag raw hex colors (warning mode, not blocking)

**Milestone**: Token pipeline running; Figma library draft shared for review.

### Week 2: First Components

**Design**:
- [ ] Finalize token values based on team feedback
- [ ] Create Figma component specs for Button (all variants: primary, secondary, ghost, destructive; all sizes; all states: default, hover, focus, active, disabled, loading)
- [ ] Create Figma component specs for Input (text, with label, with error, with helper text, disabled)

**Engineering**:
- [ ] Build Button component with full variant/size/state matrix
- [ ] Build Input component (text) with label, error, helper text, disabled states
- [ ] Build Typography components (Heading, Text, Label)
- [ ] Write unit tests and accessibility tests for each
- [ ] Write Storybook stories for each

**Milestone**: 3 production-ready components in Storybook with passing a11y tests.

### Week 3: Layout and Expansion

**Design**:
- [ ] Spec layout primitives (Stack, Flex, Grid helpers)
- [ ] Spec Icon system (size variants, color inheritance)
- [ ] Spec Select, Checkbox, Radio components
- [ ] Begin writing usage guidelines for completed components

**Engineering**:
- [ ] Build layout primitives (Stack, Flex, Grid)
- [ ] Implement icon system (SVG sprite or individual imports with standard sizing)
- [ ] Build Select component with keyboard navigation
- [ ] Build Checkbox and Radio components
- [ ] Begin first migration: pick one high-traffic screen and replace hardcoded styles + one-off components with system components

**Milestone**: Layout system usable; first screen migration underway.

### Week 4: Interactive Patterns and Migration

**Design**:
- [ ] Spec Modal/Dialog with focus management requirements
- [ ] Spec Table component (sortable headers, row selection, empty state)
- [ ] Spec Toast/Alert patterns
- [ ] Document do/don't guidelines for all Tier 1 components

**Engineering**:
- [ ] Build Modal/Dialog with focus trap hook
- [ ] Build Table component (basic: header, rows, responsive behavior)
- [ ] Build Toast/Alert component with auto-dismiss and screen reader announcements
- [ ] Build Card and Badge components
- [ ] Complete first screen migration; begin second screen migration
- [ ] Measure: count remaining one-off CSS files vs. token-based files

**Milestone**: All Tier 2 components in progress; 2 screens migrated.

### Week 5: Composition and Handoff

**Design**:
- [ ] Spec composed Form pattern (field groups, validation display, submission states)
- [ ] Spec Navigation components (sidebar, topbar)
- [ ] Create "kitchen sink" Figma page showing all components together
- [ ] Establish Figma-to-code handoff workflow: designers annotate with component names and prop values, not visual specs

**Engineering**:
- [ ] Build Form composition layer (FormField wrapper, validation integration)
- [ ] Build Tabs component
- [ ] Build Pagination component
- [ ] Build Tooltip/Popover with accessible dismiss patterns
- [ ] Promote stylelint rule from warning to error for new files
- [ ] Migrate 2 more screens (total: 4 screens on design system)

**Milestone**: Full Tier 1-3 component set available; handoff workflow documented.

### Week 6: Polish, Document, and Measure

**Design**:
- [ ] Complete documentation for all components (usage guidelines, do/don't, accessibility notes)
- [ ] Run accessibility audit on all components using screen reader (VoiceOver + NVDA or JAWS)
- [ ] Create onboarding guide: "How to use the design system" for new team members

**Engineering**:
- [ ] Fix any accessibility issues found in audit
- [ ] Performance review: ensure component bundle adds < 30KB gzipped to app
- [ ] Add CI checks: a11y tests run on every PR; Storybook deploys on merge
- [ ] Migrate 2 more screens (total: 6 screens on design system)
- [ ] Document: contribution guide for adding new components

**Milestone**: Design system v1.0 declared; 6 screens migrated; CI pipeline enforcing standards.

---

## 8. Design-to-Dev Handoff Process (New)

### Before (Current Pain)

1. Designer creates mockup in Figma with arbitrary values
2. Engineer inspects Figma, eyeballs spacing and colors
3. Engineer writes custom CSS to approximate the design
4. Designer reviews, finds discrepancies, files feedback
5. Cycle repeats 2-3 times

### After (With Design System)

1. Designer composes screen in Figma using component library and token values
2. Designer annotates: "This is `<Button variant='primary' size='md'>`, `<Input error={true}>`, spacing is `spacing.6`"
3. Engineer assembles screen using system components and token classes — no custom CSS for standard patterns
4. Designer reviews: matches 1:1 because both reference the same system
5. One round of review (if any) for layout/content, not styling

### Expected Time Savings

| Activity | Before | After | Savings |
|----------|--------|-------|---------|
| Component implementation | 4-8 hours | 0.5-1 hour (compose existing) | 75-85% |
| Visual QA cycles | 2-3 rounds | 0-1 round | 60-80% |
| CSS debugging | 3-5 hours/week/engineer | 0.5-1 hour/week/engineer | 70-80% |
| Designer spec creation | 4-6 hours/screen | 1-2 hours/screen | 50-65% |

---

## 9. Accessibility Plan

### Standards

- **Target**: WCAG 2.1 Level AA compliance
- **Stretch**: WCAG 2.2 Level AA for new components

### Automated Testing

| Tool | Scope | When |
|------|-------|------|
| axe-core (Storybook addon) | Per-component in isolation | During development |
| jest-axe | Component unit tests | Every PR (CI) |
| axe-core (Cypress/Playwright) | Integrated page-level tests | Nightly CI run |
| stylelint a11y plugin | Color contrast in token definitions | Every PR (CI) |

### Manual Testing Cadence

| Test | Frequency | Who |
|------|-----------|-----|
| Keyboard-only navigation (full app flow) | Bi-weekly | Rotating engineer |
| Screen reader testing (VoiceOver on macOS) | Monthly per component batch | Accessibility champion |
| Screen reader testing (NVDA on Windows) | Monthly | Accessibility champion (VM or BrowserStack) |
| High contrast mode / forced colors | Monthly | Accessibility champion |
| Zoom to 200% / reflow | With each new responsive component | QA |

### Component-Level Requirements Checklist

Every component PR must confirm:

- [ ] Renders correct semantic HTML element
- [ ] Has accessible name (visible label or `aria-label`)
- [ ] Keyboard operable (Tab, Enter, Space, Escape, Arrow keys as appropriate)
- [ ] Focus indicator visible and meets 3:1 contrast
- [ ] Color contrast meets 4.5:1 (text) or 3:1 (large text, UI components)
- [ ] States (error, disabled, loading) communicated to assistive technology
- [ ] No information conveyed by color alone
- [ ] Respects `prefers-reduced-motion` for animations
- [ ] jest-axe test passes with zero violations
- [ ] Tested with VoiceOver (macOS) — reads sensibly

---

## 10. Migration Strategy

### Approach: Incremental Adoption, Not Big Bang

Rewriting the entire app to use the design system at once would stall feature work. Instead:

**Rule 1: All new screens/features use the design system.** No exceptions after Week 3.

**Rule 2: Existing screens migrate when touched.** If a feature or bug fix touches a screen, that screen gets migrated to system components as part of the work. Budget +30% time on that ticket for migration.

**Rule 3: Dedicated migration sprints for high-traffic screens.** The top 10 screens (by usage analytics) get explicitly scheduled for migration, 2 per week.

### Migration Checklist per Screen

- [ ] Replace hardcoded colors with token CSS custom properties
- [ ] Replace hardcoded spacing/sizing with token values
- [ ] Replace custom button implementations with `<Button>` component
- [ ] Replace custom input implementations with `<Input>` component
- [ ] Replace custom modals with `<Modal>` component
- [ ] Replace custom tables with `<Table>` component
- [ ] Remove orphaned CSS that is no longer referenced
- [ ] Run axe-core on migrated screen — zero violations
- [ ] Visual regression test (screenshot comparison) — no unintended changes
- [ ] Designer sign-off

### Migration Tracking

Maintain a spreadsheet or project board:

| Screen | Traffic Rank | Status | Assigned To | Target Date |
|--------|-------------|--------|-------------|-------------|
| Dashboard | 1 | Migrated | Engineer A | Week 3 |
| Settings | 2 | Migrated | Engineer B | Week 4 |
| User List | 3 | In Progress | Engineer C | Week 5 |
| Reports | 4 | Planned | — | Week 6 |
| ... | ... | ... | ... | ... |

---

## 11. Success Metrics

### Leading Indicators (Track Weekly)

| Metric | Baseline | 6-Week Target |
|--------|----------|---------------|
| Number of production-ready components | 0 | 18-22 |
| Screens fully migrated to design system | 0 | 6-8 |
| % of new PRs using system components (no new one-off CSS) | 0% | 90%+ |
| Storybook documentation coverage | 0% | 100% of shipped components |
| Component a11y test pass rate | N/A | 100% |

### Lagging Indicators (Track Monthly After Launch)

| Metric | Measurement Method | Target (3 Months) |
|--------|-------------------|-------------------|
| Design-to-dev handoff time per screen | Track in project management tool | 50% reduction |
| CSS bundle size | Build output analysis | 20% reduction (as one-off CSS removed) |
| Visual bug reports | Issue tracker label | 40% reduction |
| Accessibility audit violations | axe-core automated scan, full app | 80% reduction |
| Time to onboard new team member to UI work | Self-reported | 50% reduction |
| Designer-reported "doesn't match spec" issues | Issue tracker | 60% reduction |

---

## 12. Ongoing Governance (Post-6-Weeks)

### Component Lifecycle

1. **Proposal**: Anyone files an RFC (1-page template: problem, use cases, API sketch, accessibility considerations).
2. **Review**: Design Lead + System Lead review within 1 week. Approve, request changes, or redirect to existing component.
3. **Build**: Assigned engineer builds; designer provides Figma spec.
4. **Review**: Code review + design review + a11y review.
5. **Ship**: Merge, publish to Storybook, announce in team channel.
6. **Deprecate**: When a component is superseded, mark as deprecated in Storybook with migration guide. Remove after all usages migrated.

### Versioning

- Use semantic versioning for the design system package.
- Breaking changes (prop renames, removed variants) require a minor or major version bump and a migration guide.
- Maintain a CHANGELOG.

### Health Checks

- **Monthly**: Review adoption metrics. Are new screens using the system? Are old screens getting migrated?
- **Quarterly**: Full accessibility audit (automated + manual). Review component request backlog. Assess if token values need updates (brand refresh, new product areas).
- **Annually**: Major review — is the architecture still serving the team? Evaluate tooling updates (Figma plugins, Storybook versions, testing tools).

---

## 13. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Team bandwidth: feature work competes with system work | High | High | Secure explicit time allocation from leadership. Frame migration work as part of feature tickets, not separate. |
| Over-engineering: building too many components too early | Medium | Medium | Strict prioritization by usage data. No component without 3+ usage instances. |
| Adoption resistance: engineers keep writing one-off CSS | Medium | High | Stylelint enforcement. Make the system the path of least resistance. Celebrate migrations. |
| Design token sprawl: too many tokens, developers confused | Medium | Medium | Cap token tiers. Review token additions in weekly sync. Document naming conventions. |
| Accessibility gaps discovered late | Medium | High | Test early and continuously. Include a11y in every component's definition of done. |
| Figma library drifts from code | Medium | Medium | Designate one designer as Figma library owner. Monthly sync between Figma library and Storybook. |
| Performance: component library adds too much bundle size | Low | Medium | Tree-shakeable exports. Measure bundle impact in CI. Set a budget (50KB gzipped max). |

---

## 14. Tools and Infrastructure

| Purpose | Tool | Notes |
|---------|------|-------|
| Design tool | Figma | Token library + component library |
| Token management | Style Dictionary (or Tokens Studio Figma plugin) | Single source, multi-platform output |
| Component development | Storybook | Dev environment + documentation |
| Unit testing | Jest + React Testing Library | Component behavior |
| Accessibility testing (unit) | jest-axe | Automated a11y checks per component |
| Accessibility testing (integration) | axe-core via Playwright/Cypress | Page-level scans |
| CSS enforcement | stylelint | Ban hardcoded values, enforce token usage |
| Visual regression | Chromatic (or Percy) | Catch unintended visual changes |
| CI/CD | GitHub Actions (or existing CI) | Run tests, deploy Storybook, lint |
| Communication | Slack channel `#design-system` | Announcements, questions, RFCs |

---

## 15. Quick-Start Checklist (Day 1)

For the team lead kicking this off:

- [ ] Get leadership buy-in: present this plan, secure time allocation commitment
- [ ] Create `#design-system` Slack channel
- [ ] Assign Design System Lead and Design Lead roles
- [ ] Set up design system directory in codebase
- [ ] Install and configure Storybook
- [ ] Schedule recurring weekly sync (30 min) and bi-weekly design review (45 min)
- [ ] Begin screen audit (assign top 10 screens across both designers)
- [ ] Draft initial token set from audit findings
- [ ] Create project board with Week 1 tasks

---

*This plan is designed to deliver tangible value within 6 weeks while establishing sustainable practices for long-term design system health. The key insight is to start with tokens (the foundation everything else builds on), prioritize components by actual usage, and migrate incrementally rather than attempting a risky big-bang rewrite.*
