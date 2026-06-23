from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MOJIBAKE_GUARDED_PAGES = {
    "guides/best-travel-booking-websites-uk/index.html",
    "guides/cheap-holidays-barbados-from-uk/index.html",
    "guides/cheap-holidays-bali-from-uk/index.html",
    "guides/cheap-holidays-cyprus-from-uk/index.html",
    "guides/cheap-holidays-mallorca-from-uk/index.html",
    "guides/cheap-holidays-mauritius-from-uk/index.html",
    "guides/cheap-holidays-new-york-from-uk/index.html",
    "guides/cheap-holidays-paris-from-uk/index.html",
    "guides/cheap-holidays-santorini-from-uk/index.html",
    "guides/cheap-holidays-seychelles-from-uk/index.html",
    "guides/cheap-holidays-singapore-from-uk/index.html",
    "guides/cheap-holidays-sri-lanka-from-uk/index.html",
    "guides/cheap-holidays-south-africa-from-uk/index.html",
    "guides/cheap-holidays-spain-all-inclusive-from-uk/index.html",
    "guides/cheap-holidays-thailand-from-uk/index.html",
    "guides/cheap-holidays-turkey-all-inclusive-from-uk/index.html",
    "guides/cheap-holidays-venice-from-uk/index.html",
    "guides/cheap-holidays-vietnam-from-uk/index.html",
    "make-money-for-travel/how-to-make-500-for-travel-2026.html",
}
MOJIBAKE_CODEPOINT_MARKERS = tuple(chr(codepoint) for codepoint in (0x00C2, 0x00E2, 0x00F0))
MOJIBAKE_MARKERS = ("â", "ð", "Â", "ï¸", "�")


def iter_public_pages():
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".") or rel.startswith("_site/") or rel.startswith("templates/"):
            continue
        yield path, rel


def main():
    title_seen = {}
    meta_seen = {}
    issues = []

    for file_path, rel in iter_public_pages():
        html = file_path.read_text(encoding="utf-8", errors="ignore")
        lower_html = html.lower()

        # Skip noindex pages from publish-quality reporting.
        if 'name="robots"' in lower_html and "noindex" in lower_html:
            continue

        title_match = re.search(r"<title>(.*?)</title>", html, flags=re.I | re.S)
        meta_match = re.search(
            r'<meta\b[^>]*\bname="description"[^>]*\bcontent="([^"]*)"[^>]*>',
            html,
            flags=re.I | re.S,
        ) or re.search(
            r'<meta\b[^>]*\bcontent="([^"]*)"[^>]*\bname="description"[^>]*>',
            html,
            flags=re.I | re.S,
        )
        canonical_match = re.search(
            r'<link\b[^>]*\brel="canonical"[^>]*\bhref="([^"]*)"[^>]*>',
            html,
            flags=re.I | re.S,
        ) or re.search(
            r'<link\b[^>]*\bhref="([^"]*)"[^>]*\brel="canonical"[^>]*>',
            html,
            flags=re.I | re.S,
        )
        h1_count = len(re.findall(r"<h1\b", html, flags=re.I))
        has_og = all(
            needle in html
            for needle in (
                'property="og:title"',
                'property="og:description"',
                'property="og:url"',
            )
        )
        has_twitter = all(
            needle in html
            for needle in (
                'name="twitter:title"',
                'name="twitter:description"',
            )
        )

        title = title_match.group(1).strip() if title_match else ""
        meta = meta_match.group(1).strip() if meta_match else ""

        if not title:
            issues.append((rel, "Missing <title>"))
        if not meta:
            issues.append((rel, "Missing meta description"))
        if title and len(title) > 70:
            issues.append((rel, f"Long title ({len(title)} chars)"))
        if meta and len(meta) > 170:
            issues.append((rel, f"Long meta description ({len(meta)} chars)"))
        if h1_count != 1:
            issues.append((rel, f"H1 count is {h1_count}"))
        if not has_og:
            issues.append((rel, "Missing core OG tags"))
        if not has_twitter:
            issues.append((rel, "Missing core Twitter tags"))
        if canonical_match:
            canonical = canonical_match.group(1).strip()
            if not canonical.startswith("https://budgetholidayshub.com/"):
                issues.append((rel, f"Non-standard canonical: {canonical}"))
        else:
            issues.append((rel, "Missing canonical"))

        if title:
            other = title_seen.get(title)
            if other and other != rel:
                issues.append((rel, f'Duplicate title also used by "{other}"'))
            else:
                title_seen[title] = rel

        if meta:
            other = meta_seen.get(meta)
            if other and other != rel:
                issues.append((rel, f'Duplicate meta description also used by "{other}"'))
            else:
                meta_seen[meta] = rel

        if rel.startswith("guides/") and "last updated" not in lower_html:
            issues.append((rel, "Missing visible 'Last updated' marker"))
        if re.search(r"\*\*[^*]+\*\*|__[^_]+__", html):
            issues.append((rel, "Visible Markdown formatting artifact found"))
        if rel in MOJIBAKE_GUARDED_PAGES and any(
            marker in html for marker in MOJIBAKE_MARKERS + MOJIBAKE_CODEPOINT_MARKERS
        ):
            issues.append((rel, "Visible mojibake/encoding artifact found"))

    print(f"Pages scanned: {len(list(iter_public_pages()))}")
    if not issues:
        print("SEO consistency audit passed.")
        return

    print(f"Issues found: {len(issues)}")
    for rel, msg in issues[:200]:
        print(f"- {rel}: {msg}")


if __name__ == "__main__":
    main()
