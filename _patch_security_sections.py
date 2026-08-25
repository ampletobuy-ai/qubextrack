#!/usr/bin/env python3
"""Inject data security & compliance sections across TrackPOSSystem pages."""
from pathlib import Path

DIST = Path(__file__).resolve().parent
FULL = (DIST / "_snippets/security-section-full.html").read_text(encoding="utf-8")
COMPACT = (DIST / "_snippets/security-section-compact.html").read_text(encoding="utf-8")

MARKER = 'id="security-compliance"'
TRIAL = '<div class="flex flex-wrap mx-[-15px] !mt-12">'


def patch_index():
    path = DIST / "index.html"
    c = path.read_text(encoding="utf-8")
    if MARKER in c:
        print("index.html already has security section")
        return
    needle = "    <!-- /integrations -->\n\n    <section class=\"wrapper !bg-[#f5f5ff]\">"
    if needle not in c:
        raise RuntimeError("index.html integrations anchor not found")
    c = c.replace(needle, "    <!-- /integrations -->\n\n" + FULL + "\n    <section class=\"wrapper !bg-[#f5f5ff]\">", 1)
    c = c.replace(
        '<span class="trackpos-badge"><i class="uil uil-file-check-alt"></i> GST Compliant</span>',
        '<span class="trackpos-badge"><i class="uil uil-file-check-alt"></i> GST Compliant</span>\n'
        '              <span class="trackpos-badge"><i class="uil uil-shield-check"></i> Secure Cloud ERP</span>',
        1,
    )
    path.write_text(c, encoding="utf-8")
    print("index.html")


def patch_industry(filename: str):
    path = DIST / filename
    if not path.exists():
        return
    c = path.read_text(encoding="utf-8")
    if MARKER in c:
        print(f"{filename} already patched")
        return
    if TRIAL not in c:
        print(f"{filename} — trial anchor not found, skip")
        return
    c = c.replace(TRIAL, COMPACT + "\n\n        " + TRIAL, 1)
    path.write_text(c, encoding="utf-8")
    print(filename)


def patch_about():
    path = DIST / "about.html"
    c = path.read_text(encoding="utf-8")
    if MARKER in c:
        print("about.html already patched")
        return
    needle = "    <section class=\"wrapper !bg-[#f5f5ff] trackpos-about-reviews\">"
    if needle not in c:
        raise RuntimeError("about.html anchor not found")
    c = c.replace(needle, COMPACT.replace("        ", "    ") + "\n    " + needle, 1)
    path.write_text(c, encoding="utf-8")
    print("about.html")


def patch_pricing():
    path = DIST / "pricing.html"
    c = path.read_text(encoding="utf-8")
    if "trackpos-security-pricing-note" in c:
        print("pricing.html already patched")
        return
    needle = '<section class="wrapper !bg-[#ffffff]'
    idx = c.find(needle)
    if idx < 0:
        return
    note = """
    <div class="container !pb-8">
      <div class="trackpos-security-pricing-note card !border-0 !bg-[#f5f5ff] !shadow-none">
        <div class="card-body p-6 xl:p-8 flex flex-wrap items-center gap-4">
          <div class="trackpos-security-card__icon !mb-0"><i class="uil uil-shield-check"></i></div>
          <div class="flex-1 min-w-[16rem]">
            <h4 class="!mb-1 !text-[1rem]">Security &amp; compliance included</h4>
            <p class="!mb-0 !text-[0.85rem] !text-[#60697b]">All plans include cloud tenant isolation, role-based permissions, audit logs, GST-ready billing, and secure support access. <a href="./terms.html#data-security" class="!text-[#ff4450] hover:!underline">Learn more</a></p>
          </div>
        </div>
      </div>
    </div>
"""
    c = c[:idx] + note + c[idx:]
    path.write_text(c, encoding="utf-8")
    print("pricing.html")


