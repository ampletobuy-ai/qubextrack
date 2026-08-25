#!/usr/bin/env python3
"""Restore original Sandbox UI for reviews; keep trackpossystem.com content."""
import re
from pathlib import Path

DIST = Path(__file__).resolve().parent

# Newest testimonials first (descending / reverse chronological)
REVIEWS = [
    ("Proprietor", "Aura Jewellery", "aurajewellery.png", "Aura Jewellery",
     "TrackPOSSystem makes gold and silver billing effortless — making charges, wastage, and stone details are captured accurately at the counter. Barcode tagging, daily stock reconciliation, and GST invoices save us hours every day in our showroom."),
    ("Management Team", "Mahaprasadam Bhakta Nivas · Hotel & Restaurant", "mahaprasadam.png", "Mahaprasadam Bhakta Nivas",
     "From room check-in and billing to restaurant table orders and KOT printing, TrackPOSSystem keeps our hotel and restaurant running smoothly on one platform. Day-end reports for rooms and dining are accurate, and our staff picked it up quickly."),
    ("Chandrasekhar Samal", "Proprietor", "itconcept.png", "IT Concept",
     "I love the inventory tracking and sales reporting features—they've made managing my store much easier."),
    ("Laxmikanta Pratihari", "Proprietor", "niladricomplex.png", "Niladri Complex",
     "Managing rooms, rates, and availability used to be a headache — but this new tracking system software makes it effortless. The mobile responsiveness is fantastic, and the speed is impressive."),
    ("Rajesh Malick", "Proprietor", "sairajinn.png", "Sairaj Inn",
     "The new hotel website built by your team has completely transformed how we present ourselves online. The booking process is now seamless, and guests constantly compliment how easy it is to navigate. We saw a noticeable increase in direct bookings within the first month!"),
    ("Sanatana Jena", "Founder of Prabhas Foundations", "prabhas.png", "Prabhas Foundations",
     "Customer support was quick to resolve my issues. Excellent service! Great value for the price. Highly recommended for small to medium businesses!"),
]

RATINGS = '<span class="ratings  inline-block relative w-20 h-[0.8rem] text-[0.9rem] leading-none before:text-[rgba(38,43,50,0.1)] after:inline-block after:not-italic after:font-normal after:absolute after:!text-[#fcc032] after:content-[\'\\2605\\2605\\2605\\2605\\2605\'] after:overflow-hidden after:left-0 after:top-0 before:inline-block before:not-italic before:font-normal before:absolute before:!text-[#fcc032] before:content-[\'\\2605\\2605\\2605\\2605\\2605\'] before:overflow-hidden before:left-0 before:top-0 five !mb-3"></span>'

BQ_OPEN = '<blockquote class="!text-[0.85rem] !leading-[1.7] font-medium !pl-4 icon !mb-0 relative p-0 border-0 before:content-[\'\\201d\'] before:absolute before:top-[-1.5rem] before:left-[-0.9rem] before:text-[rgba(52,63,82,0.05)] before:text-[10rem] before:leading-none before:z-[1]">'


def review_logo_class(img: str) -> str:
    return "trackpos-review-logo"


def index_card(name, role, img, alt, quote):
    return f"""            <div class="item md:w-6/12 lg:w-6/12 xl:w-4/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px]">
              <div class="card !shadow-[0_0.25rem_1.75rem_rgba(30,34,40,0.07)]">
                <div class="card-body flex-[1_1_auto] p-[40px]">
                  {RATINGS}
                  {BQ_OPEN}
                    <p>“{quote}”</p>
                    <div class="flex items-center text-left">
                      <img class="{review_logo_class(img)}" src="./assets/img/customers/{img}" alt="{alt}">
                      <div class="info !pl-4">
                        <h5 class="!mb-1 text-[.95rem] !leading-[1.5]">{name}</h5>
                        <p class="!mb-0 !text-[.8rem]">{role}</p>
                      </div>
                    </div>
                  </blockquote>
                </div>
                <!-- /.card-body -->
              </div>
              <!-- /.card -->
            </div>
            <!--/column -->"""


def pricing_slide(name, role, img, alt, quote):
    return f"""                <div class="swiper-slide">
                  <div class="item-inner">
                    <div class="card">
                      <div class="card-body flex-[1_1_auto] p-[40px]">
                        {RATINGS}
                        {BQ_OPEN}
                          <p>“{quote}”</p>
                          <div class="flex items-center text-left">
                            <img class="{review_logo_class(img)}" src="./assets/img/customers/{img}" alt="{alt}">
                            <div class="info !pl-4">
                              <h5 class="!mb-1 text-[.9rem] !leading-[1.5]">{name}</h5>
                              <p class="!mb-0 text-[.8rem]">{role}</p>
                            </div>
                          </div>
                        </blockquote>
                      </div>
                      <!-- /.card-body -->
                    </div>
                    <!-- /.card -->
                  </div>
                  <!-- /.item-inner -->
                </div>
                <!--/.swiper-slide -->"""


def about_slide(name, role, img, alt, quote):
    return f"""                  <div class="swiper-slide">
                    <blockquote class="icon relative p-0 border-0 text-[1rem] !leading-[1.7] font-medium m-[0_0_1rem] before:content-['\\201d'] before:absolute before:top-[-1.5rem] before:left-[-0.9rem] before:text-[rgba(52,63,82,0.05)] before:text-[10rem] before:leading-none before:z-[1]">
                      <p>“{quote}”</p>
                      <div class="flex items-center text-left">
                        <img class="{review_logo_class(img)}" src="./assets/img/customers/{img}" alt="{alt}">
                        <div class="info !pl-4">
                          <h5 class="!mb-1 text-[.95rem] !leading-[1.5]">{name}</h5>
                          <p class="!mb-0 text-[0.8rem]">{role}</p>
                        </div>
                      </div>
                    </blockquote>
                  </div>
                  <!--/.swiper-slide -->"""


