#!/usr/bin/env python3
"""Build retail competitor comparison HTML from COMPETITOR_COMPARISON.md (section 2 only)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "COMPETITOR_COMPARISON.md"
PARTIAL_PATH = ROOT / "assets/partials/retail-competitor-comparison.html"
PAGE_PATH = ROOT / "retail-billing-software.html"

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
            # Modal header already shows this title — skip duplicate section heading.
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


def inject_into_page(html: str) -> None:
    page = PAGE_PATH.read_text(encoding="utf-8")
    start_marker = '<template id="retail-competitor-comparison-template">'
    end_marker = "</template>"
    start = page.find(start_marker)
    if start < 0:
        raise SystemExit("Template not found in retail-billing-software.html")
    content_start = start + len(start_marker)
    end = page.find(end_marker, content_start)
    if end < 0:
        raise SystemExit("Template end not found")
    new_page = page[:content_start] + "\n" + html + "\n        " + page[end:]
    PAGE_PATH.write_text(new_page, encoding="utf-8")


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
