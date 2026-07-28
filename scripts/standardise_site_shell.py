from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NAV_PATTERN = re.compile(
    r'<nav\s+aria-label="Main navigation"\s+class="site-nav">.*?</nav>',
    flags=re.IGNORECASE | re.DOTALL,
)


def iter_public_html() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*.html"):
        relative = path.relative_to(ROOT).as_posix()
        if relative.startswith(("_site/", "templates/", ".")):
            continue
        paths.append(path)
    return paths


def nav_for(relative: str) -> str:
    current = "home"
    if relative.startswith("visit-uk/"):
        current = "visit"
    elif relative.startswith("guides/"):
        current = "outbound"
    elif relative.startswith("planner/"):
        current = "planner"
    elif relative.startswith("how-we-research/"):
        current = "research"
    elif relative.startswith("about/"):
        current = "about"
    elif relative != "index.html":
        current = ""

    def link(href: str, label: str, key: str) -> str:
        active = ' aria-current="page"' if current == key else ""
        return f'      <a href="{href}"{active}>{label}</a>'

    return "\n".join(
        [
            '<nav aria-label="Main navigation" class="site-nav">',
            '  <div class="nav-inner">',
            '    <a href="/" class="brand"><span class="brand-icon" aria-hidden="true">&#9992;</span>Budget Holidays Hub</a>',
            '    <div class="nav-links">',
            link("/", "Home", "home"),
            link("/visit-uk/", "Visit the UK", "visit"),
            link("/guides/", "Holidays from the UK", "outbound"),
            link("/planner/", "Planner", "planner"),
            link("/how-we-research/", "Research", "research"),
            link("/about/", "About", "about"),
            "    </div>",
            "  </div>",
            "</nav>",
        ]
    )


def main() -> None:
    changed = 0
    missing_nav: list[str] = []

    replacements = {
        "Â£": "£",
        "âœˆ": "✈",
        "â†\x90": "←",
        "Â©": "©",
        "â€¢": "•",
    }

    for path in iter_public_html():
        relative = path.relative_to(ROOT).as_posix()
        html = path.read_text(encoding="utf-8")
        updated = re.sub(r'<html\s+lang="en">', '<html lang="en-GB">', html, count=1)
        if 'rel="icon"' not in updated:
            updated = re.sub(
                r'(<meta\s+charset="[^"]+"\s*/?>)',
                r'\1\n<link rel="icon" href="/assets/images/logo.svg" type="image/svg+xml">',
                updated,
                count=1,
                flags=re.IGNORECASE,
            )
        updated = re.sub(
            r'<script\s+src="(/assets/js/[^"]+)"\s*></script>',
            r'<script src="\1" defer></script>',
            updated,
        )

        if NAV_PATTERN.search(updated):
            updated = NAV_PATTERN.sub(nav_for(relative), updated, count=1)
        else:
            missing_nav.append(relative)

        for broken, fixed in replacements.items():
            updated = updated.replace(broken, fixed)

        if updated != html:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed += 1

    print(f"Standardised {changed} public HTML files.")
    if missing_nav:
        print("Pages without a standard main navigation:")
        for relative in missing_nav:
            print(f"- {relative}")


if __name__ == "__main__":
    main()
