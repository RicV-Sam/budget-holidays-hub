# Budget Holidays Hub organic-search growth audit

Audit date: 28 August 2026  
Primary growth cluster: inbound UK travel under `/visit-uk/`  
Secondary cluster: holidays from the UK under `/guides/`

## Executive summary: five biggest click opportunities

1. **Obtain a current 90-day Search Console export before changing ranking pages at scale.** The repository contains only two seven-day exports covering 27 April–10 May 2026. They predate the inbound pivot and most August refreshes. A current page/query export is the only reliable way to identify high-impression, low-CTR pages and positions 4–20 now. Expected click impact 5/5; confidence 5/5; effort 1/5; likely impact within days of receiving the data.
2. **Make sitemap freshness verifiable.** Seventy-nine article URLs had sitemap `lastmod` dates that disagreed with Article `dateModified`; some sitemap dates were later than the visible review date because the generator used rollout buckets. Google says `lastmod` should represent a significant update and is useful when consistently accurate. Replace hard-coded article dates with each page's own Article date. Impact 4/5; confidence 5/5; effort 2/5; likely crawl-signal improvement in days to weeks. [Google sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
3. **Send more internal authority to proven inbound pages, not only the hub.** Every indexable page links sitewide to `/visit-uk/`, but the personally visited Land's End guide had only one unique linking page. Add contextual links from the homepage and relevant road-trip guides. Impact 4/5; confidence 5/5; effort 1/5; likely discovery/ranking impact in one to six weeks.
4. **Refresh legacy pages in current Search Console opportunity order.** The May evidence identified `/guides/greece-vs-turkey-all-inclusive/`, `/guides/best-travel-booking-websites-uk/`, and `/guides/cheap-holidays-mauritius-from-uk/`. All three have since received substantive August updates, so they should be measured before another rewrite. The next unrefreshed candidates are Spain family, Prague and Thailand, but only after a current page/query matrix confirms demand. Impact 5/5; confidence 3/5 until current data; effort 3–5/5; likely impact in two to eight weeks.
5. **Turn trust and measurement into a competitive advantage.** The inbound pages use honest evidence labels, answer early, cite official sources and show limitations. The remaining gaps are a named creator/byline, dated first-hand methodology on pages that say “personally used,” and consistent privacy-safe analytics. All six `/visit-uk/` pages omit the analytics tag used by most of the site; adding it without a consent design would create privacy risk, so consent and measurement must be solved together. Impact 3/5; confidence 4/5; effort 3/5; likely impact in four to twelve weeks.

There is no verified P0 crawling or indexing failure in the current repository or sampled live site. The fastest safe repository work is therefore signal accuracy, contextual internal links and removal of stale future-state copy—not speculative title churn.

Follow-on work completed after the initial audit: the main SEO audit now fails if an Article `dateModified` and sitemap `lastmod` diverge, and the unfinished “social media channels coming soon” section was removed from Contact. Three legacy pages still expose only a month-level visible update date, so missing schema dates were not filled with invented day-level precision.

## Evidence and baseline

### Repository and live technical baseline

| Evidence | Result | Interpretation |
| --- | ---: | --- |
| HTML pages checked by existing audit | 164 | Complete repository crawl, excluding build/test artifacts as configured |
| Indexable public pages | 108 | 92 `/guides/`, 6 `/visit-uk/`, homepage and 9 utility/trust pages |
| Intentionally noindexed pages | 56 | Income, recipe and associated video areas remain public but out of the travel index |
| Sitemap URLs | 108 | Exact set match with indexable pages |
| Live sitemap URLs returning final 200 | 108/108 | No live sitemap redirect or status failure |
| Broken internal links | 0 | Existing audit passed |
| Missing/duplicate required metadata | 0 | Existing crawl and consistency audits passed |
| Invalid JSON-LD | 0 | JSON parsing passed on all public pages |
| Article markup | 96 pages | Every indexable detail guide has Article markup; 5 lack `datePublished`, 3 lack `dateModified` |
| BreadcrumbList markup | 97 pages | Consistent with visible breadcrumbs on detail pages |
| HTTP/www handling | Passed | HTTP and www variants redirect to the canonical HTTPS host; legacy Spain URL is consolidated |
| Language | `en-GB` on all audited indexable pages | Correct for the site's editorial voice |