def patch_index():
    path = DIST / "index.html"
    c = path.read_text(encoding="utf-8")
    c = c.replace(
        '<h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3 !tracking-[0.02rem] !leading-[1.35]">What people says</h2>\n'
        '            <h3 class="xl:!text-[2rem] !text-[calc(1.325rem_+_0.9vw)] !leading-[1.2] !font-DMSerif !font-normal !tracking-normal [word-spacing:normal!important] !mb-10 xl:!px-10 xxl:!px-20">Customer <strong class="!text-[#343f52]">Review</strong></h3>',
        '<h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3 !tracking-[0.02rem] !leading-[1.35]">Happy Customers</h2>\n'
        '            <h3 class="xl:!text-[2rem] !text-[calc(1.325rem_+_0.9vw)] !leading-[1.2] !font-DMSerif !font-normal !tracking-normal [word-spacing:normal!important] !mb-10 xl:!px-10 xxl:!px-20">Don\'t take our word for it. See what customers are saying about us.</h3>',
    )
    grid = "\n".join(index_card(*r) for r in REVIEWS)
    c = re.sub(
        r'<div class="itemgrid">.*?</div>\s*<!-- /\.grid-view -->',
        f'<div class="itemgrid">\n          <div class="flex flex-wrap mx-[-15px] isotope !mt-[-30px]">\n{grid}\n          </div>\n          <!-- /.row -->\n        </div>\n        <!-- /.grid-view -->',
        c,
        count=1,
        flags=re.DOTALL,
    )
    c = re.sub(
        r'\s*</section>\s*<!-- /section -->\s*<section class="wrapper !bg-\[#ffffff\]">\s*'
        r'<div class="container py-\[3rem\].*?</section>\s*\n\s*<!-- /our-customers -->\s*',
        '\n    </section>\n    <!-- /section -->\n    <section class="wrapper !bg-[#ffffff]">\n      ',
        c,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(c, encoding="utf-8")
    print("index.html")


def patch_about():
    path = DIST / "about.html"
    c = path.read_text(encoding="utf-8")
    slides = "\n".join(about_slide(n, r, i, a, q) for n, r, i, a, q in REVIEWS)
    c = re.sub(
        r'(<div class="swiper-container dots-start dots-closer.*?<div class="swiper-wrapper">).*?(</div>\s*<!--/\.swiper-wrapper -->)',
        rf"\1\n{slides}\n                \2",
        c,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(c, encoding="utf-8")
    print("about.html")


def patch_pricing():
    path = DIST / "pricing.html"
    c = path.read_text(encoding="utf-8")
    c = re.sub(
        r'<p class="!text-\[\.75rem\] uppercase.*?</p>\s*'
        r'<h2 class="!text-\[calc\(1\.305rem.*?>Customer <strong>Review</strong></h2>',
        '<h2 class="!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-3 !text-center">Happy Customers</h2>',
        c,
        count=1,
        flags=re.DOTALL,
    )
    slides = "\n".join(pricing_slide(*r) for r in REVIEWS)
    c = re.sub(
        r'<div class="swiper-wrapper">.*?</div>\s*<!--/\.swiper-wrapper -->',
        f'<div class="swiper-wrapper">\n{slides}\n              </div>\n              <!--/.swiper-wrapper -->',
        c,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(c, encoding="utf-8")
    print("pricing.html")


def patch_css():
    path = DIST / "assets/css/trackpos.css"
    c = path.read_text(encoding="utf-8")
    c = re.sub(
        r"\n/\* Customer reviews & logos.*?\n\.trackpos-customer-logo \{[^}]+\}\n",
        "\n",
        c,
        flags=re.DOTALL,
    )
    path.write_text(c, encoding="utf-8")
    print("trackpos.css")


def apply_review_order():
    """Regenerate testimonial blocks in REVIEWS order (newest first)."""
    path = DIST / "index.html"
    c = path.read_text(encoding="utf-8")
    grid = "\n".join(index_card(*r) for r in REVIEWS)
    c = re.sub(
        r'<div class="itemgrid">.*?</div>\s*<!-- /\.grid-view -->',
        f'<div class="itemgrid">\n          <div class="flex flex-wrap mx-[-15px] isotope !mt-[-30px]">\n{grid}\n          </div>\n          <!-- /.row -->\n        </div>\n        <!-- /.grid-view -->',
        c,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(c, encoding="utf-8")
    print("index.html")

    path = DIST / "about.html"
    c = path.read_text(encoding="utf-8")
    slides = "\n".join(about_slide(n, r, i, a, q) for n, r, i, a, q in REVIEWS)
    c = re.sub(
        r'(<div class="swiper-container dots-start dots-closer.*?<div class="swiper-wrapper">).*?(</div>\s*<!--/\.swiper-wrapper -->)',
        rf"\1\n{slides}\n                \2",
        c,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(c, encoding="utf-8")
    print("about.html")

    path = DIST / "pricing.html"
    c = path.read_text(encoding="utf-8")
    slides = "\n".join(pricing_slide(*r) for r in REVIEWS)
    c = re.sub(
        r'(<h2 class="!text-\[calc\(1\.305rem.*?Happy Customers</h2>.*?<div class="swiper-wrapper">).*?(</div>\s*<!--/\.swiper-wrapper -->)',
        rf"\1\n{slides}\n              \2",
        c,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(c, encoding="utf-8")
    print("pricing.html")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "order":
        apply_review_order()
    else:
        patch_index()
        patch_about()
        patch_pricing()
        patch_css()
