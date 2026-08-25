#!/usr/bin/env python3
"""Realign about.html with trackpossystem.com content and site nav/footer."""
import re

DIST = "/Users/rajeshjena/Downloads/trackpos-main-site/dist"

def load(name):
    with open(f"{DIST}/{name}", encoding="utf-8") as f:
        return f.read()

def save(name, content):
    with open(f"{DIST}/{name}", "w", encoding="utf-8") as f:
        f.write(content)

contact = load("contact.html")
about = load("about.html")

def replace_block(text, open_tag, close_tag, replacement):
    i = text.find(open_tag)
    if i < 0:
        return text
    j = text.find(close_tag, i)
    if j < 0:
        return text
    j += len(close_tag)
    return text[:i] + replacement + text[j:]

header_m = re.search(r"<header class=.*?</header>", contact, re.DOTALL)
footer_m = re.search(r"<footer class=.*?</footer>", contact, re.DOTALL)
if header_m:
    about = replace_block(about, "<header class=", "</header>", header_m.group(0))
if footer_m:
    about = replace_block(about, "<footer class=", "</footer>", footer_m.group(0))

# Body class
about = about.replace("<body>", '<body class="[word-spacing:.05rem!important] font-Manrope text-[0.8rem] !leading-[1.7] font-medium">')

# Meta
about = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Learn about TrackPOSSystem — cloud-based POS & business management for jewellery, restaurant, hotel and retail, trusted by businesses all over India. Free 14-day trial.">',
    about,
    count=1,
)

# Hero
about = about.replace(
    "<h1 class=\"!text-[calc(1.365rem_+_1.38vw)] font-bold !leading-[1.2] xl:!text-[2.4rem] !mb-4\">Hello! This is Sandbox</h1>",
    "<h1 class=\"!text-[calc(1.365rem_+_1.38vw)] font-bold !leading-[1.2] xl:!text-[2.4rem] !mb-4\">About TrackPOSSystem</h1>",
)
about = about.replace(
    "<p class=\"lead text-[1.05rem] !leading-[1.6] font-medium !mb-0\">A company turning ideas into beautiful things.</p>",
    "<p class=\"lead text-[1.05rem] !leading-[1.6] font-medium !mb-0\">Cloud-based POS billing software for Indian SMEs — desktop, tablet &amp; mobile.</p>",
)

# Who Are We
about = about.replace(
    "<h2 class=\"!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-3\">Who Are We?</h2>",
    "<h2 class=\"!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-3\">Our Story</h2>",
)
about = about.replace(
    "<p class=\"lead !text-[1.05rem] !leading-[1.6] font-medium\">We are a digital and branding company that believes in the power of creative strategy and along with great design.</p>",
    "<p class=\"lead !text-[1.05rem] !leading-[1.6] font-medium\">We're knowledgeable about making benefits higher — supporting businesses with affordable, industry-specific POS software.</p>",
)
about = about.replace(
    "<p class=\"!mb-6\">Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Praesent commodo cursus magna, vel scelerisque nisl consectetur et.</p>",
    "<p class=\"!mb-6\">Track POS System (TPS) is revolutionizing retail by empowering jewellery, restaurant, hotel and retail businesses with smart, cloud-based POS solutions. For small and medium enterprises, finding a reliable POS that scales with growth has always been a challenge — TPS bridges that gap with comprehensive, affordable software tailored to Indian SMEs. From day one of onboarding, you'll notice a positive transformation: billing, inventory, accounting and GST reporting follow a standardized process that makes it easier to manage and grow your business.</p>",
)

bullets = [
    ("Aenean eu leo quam ornare curabitur blandit tempus.", "GST-compliant billing, inventory &amp; GSTR reports"),
    ("Nullam quis risus eget urna mollis ornare donec elit.", "Industry-specific modules for 4 verticals"),
    ("Etiam porta sem malesuada magna mollis euismod.", "Cloud sync across desktop, tablet &amp; mobile"),
    ("Fermentum massa vivamus faucibus amet euismod.", "Transparent pricing from ₹600/month + free trial"),
]
for old, new in bullets:
    about = about.replace(f"<span>{old}</span>", f"<span>{new}</span>")

# 3 steps section
about = about.replace(
    "<h2 class=\"!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-4 xl:!px-[4.5rem] lg:!px-[4.5rem]\">Here are 3 working steps to organize our business projects.</h2>",
    "<h2 class=\"!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-4 xl:!px-[4.5rem] lg:!px-[4.5rem]\">Get started with TrackPOSSystem in 3 simple steps.</h2>",
)
steps = [
    ("Collect Ideas", "Book a Demo", "Share your business type and requirements with our team."),
    ("Data Analysis", "Setup & Training", "We configure GST, inventory, users and train your staff."),
    ("Finalize Product", "Go Live", "Start billing on desktop, tablet or mobile with ongoing support."),
]
for title_old, title_new, desc_new in steps:
    about = about.replace(f"<h4 class=\"!mb-1\">{title_old}</h4>", f"<h4 class=\"!mb-1\">{title_new}</h4>", 1)
    # replace next p after each h4 - do desc via paired replace
