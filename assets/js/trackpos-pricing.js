/**
 * Industry-specific pricing: Starter & Professional plans with per-industry feature lists.
 */
(function () {
  const PRICING_DISCLAIMER_TEXT =
    'Listed plan prices may be revised year on year when required, with prior notice to existing customers before any change takes effect.';

  function ensurePricingDisclaimers() {
    const roots = document.querySelectorAll(
      '#pricing, .trackpos-jewellery-pricing, .trackpos-pricing'
    );
    roots.forEach((root) => {
      if (root.querySelector('.trackpos-pricing-disclaimer')) return;
      const p = document.createElement('p');
      p.className =
        'trackpos-pricing-disclaimer !text-center !text-[0.8rem] !text-[#aab0bc] !mt-2 !mb-0';
      p.textContent = PRICING_DISCLAIMER_TEXT;
      const gstNote = Array.from(root.querySelectorAll('p')).find((el) =>
        /exclude gst|prices exclude gst/i.test(el.textContent)
      );
      if (gstNote && gstNote.parentNode) {
        gstNote.insertAdjacentElement('afterend', p);
      } else {
        const wrapper =
          root.querySelector('.pricing-wrapper') ||
          root.querySelector('.container') ||
          root;
        wrapper.appendChild(p);
      }
    });
  }

  function formatPrice(amount) {
    return Number(amount).toLocaleString('en-IN');
  }

  const INDUSTRIES = {
    jewellery: {
      label: 'Jewellery POS',
      yearlyHint: '(Save up to 10%)',
      plans: {
        starter: {
          badge: 'Starter',
          title: 'Starter Plan',
          subtitle: 'Best for single-store jewellers, small shops, and startups.',
          monthly: 999,
          yearly: 10789,
          savePct: 10,
          cta: 'Request Free Trial',
        },
        pro: {
          badge: 'Professional',
          title: 'Professional Plan',
          subtitle: 'Best for growing jewellers, multi-branch stores, and chains.',
          monthly: 1852,
          yearly: 20000,
          savePct: 10,
          cta: 'Choose Professional',
        },
      },
      regular: [
        'GST billing &amp; gold/silver/platinum rates',
        'Barcode billing, invoice print &amp; label printing',
        'Unlimited <strong>invoices</strong> &amp; <strong>1,000 products</strong>',
        'Sales return/exchange &amp; split payment support',
        'Product master, stock inward/outward &amp; basic reports',
        'Customer outstanding, supplier payable &amp; cash book',
        'Ledger, daily sales, stock summary &amp; category reports',
        'Single user &amp; single branch',
        'WhatsApp support + basic onboarding',
      ],
      regularExcluded: [
        'Multi-store inventory &amp; inter-branch transfer',
        'Role-based permissions, audit logs &amp; commission engine',
      ],
      diamond: [
        'Everything in <strong>Starter</strong> for jewellery',
        '<strong>Multi user</strong> support',
        '<strong>Unlimited invoices</strong> &amp; billing',
        '<strong>Unlimited products</strong> in catalog',
        'Multi-store inventory &amp; inter-branch stock transfer',
        'Real-time stock visibility across branches',
        'Role-based permissions, audit logs &amp; discount approval',
        'Salesperson commission &amp; settlement workflow',
        'Dedicated database, cloud backup &amp; subscription management',
        'Day-end reconciliation &amp; advanced reporting',
        'WhatsApp invoice sharing, accounting export &amp; priority support',
      ],
    },
    restaurant: {
      label: 'Restaurant POS',
      yearlyHint: '(Save up to 17%)',
      plans: {
        starter: {
          badge: 'Starter',
          title: 'Starter Plan',
          subtitle: 'Best for single-outlet restaurants, cafés, and cloud kitchens.',
          monthly: 600,
          yearly: 6000,
          savePct: 17,
          cta: 'Request Free Trial',
        },
        pro: {
          badge: 'Professional',
          title: 'Professional Plan',
          subtitle: 'Best for multi-outlet restaurants, chains, and aggregator-led kitchens.',
          monthly: 1000,
          yearly: 10000,
          savePct: 17,
          cta: 'Choose Professional',
        },
      },
      regular: [
        'Restaurant <strong>dashboard</strong> (sales, tables, kitchen queue)',
        'Menus, items, <strong>variants &amp; add-ons</strong>',
        'Dine-in &amp; takeaway POS · <strong>KOT print</strong>',
        'Orders, payment, checkout &amp; close',
        'Up to <strong>3,000 orders</strong> / year · <strong>250 menu items</strong>',
        '2 users · single outlet',
        'WhatsApp support + basic onboarding',
      ],
      regularExcluded: [
        'Room service &amp; hotel folio posting',
        'Order grouping &amp; delta KOT workflow',
      ],
      diamond: [
        'Everything in <strong>Starter</strong> for restaurant',
        '<strong>Room service</strong> &amp; checked-in room billing',
        'Multi-table save &amp; <strong>order grouping</strong>',
        'Delta KOT &amp; KOT status manage · group receipt',
        'Void with audit · granular POS / orders / KOT permissions',
        'Multi-branch (up to 3) · <strong>8 users</strong>',
        'Hotel guest <strong>folio posting</strong> (with Hotel module)',
        'Unlimited orders &amp; menu items',
        'Swiggy / Zomato sync <strong>(add-on)</strong>',
        'Priority support &amp; onboarding session',
      ],
    },
    hotel: {
      label: 'Hotel Software',
      yearlyHint: '(Save up to 17%)',
      plans: {
        starter: {
          badge: 'Starter',
          title: 'Starter Plan',
          subtitle: 'Best for boutique hotels, guest houses, and homestays.',
          monthly: 1499,
          yearly: 14999,
          savePct: 17,
          cta: 'Request Free Trial',
        },
        pro: {
          badge: 'Business',
          title: 'Business Plan',
          subtitle: 'Best for multi-property hotels, resorts, and growing chains.',
          monthly: 2499,
          yearly: 24999,
          savePct: 17,
          cta: 'Choose Business',
        },
      },
      regular: [
        'GST billing · room booking, check-in &amp; check-out',
        'Housekeeping status board · guest <strong>folio</strong> billing',
        'Invoice print · <strong>rate plans</strong> &amp; seasonal pricing',
        'Occupancy &amp; revenue summary · daily sales &amp; ledger',
        'Real-time occupancy · role-based permissions + audit logs',
        'Up to <strong>1,000 invoices</strong> · <strong>250 packages</strong>',
        '<strong>1 user</strong> · 1 property / branch · desktop + mobile app',
        'WhatsApp support + basic onboarding',
      ],
      regularExcluded: [
        'Rate calendar, restrictions &amp; yield pricing',
        'Multi-property (up to 2 branches) &amp; stock transfer',
        'Advanced reports (pickup, cancellation, channel/source)',
      ],
      diamond: [
        'Everything in <strong>Starter</strong> for hotel',
        'Rate <strong>calendar</strong>, restrictions &amp; <strong>yield pricing</strong>',
        'Multi-property inventory (<strong>up to 2 branches</strong>)',
        'Inter-property <strong>stock transfer</strong>',
        'Advanced reporting (pickup &amp; pace, cancellation/no-show, room-type &amp; channel/source)',
        'Up to <strong>2 users</strong> · 1 mobile device',
        'Up to <strong>5,000 invoices</strong> · unlimited packages',
      ],
    },
    retail: {
      label: 'Retail Billing',
      yearlyHint: '(Save up to 17%)',
      plans: {
        starter: {
          badge: 'Starter',
          title: 'Starter Plan',
          subtitle: 'Start billing & stock in a day — on desktop or phone.',
          monthly: 449,
          yearly: 4499,
          savePct: 17,
          cta: 'Start 14-day Business Trial',
        },
        pro: {
          badge: 'Business',
          title: 'Business Plan',
          subtitle: 'Orders, warehouses, batch/serial & full finance — desktop POS + mobile staff app.',
          monthly: 899,
          yearly: 8999,
          savePct: 17,
          cta: 'Choose Business',
        },
      },
      regular: [
        '<strong>Desktop web POS</strong> + <strong>mobile staff app</strong> included',
        'POS &amp; sales invoice; quotation &amp; sale return',
        'Purchase bill &amp; purchase return',
        'Customers &amp; suppliers; payment in / out',
        'Items, categories, brands &amp; <strong>regular stock</strong>',
        'GSTR-1 &amp; GSTR-2; print / PDF &amp; barcode labels',
        'Roles &amp; permissions; import items &amp; contacts',
        '<strong>2 users</strong>, 1 store &amp; <strong>1 warehouse</strong>',
        '~2,500 invoices / year (fair use)',
        'Email support (standard SLA)',
      ],
      regularExcluded: [
        'Sale / purchase orders, expense &amp; income, P&amp;L',
        'Multi-warehouse, batch / serial &amp; API',
        'Appointments, commission, ComboPack, carrier, CRM',
      ],
      diamond: [
        'Everything in <strong>Starter</strong> for retail',
        'Sale order &amp; <strong>purchase order</strong>',
        'Expense &amp; income; cash, cheque &amp; bank registers',
        'P&amp;L, cash flow &amp; bank statement reports',
        'Multi-warehouse &amp; stock transfer (up to <strong>3</strong>)',
        'Batch &amp; serial / IMEI tracking',
        'Appointments, commission, ComboPack &amp; carrier modules',
        'SMS / email templates &amp; <strong>API tokens</strong>',
        '<strong>8 users</strong> &amp; priority email + onboarding',
      ],
    },
  };

  function featureItem(html, included) {
    const cls = included ? 'is-included' : 'is-excluded';
    return `<li class="${cls}">${html}</li>`;
  }

  function renderList(el, items, excluded) {
    if (!el) return;
    let html = items.map((t) => featureItem(t, true)).join('');
    if (excluded && excluded.length) {
      html += excluded.map((t) => featureItem(t, false)).join('');
    }
    el.innerHTML = html;
  }

  function updatePlanPricing(planKey, plan) {
    const badgeEl = document.querySelector(`[data-pricing-plan-badge="${planKey}"]`);
    const titleEl = document.querySelector(`[data-pricing-plan-title="${planKey}"]`);
    const subtitleEl = document.querySelector(`[data-pricing-subtitle="${planKey}"]`);
    const monthlyEl = document.querySelector(`[data-pricing-monthly="${planKey}"]`);
    const yearlyEl = document.querySelector(`[data-pricing-yearly="${planKey}"]`);
    const saveEl = document.querySelector(`[data-pricing-save="${planKey}"]`);
    const ctaEl = document.querySelector(`[data-pricing-cta="${planKey}"]`);

    if (badgeEl) badgeEl.textContent = plan.badge;
    if (titleEl) titleEl.textContent = plan.title;
    if (subtitleEl) subtitleEl.textContent = plan.subtitle || '';
    if (monthlyEl) monthlyEl.textContent = formatPrice(plan.monthly);
    if (yearlyEl) yearlyEl.textContent = formatPrice(plan.yearly);
    if (ctaEl) {
      if (planKey === 'pro') {
        ctaEl.innerHTML = `<span>${plan.cta}</span>`;
      } else {
        ctaEl.textContent = plan.cta;
      }
    }

    if (saveEl) {
      if (plan.savePct > 0) {
        saveEl.textContent = `Save ${plan.savePct}%`;
        saveEl.style.display = '';
      } else {
        saveEl.style.display = 'none';
      }
    }
  }

  function setIndustry(key) {
    const data = INDUSTRIES[key];
    if (!data) return;

    const labelEl = document.querySelector('[data-pricing-industry-label]');
    if (labelEl) labelEl.textContent = data.label;

    const yearlyHintEl = document.querySelector('[data-pricing-yearly-hint]');
    if (yearlyHintEl) yearlyHintEl.textContent = data.yearlyHint;

    updatePlanPricing('starter', data.plans.starter);
    updatePlanPricing('pro', data.plans.pro);

    renderList(
      document.querySelector('[data-pricing-features="regular"]'),
      data.regular,
      data.regularExcluded
    );
    renderList(
      document.querySelector('[data-pricing-features="diamond"]'),
      data.diamond,
      null
    );

    document.querySelectorAll('.trackpos-pricing-industry-btn').forEach((btn) => {
      const active = btn.dataset.industry === key;
      btn.classList.toggle('is-active', active);
      btn.setAttribute('aria-selected', active ? 'true' : 'false');
    });

    const pricingRoot = document.querySelector('.trackpos-pricing');
    if (pricingRoot) pricingRoot.dataset.industry = key;
  }

  function initIndustryButtons() {
    document.querySelectorAll('.trackpos-pricing-industry-btn').forEach((btn) => {
      btn.addEventListener('click', () => setIndustry(btn.dataset.industry));
    });
    const initial =
      document.querySelector('.trackpos-pricing-industry-btn.is-active')?.dataset
        .industry || 'jewellery';
    setIndustry(initial);
  }

  function init() {
    initIndustryButtons();
    ensurePricingDisclaimers();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
