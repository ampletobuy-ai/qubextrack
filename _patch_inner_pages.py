#!/usr/bin/env python3
"""Patch contact, about, pricing with TrackPOSSystem nav, SEO, footer."""
import re
import os

DIST = "/Users/rajeshjena/Downloads/trackpos-main-site/dist"

NEW_NAV = """<ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="./index.html">Home</a></li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">Industries</a>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="./jewellery-pos-software.html">Jewellery POS</a></li>
                    <li><a class="dropdown-item" href="./restaurant-pos-software.html">Restaurant POS</a></li>
                    <li><a class="dropdown-item" href="./hotel-management-software.html">Hotel Software</a></li>
                    <li><a class="dropdown-item" href="./retail-billing-software.html">Retail Billing</a></li>
                    <li><a class="dropdown-item" href="./pharmacy-pos-software.html">Pharmacy POS</a></li>
                    <li><a class="dropdown-item" href="./supermarket-pos-software.html">Supermarket POS</a></li>
                  </ul>
                </li>
                <li class="nav-item"><a class="nav-link" href="./index.html#features">Features</a></li>
                <li class="nav-item"><a class="nav-link" href="./index.html#integrations">Integrations</a></li>
                <li class="nav-item"><a class="nav-link" href="./about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="./contact.html">Contact</a></li>
              </ul>
              <!-- /.navbar-nav -->"""

PAGES = {
    "contact.html": {
        "title": "Contact TrackPOSSystem | Book Demo & Free Trial",
        "description": "Contact TrackPOSSystem for a free demo or 14-day trial. Serving businesses all over India. Call +91-9348457123 or email sales@trackpossystem.com.",
        "canonical": "https://trackpossystem.com/contact.html",
    },
    "about.html": {
        "title": "About TrackPOSSystem | POS Software Company India",
        "description": "TrackPOSSystem builds industry-specific POS & business management software for jewellery, restaurant, hotel and retail businesses across India.",
        "canonical": "https://trackpossystem.com/about.html",
    },
    "pricing.html": {
        "title": "TrackPOSSystem Pricing | From ₹600/month",
        "description": "TrackPOSSystem pricing: Free 14-day trial. Regular plan ₹600/month, Diamond plan ₹1000/month. Cloud & offline POS for Indian businesses.",
        "canonical": "https://trackpossystem.com/pricing.html",
    },
    "terms.html": {
        "title": "Terms of Use | TrackPOSSystem",
        "description": "Terms of use for TrackPOSSystem POS and business management software.",
        "canonical": "https://trackpossystem.com/terms.html",
    },
}

