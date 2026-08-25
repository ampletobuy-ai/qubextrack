#!/usr/bin/env python3
"""Rebuild terms.html content from Vyapar-style structure, adapted for TrackPOSSystem."""
import re

DIST = "/Users/rajeshjena/Downloads/trackpos-main-site/dist"
TERMS = f"{DIST}/terms.html"
CONTACT = f"{DIST}/contact.html"

SIDEBAR = """<ul class="pl-0 list-none text-inherit">
<li><a class="nav-link scroll active" href="#terms-of-service">1. Terms of Service</a></li>
<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#description-of-services">2. Description of Services</a></li>
<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#business-data">3. Business Data &amp; Privacy</a></li>
<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#data-ownership">4. Data Ownership</a></li>
<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#permissions">5. Permissions</a></li>
<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#data-security">6. Data Security</a></li>
<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#communications">7. Communications</a></li>
<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#refund-billing">8. Refund &amp; Billing</a></li>
<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#contact-us">9. Contact Us</a></li>
</ul>"""

SECTIONS = """
          <section id="terms-of-service" class="wrapper pt-24">
            <div class="card">
              <div class="card-body !p-10">
                <h2 class="!mb-3 !leading-[1.35]">1. Terms of Service</h2>
                <p class="lead !text-[1.05rem] !mb-4">TrackPOSSystem Terms &amp; Conditions and Privacy Policy</p>
                <p>We are dedicated to safeguarding your privacy. This document describes the terms under which you may use TrackPOSSystem (also known as <strong>Track POS System</strong> or <strong>TPS</strong>) — industry-specific POS and business management software for Indian businesses.</p>
                <p><strong>App / Service name:</strong> TrackPOSSystem — GST Billing, Inventory &amp; Business Management Software<br>
                <strong>Developer / Provider:</strong> TrackPOSSystem (trackpossystem.com)</p>
                <h3 class="!text-[1rem] !mb-2 !mt-4">General Agreement</h3>
                <p>Please review these Terms of Service (&quot;Agreement&quot;) carefully. This Agreement is a legal agreement between you (the &quot;User&quot;) and TrackPOSSystem. By accepting electronically (for example, clicking &quot;I Agree&quot;), installing, accessing, or using the Services, you agree to these terms. If you do not agree to this Agreement, you may not use the Services. This Agreement shall be governed by and construed in accordance with the laws of <strong>India</strong>.</p>
                <h3 class="!text-[1rem] !mb-2 !mt-4">Modification of Terms &amp; Conditions</h3>
                <p>These terms may be updated from time to time. You agree to review our Terms and Conditions regularly by visiting this page. Continued access to or use of the Service will mean that you agree to the updated terms.</p>
                <h3 class="!text-[1rem] !mb-2 !mt-4">When This Agreement Applies</h3>
                <p>This Agreement applies to users who download, install, register for, or use TrackPOSSystem software or services — including via our website, desktop application, or mobile apps — and who accept these Terms and Conditions.</p>
              </div>
            </div>
          </section>
          <section id="description-of-services" class="wrapper pt-24">
            <div class="card">
              <div class="card-body !p-10">
                <h2 class="!mb-3 !leading-[1.35]">2. Description of Services</h2>
                <p>We provide an array of services including inventory management, GST-compliant invoicing and billing, purchase &amp; sales management, reporting, customer &amp; supplier management, loyalty features, and industry-specific modules for jewellery, restaurant, hotel, and retail businesses (&quot;Service&quot; or &quot;Services&quot;). Together these serve as complete business management software for Indian SMEs.</p>
                <p>You may use the Services for your personal and business use, or for internal business purposes in the organization you represent. You may download the application from our official website or authorized distribution channels using the Internet. Where offline mode is supported, you may continue billing and data entry without an active internet connection; cloud sync and certain features may require connectivity.</p>
                <p>You are responsible for obtaining access to the Internet and the devices necessary to use the Services. TrackPOSSystem strives to help businesses remain compliant with GST and applicable laws, but <strong>it is solely your responsibility</strong> to ensure your business meets all statutory, tax, and regulatory requirements. TrackPOSSystem is not responsible for any non-compliance arising from your use of the software or from incorrect data entered by you or your staff.</p>
                <p>For paid subscription plans, the license period generally commences on or before <strong>60 days</strong> from the date of purchase unless otherwise stated at checkout. TrackPOSSystem reserves the right to adjust this grace period. A <strong>14-day free trial</strong> may be offered for evaluation; trial terms are described in our pricing and refund sections below.</p>
              </div>
            </div>
          </section>
          <section id="business-data" class="wrapper pt-24">
            <div class="card">
              <div class="card-body !p-10">
                <h2 class="!mb-3 !leading-[1.35]">3. Business Data &amp; Privacy</h2>
                <p>You alone are responsible for maintaining the confidentiality of your username, password, and other sensitive account information. You are responsible for all activities that occur under your user account and agree to inform us immediately of any unauthorized use of your account by emailing <a href="mailto:support@trackpossystem.com">support@trackpossystem.com</a> or calling <a href="tel:+919348457123">+91-9348457123</a>.</p>
                <p>We are not responsible for any loss or damage to you or any third party incurred as a result of unauthorized access to or use of your account. We are not responsible for any kind of data loss; performing necessary backups of your business data is your responsibility. TrackPOSSystem is not liable for data discrepancy or business loss arising from data entry errors, software misuse, or third-party integrations configured by you.</p>
              </div>
            </div>
          </section>
          <section id="data-ownership" class="wrapper pt-24">
            <div class="card">
              <div class="card-body !p-10">
                <h2 class="!mb-3 !leading-[1.35]">4. Data Ownership</h2>
                <p>You own the content you create or store in your account. We respect your right to ownership of invoices, inventory records, customer data, and other business information you enter into TrackPOSSystem.</p>
                <p>Your use of the Services grants TrackPOSSystem a limited license to use, reproduce, adapt, modify, publish, or distribute content stored in your account solely for operating, securing, and improving the Services (including backups, support, and internal analytics). We do not sell your business transaction data to third parties for advertising purposes.</p>
                <p>We take reasonable measures to keep your data safe but cannot guarantee absolute security against all threats. You should export or back up critical records periodically using built-in reports or export features where available.</p>
              </div>
            </div>
          </section>
          <section id="permissions" class="wrapper pt-24">
            <div class="card">
              <div class="card-body !p-10">
                <h2 class="!mb-3 !leading-[1.35]">5. Permissions</h2>
                <p>Depending on the platform (desktop, web, or mobile), TrackPOSSystem may request the following permissions to deliver core POS functionality:</p>
                <ul class="pl-0 list-none bullet-bg bullet-soft-primary !mb-4">
                  <li class="relative !mt-[0.35rem] flex items-start"><span class="pr-[.75rem]"><i class="uil uil-check w-4 h-4 text-[0.8rem] leading-none !tracking-[normal] !text-center flex justify-center items-center bg-[#ffe8ea] !text-[#ff4450] rounded-[100%] top-[0.2rem] before:content-['\\e9dd'] before:align-middle before:table-cell"></i></span><span><strong>Camera:</strong> To capture photos of bills, products, or documents to attach to transactions.</span></li>
                  <li class="relative !mt-[0.35rem] flex items-start"><span class="pr-[.75rem]"><i class="uil uil-check w-4 h-4 text-[0.8rem] leading-none !tracking-[normal] !text-center flex justify-center items-center bg-[#ffe8ea] !text-[#ff4450] rounded-[100%] top-[0.2rem] before:content-['\\e9dd'] before:align-middle before:table-cell"></i></span><span><strong>Storage:</strong> To save invoices, backups, exports, and application data on your device.</span></li>
                  <li class="relative !mt-[0.35rem] flex items-start"><span class="pr-[.75rem]"><i class="uil uil-check w-4 h-4 text-[0.8rem] leading-none !tracking-[normal] !text-center flex justify-center items-center bg-[#ffe8ea] !text-[#ff4450] rounded-[100%] top-[0.2rem] before:content-['\\e9dd'] before:align-middle before:table-cell"></i></span><span><strong>Contacts (optional):</strong> To import or sync customer/party contact details for faster billing. We do not upload personal contact books for unrelated purposes.</span></li>
                  <li class="relative !mt-[0.35rem] flex items-start"><span class="pr-[.75rem]"><i class="uil uil-check w-4 h-4 text-[0.8rem] leading-none !tracking-[normal] !text-center flex justify-center items-center bg-[#ffe8ea] !text-[#ff4450] rounded-[100%] top-[0.2rem] before:content-['\\e9dd'] before:align-middle before:table-cell"></i></span><span><strong>Location (optional):</strong> To verify service region or support routing when you request on-site assistance. Location is not collected continuously in the background unless clearly disclosed for a specific feature.</span></li>
                  <li class="relative !mt-[0.35rem] flex items-start"><span class="pr-[.75rem]"><i class="uil uil-check w-4 h-4 text-[0.8rem] leading-none !tracking-[normal] !text-center flex justify-center items-center bg-[#ffe8ea] !text-[#ff4450] rounded-[100%] top-[0.2rem] before:content-['\\e9dd'] before:align-middle before:table-cell"></i></span><span><strong>Device information:</strong> Basic device and app version data to improve compatibility, security, and support diagnostics.</span></li>
                </ul>
                <p class="!mb-0">Images or documents you upload may be stored on our servers when cloud backup or multi-device sync is enabled, so they can be accessed across authorized devices. We use this only to provide a seamless business experience.</p>
              </div>
            </div>
          </section>
          <section id="data-security" class="wrapper pt-24">
            <div class="card">
              <div class="card-body !p-10">
                <h2 class="!mb-3 !leading-[1.35]">6. Data Security</h2>
                <p>At TrackPOSSystem, we understand the importance of safeguarding your personal and business information. We employ industry-standard physical, technical, and administrative measures — including access controls, encryption where applicable, and monitoring — to protect information against unauthorized access, misuse, or loss.</p>
                <p>We continually work to improve our security practices. No system is completely impenetrable; protection is provided on a best-effort basis with ongoing updates.</p>
                <p><strong>Your responsibility:</strong> Keep your login credentials confidential. Do not share passwords with unauthorized persons. Report suspected security issues promptly.</p>
                <p><strong>Communication safety:</strong> Standard email or SMS may not be encrypted. Avoid sending highly sensitive credentials through unsecured channels.</p>
                <p><strong>Data retention:</strong> We retain account and business data as long as your subscription is active or as needed to provide support, comply with law, or resolve disputes. You may request account or data deletion by contacting <a href="mailto:support@trackpossystem.com">support@trackpossystem.com</a>. Some logs may be retained for a limited period for security and audit purposes.</p>
                <p class="!mb-0"><em>For security concerns, contact <a href="mailto:support@trackpossystem.com">support@trackpossystem.com</a>.</em></p>
              </div>
            </div>
          </section>
          <section id="communications" class="wrapper pt-24">
            <div class="card">
              <div class="card-body !p-10">
                <h2 class="!mb-3 !leading-[1.35]">7. Communications</h2>
                <p>In addition to the general conditions above, you agree that TrackPOSSystem may send transactional, service-related, and promotional communications via email, SMS, phone, or push notifications where you have provided contact details and applicable consent.</p>
                <p>You may opt out of promotional messages using the unsubscribe link in emails or by contacting support. Transactional messages (billing receipts, security alerts, support replies) may still be sent as needed to operate your account.</p>
                <p class="!mb-0">Under certain conditions, informational or promotional messages may be transmitted to users; TrackPOSSystem shall have no further obligation beyond providing the communication itself.</p>
              </div>
            </div>
          </section>
          <section id="refund-billing" class="wrapper pt-24">
            <div class="card">
              <div class="card-body !p-10">
                <h2 class="!mb-3 !leading-[1.35]">8. Refund, Cancellation &amp; Renewal Policies</h2>
                <ol class="!mb-4 !pl-4">
                  <li class="!mb-2"><strong>Eligibility for refund:</strong> Customers who submit a refund request via email to <a href="mailto:sales@trackpossystem.com">sales@trackpossystem.com</a> or through our <a href="./contact.html">contact page</a> within <strong>7 days</strong> from the date of purchase of an annual (or longer) paid plan may be eligible for a full refund, subject to review.</li>
                  <li class="!mb-2"><strong>Free trial:</strong> The 14-day free trial is provided for evaluation. Charges apply only after you purchase a paid plan. Trial data may be deleted if you do not convert to a paid subscription.</li>
                  <li class="!mb-2"><strong>Refund scope:</strong> Refund policies apply to qualifying paid subscriptions as stated at purchase. Convenience or payment-gateway fees, where applicable, may be non-refundable.</li>
                  <li class="!mb-2"><strong>Cancellation:</strong> You may cancel renewal by not purchasing a new license period. We do not store payment cards for automatic renewal unless explicitly enabled through a supported payment partner.</li>
                  <li class="!mb-2"><strong>Manual renewal:</strong> Unless otherwise stated, licenses are renewed manually at the end of the validity period. Current published plans include Regular (from ₹600/month) and Diamond (from ₹1000/month); pricing may change with notice on our website.</li>
                </ol>
                <p class="!mb-0">Subscription validity and feature access depend on the plan purchased. Downgrading or lapsing a license may limit access to premium modules until renewal.</p>
              </div>
            </div>
          </section>
          <section id="contact-us" class="wrapper py-24">
            <div class="card">
              <div class="card-body !p-10">
                <h2 class="!mb-3 !leading-[1.35]">9. Contact Us</h2>
                <p class="!mb-4"><strong>END OF TERMS OF SERVICE</strong></p>
                <p>If you have questions or concerns regarding this Agreement, please contact us:</p>
                <ul class="pl-0 list-none bullet-bg bullet-soft-primary !mb-0">
                  <li class="relative !mt-[0.35rem] flex items-start"><span class="pr-[.75rem]"><i class="uil uil-check w-4 h-4 text-[0.8rem] leading-none !tracking-[normal] !text-center flex justify-center items-center bg-[#ffe8ea] !text-[#ff4450] rounded-[100%] top-[0.2rem] before:content-['\\e9dd'] before:align-middle before:table-cell"></i></span><span><strong>Sales:</strong> <a href="mailto:sales@trackpossystem.com">sales@trackpossystem.com</a></span></li>
                  <li class="relative !mt-[0.35rem] flex items-start"><span class="pr-[.75rem]"><i class="uil uil-check w-4 h-4 text-[0.8rem] leading-none !tracking-[normal] !text-center flex justify-center items-center bg-[#ffe8ea] !text-[#ff4450] rounded-[100%] top-[0.2rem] before:content-['\\e9dd'] before:align-middle before:table-cell"></i></span><span><strong>Support:</strong> <a href="mailto:support@trackpossystem.com">support@trackpossystem.com</a></span></li>
                  <li class="relative !mt-[0.35rem] flex items-start"><span class="pr-[.75rem]"><i class="uil uil-check w-4 h-4 text-[0.8rem] leading-none !tracking-[normal] !text-center flex justify-center items-center bg-[#ffe8ea] !text-[#ff4450] rounded-[100%] top-[0.2rem] before:content-['\\e9dd'] before:align-middle before:table-cell"></i></span><span><strong>Phone / WhatsApp:</strong> <a href="tel:+919348457123">+91-9348457123</a></span></li>
                </ul>
              </div>
            </div>
          </section>
"""


