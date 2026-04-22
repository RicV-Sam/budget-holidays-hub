import argparse
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


BASE_URL = "https://budgetholidayshub.com"
DEFAULT_ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git", "test-results"}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self._in_title = False
        self.description = None
        self.canonical = None
        self.robots = ""
        self.h1_count = 0
        self.image_count = 0
        self.images_missing_alt = 0
        self.json_ld = []
        self._in_json_ld = False
        self._json_ld_buffer = ""
        self.hrefs = []
        self.has_site_nav = False
        self.has_site_footer = False

    def handle_starttag(self, tag, attrs):
        attr = {key.lower(): value for key, value in attrs}
        class_name = attr.get("class") or ""

        if tag == "title":
            self._in_title = True
        elif tag == "meta" and (attr.get("name") or "").lower() == "description":
            self.description = attr.get("content") or ""
        elif tag == "meta" and (attr.get("name") or "").lower() == "robots":
            self.robots = attr.get("content") or ""
        elif tag == "link" and (attr.get("rel") or "").lower() == "canonical":
            self.canonical = attr.get("href") or ""
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "img":
            self.image_count += 1
            if "alt" not in attr:
                self.images_missing_alt += 1
        elif tag == "script" and (attr.get("type") or "").lower() == "application/ld+json":
            self._in_json_ld = True
            self._json_ld_buffer = ""
        elif tag == "a" and attr.get("href"):
            self.hrefs.append(attr["href"])

        if tag == "nav" and "site-nav" in class_name:
            self.has_site_nav = True
        elif tag == "footer" and "site-footer" in class_name:
            self.has_site_footer = True

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_json_ld:
            self._json_ld_buffer += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_json_ld:
            self.json_ld.append(self._json_ld_buffer.strip())
            self._in_json_ld = False


