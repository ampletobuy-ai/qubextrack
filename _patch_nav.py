import re

path = "/Users/rajeshjena/Downloads/trackpos-main-site/dist/index.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

new_nav = """<ul class="navbar-nav">
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
                <li class="nav-item"><a class="nav-link" href="./index.html#pricing">Pricing</a></li>
                <li class="nav-item"><a class="nav-link" href="./index.html#integrations">Integrations</a></li>
                <li class="nav-item"><a class="nav-link" href="./about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="./contact.html">Contact</a></li>
              </ul>
              <!-- /.navbar-nav -->"""

content = re.sub(
    r"<ul class=\"navbar-nav\">.*?</ul>\s*<!-- /\.navbar-nav -->",
    new_nav,
    content,
    count=1,
    flags=re.DOTALL,
)

content = content.replace(
    '<h3 class="!text-white xl:!text-[1.5rem] !text-[calc(1.275rem_+_0.3vw)] !mb-0">Sandbox</h3>',
    '<h3 class="!text-white xl:!text-[1.5rem] !text-[calc(1.275rem_+_0.3vw)] !mb-0">TrackPOSSystem</h3>',
)

content = content.replace(
    '<a href="mailto:first.last@email.com" class="link-inverse">info@email.com</a>\n                  <br> 00 (123) 456 78 90 <br>',
    '<a href="mailto:sales@trackpossystem.com" class="link-inverse">sales@trackpossystem.com</a>\n                  <br> +91-9348457123 <br>',
)

content = content.replace(
    '<a href="#" class="btn btn-sm btn-primary !text-white !bg-[#ff4450] border-[#ff4450] hover:text-white hover:bg-[#ff4450] hover:!border-[#ff4450]   active:text-white active:bg-[#ff4450] active:border-[#ff4450] disabled:text-white disabled:bg-[#ff4450] disabled:border-[#ff4450] !rounded-[50rem]" data-bs-toggle="modal" data-bs-target="#modal-signin">Sign In</a>',
    '<a href="./contact.html" class="btn btn-sm btn-green !text-white !bg-[#002359] border-[#002359] hover:text-white hover:bg-[#002359] hover:!border-[#002359] active:text-white active:bg-[#002359] active:border-[#002359] disabled:text-white disabled:bg-[#002359] disabled:border-[#002359] !rounded-[50rem] !mr-2">Free Trial</a>\n                <a href="tel:+919348457123" class="btn btn-sm btn-primary !text-white !bg-[#ff4450] border-[#ff4450] hover:text-white hover:bg-[#ff4450] hover:!border-[#ff4450] active:text-white active:bg-[#ff4450] active:border-[#ff4450] disabled:text-white disabled:bg-[#ff4450] disabled:border-[#ff4450] !rounded-[50rem] hidden xl:block lg:block md:block">Call Us</a>',
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Nav patched OK")
