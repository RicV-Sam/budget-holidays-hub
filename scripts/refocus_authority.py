"""Apply the site authority refocus safely and idempotently.

This is a mechanical migration:
- keep off-topic archive pages accessible but remove them from indexing;
- remove unsupported FAQPage JSON-LD from legacy outbound travel guides;
- add an honest evidence-status notice to outbound travel articles.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOINDEX_DIRS = ("make-money-for-travel", "taste-the-world", "videos")
ARCHIVE_HREF = re.compile(
    r'href=["\']/(?:make-money-for-travel|taste-the-world|videos)(?:/[^"\']*)?["\']',
    flags=re.I,
)
STATUS_MARKER = 'class="content-status"'
STATUS_NOTICE = """
<aside class="content-status" aria-label="Guide review status">
  <strong>Planning estimates, not live prices.</strong>
  This legacy holidays-from-the-UK guide is being checked against our current
  evidence standard. Reconfirm fares, entry rules and availability before
  booking. <a href="/how-we-research/">How we review guides</a>.
</aside>
""".strip()
SUBSTANTIVELY_REVIEWED_GUIDES = {
    "guides/greece-vs-turkey-all-inclusive/index.html",
}


def add_noindex(html: str) -> str:
    robots_pattern = re.compile(
        r'<meta\b(?=[^>]*\bname=["\']robots["\'])[^>]*>',
        flags=re.I,
    )
    if robots_pattern.search(html):
        return robots_pattern.sub(
            '<meta name="robots" content="noindex, follow">',
            html,
            count=1,
        )

    viewport_pattern = re.compile(
        r'(<meta\b(?=[^>]*\bname=["\']viewport["\'])[^>]*>)',
        flags=re.I,
    )
    if viewport_pattern.search(html):
        return viewport_pattern.sub(
            r'\1\n<meta name="robots" content="noindex, follow">',
            html,
            count=1,
        )

    return html.replace(
        "<head>",
        '<head>\n<meta name="robots" content="noindex, follow">',
        1,
    )


def remove_faq_schema(html: str) -> str:
    pattern = re.compile(
        r'\s*<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>'
        r'(?P<body>[\s\S]*?)</script>',
        flags=re.I,
    )

    def replace(match: re.Match[str]) -> str:
        if re.search(r'"@type"\s*:\s*"FAQPage"', match.group("body"), flags=re.I):
            return ""
        return match.group(0)

    return pattern.sub(replace, html)


def add_status_notice(html: str) -> str:
    if STATUS_MARKER in html:
        return html

    updated_pattern = re.compile(
        r'(<p\b[^>]*class=["\'][^"\']*(?:last-updated|meta)[^"\']*["\'][^>]*>'
        r'[\s\S]*?Last updated:[\s\S]*?</p>)',
        flags=re.I,
    )
    if updated_pattern.search(html):
        return updated_pattern.sub(
            lambda match: f"{match.group(1)}\n{STATUS_NOTICE}",
            html,
            count=1,
        )

    article_pattern = re.compile(r'(<article\b[^>]*>)', flags=re.I)
    return article_pattern.sub(
        lambda match: f"{match.group(1)}\n{STATUS_NOTICE}",
        html,
        count=1,
    )


def remove_archive_links(html: str) -> str:
    """Remove promotional archive links from pages that remain indexable."""

    paragraph_pattern = re.compile(r"<p\b[^>]*>[\s\S]*?</p>", flags=re.I)
    list_item_pattern = re.compile(r"<li\b[^>]*>[\s\S]*?</li>", flags=re.I)
    anchor_pattern = re.compile(
        r'<a\b(?=[^>]*'
        r'href=["\']/(?:make-money-for-travel|taste-the-world|videos)'
        r'(?:/[^"\']*)?["\'])[^>]*>(?P<label>[\s\S]*?)</a>',
        flags=re.I,
    )

    def remove_short_promo(match: re.Match[str]) -> str:
        block = match.group(0)
        if not ARCHIVE_HREF.search(block):
            return block
        plain = re.sub(r"<[^>]+>", " ", block)
        plain = re.sub(r"\s+", " ", plain).strip().lower()
        promo_terms = (
            "afford",
            "fund",
            "income",
            "make money",
            "side hustle",
            "remote job",
            "video guide",
            "recipe",
        )
        if len(plain) < 600 and any(term in plain for term in promo_terms):
            return ""
        return block

    html = paragraph_pattern.sub(remove_short_promo, html)
    html = list_item_pattern.sub(remove_short_promo, html)
    return anchor_pattern.sub(lambda match: match.group("label"), html)


def write_if_changed(path: Path, updated: str) -> bool:
    current = path.read_text(encoding="utf-8")
    if current == updated:
        return False
    path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    noindexed = 0
    faq_removed = 0
    statuses_added = 0

    for directory in NOINDEX_DIRS:
        for path in (ROOT / directory).rglob("*.html"):
            html = path.read_text(encoding="utf-8")
            updated = add_noindex(html)
            if write_if_changed(path, updated):
                noindexed += 1

    guides_root = ROOT / "guides"
    for path in guides_root.rglob("index.html"):
        if path == guides_root / "index.html":
            continue
        html = path.read_text(encoding="utf-8")
        if "Redirecting..." in html:
            continue

        without_faq = remove_faq_schema(html)
        if without_faq != html:
            faq_removed += 1

        rel = path.relative_to(ROOT).as_posix()
        if rel in SUBSTANTIVELY_REVIEWED_GUIDES:
            updated = without_faq
        else:
            updated = add_status_notice(without_faq)
            if STATUS_MARKER not in without_faq and STATUS_MARKER in updated:
                statuses_added += 1
        write_if_changed(path, updated)

    archive_links_cleaned = 0
    for path in ROOT.rglob("*.html"):
        if any(part in {"_site", "templates", *NOINDEX_DIRS} for part in path.parts):
            continue
        html = path.read_text(encoding="utf-8")
        updated = remove_archive_links(html)
        if write_if_changed(path, updated):
            archive_links_cleaned += 1

    print(
        f"Noindexed {noindexed} archive pages; removed FAQ schema from "
        f"{faq_removed} guides; added status notices to {statuses_added} guides; "
        f"cleaned archive promotions from {archive_links_cleaned} indexable pages."
    )


if __name__ == "__main__":
    main()