def replace_block(text, open_tag, close_tag, replacement):
    i = text.find(open_tag)
    if i < 0:
        return text
    j = text.find(close_tag, i)
    if j < 0:
        return text
    j += len(close_tag)
    return text[:i] + replacement + text[j:]


with open(CONTACT, encoding="utf-8") as f:
    contact = f.read()
header_m = re.search(r"<header class=.*?</header>", contact, re.DOTALL)
footer_m = re.search(r"<footer class=.*?</footer>", contact, re.DOTALL)

with open(TERMS, encoding="utf-8") as f:
    terms = f.read()

terms = replace_block(terms, "<head>", "</head>", """<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="TrackPOSSystem Terms & Conditions — terms of service, privacy, data security, refunds, and billing policies for POS software in India.">
  <meta name="keywords" content="TrackPOSSystem, terms of service, privacy policy, POS software India, refund policy">
  <title>Terms &amp; Conditions | TrackPOSSystem</title>
  <link rel="canonical" href="https://trackpossystem.com/terms.html">
  <link rel="shortcut icon" href="./assets/img/favicon.png">
	<link rel="stylesheet" type="text/css" href="./assets/fonts/unicons/unicons.css">
  <link rel="stylesheet" href="./assets/css/plugins.css">
  <link rel="stylesheet" href="./style.css">
  <link rel="stylesheet" href="./assets/css/trackpos.css">
</head>""")

