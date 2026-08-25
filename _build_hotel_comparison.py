#!/usr/bin/env python3
"""Build hotel competitor comparison HTML from HOTEL_COMPETITOR_COMPARISON.md (section 2 only)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "HOTEL_COMPETITOR_COMPARISON.md"
PARTIAL_PATH = ROOT / "assets/partials/hotel-competitor-comparison.html"
PAGE_PATH = ROOT / "hotel-management-software.html"

SECTION_START = "## 2. Full feature comparison"
SECTION_END = "## 3."


def extract_section(md: str) -> str:
    start = md.find(SECTION_START)
    if start < 0:
        raise SystemExit(f"Missing {SECTION_START}")
    end = md.find(SECTION_END, start + len(SECTION_START))
    if end < 0:
        raise SystemExit(f"Missing {SECTION_END}")
    return md[start:end].strip()


def escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def inline_format(s: str) -> str:
    s = escape(s.strip())
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
    return s


def is_table_sep(line: str) -> bool:
    return bool(re.match(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$", line.strip()))


def parse_table(lines: list[str], i: int):
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        if not is_table_sep(lines[i]):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            rows.append(cells)
        i += 1
    return rows, i


def cell_content(c: str) -> str:
    c = c.strip()
    if re.fullmatch(r"[✅⚠️❌](?:\s*/\s*[✅⚠️❌])?", c):
        sym = c.split("/")[0].strip()
        pill = {"✅": "yes", "⚠️": "partial", "❌": "no"}.get(sym, "partial")
        return f'<span class="trackpos-compare-pill trackpos-compare-pill--{pill}">{escape(c)}</span>'
    return inline_format(c)


def render_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    header = rows[0]
    body = rows[1:]
    trackpos_col = next((j for j, c in enumerate(header) if c.strip() == "TrackPOS"), None)
    ths = []
    for j, c in enumerate(header):
        cls = "trackpos-compare-col--us" if j == trackpos_col else ""
        ths.append(f'<th scope="col" class="{cls}">{inline_format(c)}</th>')
    trs = []
    for row in body:
        tds = []
        for j, c in enumerate(row):
            cls = []
            if j == 0:
                cls.append("trackpos-compare-feature")
            if j == trackpos_col:
                cls.append("trackpos-compare-col--us")
            tds.append(f'<td class="{" ".join(cls)}">{cell_content(c)}</td>')
        trs.append("<tr>" + "".join(tds) + "</tr>")
    return (
        '<div class="trackpos-security-compare trackpos-compare-wrap">'
        '<table class="trackpos-security-table trackpos-compare-table">'
        f'<thead><tr>{"".join(ths)}</tr></thead>'
        f"<tbody>{''.join(trs)}</tbody></table></div>"
    )


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    html_parts = ['<div class="trackpos-compare-content">']
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            if re.match(r"^2\.\s*Full feature comparison\s*$", title, re.I):
                i += 1
                continue
            html_parts.append(f'<h2 class="trackpos-compare-h2">{inline_format(title)}</h2>')
            i += 1
            continue
        if stripped.startswith("### "):
            html_parts.append(f'<h4 class="trackpos-compare-h4">{inline_format(stripped[4:])}</h4>')
            i += 1
            continue
        if stripped == "---":
            html_parts.append('<hr class="trackpos-compare-divider">')
            i += 1
            continue
        if stripped.startswith("|") and not is_table_sep(stripped):
            rows, i = parse_table(lines, i)
            html_parts.append(render_table(rows))
            continue
        if stripped.startswith("**Why TrackPOS wins:**") or (
            stripped.startswith("**") and "Why TrackPOS" in stripped
        ):
            para = [stripped]
            i += 1
            while i < len(lines):
                nxt = lines[i].strip()
                if not nxt or nxt.startswith("#") or nxt.startswith("|") or nxt == "---":
                    break
                para.append(nxt)
                i += 1
            html_parts.append(f'<p class="trackpos-compare-p trackpos-compare-win">{inline_format(" ".join(para))}</p>')
            continue
        para = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith("#") or nxt.startswith("|") or nxt == "---":
                break
            para.append(nxt)
            i += 1
        html_parts.append(f'<p class="trackpos-compare-p">{inline_format(" ".join(para))}</p>')
    html_parts.append("</div>")
    return "\n".join(html_parts)


MODAL_BLOCK = """        <!-- Competitor comparison modal (hotel) -->
        <template id="hotel-competitor-comparison-template">
{html}
        </template>
        <div class="trackpos-modal trackpos-modal--wide" id="hotel-competitor-comparison" aria-hidden="true" data-trackpos-modal-template="hotel-competitor-comparison-template">
          <div class="trackpos-modal__overlay" aria-hidden="true"></div>
          <div class="trackpos-modal__dialog" role="dialog" aria-modal="true" aria-labelledby="hotel-competitor-comparison-title">
            <div class="trackpos-modal__header">
              <h4 class="trackpos-modal__title" id="hotel-competitor-comparison-title">Full feature comparison</h4>
              <button type="button" class="trackpos-modal__close" aria-label="Close" data-trackpos-modal-close>&times;</button>
            </div>
            <div class="trackpos-modal__body" data-trackpos-modal-content></div>
          </div>
        </div>
        <!-- /competitor comparison modal -->
