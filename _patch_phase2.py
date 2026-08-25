#!/usr/bin/env python3
"""Phase 2: SEO head, integrations, stats, testimonials, how-it-works."""
import re

path = "/Users/rajeshjena/Downloads/trackpos-main-site/dist/index.html"

with open(path, "r", encoding="utf-8") as f:
    c = f.read()

if "trackpossystem.com/" not in c[:2500]:
    c = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="TrackPOSSystem — industry-specific POS & business management software for jewellery, restaurant, hotel & retail. Cloud + offline, GST billing, free 14-day trial.">',
        c, count=1,
    )
    c = re.sub(
        r'<meta name="keywords" content="[^"]*">',
        '<meta name="keywords" content="TrackPOSSystem, POS software India, jewellery POS, restaurant billing, hotel management, retail GST billing, offline POS">',
        c, count=1,
    )
    c = c.replace('<meta name="author" content="elemis">', "")
    c = re.sub(
        r"<title>[^<]*</title>",
        "<title>TrackPOSSystem | Industry-Specific POS & Business Management Software India</title>",
        c, count=1,
    )
    seo = """
  <meta property="og:title" content="TrackPOSSystem | Industry-Specific POS Software India">
  <meta property="og:description" content="Cloud & offline POS for jewellery, restaurant, hotel & retail. GST billing, inventory, CRM. Free 14-day trial.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://trackpossystem.com/">
  <link rel="canonical" href="https://trackpossystem.com/">
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"SoftwareApplication","name":"TrackPOSSystem","applicationCategory":"BusinessApplication","operatingSystem":"Web, Windows","offers":{"@type":"Offer","price":"600","priceCurrency":"INR"},"description":"Industry-specific POS and business management software for Indian SMEs."}
  </script>"""
    c = c.replace("</title>", "</title>" + seo, 1)

if "trackpos.css" not in c:
    c = c.replace(
        '<link rel="stylesheet" href="./style.css">',
        '<link rel="stylesheet" href="./style.css">\n  <link rel="stylesheet" href="./assets/css/trackpos.css">',
        1,
    )

c = c.replace(
    '<a href="./index.html">\n              <img src="./assets/img/logo.png" srcset="./assets/img/logo@2x.png 2x" alt="image">\n            </a>',
    '<a href="./index.html"><img class="trackpos-logo-img" src="./assets/img/qubextrack-logo.png?v=20260822" alt="QubexTrack"></a>',
)

if "Businesses Served" not in c:
    m = re.search(
        r'        <motion class="xl:!px-5 lg:!px-5 !mb-\[4\.5rem\][\s\S]*?        <!-- /div -->',
        c,
    )
    if not m:
        m = re.search(
            r'        <div class="xl:!px-5 lg:!px-5 !mb-\[4\.5rem\][\s\S]*?        <!-- /div -->',
            c,
        )
    if m:
        stats = """        <motion class="flex flex-wrap mx-[-15px] justify-center !mb-10 counter-wrapper">
          <div class="md:w-4/12 lg:w-3/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !text-center !mb-6">
            <h3 class="counter counter-lg !text-[calc(1.345rem_+_1.14vw)] !mb-2 xl:!text-[2.2rem] !text-[#ff4450]">500</h3>
            <p class="!mb-0 !text-[0.85rem] font-medium">Businesses Served</p>
          </div>
          <div class="md:w-4/12 lg:w-3/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !text-center !mb-6">
            <h3 class="counter counter-lg !text-[calc(1.345rem_+_1.14vw)] !mb-2 xl:!text-[2.2rem] !text-[#ff4450]">6</h3>
            <p class="!mb-0 !text-[0.85rem] font-medium">Industry Solutions</p>
          </div>
          <div class="md:w-4/12 lg:w-3/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !text-center !mb-6">
            <h3 class="!text-[calc(1.345rem_+_1.14vw)] !mb-2 xl:!text-[2.2rem] !text-[#ff4450]">GST</h3>
            <p class="!mb-0 !text-[0.85rem] font-medium">Compliant Billing</p>
          </div>
          <div class="md:w-4/12 lg:w-3/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !text-center !mb-6">
            <h3 class="!text-[calc(1.345rem_+_1.14vw)] !mb-2 xl:!text-[2.2rem] !text-[#ff4450]">24/7</h3>
            <p class="!mb-0 !text-[0.85rem] font-medium">Support Available</p>
          </div>
        </div>
        <!-- /stats -->"""
        stats = stats.replace("<motion class=", "<div class=")
        c = c[:m.start()] + stats + c[m.end():]

