# QubexTrack Marketing & Packaging Plan

Go-to-market, plan packaging, and module entitlements for **general retail and service businesses**.

This document is retail-scoped only. Jewellery / metal-specific capabilities (metal masters, weight-based pricing, stones, exchange-old-item, metal-wise stock reports, jewellery invoice UI) are **out of scope** for marketing and packaging.

> **Related:** [PRICING_PLANS.md](./PRICING_PLANS.md) (prices & feature matrix) · [COMPETITOR_COMPARISON.md](./COMPETITOR_COMPARISON.md) · [MobileApp/MOBILE_USER_AND_DEVICE_LICENSING.md](./MobileApp/MOBILE_USER_AND_DEVICE_LICENSING.md) · live catalog in `config/plans.php`

---

## Table of contents

1. [Positioning](#1-positioning)
2. [Target segments](#2-target-segments)
3. [Plan packaging](#3-plan-packaging)
4. [Desktop & mobile access](#4-desktop--mobile-access)
5. [Module entitlement matrix](#5-module-entitlement-matrix)
6. [Add-on catalog](#6-add-on-catalog)
7. [Sales playbook](#7-sales-playbook)
8. [Go-to-market](#8-go-to-market)
9. [In-app upsell triggers](#9-in-app-upsell-triggers)
10. [Packaging gaps & recommendations](#10-packaging-gaps--recommendations)
11. [90-day rollout](#11-90-day-rollout)

---

## 1. Positioning

**One-liner:** GST-ready retail POS + inventory + accounts — without enterprise ERP pricing.

**Primary promise**

- Full purchase and sale cycle (not invoice-only billing)
- Party ledger, cash & bank, GST reports
- Multi-warehouse, batch / serial (Business)
- **Desktop (web browser) + mobile (Android / iOS staff app)** on the same subscription
- Self-serve portal: trial → pay → open POS
- Optional vertical modules: appointments, commission, CRM, garage, combopack, coupons, membership

**Do not lead with** industry-specific jewellery workflows. Lead with retail billing, stock, GST, service modules, and access from counter **and** phone.

**Taglines by plan**

| Plan | Tagline |
|------|---------|
| Starter | Start billing & stock in a day — on desktop or phone. |
| Business | Orders, warehouses, batch/serial, and full finance reports — desktop POS + mobile staff app. |

---

## 2. Target segments

| Segment | Pain | Offer |
|---------|------|--------|
| Single-counter retail (kirana, apparel, hardware, electronics) | Billing + stock + GST | **Starter** |
| Growing multi-counter / wholesale-retail | PO, warehouse, batch/serial, P&L | **Business** |
| Service + retail hybrids (salon, clinic, garage, wellness) | Booking / jobs / CRM | **Business + module add-ons** |

### Industry packs (marketing bundles)

| Pack name | Base plan | Modules to enable / sell |
|-----------|-----------|---------------------------|
| QubexTrack Retail | Starter or Business | Core only |
| QubexTrack for Salons & Clinics | Business | Appointments (included); CRM optional |
| QubexTrack for Workshops | Business | Garage add-on; CRM optional |
| QubexTrack for Wellness | Business | Membership (future); Appointments included |

---

## 3. Plan packaging

Source of truth for limits and included modules: `config/plans.php`.

### Pricing snapshot (ex GST)

| | Starter | Business | Trial |
|--|---------|----------|-------|
| Annual | ₹4,499 | ₹8,999 | — |
| Monthly (10× = 12 mo.) | ₹449 | ₹899 | — |
| Users | 2 | 8 | Same as Business |
| Warehouses | 1 | 3 | Same as Business |
| Desktop (web) access | **Included** | **Included** | Same as Business |
| Mobile app access | **Included** | **Included** | Same as Business |
| Suggested mobile device seats | 2 | 10 | Same as Business |
| Included modules | None | appointments, commission, combopack, carrier | Same as Business |
| Soft invoice cap | ~2,500 / year | None | Same as Business |
| Duration | — | — | 14 days (`base_plan` = business) |

### Core always-on (both plans)

- **Desktop web POS** (browser — counter, back office, reports)
- **Mobile staff app** (Android / iOS Flutter app — field & floor use)
- POS & sales invoice
- Quotation & sale return
- Purchase bill & purchase return
- Customers & suppliers
- Payment in / payment out
- Items, categories, brands
- Regular stock tracking
- GSTR-1 & GSTR-2
- Print / PDF invoices
- Roles & permissions
- Import items & contacts
- Barcode labels

### Starter — keep lean

| Area | State |
|------|--------|
| Users / warehouses | 2 / 1 |
| Desktop + mobile access | **On** (same login / tenant) |
| Plan modules | **Off** (`modules: []`) |
| Sale order / purchase order | Off (packaging) |
| Multi-warehouse & stock transfer | Off |
| Batch / serial / IMEI | Off |
| Expense & income | Off |
| P&L, cash flow, bank statement | Off |
| Appointments, commission, combopack, carrier, CRM, garage | Off unless add-on |
| Support positioning | Email, standard SLA |

### Business — growth default

| Area | State |
|------|--------|
| Users / warehouses | 8 / 3 |
| Desktop + mobile access | **On** (more users / suggested device seats) |
| Included modules | **appointments, commission, combopack, carrier** |
| CRM | Add-on only |
| Garage / coupons / membership | Not in plan config today — sell as vertical add-ons (see §10) |
| Plus core Starter features | On |
| Sale/purchase orders, multi-warehouse, batch/serial | On |
| Expense, income, full reports, P&L, cash flow | On |
| SMS / email templates, API tokens | On |
| Support positioning | Priority email + onboarding |

### Trial

- Product: **14-day Business trial**
- Entitlements follow `config/plans.trial.base_plan` → `business`
- Includes desktop web + mobile app access for the trial period
- Marketing CTA: “Start 14-day Business trial” → portal register

---

## 4. Desktop & mobile access

QubexTrack is sold as **one subscription, two surfaces** — not separate desktop and mobile SKUs.

| Surface | What it is | Best for | Plan availability |
|---------|------------|----------|-------------------|
| **Desktop (web)** | Browser app at the QubexTrack hostname (POS + portal) | Counter billing, inventory, accounts, GST reports, admin | Starter & Business |
| **Mobile (app)** | Flutter staff app (Android + iOS) | Floor sales assist, customers, jobs, check-ins, on-the-go | Starter & Business |

### How to message it

- **Same business data** on desktop and mobile — one tenant, one subscription.
- **Desktop** = full retail ERP at the counter and back office.
- **Mobile** = staff productivity on the floor / in the field (not a cut-down “billing-only” competitor app).
- **User seats** (`max_users`) apply across **web + mobile** — one staff account can use either surface.
- **Device seats** (planned / recommended): limit active phones on the Flutter app only; browsers are not counted as devices. See [MobileApp/MOBILE_USER_AND_DEVICE_LICENSING.md](./MobileApp/MOBILE_USER_AND_DEVICE_LICENSING.md).

### Suggested device entitlements (marketing & future billing)

| Plan | Max users | Suggested max mobile devices |
|------|-----------|------------------------------|
| Starter | 2 | 2 |
| Business | 8 | 10 |
| Add-on | `extra_user` (+1 user) | `extra_device` (+1 phone) |

### What to emphasize in demos

1. Open web POS on a laptop → create invoice / check stock.  
2. Same login on phone → look up customer / continue floor workflow.  
3. Close with: “No second software fee for mobile — it’s in the plan.”

### Competitive angle

| vs | Angle |
|----|--------|
| Mobile-only billing apps | Full desktop ERP depth **plus** a real staff app |
| Desktop-only legacy POS | Staff stay productive away from the counter |
| “Web only, use phone browser” | Native Android / iOS app for staff workflows |

---

## 5. Module entitlement matrix

Company flags are synced from subscription entitlements via `TenantProvisioningRulesService`.

| Module key | Company flag | Starter | Business | Add-on? | Typical buyer |
|------------|--------------|:-------:|:--------:|:-------:|---------------|
| *(core POS)* | — | On | On | — | Everyone |
| `appointments` | `is_enable_appointment_booking` | Off | **On** | Yes (if Starter) | Salon, clinic, service desk |
| `commission` | `is_enable_sales_comission` | Off | **On** | Recommended for Starter | Staff-incentive retail |
| `combopack` | `is_enable_combopack` | Off | **On** | Prefer Business-only | Bundles / kits |
| `carrier` | `is_enable_carrier` | Off | **On** | Prefer Business-only | Delivery / logistics |
| `crm` | `is_enable_crm` | Off | Off | **Yes** | Job / order pipeline |
| `garage` | `is_enable_garage` | Off | Off | **Yes** (catalog gap) | Auto workshop |
| Coupons | `is_enable_coupon` | Off | Off | **Yes** (catalog gap) | Promo-heavy retail |
| Membership | `is_enable_membership` | — | — | Future vertical | Wellness / gym |

### Quantity limits (not modules)

| Add-on code | Effect | Notes |
|-------------|--------|--------|
| `extra_user` | +1 user (web + mobile) | Available on either plan |
| `extra_warehouse` | +1 warehouse | Prefer after Business; Starter should upgrade first |
| `extra_device` | +1 mobile device seat | Recommended; not in `plans.php` yet |

---

## 6. Add-on catalog

### Live in `config/plans.php`

| Code | Name | Type | Annual (ex GST) | Monthly | Module key |
|------|------|------|----------------:|--------:|------------|
| `extra_user` | Extra User | quantity | ₹999 | ₹99 | — |
| `extra_warehouse` | Extra Warehouse | quantity | ₹1,499 | ₹149 | — |
| `crm` | CRM | module | ₹2,999 | ₹299 | `crm` |
| `appointments` | Appointments | module | ₹1,999 | ₹199 | `appointments` |

### Documented / recommended (not all in portal catalog yet)

| Add-on | Annual (ex GST) | Notes |
|--------|----------------:|--------|
| Extra mobile device | TBD (suggest ₹499–999) | `extra_device` — phone seat beyond plan allowance |
| Sales commission | ₹1,999 | Included on Business; sell to Starter |
| Garage | TBD (suggest ₹2,999) | Vertical pack for workshops |
| Coupons | TBD (suggest ₹999–1,499) | Promo engine |
| Membership | TBD | Wellness vertical; see `MEMBERSHIP_PROGRAM.md` |
| Invoice overage pack | ₹999 | +1,000 invoices (Starter soft cap) |
| Second store (separate company) | ₹3,999 | Separate tenant / database |
| Setup & data migration | ₹5,000–12,000 | One-time |
| On-site training | ₹3,999 / visit | One-time |
| Priority phone support | ₹2,499 / year | Business customers |

### Packaging rules for selling

1. **Primary CTA:** Starter → Business upgrade (not stacking many Starter add-ons).
2. **Desktop + mobile included** on every paid plan and trial — do not sell “mobile access” as a separate base SKU.
3. **Extra user** grows web + mobile seats; **extra device** (when live) grows phone seats only.
4. **CRM, Garage, Coupons:** named add-ons / industry packs.
5. **Combopack + carrier:** keep Business-included — weak as standalone SKUs; strong as upgrade reasons.
6. **Appointments:** included on Business; sell only to Starter who will not upgrade yet.
7. **Garage / Membership:** market as industry packs, not generic retail features.

---

## 7. Sales playbook

### Which plan to recommend

```
1 counter, 1–2 staff, basic GST          → Starter (desktop + mobile)
Need PO / warehouse / batch / serial     → Business
Staff on floor with phones               → Either plan; pitch mobile app included
Staff incentives                         → Business (commission on)
Salon / booking                          → Business (appointments on)
Job pipeline / service desk              → Business + CRM add-on
Auto workshop                            → Business + Garage add-on
Need 9th user / 4th warehouse            → Extra user / warehouse add-on
Need more phones than device allowance   → Extra device add-on (when live)
Promo coupons                            → Coupons add-on (once catalogued)
Wellness membership tracking             → Business + Membership (future)
```

### Competitive framing (retail)

| vs | Angle |
|----|--------|
| myBillBook / phone-only billing | Full desktop ERP **plus** staff mobile app — not mobile-only invoicing |
| Vyapar Silver | Purchase return, party ledger, web multi-user + mobile |
| Vyapar Diamond | Same price band; PO, warehouse, P&L, batch/serial |
| Marg Basic / Silver | Similar depth at lower SMB price; modern web + app access |
| Desktop-only legacy POS | Staff stay productive on Android / iOS |

Do **not** race the cheapest mobile billing apps on price. Sell ERP depth on desktop and convenience on mobile.

### Quote hygiene

1. Quote **GST-inclusive** totals on proposals (Starter ~₹5,309/year, Business ~₹10,619/year at 18% GST).
2. Prefer **annual** billing; monthly at ÷10 of annual.
3. Lead with **14-day Business trial**.
4. Prefer paid **setup & migration** over deep plan discounts.

---

## 8. Go-to-market

### Acquisition funnel

1. Marketing site → comparison vs Vyapar / Marg + pricing table (include **Desktop + Mobile** row)  
2. CTA: **Start 14-day Business trial** → `/portal/register`  
3. In-app: trial banner → upgrade / add-ons / manage subscription  
4. Day 7–10 email: “You’re using warehouse / P&L — lock it in at ₹8,999”  
5. App store / Play listing + “Download staff app” link from portal after signup  

### Channels

| Channel | Offer | Why |
|---------|--------|-----|
| Google / Meta (local retail) | Starter + trial | High intent “GST billing software” |
| CA / GST practitioner partners | Referral + setup fee | They recommend billing tools |
| Hardware dealers (printers / scanners) | Bundle + setup | Same buyer as POS |
| Vertical communities (salon, garage) | Industry packs | Modules are the hook |
| WhatsApp demos | Screen-share desktop POS + phone app | Trust for SMB |
| Short video | “Invoice on desktop → same stock on phone” | Access proof |
| Play Store / App Store | Staff app listing | Discovery for mobile-first owners |

### Campaign themes

1. **Not just billing** — purchase return + party due + cash/bank  
2. **Desktop at the counter, mobile on the floor** — one subscription, two surfaces  
3. **Grow without re-buying software** — Starter → Business, same data  
4. **Service businesses too** — appointments / CRM / garage  
5. **Accounts that match the counter** — P&L, cash & bank adjustments  

---

## 9. In-app upsell triggers

| Trigger | Suggested CTA |
|---------|----------------|
| Hit user limit | Extra user add-on or upgrade to Business |
| Hit warehouse limit | Extra warehouse or upgrade to Business |
| Hit mobile device seat limit | Extra device add-on (when live) |
| Locked module menu (CRM / Garage / Appointments on Starter) | Portal add-ons or change plan |
| Soft invoice cap approaching (Starter) | Overage pack or Business |
| Trial day 7+ using Business-only screens | Convert to paid Business |
| Header / profile “Manage subscription” | Portal subscription & add-ons |
| First mobile login on trial | Nudge to keep desktop + mobile after trial |

---

## 10. Packaging gaps & recommendations

| Gap | Recommendation |
|-----|----------------|
| Starter “core feature” soft-locks (orders, multi-warehouse, P&L) may not all be enforced in UI | Enforce so marketing claims match product |
| `garage`, `commission`, `coupons` missing from `config/plans.addons` | Add to portal catalog for self-serve purchase |
| Mobile device seats not in `plans.php` | Add `max_devices` per plan + `extra_device` add-on; see device licensing doc |
| Membership not in plan catalog | Add when module ships; sell as wellness pack |
| Combopack / carrier not sold as add-ons | Keep Business-included; do not fragment |
| Marketing site pricing page | Publish matrix from [PRICING_PLANS.md](./PRICING_PLANS.md); show Desktop + Mobile included |
| Industry landing pages | Separate pages for Workshops and (later) Wellness |
| App store presence | Clear “included with Starter & Business” copy; link to trial |

### Suggested future `plans.addons` entries

```text
extra_device → type: quantity (mobile phone seat)
commission   → module_key: commission
garage       → module_key: garage
coupons      → module_key: coupons   (wire company flag is_enable_coupon)
membership   → module_key: membership (when ready)
```

---

## 11. 90-day rollout

| Phase | Focus |
|-------|--------|
| Days 1–30 | Trial funnel live; Starter vs Business page with Desktop + Mobile; CA partner one-pager |
| Days 31–60 | Case studies: 1 retail (desktop+mobile), 1 service (appointments/CRM), 1 workshop (garage) |
| Days 61–90 | Paid ads on “GST POS” + “POS with mobile app”; retarget trial abandoners; push annual Business |

### Success metrics (suggested)

- Trial starts / week  
- Trial → paid conversion %  
- Starter → Business upgrade %  
- Mobile app installs / active devices per tenant  
- Add-on attach rate (CRM, appointments, extra user, extra device)  
- Average revenue per account (plan + add-ons)

---

## Summary

| Principle | Practice |
|-----------|----------|
| Market Starter as clean GST retail | Lean limits, no vertical modules by default |
| Market Business as the real product | Warehouse, orders, reports + included modules |
| Include desktop + mobile on every plan | One subscription, two surfaces — not separate base SKUs |
| Monetize seats carefully | Extra user (all platforms); extra device (phones only) |
| Monetize verticals via add-ons | CRM, Garage, Coupons, Membership |
| Justify the ₹8,999 jump | Appointments, commission, combopack, carrier included |
| Stay retail-scoped in all campaigns | No jewellery / metal feature messaging |

---

*Aligned with `config/plans.php` and [PRICING_PLANS.md](./PRICING_PLANS.md). Adjust prices and add-on SKUs as the portal catalog evolves.*
