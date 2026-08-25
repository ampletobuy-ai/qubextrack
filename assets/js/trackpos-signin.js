/**
 * Module sign-in chooser: injects modal and redirects to industry login hosts.
 * Subdomains use the current site apex (e.g. www.qubextrack.com → retail.qubextrack.com).
 */
(function () {
  const MODAL_ID = 'modal-module-signin';

  const MODULES = [
    {
      key: 'retail',
      label: 'Retail',
      blurb: 'Billing, stock & GST for stores',
      icon: 'uil-store',
    },
    {
      key: 'jewellery',
      label: 'Jewellery',
      blurb: 'Gold, diamond & silver POS',
      icon: 'uil-diamond',
    },
    {
      key: 'restaurant',
      label: 'Restaurant',
      blurb: 'Dine-in, takeaway & kitchen',
      icon: 'uil-restaurant',
    },
    {
      key: 'hotel',
      label: 'Hotel',
      blurb: 'Bookings, folio & property',
      icon: 'uil-bed',
    },
  ];

  /** Apex host for subdomain apps (strip www.). */
  function apexDomain() {
    var host = (window.location.hostname || '').replace(/^www\./i, '');
    if (!host || host === 'localhost' || host === '127.0.0.1') {
      return 'qubextrack.com';
    }
    return host;
  }

  function moduleUrl(subdomain) {
    var protocol = window.location.protocol === 'http:' ? 'http:' : 'https:';
    // Local file:// or odd protocols → https
    if (protocol !== 'http:' && protocol !== 'https:') {
      protocol = 'https:';
    }
    return protocol + '//' + subdomain + '.' + apexDomain() + '/';
  }

  function buildModalHtml() {
    const options = MODULES.map(function (m) {
      var url = moduleUrl(m.key);
      return (
        '<a class="trackpos-signin-option" href="' +
        url +
        '" data-module="' +
        m.key +
        '" rel="noopener">' +
        '<span class="trackpos-signin-option__icon" aria-hidden="true"><i class="uil ' +
        m.icon +
        '"></i></span>' +
        '<span class="trackpos-signin-option__text">' +
        '<span class="trackpos-signin-option__label">' +
        m.label +
        '</span>' +
        '<span class="trackpos-signin-option__blurb">' +
        m.blurb +
        '</span>' +
        '</span>' +
        '<span class="trackpos-signin-option__arrow" aria-hidden="true"><i class="uil uil-arrow-right"></i></span>' +
        '</a>'
      );
    }).join('');

    return (
      '<div class="trackpos-modal trackpos-modal--signin" id="' +
      MODAL_ID +
      '" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="trackpos-signin-title">' +
      '<div class="trackpos-modal__overlay" data-trackpos-modal-close></div>' +
      '<div class="trackpos-modal__dialog trackpos-signin-dialog">' +
      '<div class="trackpos-modal__header">' +
      '<h2 class="trackpos-modal__title" id="trackpos-signin-title">Choose your module</h2>' +
      '<button type="button" class="trackpos-modal__close" data-trackpos-modal-close aria-label="Close">&times;</button>' +
      '</div>' +
      '<div class="trackpos-modal__body">' +
      '<p class="trackpos-signin-lead">Select Retail, Jewellery, Restaurant or Hotel to continue.</p>' +
      '<div class="trackpos-signin-options">' +
      options +
      '</div>' +
      '</div>' +
      '</div>' +
      '</div>'
    );
  }

  function ensureModal() {
    if (document.getElementById(MODAL_ID)) return;
    document.body.insertAdjacentHTML('beforeend', buildModalHtml());
  }

  function dismissNavOffcanvas() {
    const openCanvas = document.querySelector('.offcanvas.show');
    if (!openCanvas || !window.bootstrap || !bootstrap.Offcanvas) return;
    const instance = bootstrap.Offcanvas.getInstance(openCanvas);
    if (instance) instance.hide();
  }

  document.addEventListener('click', function (e) {
    const trigger = e.target && e.target.closest
      ? e.target.closest('[data-trackpos-modal-open="#' + MODAL_ID + '"]')
      : null;
    if (trigger) dismissNavOffcanvas();
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ensureModal);
  } else {
    ensureModal();
  }
})();
