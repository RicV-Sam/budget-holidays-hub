# Weekly Search Console Tracking

## Week Of

- Date: 2026-05-06
- Checked by: Codex
- Source files:
  - `budgetholidayshub.com-Performance-on-Search-2026-05-06.zip`
  - `budgetholidayshub.com-Coverage-2026-05-06.zip`
- Comparison basis: Prior weekly note dated `2026-04-29`.

## Performance Snapshot

| Range | Clicks | Impressions | CTR | Avg Position |
| --- | ---: | ---: | ---: | ---: |
| Last 7 days | 0 | 267 | 0% | 31.19 |
| Prior weekly note (2026-04-29) | 4 | 660 | 0.61% | 34.43 |

## Week-over-Week Change

- Clicks: down from 4 to 0.
- Impressions: down from 660 to 267.
- CTR: down from 0.61% to 0%.
- Average position: improved from 34.43 to 31.19.
- Read: rankings improved slightly on average, but visibility and click volume fell sharply. This looks less like a snippet problem alone and more like a reduced page/query footprint.

## Indexing Snapshot

- Coverage issues:
  - `Page with redirect`: 4 pages.
  - `Crawled - currently not indexed`: 3 pages.
  - `Alternative page with proper canonical tag`: 2 pages.
  - `Excluded by 'noindex' tag`: 1 page.
  - `Discovered - currently not indexed`: 0 pages.
- Notes:
  - Indexed pages in the Coverage chart fell from `24` to `21` on `2026-04-28`.
  - Not indexed pages rose from `7` to `10` over the same period.
  - HTTP variants still appear in Performance data for some guide URLs.

## Top Pages by Impressions

| Page | Impressions | Clicks | CTR | Avg Position | Action |
| --- | ---: | ---: | ---: | ---: | --- |
| `/guides/greece-vs-turkey-all-inclusive/` | 80 | 0 | 0% | 6.55 | Still the clearest CTR win. Keep tightening title, meta, and opening summary for comparison intent. |
| `/guides/cheap-holidays-thailand-from-uk/` | 75 | 0 | 0% | 62.76 | Demand remains, but rank is far too weak for CTR work. Needs stronger query coverage and authority support. |
| `/guides/best-travel-booking-websites-uk/` | 54 | 0 | 0% | 12.26 | Commercial page is moving closer to page one. Worth improving after Greece vs Turkey. |
| `/guides/cheap-holidays-mauritius-from-uk/` | 37 | 0 | 0% | 42.03 | Keep building package/deal phrasing and supporting sections. |
| `http://budgetholidayshub.com/guides/cheap-holidays-greece-from-uk/` | 7 | 0 | 0% | 28.43 | Continue monitoring HTTP to HTTPS consolidation. |
| `/planner/` | 6 | 0 | 0% | 85 | Not a priority page right now. |
| `/guides/cheap-family-holidays-spain/` | 3 | 0 | 0% | 36.67 | Too little demand to prioritize this week. |

## Top Queries

| Query | Impressions | Clicks | CTR | Avg Position | Action |
| --- | ---: | ---: | ---: | ---: | --- |
| `cheap holidays to mauritius` | 8 | 0 | 0% | 61.75 | Mauritius page still needs stronger exact-match support. |
| `cheap deals to thailand` | 7 | 0 | 0% | 56.29 | Add "deals" language where natural on Thailand page. |
| `cheap holiday to thailand` | 7 | 0 | 0% | 61.29 | Reinforces Thailand query cluster gap. |
| `mauritius cheap holidays` | 6 | 0 | 0% | 32.33 | Add variant naturally in headings and intro copy. |
| `cheap thailand holidays` | 6 | 0 | 0% | 51.83 | Thailand page still needs stronger direct query coverage. |
| `cheap holidays to thailand` | 6 | 0 | 0% | 74.5 | Demand exists, but the page is not yet competitive. |
| `cheapest thailand holidays` | 6 | 0 | 0% | 77.33 | Useful supporting variant for Thailand content. |
| `holiday budget planner` | 6 | 0 | 0% | 85 | Low ranking, low leverage. Not a weekly focus. |
| `cheap mauritius holidays` | 5 | 0 | 0% | 33.8 | Mauritius remains a secondary optimization target. |
| `cheap greek holidays from uk` | 5 | 0 | 0% | 35.4 | Signal exists, but the HTTP Greece page needs consolidation first. |

