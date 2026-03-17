# Design System Operating Pack

**B2B SaaS Web Application**

---

## 1) Context Snapshot

**Product / area in scope:** B2B SaaS web application (all customer-facing screens and internal admin surfaces).

**Platforms in scope:** Web (responsive; desktop-first with tablet/mobile support).

**Primary system users:** Designers (2), engineers (6), and PMs who spec screens using system patterns.

**Why now:** The UI is inconsistent, riddled with one-off CSS, has no shared tokens, and the design-to-dev handoff is slow and error-prone. This is a drag on shipping speed and product quality.

**Success signals:**
- 80% of new screens built with system components within 8 weeks of first milestone.
- Design-to-dev handoff time reduced by 50% (measured as time from approved mockup to merged PR).
- Zero new one-off CSS introduced for tokenized properties (color, spacing, type, elevation) after milestone 2.
- All new components meet WCAG 2.1 AA.
- Reduction in UI-related bug reports by 30% within one quarter.

**Current state:**
- No shared design tokens.
- No canonical component library (Figma or code).
- One-off CSS scattered across the codebase.
- Ad-hoc handoff (screenshots, Slack messages, inconsistent Figma files).
- No governance or documentation.

**Constraints:**
- 6-week window to first measurable impact.
- Small team: 2 designers, 6 engineers; no dedicated design-systems engineer.
- Accessibility is required (WCAG 2.1 AA minimum).
- No enterprise theming/white-label requirement at this time.

**Assumptions:**
- Design tool is Figma.
- Engineering stack is a modern JS framework (React or equivalent) with CSS-in-JS or CSS modules.
- The team is willing to adopt a component library (e.g., Storybook for dev, Figma library for design).
- There is no existing Storybook instance.
- PMs and other non-designers occasionally create or modify screens using templates.

---

## 2) Design System Charter

**Mission (1 sentence):** Provide a single source of truth for UI decisions -- tokens, components, and patterns -- so every team member can build consistent, accessible screens faster.

**Problem statement:** Teams waste hours per feature on handoff friction, duplicate CSS, and inconsistent UI decisions. There is no shared language between design and engineering, leading to visual drift, accessibility gaps, and slow iteration.

**Audiences:**
1. **Engineers** (primary consumers): need clear component APIs, token values, and copy-pasteable code patterns.
2. **Designers** (primary contributors): need a Figma library with variants, tokens, and layout recipes.
3. **PMs and non-designers** (secondary consumers): need starter templates and guardrails to spec screens without deep design knowledge.

