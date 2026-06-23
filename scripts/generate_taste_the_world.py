import json
import re
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "taste-the-world-recipes.json"
OUTPUT_DIR = ROOT / "taste-the-world"


def load_data():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def page_path_to_file(path):
    clean = path.split("#", 1)[0].split("?", 1)[0]
    if clean == "/":
        return ROOT / "index.html"
    if clean.endswith("/"):
        return ROOT / clean.strip("/") / "index.html"
    return ROOT / clean.strip("/")


def internal_target_exists(href):
    if not href.startswith("/") or href.startswith("//"):
        return True
    clean = href.split("#", 1)[0].split("?", 1)[0]
    if not clean:
        return True
    return page_path_to_file(clean).exists()


def absolute_url(base_url, path):
    return f"{base_url.rstrip('/')}{path}"


def image_url(base_url, image_path):
    if not image_path:
        return absolute_url(base_url, "/assets/images/taste-the-world-global.svg")
    if image_path.startswith("http"):
        return image_path
    return absolute_url(base_url, image_path)


def image_size_attrs(image_path):
    if image_path.startswith("/assets/images/taste-the-world-") and image_path.endswith(".svg"):
        return ' width="1200" height="675"'
    return ""


def json_script(payload):
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(payload, indent=2)
        + "\n</script>"
    )


def track_attrs(event_name, payload):
    payload_json = json.dumps(payload, separators=(",", ":"))
    return (
        f' data-track-event="{escape(event_name, quote=True)}"'
        f' data-track-payload="{escape(payload_json, quote=True)}"'
    )


def format_cost(cost):
    match = re.match(r"GBP\s+(\d+)-(\d+)$", cost)
    if match:
        return f"&pound;{match.group(1)}-&pound;{match.group(2)}"
    return escape(cost)


def slug_label(slug):
    return " ".join(part.capitalize() for part in slug.split("-"))


def nav_html(current="taste"):
    def current_attr(key):
        return ' aria-current="page"' if key == current else ""

    return f"""
<nav aria-label="Main navigation" class="site-nav">
    <div class="nav-inner">
        <a href="/" class="brand"><span class="brand-icon" aria-hidden="true">&#9992;</span>Budget Holidays Hub</a>
        <div class="nav-links">
            <a href="/"{current_attr("home")}>Home</a>
            <a href="/guides/"{current_attr("guides")}>Guides</a>
            <a href="/make-money-for-travel/"{current_attr("money")}>Make Money for Travel</a>
            <a href="/videos/"{current_attr("videos")}>Videos</a>
            <a href="/about/"{current_attr("about")}>About</a>
            <a href="/how-we-research/"{current_attr("research")}>How We Research</a>
            <a href="/editorial-standards/"{current_attr("standards")}>Editorial Standards</a>
            <a href="/affiliate-disclosure/"{current_attr("disclosure")}>Disclosure</a>
            <a href="/contact/"{current_attr("contact")}>Contact</a>
        </div>
    </div>
</nav>"""


def footer_html():
    return """
<footer class="site-footer">
    <a href="/" class="brand"><span class="brand-icon" aria-hidden="true">&#9992;</span>Budget Holidays Hub</a>
    <nav aria-label="Footer navigation">
        <a href="/">Home</a>
        <a href="/guides/">Guides</a>
        <a href="/taste-the-world/" aria-current="page">Taste the World</a>
        <a href="/make-money-for-travel/">Make Money for Travel</a>
        <a href="/videos/">Videos</a>
        <a href="/about/">About</a>
        <a href="/how-we-research/">Research</a>
        <a href="/editorial-standards/">Standards</a>
        <a href="/affiliate-disclosure/">Disclosure</a>
        <a href="/privacy/">Privacy</a>
        <a href="/terms/">Terms</a>
    </nav>
    <p>&copy; 2026 Budget Holidays Hub &bull; For UK Travellers</p>
</footer>"""


def analytics_and_ads():
    return """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VEDYHTE156"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag("js", new Date());
  gtag("config", "G-VEDYHTE156");
</script>"""