if 'id="integrations"' not in c:
    integrations = """
    <section class="wrapper !bg-[#ffffff]" id="integrations">
      <div class="container py-16 xl:!py-20">
        <div class="flex flex-wrap mx-[-15px] !text-center !mb-10">
          <div class="w-full flex-[0_0_auto] !px-[15px] max-w-full lg:w-8/12 xl:w-7/12 !mx-auto">
            <h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3">Integrations</h2>
            <h3 class="xl:!text-[2rem] !font-DMSerif !mb-3">Connect with the tools you already use</h3>
            <p class="lead !mb-0">WhatsApp billing, payment gateways, food aggregators, GST, barcode & thermal printers.</p>
          </div>
        </div>
        <div class="flex flex-wrap mx-[-15px] justify-center !mt-[-20px]">
          <div class="md:w-4/12 lg:w-2/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[20px] !text-center">
            <div class="icon btn btn-circle btn-lg btn-soft-green !mx-auto !mb-2"><i class="uil uil-whatsapp before:content-['\ed9a'] !text-[1.3rem]"></i></motion>
            <p class="!mb-0 !text-[0.8rem] font-medium">WhatsApp</p>
          </div>
          <div class="md:w-4/12 lg:w-2/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[20px] !text-center">
            <div class="icon btn btn-circle btn-lg btn-soft-primary !mx-auto !mb-2"><i class="uil uil-credit-card !text-[1.3rem]"></i></div>
            <p class="!mb-0 !text-[0.8rem] font-medium">Razorpay</p>
          </div>
          <div class="md:w-4/12 lg:w-2/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[20px] !text-center">
            <div class="icon btn btn-circle btn-lg btn-soft-yellow !mx-auto !mb-2"><i class="uil uil-restaurant !text-[1.3rem]"></i></div>
            <p class="!mb-0 !text-[0.8rem] font-medium">Swiggy / Zomato</p>
          </div>
          <div class="md:w-4/12 lg:w-2/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[20px] !text-center">
            <div class="icon btn btn-circle btn-lg btn-soft-red !mx-auto !mb-2"><i class="uil uil-file-check-alt !text-[1.3rem]"></i></div>
            <p class="!mb-0 !text-[0.8rem] font-medium">GST / GSTR</p>
          </div>
          <div class="md:w-4/12 lg:w-2/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[20px] !text-center">
            <div class="icon btn btn-circle btn-lg btn-soft-primary !mx-auto !mb-2"><i class="uil uil-print !text-[1.3rem]"></i></div>
            <p class="!mb-0 !text-[0.8rem] font-medium">Barcode Printers</p>
          </div>
          <div class="md:w-4/12 lg:w-2/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[20px] !text-center">
            <motion class="icon btn btn-circle btn-lg btn-soft-green !mx-auto !mb-2"><i class="uil uil-cloud !text-[1.3rem]"></i></div>
            <p class="!mb-0 !text-[0.8rem] font-medium">Cloud Sync</p>
          </div>
        </div>
      </div>
    </section>
    <!-- /integrations -->
"""
    integrations = integrations.replace("<motion class=", "<div class=").replace("</motion>", "</div>")
    marker = '    <section class="wrapper !bg-[#f5f5ff]">\n      <div class="container py-[4.5rem] xl:!py-28 lg:!py-28 md:!py-28">\n        <div class="flex flex-wrap mx-[-15px] xl:!mt-[-22.5rem]'
    if marker in c:
        c = c.replace(marker, integrations + "\n" + marker, 1)

quotes = [
    ("Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Vestibulum id ligula porta felis euismod semper. Cras justo odio dapibus facilisis sociis natoque penatibus.", "TrackPOSSystem simplified our billing and inventory. The offline mode is a lifesaver during power cuts. Highly recommended for jewellery stores."),
    ("Fusce dapibus, tellus ac cursus tortor mauris condimentum fermentum massa justo sit amet. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Cras mattis consectetur purus sit amet fermentum. Aenean lacinia bibendum nulla sed consectetur.", "We switched from manual billing to TrackPOSSystem. KOT printing and table management made our restaurant operations much smoother."),
    ("Curabitur blandit tempus porttitor. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Nullam quis risus eget porta ac consectetur vestibulum. Donec sed odio dui consectetur adipiscing elit.", "GST reports and barcode billing work perfectly for our retail store. Support team responds quickly on WhatsApp."),
    ("Etiam adipiscing tincidunt elit convallis felis suscipit ut. Phasellus rhoncus tincidunt auctor. Nullam eu sagittis mauris. Donec non dolor ac elit aliquam tincidunt at at sapien. Aenean tortor libero condimentum ac laoreet vitae.", "Affordable pricing with all features we need. Multi-store inventory sync saves us hours every week."),
    ("Maecenas sed diam eget risus varius blandit sit amet non magna. Cum sociis natoque penatibus magnis dis montes, nascetur ridiculus mus. Donec sed odio dui. Nulla vitae elit libero a pharetra.", "Easy to learn for staff. We started billing on day one after a short demo. Great value for money."),
    ("Donec id elit non mi porta gravida at eget metus. Nulla vitae elit libero, a pharetra augue. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.", "TrackPOSSystem handles our pharmacy batch tracking and expiry alerts reliably. Billing is fast at the counter."),
]
for old, new in quotes:
    c = c.replace(old, new, 1)

