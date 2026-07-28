from __future__ import annotations

import re
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / "assets" / "images"


def public_html_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.html"):
        relative = path.relative_to(ROOT).as_posix()
        if relative.startswith(("_site/", "templates/", ".")):
            continue
        files.append(path)
    return files


def main() -> None:
    original_bytes = 0
    optimized_bytes = 0
    converted = 0

    for source in sorted(IMAGE_DIR.glob("*.jpg")):
        destination = source.with_suffix(".webp")
        with Image.open(source) as image:
            image = ImageOps.exif_transpose(image).convert("RGB")
            image.save(destination, "WEBP", quality=78, method=6, optimize=True)
        original_bytes += source.stat().st_size
        optimized_bytes += destination.stat().st_size
        converted += 1

    image_src = re.compile(
        r'(?P<prefix><img\b[^>]*\bsrc=")/assets/images/(?P<name>[^"]+)\.jpg(?P<suffix>")',
        flags=re.IGNORECASE,
    )
    files_changed = 0

    for path in public_html_files():
        html = path.read_text(encoding="utf-8")
        updated = image_src.sub(
            lambda match: (
                f'{match.group("prefix")}/assets/images/'
                f'{match.group("name")}.webp{match.group("suffix")}'
            ),
            html,
        )
        if updated != html:
            path.write_text(updated, encoding="utf-8", newline="\n")
            files_changed += 1

    stylesheet = ROOT / "assets" / "css" / "style.css"
    css = stylesheet.read_text(encoding="utf-8")
    updated_css = re.sub(
        r"(?P<prefix>url\(['\"]?/assets/images/)(?P<name>[^)'\"?]+)\.jpg(?P<suffix>['\"]?\))",
        r"\g<prefix>\g<name>.webp\g<suffix>",
        css,
        flags=re.IGNORECASE,
    )
    if updated_css != css:
        stylesheet.write_text(updated_css, encoding="utf-8", newline="\n")
        files_changed += 1

    saving = original_bytes - optimized_bytes
    percent = (saving / original_bytes * 100) if original_bytes else 0
    print(
        f"Converted {converted} JPEGs to WebP; "
        f"saved {saving / 1024:.0f} KiB ({percent:.1f}%)."
    )
    print(f"Updated image references in {files_changed} files.")


if __name__ == "__main__":
    main()
