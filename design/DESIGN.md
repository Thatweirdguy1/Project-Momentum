---
name: Momentum ADHD Fitness
colors:
  surface: '#0c1321'
  surface-dim: '#0c1321'
  surface-bright: '#323949'
  surface-container-lowest: '#070e1c'
  surface-container-low: '#151b2a'
  surface-container: '#19202e'
  surface-container-high: '#232a39'
  surface-container-highest: '#2e3544'
  on-surface: '#dce2f6'
  on-surface-variant: '#bbcac5'
  inverse-surface: '#dce2f6'
  inverse-on-surface: '#2a3040'
  outline: '#86948f'
  outline-variant: '#3c4946'
  surface-tint: '#5bdbc3'
  primary: '#75f3da'
  on-primary: '#00382f'
  primary-container: '#55d6be'
  on-primary-container: '#005a4d'
  inverse-primary: '#006b5c'
  secondary: '#f5bc7e'
  on-secondary: '#482900'
  secondary-container: '#67400d'
  on-secondary-container: '#e5ae71'
  tertiary: '#d0dff5'
  on-tertiary: '#233143'
  tertiary-container: '#b4c3d9'
  on-tertiary-container: '#425063'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7af8de'
  primary-fixed-dim: '#5bdbc3'
  on-primary-fixed: '#00201b'
  on-primary-fixed-variant: '#005045'
  secondary-fixed: '#ffddbb'
  secondary-fixed-dim: '#f5bc7e'
  on-secondary-fixed: '#2b1700'
  on-secondary-fixed-variant: '#653e0b'
  tertiary-fixed: '#d4e4fa'
  tertiary-fixed-dim: '#b9c8de'
  on-tertiary-fixed: '#0d1c2d'
  on-tertiary-fixed-variant: '#39485a'
  background: '#0c1321'
  on-background: '#dce2f6'
  surface-variant: '#2e3544'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: 0em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0.005em
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.01em
  label-lg:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-md:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.03em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.04em
  numeric-metric:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  numeric-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.25rem
  gutter-desktop: 1.5rem
  margin: 1.5rem
  margin-desktop: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system targets neurodivergent adults—specifically individuals with ADHD—seeking sustainable, non-punitive physical training and nutrition logging. Executive dysfunction, working memory limits, and sensory overwhelm make conventional fitness interfaces counterproductive. The system rejects gamified guilt, flashing streaks, visual clutter, and aggressive push cues.

Instead, the aesthetic blends **Modern Minimalist Surface Hierarchy** with **Windows-Native Desktop Ergonomics**. It delivers a calm sanctuary through deep slate navy surfaces, warm daylight-toned typography, tactile low-stimulation feedback, and clear structural anchor points.

### Visual Tenets
- **Cognitive Calm:** High baseline contrast between dark structural surfaces and warm-white text minimizes optical fatigue and visual hunting.
- **Forgiving & Elastic:** Zero shame mechanics. The interface accommodates oscillating motivation and energy states (Minimum, Short, Normal, Recovery) without breaking visual continuity or signaling failure.
- **Physicality & Legibility:** Crisp tabular metrics, explicit card bounds, and generous spatial separation offer instant visual chunking that scaffolds working memory.
- **Desktop Precision:** Built around Windows-tailored desktop paradigms, supporting clear title bar allocations, dense yet breathable utility toolbars, and unambiguous keyboard focus states.

## Colors

The palette is engineered exclusively for a deep, non-glare dark mode that preserves attentional focus during prolonged desktop sessions.

### Core Swatches
- **Canvas Base (`#0B1220`):** The primary canvas background; grounds the app in a deep, void-adjacent navy that eliminates edge vibration on high-refresh desktop monitors.
- **Surface Secondary (`#111A2E`):** Distinct structural layer used for persistent sidebars, fixed headers, and structural trays.
- **Surface Elevated (`#162238`):** Card panels, active input contexts, and floating panels.
- **Structural Border (`#1E2B45`):** Subdued boundary line separating spatial contexts without creating visual prison-bars.
- **Primary Teal (`#55D6BE`):** Non-aggressive, affirmative accent indicating completion, active toggles, primary buttons, and successful synchronization.
- **Gentle Amber (`#E0A96D` / `#F59E0B`):** Warm gold accent used strictly for attention-needing states, local edits, and capacity shifts. Never used as an aggressive error red or shame trigger.

### Neutral & Typography Tokens
- **Text Primary (`#F2F0EA`):** Soft, warm-white foreground reducing the harsh optical vibration of pure `#FFFFFF` against dark navy.
- **Text Secondary (`#94A3B8`):** Readable slate for secondary data, guidance microcopy, and unit markers.
- **Text Tertiary / Disabled (`#64748B`):** Muted slate for metadata, hotkeys, and passive dividers.

### Status Tones
- **Synced / Healthy:** Subtle muted teal fill (`rgba(85, 214, 190, 0.12)`) with `#55D6BE` text.
- **Pending / Offline Draft:** Muted amber fill (`rgba(224, 169, 109, 0.14)`) with `#E0A96D` text.
- **Neutral / Demo:** Slate fill (`rgba(148, 163, 184, 0.12)`) with `#94A3B8` text.

## Typography

The type system pairs **Space Grotesk** for structural markers, navigation, data metrics, and labels with **Plus Jakarta Sans** for body readability and instructions.

