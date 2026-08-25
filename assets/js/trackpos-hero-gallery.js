/**
 * Hero screenshot gallery: thumbnail rail with prev/next (no visible scrollbar).
 */
(function () {
  function initGallery(gallery) {
    var galleryAttr = gallery.querySelector('[data-glightbox]');
    if (!galleryAttr) return;
    var galleryMatch = galleryAttr.getAttribute('data-glightbox').match(/gallery:\s*([^;]+)/);
    if (!galleryMatch) return;
    var galleryName = galleryMatch[1].trim();
    var slideSelector = '[data-glightbox*="gallery: ' + galleryName + '"]';
    var slides = gallery.querySelectorAll(slideSelector);
    var thumbButtons = gallery.querySelectorAll('[data-trackpos-gallery-index]');
    var rail = gallery.querySelector('.trackpos-hero-thumbs-rail');
    if (!thumbButtons.length || !rail) return;

    var viewport = rail.querySelector('.trackpos-hero-thumbs__viewport');
    var scroller = rail.querySelector('.trackpos-hero-thumbs');
    var btnPrev = rail.querySelector('.trackpos-hero-thumbs__nav--prev');
    var btnNext = rail.querySelector('.trackpos-hero-thumbs__nav--next');
    if (!viewport || !scroller || !btnPrev || !btnNext) return;

    function setActive(btn) {
      thumbButtons.forEach(function (b) {
        b.classList.toggle('is-active', b === btn);
      });
      btn.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }

    function updateRail() {
      var maxScroll = scroller.scrollWidth - scroller.clientWidth;
      var scrollable = maxScroll > 4;
      rail.classList.toggle('is-scrollable', scrollable);
      if (!scrollable) {
        btnPrev.disabled = true;
        btnNext.disabled = true;
        return;
      }
      btnPrev.disabled = scroller.scrollLeft <= 2;
      btnNext.disabled = scroller.scrollLeft >= maxScroll - 2;
      rail.classList.toggle('can-scroll-left', scroller.scrollLeft > 2);
      rail.classList.toggle('can-scroll-right', scroller.scrollLeft < maxScroll - 2);
    }

    function scrollByDir(dir) {
      var first = scroller.querySelector('li');
      var step = first ? first.offsetWidth + 10 : 120;
      scroller.scrollBy({ left: dir * step, behavior: 'smooth' });
    }

    thumbButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var index = parseInt(btn.getAttribute('data-trackpos-gallery-index'), 10);
        setActive(btn);
        if (slides[index]) slides[index].click();
      });
    });

    btnPrev.addEventListener('click', function () {
      scrollByDir(-1);
    });
    btnNext.addEventListener('click', function () {
      scrollByDir(1);
    });

    scroller.addEventListener('scroll', updateRail, { passive: true });
    window.addEventListener('resize', updateRail);
    updateRail();
  }

  document.querySelectorAll('.trackpos-hero-gallery').forEach(initGallery);
})();