"""

CTA_BLOCK = """        <div class="flex flex-wrap mx-[-15px] !mb-10">
          <div class="w-full flex-[0_0_auto] !px-[15px] max-w-full flex justify-center">
            <a href="#" class="trackpos-compare-cta" data-trackpos-modal-open="#hotel-competitor-comparison" aria-label="Open full hotel PMS feature comparison">
              <span class="trackpos-compare-cta__glow" aria-hidden="true"></span>
              <span class="trackpos-compare-cta__icon" aria-hidden="true"><i class="uil uil-chart-bar"></i></span>
              <span class="trackpos-compare-cta__content">
                <span class="trackpos-compare-cta__eyebrow">Feature-wise comparison</span>
                <span class="trackpos-compare-cta__title">Why TrackPOS beats typical hotel PMS apps</span>
              </span>
              <span class="trackpos-compare-cta__action">
                <span>View full comparison</span>
                <i class="uil uil-arrow-right" aria-hidden="true"></i>
              </span>
            </a>
          </div>
        </div>
"""


def inject_into_page(html: str) -> None:
    page = PAGE_PATH.read_text(encoding="utf-8")
    if "hotel-competitor-comparison-template" in page:
        start = page.find('<template id="hotel-competitor-comparison-template">')
        content_start = start + len('<template id="hotel-competitor-comparison-template">')
        end = page.find("</template>", content_start)
        page = page[:content_start] + "\n" + html + "\n        " + page[end:]
    else:
        anchor = "\n        </section>\n\n\n\n        <div class=\"flex flex-wrap mx-[-15px] !mt-12\">"
        if anchor not in page:
            anchor = "\n        </section>\n\n        <div class=\"flex flex-wrap mx-[-15px] !mt-12\">"
        if anchor not in page:
            raise SystemExit("Modal insert anchor not found")
        page = page.replace(anchor, "\n        </section>\n\n" + MODAL_BLOCK.format(html=html) + anchor, 1)

    if "trackpos-compare-cta" not in page.split("Platform modules")[0]:
        page = page.replace(
            '    <section class="wrapper !bg-[#f5f5ff]">\n      <div class="container py-16 xl:!py-20">\n        <div class="flex flex-wrap mx-[-15px] items-end !mb-10">',
            '    <section class="wrapper !bg-[#f5f5ff]">\n      <div class="container py-16 xl:!py-20">\n' + CTA_BLOCK + '        <div class="flex flex-wrap mx-[-15px] items-end !mb-10">',
            1,
        )

    PAGE_PATH.write_text(page, encoding="utf-8")


def main() -> None:
    md = MD_PATH.read_text(encoding="utf-8")
    section = extract_section(md)
    html = md_to_html(section)
    PARTIAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    PARTIAL_PATH.write_text(html, encoding="utf-8")
    inject_into_page(html)
    print(f"Wrote {PARTIAL_PATH} ({len(html)} chars)")
    print(f"Updated {PAGE_PATH}")


if __name__ == "__main__":
    main()
