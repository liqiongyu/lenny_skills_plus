# Saved Views for Analytics Dashboard

## Part 1: PR/FAQ (Press Release / Frequently Asked Questions)

---

### PRESS RELEASE

**FOR IMMEDIATE RELEASE**

**Analytics Dashboard Introduces "Saved Views" — Empowering Admins to Instantly Access the Reports That Matter Most**

*New feature eliminates repetitive configuration and lets administrators save, share, and recall custom dashboard layouts in one click.*

**The Problem**

Administrators using the analytics dashboard spend significant time each day reconfiguring filters, date ranges, metric selections, and layout arrangements to reach the specific data views they need. Research shows that power users configure an average of 5–8 distinct dashboard setups throughout their workweek, with each configuration taking 2–4 minutes to rebuild from scratch. This repetitive work erodes productivity, introduces errors (wrong filters left in place), and discourages deeper exploration of the data.

**The Solution**

Starting today, admins can save any dashboard configuration as a named "Saved View" and recall it instantly. Saved Views capture the complete state of a dashboard — including selected metrics, applied filters, date ranges, sort orders, chart types, and column visibility — and let admins restore that exact configuration with a single click. Admins can organize views into folders, mark favorites for quick access, and share views with teammates so the entire admin team benefits from a consistent, curated set of reports.

**How It Works**

1. An admin configures the dashboard to show exactly the data they need.
2. They click the "Save View" button in the toolbar.
3. They name the view, optionally add a description, choose a folder, and set sharing permissions (private, team, or organization-wide).
4. The saved view appears in the sidebar panel and can be loaded at any time.
5. When the underlying data updates, the saved view automatically reflects the latest numbers without any manual refresh.

**Customer Quote**

*"Before Saved Views, I'd spend the first 15 minutes of every morning rebuilding my executive summary dashboard. Now I click one button and I'm looking at live data in the exact layout I need. It's a small feature that has a massive impact on my daily workflow."*
— Sarah Chen, Head of Operations

**Getting Started**

Saved Views is available to all admin-tier users at no additional cost. Admins will see a new "Views" panel in the left sidebar upon their next login. Existing dashboard configurations can be saved immediately — no migration required.

---

### FREQUENTLY ASKED QUESTIONS

#### External FAQs (Customer-Facing)

**Q1: How many saved views can I create?**
A: Each admin can create up to 100 personal saved views. Shared (team-level) views have an additional pool of 200 per organization. Enterprise plans have unlimited views.

**Q2: Can I share a saved view with someone who isn't an admin?**
A: Saved views respect existing role-based access controls. You can share a view with any user who has at least read access to the underlying data sources referenced in that view. If a recipient lacks access to certain metrics, those will display as "restricted" when they load the view.

**Q3: What exactly is captured in a saved view?**
A: A saved view captures: selected metrics/KPIs, applied filters and segments, date range (relative or absolute), sort order, chart type selections, column visibility and ordering, layout/grid arrangement, and any comparison settings (e.g., period-over-period).

**Q4: If I use a relative date range (e.g., "Last 7 Days"), does the view update automatically?**
A: Yes. Relative date ranges are stored as relative references, so "Last 7 Days" always reflects the most recent 7-day window when the view is loaded.

**Q5: Can I edit a saved view after creating it?**
A: Yes. Load the saved view, make your changes, then click "Update View" to overwrite or "Save as New View" to create a copy. You can also rename, re-describe, move to a different folder, or change sharing permissions from the view's context menu.

**Q6: What happens to shared views if the creator's account is deactivated?**
A: Shared views are retained and transferred to the organization's admin pool. An org-level admin can reassign ownership. Private views belonging to deactivated accounts are archived for 90 days before permanent deletion.

**Q7: Will Saved Views slow down my dashboard?**
A: No. Saved Views are lightweight metadata objects (typically < 2 KB). They store configuration state, not cached data. Loading a saved view is equivalent in performance to manually applying the same filters.

#### Internal FAQs (Team-Facing)

**Q8: Why are we building this now?**
A: "Save my dashboard setup" has been the #1 most-requested feature in our admin feedback channel for three consecutive quarters. Churn interviews reveal that 23% of departing admin users cite "too much repetitive setup" as a friction point. Competitive analysis shows 4 of our top 5 competitors already offer some form of saved/bookmarked views.

