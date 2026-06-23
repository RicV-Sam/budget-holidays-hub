import os
import datetime
import json

base_url = "https://budgetholidayshub.com"
focus_pages = [
    "guides/cheap-holidays-spain-from-uk/",
    "guides/best-travel-booking-websites-uk/",
    "guides/greece-vs-turkey-all-inclusive/",
    "guides/cheap-holidays-turkey-all-inclusive-from-uk/",
    "guides/cheap-holidays-mauritius-from-uk/"
]

current_sprint_lastmod_paths = {
    "",
    "about/",
    "affiliate-disclosure/",
    "contact/",
    "editorial-standards/",
    "guides/",
    "guides/best-travel-booking-websites-uk/",
    "guides/cheap-family-holidays-spain/",
    "guides/cheap-holidays-antalya-from-uk/",
    "guides/cheap-holidays-greece-from-uk/",
    "guides/cheap-holidays-lanzarote-from-uk/",
    "guides/cheap-holidays-mauritius-from-uk/",
    "guides/cheap-holidays-spain-from-uk/",
    "guides/cheap-holidays-turkey-all-inclusive-from-uk/",
    "guides/cheap-holidays-zante-from-uk/",
    "guides/cheapest-holidays-under-500-uk/",
    "guides/greece-vs-turkey-all-inclusive/",
    "guides/prague-vs-budapest/",
    "guides/spain-vs-greece-holidays/",
    "guides/spain-vs-portugal-holidays/",
    "guides/turkey-vs-spain-all-inclusive/",
    "guides/tenerife-vs-antalya-winter-sun/",
    "how-we-research/",
    "planner/",
    "privacy/",
    "terms/",
}

pages = [
    ("", "daily", "1.0"),
    ("guides/", "weekly", "0.9"),
    ("make-money-for-travel/", "weekly", "0.9"),
    ("videos/", "weekly", "0.9"),
    ("planner/", "monthly", "0.7"),
    ("calculator/", "monthly", "0.7"),
    ("contact/", "monthly", "0.5"),
    ("privacy/", "monthly", "0.5"),
    ("terms/", "monthly", "0.5"),
    ("how-we-research/", "monthly", "0.6"),
    ("editorial-standards/", "monthly", "0.6"),
    ("affiliate-disclosure/", "monthly", "0.6"),
    ("about/", "monthly", "0.5"),
]

# Pages updated during current rollout; use fresher lastmod.
recent_lastmod_paths = {
    "guides/best-travel-booking-websites-uk/",
    "guides/cheap-all-inclusive-holidays-uk/",
    "guides/cheap-holidays-algarve-from-uk/",
    "guides/cheap-holidays-bulgaria-from-uk/",
    "guides/cheap-holidays-greece-from-uk/",
    "guides/cheap-holidays-italy-from-uk/",
    "guides/cheap-holidays-portugal-from-uk/",
    "guides/cheap-holidays-spain-from-uk/",
    "guides/cheap-holidays-tenerife-from-uk/",
    "guides/cheap-holidays-turkey-from-uk/",
    "guides/cheapest-holiday-destinations-from-uk-2026/",
    "guides/cheapest-holidays-under-500-uk/",
    "guides/cheapest-winter-sun-destinations-uk/",
}

current_money_lastmod_paths = {
    "make-money-for-travel/affiliate-marketing-for-travel-fund-uk.html",
    "make-money-for-travel/ai-tools-vs-side-hustles-for-travel.html",
    "make-money-for-travel/best-ai-tools-to-make-money-for-travel.html",
    "make-money-for-travel/best-ai-tools-to-make-money-online-2026-uk.html",
    "make-money-for-travel/best-side-hustles-uk-2026-ranked.html",
    "make-money-for-travel/content-writing-side-hustle-for-travel.html",
    "make-money-for-travel/delivery-apps-to-save-for-holiday-uk.html",
    "make-money-for-travel/earn-500-fast-uk-for-travel.html",
    "make-money-for-travel/freelance-jobs-for-travel-uk.html",
    "make-money-for-travel/freelancing-for-travel-income.html",
    "make-money-for-travel/how-to-make-500-for-travel-2026.html",
    "make-money-for-travel/how-to-make-money-for-travel-uk.html",
    "make-money-for-travel/how-to-make-money-online-uk-beginners-2026.html",
    "make-money-for-travel/make-money-fast-for-holiday-uk.html",
    "make-money-for-travel/make-money-online-uk-beginners-for-travel.html",
    "make-money-for-travel/no-experience-remote-work-for-travel-uk.html",
    "make-money-for-travel/online-tutoring-to-fund-travel-uk.html",
    "make-money-for-travel/passive-income-for-travel-beginners-uk.html",
    "make-money-for-travel/passive-income-ideas-for-travel-2026.html",
    "make-money-for-travel/pet-sitting-and-dog-walking-for-travel-money-uk.html",
    "make-money-for-travel/print-on-demand-for-travel-fund-uk.html",
    "make-money-for-travel/remote-jobs-to-fund-travel.html",
    "make-money-for-travel/remote-jobs-to-travel-the-world-uk.html",
    "make-money-for-travel/reselling-items-to-fund-travel-uk.html",
    "make-money-for-travel/sell-digital-products-for-travel-income-uk.html",
    "make-money-for-travel/side-hustles-to-fund-holidays-uk-2026.html",
    "make-money-for-travel/side-hustles-to-pay-for-holidays.html",
    "make-money-for-travel/side-hustles-vs-freelancing-for-travel.html",
    "make-money-for-travel/side-hustles-vs-passive-income-for-travel.html",
    "make-money-for-travel/social-media-management-for-travel-income-uk.html",
    "make-money-for-travel/virtual-assistant-work-for-travel-uk.html",
    "make-money-for-travel/weekend-side-hustles-for-travel-fund-uk.html",
}

