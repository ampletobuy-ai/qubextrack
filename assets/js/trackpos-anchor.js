/**
 * Scroll to in-page anchors with offset for sticky navbar.
 */
(function () {
  function getHeaderOffset() {
    const navbar = document.querySelector('.navbar.fixed .navbar-collapse') ||
      document.querySelector('.navbar.fixed') ||
      document.querySelector('.navbar');
    return navbar ? navbar.offsetHeight + 16 : 88;
  }

  function scrollToHash(hash, behavior) {
    if (!hash || hash === '#') return;
    const id = hash.replace(/^#/, '');
    const target = document.getElementById(id);
    if (!target) return;

    const top = target.getBoundingClientRect().top + window.pageYOffset - getHeaderOffset();
    window.scrollTo({ top: Math.max(0, top), behavior: behavior || 'smooth' });
  }

  function handleInitialHash() {
    if (!window.location.hash) return;
    scrollToHash(window.location.hash, 'auto');
    window.setTimeout(function () {
      scrollToHash(window.location.hash, 'auto');
    }, 150);
  }

  document.addEventListener('click', function (event) {
    const link = event.target.closest('a[href*="#"]');
    if (!link) return;

    const url = new URL(link.href, window.location.href);
    if (url.pathname !== window.location.pathname) return;

    const hash = url.hash;
    if (!hash || hash === '#') return;

    const target = document.getElementById(hash.replace(/^#/, ''));
    if (!target) return;

    event.preventDefault();
    history.pushState(null, '', hash);
    scrollToHash(hash, 'smooth');
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', handleInitialHash);
  } else {
    handleInitialHash();
  }

  window.addEventListener('load', handleInitialHash);
})();
