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

## Bing And IndexNow Submission

After publishing important URL changes, refresh the sitemap and dry-run search submissions. By default, both submission scripts only use sitemap URLs with recent `lastmod` values:

```powershell
npm run generate:sitemap
npm run submit:indexnow -- --dry-run
npm run submit:bing -- --dry-run
```

To submit to IndexNow, run:

```powershell
npm run submit:indexnow
```

To use the Bing Webmaster URL Submission API, set `BING_WEBMASTER_API_KEY` first, then run:

```powershell
npm run submit:bing
```

Use `--all` only for a deliberate full-sitemap resubmission:

```powershell
npm run submit:bing -- --all
npm run submit:indexnow -- --all
```
