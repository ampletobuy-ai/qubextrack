#!/usr/bin/env python3
"""Replace site header/nav on all pages with the homepage header (nav + info offcanvas)."""
import re
from pathlib import Path

DIST = Path(__file__).resolve().parent
INDEX = DIST / "index.html"

SKIP = {"index.html", "sandbox-index-backup.html"}

PAGES = [
    "jewellery-pos-software.html",
    "restaurant-pos-software.html",
    "hotel-management-software.html",
    "retail-billing-software.html",
    "pharmacy-pos-software.html",
    "supermarket-pos-software.html",
    "about.html",
    "contact.html",
    "terms.html",
    "pricing.html",
]


def build_standard_header(index_html: str) -> str:
    nav_m = re.search(
        r'<nav class="navbar navbar-expand-lg classic transparent navbar-light">.*?</nav>\s*<!-- /\.navbar -->',
        index_html,
        re.DOTALL,
    )
    offcanvas_m = re.search(
        r'<div class="offcanvas offcanvas-end text-inverse !text-\[#cacaca\] opacity-100" id="offcanvas-info".*?</div>\s*<!-- /\.offcanvas -->',
        index_html,
        re.DOTALL,
    )
    if not nav_m or not offcanvas_m:
        raise RuntimeError("Could not extract nav or offcanvas-info from index.html")
    return (
        '    <header class="relative wrapper !bg-[#f5f5ff]">\n'
        f"      {nav_m.group(0)}\n"
        f"      {offcanvas_m.group(0)}\n"
        "    </header>\n"
        "    <!-- /header -->"
    )


def patch_file(path: Path, header: str) -> bool:
    text = path.read_text(encoding="utf-8")
    m = re.search(
        r'<header class="relative wrapper[^"]*">.*?</header>\s*(?:<!-- /header -->)?',
        text,
        re.DOTALL,
    )
    if not m:
        print(f"  SKIP {path.name}: header block not found")
        return False
    path.write_text(text[: m.start()] + header + text[m.end() :], encoding="utf-8")
    return True


def main() -> None:
    index_html = INDEX.read_text(encoding="utf-8")
    header = build_standard_header(index_html)

    # Fix Contact Us in offcanvas (homepage still had #)
    header = header.replace(
        'href="#">Contact Us</a>',
        'href="./contact.html">Contact Us</a>',
    )

    ok = 0
    for name in PAGES:
        path = DIST / name
        if not path.exists():
            print(f"  missing {name}")
            continue
        if patch_file(path, header):
            print(f"  patched {name}")
            ok += 1

    print(f"Done: {ok} pages updated.")


if __name__ == "__main__":
    main()
