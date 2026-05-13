from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def iter_public_pages():
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".") or rel.startswith("templates/"):
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

    print(f"Pages scanned: {len(list(iter_public_pages()))}")
    if not issues:
        print("SEO consistency audit passed.")
        return

    print(f"Issues found: {len(issues)}")
    for rel, msg in issues[:200]:
        print(f"- {rel}: {msg}")


if __name__ == "__main__":
    main()