# Get all guides
guides = []
for d in os.listdir("guides"):
    if os.path.isdir(os.path.join("guides", d)):
        path = f"guides/{d}/"
        if path not in focus_pages and d != "spain-budget-holidays":
            guides.append(path)

guides.sort()

money_pages = []
money_dir = "make-money-for-travel"
if os.path.isdir(money_dir):
    for name in os.listdir(money_dir):
        full = os.path.join(money_dir, name)
        if not os.path.isfile(full) or not name.endswith(".html"):
            continue
        if name == "index.html":
            continue
        money_pages.append(f"make-money-for-travel/{name}")

money_pages.sort()

video_pages = []
video_dir = "videos"
if os.path.isdir(video_dir):
    for name in os.listdir(video_dir):
        full = os.path.join(video_dir, name)
        if not os.path.isfile(full) or not name.endswith(".html"):
            continue
        if name == "index.html":
            continue
        video_pages.append(f"videos/{name}")

video_pages.sort()

taste_pages = []
taste_data_path = os.path.join("data", "taste-the-world-recipes.json")
if os.path.isfile(taste_data_path):
    with open(taste_data_path, encoding="utf-8") as f:
        taste_data = json.load(f)
    taste_pages.append("taste-the-world/")
    for cuisine in taste_data.get("cuisines", []):
        taste_pages.append(f"taste-the-world/{cuisine['slug']}/")
    for recipe in taste_data.get("recipes", []):
        taste_pages.append(f"taste-the-world/{recipe['cuisineSlug']}/{recipe['slug']}/")
elif os.path.isdir("taste-the-world"):
    for root, _, files in os.walk("taste-the-world"):
        if "index.html" not in files:
            continue
        rel = os.path.relpath(root, ".").replace(os.sep, "/")
        taste_pages.append(f"{rel}/")

taste_pages = sorted(set(taste_pages))

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n'

# Main pages
for path, freq, prio in pages:
    lastmod = "2026-06-23" if path in current_sprint_lastmod_paths else "2026-03-24"
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>{lastmod}</lastmod>\n<changefreq>{freq}</changefreq>\n<priority>{prio}</priority>\n</url>\n\n'

# Focus pages
for path in focus_pages:
    lastmod = "2026-06-23" if path in current_sprint_lastmod_paths else ("2026-04-20" if path in recent_lastmod_paths else "2026-03-24")
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>{lastmod}</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.9</priority>\n</url>\n\n'

# Other guides
for path in guides:
    lastmod = "2026-06-23" if path in current_sprint_lastmod_paths else ("2026-04-20" if path in recent_lastmod_paths else "2026-03-17")
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>{lastmod}</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.8</priority>\n</url>\n\n'

# Money pages
for path in money_pages:
    lastmod = "2026-06-23" if path in current_money_lastmod_paths else "2026-04-20"
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>{lastmod}</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.8</priority>\n</url>\n\n'

# Video pages
for path in video_pages:
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>2026-04-22</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.8</priority>\n</url>\n\n'

# Taste the World recipe pages
for path in taste_pages:
    depth = path.count("/")
    priority = "0.9" if depth <= 2 else "0.8"
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>2026-06-23</lastmod>\n<changefreq>weekly</changefreq>\n<priority>{priority}</priority>\n</url>\n\n'

sitemap += '</urlset>\n'

with open("sitemap.xml", "w") as f:
    f.write(sitemap)