`robots.txt` allows crawling and points to the canonical sitemap. Canonicals are absolute HTTPS URLs and agree with local paths. Core content and internal links are present in server-delivered HTML, not JavaScript-dependent.

### Search Console baseline available in the repository

| Window | Clicks | Impressions | CTR | Average position | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| 27 Apr–3 May 2026 | 0 | 267 | 0% | 31.17 | Visibility concentrated in Greece/Turkey, Thailand, booking sites and Mauritius |
| 4–10 May 2026 | 1 | 42 | 2.38% | 14.71 | Much smaller footprint; one click on Greece vs Turkey |

The later seven-day export showed 38 desktop impressions at position 11.18 and only 4 mobile impressions at position 48.25; the sample is too small for a device conclusion. Country data was also sparse (23 US impressions and 10 UK impressions). These exports cannot establish the latest 90-day trend, cannot measure the current inbound cluster, and cannot support a causal conclusion about August changes.

The 8 May 2026 coverage export recorded 21 indexed and 131 not indexed URLs, including 118 “Discovered – currently not indexed.” The current repository has since deliberately noindexed 56 off-focus pages and exposes 108 indexable sitemap URLs. Current Search Console coverage is required to learn whether Google's index now matches that intended set.

### Rendered and performance baseline

Representative pages were inspected in a real browser at 1440px desktop, 1024px intermediate and 390px mobile widths. The inbound hub, Land's End guide and booking-sites guide retained semantic headings, skip links, readable order, crawlable tables and visible sources. No browser console warnings were observed on the sampled booking page.

| Page / mode | Performance | Accessibility | Best practices | SEO | LCP | TBT | CLS |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `/visit-uk/` mobile | 100 | 100 | 100 | 100 | 1.1s | 0ms | 0 |
| `/visit-uk/` desktop | 100 | 100 | 100 | 100 | 0.3s | 0ms | 0 |
| Land's End mobile | 96 | 100 | 100 | 100 | 2.9s | 0ms | 0 |
| Booking sites mobile | 82 | 100 | 77 | 100 | 4.1s | 270ms | 0 |

These are local Lighthouse lab results, not field Core Web Vitals. The booking-page penalty was associated with the analytics third party and unused/unminified shared CSS. No CLS risk appeared in the samples; committed local images have dimensions.

### Current search-result sampling

Search sampling on 28 August surfaced the homepage, London, motorway fuel, Land's End and booking-sites pages. Land's End and the booking page were crawled within days. Exact site queries did not surface Gatwick or supermarkets in the limited result set; this is not proof of non-indexation and should be checked with URL Inspection/Search Console.

Competing results tend to win with one or more of: a current price table, an explicit test methodology, a strong editorial brand, daily-updated data, or a title that states the exact decision. Budget Holidays Hub's defensible advantage is different: current official checks plus local/first-hand friction, costs and trade-offs. It should not imitate deal aggregators without live inventory.

## Prioritised findings

Scores are 1 (low) to 5 (high). Effort 1 is easiest.

