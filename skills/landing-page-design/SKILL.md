---
name: landing-page-design
description: "Complete system for building, editing, styling, or reviewing landing pages and marketing UI: intake, page structure, conversion copy, SEO, adaptable visual rules, claim verification, visual-source verification, accessibility, responsive QA, and release evidence. Use whenever work touches a landing page, marketing site, campaign page, web UI section, conversion component, or prototype, even when the user does not explicitly ask for design, truth checking, mobile QA, or a design system. Always consult it before choosing sections, claims, proof, CTAs, media, fonts, spacing, colors, motion, or declaring a page ready to ship."
---

# Landing Page Design

A landing page is not a homepage. A homepage serves multiple intents. A landing page wins one intent:

**one offer → one audience → one primary action.**

This skill has three parts. **Part A** decides what the page says and how it is structured. **Part B** supplies an adaptable visual system. **Part C** verifies claims, media, accessibility, responsive behavior, and release readiness. Work through A before B, then complete C before calling the page ready.

## Scope

Apply to landing pages, marketing sites, campaign components, prototypes, and design reviews. The user's explicit direction wins. An existing brand system, product truth source, or proven control page also wins over this file's default visual profile. Never overwrite established brand or product truth merely to match a generic preference below.

**Companion skill.** For upgrading an *existing* site rather than building a new one, use `redesign-existing-projects` ([github.com/elayadesign/redesign-skill](https://github.com/elayadesign/redesign-skill)). It diagnoses generic patterns and defers to this file for every concrete value.

---

# PART A — Strategy and structure

## A1. Intake

Gather these before designing or writing. Ask only for what is missing, and ask in one batch rather than one question at a time.

**Purpose**
- What is the ONE primary action? (trial, demo, buy, waitlist, download)
- What is the offer, exactly what do they get?
- What counts as a conversion? (click, signup, purchase)

**Audience and context**
- Who is the ICP?
- What problem are they trying to solve?
- Top three objections, meaning why they do not convert today
- Traffic source: ads, search, social, email
- What do visitors already know when they land?

**Proof and assets**
- Proof points: logos, testimonials, numbers, case studies
- Screenshots, demo video, product GIFs
- Guarantees, refund terms, cancellation terms
- Source owner for every factual or commercial claim
- Source owner for every product image, logo, testimonial, and proof asset
- Verification date or freshness requirement when a claim can change

**Constraints**
- Brand voice: casual or professional
- Design direction: minimal editorial, playful 3D, glass UI
- Mobile priority?

If the user cannot answer, make and state reasonable assumptions about layout, hierarchy, and draft positioning. Do not invent prices, guarantees, deadlines, statistics, testimonials, customer identities, product details, or other factual claims. Mark those as explicit holds and continue with neutral copy or visibly labeled placeholders.

## A2. Page structure

**Above the fold (required)**
1. Headline, outcome plus audience
2. Subheadline, clarifies how and adds specificity
3. Primary CTA, clear verb plus what they get
4. One proof signal, logo strip, stat, or short testimonial
5. Hero visual, product screenshot or video, or a strong illustration

**Mid page (the argument)**
6. Problem to solution, one section
7. Benefits, three to five, outcome driven
8. How it works, three steps
9. Social proof, testimonials or a case study

**Bottom (objection handling)**
10. FAQ, six to twelve questions
11. Risk reversal, trial, cancel anytime, guarantee
12. Final CTA, identical to the top

Use the tagline reveal pattern from B11 only when it strengthens the argument and fits the brand, typically after the hero or benefits.

## A3. Layout selection

Pick one and say why.

| Type | Use when |
|---|---|
| **A. Classic hero plus sections** | The product is understandable from a hero screenshot. Most common. |
| **B. Long form story** | You need to educate and overcome skepticism. |
| **C. Minimal conversion page** | High intent traffic (email to known users), or a short offer like a download or waitlist. |
| **D. Comparison page** | Search intent includes alternatives ("X vs Y", "best for"). Usually paired with SEO pages. |

## A4. Conversion rules

**Match message to source.** If traffic comes from ads, mirror the ad headline in the hero and keep the same promise and visual tone.

**Make the next step obvious.** One primary CTA. Never place competing CTAs above the fold.

**Write benefit first.** Features are what it does. Benefits are what that means for them.

**Be specific.**
- ❌ "Save time and streamline"
- ✅ "Cut your weekly reporting from 4 hours to 15 minutes"

Specificity is not permission to fabricate. Every number and measurable outcome must be sourced, clearly labeled as an estimate, or replaced with non-numeric draft language.

**Reduce risk.** Use a verified risk reversal when one exists: free trial, free plan, no credit card, cancel anytime, or money back guarantee. Never invent one to complete the page structure.

**Treat objections as a section, not a footnote.** Move the FAQ earlier for high friction offers. Put proof directly beside the claim it supports.

## A5. Copywriting

**Headline formulas**
- "{Outcome} without {pain}"
- "The {category} for {audience}"
- "Ship {result} in {time}"

**Subheadline.** One or two sentences. Clarify what it is and who it is for.

**CTA.** Verb plus what they get. Never "Learn more" or "Submit". Use "Start free trial", "Book a demo", "Get the checklist".

**Benefit bullets.** Bold benefit, then the proof or detail. Example: **Faster iteration** — generate three layout variants in one click.

Note: the copy and readability rules in B1 still apply.

## A6. Build order

Work section by section, in this order:

1. Hero
2. Benefits
3. How it works
4. Proof
5. FAQ
6. Final CTA

Never rebuild the whole page on each iteration. Section by section keeps control and keeps diffs reviewable.

## A7. SEO and AEO

**Do not index** ad only campaign pages or highly time bound offers. Use `noindex` or keep them behind a non indexed path.

**Do index** evergreen offers and pages where search intent matches the promise. Add a clear title and meta description, internal links from the homepage and feature pages, and the FAQ in plain question and answer form for AEO. Add FAQ schema if appropriate.

## A8. Pitfalls

- Too many CTAs above the fold
- Vague value prop: "streamline", "optimize"
- A large feature list with no outcomes
- Proof buried at the bottom
- Mobile layout that breaks readability
- No clear next step
- Unsourced numbers, testimonials, guarantees, comparisons, or urgency
- Product or proof visuals whose source and accuracy are unknown

---

# PART B — Visual system

This is the default visual profile, not a universal brand. Use an existing project design system first. When none exists, resolve visual values through these rules instead of inventing them ad hoc. Preserve a proven control page's visual language unless the requested work is an intentional redesign.

## B1. Typography

### Fonts

**Default choices:** Geist, Manrope, Geist Mono, Poppins.

Prefer a project's existing licensed typeface. In a new unbranded build, avoid defaulting to Inter, Roboto, Arial, Open Sans, or Helvetica when a more distinctive approved choice is available.

Avoid decorative italics that reduce readability. Use italics when the brand system or content semantics genuinely call for them.

Default to one typeface per site. Pair two only when the brand system or design direction gives each a clear role. Geist Mono is allowed alongside a primary font for code, data, or numeric UI where monospace is functional.

**Never use ultra bold weights** (900 / black). Cap at semibold or bold.

### Copy rules

Use correct punctuation. Do not remove meaningful hyphens or dashes merely to satisfy a visual preference.

**No orphaned words.** A single word must never sit alone on the last line. Apply `text-wrap: balance` for headings and `text-wrap: pretty` for body copy.

### Type scale

Use the project's type tokens when they exist. Otherwise resolve font sizes to Tailwind's default type scale and avoid one-off arbitrary values such as `text-[19px]`, `font-size: 22px`, or `1.4rem`.

If an existing size does not land exactly on a step, snap it to the **closest step below**, taking both the size and its paired line height.

| Class | Size | Line height |
|---|---|---|
| `text-xs` | 12px (0.75rem) | 16px |
| `text-sm` | 14px (0.875rem) | 20px |
| `text-base` | 16px (1rem) | 24px |
| `text-lg` | 18px (1.125rem) | 28px |
| `text-xl` | 20px (1.25rem) | 28px |
| `text-2xl` | 24px (1.5rem) | 32px |
| `text-3xl` | 30px (1.875rem) | 36px |
| `text-4xl` | 36px (2.25rem) | 40px |
| `text-5xl` | 48px (3rem) | 1 |
| `text-6xl` | 60px (3.75rem) | 1 |
| `text-7xl` | 72px (4.5rem) | 1 |
| `text-8xl` | 96px (6rem) | 1 |
| `text-9xl` | 128px (8rem) | 1 |

Do not combine scale snapping with independently set custom line heights elsewhere in an audit. Tracking and line height may only be adjusted **within** the value the matched step already provides, so the two rules never fight each other.

### Button type

- Main buttons: `text-base` (16px), semibold.
- Smaller header buttons: `text-sm` (14px), semibold.

## B2. Spacing

Use the project's spacing tokens when they exist. Otherwise use only these fallback values.

| Token | Value |
|---|---|
| Spacing-0 | 0 |
| Spacing-25 | 2px |
| Spacing-50 | 4px |
| Spacing-75 | 8px |
| Spacing-100 | 12px |
| Spacing-200 | 16px |
| Spacing-300 | 24px |
| Spacing-400 | 32px |
| Spacing-500 | 40px |
| Spacing-600 | 48px |
| Spacing-700 | 64px |
| Spacing-800 | 80px |
| Spacing-900 | 96px |

**Main buttons:** 8px vertical padding, 12px horizontal padding.

## B3. Corner radius

Use the project's radius tokens when they exist. Otherwise use Tailwind's radius values.

**Nested radius formula.** When a shape sits inside another shape and the gap between them is **less than 32px**:

```
inner radius = outer radius − gap
```

Apply this only when the result is **greater than 2**. Below that, leave the inner shape square or unchanged.

Example: an outer card at `rounded-2xl` (16px) with 8px of internal padding gives an inner element an 8px radius (`rounded-lg`).

## B4. Borders and backgrounds

- In the default profile, borders go all the way around a card or are omitted. A brand system may define intentional edge accents.
- In the default profile, backgrounds are flat. Use gradients only when the chosen design direction explicitly calls for them and contrast remains accessible.

### Dark mode background colors

Default dark-mode surfaces:

`#000000` · `#181818` · `#1F1F1F` · `#272727` · `#313131` · `#131209`

## B5. Hero section

### Heading color

- **Default dark theme:** left to right gradient on the heading text, `#FFFFFF` → `#9B9B9B`.
- **Default light theme:** left to right gradient on the heading text, `#000000` → `#666666`.

This is the default profile's only gradient. Skip it when it conflicts with the brand or reduces readability.

### Layout

- Heading and subheading both get a **max width of 680px**.
- Read the heading copy and insert line breaks at **meaningful** points.
- Never break a line in a way that cuts a phrase awkwardly or makes the sentence harder to read. Break where the thought breaks.

## B6. Icons

**Default choices:** Phosphor, Solar, or Iconamoon.

Use the project's existing icon family when one exists. Do not mix unrelated icon families on the same page.

## B7. Motion choreography (fluid dynamics)

Motion is optional and must communicate hierarchy, state, or continuity. Do not animate merely to make the page feel generated. When motion is used, prefer custom cubic beziers that suggest real-world mass.

```
transition-all duration-700 ease-[cubic-bezier(0.32,0.72,0,1)]
```

Every animation must respect `prefers-reduced-motion: reduce`. Essential content and controls must remain visible and usable when animation JavaScript fails or motion is disabled.

### Fluid island nav (when selected)

**Closed state.** The navbar is a floating glass pill detached from the top: `mt-6`, `mx-auto`, `w-max`, `rounded-full`.

**Hamburger morph.** On click, the hamburger lines fluidly rotate and translate into a perfect X using `rotate-45` and `-rotate-45` with absolute positioning. They must never simply disappear.

**Modal expansion.** The menu opens as a screen filling overlay with a heavy glass effect: `backdrop-blur-3xl bg-black/80` or `bg-white/80`.

**Staggered mask reveal.** Nav links inside the expanded state fade in and slide up from an invisible box, `translate-y-12 opacity-0` resolving to `translate-y-0 opacity-100`, staggered per item with `delay-100`, `delay-150`, `delay-200`, and so on.

### Scroll interpolation (optional)

When scroll motion supports the design direction, elements may enter with a gentle fade up:

```
translate-y-16 blur-md opacity-0  →  translate-y-0 blur-0 opacity-100
```

over 800ms or longer.

For JavaScript-driven reveals use `IntersectionObserver` or Framer Motion's `whileInView`. Avoid unthrottled scroll listeners. Render content visible by default, then apply motion as progressive enhancement so a script failure never leaves the page blank.

---

## B8. Content realism

Never ship filler. These are the tells that a page was generated rather than made.

- **No Lorem Ipsum.** Write real draft copy.
- **No invented customer identities or testimonials.** Use sourced identities, approved anonymization, or clearly labeled placeholders.
- **No placeholder brands presented as real.** In prototypes, label fictional names and data clearly.
- **No fake precision.** Use sourced numbers, a clearly labeled estimate, or an explicit placeholder token such as `{{VERIFIED_STAT}}`.
- **No AI cliches.** Never "Elevate", "Seamless", "Unleash", "Next Gen", "Game changer", "Delve", "Tapestry", or "In the world of".
- **Sentence case headers**, not Title Case On Everything.
- **Active voice.** "We could not save your changes", not "Mistakes were made".
- **No exclamation marks in success messages**, and no "Oops!" in errors. Be direct: "Connection failed. Please try again."
- **Unique avatars** per person, and varied blog post dates.

## B9. States

Every interactive element ships with every state it can actually enter:

- **Hover** — background shift, slight scale, or translate
- **Active** — `scale(0.98)` or `translateY(1px)` for physical feedback
- **Focus** — a visible focus ring. Accessibility requirement, not optional.
- **Loading** — skeleton loaders shaped like the real layout, not circular spinners
- **Empty** — a composed "getting started" view, never a blank panel
- **Error** — inline and specific. Never `window.alert()`.

No dead links. A button pointing at `#` is either linked or visually disabled. The current page must be indicated in the navigation.

## B10. Ship requirements

Things that get forgotten and make a page feel unfinished. Apply site-level items when the page or project owns them:

- Privacy policy and terms links in the footer
- A custom, branded 404
- Client side form validation for email format and required fields
- A skip to content link for keyboard users
- Cookie consent where the jurisdiction requires it
- A branded favicon
- `<title>`, meta description, `og:image`, and social sharing tags
- Alt text on every meaningful image
- Semantic HTML: `<nav>`, `<main>`, `<article>`, `<aside>`, `<section>`
- A way back from every page

## B11. Tagline reveal section (optional signature)

Use this pattern when a large type moment reinforces the core benefit and fits the brand. It sits further down the page as its own moment, not stacked directly under the hero.

**Copy**
- Minimum two lines of text.
- A benefit statement or tagline, written in the voice of A5, not a generic section heading.

**Typography**
- Size `text-4xl` to `text-6xl` depending on line count, following the B1 type scale.
- Max width capped like the hero, so lines break at meaningful points per B5.

**Animation**
- Text starts in a subtle, muted tone, roughly 25 to 35% opacity of the theme's base text color.
- As the section scrolls into view, each word transitions individually from that muted tone to the full text color, in reading order.
- Words activate one at a time as they cross a trigger line, not the entire block flipping at once. The transition uses the custom easing curve from B7, never a linear fade.
- Implement with `IntersectionObserver` per word, or a single scroll listener throttled through `requestAnimationFrame`. Never an unthrottled `window.addEventListener('scroll')`, per B7.
- Under `prefers-reduced-motion: reduce`, show the final fully legible text without word-by-word animation.

---

# PART C — Truth and release gates

These gates are part of this skill. Run them automatically; do not wait for the user to remember a separate audit.

Apply them proportionally. During ideation, preserve unknown facts and media as visible holds. Run the full rendered and performance evidence pass before a production-ready claim, launch handoff, or final review.

## C1. Claim truth gate

Build a claim inventory before final copy and recheck it before shipping. Include:

- offer, price, discount, trial, guarantee, refund, cancellation, and shipping terms
- deadlines, countdowns, availability, inventory, or urgency
- product capabilities, specifications, integrations, comparisons, and performance claims
- statistics, customer counts, logos, awards, case studies, testimonials, and quoted outcomes

For each claim record:

- exact claim and page location
- source owner and source link or file
- status: `verified`, `estimate`, `placeholder`, or `hold`
- verification date when the fact can change

Rules:

- A competitor, old page, mockup, or generated draft is a pattern source, not factual truth.
- Proof must support the exact nearby claim, not merely the general company.
- Estimates must be labeled as estimates.
- If a material claim lacks a source, use neutral draft language or leave an explicit hold.
- Any material claim still marked `placeholder` or `hold` makes this gate `BLOCKED` and blocks shipping.
- Contradictory CTA destinations, prices, terms, or guarantees block shipping.
- A countdown without a verified basis, end time, and timezone blocks shipping.

Result:

- `PASS` — every material claim is verified or is an explicitly labeled estimate that is safe for the intended use.
- `PASS WITH WARNINGS` — only documented non-material warnings remain.
- `BLOCKED` — a material `placeholder` or `hold`, a conflicting term, or an unverified countdown remains.

## C2. Visual truth gate

Inventory every meaningful image, video, logo, avatar, screenshot, badge, and proof graphic. For each asset record:

- page slot and file path or URL
- source owner
- what the asset visibly depicts
- any product, identity, result, certification, or offer claim carried by the pixels
- approval status and review note

Rules:

- Real product references own product details. Do not let generated imagery invent labels, controls, packaging, screens, ports, or included items.
- Logos, testimonials, awards, press marks, and customer identities must map to real approved sources.
- Legacy assets are not current truth by default.
- Generated or materially edited product and proof visuals require visual review.
- When several assets changed or product fidelity is important, create a contact sheet for one-glance review.
- Broken, missing, or unapproved claim-bearing media blocks shipping. Decorative draft media may ship only when clearly approved for that use.

Result: `PASS`, `PASS WITH WARNINGS`, or `BLOCKED`.

## C3. Responsive ship check

For an existing page, capture a baseline before editing. Verify the rendered result, not source code alone.

Test at minimum:

- `320px`, `360px`, `375px`, `390px`, and `430px`
- one tablet width
- one desktop width

Check:

- no horizontal overflow
- CTA text bounds remain inside the button; `white-space: nowrap` alone is not proof
- readable first viewport, clear primary action, usable touch targets, and no obscured content
- keyboard navigation, visible focus, semantic landmarks, labels, and useful alt text
- rendered color contrast meets WCAG AA for normal text, large text, and meaningful UI components, including text over images or gradients
- sticky or fixed UI does not cover content or controls
- forms show relevant validation, loading, success, and error states
- motion respects reduced-motion settings and content remains visible without animation
- meaningful images have dimensions; below-fold media is lazy-loaded where appropriate
- no broken links, missing assets, or buyer-facing console errors

Measure performance with Lighthouse or the closest available equivalent. Record the tested URL or build, LCP, CLS, and the largest remaining bottleneck. For edits, report before and after. A static checklist is not a substitute for screenshots or browser verification.

Result: `PASS`, `PASS WITH WARNINGS`, or `BLOCKED`.

## C4. Release receipt

Do not say a page is ready without this evidence:

```text
Readiness: READY | READY WITH CAVEATS | BLOCKED
Target: [page, URL, build, or commit]
Claim truth: [result + source summary]
Visual truth: [result + source/contact-sheet summary]
Responsive QA: [widths, browsers, screenshots, result]
Accessibility: [keyboard, focus, semantics, color contrast, reduced motion]
Performance: [tested target, LCP, CLS, largest bottleneck]
Remaining holds: [none for READY; any material hold forces BLOCKED]
```

Map gate results to readiness:

- `READY` requires every applicable gate to be `PASS`.
- `READY WITH CAVEATS` allows only documented non-material warnings.
- `BLOCKED` is required when any gate is `BLOCKED` or any material `placeholder` or `hold` remains.

---

# Output format

When generating a landing page from scratch, return these in order before writing code:

1. **Page outline** — sections and their order
2. **Hero copy** — headline, subheadline, CTA, proof line
3. **Benefits** — three to five outcome driven bullets
4. **How it works** — three steps
5. **FAQ** — six to twelve questions and answers
6. **SEO / AEO** — index or noindex recommendation, plus title and meta if indexed
7. **Layout recommendation** — A, B, C, or D, and why
8. **Truth lock** — verified claims, estimates, placeholders, and holds
9. **Media plan** — source owner and approval status for each meaningful asset

Then build section by section per A6. After implementation, return the Part C release receipt.

---

# Quick checklist

**Strategy**
- [ ] One offer, one audience, one primary action
- [ ] No competing CTAs above the fold
- [ ] Specific numbers instead of vague verbs
- [ ] Every factual number and commercial term has a source; any remaining hold is visible and blocks shipping
- [ ] Risk reversal is verified, not invented
- [ ] Proof sits next to the claim it supports
- [ ] Layout type chosen deliberately

**Visual**
- [ ] Existing brand/design tokens were used when available
- [ ] Typography choices are readable and intentional
- [ ] No orphaned words in important headings or CTAs
- [ ] Font and spacing values resolve through project tokens or the fallback scale
- [ ] Nested radii follow the formula
- [ ] Borders and gradients match the chosen design direction
- [ ] Hero heading and subheading capped at 680px with meaningful line breaks
- [ ] One coherent icon family
- [ ] Motion has a purpose, uses efficient primitives, and respects reduced motion
- [ ] Essential content remains visible if animation does not run

**Truth and media**
- [ ] Claim inventory is `PASS`, or `PASS WITH WARNINGS` with only documented non-material warnings
- [ ] No unsourced price, guarantee, deadline, statistic, testimonial, or comparison
- [ ] Visual inventory names the source and approval state of every meaningful asset
- [ ] Generated or edited product/proof visuals received visual review
- [ ] Contact sheet created when several assets changed or fidelity risk is high

**Content and ship**
- [ ] No Lorem Ipsum, AI cliches, invented identities, or fake precision
- [ ] Relevant hover, active, focus, loading, empty, and error states are present
- [ ] No dead links, current nav item indicated
- [ ] 404, legal links, form validation, favicon, meta tags, alt text
- [ ] Rendered screenshots cover 320, 360, 375, 390, 430, tablet, and desktop
- [ ] No horizontal overflow; CTA text stays inside button bounds
- [ ] Keyboard, focus, semantics, touch targets, and reduced motion verified
- [ ] Rendered color contrast meets WCAG AA, including text over images or gradients
- [ ] Performance measured on the exact target being reported
- [ ] Release receipt says `READY`, `READY WITH CAVEATS`, or `BLOCKED`