def patch_terms():
    path = DIST / "terms.html"
    c = path.read_text(encoding="utf-8")
    if "id=\"compliance\"" in c:
        print("terms.html already expanded")
        return
    old = """                <h2 class="!mb-3 !leading-[1.35]">6. Data Security</h2>
                <p>At TrackPOSSystem, we understand the importance of safeguarding your personal and business information. We employ industry-standard physical, technical, and administrative measures — including access controls, encryption where applicable, and monitoring — to protect information against unauthorized access, misuse, or loss.</p>
                <p>We continually work to improve our security practices. No system is completely impenetrable; protection is provided on a best-effort basis with ongoing updates.</p>
                <p><strong>Your responsibility:</strong> Keep your login credentials confidential. Do not share passwords with unauthorized persons. Report suspected security issues promptly.</p>
                <p><strong>Communication safety:</strong> Standard email or SMS may not be encrypted. Avoid sending highly sensitive credentials through unsecured channels.</p>
                <p><strong>Data retention:</strong> We retain account and business data as long as your subscription is active or as needed to provide support, comply with law, or resolve disputes. You may request account or data deletion by contacting <a href="mailto:support@trackpossystem.com">support@trackpossystem.com</a>. Some logs may be retained for a limited period for security and audit purposes.</p>
                <p class="!mb-0"><em>For security concerns, contact <a href="mailto:support@trackpossystem.com">support@trackpossystem.com</a>.</em></p>"""
    new = """                <h2 class="!mb-3 !leading-[1.35]">6. Data Security</h2>
                <p>At TrackPOSSystem, we understand the importance of safeguarding your personal and business information — especially billing, inventory, customer, and financial records processed across our jewellery, restaurant, hotel, and retail products.</p>
                <h3 class="!text-[1.05rem] !mt-6 !mb-3">6.1 Platform architecture</h3>
                <p>TrackPOSSystem is designed as a <strong>modern cloud SaaS platform</strong> (not traditional single-PC desktop software). Key design principles include:</p>
                <ul class="unordered-list bullet-primary !mb-4">
                  <li><strong>Multi-tenant isolation:</strong> Business data is logically separated so one customer’s records are not exposed to another.</li>
                  <li><strong>Branch isolation:</strong> Multi-store customers can restrict users and stock visibility by branch or warehouse where configured.</li>
                  <li><strong>API-ready design:</strong> Structured services to support integrations, scaling, and future channels.</li>
                  <li><strong>Subscription enforcement:</strong> Licensed access aligned to your active plan and users.</li>
                </ul>
                <h3 class="!text-[1.05rem] !mt-6 !mb-3">6.2 Operational security controls</h3>
                <p>Depending on your industry module and plan, the platform may include:</p>
                <ul class="unordered-list bullet-primary !mb-4">
                  <li>Role-based permissions and menu-level access control</li>
                  <li>Audit logs for sensitive actions (e.g. billing changes, stock movements, voids, reprints, transfers)</li>
                  <li>Approval workflows for discounts, inter-branch transfers, or other restricted operations</li>
                  <li>Invoice reprint tracking and staff accountability features</li>
                  <li>Commission rules, reversals, and settlement records where sales commission is enabled</li>
                  <li>Controlled support access for troubleshooting with your authorization</li>
                </ul>
                <h3 class="!text-[1.05rem] !mt-6 !mb-3" id="compliance">6.3 Compliance (India)</h3>
                <p>TrackPOSSystem helps Indian businesses operate with structured GST-ready billing, inventory, and reporting (including exports useful for GSTR-1 / GSTR-3B preparation where supported in your module). <strong>You remain solely responsible</strong> for accurate data entry, tax classification, filings, and meeting all statutory obligations under GST and other applicable laws.</p>
                <p>We employ industry-standard physical, technical, and administrative measures — including access controls, encryption in transit (HTTPS/TLS), and monitoring — to protect information against unauthorized access, misuse, or loss. Cloud backup practices apply as described in your service plan.</p>
                <p>We continually work to improve our security practices. No system is completely impenetrable; protection is provided on a best-effort basis with ongoing updates.</p>
                <p><strong>Your responsibility:</strong> Keep login credentials confidential. Assign roles carefully. Review audit reports periodically. Report suspected security issues promptly to <a href="mailto:support@trackpossystem.com">support@trackpossystem.com</a>.</p>
                <p><strong>Communication safety:</strong> Standard email or SMS may not be encrypted end-to-end. Avoid sending passwords or OTPs through unsecured channels.</p>
                <p><strong>Data retention:</strong> We retain account and business data while your subscription is active or as needed for support, legal compliance, or dispute resolution. You may request account or data deletion by contacting support. Security and audit logs may be retained for a limited period after deletion requests.</p>
                <p class="!mb-0"><em>For security or compliance questions, contact <a href="mailto:support@trackpossystem.com">support@trackpossystem.com</a>.</em></p>"""
    if old not in c:
        raise RuntimeError("terms.html security block not found")
    c = c.replace(old, new, 1)
    c = c.replace(
        '<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#data-security">6. Data Security</a></li>',
        '<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#data-security">6. Data Security</a></li>\n'
        '<li class="!mt-[0.35rem]"><a class="nav-link scroll" href="#compliance">6.3 Compliance</a></li>',
        1,
    )
    path.write_text(c, encoding="utf-8")
    print("terms.html")


def main():
    patch_index()
    patch_about()
    patch_pricing()
    patch_terms()
    for name in [
        "jewellery-pos-software.html",
        "restaurant-pos-software.html",
        "hotel-management-software.html",
        "retail-billing-software.html",
        "pharmacy-pos-software.html",
        "supermarket-pos-software.html",
    ]:
        patch_industry(name)


if __name__ == "__main__":
    main()
