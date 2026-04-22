# Budget Holidays Hub

## Local SEO QA

Run the local crawlability and SEO audit before publishing content batches:

```powershell
python scripts/seo_audit.py
```

To also validate YouTube embeds through oEmbed:

```powershell
python scripts/seo_audit.py --check-videos
```

The audit checks public HTML pages for titles, meta descriptions, canonicals, H1 count, missing image alt text, JSON-LD validity, broken internal links, sitemap coverage, money-page inlinks, and shared money-page nav/footer.