def html_files(root):
    for path in root.rglob("*.html"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        yield path


def path_to_url_path(root, path):
    rel = "/" + path.relative_to(root).as_posix()
    if rel == "/index.html":
        return "/"
    if rel.endswith("/index.html"):
        return rel[:-10]
    return rel


def load_page(path):
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    return parser


def is_noindex(page):
    return "noindex" in page.robots.lower()


def internal_target(root, href):
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return None
    if not href.startswith("/"):
        return None

    clean = href.split("#", 1)[0].split("?", 1)[0]
    if not clean:
        return None

    if clean.endswith("/"):
        return root / clean.strip("/") / "index.html"
    return root / clean.strip("/")


def load_sitemap(root):
    sitemap_path = root / "sitemap.xml"
    if not sitemap_path.exists():
        return set()
    text = sitemap_path.read_text(encoding="utf-8", errors="ignore")
    locs = re.findall(r"<loc>(.*?)</loc>", text)
    paths = set()
    for loc in locs:
        parsed = urlparse(loc)
        if loc.startswith(BASE_URL):
            paths.add(parsed.path or "/")
    return paths


def check_video_oembed(video_id, timeout=20):
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return response.status == 200


def audit(root, check_videos=False):
    pages = {}
    for path in html_files(root):
        url_path = path_to_url_path(root, path)
        pages[url_path] = (path, load_page(path))

    issues = []
    public_pages = set()
    noindex_pages = set()

    for url_path, (path, page) in pages.items():
        rel = path.relative_to(root).as_posix()
        noindex = is_noindex(page)
        if noindex:
            noindex_pages.add(url_path)
        else:
            public_pages.add(url_path)

        if noindex:
            continue

        if not page.title.strip():
            issues.append(("metadata", rel, "Missing <title>."))
        if not page.description:
            issues.append(("metadata", rel, "Missing meta description."))
        if not page.canonical:
            issues.append(("metadata", rel, "Missing canonical URL."))
        if page.h1_count != 1:
            issues.append(("content", rel, f"Expected exactly one H1, found {page.h1_count}."))
        if page.images_missing_alt:
            issues.append(("accessibility", rel, f"{page.images_missing_alt} image(s) missing alt text."))

        for raw_json in page.json_ld:
            try:
                json.loads(raw_json)
            except json.JSONDecodeError as exc:
                issues.append(("schema", rel, f"Invalid JSON-LD: {exc}."))

        if url_path.startswith("/make-money-for-travel/") and url_path != "/make-money-for-travel/":
            if not page.has_site_nav:
                issues.append(("ui", rel, "Money page missing shared site nav."))
            if not page.has_site_footer:
                issues.append(("ui", rel, "Money page missing shared site footer."))
            if not page.json_ld:
                issues.append(("schema", rel, "Money page missing JSON-LD."))

    sitemap_paths = load_sitemap(root)
    for url_path in sorted(public_pages - sitemap_paths):
        if url_path.startswith("/templates/"):
            continue
        issues.append(("sitemap", url_path, "Public indexable page is missing from sitemap.xml."))
    for url_path in sorted(sitemap_paths - public_pages):
        issues.append(("sitemap", url_path, "Sitemap URL is missing or points to a noindex page."))

    for source_url, (source_path, page) in pages.items():
        if is_noindex(page):
            continue
        for href in page.hrefs:
            target = internal_target(root, href)
            if target and not target.exists():
                rel = source_path.relative_to(root).as_posix()
                issues.append(("links", rel, f"Broken internal link: {href}"))

    inlinks = {url_path: set() for url_path in pages}
    for source_url, (_, page) in pages.items():
        if is_noindex(page):
            continue
        for href in page.hrefs:
            if href.startswith("/") and not href.startswith("//"):
                clean = href.split("#", 1)[0].split("?", 1)[0]
                if clean in inlinks:
                    inlinks[clean].add(source_url)

    for url_path in sorted(public_pages):
        if url_path.startswith("/make-money-for-travel/") and url_path != "/make-money-for-travel/":
            if len(inlinks.get(url_path, set())) < 2:
                issues.append(("links", url_path, "Money page has fewer than 2 internal inlinks."))

    video_ids = set()
    for _, (path, _) in pages.items():
        text = path.read_text(encoding="utf-8", errors="ignore")
        video_ids.update(re.findall(r"youtube\.com/embed/([A-Za-z0-9_-]{11})", text))

    video_results = []
    if check_videos:
        for video_id in sorted(video_ids):
            try:
                ok = check_video_oembed(video_id)
            except Exception as exc:  # Network failures should be visible in audit output.
                ok = False
                issues.append(("video", video_id, f"oEmbed validation failed: {exc}"))
            video_results.append((video_id, ok))
            if not ok:
                issues.append(("video", video_id, "oEmbed returned a non-OK response."))

    return {
        "pages_checked": len(pages),
        "public_pages": len(public_pages),
        "noindex_pages": len(noindex_pages),
        "sitemap_urls": len(sitemap_paths),
        "videos_found": len(video_ids),
        "video_results": video_results,
        "issues": issues,
    }


def main():
    parser = argparse.ArgumentParser(description="Run local SEO and crawlability checks.")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="Repository root. Defaults to this repo.")
    parser.add_argument("--check-videos", action="store_true", help="Validate YouTube embeds via oEmbed.")
    args = parser.parse_args()

    result = audit(Path(args.root).resolve(), check_videos=args.check_videos)
    print(f"Pages checked: {result['pages_checked']}")
    print(f"Public pages: {result['public_pages']}")
    print(f"Noindex pages: {result['noindex_pages']}")
    print(f"Sitemap URLs: {result['sitemap_urls']}")
    print(f"YouTube embeds found: {result['videos_found']}")
    if result["video_results"]:
        for video_id, ok in result["video_results"]:
            status = "OK" if ok else "FAIL"
            print(f"Video oEmbed {status}: {video_id}")

    if result["issues"]:
        print("\nIssues:")
        for category, location, message in result["issues"]:
            print(f"- [{category}] {location}: {message}")
        return 1

    print("\nSEO audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