for i, (_, _, desc) in enumerate(steps):
    pass

about = about.replace(
    "<p class=\"!mb-0\">Nulla vitae elit libero pharetra augue dapibus.</p>",
    "<p class=\"!mb-0\">Share your business type and requirements with our team.</p>",
    1,
)
about = about.replace(
    "<p class=\"!mb-0\">Vivamus sagittis lacus vel augue laoreet.</p>",
    "<p class=\"!mb-0\">We configure GST, inventory, users and train your staff.</p>",
    1,
)
about = about.replace(
    "<p class=\"!mb-0\">Cras mattis consectetur purus sit amet.</p>",
    "<p class=\"!mb-0\">Start billing on desktop, tablet or mobile with ongoing support.</p>",
    1,
)

# How It Works sidebar
about = about.replace(
    "<p class=\"lead text-[1rem] xl:!pr-5 lg:!pr-5\">Find out everything you need to know and more about how we create our business process models.</p>",
    "<p class=\"lead text-[1rem] xl:!pr-5 lg:!pr-5\">TrackPOSSystem serves as a comprehensive billing solution for retailers, wholesalers, distributors, restaurants and hotels across India.</p>",
)
about = about.replace(
    "<p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare.</p>",
    "<p>A strong emphasis on industry-specific POS features, deep expertise in retail software, and affordable transparent pricing stand out TPS among competitors. Our pricing is designed to be flexible — whether you're a small shop or a growing chain, you get excellent value without compromising on quality.</p>",
)
about = about.replace(
    "<p class=\"!mb-6\">Nullam id dolor id nibh ultricies vehicula ut id elit. Vestibulum id ligula porta felis euismod semper. Aenean lacinia bibendum nulla sed consectetur. Sed posuere consectetur est at lobortis. Vestibulum id ligula porta felis.</p>",
    "<p class=\"!mb-6\">Complete solutions for billing, inventory, purchase &amp; sales, CRM, loyalty, accounting and GST — with dedicated support when you need it. Start with a free 14-day trial and see the difference from day one.</p>",
)
about = about.replace(
    '<a href="#" class="btn btn-primary',
    '<a href="./contact.html" class="btn btn-primary',
    1,
)
about = about.replace(">Learn More</a>", ">Request Free Trial</a>", 1)

# Testimonials swiper
testimonials = [
    (
        "“Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Vestibulum ligula porta felis euismod semper. Cras justo odio consectetur nulla dapibus curabitur blandit.”",
        "“TrackPOSSystem simplified our billing and inventory. GST reports and daily summaries are accurate. Highly recommended for jewellery stores.”",
        "Coriss Ambady", "Sanatana Jena",
        "Founder & CEO", "Founder, Prabhas Foundations",
    ),
    (
        "“Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Vestibulum ligula porta felis euismod semper. Cras justo odio consectetur adipiscing dapibus curabitur blandit.”",
        "“We switched from manual billing to TrackPOSSystem. KOT printing and table management made our restaurant operations much smoother.”",
        "Cory Zamora", "Laxmikanta Pratihari",
        "Co-Founder", "Proprietor",
    ),
    (
        "“Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Vestibulum ligula porta felis euismod semper. Cras justo odio consectetur adipiscing dapibus curabitur blandit.”",
        "“GST reports and barcode billing work perfectly for our retail store. Support team responds quickly on WhatsApp.”",
        "Nikolas Brooten", "Chandrasekhar Samal",
        "Sales Manager", "Proprietor",
    ),
]
for old_q, new_q, old_n, new_n, old_r, new_r in testimonials:
    about = about.replace(f"<p>{old_q}</p>", f"<p>{new_q}</p>", 1)
    about = about.replace(f"<h5 class=\"!mb-1 text-[.95rem] !leading-[1.5]\">{old_n}</h5>", f"<h5 class=\"!mb-1 text-[.95rem] !leading-[1.5]\">{new_n}</h5>", 1)
    about = about.replace(f"<p class=\"!mb-0 text-[0.8rem]\">{old_r}</p>", f"<p class=\"!mb-0 text-[0.8rem]\">{new_r}</p>", 1)

# Team heading
about = about.replace(
    "<h2 class=\"!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-3 xl:!px-[4.5rem] lg:!px-[4.5rem]\">Meet the team behind TrackPOSSystem.</h2>",
    "<h2 class=\"!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-3 xl:!px-[4.5rem] lg:!px-[4.5rem]\">Meet the team behind TrackPOSSystem</h2>",
)

