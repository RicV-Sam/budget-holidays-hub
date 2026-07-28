# UK Field Guide Workflow

Use this folder to turn a real UK trip into a useful, evidence-backed page.
Nothing in `fieldwork/` is deployed by the public-site build.

## 1. Choose a reader question

A trip needs one primary question. Good examples:

- Is this day trip worth doing without a car?
- Which airport transfer is easiest with luggage?
- Should a visitor stay overnight or return to the arrival city?
- Does an attraction pass save money on a realistic itinerary?
- What is the best poor-weather version of this route?

Avoid starting with a generic title such as "The complete guide to [place]."

## 2. Prepare the capture sheet

Copy `trip-capture-template.md` and rename it with the trip date and route:

`YYYY-MM-DD-origin-to-destination.md`

Complete the planned-route and official-source sections before leaving.

## 3. Complete the journey

Record what a visitor would actually experience:

- Door-to-door time.
- Every change and meaningful walk.
- Luggage and accessibility friction.
- Tickets, entry, food and unavoidable extras.
- Queues, crowding, toilets, seating and mobile signal.
- A workable bad-weather alternative.
- What was not worth the time or price.

Do not record or publish card numbers, booking references, home addresses,
faces without permission or other personal information.

## 4. Draft the page

Copy `templates/uk-field-guide-template.html` to:

`visit-uk/<descriptive-slug>/index.html`

The template is deliberately `noindex`. Keep it that way until:

- All placeholder text is removed.
- The visible visit date is accurate.
- The evidence label matches what happened.
- Prices are dated and described as point-in-time checks.
- Changing facts link to official sources.
- The page has a clear verdict and states who should choose another option.
- Original images have useful alt text, explicit dimensions and no sensitive
  metadata.
- At least two relevant public pages link to it.
- The page passes both SEO audits and visual checks.

## 5. Publish deliberately

When the page is ready:

1. Change `noindex, nofollow` to `index, follow`.
2. Add the URL to `sitemap_gen.py`.
3. Add it to the `/visit-uk/` hub and one other relevant page.
4. Regenerate the sitemap.
5. Run `npm run audit:seo` and `npm run prepare:pages`.
6. Review desktop, mobile, keyboard focus and 200% zoom.
7. Publish through the normal GitHub Pages workflow.

Do not change the homepage or hub review date unless their visible main
content also changes.