**Scope (in):**
- Design tokens (color, spacing, typography, radius, elevation, motion).
- Core UI components (primitives and composites) for web.
- Component documentation (usage, variants, states, do/don't).
- Figma library and code component library (Storybook).
- Governance workflow (contribution, review, release).
- Starter templates for common page layouts.

**Scope (out):**
- Brand identity / logo system (different process).
- User research or discovery to decide what features to build.
- Native mobile component libraries (iOS/Android) -- web only for now.
- Marketing site or email templates (future phase).
- Design engineering practice/role definition (use `design-engineering`).
- One-off design critiques (use `running-design-reviews`).

**Principles:**
1. **Consistency over creativity** -- Default to system patterns; deviate only with a documented reason.
2. **Accessible by default** -- Every token and component ships with AA contrast, keyboard support, and reduced-motion handling baked in.
3. **Teach by structure** -- Documentation, defaults, and constraints should make correct usage easy and incorrect usage hard, even for non-experts.
4. **Ship incrementally** -- Deliver value in small, pattern-setting milestones rather than a big-bang library.
5. **Tokens first, components second** -- Decisions live in tokens; components consume tokens. Style can evolve without rewriting components.

**Anti-goals:**
- Pixel-perfect enforcement of every screen (the system provides patterns, not a straitjacket).
- Building every possible component before adoption (start narrow).
- Optimizing for enterprise theming or white-labeling at this stage.

**Decision-maker(s):**
- **Token decisions:** Lead designer (final call), consulting lead engineer for feasibility.
- **Component API decisions:** Lead engineer (final call), consulting lead designer for UX.
- **Visual direction:** Lead designer, with PM sign-off on scope.

**Interfaces:**
- Design <-> Eng: Figma library mirrors code components 1:1; token values are the contract.
- Eng <-> PM: Storybook is the living reference; PMs review in Storybook before sign-off.
- Design <-> PM: Blockframes (lo-fi) reviewed before hi-fi; hi-fi uses system components only.

**Release cadence:** Biweekly releases aligned with sprint cycles. Hotfixes (a11y, breaking bugs) released as needed.

**Success metrics:**
| Metric | Baseline (now) | Target (8 weeks) |
|--------|---------------|-------------------|
| % new screens using system components | 0% | 80% |
| Avg. handoff-to-merge time | ~5 days | ~2.5 days |
| New one-off CSS per sprint | ~40 declarations | 0 for tokenized properties |
| UI bug reports per sprint | ~12 | ~8 |
| WCAG AA compliance (new components) | Unknown | 100% |

---

## 3) UI Audit + Operational Blockers

### Inventory

| Area / flow | What's inconsistent today | Operational impact | Proposed system fix | Priority |
|:------------|:--------------------------|:-------------------|:--------------------|:---------|
| Typography | 8+ font sizes used ad-hoc; no type scale; inconsistent line heights | Every screen reinvents heading/body styles; accessibility issues with small text | Type tokens (`font.size.*`, `font.lineHeight.*`, `font.weight.*`) + Text component | P0 |
| Color | Raw hex values in CSS; 30+ grays; no semantic naming; insufficient contrast in some states | Designers and engineers guess colors; dark-on-dark contrast failures | Semantic color tokens (`color.text.*`, `color.bg.*`, `color.border.*`, `color.interactive.*`) with AA contrast guarantees | P0 |
| Spacing | Ad-hoc pixel values everywhere; no consistent scale | Layouts drift between screens; padding/margin arguments in code review | Spacing tokens (`space.1`..`space.10`) on a 4px base grid | P0 |
| Forms (inputs, selects, textareas) | 5+ input styles; inconsistent error/focus states; no shared validation patterns | Every form is custom-built; accessibility gaps in focus indicators | Input, Select, Textarea primitives + FormField composite with built-in error/focus states | P0 |
| Buttons | 4+ button styles with inconsistent sizing, padding, and disabled states | Engineers create new button variants per feature | Button primitive with size/variant tokens and all states | P0 |
| Tables | Custom table markup per feature; no shared sorting/pagination | Table-heavy B2B flows are slow to build and inconsistent | Table composite (header, row, cell, pagination) with sorting pattern | P1 |
| Page layout / navigation | No shared layout shell; sidebar/header reimplemented per section | New pages require full layout scaffolding from scratch | PageLayout pattern + Sidebar/Header composites + layout recipe | P1 |
| Cards | Multiple card styles with inconsistent padding, radius, and elevation | Visual inconsistency on dashboards and list views | Card composite with elevation tokens | P1 |
| Modals / dialogs | Different modal implementations; inconsistent close behavior and focus trapping | Accessibility failures (focus trap, Escape key); visual drift | Modal/Dialog composite with a11y baked in | P1 |
| Icons | No shared icon set; mix of inline SVGs, font icons, and PNGs | Icon inconsistency; large bundle sizes | Icon primitive + curated icon set (e.g., Lucide or Phosphor) | P2 |

### Operational Hook

- **Primary blocker:** Slow design-to-dev handoff caused by lack of shared tokens and component language. Every feature requires designers to redraw and engineers to re-implement basic UI from scratch, consuming 30-40% of feature time on "infrastructure" rather than product logic.
- **Secondary blocker:** Inconsistent UI and accessibility gaps erode user trust and create bug reports that consume engineering time (estimated 12+ UI bugs/sprint, many avoidable with shared components).
- **"First slice" to ship:** **Forms + Buttons + Typography + Color/Spacing tokens + a "Form Page" layout recipe.** This slice covers the most-repeated patterns in a B2B SaaS app (data entry, settings, onboarding) and establishes the token + component + recipe pattern that all future work follows.

---

## 4) Blockframe-to-Component Map

### Blockframe Spec: "Form Page" (representative key flow)

The Form Page is the most common pattern in the app (settings, data entry, record creation/editing). Locking its structure in a blockframe sets the template for 60%+ of screens.

```
+----------------------------------------------------------+
| [Header]                                                  |
|  Logo | Nav Links | User Menu                            |
+--------+-------------------------------------------------+
| [Sidebar] | [Page Content]                               |
|           |  +------------------------------------------+ |
|  Nav      |  | [PageHeader]                             | |
|  items    |  |  Title (h1) | Breadcrumb | Action Button | |
|           |  +------------------------------------------+ |
|           |  | [FormSection]                            | |
|           |  |  Section heading (h2)                    | |
|           |  |  +-- FormField (label + Input) ---------+| |
|           |  |  +-- FormField (label + Select) --------+| |
|           |  |  +-- FormField (label + Textarea) ------+| |
|           |  |  +-- Inline validation (error state) ---+| |
|           |  +------------------------------------------+ |
|           |  | [FormSection]                            | |
|           |  |  Section heading (h2)                    | |
|           |  |  +-- FormField (label + Input) ---------+| |
|           |  |  +-- FormField (label + Checkbox) ------+| |
|           |  +------------------------------------------+ |
|           |  | [ActionBar]                              | |
|           |  |  [Button:secondary] Cancel               | |
|           |  |  [Button:primary] Save                   | |
|           |  +------------------------------------------+ |
+---------+------------------------------------------------+
```

- **Grid/layout:** 12-column grid; sidebar = 240px fixed; content area = fluid with max-width 960px; `space.6` (24px) page padding; `space.4` (16px) between form fields.
- **Spacing scale (token names):** `space.1` (4px), `space.2` (8px), `space.3` (12px), `space.4` (16px), `space.5` (20px), `space.6` (24px), `space.8` (32px), `space.10` (40px).
- **Component placeholders labeled:** Header, Sidebar, PageHeader, FormSection, FormField, Input, Select, Textarea, Checkbox, Button, ActionBar.
- **State annotations:** Form fields: default / focus / error / disabled. Buttons: default / hover / active / focus / disabled / loading. Page: loading skeleton / empty state (no data) / error state (API failure).
- **Accessibility/keyboard flow:** Tab order follows visual order (top-to-bottom, left-to-right within form). Focus indicator visible on all interactive elements (`color.focus.ring`). Error messages associated via `aria-describedby`. Required fields marked with `aria-required`.

### Mapping Table

| Blockframe section | Intended component/pattern | Tokens used | States required | Notes |
|:-------------------|:---------------------------|:------------|:----------------|:------|
| Header | `Header` (composite) | `color.bg.surface`, `color.text.primary`, `space.4`, `elevation.1` | default, mobile-collapsed | Sticky; elevation token for subtle shadow |
| Sidebar | `Sidebar` (composite) | `color.bg.subtle`, `color.text.secondary`, `space.3`, `space.4` | expanded, collapsed, active-item, hover-item | Collapsible on smaller viewports |
| Page header | `PageHeader` (pattern) | `font.size.xl`, `font.weight.semibold`, `space.6` | default | Includes breadcrumb + optional action button slot |
| Form section | `FormSection` (pattern) | `font.size.lg`, `space.4`, `space.6`, `color.border.subtle` | default | Groups related fields with a heading |
| Form field | `FormField` (composite) | `font.size.sm` (label), `space.1`, `space.2` | default, error (shows message), disabled | Wraps label + input + helper/error text |
| Input | `Input` (primitive) | `color.bg.input`, `color.border.default`, `color.border.focus`, `color.text.primary`, `radius.md`, `space.3` | default, focus, error, disabled, read-only | Focus ring uses `color.focus.ring` |
| Select | `Select` (primitive) | Same as Input + `color.bg.surface` for dropdown | default, focus, error, disabled, open | Dropdown uses `elevation.2` |
| Textarea | `Textarea` (primitive) | Same as Input | default, focus, error, disabled | Auto-resize option |
| Checkbox | `Checkbox` (primitive) | `color.interactive.primary`, `color.bg.input`, `radius.sm` | unchecked, checked, indeterminate, focus, disabled | Visible focus ring |
| Button (primary) | `Button` (primitive, variant: primary) | `color.interactive.primary`, `color.text.onPrimary`, `font.size.md`, `font.weight.medium`, `radius.md`, `space.3`, `space.5` | default, hover, active, focus, disabled, loading | Loading shows spinner + disabled state |
| Button (secondary) | `Button` (primitive, variant: secondary) | `color.bg.surface`, `color.border.default`, `color.text.primary` | Same as primary | Outlined style |
| Action bar | `ActionBar` (pattern) | `space.4`, `color.border.subtle` | default, sticky (on scroll) | Sticky to bottom on long forms; contains primary + secondary actions |

---

## 5) Token Model + Token Backlog

### Token Taxonomy

| Category | Token examples | Usage rules | A11y / behavior notes |
|:---------|:---------------|:------------|:----------------------|
| **Color -- semantic** | `color.text.primary`, `color.text.secondary`, `color.text.disabled`, `color.text.onPrimary`, `color.text.error` | Always use semantic tokens. Never reference raw hex in component code or Figma. | All text/bg combinations must meet 4.5:1 contrast (AA). `color.text.disabled` exempt from contrast but must have non-color indicator. |
| **Color -- background** | `color.bg.page`, `color.bg.surface`, `color.bg.subtle`, `color.bg.input`, `color.bg.overlay` | Surfaces layer: page < surface < overlay. | `color.bg.overlay` includes scrim at 40% opacity for modals. |
| **Color -- border** | `color.border.default`, `color.border.subtle`, `color.border.focus`, `color.border.error` | Use `default` for structural borders, `subtle` for dividers. | `color.border.focus` must meet 3:1 contrast against adjacent backgrounds. |
| **Color -- interactive** | `color.interactive.primary`, `color.interactive.primaryHover`, `color.interactive.primaryActive`, `color.interactive.secondary`, `color.interactive.danger` | Interactive colors pair with `color.text.onPrimary` or `color.text.onDanger`. | Hover/active states must be visually distinct beyond color alone (underline, shadow, or scale). |
| **Color -- feedback** | `color.feedback.success`, `color.feedback.warning`, `color.feedback.error`, `color.feedback.info` | Used for banners, badges, inline messages. | Pair with an icon; do not rely on color alone. |
| **Spacing** | `space.1` (4px), `space.2` (8px), `space.3` (12px), `space.4` (16px), `space.5` (20px), `space.6` (24px), `space.8` (32px), `space.10` (40px) | Use token names only. No ad-hoc px values for padding/margin/gap. | Grid alignment on 4px base. |
| **Typography** | `font.size.xs` (12px), `font.size.sm` (14px), `font.size.md` (16px), `font.size.lg` (18px), `font.size.xl` (24px), `font.size.2xl` (30px), `font.size.3xl` (36px) | Use scale only. `font.size.md` is the body default. | Minimum interactive text: `font.size.sm` (14px). Minimum body text: `font.size.md` (16px). |
| **Typography (weight)** | `font.weight.regular` (400), `font.weight.medium` (500), `font.weight.semibold` (600), `font.weight.bold` (700) | Limit to 2-3 weights per screen for hierarchy clarity. | -- |
| **Typography (line-height)** | `font.lineHeight.tight` (1.25), `font.lineHeight.normal` (1.5), `font.lineHeight.relaxed` (1.75) | Body text uses `normal`; headings use `tight`. | `normal` (1.5) ensures readability for body text per WCAG. |
| **Border radius** | `radius.sm` (4px), `radius.md` (8px), `radius.lg` (12px), `radius.full` (9999px) | Inputs and buttons use `radius.md`; pills/badges use `radius.full`. | -- |
| **Elevation** | `elevation.0` (none), `elevation.1` (subtle: `0 1px 2px`), `elevation.2` (medium: `0 2px 8px`), `elevation.3` (high: `0 4px 16px`), `elevation.4` (overlay: `0 8px 32px`) | Higher elevation = closer to user. Sticky elements: `elevation.1`. Dropdowns: `elevation.2`. Modals: `elevation.4`. | Elevation should not be the only indicator of layering; pair with background change or border. |
| **Motion** | `motion.duration.fast` (100ms), `motion.duration.normal` (200ms), `motion.duration.slow` (350ms), `motion.easing.default` (ease-in-out), `motion.easing.enter` (ease-out), `motion.easing.exit` (ease-in) | Use consistent durations. Micro-interactions: `fast`. State transitions: `normal`. Page transitions: `slow`. | **Reduced motion:** wrap all motion in `@media (prefers-reduced-motion: reduce)` and provide instant or minimal alternative. `motion.duration.reduced` = 0ms. |
| **Focus** | `color.focus.ring` (a distinct, high-contrast ring color, e.g., blue-600 at 2px offset) | Every interactive element must show a visible focus indicator on `:focus-visible`. | Focus ring must meet 3:1 contrast against adjacent backgrounds. Ring width: 2px. Offset: 2px. |

### Token Backlog

| ID | Token / change | Why | Dependencies | Owner | Priority | Notes |
|---:|:---------------|:----|:-------------|:------|:---------|:------|
| 1 | Semantic color tokens (full set: text, bg, border, interactive, feedback) | Foundation for every component; eliminates raw hex in codebase | None | Lead designer + lead engineer | P0 | ~40 tokens; document contrast pairs |
| 2 | Spacing scale (`space.1`..`space.10`) | Replaces ad-hoc px; enforces grid alignment | None | Lead engineer | P0 | 4px base; 8 values |
| 3 | Typography scale (size, weight, line-height) | Standardizes text hierarchy; fixes a11y minimum sizes | None | Lead designer | P0 | ~15 tokens |
| 4 | Border radius tokens | Consistent rounding across inputs, buttons, cards | None | Lead engineer | P0 | 4 values |
| 5 | Focus ring token (`color.focus.ring`) | Accessibility: visible focus for keyboard users | Color tokens (#1) | Lead designer | P0 | Must meet 3:1 contrast |
| 6 | Elevation tokens (`elevation.0`..`elevation.4`) | Depth and layering for dropdowns, modals, sticky headers | None | Lead engineer | P1 | 5 levels; pair with bg tokens |
| 7 | Motion tokens (duration, easing, reduced) | Consistent animation; reduced-motion support | None | Lead engineer | P1 | Include `prefers-reduced-motion` rule |
| 8 | Dark mode semantic mappings | Future-proofing; not in scope for first 6 weeks | All semantic tokens (#1) | -- | P2 | Defer; design token layer supports it |

---

## 6) Component Inventory + Roadmap

### Component Tiering

- **Primitives:** Button, Input, Select, Textarea, Checkbox, Radio, Toggle, Label, Badge, Icon, Text (typography), Link, Spinner/Loader, Tooltip, Avatar.
- **Composites:** FormField (label + input + error), Card, Modal/Dialog, Table (header + row + cell + pagination), Dropdown Menu, Tabs, Sidebar, Header, Banner/Alert, Toast/Notification.
- **Patterns/recipes:** PageLayout (sidebar + header + content), FormPage (page header + form sections + action bar), TablePage (page header + filters + table + pagination), EmptyState, ErrorState, LoadingSkeleton.

### Backlog Table

| ID | Component / pattern | Tier | Reuse | User impact | Complexity | Dependencies | Owner | Milestone |
|---:|:--------------------|:-----|:------|:------------|:-----------|:-------------|:------|:----------|
| 1 | Button | Primitive | High | High | Low | Tokens: color, spacing, radius, font, focus | Eng 1 | M1 |
| 2 | Input | Primitive | High | High | Low | Tokens: color, spacing, radius, font, focus | Eng 2 | M1 |
| 3 | Select | Primitive | High | High | Med | Input, elevation tokens | Eng 2 | M1 |
| 4 | Textarea | Primitive | Med | Med | Low | Input tokens | Eng 2 | M1 |
| 5 | Checkbox | Primitive | Med | Med | Low | Tokens: color, radius, focus | Eng 1 | M1 |
| 6 | Label | Primitive | High | Med | Low | Typography tokens | Eng 1 | M1 |
| 7 | Text (typography) | Primitive | High | High | Low | Typography tokens | Eng 1 | M1 |
| 8 | FormField | Composite | High | High | Med | Label, Input/Select/Textarea, error state | Eng 2 | M1 |
| 9 | FormPage recipe | Pattern | High | High | Med | FormField, Button, PageHeader | Designer 1 + Eng 3 | M1 |
| 10 | Spinner / Loader | Primitive | Med | Med | Low | Motion tokens, color tokens | Eng 3 | M1 |
| 11 | Card | Composite | High | Med | Low | Tokens: elevation, spacing, radius, color | Eng 3 | M2 |
| 12 | Table | Composite | High | High | High | Text, Button, spacing, elevation tokens | Eng 4 | M2 |
| 13 | Modal / Dialog | Composite | High | High | High | Elevation, focus trap, motion tokens | Eng 3 | M2 |
| 14 | Tabs | Composite | Med | Med | Med | Color, border, focus tokens | Eng 4 | M2 |
| 15 | Badge | Primitive | Med | Low | Low | Color, radius, font tokens | Eng 1 | M2 |
| 16 | Tooltip | Primitive | Med | Low | Med | Elevation, motion tokens | Eng 1 | M2 |
| 17 | Header | Composite | High | Med | Med | Nav, Avatar, elevation tokens | Eng 5 | M2 |
| 18 | Sidebar | Composite | High | Med | Med | Nav items, color tokens | Eng 5 | M2 |
| 19 | PageLayout | Pattern | High | High | Med | Header, Sidebar, content area | Eng 5 + Designer 2 | M2 |
| 20 | TablePage recipe | Pattern | High | High | Med | Table, PageLayout, Button, filters | Eng 4 + Designer 2 | M2 |
| 21 | Banner / Alert | Composite | Med | Med | Low | Color feedback tokens, Icon | Eng 6 | M3 |
| 22 | Toast / Notification | Composite | Med | Med | Med | Elevation, motion, color tokens | Eng 6 | M3 |
| 23 | Dropdown Menu | Composite | Med | Med | Med | Elevation, focus trap, motion tokens | Eng 3 | M3 |
| 24 | Radio | Primitive | Med | Med | Low | Same as Checkbox | Eng 1 | M3 |
| 25 | Toggle | Primitive | Med | Med | Low | Color, motion tokens | Eng 1 | M3 |
| 26 | Avatar | Primitive | Med | Low | Low | Color, radius tokens | Eng 6 | M3 |
| 27 | Link | Primitive | High | Med | Low | Color, font tokens | Eng 2 | M3 |
| 28 | Icon | Primitive | High | Med | Med | Curate icon set (Lucide/Phosphor) | Designer 1 + Eng 6 | M3 |
| 29 | EmptyState | Pattern | Med | Med | Low | Text, Icon, Button | Designer 2 + Eng 5 | M3 |
| 30 | ErrorState | Pattern | Med | Med | Low | Text, Icon, Button | Designer 2 + Eng 5 | M3 |
| 31 | LoadingSkeleton | Pattern | Med | Med | Med | Motion tokens, color tokens | Eng 6 | M3 |

### Milestones

| Milestone | Timeline | Outcome | Scope | Acceptance criteria | Rollback / stop condition |
|:----------|:---------|:--------|:------|:--------------------|:--------------------------|
| **M0: Tokens + tooling** | Weeks 1-2 | Token infrastructure is live; design and code in sync | All P0 tokens defined in Figma variables and code (CSS custom properties or JS tokens). Storybook initialized. Figma library created. | Tokens render correctly in Storybook; Figma variables match code values 1:1; CI lint catches raw hex/px in new code. | If token tooling takes >2 weeks, descope motion/elevation tokens to P1 and ship color+spacing+type only. |
| **M1: Forms foundation** | Weeks 2-4 | Teams can build any form screen using system components | Button, Input, Select, Textarea, Checkbox, Label, Text, FormField, Spinner, FormPage recipe. Figma components + code components + Storybook docs. | All M1 components pass a11y audit (axe-core). At least 1 real product form rebuilt using system components. Documentation includes usage, variants, states, and do/don't for each. | If adoption on the first real form takes >3 days of integration work, pause and investigate API friction before adding more components. |
| **M2: Layout + data display** | Weeks 4-6 | Teams can build full pages (forms + tables + navigation) | Card, Table, Modal, Tabs, Badge, Tooltip, Header, Sidebar, PageLayout, TablePage recipe. | All M2 components pass a11y audit. At least 1 real product page (table view) rebuilt using system components. PageLayout recipe documented with copy-paste example. | If M1 adoption is below 50% of new screens, freeze M2 and focus on adoption/migration support for M1. |
| **M3: Polish + coverage** | Weeks 6-8 | Broad coverage; system handles 80%+ of UI needs | Banner, Toast, Dropdown Menu, Radio, Toggle, Avatar, Link, Icon set, EmptyState, ErrorState, LoadingSkeleton. | 80% of new screens use system components. UI bug reports trending down. All components documented. | If team bandwidth is consumed by M1/M2 bugs, defer M3 components and focus on stabilization. |

---

## 7) Documentation + Enablement Plan

### Doc Set (Minimum)

1. **Quickstart guide:** "How to build a screen using the design system"
   - Start from a recipe (FormPage or TablePage).
   - Replace placeholder content with real data.
   - Use tokens for any custom styling (no raw values).
   - Run the a11y checklist before submitting for review.

2. **Token reference:**
   - Full token list with values, usage rules, and do/don't.
   - Contrast pairing table (which text tokens are safe on which bg tokens).
   - Code snippet showing how to use tokens in CSS/JS.

3. **Component pages (per component):**
   - Purpose (1 sentence).
   - Variants (with visual examples).
   - States (default, hover, focus, active, disabled, error, loading).
   - Props/API reference (for engineers).
   - Do/Don't (with screenshots).
   - Accessibility notes (keyboard, screen reader, contrast).
   - Code example (copy-pasteable).

4. **Recipes:**
   - FormPage recipe (complete code + Figma template).
   - TablePage recipe (complete code + Figma template).
   - EmptyState recipe.
   - SettingsPage recipe.

5. **Contribution guide:**
   - How to request a new component or token.
   - How to propose a change.
   - Review process and timeline.
   - What "done" looks like (states, a11y, docs, Storybook, Figma).

### Enablement Plan

| Audience | Common mistakes | Guardrails to add | Enablement tactic |
|:---------|:----------------|:------------------|:------------------|
| **Non-designers (PMs)** | Using raw colors/sizes in specs; creating new patterns instead of using existing recipes; skipping accessibility requirements | Starter templates in Figma (locked structure, editable content); recipe library with copy-paste examples; "Which component should I use?" decision tree | Biweekly 30-min office hours; Slack channel for quick questions; onboarding walkthrough (15 min) for new team members |
| **Designers** | Detaching Figma components to customize; creating new color/spacing values outside the token set; skipping error/empty/loading states | Figma library with locked base components and constrained variants; token-only color/spacing styles (no custom values); state checklist in component description | Weekly 15-min design sync to review new work against system; Figma library updates pushed with changelog; pair review on first 2 features using the system |
| **Engineers** | Hard-coding values instead of using tokens; building one-off components instead of using/extending system components; skipping keyboard/focus testing | CI lint rule to flag raw hex/px in new CSS; PR template checkbox for "uses system components and tokens"; Storybook a11y addon (axe-core) runs on every story | Storybook as living docs (bookmark it, use it as the source of truth); PR review checklist; pair programming on first system component integration; Slack channel for system questions |

---

## 8) Governance + Adoption Plan

### Decision Rights (Lightweight RACI)

| Area | Responsible | Approver | Consulted | Informed |
|:-----|:------------|:---------|:----------|:---------|
| Token values + naming | Lead designer | Lead designer | Lead engineer, PM | All engineers |
| Component API + behavior | Lead engineer | Lead engineer | Lead designer | All engineers, PM |
| Visual direction / style | Lead designer | PM (scope), Lead designer (execution) | Lead engineer | All team members |
| New component requests | Requesting team member | Lead designer + lead engineer (joint) | -- | All team members |
| Breaking changes | Lead engineer | Lead designer + lead engineer (joint) | PM | All team members |
| Release schedule | Lead engineer | Lead engineer | Lead designer | All team members |

### Contribution Workflow

1. **Request / proposal:** Any team member opens a GitHub issue using the "Design System Request" template (problem statement + screenshots + desired outcome + urgency).
2. **Triage (weekly):** Lead designer + lead engineer review new requests, assign priority (P0/P1/P2), and assign an owner. P0 items enter the current sprint; P1 items enter the next sprint; P2 items go to the backlog.
3. **Spec:** Owner writes a brief spec: variants, states, tokens used, a11y requirements, acceptance criteria. Spec is reviewed by the other discipline (designer specs reviewed by engineer; engineer specs reviewed by designer).
4. **Implementation:** Owner builds the component in both Figma and code. Storybook story created with all states. axe-core a11y check passes.
5. **Review gate:** PR requires approval from at least 1 designer and 1 engineer. Checklist: tokens used (no raw values), all states covered, a11y passing, docs written, Figma component updated.
6. **Release:** Merged to main; included in next biweekly release. Changelog entry written. If breaking change, migration notes provided.
7. **Adoption:** Announcement in Slack with before/after screenshots. Office hours available for migration support.

### Enforcement Mechanisms

- **CI lint (automated):** Fail builds that introduce raw hex, raw px for tokenized properties, or non-system component patterns in new code. Implemented as an ESLint/Stylelint plugin.
- **PR template (semi-automated):** Required checklist item: "New UI changes use design system tokens and components."
- **Storybook a11y (automated):** axe-core addon runs in CI; failing a11y = failing build for system component PRs.
- **Design review (manual):** Lead designer reviews Figma files for system compliance before handoff.

### Champion Plan

| Champion / team | Why they'll adopt first | What they get | Ask | Support needed |
|:----------------|:------------------------|:--------------|:----|:---------------|
| Settings / Admin team (2 engineers) | Forms-heavy; highest pain from inconsistent inputs and layouts; vocal about handoff friction | FormPage recipe eliminates 70% of layout work; consistent forms with built-in a11y | Rebuild 1 settings page using M1 components in week 3-4; provide feedback on component APIs | Pair programming session (2 hrs) with system owner; priority Slack support for first integration |
| Dashboard team (2 engineers) | Table-heavy; most visible to customers; tables are the most-requested component | TablePage recipe + Table component; consistent data display | Rebuild 1 dashboard table view using M2 components in week 5-6; provide feedback on Table API | Pair programming session (2 hrs); priority Slack support |
| Lead designer | Owns Figma library; wants to stop redrawing the same inputs every sprint | Figma library with variants and auto-layout; faster hi-fi output | Maintain Figma library; review all component specs; champion system in design reviews | Dedicated time allocation (20% of sprint) for system work |

### Release Cadence

| Cadence | What | Who |
|:--------|:-----|:----|
| **Biweekly** (aligned with sprints) | Versioned release of new/updated components + tokens. Changelog published. | Lead engineer releases; lead designer reviews. |
| **As needed** | Hotfixes for a11y regressions or breaking bugs. | Any engineer; lead engineer approves. |
| **Monthly** | Adoption report: % of new screens using system components, number of one-off CSS additions, UI bug count. Shared with full team. | Lead designer + lead engineer. |
| **Quarterly** | Roadmap review: reprioritize backlog based on adoption data, team feedback, and product needs. | Lead designer + lead engineer + PM. |

---

## 9) Quality Gate

### Checklist Results

#### A) Scope + assumptions
- [x] The system's audiences are explicit (designers, engineers, PMs/non-designers).
- [x] In-scope vs out-of-scope is clear (no hidden work).
- [x] Stakeholders and decision-maker(s) are explicit.
- [x] Assumptions are labeled (platforms, stack, tooling, timeline).

#### B) Operational hook + first slice
- [x] The "operational blocker" is stated in plain language.
- [x] The first slice is narrow enough to ship but pattern-setting.
- [x] Success signals include adoption and at least one speed/quality metric.

#### C) Blockframes (logic before styling)
- [x] Key flows have lo-fi blockframes or an equivalent structural spec.
- [x] Blockframes map blocks to components/patterns (not just rectangles).
- [x] Key states (loading/empty/error/disabled/focus) are considered where relevant.

#### D) Token model quality
- [x] Token taxonomy and naming rules are documented.
- [x] Semantic tokens are used (not raw colors/values in specs).
- [x] Elevation/depth and state tokens exist.
- [x] Accessibility constraints are addressed (contrast, focus, reduced motion).

#### E) Component model + roadmap
- [x] Components are tiered (primitives/composites/patterns).
- [x] Roadmap prioritizes reuse + user impact (not convenience).
- [x] Milestones have acceptance criteria and a rollback/stop condition.

#### F) Documentation + ease-of-use
- [x] Docs are example-first and include do/don't guidance.
- [x] Templates/recipes exist so non-experts can produce consistent UI.
- [x] The system has sensible defaults and constrained variants (guardrails).

#### G) Governance + adoption
- [x] Decision rights are explicit (tokens, components, visual direction).
- [x] Contribution workflow is clear (proposal to review to release).
- [x] Adoption plan includes champions/office hours and migration support.

#### H) Finalization
- [x] Risks, open questions, and next steps are included at the end.
- [x] No secrets/credentials were requested or recorded.

### Rubric Score

| Dimension | Score (1-5) | Notes |
|:----------|:------------|:------|
| Scope clarity | 5 | Clear audiences, in/out scope, explicit redirects to `design-engineering`, `running-design-reviews`, `engineering-culture`, and `writing-specs-designs`. |
| Operational leverage | 5 | Strong hook (slow handoff + one-off CSS), narrow first slice (forms + tokens), measurable success signals with concrete targets (50% handoff reduction, 80% adoption). |
| Token architecture | 5 | Full taxonomy with semantic color, spacing, type, radius, elevation, motion, and focus tokens. Explicit a11y rules (contrast pairs, focus ring, reduced motion). Token model supports style evolution (dark mode deferred but structurally supported). |
| Component roadmap executability | 5 | Tiered (primitives to composites to patterns). 4 milestones with acceptance criteria and rollback/stop conditions. Each milestone has a committed consumer team. M1 ships in weeks 2-4. |
| Documentation usability | 4 | Example-first docs with do/don't, recipes, quickstart guide, and contribution guide. Both audiences addressed. Starter templates present. Minor gap: recipes are planned but not yet written (will ship with M1/M2). |
| Governance + adoption plan | 5 | Clear decision rights, 7-step contribution workflow, enforcement mechanisms (CI lint, PR template, Storybook a11y), champion plan with specific teams and asks, release cadence with adoption tracking. |

**Total: 29/30**

**Top 3 improvements:**
1. Write the actual FormPage and TablePage recipe content (code + Figma) before M1 ships, not just the plan for them.
2. Add a "component decision tree" diagram that helps non-designers pick the right component for their use case (currently described as a tactic but not drafted).
3. Define the specific CI lint rules (ESLint/Stylelint config) as a concrete task in M0 so token enforcement is automated from day one.

---

### Risks

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| **Small team bandwidth:** 2 designers + 6 engineers must ship product features AND build the system | High | High | Allocate 20% of sprint capacity to system work (not 100%). First slice is deliberately narrow. Milestones have stop conditions. |
| **Adoption friction:** Engineers resist adopting new components because migration is painful or APIs are awkward | Medium | High | Champion plan ensures early adopters provide API feedback before broad rollout. Pair programming support for first integrations. Stop condition on M2 if M1 adoption is below 50%. |
| **Token drift:** Designers or engineers create values outside the token set under time pressure | Medium | Medium | CI lint catches raw values in code. Figma library uses locked base components. Monthly adoption report tracks one-off CSS count. |
| **Scope creep:** Requests for enterprise theming, dark mode, or mobile components before the foundation is solid | Medium | Medium | Charter explicitly scopes these out. Quarterly roadmap review is the venue for expanding scope. |
| **Single points of failure:** Lead designer and lead engineer are sole decision-makers; if either is unavailable, system work stalls | Low | High | Document all decisions in the system's changelog and ADR (architecture decision records). Cross-train at least 1 backup per role by M2. |

### Open Questions

1. **Which CSS methodology/tooling will enforce token usage?** Options: CSS custom properties + Stylelint plugin, Tailwind with custom config, or CSS-in-JS theme object. Decision needed before M0 implementation begins.
2. **Should the Figma library use Figma Variables (new) or traditional styles?** Variables offer better token mapping but require team familiarity. Recommend Variables if the team is on Figma plan that supports them.
3. **What is the existing codebase's CSS architecture?** The migration strategy (gradual replacement vs. parallel system) depends on whether CSS is in modules, global stylesheets, styled-components, etc.
4. **Is there a staging/preview environment where Storybook can be deployed?** Needed for the "Storybook as living docs" strategy.
5. **Who is the PM sponsor?** The charter assumes PM involvement for scope decisions and success metric tracking, but no specific PM has been identified.

### Next Steps

1. **This week:** Hold a 1-hour kickoff with the full team (2 designers + 6 engineers + PM). Walk through this operating pack. Confirm the token tooling decision (open question #1) and assign M0 owners.
2. **Weeks 1-2 (M0):** Implement token infrastructure in code and Figma. Set up Storybook. Configure CI lint for token enforcement. Publish the token reference doc.
3. **Weeks 2-4 (M1):** Build forms foundation (Button, Input, Select, Textarea, Checkbox, FormField, FormPage recipe). Settings team rebuilds 1 real form. Collect feedback on component APIs and adjust before M2.
