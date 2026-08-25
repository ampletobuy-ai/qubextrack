#!/usr/bin/env python3
"""Generate TrackPOSSystem industry landing pages."""
import os
import re
from pathlib import Path

DIST = Path(__file__).resolve().parent

def _load_home_header():
    index = (DIST / "index.html").read_text(encoding="utf-8")
    nav_m = re.search(
        r'<nav class="navbar navbar-expand-lg classic transparent navbar-light">.*?</nav>\s*<!-- /\.navbar -->',
        index,
        re.DOTALL,
    )
    offcanvas_m = re.search(
        r'<div class="offcanvas offcanvas-end text-inverse !text-\[#cacaca\] opacity-100" id="offcanvas-info".*?</div>\s*<!-- /\.offcanvas -->',
        index,
        re.DOTALL,
    )
    if not nav_m or not offcanvas_m:
        raise RuntimeError("Homepage nav or offcanvas-info not found in index.html")
    return (
        '    <header class="relative wrapper !bg-[#f5f5ff]">\n'
        f"      {nav_m.group(0)}\n"
        f"      {offcanvas_m.group(0)}\n"
        "    </header>"
    )


HEADER = _load_home_header()

def _load_home_footer():
    index = (DIST / "index.html").read_text(encoding="utf-8")
    m = re.search(
        r'\n  <footer class=" bg-\[#21262c\].*?</footer>\s*<!-- progress wrapper -->.*?</div>\s*\n\s*',
        index,
        re.DOTALL,
    )
    if not m:
        raise RuntimeError("Homepage footer block not found in index.html")
    return m.group(0)


FOOTER = _load_home_footer()

PAGES = [
    {
        "file": "jewellery-pos-software.html",
        "title": "Jewellery POS Software India | TrackPOSSystem",
        "description": "Jewellery billing software with gold rate management, hallmark tracking, karigar management, repair orders, old gold exchange and GST billing.",
        "h1": "Jewellery POS Software for Gold & Silver Retailers",
        "subtitle": "Manage gold rates, hallmark, karigar, stone weight, repair orders, and GST billing from one cloud & offline POS.",
        "features": [
            "Gold & silver daily rate management",
            "Hallmark & purity tracking",
            "Karigar / artisan job management",
            "Stone weight & making charge calculation",
            "Barcode, RFID & item tagging",
            "Repair order & old gold exchange",
            "GST-compliant jewellery invoices",
            "Profit reports by item & invoice",
        ],
    },
    {
        "file": "restaurant-pos-software.html",
        "title": "Restaurant POS Software India | TrackPOSSystem",
        "description": "Restaurant billing software with KDS, table management, KOT printing, Swiggy/Zomato integration and recipe costing.",
        "h1": "Restaurant POS & Billing Software",
        "subtitle": "Streamline dine-in, takeaway, and delivery with kitchen display, table management, and aggregator integration.",
        "features": [
            "Kitchen Display System (KDS)",
            "Table & floor management",
            "KOT & bill printing",
            "Swiggy / Zomato integration",
            "QR menu ordering",
            "Recipe & food cost management",
            "Split bills & multiple payments",
            "Sales & item-wise reports",
        ],
    },
    {
        "file": "hotel-management-software.html",
        "title": "Hotel Management Software India | TrackPOSSystem",
        "description": "Hotel management system with room booking, check-in/out, OTA integration, guest CRM and restaurant billing.",
        "h1": "Hotel Management & Booking Software",
        "subtitle": "Manage rooms, rates, availability, guest CRM, and restaurant billing in one integrated platform.",
        "features": [
            "Room booking & reservation management",
            "Check-in / check-out workflow",
            "OTA & channel manager integration",
            "Guest CRM & history",
            "Rate plans & seasonal pricing",
            "Housekeeping status tracking",
            "Restaurant billing integration",
            "Occupancy & revenue reports",
        ],
    },
    {
        "file": "retail-billing-software.html",
        "title": "Retail POS Billing Software India | TrackPOSSystem",
        "description": "Retail billing software with barcode POS, inventory, multi-store support, loyalty points and GST reports.",
        "h1": "Retail POS & Billing Software",
        "subtitle": "Fast barcode billing, inventory control, and GST reports for kirana, garment, electronics and retail stores.",
        "features": [
            "Barcode / name / code wise billing",
            "Multi-warehouse inventory",
            "Multi-store management",
            "Customer loyalty points",
            "Purchase, sales & returns",
            "Expense & income tracking",
            "GSTR-1 & GSTR-3B reports",
            "Cloud + offline sync",
        ],
    },
    {
        "file": "pharmacy-pos-software.html",
        "title": "Pharmacy POS Software India | TrackPOSSystem",
        "description": "Pharmacy billing software with batch tracking, expiry alerts, GST billing and inventory management.",
        "h1": "Pharmacy POS & Billing Software",
        "subtitle": "Batch-wise stock, expiry alerts, and GST-compliant billing built for pharmacy and medical stores.",
        "features": [
            "Batch & expiry date tracking",
            "Schedule drug category support",
            "Barcode billing at counter",
            "Supplier & purchase management",
            "GST pharmacy invoices",
            "Stock adjustment & alerts",
            "Sales & purchase reports",
            "Multi-user role access",
        ],
    },
    {
        "file": "supermarket-pos-software.html",
        "title": "Supermarket POS Software India | TrackPOSSystem",
        "description": "Supermarket POS with fast checkout, barcode scanning, multi-warehouse inventory and GST billing.",
        "h1": "Supermarket & Grocery POS Software",
        "subtitle": "High-speed checkout, barcode scanning, and warehouse inventory for supermarkets and grocery chains.",
        "features": [
            "Fast multi-item checkout",
            "Barcode scanner integration",
            "Category-wise product search",
            "Multi-warehouse stock control",
            "Combo pack & offer management",
            "Supplier payment tracking",
            "Daily sales summary reports",
            "Weighing scale integration ready",
        ],
    },
]