**Q9: What is the expected impact on key metrics?**
A: We expect:
- **Admin DAU/MAU ratio** to increase by 5–10% (reduced friction = more frequent visits)
- **Session duration** to decrease by 10–15% for routine tasks (faster time-to-insight)
- **NPS among admin users** to increase by 3–5 points within one quarter of launch
- **Support tickets related to "how to filter/configure"** to decrease by 20%

**Q10: What are the main technical risks?**
A: (1) Schema evolution — if we add new dashboard features (new filter types, new chart options), saved views must gracefully handle missing or deprecated fields. We will version the view schema and implement forward-compatible defaults. (2) Permissions drift — if a user's role changes, shared views must re-evaluate access at load time, not at save time. (3) Storage at scale — at 100 views per user across thousands of admins, we need efficient indexing; we plan to use a dedicated views table with JSON payloads and appropriate indices.

**Q11: What are we explicitly NOT building in v1?**
A: We are not building: scheduled email delivery of saved views, PDF/image export of saved views, version history/undo for view edits, or embedding saved views in external pages. These are candidates for v2 based on adoption data.

**Q12: How will we measure success?**
A: Primary metric: adoption rate (% of active admins who create at least one saved view within 30 days of launch). Target: 40%. Secondary metrics: views-loaded-per-week, reduction in average dashboard configuration time, and NPS lift.

---

## Part 2: Product Requirements Document (PRD)

---

### 1. Overview

| Field | Detail |
|---|---|
| **Product** | Analytics Dashboard |
| **Feature** | Saved Views |
| **Author** | Product Team |
| **Status** | Draft |
| **Target Users** | Admin users |
| **Target Release** | Q3 2026 |
| **Priority** | P0 (High) |

### 2. Problem Statement

Admin users of the analytics dashboard frequently need to view the same data configurations repeatedly — for example, a daily executive summary, a weekly funnel report, or a monthly cohort analysis. Today, they must manually reconfigure filters, metrics, date ranges, and layouts each time. This leads to:

- **Wasted time**: 10–20 minutes per day per admin spent on repetitive configuration.
- **Inconsistency**: When multiple admins configure the same report manually, they often end up with slightly different filter combinations, leading to conflicting numbers in meetings.
- **Frustration**: The lack of persistence is the #1 complaint in our admin feedback channel.
- **Reduced exploration**: Admins avoid experimenting with new configurations because they fear losing their current setup.

### 3. Goals and Success Metrics

#### Goals

1. **Eliminate repetitive configuration work** by allowing admins to save and recall dashboard states.
2. **Promote consistency** by enabling shared views that serve as a single source of truth.
3. **Increase admin engagement** by reducing friction and enabling faster time-to-insight.

#### Success Metrics

| Metric | Current Baseline | Target (90 days post-launch) |
|---|---|---|
| Adoption rate (% admins with >= 1 saved view) | 0% | 40% |
| Avg. views loaded per admin per week | 0 | 8 |
| Avg. time to reach desired dashboard state | ~3.5 min | < 30 sec (via saved view) |
| Admin NPS | 32 | 37 |
| Config-related support tickets per month | ~120 | < 95 |

### 4. User Personas

#### Primary: Power Admin ("Ops Lead")
- Uses the dashboard 5–7 days/week
- Maintains 6–10 distinct report configurations
- Shares reports with team leads in weekly standups
- Pain: spends 15+ minutes each morning rebuilding views

#### Secondary: Occasional Admin ("Department Head")
- Uses the dashboard 2–3 times/week
- Relies on 2–3 standard reports
- Often asks the Ops Lead to "send me that view"
- Pain: can never remember which filters to apply

### 5. User Stories