| Priority | Finding | URLs/files | Impact | Confidence | Effort | Time to likely impact | Evidence / mechanism | Validation |
| --- | --- | --- | ---: | ---: | ---: | --- | --- | --- |
| P1 | Current 90-day Search Console data is missing | External data | 5 | 5 | 1 | Immediate prioritisation | Only two old seven-day exports exist; August pages cannot be assessed | Export pages, queries, dates, devices and countries for latest 90 days plus preceding 90 |
| P1 | Article sitemap freshness was inconsistent | `sitemap_gen.py`, `sitemap.xml` | 4 | 5 | 2 | Days–weeks | 79 Article `dateModified`/sitemap mismatches; inaccurate `lastmod` can be ignored | Regenerate; assert Article dates equal sitemap dates; resubmit sitemap |
| P1 | Land's End received only one unique internal source | `/visit-uk/lands-end-cornwall-on-a-budget/` | 4 | 5 | 1 | 1–6 weeks | Inlink crawl found one source despite first-hand content and current search visibility | Re-crawl unique inlinks; compare impressions/position after recrawl |
| P1 | Legacy quality debt limits trust and intent satisfaction | Spain family, Prague, Thailand and similar unrefreshed `/guides/` pages | 4 | 5 | 4 | 2–8 weeks | Sample pages have fixed price claims and superlatives with no external sources; visible disclaimers admit estimates | Refresh only pages with current impressions; fact-check claims and track page/query results |
| P1 | May CTR opportunity pages have changed since measurement | Booking sites, Greece vs Turkey, Mauritius | 5 | 4 | 1 | 2–6 weeks | May GSC: 54/6 booking impressions with 0 clicks; Greece/Turkey 80 then 30 impressions; all refreshed in August | Hold titles until a current 28-day/90-day comparison is available |
| P2 | Homepage still described future fieldwork after first-hand guide launched | `/index.html` | 3 | 5 | 1 | Days–weeks | Visible “future field note” and “build the first cluster” copy contradicted the live Land's End guide | Update copy/link; confirm rendered hierarchy and inlinks |
| P2 | Inbound analytics is inconsistent and consent handling is not evident | Six `/visit-uk/` pages, `privacy/index.html` | 3 | 5 | 3 | 2–8 weeks | 152/161 source pages contain GA ID; all six inbound pages omit it; privacy copy is generic | Decide consent mode/cookie policy first, then test page_view and CTA events with consent states |
| P2 | No named human creator/profile | Sitewide Article pages, `/about/` | 3 | 5 | 3 | 1–3 months | Article author is the organisation; About gives no person or verifiable experience | Add a truthful named profile, bio, role, methodology and relevant first-hand scope; reflect it in markup |
| P2 | Three Article pages lack modified dates; five lack publication dates | Selected legacy strategy guides | 2 | 5 | 2 | Weeks | Schema inventory | Add only dates supported by repository history/visible content; do not invent |
| P2 | Gatwick/London pages lack original route images or diagrams | Gatwick and London | 3 | 4 | 4 | 1–3 months | Pages are useful but visually/research-wise less defensible than the Land's End field guide | Capture privacy-safe original wayfinding/route evidence and record visit date |
| P2 | Booking page has lab LCP/TBT risk | Booking sites | 3 | 4 | 2 | Days–weeks | Mobile lab: LCP 4.1s, TBT 270ms; analytics third party and 35KiB unused CSS | Test live PSI/CrUX, then defer/consent-gate analytics and trim critical CSS without losing tracking |
| P3 | Shared sitewide links give the hubs strong authority but repetitive anchors | All indexable pages | 2 | 4 | 3 | Weeks | 108 unique inlink sources to both `/visit-uk/` and `/guides/`; most anchor text is identical | Keep nav links; concentrate new contextual links on priority detail pages rather than adding more hub links |

## URL-level opportunity table