### Executive Function Rules
- **Tabular Numerals Everywhere:** All numerical outputs (reps, weights, calories, time, sets) enforce `font-variant-numeric: tabular-nums;`. This prevents visual shifting during live adjustments and facilitates column scanning.
- **Scannable Weight Steps:** Avoid nuanced, low-contrast weight differences (e.g., mixing 400 and 500 weights within the same visual boundary). Only regular (400), medium (500), and semibold (600) are utilized.
- **Generous Text Line Height:** Body text uses a minimum of 1.55x line height to prevent line-jumping when reading multi-step workout sequences or meal recipes.

## Layout & Spacing

The layout model is anchored by a persistent Windows-optimized workspace: a rigid left-hand global navigation bar (width: 260px) paired with a 12-column adaptive fluid content canvas.

### Layout Structure
- **Windows Title & System Bar:** Top 40px reserved for mock window controls, workspace status pills, and global sync alerts.
- **Sidebar (Fixed):** Anchored to `#111A2E`, providing constant situational awareness without menu diving.
- **Main Canvas Grid:** 12 columns with standard 24px desktop gutters (`gutter-desktop`) and 32px canvas margins (`margin-desktop`).
- **Content Max-Width:** Data density is intentionally bounded; card grids cap at `1440px` to prevent sprawling data rows that cause tracking drop-off on ultrawide monitors.

### Spacing Rhythm
Spacing is derived from a strict 4px/8px modular scale. Spacing within an informational unit (e.g., set inputs, macro metrics) uses `space-xs` and `space-sm`. Structural boundaries between unassociated clusters mandate `space-lg` to `space-xl` to ensure cognitive isolation.

## Elevation & Depth

To avoid visual fuzziness that can tax attention, this design system minimizes heavy drop shadows. Depth is communicated via **Tonal Layering** accompanied by **Subtle Low-Contrast Outlines**.

### Surface Hierarchy
1. **Base Layer (`#0B1220`):** Application canvas and desktop gutter backdrop.
2. **Structural Layer (`#111A2E`):** Sidebar navigation, fixed search trays, and app utility panels. Outlined with 1px border of `#1E2B45`.
3. **Card Layer (`#162238`):** Discrete workout items, meal entry panels, and metric monitors. Bordered with 1px `#1E2B45`.
4. **Interactive Overlay / Popover (`#1C2A44`):** Context menus, quick-log drawers, and modal dialogs. Elevated using a single ambient shadow: `0 12px 32px -4px rgba(4, 8, 16, 0.65)` with a 1px border of `rgba(85, 214, 190, 0.25)` to clearly delimit modal context.

### Interaction States
Cards never jump toward the user with aggressive vertical translation. On hover, a card’s border transitions smoothly from `#1E2B45` to a muted highlight (`#2B3D60`), reinforcing clickability without visual vibration.

## Shapes

The design system employs a **Rounded** shape profile (`roundedness: 2`). Base UI elements feature an 8px radius (`0.5rem`), scaling to 16px (`1rem`) on content containers, and 24px (`1.5rem`) on hero summary zones.

This balance avoids the aggressive edge of brutalism while steering clear of overly bubbly, juvenile pill geometry that detracts from desktop productivity. Circular geometry is reserved strictly for icon buttons, status dots, and progress rings.

## Components

### Buttons
- **Primary Action:** Solid `#55D6BE` background with dark navy text (`#0B1220`) in `label-lg` Space Grotesk. Hover: shifts to `#6FE2CB`. Active: pressed state with 0.98 scale transform.
- **Secondary Action:** Transparent background with 1px border of `#1E2B45` and `#F2F0EA` text. Hover: `#162238` surface fill with `#2B3D60` border.
- **Capacity Selector Buttons:** Segmented multi-state toggle (Minimum, Short, Normal, Recovery). Selected state features a subtle warm amber or teal surface wash (`rgba(85, 214, 190, 0.15)`) with a crisp solid border, explicitly communicating current energy capacity.
- **Focus Ring Standard:** All interactive controls display an offset 2px solid teal ring (`#55D6BE`) with a 2px gap (`#0B1220`) under keyboard navigation.

### Status Pills & Sync Tags
- Compact tags formatted in `label-sm` Space Grotesk with 4px vertical padding and 8px horizontal padding, rounded to 6px.
- **"DEMO DATA" / "LOCAL DRAFT":** Slate border, slate text (`#94A3B8`).
- **"PENDING UPLOAD":** Muted amber text (`#E0A96D`), amber-tinted background (`rgba(224, 169, 109, 0.12)`).
- **"SYNCED":** Soft teal text (`#55D6BE`), teal-tinted background (`rgba(85, 214, 190, 0.10)`).

### Metric Cards & Quick-Log Cards
- Structured rectangular cards with surface `#162238` and a 1px `#1E2B45` border.
- Data displays highlight numbers using the `numeric-metric` token in Space Grotesk, while unit designations (kg, reps, kcal) sit inline in `body-sm` slate text (`#94A3B8`).
- Progress indicators do not show "missed days" or broken streak marks. Instead, they present total volume completed and positive capacity markers.

### Input Fields & Numeric Steppers
- Input backgrounds use `#111A2E` with an internal padding of `10px 14px` and a 1px `#1E2B45` outline.
- Active typing shifts the border to `#55D6BE`.
- Numeric steppers (weight/reps) feature dedicated plus/minus touch-and-click zones with large hit surfaces (36x36px) alongside a direct numeric keyboard input field with tabular numerals.

### Lists & Workout Rows
- High-contrast alternating states are avoided to reduce noise. Instead, rows use clean 1px bottom-divider lines (`#1E2B45`).
- Checkboxes are large (20x20px), featuring a soft `#1E2B45` border that transitions to solid `#55D6BE` with a dark checkmark when completed, triggering subtle, non-disruptive audio or visual confirmation.