def render_page(p):
    features_html = "\n".join(
        f'              <li class="relative !pl-6 !mt-[0.35rem]"><i class="uil uil-check absolute left-0 w-4 h-4 text-[0.8rem] flex items-center justify-center bg-[#ffe8ea] !text-[#ff4450] rounded-[100%] top-[0.2rem]"></i><span>{f}</span></li>'
        for f in p["features"]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{p['description']}">
  <meta name="keywords" content="TrackPOSSystem, {p['h1']}, POS software India, GST billing">
  <link rel="canonical" href="https://trackpossystem.com/{p['file']}">
  <title>{p['title']}</title>
  <link rel="shortcut icon" href="./assets/img/favicon.png">
  <link rel="stylesheet" type="text/css" href="./assets/fonts/unicons/unicons.css">
  <link rel="stylesheet" href="./assets/css/plugins.css">
  <link rel="stylesheet" href="./style.css">
  <link rel="stylesheet" href="./assets/css/trackpos.css">
</head>
<body class="font-Manrope text-[0.8rem] !leading-[1.7] font-medium">
  <div class="grow shrink-0">
{HEADER}
    <section class="wrapper !bg-[#f5f5ff] trackpos-industry-hero">
      <div class="container">
        <div class="flex flex-wrap mx-[-15px] items-center">
          <div class="lg:w-6/12 w-full flex-[0_0_auto] !px-[15px] max-w-full">
            <h1 class="xl:!text-[2.4rem] !text-[calc(1.375rem_+_1.5vw)] !font-DMSerif !leading-[1.15] !mb-4">{p['h1']}</h1>
            <p class="lead !mb-6">{p['subtitle']}</p>
            <a href="./contact.html" class="btn btn-lg btn-primary !text-white !bg-[#ff4450] border-[#ff4450] !rounded !mr-2">Book Free Demo</a>
            <a href="https://wa.me/919348457123" target="_blank" rel="noopener" class="btn btn-lg btn-outline-primary !rounded">WhatsApp</a>
          </div>
          <div class="lg:w-6/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-8 lg:!mt-0">
            <img class="rounded-[.4rem] !shadow-[0_0.25rem_1.75rem_rgba(30,34,40,0.07)] w-full" src="./assets/img/photos/sa16.jpg" alt="{p['h1']} dashboard preview">
          </div>
        </div>
      </div>
    </section>
    <section class="wrapper !bg-[#ffffff]">
      <div class="container py-16 xl:!py-20">
        <h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3">Key Features</h2>
        <h3 class="xl:!text-[1.8rem] !font-DMSerif !mb-8">Built for your industry workflow</h3>
        <div class="flex flex-wrap mx-[-15px]">
          <div class="lg:w-6/12 w-full flex-[0_0_auto] !px-[15px] max-w-full">
            <ul class="pl-0 list-none bullet-bg bullet-soft-primary">
{features_html}
            </ul>
          </div>
          <div class="lg:w-6/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-8 lg:!mt-0">
            <motion class="card !bg-[#f5f5ff] !border-0">
              <div class="card-body p-8">
                <h4 class="!mb-3">Start your free 14-day trial</h4>
                <p class="!mb-4">Experience all features with dedicated support. Cloud &amp; offline. GST compliant. From ₹600/month.</p>
                <a href="./contact.html" class="btn btn-primary !text-white !bg-[#ff4450] border-[#ff4450] !rounded">Request Free Trial</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
{FOOTER}
  <a href="https://wa.me/919348457123" class="trackpos-float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="uil uil-whatsapp before:content-['\ed9a']"></i></a>
  <a href="tel:+919348457123" class="trackpos-float-call" aria-label="Call us"><i class="uil uil-phone before:content-['\ec51']"></i></a>
  <script src="./assets/js/plugins.js"></script>
  <script src="./assets/js/theme.js"></script>
</body>
</html>
""".replace("<motion class=", "<motion class=").replace("</motion>", "</div>")

for page in PAGES:
    html = render_page(page)
    html = html.replace("<motion class=", "<div class=").replace("</motion>", "</div>")
    out = DIST / page["file"]
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote", page["file"])
