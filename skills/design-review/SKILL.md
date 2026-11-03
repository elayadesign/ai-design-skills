---
name: design-review
description: "Audit and critique a built page, screen, component, or flow against the shared design system, then return a prioritized, evidence-backed fix list. Captures real screenshots first, checks typography, spacing, radius, color, contrast, accessibility, content, states, and ship readiness, and ranks each finding P0, P1, or P2 with the exact fix. Use this skill whenever the user asks to review, audit, critique, QA, inspect, sanity check, or give feedback on a landing page, marketing site, dashboard, app screen, component, or multi-step flow, or asks whether something looks like slop, or shares a URL, screenshot, or local build and asks what is wrong with it or what to fix."
---

# Design Review

Review a built surface against the same system it was supposed to follow, and hand back a fix list someone can act on today.

This skill is **review only**. It does not rebuild the surface, redesign it, or write new copy. Its whole job is to look at what exists, find what is broken, rank it by impact, and say exactly how to fix it.

## Scope

Use this skill for review, audit, critique, inspection, QA, or feedback requests on any built surface:

- A landing page, marketing site, or single page.
- A dashboard, admin panel, or app screen.
- A single component, section, or state.
- A multi-step flow: onboarding, signup, checkout, settings, a funnel.

**Not this skill:**

- **Changing an existing site.** Route to `redesign-existing-projects` ([github.com/elayadesign/redesign-skill](https://github.com/elayadesign/redesign-skill)).
- **Building a new page or section.** Route to `landing-page-design`.
- **Designing inside Figma.** Route to `figma-designer`.
- **Confirming a build matches its own source design.** That is QA of a deliverable against a spec, not a critique of design quality. Use the build workflow that produced it.

## The two rules

1. **Evidence before opinion.** Never report a finding you have not seen. Capture the surface first, then read it. A finding without a screenshot, a selector, or a file and line is not allowed.
2. **Review against the system, not your taste.** The shared system is authoritative: `landing-page-design` (and `figma-designer` for Figma files) holds every concrete value. This skill checks the built surface against those rules and does not invent new ones. If a rule is genuinely missing there, say so instead of improvising a value.

Load `landing-page-design` before reviewing. It is the source of truth for the type scale, spacing values, radius values, color rules, motion rules, and content rules this skill checks. Do not copy those values into a review; cite the rule.

## Workflow

### 1. Set up the target

Ask for, or detect:

- **What is it?** URL, local build, screenshot set, or source files.
- **Type:** landing page, dashboard, component, or flow.
- **Intent:** what is the one thing this surface is meant to make a user do, or get from it?
- **Audience:** who uses it.
- **Scope:** the whole surface, or a named section, step, or state.
- **Any known constraints:** brand font, legacy decisions, accessibility target.

If the target is a URL or a local build and a browser tool (Playwright, Chrome, or the in-app browser) is available, **capture real screenshots**. If the user gives screenshots, work from those and say so.

### 2. Capture the evidence

Collect, at minimum:

- **Full page or full screen** at desktop, plus mobile (390 wide).
- **Each step** for a flow, in order.
- **Each state** that matters: default, hover, focus, disabled, loading, empty, error.
- **Dark and light**, when the surface supports both.
- **The DOM and computed styles** for anything you are going to flag, so the fix can name a selector or a token.

For a flow, note where in the sequence each problem appears.

### 3. Inspect

Run the surface through [What to check](#what-to-check). For every candidate finding, capture the evidence that proves it before writing it down. Where source is available, get the file and line so the fix can point at it.

### 4. Rank

Assign each confirmed finding a severity:

| Severity | Meaning | Examples |
|---|---|---|
| **P0** | Blocks the primary action, breaks accessibility, or ships something false. | CTA unclickable on mobile, contrast under 4.5:1 on body text, an invented price or testimonial, a dead link in the main path, a form that cannot submit. |
| **P1** | Clearly hurts usability, trust, or the stated goal, but does not block it. | No focus ring on interactive elements, empty state is a blank panel, headings on off-scale sizes, three competing CTAs above the fold. |
| **P2** | Polish. Real but low impact. | One card with a single-side border, a radius that misses the nested formula, a transition on the default easing curve. |

Rank **P0 first, then P1, then P2**. Within a severity, order by how much it affects the primary intent of the surface.

### 5. Report

Return the review in [Output format](#output-format). Lead with the verdict and the P0s. Do not bury blockers under polish.

## What to check

Check the surface against the shared system. `landing-page-design` holds the exact values; this is the inspection list, grouped by where problems hide.

### Primary intent

- Does the surface do its one job? Is the primary action present, obvious, and reachable in the first screen?
- On mobile, is the primary action visible and tappable without horizontal scroll?
- Are there competing calls to action fighting for the same attention?

### Typography

- Does every font size land on the type scale? Flag off-scale sizes (`text-[19px]`, `1.4rem`, `22px`).
- Does every text element map to a named text style, or is it ad hoc size plus weight?
- Single approved typeface. No italics. No ultra bold.
- No orphaned words on a heading's last line. No hyphens inside copy.

### Spacing and radius

- Does every gap and padding come from the spacing scale, or is there a stray `13px`, `18px`, `37px`?
- Do nested radii follow `inner = outer − gap`, applied only when the result is greater than 2?
- Is spacing applied consistently across siblings, or do cards in a row drift?

### Color and surfaces

- Are fills and strokes bound to system tokens, or hardcoded hex?
- Both light and dark modes work, and text stays legible in each.
- No background gradients. (The hero heading text gradient is the one allowed exception.)
- Dark surfaces come from the approved set.
- One accent color, kept under 80% saturation.

### Contrast and accessibility

- Body text at least **4.5:1** against its background.
- Large text (24 and up, or 18 bold and up) and UI parts (icons, input borders, focus rings) at least **3:1**.
- On a gradient heading, contrast is checked at the **lightest** end.
- Visible focus ring on every interactive element.
- State is never shown by color alone; it is paired with an icon, label, or weight change.
- Touch targets at least **44 × 44** on mobile.
- Every meaningful image has alt text. Semantic HTML is used (`nav`, `main`, `article`, `section`). Skip to content link present.

### Borders and layout

- Borders go all the way around a card or not at all. No single-side borders.
- Content is aligned across side-by-side cards: titles, prices, lists, and buttons start on the same line.
- The layout is deliberate, not a default row of three equal cards.

### Motion

- Transitions use the system curve, not `ease`, `linear`, or `ease-in-out`.
- Only `transform` and `opacity` are animated. No layout properties.
- `prefers-reduced-motion` is respected.

### Content

- Real copy, not placeholder or lorem.
- No banned filler: "revolutionize", "supercharge", "cutting edge", "effortless", "transform your workflow", "take it to the next level", "harness the power", "world class".
- No invented facts. Prices, statistics, testimonials, guarantees, and logos trace to the user or a real source. On a real product, a made-up number is a P0, not a nitpick.
- Sentence case for headings and buttons.
- System messages are calm and specific.

### States

- Every interactive element has hover, active, focus, disabled.
- Data views have loading (a skeleton shaped like the real layout, not a spinner), empty (a composed getting-started view), and error states.
- Errors are inline and specific. No `window.alert()`.

### Ship readiness

- No dead links. A button pointing at `#` is linked or visually disabled.
- The current page is indicated in the navigation.
- Custom, branded 404.
- Legal links (privacy, terms) in the footer.
- Client-side form validation for email format and required fields.
- Branded favicon, `<title>`, meta description, `og:image`.

### Flow-specific

When reviewing a multi-step flow, also check:

- Can the user reach the goal in the fewest reasonable steps?
- Is there a way back from every step?
- Is progress visible?
- Does the user know what happens next at each step?
- Is data preserved if a step fails?

## Severity and language rules

- **Name the problem, not the person.** "The primary button has no focus ring", not "the button was done wrong".
- **One finding per row.** Do not bundle three problems into one line.
- **Point at the evidence.** Give the screenshot, the selector, or the `file:line`.
- **Give the fix, not the diagnosis.** "Add a visible focus ring: 2px outline at 3:1 or better" beats "focus states are inconsistent".
- **Cite the rule.** When a finding comes from the shared system, cite the skill and section so the fix is verifiable.

## Output format

Return exactly this, in order:

### 1. Verdict

One paragraph. What the surface is, its one job, and whether it currently does it. State the count of P0 / P1 / P2 findings.

### 2. P0 — Blockers

Findings that block the primary action, break accessibility, or ship something false. If there are none, say so in one line.

### 3. P1 — High impact

Findings that clearly hurt usability, trust, or the goal.

### 4. P2 — Polish

Lower-impact findings.

Each finding is one row:

| # | Finding | Evidence | Fix | Rule |
|---|---|---|---|---|
| 1 | Primary CTA sits below the fold on mobile | `screens/mobile-390.png`, `#hero-cta` at y=742 | Move the CTA into the first screen; keep hero copy to two lines | `landing-page-design` A2 |

For a flow, include the step in the Evidence column.

### 5. What passed

A short list of the checks the surface genuinely passes. This keeps the review fair and shows the work, so the reader trusts the P0s.

### 6. Recommended order

The P0s and P1s in the order to fix them, with a one-line reason each. Group findings that share a fix.

## Make it yours

The concrete design values this skill checks against live in one place: **`landing-page-design`**. This file deliberately does not restate them, so there is a single source of truth. If you fork and change the type scale, spacing, radius, color, or motion rules there, this skill's checks follow automatically, because they cite those rules rather than copying them.

If you want to change how reviews are ranked or reported, edit the severity table and the [Output format](#output-format) section here, and leave the values alone.
