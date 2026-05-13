# Weekly Search Console Tracking

## Week Of

- Date: 2026-05-13
- Checked by: Codex
- Source files:
  - `budgetholidayshub.com-Performance-on-Search-2026-05-13.zip`
  - `budgetholidayshub.com-Coverage-2026-05-13.zip`
- Comparison basis: Prior weekly note dated `2026-05-06`.

## Performance Snapshot

| Range | Clicks | Impressions | CTR | Avg Position |
| --- | ---: | ---: | ---: | ---: |
| Last 7 days | 1 | 42 | 2.38% | 14.71 |
| Prior weekly note (2026-05-06) | 0 | 267 | 0% | 31.17 |

## Week-over-Week Change

- Clicks: up from 0 to 1.
- Impressions: down from 267 to 42.
- CTR: up from 0% to 2.38%.
- Average position: improved from 31.17 to 14.71.
- Read: search visibility is much lower in total volume, but the traffic that remains is ranking materially better. This is a smaller footprint with stronger average placement, not a broad recovery yet.

## Indexing Snapshot

- Coverage issues:
  - `Page with redirect`: 7 pages.
  - `Crawled - currently not indexed`: 3 pages.
  - `Discovered - currently not indexed`: 118 pages.
  - `Alternative page with proper canonical tag`: 2 pages.
  - `Excluded by 'noindex' tag`: 1 page.
- Notes:
  - Indexed pages stayed flat at `21`.
  - Not indexed pages jumped from `10` to `131`.
  - The new spike is almost entirely the `Discovered - currently not indexed` bucket.
  - Redirected pages rose from `4` to `7`.

## Top Pages by Impressions

| Page | Impressions | Clicks | CTR | Avg Position | Action |
| --- | ---: | ---: | ---: | ---: | --- |
| `/guides/greece-vs-turkey-all-inclusive/` | 30 | 1 | 3.33% | 10.4 | Early sign that the 2026-05-06 rewrite helped. Keep monitoring before changing it again. |
| `/guides/best-travel-booking-websites-uk/` | 6 | 0 | 0% | 6.17 | Strongest next CTR candidate. It is already ranking well enough to justify title, meta, and intro improvements. |
| `/` | 5 | 0 | 0% | 2 | Homepage is visible, but it is not the best focused SEO edit target for this cycle. |
| `/planner/` | 4 | 0 | 0% | 25.5 | Too far from competitive positions to prioritize this week. |
| `/make-money-for-travel/best-side-hustles-uk-2026-ranked.html` | 2 | 0 | 0% | 7.5 | Worth monitoring, but the sample is too small to outrank guide-page opportunities. |
| `/make-money-for-travel/side-hustles-vs-passive-income-for-travel.html` | 2 | 0 | 0% | 17 | Informational support page only for now. |
| `/guides/cheap-holidays-mauritius-from-uk/` | 2 | 0 | 0% | 45 | Still not ranking strongly enough for CTR-first work. |
| `/guides/cheap-holidays-greece-from-uk/` | 1 | 0 | 0% | 6 | Good position, but the sample is too thin this week. |
| `http://budgetholidayshub.com/guides/cheap-holidays-greece-all-inclusive-from-uk/` | 1 | 0 | 0% | 8 | Continue watching HTTP consolidation signals. |
| `http://budgetholidayshub.com/guides/cheap-holidays-morocco-from-uk/` | 1 | 0 | 0% | 9 | Another HTTP variant showing up in Performance. Monitor redirects and canonicals. |

## Top Queries

| Query | Impressions | Clicks | CTR | Avg Position | Action |
| --- | ---: | ---: | ---: | ---: | --- |
| `short4vonte` | 1 | 0 | 0% | 30 | Ignore. This does not look like a meaningful target query. |
| `thailand holidays cheap deals from uk` | 1 | 0 | 0% | 68 | Confirms the Thailand page still lacks competitive query coverage. |
| `mauritius holidays 2026` | 1 | 0 | 0% | 83 | Mauritius remains a secondary content opportunity, not a quick win. |
| `holiday budget planner` | 1 | 0 | 0% | 97 | Planner visibility is still too weak to focus on next. |

## Low CTR Opportunities

| Page | Why it matters | Planned Change |
| --- | --- | --- |
| `/guides/best-travel-booking-websites-uk/` | `6` impressions, `0` clicks, and average position `6.17` means it is already close enough to page-one click territory. | Rework title and meta around a sharper 2026 comparison intent, tighten the opening summary, and make the ranking criteria obvious above the fold. |
| `/guides/greece-vs-turkey-all-inclusive/` | It earned its first click after last week's update, but `30` impressions at position `10.4` still leave room to improve. | Monitor one more export before making another major rewrite unless the page loses rank again. |
| `/make-money-for-travel/best-side-hustles-uk-2026-ranked.html` | Position `7.5` is promising, but the sample is still tiny. | Keep an eye on it; do not let it displace the core travel guide priorities yet. |

## Indexing / Crawl Issues

| URL / Area | Issue | Next Step |
| --- | --- | --- |
| Coverage trend | `Not indexed` rose from `10` to `131`, while indexed pages stayed flat at `21`. | Treat this as the main technical issue from this export. Review whether recently added or lightly linked pages are being discovered but not crawled into the index. |
| `Discovered - currently not indexed` | New bucket at `118` pages. This dominates the week's Coverage change. | Check sitemap freshness, internal link depth, and whether low-priority pages are being overproduced relative to crawl demand. |
| Redirected pages | `Page with redirect` increased from `4` to `7`. | Confirm those URLs are intentionally redirected and that redirected URLs are not present in the sitemap. |
| Guide URLs appearing as `http://` | Search Console still reports HTTP variants for Greece and Morocco pages. | Keep monitoring. Local canonicals and internal links are HTTPS-only, so this may still be Google consolidating older variants. |
| Local audit vs Search Console | Local audit passed with `139` public pages, `139` sitemap URLs, and `3` intentional noindex pages. | This suggests the spike is not a simple sitemap or sitewide noindex regression. Prioritize crawl/indexation diagnosis over template-level SEO tweaks. |

## Implementation Notes

- New exports were imported to `data/search-console/2026-05-13/`.
- Local audit passed on `2026-05-13`: `139` public pages, `139` sitemap URLs, `3` intentional noindex pages.
- The prior `/guides/greece-vs-turkey-all-inclusive/` update appears to have produced an early positive signal: first click recorded, with CTR rising from `0%` to `3.33%` on that page.
- Performance export scope matches last week: `Web`, `Last 7 days`.
- The new Search Console dataset is much smaller than last week, so page-level recommendations should be treated as directional rather than conclusive.

## Content Actions for Next Week

- Monitor first: `/guides/greece-vs-turkey-all-inclusive/` for a second week before reworking it again.
- Improve second: `/guides/best-travel-booking-websites-uk/`
- Improve third: `/guides/cheap-holidays-thailand-from-uk/` if Thailand query impressions return in the next export.
- Re-check immediately: whether the `Discovered - currently not indexed` count persists in the next Coverage export.
- Monitor: HTTP/HTTPS duplication signals in guide exports.

## Recommendation

- Next SEO page to improve: `/guides/best-travel-booking-websites-uk/`
- Reason: it now looks like the clearest content candidate because it is already sitting at average position `6.17` with `0` clicks. Greece vs Turkey has at least shown an early response to last week's work, so the booking-sites page is the better next optimization bet.
- Important caveat: the bigger issue in this export is technical, not editorial. If the `Discovered - currently not indexed` spike is real and persistent, fixing crawl/indexation will matter more than any single-page content improvement.