| URL | Search intent / decision | Evidence | Recommended disposition | Next action |
| --- | --- | --- | --- | --- |
| `/visit-uk/` | Plan a realistic first UK trip | Strong answer-first hub; 108 inlink sources; no current GSC | Keep and measure | Track inbound queries/countries; add new field evidence only when real |
| `/visit-uk/london-on-a-budget/` | Reduce London cost without damaging the trip | Indexed in search sample; current sources; 5 inlink sources | Keep; selective refresh | Add field-tested route/spend after completing it; do not change date before then |
| `/visit-uk/gatwick-airport-to-london/` | Find station and choose the right direct London train | Good intent alignment; 3 inlink sources; not surfaced in limited exact search sample | Keep; improve proof | URL Inspection; add dated original wayfinding evidence; test query wording before title change |
| `/visit-uk/lands-end-cornwall-on-a-budget/` | Decide if Land's End is worth it and how to park/walk cheaply | Personally visited, original images, current search result; only 1 inlink source | Strengthen | Add homepage and road-trip contextual links; monitor parking/walk queries |
| `/visit-uk/supermarkets-for-tourists/` | Choose cheap ready-to-eat/self-catering food | Detailed current price checks; 4 inlink sources; crowded meal-deal SERP | Keep; measure | Inspect indexing and queries; compete on tourist scenarios and kitchen access, not only “cheapest meal deal” |
| `/visit-uk/avoid-motorway-fuel-prices/` | Find a safe cheaper fuel stop | Indexed; strong official evidence; 2 inlink sources | Keep | Link to a real road-trip field guide; monitor “motorway fuel prices” and “Fuel Finder” themes |
| `/guides/greece-vs-turkey-all-inclusive/` | Choose the better-value destination style | May: 80 impressions at 6.55, then 30 at 10.4 and 1 click; refreshed 25 Aug | Hold | Compare current 28 days with pre-refresh; no title churn yet |
| `/guides/best-travel-booking-websites-uk/` | Choose tools/providers by booking job | May: 54 impressions at 12.26, then 6 at 6.17, 0 clicks; refreshed 11 Aug | Hold and measure | Check current queries and live LCP; title test only if impressions remain meaningful and CTR weak |
| `/guides/cheap-holidays-mauritius-from-uk/` | Compare package with DIY | May: 37 impressions at 42.03; refreshed 18 Aug | Hold | Current data should show whether package-vs-DIY repositioning matches demand |
| `/guides/cheap-family-holidays-spain/` | Choose family region and booking type | Only 3 old impressions at position 36.67; 590 words, no authoritative external sources | Refresh if demand returns | Replace unsupported costs/superlatives; official entry, climate, airport/transport and package-protection sources |
| `/guides/cheap-holidays-prague-from-uk/` | Decide if Prague fits a cheap city break | One old impression at position 9; unsupported “Authority Guide,” “expert,” and “best-value beer” language | Refresh before snippet change | Remove claims without evidence; source transport/cost/entry information; then align title |
| `/guides/cheap-holidays-thailand-from-uk/` | Estimate total trip cost and best timing | 75 old impressions at position 62.76; fixed prices and no external sources | Substantive refresh or leave | Current GSC first; if demand persists, rebuild around live quote method, seasons, entry checks and route decisions |
| `/guides/travel-essentials-amazon-uk/` | Decide which travel items solve a real problem | One inlink source; commercial but transparent and well sourced | Leave low priority | Do not send scarce authority here ahead of inbound travel guides |

## Search-result presentation

