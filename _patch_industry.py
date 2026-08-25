#!/usr/bin/env python3
"""Insert industry solutions section into index.html"""
path = "/Users/rajeshjena/Downloads/trackpos-main-site/dist/index.html"

INDUSTRY_SECTION = """
    <section class="wrapper !bg-[#ffffff]" id="industries">
      <motion class="container py-[4.5rem] xl:!py-24 lg:!py-24 md:!py-24">
        <div class="flex flex-wrap mx-[-15px] !text-center !mb-10">
          <div class="w-full flex-[0_0_auto] !px-[15px] max-w-full lg:w-8/12 xl:w-7/12 !mx-auto">
            <h2 class="!text-[.75rem] uppercase !text-[#aab0bc] !mb-3 !tracking-[0.02rem]">Industry Solutions</h2>
            <h3 class="xl:!text-[2rem] !text-[calc(1.325rem_+_0.9vw)] !leading-[1.2] !font-DMSerif !font-normal !mb-3">Specialized software for your business type</h3>
            <p class="lead !mb-0">TrackPOSSystem is built for industry-specific workflows — not generic billing alone.</p>
          </div>
        </div>
        <div class="flex flex-wrap mx-[-15px] !mt-[-30px]">
          <div class="md:w-6/12 lg:w-4/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px]">
            <a href="./jewellery-pos-software.html" class="card industry-card h-full !shadow-[0_0.25rem_1.75rem_rgba(30,34,40,0.07)] !no-underline block">
              <div class="card-body p-8 text-center">
                <div class="icon btn btn-circle btn-lg btn-soft-primary !mb-4 !mx-auto"><i class="uil uil-diamond !text-[1.4rem]"></i></motion>
                <h4 class="!mb-2 !text-[#343f52]">Jewellery POS</h4>
                <p class="!mb-0 !text-[#60697b]">Gold rates, hallmark, karigar, repair orders &amp; GST billing.</p>
              </div>
            </a>
          </div>
          <div class="md:w-6/12 lg:w-4/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px]">
            <a href="./restaurant-pos-software.html" class="card industry-card h-full !shadow-[0_0.25rem_1.75rem_rgba(30,34,40,0.07)] !no-underline block">
              <div class="card-body p-8 text-center">
                <div class="icon btn btn-circle btn-lg btn-soft-green !mb-4 !mx-auto"><i class="uil uil-restaurant !text-[1.4rem]"></i></motion>
                <h4 class="!mb-2 !text-[#343f52]">Restaurant POS</h4>
                <p class="!mb-0 !text-[#60697b]">KDS, table management, KOT printing &amp; aggregator integration.</p>
              </div>
            </a>
          </div>
          <div class="md:w-6/12 lg:w-4/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px]">
            <a href="./hotel-management-software.html" class="card industry-card h-full !shadow-[0_0.25rem_1.75rem_rgba(30,34,40,0.07)] !no-underline block">
              <div class="card-body p-8 text-center">
                <motion class="icon btn btn-circle btn-lg btn-soft-yellow !mb-4 !mx-auto"><i class="uil uil-bed !text-[1.4rem]"></i></motion>
                <h4 class="!mb-2 !text-[#343f52]">Hotel Software</h4>
                <p class="!mb-0 !text-[#60697b]">Room booking, check-in/out, OTA integration &amp; guest CRM.</p>
              </div>
            </a>
          </div>
          <div class="md:w-6/12 lg:w-4/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px]">
            <a href="./retail-billing-software.html" class="card industry-card h-full !shadow-[0_0.25rem_1.75rem_rgba(30,34,40,0.07)] !no-underline block">
              <div class="card-body p-8 text-center">
                <div class="icon btn btn-circle btn-lg btn-soft-red !mb-4 !mx-auto"><i class="uil uil-store !text-[1.4rem]"></i></motion>
                <h4 class="!mb-2 !text-[#343f52]">Retail Billing</h4>
                <p class="!mb-0 !text-[#60697b]">Barcode billing, inventory, multi-store &amp; loyalty points.</p>
              </div>
            </a>
          </motion>
          <div class="md:w-6/12 lg:w-4/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px]">
            <a href="./pharmacy-pos-software.html" class="card industry-card h-full !shadow-[0_0.25rem_1.75rem_rgba(30,34,40,0.07)] !no-underline block">
              <div class="card-body p-8 text-center">
                <div class="icon btn btn-circle btn-lg btn-soft-primary !mb-4 !mx-auto"><i class="uil uil-medical-square !text-[1.4rem]"></i></motion>
                <h4 class="!mb-2 !text-[#343f52]">Pharmacy POS</h4>
                <p class="!mb-0 !text-[#60697b]">Batch tracking, expiry alerts &amp; GST-compliant pharmacy billing.</p>
              </div>
            </a>
          </div>
          <div class="md:w-6/12 lg:w-4/12 w-full flex-[0_0_auto] !px-[15px] max-w-full !mt-[30px]">
            <a href="./supermarket-pos-software.html" class="card industry-card h-full !shadow-[0_0.25rem_1.75rem_rgba(30,34,40,0.07)] !no-underline block">
              <div class="card-body p-8 text-center">
                <div class="icon btn btn-circle btn-lg btn-soft-green !mb-4 !mx-auto"><i class="uil uil-shopping-cart !text-[1.4rem]"></i></motion>
                <h4 class="!mb-2 !text-[#343f52]">Supermarket POS</h4>
                <p class="!mb-0 !text-[#60697b]">Fast checkout, barcode scanning &amp; multi-warehouse inventory.</p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </section>
    <!-- /section -->
"""

# Fix motion typos in template string - replace motion with div
INDUSTRY_SECTION = INDUSTRY_SECTION.replace("<motion", "<div").replace("</motion>", "</div>")

with open(path, "r", encoding="utf-8") as f:
    c = f.read()

marker = '    <section class="wrapper !bg-[#f5f5ff]">\n      <div class="container py-[4.5rem] xl:!py-28 lg:!py-28 md:!py-28">\n        <div class="flex flex-wrap mx-[-15px] xl:!mt-[-22.5rem]'
if 'id="industries"' not in c:
    c = c.replace(marker, INDUSTRY_SECTION + marker)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("Industry section inserted")
