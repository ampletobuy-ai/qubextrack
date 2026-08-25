#!/usr/bin/env python3
"""Update corporate + branch addresses across TrackPOS HTML pages."""
import os
import re

DIST = "/Users/rajeshjena/Downloads/trackpos-main-site/dist"

# Update these strings if you have exact plot/street numbers
CORPORATE = "Doddathogur Road, Electronic City, Bengalure-560100"
PURI_BRANCH = "Clark Road, Near Policeline Square, Puri — 752001, India"
BBSR_BRANCH = "K7, Ghatikia Road, Bhubaneswar, Khordha — 751029, India"

MAP_EMBED = (
    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3113.107376246531!2d77.648276!3d12.839937!"
    "2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae14fcf2392f27%3A0x553e43c8b8438fa5!"
    "2sElectronic%20City%2C%20Bengaluru%2C%20Karnataka%20560100!5e0!3m2!1sen!2sin!4v1700000000000!"
    "5m2!1sen!2sin"
)

OFFICES_INLINE = ""

OFFICES_CONTACT = f"""<div class="trackpos-offices !text-[0.9rem] !leading-[1.65] !text-[#60697b]">
  <p class="!mb-3"><strong class="!text-[#343f52]">Branch — Puri</strong><br>{PURI_BRANCH}</p>
  <p class="!mb-0"><strong class="!text-[#343f52]">Branch — Bhubaneswar</strong><br>{BBSR_BRANCH}</p>
</div>"""

OFFCANVAS = ""  # branch/corporate addresses only in page footer (FOOTER)

FOOTER = f"""<address class="trackpos-offices-footer xl:!pr-20 xxl:!pr-28 not-italic !leading-[inherit] block !mb-4">
  <span class="block"><strong>Corporate Office:</strong><br>Doddathogur Road, Electronic City, Bengalure-560100</span>
</address>"""

FOOTER_MOBILE = ""

ABOUT_SINGLE = ""

PAGES = [
    "index.html",
    "contact.html",
    "about.html",
    "pricing.html",
    "terms.html",
]

OLD_FOOTER = '<address class="xl:!pr-20 xxl:!pr-28 not-italic !leading-[inherit] block !mb-4">Serving businesses all over India</address>'
OLD_OFFCANVAS = '<address class="not-italic !leading-[inherit] !mb-[1rem]">Serving businesses all over India</address>'
OLD_OFFCANVAS_SP = '<address class=" not-italic !leading-[inherit] !mb-[1rem]"> Serving businesses all over India </address>'


def patch_file(path):
    with open(path, encoding="utf-8") as f:
        c = f.read()
    orig = c

    c = c.replace(OLD_FOOTER, FOOTER)
    c = c.replace(OLD_OFFCANVAS, OFFCANVAS)
    c = c.replace(OLD_OFFCANVAS_SP, OFFCANVAS)

    if "contact.html" in path:
        c = re.sub(
            r"<h5 class=\"!mb-1\">Location</h5>\s*"
            r"<address class=\"not-italic !leading-\[inherit\] !mb-0\">.*?</address>",
            f"<h5 class=\"!mb-1\">Our Offices</h5>\n                        {OFFICES_CONTACT}",
            c,
            count=1,
            flags=re.DOTALL,
        )
        c = re.sub(
            r'<iframe src="[^"]*" title="TrackPOSSystem[^"]*"[^>]*></iframe>',
            f'<iframe src="{MAP_EMBED}" title="TrackPOSSystem — Office locations" style="width:100%; height: 100%; border:0" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
            c,
            count=1,
        )
        c = c.replace(
            'content="Contact TrackPOSSystem for sales, support, free demo or 14-day trial. Serving businesses all over India. sales@trackpossystem.com, support@trackpossystem.com, +91-9348457123."',
            "content=\"Contact TrackPOSSystem — corporate office Electronic City, Bengalure; branches in Puri & Bhubaneswar. sales@trackpossystem.com, +91-9348457123.\"",
        )

    if "about.html" in path:
        c = c.replace(
            '<address class=" not-italic !leading-[inherit] !mb-4">Serving businesses all over India</address>',
            ABOUT_SINGLE,
        )
        c = c.replace(
            "Trusted by businesses all over India. Free 14-day trial.",
            "Trusted by businesses all over India. Corporate office in Electronic City, Bengaluru; branches in Bhubaneswar and Puri. Free 14-day trial.",
        )

    if c != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print("Updated", os.path.basename(path))
    else:
        print("No changes", os.path.basename(path))


for name in PAGES:
    patch_file(os.path.join(DIST, name))

# Mobile offcanvas footer on pages that still have legacy address text
for name in PAGES:
    path = os.path.join(DIST, name)
    with open(path, encoding="utf-8") as f:
        c = f.read()
    if "offcanvas-footer" in c and "Puri Branch" not in c:
        c = c.replace(
            "<br> +91-9348457123 <br>",
            f"<br> +91-9348457123{FOOTER_MOBILE}<br>",
            1,
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print("Mobile footer:", name)

print("Done.")
