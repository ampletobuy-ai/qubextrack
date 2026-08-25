#!/usr/bin/env python3
"""Sync Customer Review section from trackpossystem.com."""
import re
from pathlib import Path

DIST = Path(__file__).resolve().parent

REVIEWS = [
    {
        "name": "Sanatana Jena",
        "role": "Founder of Prabhas Foundations",
        "img": "prabhas.png",
        "alt": "Prabhas Foundations",
        "quote": "Customer support was quick to resolve my issues. Excellent service! Great value for the price. Highly recommended for small to medium businesses!",
    },
    {
        "name": "Rajesh Malick",
        "role": "Proprietor",
        "img": "sairajinn.png",
        "alt": "Sairaj Inn",
        "quote": "The new hotel website built by your team has completely transformed how we present ourselves online. The booking process is now seamless, and guests constantly compliment how easy it is to navigate. We saw a noticeable increase in direct bookings within the first month!",
    },
    {
        "name": "Laxmikanta Pratihari",
        "role": "Proprietor",
        "img": "niladricomplex.png",
        "alt": "Niladri Complex",
        "quote": "Managing rooms, rates, and availability used to be a headache — but this new tracking system software makes it effortless. The mobile responsiveness is fantastic, and the speed is impressive.",
    },
    {
        "name": "Chandrasekhar Samal",
        "role": "Proprietor",
        "img": "itconcept.png",
        "alt": "IT Concept",
        "quote": "I love the inventory tracking and sales reporting features—they've made managing my store much easier.",
    },
]

CUSTOMER_LOGOS = [
    ("prabhas.png", "Prabhas Foundations"),
    ("sairajinn.png", "Sairaj Inn"),
    ("niladricomplex.png", "Niladri Complex"),
    ("itconcept.png", "IT Concept"),
    ("AmpleToBuy.png", "AmpleToBuy"),
]

RATINGS = (
    '<span class="ratings inline-block relative w-20 h-[0.8rem] text-[0.9rem] leading-none '
    "before:text-[rgba(38,43,50,0.1)] after:inline-block after:not-italic after:font-normal "
    "after:absolute after:!text-[#fcc032] after:content-['\\2605\\2605\\2605\\2605\\2605'] "
    "after:overflow-hidden after:left-0 after:top-0 before:inline-block before:not-italic "
    "before:font-normal before:absolute before:!text-[#fcc032] "
    "before:content-['\\2605\\2605\\2605\\2605\\2605'] before:overflow-hidden before:left-0 "
    "before:top-0 five !mb-3\"></span>"
)

BLOCKQUOTE_OPEN = (
    '<blockquote class="!text-[0.85rem] !leading-[1.7] font-medium !pl-4 icon !mb-0 relative '
    "p-0 border-0 before:content-['\\201d'] before:absolute before:top-[-1.5rem] "
    "before:left-[-0.9rem] before:text-[rgba(52,63,82,0.05)] before:text-[10rem] "
    'before:leading-none before:z-[1]">'
)


def review_card_index(r):
    return f"""            <div class="item md:w-6/12 lg:w-6/12 xl:w-6/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px]">
              <div class="card !shadow-[0_0.25rem_1.75rem_rgba(30,34,40,0.07)]">
                <div class="card-body flex-[1_1_auto] p-[40px]">
                  {RATINGS}
                  {BLOCKQUOTE_OPEN}
                    <p>“{r['quote']}”</p>
                    <div class="flex items-center text-left">
                      <img class="trackpos-review-logo !rounded-[.4rem] !w-auto !max-w-[5.5rem] !max-h-[3.5rem] object-contain bg-white p-2 !shadow-[0_0_1rem_rgba(30,34,40,0.06)]" src="./assets/img/customers/{r['img']}" alt="{r['alt']}">
                      <div class="info !pl-4">
                        <h5 class="!mb-1 text-[.95rem] !leading-[1.5]">{r['name']}</h5>
                        <p class="!mb-0 !text-[.8rem]">{r['role']}</p>
                      </div>
                    </div>
                  </blockquote>
                </div>
              </div>
            </div>"""


