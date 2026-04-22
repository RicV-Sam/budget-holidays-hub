# SEO + UI Growth Roadmap

This file is the working checklist for growing Budget Holidays Hub without creating thin, orphaned, or hard-to-monetise pages.

## Current Priorities

1. Strengthen topic clusters before adding more page volume.
2. Keep every new page connected to the hub, at least two related pages, one video page, and one travel guide.
3. Use structured data only when it matches visible page content.
4. Preserve fast, readable pages before adding heavier ad or affiliate units.

## Publishing Rules

- Every public page must have one H1, a unique title, a unique meta description, a canonical URL, and a clear next step.
- Every guide should answer the query quickly, then support the answer with realistic costs, timing, and booking decisions.
- Every money page should connect earnings to a travel outcome such as flights, hotel nights, or a full short-haul break.
- Avoid arbitrary word-count expansion. Add content only when it improves the reader's decision.
- Do not publish a page unless it has at least two internal links pointing to it from relevant existing pages.

## Internal Linking Rules

- Link from hubs to every important supporting page.
- Link from supporting pages back to the hub and to one next-step guide.
- Use natural anchors that describe the destination page.
- Prefer contextual paragraph links over standalone link blocks when adding links to existing guides.
- Recheck orphan pages after every content batch.

## Video Rules

- Use video pages when the video is the primary purpose of the page.
- Add `VideoObject` schema only to video-first pages.
- Validate every YouTube ID with oEmbed before publishing or reusing the embed.
- Keep videos visible and easy to access; do not hide them behind tabs.

## Schema Rules

- Add `Article` schema to article-style money pages and travel guides.
- Add `BreadcrumbList` schema when the page has a visible breadcrumb.
- Add `FAQPage` schema only when the FAQ is visible on the page.
- Do not duplicate or reuse schema blindly across pages.

## Monetization Readiness

- Keep affiliate and ad placements secondary until traffic grows.
- Reserve stable ad slots so future AdSense units do not cause layout shift.
- Keep affiliate CTAs relevant to the page intent and clearly separated from editorial advice.
- Maintain disclosure links in the global footer and near commercial CTAs when needed.

## Post-Publish QA

- Confirm the page appears in `sitemap.xml` or is intentionally `noindex`.
- Confirm all internal links resolve to real files.
- Confirm images include alt text.
- Confirm schema parses as valid JSON-LD.
- Confirm mobile and desktop layouts remain readable.
- Confirm at least two relevant internal pages link to every new page.
