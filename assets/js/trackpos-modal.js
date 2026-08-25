/**
 * Lightweight modal helper for QubexTrack pages.
 * Usage:
 * - Add: data-trackpos-modal-open="#modalId" on a link/button
 * - Add: data-trackpos-modal-close on close buttons inside modal
 * - Modal root: .trackpos-modal#modalId
 * - Optional: data-trackpos-modal-template="templateElementId" (inline, works on file://)
 * - Optional: data-trackpos-modal-src="./path/to/partial.html" (fetch, needs http server)
 */
(function () {
  const OPEN_ATTR = 'data-trackpos-modal-open';
  const CLOSE_ATTR = 'data-trackpos-modal-close';
  const TEMPLATE_ATTR = 'data-trackpos-modal-template';
  const SRC_ATTR = 'data-trackpos-modal-src';
  const CONTENT_ATTR = 'data-trackpos-modal-content';
  const loadedModals = new WeakSet();

  function getModal(selectorOrId) {
    if (!selectorOrId) return null;
    try {
      return document.querySelector(selectorOrId);
    } catch (_e) {
      return null;
    }
  }

  function loadFromTemplate(modal, container) {
    const templateId = modal.getAttribute(TEMPLATE_ATTR);
    if (!templateId) return false;

    const tpl = document.getElementById(templateId);
    if (!tpl || !('content' in tpl)) return false;

    container.innerHTML = '';
    container.appendChild(tpl.content.cloneNode(true));
    loadedModals.add(modal);
    return true;
  }

  function loadModalContent(modal) {
    const container = modal.querySelector(`[${CONTENT_ATTR}]`);
    if (!container || loadedModals.has(modal)) {
      return Promise.resolve();
    }

    if (loadFromTemplate(modal, container)) {
      return Promise.resolve();
    }

    const src = modal.getAttribute(SRC_ATTR);
    if (!src) {
      return Promise.resolve();
    }

    container.innerHTML = '<p class="trackpos-modal__loading">Loading comparison…</p>';

    return fetch(src)
      .then(function (res) {
        if (!res.ok) throw new Error('Failed to load content');
        return res.text();
      })
      .then(function (html) {
        container.innerHTML = html;
        loadedModals.add(modal);
      })
      .catch(function () {
        container.innerHTML = '<p class="trackpos-modal__error">Could not load comparison. Please refresh and try again.</p>';
      });
  }

  function openModal(modal) {
    if (!modal) return;
    loadModalContent(modal).finally(function () {
      modal.classList.add('is-open');
      modal.setAttribute('aria-hidden', 'false');
      document.documentElement.classList.add('trackpos-modal-open');
    });
  }

  function closeModal(modal) {
    if (!modal) return;
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.documentElement.classList.remove('trackpos-modal-open');
  }

  function closestModal(el) {
    return el ? el.closest('.trackpos-modal') : null;
  }

  document.addEventListener('click', function (e) {
    const openEl = e.target && e.target.closest ? e.target.closest(`[${OPEN_ATTR}]`) : null;
    if (openEl) {
      const modal = getModal(openEl.getAttribute(OPEN_ATTR));
      if (modal) {
        e.preventDefault();
        openModal(modal);
      }
      return;
    }

    const closeEl = e.target && e.target.closest ? e.target.closest(`[${CLOSE_ATTR}]`) : null;
    if (closeEl) {
      const modal = closestModal(closeEl);
      if (modal) {
        e.preventDefault();
        closeModal(modal);
      }
      return;
    }

    const overlayEl = e.target && e.target.classList && e.target.classList.contains('trackpos-modal__overlay') ? e.target : null;
    if (overlayEl) {
      const modal = closestModal(overlayEl);
      if (modal) closeModal(modal);
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    const openModalEl = document.querySelector('.trackpos-modal.is-open');
    if (openModalEl) closeModal(openModalEl);
  });
})();
