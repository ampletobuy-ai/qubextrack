#!/usr/bin/env python3
"""Patch index.html with TrackPOSSystem content."""
path = "/Users/rajeshjena/Downloads/trackpos-main-site/dist/index.html"

with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Hero
c = c.replace("Sandbox is effortless and powerful with", "Smart POS & Business Management for")
c = c.replace(
    'data-words="easy usage,fast transactions,secure payments"',
    'data-words="Jewellery Stores,Restaurants,Hotels,Retail Businesses"',
)
c = c.replace(
    "Achieve your saving goals. Have all your recurring and one time expenses and incomes in one place.",
    "Cloud & offline POS solutions for billing, inventory, accounting, CRM, and customer loyalty — trusted by businesses all over India.",
)
c = c.replace('!mb-7">Cloud & offline', '!mb-4">Cloud & offline')

if "trackpos-badge" not in c:
    badges = """
            <div class="!mb-6 flex flex-wrap justify-center lg:!justify-start">
              <span class="trackpos-badge"><i class="uil uil-cloud"></i> Cloud POS</span>
              <span class="trackpos-badge"><i class="uil uil-wifi-slash"></i> Offline Mode</span>
              <span class="trackpos-badge"><i class="uil uil-file-check-alt"></i> GST Compliant</span>
            </div>"""
    c = c.replace(
        "trusted by businesses all over India.</p>\n            <div class=\"flex justify-center",
        "trusted by businesses all over India.</p>" + badges + "\n            <div class=\"flex flex-wrap justify-center gap-2",
    )
    c = c.replace(
        "trusted by businesses all over India.</p>\n            <div class=\"flex justify-center",
        "trusted by businesses all over India.</p>" + badges + "\n            <motion class=\"flex flex-wrap justify-center gap-2",
    )

c = c.replace("Get Started</a></span>", "Book Free Demo</a>")
c = c.replace(
    '<span><a class="btn btn-lg btn-primary !text-white !bg-[#ff4450] border-[#ff4450] hover:text-white hover:bg-[#ff4450] hover:!border-[#ff4450]   active:text-white active:bg-[#ff4450] active:border-[#ff4450] disabled:text-white disabled:bg-[#ff4450] disabled:border-[#ff4450] rounded !mr-2">Book Free Demo</a>',
    '<a href="./contact.html" class="btn btn-lg btn-primary !text-white !bg-[#ff4450] border-[#ff4450] hover:text-white hover:bg-[#ff4450] hover:!border-[#ff4450] active:text-white active:bg-[#ff4450] active:border-[#ff4450] disabled:text-white disabled:bg-[#ff4450] disabled:border-[#ff4450] rounded">Book Free Demo</a>',
)
c = c.replace(
    '<span><a class="btn btn-lg btn-green !text-white !bg-[#002359] border-[#002359] hover:text-white hover:bg-[#002359] hover:!border-[#002359]   active:text-white active:bg-[#002359] active:border-[#002359] disabled:text-white disabled:bg-[#002359] disabled:border-[#002359]  rounded">Free Trial</a></span>',
    '<a href="./contact.html" class="btn btn-lg btn-green !text-white !bg-[#002359] border-[#002359] hover:text-white hover:bg-[#002359] hover:!border-[#002359] active:text-white active:bg-[#002359] active:border-[#002359] disabled:text-white disabled:bg-[#002359] disabled:border-[#002359] rounded">Start Free Trial</a>\n              <a href="https://wa.me/919348457123" target="_blank" rel="noopener" class="btn btn-lg btn-outline-primary !rounded">WhatsApp</a>',
)

c = c.replace("Trusted by Over 5000 Clients", "Trusted by Businesses Across India")
c = c.replace("Why Choose Sandbox?", "Why Choose TrackPOSSystem?")
c = c.replace(
    "Here are a few reasons why our customers choose Sandbox.",
    "Industry-specific workflows, GST compliance, and affordable pricing built for Indian SMEs.",
)

c = c.replace("<h4 class=\"!mb-[.25rem]\">Easy Usage</h4>", "<h4 class=\"!mb-[.25rem]\">Jewellery POS</h4>")
c = c.replace("<h4 class=\"!mb-[.25rem]\">Fast Transactions</h4>", "<h4 class=\"!mb-[.25rem]\">Restaurant POS</h4>")
c = c.replace("<h4 class=\"!mb-[.25rem]\">Secure Payments</h4>", "<h4 class=\"!mb-[.25rem]\">Retail & GST</h4>")
c = c.replace("Duis mollis commodo luctus cursus commodo tortor mauris.", "Gold rates, hallmark, karigar & repair orders.")
c = c.replace("Vivamus sagittis lacus augue fusce dapibus tellus nibh.", "KDS, table management & Swiggy/Zomato integration.")
c = c.replace("Vestibulum ligula porta felis maecenas faucibus mollis.", "Barcode billing, multi-warehouse & GSTR reports.")
c = c.replace("<h2 class=\"!mb-3 !leading-[1.35]\">Easy Usage</h2>", "<h2 class=\"!mb-3 !leading-[1.35]\">Jewellery POS</h2>")
c = c.replace("<h2 class=\"!mb-3 !leading-[1.35]\">Fast Transactions</h2>", "<h2 class=\"!mb-3 !leading-[1.35]\">Restaurant POS</h2>")
c = c.replace("<h2 class=\"!mb-3 !leading-[1.35]\">Secure Payments</h2>", "<h2 class=\"!mb-3 !leading-[1.35]\">Retail & GST Billing</h2>")