def review_slide_pricing(r):
    return f"""                <div class="swiper-slide">
                  <div class="item-inner">
                    <div class="card">
                      <div class="card-body flex-[1_1_auto] p-[40px]">
                        {RATINGS}
                        {BLOCKQUOTE_OPEN}
                          <p>“{r['quote']}”</p>
                          <div class="flex items-center text-left">
                            <img class="trackpos-review-logo !rounded-[.4rem] !w-auto !max-w-[5.5rem] !max-h-[3.5rem] object-contain bg-white p-2 !shadow-[0_0_1rem_rgba(30,34,40,0.06)]" src="./assets/img/customers/{r['img']}" alt="{r['alt']}">
                            <div class="info !pl-4">
                              <h5 class="!mb-1 text-[.9rem] !leading-[1.5]">{r['name']}</h5>
                              <p class="!mb-0 text-[.8rem]">{r['role']}</p>
                            </div>
                          </div>
                        </blockquote>
                      </div>
                    </div>
                  </div>
                </div>"""


def review_slide_about(r):
    return f"""                  <div class="swiper-slide">
                    <blockquote class="icon relative p-0 border-0 text-[1rem] !leading-[1.7] font-medium m-[0_0_1rem] before:content-['\\201d'] before:absolute before:top-[-1.5rem] before:left-[-0.9rem] before:text-[rgba(52,63,82,0.05)] before:text-[10rem] before:leading-none before:z-[1]">
                      <p>“{r['quote']}”</p>
                      <div class="flex items-center text-left !mt-4">
                        <img class="trackpos-review-logo !rounded-[.4rem] !w-auto !max-w-[5rem] !max-h-[3rem] object-contain bg-white p-2 !shadow-[0_0_1rem_rgba(30,34,40,0.06)] !mr-4" src="./assets/img/customers/{r['img']}" alt="{r['alt']}">
                        <div class="info !pl-0">
                          <h5 class="!mb-1 text-[.95rem] !leading-[1.5]">{r['name']}</h5>
                          <p class="!mb-0 text-[0.8rem]">{r['role']}</p>
                        </div>
                      </div>
                    </blockquote>
                  </div>"""


def customers_logos_html():
    items = "\n".join(
        f"""          <div class="w-full sm:w-6/12 md:w-4/12 lg:w-1/5 flex-[0_0_auto] !px-[15px] max-w-full !mb-6 flex justify-center items-center">
            <img class="trackpos-customer-logo max-h-[4.5rem] w-auto object-contain opacity-90 hover:opacity-100 transition-opacity" src="./assets/img/customers/{img}" alt="{alt}" loading="lazy">
          </div>"""
        for img, alt in CUSTOMER_LOGOS
    )
    return f"""    <section class="wrapper !bg-[#ffffff]">
      <div class="container py-[3rem] xl:!py-16 lg:!py-16 md:!py-16">
        <div class="flex flex-wrap mx-[-15px]">
          <div class="md:w-10/12 lg:w-8/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mx-auto !text-center">
            <h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3 !tracking-[0.02rem] !leading-[1.35]">We're trusted by</h2>
            <h3 class="xl:!text-[2rem] !text-[calc(1.325rem_+_0.9vw)] !leading-[1.2] !font-DMSerif !font-normal !tracking-normal !mb-4">Our Customers</h3>
            <p class="lead !text-[0.9rem] font-medium !leading-[1.65] !mb-10 xl:!px-10">We take pride in the trust our customers place in us. With a commitment to delivering reliable solutions and exceptional service, we have built strong relationships with businesses across industries.</p>
          </div>
        </div>
        <div class="flex flex-wrap mx-[-15px] justify-center items-center">
{items}
        </div>
      </div>
    </section>
"""