These are proposed test snippets, not promises that Google will display them. Google builds title links and snippets from several page signals and may rewrite them; title, H1, visible answer and link anchors should remain aligned. [Google title guidance](https://developers.google.com/search/docs/appearance/title-link) and [snippet guidance](https://developers.google.com/search/docs/appearance/snippet).

| URL | Current title | Recommended title | Current meta | Recommended meta | Primary query theme / why it may win | Rewrite or trust risk |
| --- | --- | --- | --- | --- | --- | --- |
| `/visit-uk/` | Visit the UK on a Budget: 2026 Trip Planning Guide | Visit the UK on a Budget (2026): Routes, Costs & Local Tips | Plan a budget trip to the UK with current local advice on entry checks, London, trains, coaches, daily costs and realistic routes beyond the capital. | Plan a better-value UK trip with local advice on entry checks, London costs, trains, coaches and realistic routes beyond the capital. | “visit UK on a budget”; states the planning decisions | “Costs” is supported generally, but not a full daily-cost dataset; test only with current query evidence |
| `/visit-uk/london-on-a-budget/` | London on a Budget (2026): A Local Planning Guide | London on a Budget: Transport, Areas & 2-Day Plan (2026) | Visit London on a budget with a locally researched 2026 guide to contactless transport, free sights, where to stay, airport transfers and a two-day route. | Cut London costs without losing time: compare transport, where to stay, free sights, airport transfers and a realistic two-day plan. | “London on a budget”; concrete benefit and decisions | Low; visible content matches |
| `/visit-uk/gatwick-airport-to-london/` | Gatwick Airport to London: Terminals, Trains & Tips | Gatwick Airport to London: Which Train Should You Take? | A local guide to Gatwick Airport's North and South terminals, the free shuttle, railway station and choosing the right direct train into London. | Find Gatwick station from either terminal and choose the direct train for Victoria, London Bridge or St Pancras, with a simple luggage-friendly route. | “Gatwick Airport to London train”; exact decision and destinations | Must add/verify St Pancras wording visibly before use; Google may prefer the existing descriptive title |
| `/visit-uk/lands-end-cornwall-on-a-budget/` | Land's End Cornwall on a Budget: Walk & Parking Guide | Land's End on a Budget: Parking, Bus & Coast Walks | An honest, first-hand guide to Land's End in Cornwall: avoid the tourist-trap spend, find better-value parking and make the coast walk the main event. | Land's End is free to visit. Compare official and Sennen parking, bus access and three coast walks in this personally visited Cornwall guide. | “Land's End parking/walk”; proof plus exact choices | Price-free title is durable; “three walks” is visibly supported |
| `/visit-uk/supermarkets-for-tourists/` | UK Supermarkets for Tourists: Cheap Food & Ready Meals | UK Supermarkets for Tourists: Meal Deals & Cheap Food | Save money on food in the UK with this practical guide to Aldi, Lidl, Tesco, M&S, Waitrose, meal deals, ready meals and convenience stores. | Compare UK supermarkets, meal deals and ready meals for a hotel room, microwave or self-catering stay, with prices checked in August 2026. | “UK supermarkets for tourists”; scenario-specific advantage | Date becomes stale; remove or refresh through a substantive price check |
| `/visit-uk/avoid-motorway-fuel-prices/` | Avoid Motorway Fuel Prices: UK Route Planning Guide | UK Motorway Fuel Prices: How to Find Cheaper Stops | Avoid expensive UK motorway fuel with a safer route plan, near-live petrol price apps, simple savings examples and essential motorway service advice. | Find cheaper petrol or diesel near your UK motorway route using Fuel Finder tools, a five-minute stop plan and a simple detour-saving calculation. | “motorway fuel prices”; names the tool and task | Low; keep the safety caveat prominent |
| `/guides/best-travel-booking-websites-uk/` | Best Travel Websites for UK Travellers (2026) | Best Travel Booking Websites UK (2026): Compare by Trip | Compare the best travel websites for UK flights, hotels and package holidays. Use a practical booking-site checklist and verify the final price and protection. | Compare flight, hotel and package-booking websites by job, final price, support and protection—then choose who should take your payment. | “best travel booking websites UK”; sharper comparison method | “Best” needs the visible methodology, which is present; current GSC required before test |
| `/guides/greece-vs-turkey-all-inclusive/` | Greece or Turkey All-Inclusive: Which Is Better Value? | Keep current title | Greece or Turkey all-inclusive? Compare like-for-like package totals, resort facilities and holiday style to choose better value for your UK trip. | Keep current description | Exact comparison intent; current page now gives a clear decision | Recently refreshed; changing again would confound measurement |
| `/guides/cheap-holidays-mauritius-from-uk/` | Mauritius Holidays from the UK: Packages vs DIY | Mauritius Holidays from the UK: Packages vs DIY (2026) | Compare Mauritius holiday packages with DIY flights and accommodation using the same dates, inclusions, booking terms and current UK travel checks. | Compare a Mauritius package with DIY flights and hotels using the same dates, baggage, meals, transfers, protection and booking terms. | “Mauritius package vs DIY”; transparent method | Year is useful only while facts remain substantively reviewed |
| `/guides/cheap-family-holidays-spain/` | Cheap Family Holidays Spain: Best Low-Cost Resorts for UK Families | Cheap Family Holidays in Spain: Resorts, Costs & Best Months | Find cheap family holidays Spain deals with kid-friendly resort picks, UK flight costs, sample budgets, and practical ways to cut food, transfer, and hotel spend. | Compare family-friendly Spanish resorts, travel months and package versus self-catering costs, with practical ways to reduce the total from the UK. | Family Spain planning | Do not deploy until claims and costs are sourced |
| `/guides/cheap-holidays-prague-from-uk/` | Cheap Holidays to Prague From UK: 2026 Authority Guide | Cheap Prague Holidays from the UK: Costs, Areas & When to Go | Find cheap holidays to Prague from the UK in 2026. Expert research on beer prices, local 'Pivo' culture, and budget areas like Žižkov and Vinohrady. | Plan a lower-cost Prague city break from the UK: compare trip costs, areas to stay, flight options and when Budapest may offer a better fit. | Prague cost/area decision | Remove unsupported “authority/expert/best” language and source the content before deployment |

## Internal-link plan

| Priority | Source | Destination | Exact anchor | Placement context | Status |
| --- | --- | --- | --- | --- | --- |
| P1 | `/` | `/visit-uk/lands-end-cornwall-on-a-budget/` | `Land's End parking and coast-walk guide` | Replace the obsolete third “future side trip” route card with the live personally visited Cornwall field guide | Implemented in this audit sprint |
| P1 | `/visit-uk/avoid-motorway-fuel-prices/` | `/visit-uk/lands-end-cornwall-on-a-budget/` | `Land's End parking and coast-walk guide` | Closing planning paragraph for readers using a car on a Cornwall trip | Implemented in this audit sprint |
| P1 | `/visit-uk/lands-end-cornwall-on-a-budget/` | `/visit-uk/avoid-motorway-fuel-prices/` | `plan cheaper fuel stops on UK motorways` | “By car” bullet in Getting there; directly useful before the A30 journey | Implemented in this audit sprint |
| P2 | `/visit-uk/supermarkets-for-tourists/` | `/visit-uk/lands-end-cornwall-on-a-budget/` | `a budget day at Land's End` | Road-trip food section, as a concrete example of packing lunch before remote facilities | Add when that paragraph receives its next substantive edit |
| P2 | `/visit-uk/gatwick-airport-to-london/` | `/visit-uk/london-on-a-budget/` | `London on a budget guide` | Existing closing/next-step context | Already present; keep |
| P2 | `/visit-uk/london-on-a-budget/` | `/visit-uk/supermarkets-for-tourists/` | `saving money on food in the UK` | Existing food-budget context | Already present; keep |
| P2 | `/guides/best-travel-booking-websites-uk/` | `/guides/cheap-holidays-mauritius-from-uk/` | `compare a long-haul package with DIY` | Package-protection section after explaining like-for-like totals | Add only if current GSC shows Mauritius demand and the next-comparison CTA remains relevant |

Avoid adding more sitewide links to `/visit-uk/`: it already has 108 unique linking pages. New links should flow to the detail guide that best completes the reader's next decision.

## Cannibalisation and consolidation report

| URL set | Risk | Evidence | Recommendation |
| --- | --- | --- | --- |
| `/guides/spain-budget-holidays/` and `/guides/cheap-holidays-spain-from-uk/` | Resolved | Legacy page is noindex/canonical; live platform redirects to canonical; excluded from sitemap | Leave unchanged and keep monitoring HTTP/canonical variants in GSC |
| Spain generic, all-inclusive, June, September, cheapest places and family pages | Medium | Closely related titles, but intents can be distinct; no current query-to-page matrix | Keep separate only where each page answers a distinct decision. Export queries by page; consolidate pages sharing the same dominant queries and no unique value |
| Greece generic, Greece all-inclusive and Greece-vs-Turkey | Low–medium | Generic destination, package type and head-to-head decisions differ | Preserve; ensure comparison pages link to relevant detail pages and do not duplicate generic price tables |
| Turkey generic, Turkey all-inclusive and Turkey comparisons | Low–medium | Same pattern as Greece | Preserve while query themes remain distinct; refresh facts before expanding |
| Prague guide and Prague-vs-Budapest | Low | Destination plan versus comparison intent | Preserve and cross-link with explicit “choose” versus “plan” anchors |
| Mauritius page and generic cheapest-destination lists | Medium | Old GSC queries were generic “cheap Mauritius”; current page now targets package-vs-DIY | Use current page-query data. If generic intent dominates, broaden the visible answer without creating a second Mauritius URL |
| Thailand guide and generic cheapest-destination lists | Medium | Old page impressions came from broad cheap-holiday phrases; no first-page performance | Do not create more Thailand pages. Rebuild the existing URL if current demand justifies it |

No mass redirects are recommended without current GSC and backlink data. Consolidation should preserve the stronger URL, merge unique useful sections, implement a single-hop 301, update all internal links/canonical/sitemap entries, and measure query coverage for at least 28 days.

## Technical SEO report

### Passing controls

- Crawlable HTML, one H1, unique title and meta description, canonical, alt text and image dimensions all pass the repository audits.
- The live sitemap is reachable; all 108 listed URLs resolve to the same final URL with status 200.
- HTTP/www redirects and the known legacy Spain handoff pass live checks.
- `robots.txt` is permissive and references the canonical sitemap.
- 56 off-focus pages are intentionally `noindex` and excluded from the sitemap, supporting the travel focus.
- Breadcrumb and Article JSON-LD parses successfully and is consistent with visible content on sampled pages.
- No indexable video-first pages exist; therefore `VideoObject` is not a current rich-result opportunity. Eight YouTube embeds exist in the noindexed library.
- No pagination/archive system is present that requires canonical or crawl handling.

### Required repairs and risks

1. **Sitemap dates:** derive Article `lastmod` from Article `dateModified`; add a regression check. This audit implements the generator repair and regenerated sitemap.
2. **Schema completeness:** use repository history and visible dates to fill the 5 missing `datePublished` and 3 missing `dateModified` values. Do not infer a publication date from file timestamps. Google recommends accurate Article dates and author details. [Article structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/article)
3. **Current indexation:** inspect all 108 intended indexable URLs in current Search Console coverage. The May “discovered, not indexed” count is stale and likely includes pages later noindexed.
4. **Analytics/privacy:** do not simply copy the GA tag onto inbound pages. First establish a UK/EU-appropriate consent implementation and accurate privacy notice, then measure inbound page views and next-step events. This requires legal/privacy review.
5. **Performance:** verify live field CWV/CrUX where traffic permits. If booking-page demand is material, consent-gate/defer analytics and split/trim shared CSS. Do not remove valid tracking solely to improve a lab score.
6. **Images:** keep explicit dimensions and WebP. Add original images only where they convey route, wayfinding, accessibility or field evidence. Avoid decorative stock media.

## Content quality, intent and trust report

### Inbound cluster

The six inbound pages are the strongest content on the site. They answer the decision early, state evidence level, use limitations, link official sources and avoid pretending that a single cheapest option exists. Land's End is the model to repeat: visit date, original photography, current costs with warnings, accessibility limits, transit alternatives and a candid verdict.

Gaps:

- Gatwick says “personally used” but does not state when that use occurred or show original wayfinding evidence.
- London is explicitly locally researched and correctly avoids a field-tested claim; its future field-tested route should include exact spend, timing, accessibility and weather fallback.
- Fuel is well sourced and says which app “we use,” but should make the date and limits of that personal use explicit if this remains a recommendation.
- Supermarkets is distinctive because it maps advice to hotel room, microwave and self-catering scenarios. Its price-led sections require scheduled substantive rechecks.
- The hub has no original media, which is acceptable for speed but leaves less proof than the field guide; useful maps/route diagrams should be added only when original and accurate.

### Legacy cluster

The refreshed Greece/Turkey, booking-sites and Mauritius pages now use methods, limitations and official sources. Older sampled pages do not meet that standard:

- Spain family: no external sources; fixed cost and resort claims.
- Prague: “Authority Guide,” “Expert research,” “gold standard,” “world-class” and price claims without sources.
- Thailand: fixed flight/daily budgets and “cheapest month” claims without sources.

Do not expand these pages by word count. For a page with current demand, replace unsupported certainty with: a reproducible live-quote method, official entry/safety sources, realistic inclusion comparison, a dated climate/season source, transport friction, who should choose another destination, and a relevant next action. If there is no current demand or unique value, leave it unchanged or consolidate rather than refreshing for volume.

### Trust and conversion

- Affiliate disclosure is visible on the Amazon page and commercial links are labelled. The travel-information pages are not crowded by affiliate units.
- Organisation-level About, Research, Standards, Contact, Privacy and Disclosure pages exist.
- The biggest trust gap is identity: no named creator, author profile, qualifications/experience boundaries or correction owner is visible. Add only truthful details.
- The unfinished “social media channels coming soon” Contact section was removed during the follow-on sprint.
- Calls to action on inbound pages are generally relevant planning steps. Keep commercial CTAs secondary to the answer.

## Roadmap

### Immediate actions: next 48 hours

| Action | Files/URLs | Mechanism | Effort | Risk | Validation / external dependency |
| --- | --- | --- | ---: | --- | --- |
| Derive Article sitemap dates from `dateModified` and regenerate | `sitemap_gen.py`, `sitemap.xml` | Verifiable freshness and consistent crawl signals | 2 | Low | Local SEO audits; compare all Article dates; live check after deploy; no GSC required |
| Add contextual authority to Land's End and remove obsolete future-state homepage copy | `index.html`, fuel and Land's End pages | More relevant inlinks and accurate user expectation | 1 | Low | Re-crawl inlinks; browser QA; no GSC required |
| Export current Search Console data | External | Reveals actual CTR and near-page-one opportunities | 1 | None | Requires GSC access |
| URL Inspection for all six inbound pages | External | Distinguishes indexed, crawled and discovered states | 1 | None | Requires GSC access |

### Short-term sprint: next 7 days

- Build a latest-90-days versus preceding-90-days page/query workbook, separated into `/visit-uk/` and `/guides/`.
- For pages with at least meaningful impressions, identify query groups in positions 4–20 and compare mobile/desktop and key countries.
- Decide whether booking-sites, Greece/Turkey and Mauritius August refreshes should be kept based on post-change impressions, CTR and position; avoid overlapping change windows.
- Keep the new automated assertion that sitemap Article `lastmod == dateModified` in every publishing run.
- Resolve the analytics/consent architecture and update the privacy notice before instrumenting inbound pages.
- Verify Google rich-result parsing for representative Article and Breadcrumb markup after deployment.

### Growth work: next 30 days

- Refresh one legacy page at a time in current GSC opportunity order. Start with a page that has both meaningful impressions and positions 4–20, not the weakest page.
- Add truthful creator identity/profile and connect visible byline, Article author markup and About page.
- Complete a field-tested Gatwick or London route with visit date, original wayfinding/accessibility evidence, actual timings and spend.
- Reconcile the London/base claims with the real author profile; unfinished social-channel copy has already been removed.
- Evaluate Spain query overlap and consolidate only with page-level query evidence and backlink checks.

### Longer-term work: 60–90 days

- Publish the next inbound field guide only when a real trip answers a distinct high-friction question surfaced by GSC or visitor questions.
- Build original decision assets: airport wayfinding, door-to-door route diagrams, accessibility notes, wet-weather fallbacks and dated cost worksheets.
- Earn relevant links through genuinely useful local evidence, not generic destination outreach.
- Review field CWV and consented analytics data; optimise high-traffic templates only where real users show friction.
- Reassess the 108-URL indexable set. Noindex, merge or retire low-value pages only after current GSC/backlink checks.

## Measurement plan

Create one row per changed URL and one row per target query theme:

| Field | Rule |
| --- | --- |
| Change date | Deployment date, not commit date |
| URL and change type | Title/meta, content, internal links, schema, redirect or technical |
| Queries targeted | Actual pre-change GSC query groups; do not invent volume |
| Baseline | Previous 28 complete days; also retain a 90-day view for low-volume pages |
| Comparison | First stable 28 complete days after recrawl versus previous 28; use year-on-year where seasonality makes it useful |
| Metrics | Clicks, impressions, CTR, average position, indexed status |
| Splits | Mobile/desktop/tablet and country; focus inbound pages on markets that actually produce impressions |
| Confounders | Seasonality, algorithm updates, SERP features, another page change, outages, promotions |
| Decision | Keep if qualified clicks improve without material intent/rank loss; revise if impressions/rank hold but CTR does not; reverse only with enough data and a credible causal case |

For a title test, change only title/meta/above-fold alignment on that URL, record the recrawl date, and avoid another major edit for at least 28 complete days unless the change is misleading or broken. Low-volume pages may need 56–84 days; do not claim a win from a handful of impressions.

Suggested tracking sheet columns:

`URL | change date | changed element | target query group | pre clicks | post clicks | pre impressions | post impressions | pre CTR | post CTR | pre position | post position | device | country | recrawl date | seasonality/confounders | keep/revise/reverse | notes`

## Assumptions, missing data and uncompleted checks

- No current Search Console connection/export was available. The latest repository data ends 10 May 2026 and covers only two seven-day windows.
- No GA4 report, consent configuration, conversion data, backlink export, server log or revenue data was available.
- Search-result sampling is not a neutral rank tracker, and personalised/location/device SERPs were not available. Competitor observations are hypotheses, not measured ranking factors.
- Current Google URL Inspection, rich-result test results and rendered Googlebot screenshots require external access.
- Lighthouse results are local lab diagnostics, not field CWV or a claim of WCAG conformance.
- Keyboard/semantic order and narrow rendered layouts were inspected; a full assistive-technology audit, 200% zoom matrix and every interactive state were not completed.
- YouTube oEmbed network validation was not rerun because the relevant pages are intentionally noindex; the local audit found eight embed IDs and valid JSON-LD.
- No first-hand claim, factual review date, price or business rule was changed by the implemented immediate work.