def head_html(data, title, description, path, og_type, image_path, schemas):
    base_url = data["site"]["baseUrl"]
    canonical = absolute_url(base_url, path)
    og_image = image_url(base_url, image_path)
    schema_markup = "\n".join(json_script(schema) for schema in schemas)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
{analytics_and_ads()}
<meta charset="UTF-8">
<link rel="canonical" href="{escape(canonical, quote=True)}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0a4da3">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="stylesheet" href="/assets/css/style.css">
<link rel="prefetch" href="/guides/">
<meta property="og:type" content="{escape(og_type, quote=True)}">
<meta property="og:url" content="{escape(canonical, quote=True)}">
<meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:image" content="{escape(og_image, quote=True)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="{escape(canonical, quote=True)}">
<meta name="twitter:title" content="{escape(title, quote=True)}">
<meta name="twitter:description" content="{escape(description, quote=True)}">
<meta name="twitter:image" content="{escape(og_image, quote=True)}">
{schema_markup}
</head>"""


def breadcrumb_schema(data, items):
    base_url = data["site"]["baseUrl"]
    elements = []
    for index, item in enumerate(items, start=1):
        element = {
            "@type": "ListItem",
            "position": index,
            "name": item["name"],
        }
        if item.get("href"):
            element["item"] = absolute_url(base_url, item["href"])
        elements.append(element)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq["answer"],
                },
            }
            for faq in faqs
        ],
    }


def breadcrumb_html(items):
    parts = ['<nav aria-label="Breadcrumb" class="breadcrumb"><ol>']
    for index, item in enumerate(items):
        if index == len(items) - 1:
            parts.append(f'<li aria-current="page">{escape(item["name"])}</li>')
        else:
            parts.append(
                f'<li><a href="{escape(item["href"], quote=True)}">{escape(item["name"])}</a></li>'
            )
    parts.append("</ol></nav>")
    return "\n".join(parts)


def get_recipes_by_slug(data):
    return {recipe["slug"]: recipe for recipe in data["recipes"]}


def get_cuisines_by_slug(data):
    return {cuisine["slug"]: cuisine for cuisine in data["cuisines"]}


def recipe_url(recipe):
    return f"/taste-the-world/{recipe['cuisineSlug']}/{recipe['slug']}/"


def cuisine_url(cuisine):
    return f"/taste-the-world/{cuisine['slug']}/"


def valid_travel_links(data, keys):
    links = []
    seen = set()
    for key in keys:
        for link in data["travelLinks"].get(key, []):
            href = link["href"]
            if href in seen:
                continue
            if internal_target_exists(href):
                links.append(link)
                seen.add(href)
    return links


def travel_link_cards(data, keys, event_name, payload_base):
    links = valid_travel_links(data, keys)
    if not links:
        return '<p class="meta">Destination links will be added here once matching BudgetHolidayHub guides are live.</p>'

    cards = []
    for link in links:
        payload = dict(payload_base)
        payload.update({"destination": link.get("destination", ""), "link_url": link["href"]})
        cards.append(
            f"""<a class="travel-link-card" href="{escape(link['href'], quote=True)}"{track_attrs(event_name, payload)}>
    <span>{escape(link.get("destination", "Travel"))}</span>
    <strong>{escape(link["label"])}</strong>
    <em>Explore guide &rarr;</em>
</a>"""
        )
    return '<div class="travel-link-grid">\n' + "\n".join(cards) + "\n</div>"


def recipe_card(recipe, cuisine, location="hub"):
    attrs = track_attrs(
        "recipe_card_click",
        {
            "recipe_slug": recipe["slug"],
            "cuisine": recipe["cuisine"],
            "click_location": location,
        },
    )
    return f"""<a class="guide-card recipe-card" href="{escape(recipe_url(recipe), quote=True)}"{attrs}>
    <div class="guide-card-image">
        <img src="{escape(recipe['heroImage'], quote=True)}" alt="{escape(recipe['imageAlt'], quote=True)}" loading="lazy"{image_size_attrs(recipe['heroImage'])}>
    </div>
    <div class="guide-card-content">
        <span class="badge badge-city">{escape(recipe['cuisine'])}</span>
        <h3>{escape(recipe['title'])}</h3>
        <p>{escape(recipe['metaDescription'])}</p>
        <span class="recipe-card-meta">{escape(recipe['totalTime'])} &bull; {escape(recipe['difficulty'])} &bull; {format_cost(recipe['estimatedCost'])}</span>
        <span class="guide-card-cta">Cook this recipe <span aria-hidden="true">&rarr;</span></span>
    </div>
</a>"""


def cuisine_card(cuisine, recipe_count):
    attrs = track_attrs(
        "taste_world_cuisine_click",
        {
            "cuisine": cuisine["name"],
            "link_url": cuisine_url(cuisine),
            "click_location": "main_hub",
        },
    )
    return f"""<a class="guide-card cuisine-card" href="{escape(cuisine_url(cuisine), quote=True)}"{attrs}>
    <div class="guide-card-image">
        <img src="{escape(cuisine['image'], quote=True)}" alt="{escape(cuisine['imageAlt'], quote=True)}" loading="lazy"{image_size_attrs(cuisine['image'])}>
    </div>
    <div class="guide-card-content">
        <span class="badge badge-popular">{recipe_count} recipes</span>
        <h3>{escape(cuisine['name'])}</h3>
        <p>{escape(cuisine['cardDescription'])}</p>
        <span class="guide-card-cta">Explore {escape(cuisine['name'])} <span aria-hidden="true">&rarr;</span></span>
    </div>
</a>"""


def render_main_hub(data):
    site = data["site"]
    cuisines = data["cuisines"]
    recipes = data["recipes"]
    base_url = site["baseUrl"]
    path = "/taste-the-world/"

    item_list = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Taste the World recipe cuisines",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "url": absolute_url(base_url, cuisine_url(cuisine)),
                "name": cuisine["name"],
            }
            for index, cuisine in enumerate(cuisines, start=1)
        ],
    }
    webpage_schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": site["sectionName"],
        "description": site["sectionMetaDescription"],
        "url": absolute_url(base_url, path),
        "isPartOf": {
            "@type": "WebSite",
            "name": "Budget Holidays Hub",
            "url": base_url,
        },
    }
    breadcrumbs = [
        {"name": "Home", "href": "/"},
        {"name": "Taste the World"},
    ]
    counts = {
        cuisine["slug"]: len([r for r in recipes if r["cuisineSlug"] == cuisine["slug"]])
        for cuisine in cuisines
    }

    cards = "\n".join(cuisine_card(cuisine, counts[cuisine["slug"]]) for cuisine in cuisines)
    travel_links = travel_link_cards(
        data,
        ["global"],
        "recipe_travel_cta_click",
        {"click_location": "taste_world_hub"},
    )

    return f"""{head_html(data, site['sectionSeoTitle'], site['sectionMetaDescription'], path, "website", "/assets/images/taste-the-world-global.svg", [webpage_schema, item_list, breadcrumb_schema(data, breadcrumbs)])}
<body data-taste-world-view="taste_world_hub_view" data-taste-world-payload="{{}}">
<a href="#main-content" class="skip-link">Skip to main content</a>
{nav_html("taste")}
<main id="main-content" class="taste-page">
{breadcrumb_html(breadcrumbs)}
<section class="section-panel hero taste-hero" aria-label="Taste the World hero">
    <p class="eyebrow">Travel-Inspired Recipes</p>
    <h1>Taste the World</h1>
    <p class="hero-subtitle">{escape(site['sectionIntro'])}</p>
    <div class="taste-hero-actions">
        <a href="/taste-the-world/thai-recipes/" class="hero-cta"{track_attrs("taste_world_cuisine_click", {"cuisine": "Thai Recipes", "link_url": "/taste-the-world/thai-recipes/", "click_location": "hero"})}>Explore Thai Recipes <span aria-hidden="true">&rarr;</span></a>
        <a href="/taste-the-world/indian-recipes/" class="hero-cta hero-cta-secondary"{track_attrs("taste_world_cuisine_click", {"cuisine": "Indian Recipes", "link_url": "/taste-the-world/indian-recipes/", "click_location": "hero"})}>Explore Indian Recipes</a>
    </div>
</section>

<section class="section" aria-labelledby="cuisine-title">
    <h2 id="cuisine-title">Choose a Cuisine</h2>
    <p class="section-intro">Start with Thai and Indian recipe clusters built around useful home cooking and travel inspiration.</p>
    <div class="guides-grid taste-card-grid">
        {cards}
    </div>
</section>

<section class="section taste-editorial" aria-labelledby="cook-holiday-title">
    <div class="editorial-container">
        <p class="eyebrow">Cook Your Next Holiday</p>
        <h2 id="cook-holiday-title">Bring the Trip Home First</h2>
        <p class="editorial-text">Food is one of the easiest ways to bring a holiday home. These recipes are designed for everyday kitchens, using ingredients that are easier to find in UK and European supermarkets, while linking back to the destinations that inspired them.</p>
    </div>
</section>

<section class="section" aria-labelledby="plan-trip-title">
    <h2 id="plan-trip-title">Plan the Trip Behind the Taste</h2>
    <p class="section-intro">Move from the recipe to confirmed BudgetHolidayHub travel pages without broken destination links.</p>
    {travel_links}
</section>
</main>
<script src="/assets/js/taste-the-world.js"></script>
{footer_html()}
</body>
</html>"""


def render_cuisine_hub(data, cuisine):
    site = data["site"]
    base_url = site["baseUrl"]
    path = cuisine_url(cuisine)
    recipes = [recipe for recipe in data["recipes"] if recipe["cuisineSlug"] == cuisine["slug"]]
    cards = "\n".join(recipe_card(recipe, cuisine, "cuisine_hub") for recipe in recipes)
    other_cuisines = [item for item in data["cuisines"] if item["slug"] != cuisine["slug"]]
    other_cards = "\n".join(
        cuisine_card(item, len([r for r in data["recipes"] if r["cuisineSlug"] == item["slug"]]))
        for item in other_cuisines
    )
    breadcrumbs = [
        {"name": "Home", "href": "/"},
        {"name": "Taste the World", "href": "/taste-the-world/"},
        {"name": cuisine["name"]},
    ]
    collection_schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": cuisine["h1"],
        "description": cuisine["metaDescription"],
        "url": absolute_url(base_url, path),
        "about": {
            "@type": "Country",
            "name": cuisine["country"],
        },
        "isPartOf": {
            "@type": "WebSite",
            "name": "Budget Holidays Hub",
            "url": base_url,
        },
    }
    item_list = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": cuisine["name"],
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "url": absolute_url(base_url, recipe_url(recipe)),
                "name": recipe["title"],
            }
            for index, recipe in enumerate(recipes, start=1)
        ],
    }
    faqs = "".join(
        f"""<details class="faq-item">
    <summary>{escape(faq['question'])}</summary>
    <p>{escape(faq['answer'])}</p>
</details>"""
        for faq in cuisine["faqs"]
    )
    why_body = "\n".join(f"<p>{escape(paragraph)}</p>" for paragraph in cuisine["whyBody"])
    travel_links = travel_link_cards(
        data,
        cuisine["travelLinkKeys"],
        "recipe_travel_cta_click",
        {"cuisine": cuisine["name"], "click_location": "cuisine_hub"},
    )

    return f"""{head_html(data, cuisine['seoTitle'], cuisine['metaDescription'], path, "website", cuisine["image"], [collection_schema, item_list, breadcrumb_schema(data, breadcrumbs), faq_schema(cuisine["faqs"])])}
<body data-taste-world-view="taste_world_cuisine_view" data-taste-world-payload="{escape(json.dumps({"cuisine": cuisine["name"]}), quote=True)}">
<a href="#main-content" class="skip-link">Skip to main content</a>
{nav_html("taste")}
<main id="main-content" class="taste-page cuisine-page">
{breadcrumb_html(breadcrumbs)}
<section class="section-panel hero taste-hero cuisine-hero" aria-label="{escape(cuisine['name'], quote=True)} hero">
    <p class="eyebrow">Taste the World</p>
    <h1>{escape(cuisine['h1'])}</h1>
    <p class="hero-subtitle">{escape(cuisine['intro'])}</p>
</section>

<section class="section" aria-labelledby="recipes-title">
    <h2 id="recipes-title">{escape(cuisine['name'])}</h2>
    <p class="section-intro">Quick routes into the first {len(recipes)} travel-inspired recipes in this cuisine cluster.</p>
    <div class="guides-grid taste-card-grid">
        {cards}
    </div>
</section>

<section class="section taste-editorial" aria-labelledby="why-title">
    <div class="editorial-container">
        <h2 id="why-title">{escape(cuisine['whyTitle'])}</h2>
        {why_body}
    </div>
</section>

<section class="section" aria-labelledby="travel-title">
    <h2 id="travel-title">{escape(cuisine['travelTitle'])}</h2>
    <p class="section-intro">{escape(cuisine['travelIntro'])}</p>
    {travel_links}
</section>

<section class="section" aria-labelledby="faq-title">
    <h2 id="faq-title">FAQs</h2>
    <div class="recipe-faq-list">
        {faqs}
    </div>
</section>

<section class="section" aria-labelledby="related-cuisines-title">
    <h2 id="related-cuisines-title">Related Cuisines</h2>
    <div class="guides-grid taste-card-grid">
        {other_cards}
    </div>
</section>
</main>
<script src="/assets/js/taste-the-world.js"></script>
{footer_html()}
</body>
</html>"""


def summary_card(recipe):
    rows = [
        ("Prep time", recipe["prepTime"]),
        ("Cook time", recipe["cookTime"]),
        ("Total time", recipe["totalTime"]),
        ("Servings", str(recipe["servings"])),
        ("Difficulty", recipe["difficulty"]),
        ("Estimated cost", format_cost(recipe["estimatedCost"])),
        ("Cuisine", recipe["cuisine"]),
        ("Inspired by", recipe["inspiredBy"]),
    ]
    items = "\n".join(
        f"<div><dt>{escape(label)}</dt><dd>{value if label == 'Estimated cost' else escape(value)}</dd></div>"
        for label, value in rows
    )
    return f"""<section class="recipe-summary-card" aria-labelledby="recipe-summary-title">
    <h2 id="recipe-summary-title">Recipe Summary</h2>
    <dl>{items}</dl>
</section>"""


def list_items(items):
    return "\n".join(f"<li>{escape(item)}</li>" for item in items)


def method_items(items):
    return "\n".join(
        f"<li><span>{index}</span><p>{escape(item)}</p></li>"
        for index, item in enumerate(items, start=1)
    )


def substitutions_table(items):
    rows = "\n".join(
        f"<tr><td>{escape(item['original'])}</td><td>{escape(item['substitute'])}</td></tr>"
        for item in items
    )
    return f"""<div class="responsive-table">
<table class="substitution-table">
    <thead>
        <tr><th>Ingredient</th><th>Easy swap</th></tr>
    </thead>
    <tbody>
        {rows}
    </tbody>
</table>
</div>"""


def render_recipe_page(data, recipe):
    site = data["site"]
    base_url = site["baseUrl"]
    cuisines = get_cuisines_by_slug(data)
    recipes_by_slug = get_recipes_by_slug(data)
    cuisine = cuisines[recipe["cuisineSlug"]]
    path = recipe_url(recipe)
    breadcrumbs = [
        {"name": "Home", "href": "/"},
        {"name": "Taste the World", "href": "/taste-the-world/"},
        {"name": cuisine["name"], "href": cuisine_url(cuisine)},
        {"name": recipe["title"]},
    ]
    recipe_schema = {
        "@context": "https://schema.org",
        "@type": "Recipe",
        "name": recipe["title"],
        "description": recipe["metaDescription"],
        "image": [image_url(base_url, recipe["heroImage"])],
        "author": {
            "@type": "Organization",
            "name": "Budget Holidays Hub",
            "url": base_url,
        },
        "publisher": {
            "@type": "Organization",
            "name": "Budget Holidays Hub",
            "url": base_url,
        },
        "datePublished": site["datePublished"],
        "dateModified": site["dateModified"],
        "prepTime": recipe["prepTimeIso"],
        "cookTime": recipe["cookTimeIso"],
        "totalTime": recipe["totalTimeIso"],
        "recipeYield": f"{recipe['servings']} servings",
        "recipeCuisine": recipe["cuisine"],
        "recipeCategory": recipe["category"],
        "recipeIngredient": recipe["ingredients"],
        "recipeInstructions": [
            {"@type": "HowToStep", "position": index, "text": step}
            for index, step in enumerate(recipe["method"], start=1)
        ],
        "keywords": ", ".join(recipe["keywords"]),
        "mainEntityOfPage": absolute_url(base_url, path),
    }
    faqs = "".join(
        f"""<details class="faq-item">
    <summary>{escape(faq['question'])}</summary>
    <p>{escape(faq['answer'])}</p>
</details>"""
        for faq in recipe["faqs"]
    )
    related_cards = "\n".join(
        recipe_card(recipes_by_slug[slug], cuisine, "related_recipes")
        for slug in recipe["relatedRecipes"]
        if slug in recipes_by_slug
    )
    travel_links = travel_link_cards(
        data,
        recipe["travelLinkKeys"],
        "recipe_travel_cta_click",
        {
            "recipe_slug": recipe["slug"],
            "cuisine": recipe["cuisine"],
            "click_location": "recipe_page",
        },
    )

    return f"""{head_html(data, recipe['seoTitle'], recipe['metaDescription'], path, "article", recipe["heroImage"], [recipe_schema, breadcrumb_schema(data, breadcrumbs), faq_schema(recipe["faqs"])])}
<body data-taste-world-view="recipe_page_view" data-taste-world-payload="{escape(json.dumps({"recipe_slug": recipe["slug"], "cuisine": recipe["cuisine"]}), quote=True)}">
<a href="#main-content" class="skip-link">Skip to main content</a>
{nav_html("taste")}
<main id="main-content" class="recipe-layout">
{breadcrumb_html(breadcrumbs)}
<article class="recipe-article">
    <header class="recipe-hero">
        <div class="recipe-hero-copy">
            <p class="eyebrow">Taste the World</p>
            <h1>{escape(recipe['h1'])}</h1>
            <p class="last-updated">Last updated: May 2026</p>
            <p class="recipe-intro">{escape(recipe['intro'])}</p>
        </div>
        <div class="recipe-hero-media">
            <img src="{escape(recipe['heroImage'], quote=True)}" alt="{escape(recipe['imageAlt'], quote=True)}" loading="eager"{image_size_attrs(recipe['heroImage'])}>
        </div>
    </header>

    {summary_card(recipe)}

    <nav class="quick-nav recipe-jump-links" aria-label="Recipe sections">
        <strong>Jump to:</strong>
        <ul>
            <li><a href="#ingredients">Ingredients</a></li>
            <li><a href="#method">Method</a></li>
            <li><a href="#swaps">Ingredient swaps</a></li>
            <li><a href="#budget-tips">Budget tips</a></li>
            <li><a href="#travel">Travel links</a></li>
            <li><a href="#faqs">FAQs</a></li>
        </ul>
    </nav>

    <section id="ingredients" class="recipe-section">
        <h2>Ingredients</h2>
        <ul class="ingredient-list">
            {list_items(recipe['ingredients'])}
        </ul>
    </section>

    <section id="method" class="recipe-section">
        <h2>Method</h2>
        <ol class="method-list">
            {method_items(recipe['method'])}
        </ol>
    </section>

    <section id="swaps" class="recipe-section">
        <h2>Easy UK &amp; European Ingredient Swaps</h2>
        {substitutions_table(recipe['substitutions'])}
    </section>

    <section id="budget-tips" class="recipe-section budget-tips-block">
        <h2>Budget Cooking Tips</h2>
        <ul>
            {list_items(recipe['budgetTips'])}
        </ul>
    </section>

    <section id="travel" class="recipe-section travel-connection">
        <h2>Plan the Holiday Behind This Dish</h2>
        <p>{escape(recipe['travelConnection'])}</p>
        {travel_links}
    </section>

    <section class="recipe-section" aria-labelledby="related-recipes-title">
        <h2 id="related-recipes-title">Related Recipes</h2>
        <div class="guides-grid taste-card-grid related-recipe-grid">
            {related_cards}
        </div>
    </section>

    <section id="faqs" class="recipe-section">
        <h2>FAQs</h2>
        <div class="recipe-faq-list">
            {faqs}
        </div>
    </section>
</article>
</main>
<script src="/assets/js/taste-the-world.js"></script>
{footer_html()}
</body>
</html>"""


def write_page(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def main():
    data = load_data()
    write_page(OUTPUT_DIR / "index.html", render_main_hub(data))

    for cuisine in data["cuisines"]:
        write_page(OUTPUT_DIR / cuisine["slug"] / "index.html", render_cuisine_hub(data, cuisine))

    for recipe in data["recipes"]:
        write_page(
            OUTPUT_DIR / recipe["cuisineSlug"] / recipe["slug"] / "index.html",
            render_recipe_page(data, recipe),
        )

    print(f"Generated Taste the World pages in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