## Low CTR Opportunities

| Page | Why it matters | Planned Change |
| --- | --- | --- |
| `/guides/greece-vs-turkey-all-inclusive/` | `80` impressions, `0` clicks, average position `6.55`. It still ranks close enough to earn clicks with better SERP and above-the-fold messaging. | Rewrite title and meta for comparison intent, sharpen the intro around value and decision-making, and add a stronger "winner for budget travellers" summary near the top. |
| `/guides/best-travel-booking-websites-uk/` | Commercial intent, `54` impressions, and average position improved to `12.26`. This page is approaching first-page contention. | Improve title/meta with a stronger 2026 comparison hook, tighten affiliate intent alignment, and make the comparison table more obviously useful from search. |
| `/guides/cheap-holidays-mauritius-from-uk/` | Still surfacing for multiple Mauritius variants, but matching is weak and no clicks landed. | Add package/deal wording, expand FAQ coverage, and improve internal links from related destination content. |

## Indexing / Crawl Issues

| URL / Area | Issue | Next Step |
| --- | --- | --- |
| Coverage trend | Indexed pages dropped from `24` to `21` on `2026-04-28`, while not indexed pages rose from `7` to `10`. | Check which URLs fell out of the indexed set and verify sitemap, canonicals, internal links, and recent page-level changes. |
| Guide URLs appearing as `http://` | Search Console still reports HTTP variants for Greece, Morocco, and Amsterdam guide URLs. | Verify redirects and canonical signals remain consistent and that internal links always point to HTTPS versions. |
| Redirected pages | 4 pages are in `Page with redirect`. | Accept if intentional; otherwise remove redirected URLs from sitemaps and internal navigation. |
| Crawled but not indexed pages | 3 pages are now in `Crawled - currently not indexed`, up from 1 last week. | Review content quality, duplication, and internal linking on those pages before adding more new content. |
| Noindex page | 1 page is excluded by `noindex`. | Confirm whether that directive is intentional. |

## Implementation Notes

- Local SEO audit passed after the 2026-05-06 changes: `139` public pages, `139` sitemap URLs, `3` intentional noindex pages.
- The `noindex` signals found locally are intentional: the legacy `/guides/spain-budget-holidays/` redirect page and two HTML templates.
- The likely `Alternative page with proper canonical tag` signal is the legacy Spain URL canonicalising to `/guides/cheap-holidays-spain-from-uk/`.
- No internal links or sitemap URLs use `http://budgetholidayshub.com`; the remaining HTTP Performance rows should be monitored as Google consolidates old variants through the existing HTTPS redirect.
- CTR work completed for `/guides/greece-vs-turkey-all-inclusive/`: title/meta, social metadata, structured data headline/description, top verdict copy and sitemap `lastmod` were updated on `2026-05-06`.

## Content Actions for Next Week

- Monitor first: `/guides/greece-vs-turkey-all-inclusive/` CTR after the 2026-05-06 update.
- Improve second: `/guides/best-travel-booking-websites-uk/`
- Improve third: `/guides/cheap-holidays-mauritius-from-uk/`
- Re-check immediately: the indexed-page count in the next Coverage export.
- Monitor: HTTP/HTTPS duplication signals in guide exports.

## Recommendation

- Next SEO page to improve: `/guides/greece-vs-turkey-all-inclusive/`
- Reason: it still has the best combination of demand and rank, with average position `6.55` and `80` impressions but `0` clicks. That keeps it as the fastest likely content win.
- Important caveat: the sharper site-wide issue this week is indexing loss. If the Coverage drop reflects important guide pages falling out of the index, fixing that may matter more than any single-page rewrite.
