import os
import datetime

base_url = "https://budgetholidayshub.com"
focus_pages = [
    "guides/cheap-holidays-spain-from-uk/",
    "guides/best-travel-booking-websites-uk/",
    "guides/greece-vs-turkey-all-inclusive/",
    "guides/cheap-holidays-turkey-all-inclusive-from-uk/",
    "guides/cheap-holidays-mauritius-from-uk/"
]

pages = [
    ("", "daily", "1.0"),
    ("guides/", "weekly", "0.9"),
    ("make-money-for-travel/", "weekly", "0.9"),
    ("how-we-research/", "monthly", "0.6"),
    ("editorial-standards/", "monthly", "0.6"),
    ("affiliate-disclosure/", "monthly", "0.6"),
    ("about/", "monthly", "0.5"),
    ("contact/", "monthly", "0.5"),
    ("privacy/", "monthly", "0.5"),
    ("terms/", "monthly", "0.5"),
]

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

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n'

# Main pages
for path, freq, prio in pages:
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>2026-03-24</lastmod>\n<changefreq>{freq}</changefreq>\n<priority>{prio}</priority>\n</url>\n\n'

# Focus pages
for path in focus_pages:
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>2026-03-24</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.9</priority>\n</url>\n\n'

# Other guides
for path in guides:
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>2026-03-17</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.8</priority>\n</url>\n\n'

# Money pages
for path in money_pages:
    sitemap += f'<url>\n<loc>{base_url}/{path}</loc>\n<lastmod>2026-04-20</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.8</priority>\n</url>\n\n'

sitemap += '</urlset>\n'

with open("sitemap.xml", "w") as f:
    f.write(sitemap)