c = c.replace("We offer great and premium prices.", "Transparent pricing for every business size.")
c = c.replace("free 30-day trial", "free 14-day trial")
c = c.replace('<span class="price-currency">$</span><span class="price-value">19</span>', '<span class="price-currency">₹</span><span class="price-value">600</span>')
c = c.replace('<span class="price-currency">$</span><span class="price-value">199</span>', '<span class="price-currency">₹</span><span class="price-value">7200</span>')
c = c.replace('<span class="price-currency">$</span><span class="price-value">49</span>', '<span class="price-currency">₹</span><span class="price-value">1000</span>')
c = c.replace('<span class="price-currency">$</span><span class="price-value">499</span>', '<span class="price-currency">₹</span><span class="price-value">12000</span>')
c = c.replace("<h4 class=\"card-title !mt-2\">Premium Plan</h4>", "<h4 class=\"card-title !mt-2\">Regular Plan</h4>")
c = c.replace("<h4 class=\"card-title !mt-2\">Corporate Plan</h4>", "<h4 class=\"card-title !mt-2\">Diamond Plan</h4>")

c = c.replace("How do I get my subscription receipt?", "Does TrackPOSSystem work offline?")
c = c.replace("Are there any discounts for people in need?", "Can I manage multiple stores and warehouses?")
c = c.replace("Do you offer a free trial edit?", "Does TrackPOSSystem support GST billing and GSTR reports?")
c = c.replace("How do I reset my Account password?", "Does it support barcode printers and WhatsApp billing?")

c = c.replace(
    "Sandbox is a multipurpose HTML5 template with various layouts which will be a great solution for your business.",
    "TrackPOSSystem is industry-specific POS & business management software for jewellery, restaurant, hotel and retail businesses in India.",
)
c = c.replace("Moonshine St. 14/05 <br> Light City, London", "Serving businesses all over India")
c = c.replace('href="mailto:first.last@email.com">info@email.com', 'href="mailto:sales@trackpossystem.com">sales@trackpossystem.com')
c = c.replace("00 (123) 456 78 90", "+91-9348457123")
c = c.replace("© 2024 Sandbox.", "© 2024-2026 TrackPOSSystem.")
c = c.replace("Moonshine St. 14/05 Light City, London, United Kingdom", "Serving businesses all over India")
c = c.replace('href="#">About Us</a>', 'href="./about.html">About Us</a>')
c = c.replace('href="#">Our Story</a>', 'href="./about.html">Our Story</a>')
c = c.replace('href="#">Terms of Use</a>', 'href="./terms.html">Terms of Use</a>')

if 'id="features"' not in c:
    c = c.replace(
        'uppercase !text-[#aab0bc] !text-center !mb-8">Trusted by Businesses Across India</h2>',
        'uppercase !text-[#aab0bc] !text-center !mb-8" id="features">Trusted by Businesses Across India</h2>',
        1,
    )
if 'id="pricing"' not in c:
    c = c.replace(
        '<h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3 !tracking-[0.02rem] !leading-[1.35]">Our Pricing</h2>',
        '<h2 id="pricing" class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3 !tracking-[0.02rem] !leading-[1.35]">Our Pricing</h2>',
        1,
    )

if "trackpos-float-whatsapp" not in c:
    float_btns = """
  <a href="https://wa.me/919348457123" class="trackpos-float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="uil uil-whatsapp before:content-['\ed9a']"></i></a>
  <a href="tel:+919348457123" class="trackpos-float-call" aria-label="Call us"><i class="uil uil-phone before:content-['\ec51']"></i></a>
"""
    c = c.replace("<script src=\"./assets/js/plugins.js\"></script>", float_btns + "  <script src=\"./assets/js/plugins.js\"></script>")

names_roles = [
    ("Sanatana Jena", "Founder, Prabhas Foundations"),
    ("Rajesh Malick", "Proprietor"),
    ("Laxmikanta Pratihari", "Proprietor"),
    ("Chandrasekhar Samal", "Proprietor"),
]
for name, role in names_roles:
    c = c.replace('<h5 class="!mb-1 text-[.95rem] !leading-[1.5]">Coriss Ambady</h5>', f'<h5 class="!mb-1 text-[.95rem] !leading-[1.5]">{name}</h5>', 1)
    c = c.replace('<p class="!mb-0 !text-[.8rem]">Financial Analyst</p>', f'<p class="!mb-0 !text-[.8rem]">{role}</p>', 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("Content patch complete")