c = c.replace("Cory Zamora", "Laxmikanta Pratihari")
c = c.replace("Marketing Specialist", "Proprietor", 1)
c = c.replace("Nikolas Brooten", "Chandrasekhar Samal")
c = c.replace("Sales Manager", "Proprietor", 1)
c = c.replace("Jackie Sanders", "Deepak Sahoo")
c = c.replace("Investment Planner", "Co-Founder, TrackPOSSystem", 1)
c = c.replace("Laura Widerski", "Jonas Bubhan")
c = c.replace("Sales Specialist", "Co-Founder, TrackPOSSystem", 1)

c = c.replace("Here are the 3 working steps on success.", "Get started with TrackPOSSystem in three simple steps.")
c = c.replace("<h4 class=\"!mb-1\">Secured Transactions</h4>", "<h4 class=\"!mb-1\">Book a Free Demo</h4>")
c = c.replace("<p class=\"!mb-0\">Nulla vitae elit libero pharetra augue dapibus. Praesent commodo cursus.</p>", "<p class=\"!mb-0\">Schedule a personalised demo for your industry — jewellery, restaurant, hotel or retail.</p>", 1)
c = c.replace("<h4 class=\"!mb-1\">Bills Planning</h4>", "<h4 class=\"!mb-1\">Start Free Trial</h4>")
c = c.replace("<p class=\"!mb-0\">Vivamus sagittis lacus vel augue laoreet. Etiam porta sem malesuada magna.</p>", "<p class=\"!mb-0\">Get full access for 14 days. Cloud & offline. No credit card required.</p>", 1)
c = c.replace("<h4 class=\"!mb-1\">Always up to date</h4>", "<h4 class=\"!mb-1\">Go Live & Grow</h4>")
c = c.replace("<p class=\"!mb-0\">Cras mattis consectetur purus sit amet. Aenean lacinia bibendum nulla sed.</p>", "<p class=\"!mb-0\">Bill faster, manage inventory, and grow with GST reports and dedicated support.</p>", 1)

c = c.replace(
    "Etiam porta sem malesuada magna mollis euismod. Donec ullamcorper nulla non metus auctor fringilla. Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Nullam quis risus eget urna.",
    "Fast barcode billing, multi-warehouse inventory, customer loyalty, purchase & sales management, expense tracking, and GSTR-1 / GSTR-3B reports — all in one retail POS.",
)
c = c.replace("Aenean eu leo quam. Pellentesque ornare.", "Barcode, name & code wise billing")
c = c.replace("Nullam quis risus eget urna mollis ornare.", "Multi-store & warehouse management")
c = c.replace("Donec id elit non mi porta gravida at eget.", "GSTR-1, GSTR-3B & GST invoices")

c = c.replace('href="#" class="btn btn-red', 'href="./retail-billing-software.html" class="btn btn-red')
c = c.replace('Enjoy a <a href="#" class="hover', 'Enjoy a <a href="./contact.html" class="hover')
c = c.replace('href="#" class="btn btn-primary !text-white !bg-[#ff4450] border-[#ff4450] hover:text-white hover:bg-[#ff4450] hover:!border-[#ff4450]   active:text-white active:bg-[#ff4450] active:border-[#ff4450] disabled:text-white disabled:bg-[#ff4450] disabled:border-[#ff4450] !text-[.85rem] !rounded-[.4rem] !mt-2', 'href="./pricing.html" class="btn btn-primary !text-white !bg-[#ff4450] border-[#ff4450] hover:text-white hover:bg-[#ff4450] hover:!border-[#ff4450]   active:text-white active:bg-[#ff4450] active:border-[#ff4450] disabled:text-white disabled:bg-[#ff4450] disabled:border-[#ff4450] !text-[.85rem] !rounded-[.4rem] !mt-2', 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("Phase 2 patch complete")