| ID | Story | Priority |
|---|---|---|
| US-1 | As an admin, I want to save my current dashboard configuration so I can return to it later without manual setup. | P0 |
| US-2 | As an admin, I want to name and describe my saved views so I can identify them quickly. | P0 |
| US-3 | As an admin, I want to load a saved view with one click so I can immediately see the data I need. | P0 |
| US-4 | As an admin, I want to update an existing saved view with my current configuration so I can evolve my views over time. | P0 |
| US-5 | As an admin, I want to delete saved views I no longer need so my view list stays manageable. | P0 |
| US-6 | As an admin, I want to organize my saved views into folders so I can group related views (e.g., "Daily Reports", "Monthly Reviews"). | P1 |
| US-7 | As an admin, I want to share a saved view with other admins so we can align on the same data perspective. | P1 |
| US-8 | As an admin, I want to mark certain views as favorites so my most-used views are always accessible at the top. | P1 |
| US-9 | As an admin, I want to duplicate a saved view so I can use it as a starting point for a variation. | P2 |
| US-10 | As an admin, I want to see when a saved view was last modified and by whom so I have context on its freshness. | P2 |

### 6. Detailed Requirements

#### 6.1 Saving a View

- A "Save View" button is present in the dashboard toolbar whenever the current configuration differs from the default state or from the currently loaded saved view.
- Clicking "Save View" opens a modal with the following fields:
  - **Name** (required, max 80 characters)
  - **Description** (optional, max 300 characters)
  - **Folder** (optional, select from existing or create new)
  - **Sharing** (radio: Private / Team / Organization)
