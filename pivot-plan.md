# Budget Holidays Hub Pivot Plan v3

## Strategic Shift

The current plan is not failing because the site lacks pages. It is underperforming because too many pages are waiting for authority while only a small set are receiving meaningful Search Console tests.

The pivot is therefore:

- From broad content expansion to evidence-led optimization.
- From "publish more destinations" to "improve pages Google is already testing."
- From a separate money-content experiment to a travel-funding support cluster.
- From passive waiting to weekly Search Console decisions.

## Current Evidence

Latest 7-day Search Console snapshot, checked 2026-04-29:

| Metric | Current | Prior weekly note |
| --- | ---: | ---: |
| Clicks | 4 | 2 |
| Impressions | 660 | 781 |
| CTR | 0.61% | 0.26% |
| Avg position | 34.43 | 32.57 |

The site is getting small but useful tests. The priority is to turn those tests into stronger CTR, stronger internal signals, and clearer topical authority before adding another large content batch.

## What Changes Now

### 1. Pause Broad Publishing

Do not add another large batch of destination, money, video, tools, or programmatic pages until existing pages show stronger traction.

Allowed new content:

- One page only if Search Console exposes a clear query gap.
- One supporting page only if it strengthens a page already getting impressions.
- One tool only if it can be linked naturally from multiple pages already receiving impressions.

### 2. Optimize Pages Google Is Already Testing

Use this priority order from the 2026-04-29 tracker:

1. `/guides/greece-vs-turkey-all-inclusive/`
2. `/guides/best-travel-booking-websites-uk/`
3. `/guides/cheap-holidays-thailand-from-uk/`
4. `/guides/cheap-holidays-mauritius-from-uk/`
5. `/make-money-for-travel/`

Decision rules:

- If a page ranks top 10 with impressions but weak clicks, improve title, meta, intro verdict, and above-the-fold decision support.
- If a page ranks 30-70 with impressions, improve topical depth, exact-query coverage, supporting FAQs, and internal links.
- If a page has almost no impressions, leave it alone unless it supports a stronger page.

### 3. Reframe The Money Pivot

The money cluster should not become a separate generic side-hustle site. Its role is to answer one travel-specific question:

How can a UK traveller afford the trip they want?

Keep the `/make-money-for-travel/` cluster, but connect it directly to holiday outcomes:

- Travel pages should link to relevant funding guides only where useful.
- Money pages should link back to destination or booking pages that turn income into a realistic trip.
- Avoid generic money content unless it clearly supports travel intent.

### 4. Strengthen Commercial Intent

Commercial pages should get priority over broad informational pages because they are closer to monetization.

Priority commercial angles:

- Best travel booking websites.
- Package holiday comparisons.
- All-inclusive comparison pages.
- Destination pages with clear package or booking intent.
- Travel-funding pages that naturally introduce tools, platforms, or booking workflows.

## 30-Day Execution Plan

### Week 1

- Request indexing for the updated Greece vs Turkey page.
- Commit and retain the weekly Search Console tracker.
- Optimize `/guides/best-travel-booking-websites-uk/` for CTR and commercial intent.
- Add natural internal links from the top comparison pages to relevant booking and funding guides.

### Week 2

- Review Search Console movement for Greece vs Turkey.
- Improve `/guides/cheap-holidays-thailand-from-uk/` for query coverage around cheap Thailand holidays, Thailand holiday packages, and Thailand breaks.
- Improve `/guides/cheap-holidays-mauritius-from-uk/` for package/deal language.

### Week 3

- Audit the `/make-money-for-travel/` hub for clarity, encoding issues, and strongest links to travel outcomes.
- Pick 5 money pages that support travel intent best and improve only those.
- Add reciprocal links between those money pages and relevant travel pages.

### Week 4

- Compare fresh 7-day Search Console data against the 2026-04-29 baseline.
- Decide whether the next month should focus on CTR fixes, ranking support, or pruning/noindexing weak pages.
- Do not publish a new content batch unless Search Console data supports it.

## Measurement Rules

Track weekly:

- Clicks.
- Impressions.
- CTR.
- Average position.
- Top pages gaining impressions.
- Top pages losing impressions.
- Queries with impressions and no clicks.
- Pages indexed but not earning impressions.

Success for the pivot is not "more pages." Success is:

- More clicks from existing impressions.
- More pages moving from position 30-70 into position 10-30.
- More commercial pages receiving impressions.
- Cleaner internal links between travel, booking, and travel-funding content.

## Guardrails

- Do not remove existing guide URLs.
- Do not change canonical URLs unless fixing a confirmed canonical issue.
- Do not add large batches of content without Search Console evidence.
- Do not make the money cluster generic; every page should connect back to travel affordability.
- Keep the static GitHub Pages structure simple and fast.
- Run `python scripts/seo_audit.py` before publishing meaningful batches.

## Next Best Action

The next page to improve after the live Greece vs Turkey CTR update is:

`/guides/best-travel-booking-websites-uk/`

Reason: it has commercial intent, Search Console impressions, existing affiliate relevance, and a clear opportunity to improve the snippet, comparison table, and booking workflow.