team_updates = [
    ("Rajesh Kumar Sethy", "Founder & CEO", "Sales & Marketing",
     "Key driver in promoting our products and building strong customer relationships across India."),
    ("Ranjan Giri", "Co-Founder", "Business Development Lead",
     "Identifies new markets, builds client relationships and develops strategies for long-term growth."),
    ("Deepak Sahoo", "Sales Manager", "Technical Lead",
     "Ensures seamless system functionality, technical support and innovative feature development."),
]
# Fix team cards - order in file: te1 Rajesh, te2 Jonas, te3 Nikolas->Deepak, te4 Jackie->remove later
about = about.replace(
    '<div class="!text-[0.65rem] !mb-2 uppercase !tracking-[0.02rem] font-bold !text-[#aab0bc]">Founder & CEO</div>',
    '<div class="!text-[0.65rem] !mb-2 uppercase !tracking-[0.02rem] font-bold !text-[#aab0bc]">Sales & Marketing</div>',
    1,
)
about = about.replace(
    '<div class="!text-[0.65rem] !mb-2 uppercase !tracking-[0.02rem] font-bold !text-[#aab0bc]">Co-Founder</div>',
    '<div class="!text-[0.65rem] !mb-2 uppercase !tracking-[0.02rem] font-bold !text-[#aab0bc]">Business Development Lead</div>',
    1,
)
about = about.replace("<h4 class=\"!mb-1\">Nikolas Brooten</h4>", "<h4 class=\"!mb-1\">Deepak Sahoo</h4>")
about = about.replace(
    '<div class="!text-[0.65rem] !mb-2 uppercase !tracking-[0.02rem] font-bold !text-[#aab0bc]">Sales Manager</div>',
    '<div class="!text-[0.65rem] !mb-2 uppercase !tracking-[0.02rem] font-bold !text-[#aab0bc]">Technical Lead</div>',
    1,
)
about = about.replace(
    "<p class=\"!mb-2\">Building industry-specific POS solutions for Indian SMEs.</p>",
    "<p class=\"!mb-2\">Key driver in promoting our products and building strong customer relationships across India.</p>",
    1,
)
about = about.replace(
    "<p class=\"!mb-2\">Fermentum massa justo sit amet risus morbi leo.</p>",
    "<p class=\"!mb-2\">Identifies new markets, builds client relationships and develops strategies for long-term growth.</p>",
    1,
)
about = about.replace(
    "<p class=\"!mb-2\">Fermentum massa justo sit amet risus morbi leo.</p>",
    "<p class=\"!mb-2\">Ensures seamless system functionality, technical support and innovative feature development.</p>",
    1,
)

# Remove extra team slides (Jackie, Laura, Tina) - keep first 3 only
team_start = about.find('<div class="swiper-wrapper">', about.find("Meet the team"))
team_end = about.find("</div>\n              <!--/.swiper-wrapper -->", team_start)
if team_start > 0 and team_end > team_start:
    wrapper_inner = about[team_start:team_end]
    slides = re.findall(r'<div class="swiper-slide">.*?</div>\s*<!--/\.swiper-slide -->', wrapper_inner, re.DOTALL)
    if len(slides) >= 3:
        new_wrapper = '<div class="swiper-wrapper">\n' + "\n".join(slides[:3]) + "\n"
        about = about[:team_start] + new_wrapper + about[team_end:]

# Stats
about = about.replace("<h3 class=\"counter xl:!text-[2rem]", "<h3 class=\"counter xl:!text-[2rem]", 4)  # noop anchor
about = about.replace(">7518</h3>", ">500</h3>")
about = about.replace(">3472</h3>", ">4</h3>")
about = about.replace(">2184</h3>", ">24</h3>")
about = about.replace(">4523</h3>", ">14</h3>")
about = about.replace(">Completed Projects</p>", ">Businesses Served</p>")
about = about.replace(">Satisfied Customers</p>", ">Industry Solutions</p>")
about = about.replace(">Expert Employees</p>", ">Hour Support</p>")
about = about.replace(">Awards Won</p>", ">Day Free Trial</p>")

# Bottom contact CTA
about = about.replace(
    "<h2 class=\"!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-8\">Convinced yet? Let's make something great together.</h2>",
    "<h2 class=\"!text-[calc(1.305rem_+_0.66vw)] font-bold xl:!text-[1.8rem] !leading-[1.3] !mb-8\">Ready to transform your business with TrackPOSSystem?</h2>",
)
about = about.replace(
    "<address class=\" not-italic !leading-[inherit] !mb-4\">Moonshine St. 14/05 Light City, <br class=\"hidden xl:block lg:block md:block\">London, United Kingdom</address>",
    "<address class=\" not-italic !leading-[inherit] !mb-4\">Serving businesses all over India</address>",
)
about = about.replace(
    '<p class="!mb-0"><a href="mailto:sandbox@email.com" class="!text-[#60697b]">sandbox@email.com</a></p>',
    '<p class="!mb-0"><a href="mailto:sales@trackpossystem.com" class="!text-[#60697b]">sales@trackpossystem.com</a></p>\n                <p class="!mb-0 !mt-1"><a href="mailto:support@trackpossystem.com" class="!text-[#60697b]">support@trackpossystem.com</a></p>',
)

# Offcanvas emails in mobile nav (if header sync missed)
about = about.replace('href="mailto:first.last@email.com"', 'href="mailto:sales@trackpossystem.com"')
about = about.replace("info@email.com", "sales@trackpossystem.com")

save("about.html", about)
print("Patched about.html")
