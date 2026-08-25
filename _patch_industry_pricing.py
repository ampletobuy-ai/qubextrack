#!/usr/bin/env python3
"""Add jewellery-style pricing sections to restaurant, hotel, and retail pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

ADDONS = """
                <div class="flex flex-wrap mx-[-15px] !mt-12">
              <div class="w-full flex-[0_0_auto] !px-[15px] max-w-full">
                <h4 class="!text-[1.25rem] !font-DMSerif !mb-4">Recommended add-ons</h4>
                <div class="trackpos-security-compare overflow-x-auto">
                  <table class="trackpos-security-table w-full">
                    <thead>
                      <tr>
                        <th scope="col">Add-on</th>
                        <th scope="col">Suggested price</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td>Extra Branch</td><td>₹999/month</td></tr>
                      <tr><td>Extra User</td><td>₹199/month</td></tr>
                      <tr><td>WhatsApp Automation</td><td>Usage-based</td></tr>
                      <tr><td>SMS Integration</td><td>Usage-based</td></tr>
                      <tr><td>Custom Reports</td><td>₹5,000+</td></tr>
                      <tr><td>Data Migration</td><td>₹3,000–₹20,000</td></tr>
                      <tr><td>Onsite Training</td><td>₹5,000/day</td></tr>
                    </tbody>
                  </table>
                </div>
                <p class="!text-center !text-[0.8rem] !text-[#aab0bc] !mt-4 !mb-0">Add-ons depend on your setup and integration requirements.</p>
                <p class="!text-center !text-[0.85rem] !text-[#60697b] !mt-4 !mb-0">All plan prices exclude GST. Cloud sync &amp; mobile app access included.</p>
                <p class="trackpos-pricing-disclaimer !text-center !text-[0.8rem] !text-[#aab0bc] !mt-2 !mb-0">Listed plan prices may be revised year on year when required, with prior notice to existing customers before any change takes effect.</p>
              </div>
            </div>