def patch_file(filename, meta):
    path = os.path.join(DIST, filename)
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    c = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{meta["description"]}">', c, count=1)
    c = re.sub(r'<meta name="keywords" content="[^"]*">', '<meta name="keywords" content="TrackPOSSystem, POS software India, GST billing, free trial">', c, count=1)
    c = c.replace('<meta name="author" content="elemis">', "")
    c = re.sub(r"<title>[^<]*</title>", f"<title>{meta['title']}</title>", c, count=1)
    if meta["canonical"] not in c:
        c = c.replace("</title>", f"</title>\n  <link rel=\"canonical\" href=\"{meta['canonical']}\">", 1)

    if "trackpos.css" not in c:
        c = c.replace(
            '<link rel="stylesheet" href="./style.css">',
            '<link rel="stylesheet" href="./style.css">\n  <link rel="stylesheet" href="./assets/css/trackpos.css">',
            1,
        )

    c = re.sub(
        r'<ul class="navbar-nav">.*?</ul>\s*<!-- /\.navbar-nav -->',
        NEW_NAV,
        c,
        count=1,
        flags=re.DOTALL,
    )

    c = c.replace(
        '<h3 class="!text-white xl:!text-[1.5rem] !text-[calc(1.275rem_+_0.3vw)] !mb-0">Sandbox</h3>',
        '<h3 class="!text-white xl:!text-[1.5rem] good">TrackPOSSystem</h3>'.replace(' good">', '">'),
    )

    # Logo
    c = re.sub(
        r'<a href="\./index\.html">\s*<img[^>]*logo[^>]*>\s*(?:<img[^>]*>)?\s*</a>',
        '<a href="./index.html"><img class="trackpos-logo-img" src="./assets/img/qubextrack-logo.png?v=20260822" alt="QubexTrack"></a>',
        c,
        count=1,
        flags=re.DOTALL,
    )

    c = c.replace(
        '<a href="./contact.html" class="btn btn-sm btn-white !rounded-[50rem] hover:translate-y-[-0.15rem] hover:shadow-[0_0.25rem_0.75rem_rgba(30,34,40,0.15)]">Contact</a>',
        '<a href="./contact.html" class="btn btn-sm btn-green !text-white !bg-[#002359] border-[#002359] !rounded-[50rem] !mr-2">Free Trial</a>\n                <a href="tel:+919348457123" class="btn btn-sm btn-primary !text-white !bg-[#ff4450] border-[#ff4450] !rounded-[50rem]">Call Us</a>',
    )
    c = re.sub(
        r'<li class="nav-item dropdown language-select[^>]*>.*?</li>\s*',
        "",
        c,
        count=1,
        flags=re.DOTALL,
    )
    # Remove leftover Sandbox language links (De / Es) in navbar-other
    c = re.sub(
        r'<li class="nav-item"><a class="dropdown-item[^"]*" href="#">De</a></li>\s*'
        r'<li class="nav-item"><a class="dropdown-item[^"]*" href="#">Es</a></li>\s*',
        "",
        c,
    )

    # Footer
    c = c.replace("© 2024 Sandbox.", "© 2024-2026 TrackPOSSystem.")
    c = c.replace("Moonshine St. 14/05 Light City, London, United Kingdom", "Serving businesses all over India")
    c = c.replace('href="mailto:#">info@email.com', 'href="mailto:sales@trackpossystem.com">sales@trackpossystem.com')
    c = c.replace("00 (123) 456 78 90", "+91-9348457123")
    c = c.replace('href="#">About Us</a>', 'href="./about.html">About Us</a>')

    # Contact-specific
    if filename == "contact.html":
        c = c.replace("Drop Us a Line", "Request Demo or Free Trial")
        c = c.replace(
            "Reach out to us from our contact form and we will get back to you shortly.",
            "Fill in the form and our team will contact you within 24 hours to schedule your demo.",
        )
        c = c.replace("00 (123) 456 78 90 <br>00 (987) 654 32 10", "+91-9348457123")
        c = c.replace('href="mailto:sandbox@email.com"', 'href="mailto:sales@trackpossystem.com"')
        c = c.replace("sandbox@email.com", "sales@trackpossystem.com")
        c = c.replace("help@sandbox.com", "support@trackpossystem.com")
        c = c.replace("<option value=\"Sales\">Sales</option>", "<option value=\"Free Trial\">Free Trial</option>")
        c = c.replace("<option value=\"Marketing\">Marketing</option>", "<option value=\"Demo\">Book Demo</option>")
        c = c.replace("Select a department", "How can we help?")
        c = c.replace("We are trusted by over 5000+ clients", "Trusted by businesses all over India")
        c = c.replace("7518", "500")
        c = c.replace("Completed Projects", "Businesses Served")
        c = c.replace("5472", "6")
        c = c.replace("Satisfied Customers", "Industry Solutions")
        c = c.replace("2184", "24")
        c = c.replace("Expert Employees", "Hour Support")

    # About-specific team
    if filename == "about.html":
        c = c.replace("Save your time and money by choosing our professional team.", "Meet the team behind TrackPOSSystem.")
        c = c.replace("<h4 class=\"!mb-1\">Coriss Ambady</h4>", "<h4 class=\"!mb-1\">Rajesh Kumar Sethy</h4>")
        c = c.replace("Financial Analyst", "Founder & CEO", 1)
        c = c.replace("<h4 class=\"!mb-1\">Cory Zamora</h4>", "<h4 class=\"!mb-1\">Jonas Bubhan</h4>", 1)
        c = c.replace("Marketing Specialist", "Co-Founder", 1)
        c = c.replace("Fermentum massa justo sit amet risus morbi leo.", "Building industry-specific POS solutions for Indian SMEs.", 1)

    if "trackpos-float-whatsapp" not in c:
        floats = """
  <a href="https://wa.me/919348457123" class="trackpos-float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="uil uil-whatsapp before:content-['\ed9a']"></i></a>
  <a href="tel:+919348457123" class="trackpos-float-call" aria-label="Call us"><i class="uil uil-phone before:content-['\ec51']"></i></a>
"""
        c = c.replace("<script src=\"./assets/js/plugins.js\"></script>", floats + "  <script src=\"./assets/js/plugins.js\"></script>")

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Patched", filename)

for fn, meta in PAGES.items():
    patch_file(fn, meta)