def patch_index():
    path = DIST / "index.html"
    c = path.read_text(encoding="utf-8")
    c = c.replace(
        '<h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3 !tracking-[0.02rem] !leading-[1.35]">Happy Customers</h2>\n'
        '            <h3 class="xl:!text-[2rem] !text-[calc(1.325rem_+_0.9vw)] !leading-[1.2] !font-DMSerif !font-normal !tracking-normal [word-spacing:normal!important] !mb-10 xl:!px-10 xxl:!px-20">Don\'t take our word for it. See what customers are saying about us.</h3>',
        '<h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3 !tracking-[0.02rem] !leading-[1.35]">What people says</h2>\n'
        '            <h3 class="xl:!text-[2rem] !text-[calc(1.325rem_+_0.9vw)] !leading-[1.2] !font-DMSerif !font-normal !tracking-normal [word-spacing:normal!important] !mb-10 xl:!px-10 xxl:!px-20">Customer <strong class="!text-[#343f52]">Review</strong></h3>',
    )
    grid = "\n".join(review_card_index(r) for r in REVIEWS)
    c = re.sub(
        r'<div class="itemgrid">\s*<div class="flex flex-wrap mx-\[-15px\] isotope.*?</div>\s*<!-- /\.grid-view -->',
        f'<div class="itemgrid">\n          <div class="flex flex-wrap mx-[-15px] isotope !mt-[-30px]">\n{grid}\n          </div>\n          <!-- /.row -->\n        </div>\n        <!-- /.grid-view -->',
        c,
        count=1,
        flags=re.DOTALL,
    )
    if 'trackpos-customer-logo' not in c:
        c = c.replace(
            '    </section>\n    <!-- /section -->\n    <section class="wrapper !bg-[#ffffff]">\n      <div class="container py-[4.5rem] xl:!py-28 lg:!py-28 md:!py-28">\n        <div class="flex flex-wrap mx-[-15px] max-sm:!mt-[-50px]',
            customers_logos_html() + '\n    <!-- /our-customers -->\n    <section class="wrapper !bg-[#ffffff]">\n      <div class="container py-[4.5rem] xl:!py-28 lg:!py-28 md:!py-28">\n        <div class="flex flex-wrap mx-[-15px] max-sm:!mt-[-50px]',
            1,
        )
    path.write_text(c, encoding="utf-8")
    print("Updated index.html")


def patch_about():
    path = DIST / "about.html"
    c = path.read_text(encoding="utf-8")
    slides = "\n".join(review_slide_about(r) for r in REVIEWS)
    slides += "\n                  <!--/.swiper-slide -->"
    c = re.sub(
        r'<div class="swiper-wrapper">\s*<div class="swiper-slide">.*?</div>\s*<!-- /\.swiper-wrapper -->',
        f'<div class="swiper-wrapper">\n{slides}\n                </div>\n                <!--/.swiper-wrapper -->',
        c,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(c, encoding="utf-8")
    print("Updated about.html")


def patch_pricing():
    path = DIST / "pricing.html"
    c = path.read_text(encoding="utf-8")
    c = c.replace(
        '<h2 class="!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-3 !text-center">Happy Customers</h2>\n'
        '        <p class="lead text-[0.9rem] font-medium !leading-[1.65] !text-center !mb-6 md:!px-24 lg:!px-0">Customer satisfaction is our major goal. See what our customers are saying about us.</p>',
        '<p class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-2 !tracking-[0.02rem] !leading-[1.35] !text-center">What people says</p>\n'
        '        <h2 class="!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-3 !text-center">Customer <strong>Review</strong></h2>\n'
        '        <p class="lead text-[0.9rem] font-medium !leading-[1.65] !text-center !mb-6 md:!px-24 lg:!px-0">Customer satisfaction is our major goal. See what our customers are saying about us.</p>',
    )
    slides = "\n".join(review_slide_pricing(r) for r in REVIEWS)
    slides += "\n                <!--/.swiper-slide -->"
    c = re.sub(
        r'<div class="swiper-wrapper">\s*<div class="swiper-slide">.*?</div>\s*<!--/\.swiper-wrapper -->',
        f'<div class="swiper-wrapper">\n{slides}\n              </div>\n              <!--/.swiper-wrapper -->',
        c,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(c, encoding="utf-8")
    print("Updated pricing.html")


def patch_css():
    path = DIST / "assets/css/trackpos.css"
    css = path.read_text(encoding="utf-8")
    block = """
/* Customer reviews & logos (from trackpossystem.com) */
.trackpos-review-logo {
  flex-shrink: 0;
}
.trackpos-customer-logo {
  filter: none;
  max-width: 100%;
}
"""
    if "trackpos-review-logo" not in css:
        path.write_text(css.rstrip() + block, encoding="utf-8")
        print("Updated trackpos.css")


if __name__ == "__main__":
    patch_index()
    patch_about()
    patch_pricing()
    patch_css()