"""

PAGES = {
    "restaurant-pos-software.html": {
        "plans_label": "Restaurant plans",
        "heading": "Choose a plan for your outlet size",
        "lead": "Modern cloud POS for restaurants — table service, KOT, inventory, aggregator sync, and GST billing.",
        "starter_sub": "Best for single-outlet restaurants, cafés, and cloud kitchens.",
        "pro_sub": "Best for multi-outlet restaurants, chains, and aggregator-led kitchens.",
        "starter_features": [
            "GST billing",
            "Table, floor plan &amp; KOT printing",
            "Menu variants, combos &amp; split bills",
            "Invoice print",
            "Up to 1,000 invoices",
            "Kitchen order routing &amp; order history",
            "Inventory &amp; recipe-wise stock deduction",
            "Up to 250 menu items",
            "Sales return/exchange",
            "Customer outstanding",
            "Daily sales &amp; category reports",
            "Single user",
            "Single outlet",
            "WhatsApp support + basic onboarding",
        ],
        "pro_features": [
            "Multi-outlet inventory",
            "Inter-outlet stock transfer",
            "Swiggy &amp; Zomato order sync",
            "Kitchen display (KDS) &amp; course timing",
            "Role-based permissions + audit logs",
            "Staff tips, attendance &amp; payroll",
            "Dedicated database + cloud backup",
            "Advanced reporting",
            "WhatsApp/SMS marketing to guests",
            "Multi user support",
            "Unlimited invoices",
            "Unlimited products",
            "Priority support + remote setup assistance",
        ],
    },
    "hotel-management-software.html": {
        "plans_label": "Hotel plans",
        "heading": "Choose a plan for your property size",
        "lead": "Modern cloud PMS for hotels — bookings, housekeeping, folio billing, OTA sync, and GST reports.",
        "starter_sub": "Best for boutique hotels, guest houses, and homestays.",
        "pro_sub": "Best for multi-property hotels, resorts, and chains.",
        "starter_features": [
            "GST billing",
            "Room booking, check-in &amp; check-out",
            "Housekeeping status &amp; guest folio billing",
            "Invoice print",
            "Up to 1,000 invoices",
            "Rate plans, packages &amp; add-on services",
            "Occupancy &amp; revenue summary reports",
            "Up to 250 room/service packages",
            "Customer outstanding",
            "Daily sales &amp; ledger reports",
            "Single user",
            "Single property",
            "WhatsApp support + basic onboarding",
        ],
        "pro_features": [
            "Multi-property inventory",
            "Inter-property stock transfer",
            "OTA channel distribution &amp; sync",
            "Real-time occupancy visibility",
            "Role-based permissions + audit logs",
            "Seasonal pricing &amp; dynamic rate rules",
            "Dedicated database + cloud backup",
            "Advanced reporting",
            "e-Way bills &amp; e-Invoices",
            "Multi user support",
            "Unlimited invoices",
            "Unlimited products",
            "Staff roster, attendance &amp; payroll",
            "Priority support + property onboarding",
        ],
    },
    "retail-billing-software.html": {
        "plans_label": "Retail plans",
        "heading": "Choose a plan for your store size",
        "lead": "Modern cloud POS for retail — barcode billing, inventory, purchases, loyalty, and GST compliance.",
        "starter_sub": "Best for single-store retail, kirana, and specialty shops.",
        "pro_sub": "Best for multi-store retail chains and franchises.",
        "starter_features": [
            "GST billing",
            "Barcode billing at counter",
            "Invoice print",
            "Up to 1,000 invoices",
            "Inventory, categories &amp; low stock alerts",
            "Up to 250 products",
            "Customer ledger &amp; party-wise dues",
            "GSTR-1, GSTR-3B &amp; JSON export",
            "Sales return/exchange",
            "Daily sales &amp; stock summary",
            "Single user",
            "Single store",
            "WhatsApp support + basic onboarding",
        ],
        "pro_features": [
            "Multi-store inventory sync",
            "Inter-store stock transfer",
            "Real-time stock visibility",
            "Role-based permissions + audit logs",
            "Barcode generate, print &amp; scan at POS",
            "Dedicated database + cloud backup",
            "Advanced reporting",
            "e-Way bills &amp; B2B e-Invoices",
            "Loyalty points &amp; WhatsApp marketing",
            "Multi user support",
            "Unlimited invoices",
            "Unlimited products",
            "Staff attendance &amp; payroll",
            "Priority support + CA-ready reports",
        ],
    },
}


def feature_items(items):
    return "\n".join(f"                        <li>{item}</li>" for item in items)


def pricing_section(cfg):
    return f"""
        <section id="pricing" class="wrapper !bg-[#ffffff] trackpos-jewellery-pricing">
          <div class="container py-[4.5rem] xl:!py-24 lg:!py-24 md:!py-24">
            <div class="flex flex-wrap mx-[-15px] !mb-10">
              <div class="lg:w-10/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mx-auto !text-center">
                <h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3 !tracking-[0.02rem] !leading-[1.35]">{cfg['plans_label']}</h2>
                <h3 class="xl:!text-[2rem] !text-[calc(1.325rem_+_0.9vw)] !leading-[1.2] !font-DMSerif !font-normal !tracking-normal [word-spacing:normal!important] !mb-4">{cfg['heading']}</h3>
                <p class="lead !mb-0 !text-[#60697b]">{cfg['lead']}</p>
              </div>
            </div>

            <div class="flex flex-wrap mx-[-15px] justify-center trackpos-jewellery-pricing-grid">
              <div class="md:w-6/12 lg:w-5/12 xl:w-5/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px]">
                <div class="trackpos-jewellery-pricing-card trackpos-jewellery-pricing-card--starter">
                  <div class="trackpos-jewellery-pricing-card__body">
                    <span class="trackpos-jewellery-plan-badge trackpos-jewellery-plan-badge--starter">Starter</span>
                    <h4 class="trackpos-jewellery-pricing-card__title">Starter Plan</h4>
                    <p class="trackpos-jewellery-pricing-card__subtitle">{cfg['starter_sub']}</p>

                    <div class="trackpos-jewellery-pricing-card__price">
                      <div class="trackpos-jewellery-pricing-card__price-row">₹1,499 <span>/ month</span></div>
                      <div class="trackpos-jewellery-pricing-card__price-or">OR</div>
                      <div class="trackpos-jewellery-pricing-card__price-row">₹14,999 <span>/ year</span> <span class="trackpos-jewellery-pricing-card__price-save">Save 17%</span></div>
                    </div>

                    <div class="trackpos-jewellery-pricing-card__features">
                      <h5 class="trackpos-jewellery-pricing-card__features-title">Features included</h5>
                      <ul class="trackpos-jewellery-pricing-list">
{feature_items(cfg['starter_features'])}
                      </ul>
                    </div>

                    <a href="./contact.html" class="trackpos-jewellery-pricing-card__btn trackpos-jewellery-pricing-card__btn--starter">Request Free Trial</a>
                  </div>
                </div>
              </div>

              <div class="md:w-6/12 lg:w-5/12 xl:w-5/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px] popular">
                <div class="trackpos-jewellery-pricing-card trackpos-jewellery-pricing-card--pro">
                  <div class="trackpos-jewellery-pricing-card__accent"></div>
                  <div class="trackpos-jewellery-pricing-card__body">
                    <span class="trackpos-jewellery-plan-badge trackpos-jewellery-plan-badge--pro">Professional</span>
                    <h4 class="trackpos-jewellery-pricing-card__title">Professional Plan</h4>
                    <p class="trackpos-jewellery-pricing-card__subtitle">{cfg['pro_sub']}</p>

                    <div class="trackpos-jewellery-pricing-card__price">
                      <div class="trackpos-jewellery-pricing-card__price-row">₹2,499 <span>/ month</span></div>
                      <div class="trackpos-jewellery-pricing-card__price-or">OR</div>
                      <div class="trackpos-jewellery-pricing-card__price-row">₹24,999 <span>/ year</span> <span class="trackpos-jewellery-pricing-card__price-save">Save 17%</span></div>
                    </div>

                    <div class="trackpos-jewellery-pricing-card__features">
                      <h5 class="trackpos-jewellery-pricing-card__features-title">Everything in Starter PLUS</h5>
                      <ul class="trackpos-jewellery-pricing-list">
{feature_items(cfg['pro_features'])}
                      </ul>
                    </div>

                    <a href="./contact.html" class="trackpos-jewellery-pricing-card__btn trackpos-jewellery-pricing-card__btn--pro">
                      <span>Choose Professional</span>
                    </a>
                  </div>
                </div>
              </div>
            </div>

{ADDONS}
          </div>
        </section>
"""


def patch_file(name, cfg):
    path = ROOT / name
    text = path.read_text(encoding="utf-8")

    text = text.replace('href="./index.html#pricing"', 'href="#pricing"')

    marker = "        <!-- /security-compliance -->"
    if marker not in text:
        raise SystemExit(f"marker not found in {name}")

    if 'id="pricing"' in text:
        start = text.index('<section id="pricing"')
        end = text.index('        </section>', start) + len('        </section>\n')
        text = text[:start] + pricing_section(cfg).strip() + "\n\n" + text[end:]
    else:
        insert = pricing_section(cfg)
        text = text.replace(marker, marker + insert, 1)

    if "trackpos-anchor.js" not in text:
        text = text.replace(
            '<script src="./assets/js/theme.js"></script>',
            '<script src="./assets/js/theme.js"></script>\n  <script src="./assets/js/trackpos-anchor.js"></script>',
        )

    path.write_text(text, encoding="utf-8")
    print("patched", name)


def main():
    for name, cfg in PAGES.items():
        patch_file(name, cfg)


if __name__ == "__main__":
    main()