- Upon saving, the system captures the full dashboard state:
  - Selected metrics and KPIs
  - All applied filters (dimension, operator, value)
  - Segments
  - Date range (stored as relative or absolute, based on user's selection)
  - Comparison settings (e.g., previous period, year-over-year)
  - Sort column and direction
  - Chart type per widget
  - Column visibility and order
  - Dashboard layout/grid positions (if customizable)
- The view is persisted to the backend and immediately appears in the sidebar.
- If an existing saved view is loaded and modified, the button changes to offer "Update View" (overwrite) and "Save as New View" (fork).

#### 6.2 Loading a View

- The left sidebar contains a collapsible "Saved Views" panel.
- Views are displayed in a tree structure organized by folders.
- Each view shows: name, sharing icon (private/team/org), and a favorite star.
- Clicking a view name instantly loads the saved configuration.
- While loading, the dashboard shows a brief transition indicator (skeleton or shimmer).
- If the saved view references a filter value or metric that no longer exists (e.g., a deleted segment), the system loads the view with a warning banner: "Some elements of this view are no longer available. [Details]"

#### 6.3 Managing Views

- **Edit metadata**: Right-click or kebab menu on any view to rename, edit description, move to a different folder, or change sharing permissions.
- **Delete**: Available via context menu. Confirmation dialog required. If the view is shared, warn that other users will lose access.
- **Duplicate**: Creates a copy with " (Copy)" appended to the name, placed in the same folder.
- **Favorites**: Click the star icon to toggle favorite status. Favorites appear in a pinned "Favorites" section at the top of the sidebar panel.

#### 6.4 Folders

- Admins can create, rename, and delete folders.
- Folders support one level of nesting only (no sub-sub-folders) to keep the UI clean.
- Deleting a folder moves its views to "Uncategorized."
- Default folders: "Uncategorized" (cannot be deleted or renamed).

#### 6.5 Sharing and Permissions

| View Visibility | Who Can See | Who Can Edit |
|---|---|---|
| Private | Creator only | Creator only |
| Team | All admins in the creator's team | Creator + team admins with "manage views" permission |
| Organization | All admins in the org | Creator + org-level admins |

- Shared views are read-only for non-owners by default. Users with edit permissions can update the view.
- Loading a shared view does not modify the sharer's version — it operates on the viewer's dashboard session.
- Admins can "Save as New View" from a shared view to create their own private copy.

#### 6.6 View Versioning (v1 Scope — Minimal)

- Each save/update operation creates a new version internally.
- v1 does not expose version history in the UI; this is for data integrity and future extensibility.
- The system stores the 10 most recent versions per view for potential future rollback functionality.

### 7. Information Architecture and UX

#### 7.1 Navigation Changes

```
Dashboard (existing)
├── [Toolbar]
│   ├── ... existing controls ...
│   └── [Save View] button (NEW)
├── [Left Sidebar]
│   ├── ... existing navigation ...
│   └── [Saved Views Panel] (NEW)
│       ├── ★ Favorites
│       ├── 📁 Folder 1
│       │   ├── View A
│       │   └── View B
│       ├── 📁 Folder 2
│       │   └── View C
│       └── Uncategorized
│           └── View D
└── [Main Content Area] (unchanged)
```

#### 7.2 Key Screens and Flows

1. **Save View Modal**: Triggered from toolbar. Clean form with name, description, folder picker, sharing radio buttons, and Save/Cancel actions.
2. **Sidebar Panel**: Collapsible tree view. Search/filter bar at the top. Drag-and-drop reordering within and between folders.
3. **View Context Menu**: Right-click or kebab icon. Options: Open, Edit Details, Duplicate, Move to Folder, Share Settings, Delete.
4. **Unsaved Changes Indicator**: When a loaded view has been modified, the view name in the toolbar shows a dot indicator and the save button becomes "Update View | Save as New."

#### 7.3 Empty States

- **No saved views yet**: Illustration + "Save your first view" CTA with brief explanation of the feature.
- **No views in folder**: "This folder is empty. Drag views here to organize them."
- **Search yields no results**: "No views match your search."

### 8. Technical Design

#### 8.1 Data Model

```
saved_views
├── id (UUID, PK)
├── name (VARCHAR 80, NOT NULL)
├── description (VARCHAR 300, NULLABLE)
├── creator_id (FK → users.id)
├── organization_id (FK → organizations.id)
├── team_id (FK → teams.id, NULLABLE)
├── folder_id (FK → view_folders.id, NULLABLE)
├── visibility (ENUM: private, team, organization)
├── is_favorite (BOOLEAN, per-user — stored in separate table)
├── schema_version (INTEGER, default 1)
├── configuration (JSONB)
│   ├── metrics: [...]
│   ├── filters: [...]
│   ├── date_range: { type, start, end, relative_period }
│   ├── comparison: { enabled, type, ... }
│   ├── sort: { column, direction }
│   ├── charts: [{ widget_id, chart_type }]
│   ├── columns: [{ id, visible, order }]
│   └── layout: { grid_positions }
├── display_order (INTEGER)
├── created_at (TIMESTAMP)
├── updated_at (TIMESTAMP)
└── deleted_at (TIMESTAMP, soft delete)

view_folders
├── id (UUID, PK)
├── name (VARCHAR 80, NOT NULL)
├── owner_id (FK → users.id)
├── parent_folder_id (FK → view_folders.id, NULLABLE — one level only)
├── display_order (INTEGER)
├── created_at (TIMESTAMP)
└── updated_at (TIMESTAMP)

view_favorites (join table)
├── user_id (FK → users.id)
├── view_id (FK → saved_views.id)
└── created_at (TIMESTAMP)

view_versions
├── id (UUID, PK)
├── view_id (FK → saved_views.id)
├── version_number (INTEGER)
├── configuration (JSONB)
├── updated_by (FK → users.id)
└── created_at (TIMESTAMP)
```

#### 8.2 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/views` | Create a new saved view |
| GET | `/api/v1/views` | List all views accessible to the current user |
| GET | `/api/v1/views/:id` | Get a specific view's configuration |
| PUT | `/api/v1/views/:id` | Update a saved view |
| DELETE | `/api/v1/views/:id` | Soft-delete a saved view |
| POST | `/api/v1/views/:id/duplicate` | Duplicate a view |
| PUT | `/api/v1/views/:id/favorite` | Toggle favorite status |
| POST | `/api/v1/folders` | Create a folder |
| GET | `/api/v1/folders` | List folders for current user |
| PUT | `/api/v1/folders/:id` | Update folder (rename, reorder) |
| DELETE | `/api/v1/folders/:id` | Delete folder (moves views to uncategorized) |

#### 8.3 Performance Considerations

- Saved view configurations (JSONB) are typically 1–2 KB. At 100 views per user across 10,000 admin users, total storage is ~1–2 GB — trivially manageable.
- List endpoints should support pagination but will rarely need it given the per-user cap.
- Loading a view is a single GET followed by client-side state hydration — no additional data queries beyond the normal dashboard data fetch.
- Index on `(organization_id, visibility)` and `(creator_id)` for efficient list queries.

#### 8.4 Schema Evolution Strategy

- The `schema_version` field tracks the configuration format version.
- When loading a view, a migration function upgrades the configuration from its stored version to the current version.
- Migrations are additive: new fields get sensible defaults; removed fields are ignored.
- This ensures backward compatibility as the dashboard adds new features.

### 9. Edge Cases and Error Handling

| Scenario | Handling |
|---|---|
| Saved view references a deleted metric | Load view with available elements; show warning banner listing unavailable items |
| Saved view references a filter value that no longer exists | Omit the invalid filter; show warning |
| User tries to load a shared view they no longer have permission to see | Return 403; show "This view is no longer available to you" |
| User reaches the 100-view limit | Disable "Save View" button; show tooltip: "View limit reached. Delete existing views to save new ones." |
| Two users simultaneously update a shared view | Last-write-wins with optimistic concurrency (ETag/If-Match). Show conflict notification to the second user. |
| Dashboard is loading when user clicks a saved view | Queue the view load; apply after current load completes |
| Browser crashes mid-save | Standard autosave/draft behavior: the incomplete view is not persisted |
| Exported/imported views between environments | Out of scope for v1; earmarked for v2 |

### 10. Security Considerations

- All view CRUD operations require valid admin authentication.
- View access is checked at load time (not just save time) to handle permission changes.
- The `configuration` JSONB payload is validated server-side against a schema to prevent injection of unexpected fields.
- Shared views do not expose data the recipient cannot already access — the view is a configuration template, and data is fetched with the loading user's permissions.
- Soft deletes ensure audit trail; hard deletes occur only via scheduled cleanup after 90-day retention.
- API rate limits: 50 view operations per minute per user to prevent abuse.

### 11. Rollout Plan

| Phase | Timeline | Description |
|---|---|---|
| Alpha | Week 1–2 | Internal dogfooding with the product and engineering teams |
| Beta | Week 3–4 | Invite 50 power-admin users from top accounts; collect feedback |
| GA Rollout (10%) | Week 5 | Enable for 10% of admin users; monitor error rates and performance |
| GA Rollout (50%) | Week 6 | Expand to 50%; monitor adoption metrics |
| GA Rollout (100%) | Week 7 | Full availability to all admin users |
| Post-launch | Week 8–10 | Analyze adoption data, collect feedback, plan v2 features |

### 12. Dependencies

- **Frontend**: Dashboard state serialization/deserialization logic
- **Backend**: New database tables and API endpoints
- **Design**: Updated sidebar component, save modal, empty states, warning banners
- **Infrastructure**: No new infrastructure required; uses existing database
- **Other teams**: None — fully owned by the dashboard team

### 13. Out of Scope (v1)

The following are explicitly deferred to future iterations:

- Scheduled delivery (email saved views on a cadence)
- Export to PDF/PNG/CSV from a saved view
- Version history UI and rollback
- Embedding saved views in external pages or iframes
- Public (unauthenticated) sharing links
- Saved views for non-admin user roles
- Cross-dashboard views (combining widgets from multiple dashboards)
- Mobile-optimized saved views management

### 14. Open Questions

| # | Question | Owner | Status |
|---|---|---|---|
| 1 | Should we support URL-based deep links to saved views (e.g., `/dashboard?view=abc-123`)? | Engineering | **Recommended yes** — low effort, high utility |
| 2 | Should shared views count against the creator's personal limit of 100? | Product | Pending decision |
| 3 | Do we want to track view load analytics (which views are loaded most often) for internal reporting? | Data/Analytics | **Recommended yes** — useful for understanding feature value |
| 4 | Should we allow admins to set a "default view" that loads automatically on dashboard open? | Product | Candidate for fast follow |

### 15. Milestones and Timeline

| Milestone | Target Date | Key Deliverables |
|---|---|---|
| Design complete | Week 1 | Figma mockups for all screens and states |
| Backend API complete | Week 3 | All endpoints functional with tests |
| Frontend integration | Week 5 | Save, load, manage flows working end-to-end |
| QA complete | Week 6 | All edge cases tested, performance validated |
| Alpha launch | Week 7 | Internal release |
| Beta launch | Week 8 | External beta with select customers |
| GA launch | Week 10 | Full release to all admin users |

---

*This document should be reviewed by Engineering, Design, and QA leads before development begins. All stakeholders should sign off on the scope boundaries defined in Section 13.*