terms = terms.replace("<body>", '<body class="[word-spacing:.05rem!important] font-Manrope text-[0.8rem] !leading-[1.7] font-medium">')

if header_m:
    terms = replace_block(terms, "<header class=", "</header>", header_m.group(0))
if footer_m:
    terms = replace_block(terms, "<footer class=", "</footer>", footer_m.group(0))

terms = re.sub(
    r"<h1[^>]*>Terms and Conditions</h1>",
    '<h1 class="!text-[calc(1.365rem_+_1.38vw)] font-bold !leading-[1.2] xl:!text-[2.4rem] !mb-3">Terms &amp; Conditions</h1>',
    terms,
    count=1,
)
terms = re.sub(
    r'<li class="breadcrumb-item flex !text-\[#60697b\]"><a class="!text-\[#60697b\] hover:!text-\[#ff4450\]" href="#">Home</a></li>',
    '<li class="breadcrumb-item flex !text-[#60697b]"><a class="!text-[#60697b] hover:!text-[#ff4450]" href="./index.html">Home</a></li>',
    terms,
    count=1,
)
terms = re.sub(
    r'<nav id="sidebar-nav">.*?</nav>',
    f'<nav id="sidebar-nav">{SIDEBAR}',
    terms,
    count=1,
    flags=re.DOTALL,
)
start = terms.find('          <section id="terms-conditions"')
end = terms.find("        <!-- /column -->", start)
if start > 0 and end > start:
    terms = terms[:start] + SECTIONS + "\n" + terms[end:]

if "trackpos-float-whatsapp" not in terms:
    floats = """
  <a href="https://wa.me/919348457123" class="trackpos-float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="uil uil-whatsapp before:content-['\\ed9a']"></i></a>
  <a href="tel:+919348457123" class="trackpos-float-call" aria-label="Call us"><i class="uil uil-phone before:content-['\\ec51']"></i></a>
"""
    terms = terms.replace('<script src="./assets/js/plugins.js"></script>', floats + '  <script src="./assets/js/plugins.js"></script>')

with open(TERMS, "w", encoding="utf-8") as f:
    f.write(terms)
print("Patched terms.html")
