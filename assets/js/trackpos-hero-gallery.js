/**
 * Hero screenshot gallery — loads images from assets/img/photos/{industry}/.
 * Prefers manifest.json (static), then PHP list API.
 * Thumbnail boxes without text labels; horizontal scroll rail with prev/next.
 * Single-image lightbox with previous / next (not multi-slide GLightbox).
 */
(function () {
  var viewer = null;

  function titleFromFile(file) {
    var base = String(file || '').replace(/\.[^.]+$/, '');
    base = base.replace(/^(jewellery|hotel|restaurant|retail|hospital)-/i, '');
    base = base.replace(/-screenshot$/i, '');
    base = base.replace(/[-_]+/g, ' ').trim();
    if (/^pos$/i.test(base)) return 'POS';
    if (/profit\s*loss|^pl$/i.test(base)) return 'Profit & Loss';
    if (/gstr/i.test(base)) return 'GSTR-1';
    if (/^report$/i.test(base)) return 'Report';
    return base.replace(/\b([a-z])/g, function (m, c) {
      return c.toUpperCase();
    });
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function assetUrl(path) {
    try {
      return new URL(path, window.location.href).href;
    } catch (e) {
      return path;
    }
  }

  function fetchJson(url) {
    return fetch(url, { credentials: 'same-origin', cache: 'no-store' }).then(function (res) {
      if (!res.ok) throw new Error(String(res.status));
      return res.json();
    });
  }

  function normalizeImages(images) {
    return (images || []).map(function (img) {
      var url = img.url || '';
      if (url.indexOf('./') === 0 || url.indexOf('../') === 0 || url.indexOf('/') !== 0) {
        url = assetUrl(url);
      }
      return {
        file: img.file || '',
        url: url,
        mtime: img.mtime || 0,
      };
    });
  }

  function fetchImages(industry) {
    var q = encodeURIComponent(industry);
    var bust = Date.now();
    var urls = [
      assetUrl('./assets/img/photos/' + q + '/manifest.json?t=' + bust),
      assetUrl('./assets/php/list-industry-photos.php?industry=' + q),
    ];

    var chain = Promise.reject(new Error('start'));
    urls.forEach(function (url) {
      chain = chain.catch(function () {
        return fetchJson(url).then(function (data) {
          if (!data || !Array.isArray(data.images) || !data.images.length) {
            throw new Error('empty');
          }
          return normalizeImages(data.images);
        });
      });
    });
    return chain;
  }

  function imagesFromDom(gallery) {
    var thumbs = gallery.querySelectorAll('.trackpos-hero-thumbs__link img');
    var out = [];
    thumbs.forEach(function (img) {
      var src = img.getAttribute('src');
      if (!src) return;
      var file = src.split('/').pop().split('?')[0];
      out.push({ file: decodeURIComponent(file), url: assetUrl(src) });
    });
    return out;
  }

  function railMarkup() {
    return (
      '<div class="trackpos-hero-thumbs-rail">' +
      '<button type="button" class="trackpos-hero-thumbs__nav trackpos-hero-thumbs__nav--prev" aria-label="Scroll thumbnails left" disabled>' +
      '<i class="uil uil-angle-left-b" aria-hidden="true"></i>' +
      '</button>' +
      '<div class="trackpos-hero-thumbs__viewport">' +
      '<ul class="trackpos-hero-thumbs" aria-label="Screenshot thumbnails"></ul>' +
      '</div>' +
      '<button type="button" class="trackpos-hero-thumbs__nav trackpos-hero-thumbs__nav--next" aria-label="Scroll thumbnails right">' +
      '<i class="uil uil-angle-right-b" aria-hidden="true"></i>' +
      '</button>' +
      '</div>'
    );
  }

  function ensureThumbsHost(gallery) {
    var wrap = gallery.querySelector('.trackpos-hero-thumbs-wrap');
    if (wrap) {
      if (!wrap.querySelector('.trackpos-hero-thumbs__nav--prev')) {
        var existingList = wrap.querySelector('.trackpos-hero-thumbs');
        var keep = existingList ? existingList.innerHTML : '';
        wrap.innerHTML = railMarkup();
        if (keep) wrap.querySelector('.trackpos-hero-thumbs').innerHTML = keep;
      }
      return wrap.querySelector('.trackpos-hero-thumbs');
    }

    wrap = document.createElement('div');
    wrap.className = 'trackpos-hero-thumbs-wrap';
    wrap.innerHTML = railMarkup();

    var caption = gallery.querySelector('.trackpos-hero-gallery__caption');
    var mainLink = gallery.querySelector('.trackpos-hero-lightbox');
    if (mainLink) {
      var insertAfter = mainLink;
      var next = mainLink.nextElementSibling;
      while (next && next.classList && next.classList.contains('trackpos-hero-gallery__extra')) {
        insertAfter = next;
        next = next.nextElementSibling;
      }
      insertAfter.insertAdjacentElement('afterend', wrap);
    } else if (caption) {
      caption.insertAdjacentElement('beforebegin', wrap);
    } else {
      gallery.appendChild(wrap);
    }
    return wrap.querySelector('.trackpos-hero-thumbs');
  }

  function setMainImage(gallery, image, index, total) {
    var mainLink = gallery.querySelector('.trackpos-hero-lightbox');
    var mainImg = gallery.querySelector('.trackpos-hero-screenshot');
    if (!mainLink || !mainImg || !image) return;

    var industry = gallery.getAttribute('data-trackpos-gallery-industry') || 'product';
    var title = titleFromFile(image.file);

    mainLink.setAttribute('href', image.url);
    mainLink.removeAttribute('data-glightbox');
    mainLink.setAttribute(
      'aria-label',
      'View product screenshots — ' + title + ' (' + (index + 1) + ' of ' + total + ')'
    );
    mainImg.setAttribute('src', image.url);
    mainImg.setAttribute('alt', 'QubexTrack ' + industry + ' — ' + title);
  }

  function syncThumbActive(gallery, index) {
    gallery.querySelectorAll('[data-trackpos-gallery-index]').forEach(function (btn) {
      var i = parseInt(btn.getAttribute('data-trackpos-gallery-index'), 10);
      btn.classList.toggle('is-active', i === index);
    });
  }

  function ensureViewer() {
    if (viewer) return viewer;

    var root = document.createElement('div');
    root.className = 'trackpos-shot-viewer';
    root.setAttribute('hidden', '');
    root.innerHTML =
      '<div class="trackpos-shot-viewer__backdrop" data-trackpos-viewer-close></div>' +
      '<button type="button" class="trackpos-shot-viewer__close" data-trackpos-viewer-close aria-label="Close">' +
      '<i class="uil uil-times" aria-hidden="true"></i>' +
      '</button>' +
      '<button type="button" class="trackpos-shot-viewer__nav trackpos-shot-viewer__nav--prev" data-trackpos-viewer-prev aria-label="Previous image">' +
      '<i class="uil uil-angle-left-b" aria-hidden="true"></i>' +
      '</button>' +
      '<button type="button" class="trackpos-shot-viewer__nav trackpos-shot-viewer__nav--next" data-trackpos-viewer-next aria-label="Next image">' +
      '<i class="uil uil-angle-right-b" aria-hidden="true"></i>' +
      '</button>' +
      '<div class="trackpos-shot-viewer__stage">' +
      '<img class="trackpos-shot-viewer__img" alt="">' +
      '<p class="trackpos-shot-viewer__counter"></p>' +
      '</div>';

    document.body.appendChild(root);

    viewer = {
      root: root,
      img: root.querySelector('.trackpos-shot-viewer__img'),
      counter: root.querySelector('.trackpos-shot-viewer__counter'),
      btnPrev: root.querySelector('[data-trackpos-viewer-prev]'),
      btnNext: root.querySelector('[data-trackpos-viewer-next]'),
      gallery: null,
      index: 0,
    };

    function onKey(e) {
      if (root.hasAttribute('hidden')) return;
      if (e.key === 'Escape') closeViewer();
      else if (e.key === 'ArrowLeft') stepViewer(-1);
      else if (e.key === 'ArrowRight') stepViewer(1);
    }

    root.addEventListener('click', function (e) {
      var t = e.target;
      if (t.closest('[data-trackpos-viewer-close]')) closeViewer();
      else if (t.closest('[data-trackpos-viewer-prev]')) stepViewer(-1);
      else if (t.closest('[data-trackpos-viewer-next]')) stepViewer(1);
    });

    document.addEventListener('keydown', onKey);
    return viewer;
  }

  function renderViewer() {
    if (!viewer || !viewer.gallery) return;
    var images = viewer.gallery._trackposImages || [];
    if (!images.length) return;

    var index = ((viewer.index % images.length) + images.length) % images.length;
    viewer.index = index;
    viewer.gallery._trackposIndex = index;

    var image = images[index];
    viewer.img.setAttribute('src', image.url);
    viewer.img.setAttribute('alt', titleFromFile(image.file));
    viewer.counter.textContent = index + 1 + ' / ' + images.length;

    var multi = images.length > 1;
    viewer.btnPrev.hidden = !multi;
    viewer.btnNext.hidden = !multi;

    setMainImage(viewer.gallery, image, index, images.length);
    syncThumbActive(viewer.gallery, index);
  }

  function openViewer(gallery, index) {
    var v = ensureViewer();
    v.gallery = gallery;
    v.index = index || 0;
    renderViewer();
    v.root.removeAttribute('hidden');
    document.documentElement.classList.add('trackpos-shot-viewer-open');
  }

  function closeViewer() {
    if (!viewer) return;
    viewer.root.setAttribute('hidden', '');
    document.documentElement.classList.remove('trackpos-shot-viewer-open');
  }

  function stepViewer(dir) {
    if (!viewer || !viewer.gallery) return;
    var images = viewer.gallery._trackposImages || [];
    if (images.length < 2) return;
    viewer.index += dir;
    renderViewer();
  }

  function bindThumbsRail(gallery) {
    var images = gallery._trackposImages || imagesFromDom(gallery);
    gallery._trackposImages = images;
    if (typeof gallery._trackposIndex !== 'number') gallery._trackposIndex = 0;

    var thumbButtons = gallery.querySelectorAll('[data-trackpos-gallery-index]');
    var rail = gallery.querySelector('.trackpos-hero-thumbs-rail');
    if (!thumbButtons.length || !rail) return;

    var scroller = rail.querySelector('.trackpos-hero-thumbs');
    var btnPrev = rail.querySelector('.trackpos-hero-thumbs__nav--prev');
    var btnNext = rail.querySelector('.trackpos-hero-thumbs__nav--next');
    if (!scroller || !btnPrev || !btnNext) return;

    function setActive(btn) {
      thumbButtons.forEach(function (b) {
        b.classList.toggle('is-active', b === btn);
      });
      try {
        btn.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
      } catch (e) {}
    }

    function updateRail() {
      var maxScroll = scroller.scrollWidth - scroller.clientWidth;
      var scrollable = maxScroll > 4;
      rail.classList.toggle('is-scrollable', scrollable);
      if (!scrollable) {
        btnPrev.disabled = true;
        btnNext.disabled = true;
        rail.classList.remove('can-scroll-left', 'can-scroll-right');
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
      btn.onclick = function (event) {
        if (event) {
          event.preventDefault();
          event.stopPropagation();
        }
        var index = parseInt(btn.getAttribute('data-trackpos-gallery-index'), 10);
        if (isNaN(index) || index < 0) return;

        var image = images[index];
        if (!image) {
          var thumbImg = btn.querySelector('img');
          if (!thumbImg || !thumbImg.getAttribute('src')) return;
          image = {
            file: (thumbImg.getAttribute('src') || '').split('/').pop(),
            url: assetUrl(thumbImg.getAttribute('src')),
          };
        }

        gallery._trackposIndex = index;
        setActive(btn);
        setMainImage(gallery, image, index, images.length || 1);
      };
    });

    var mainLink = gallery.querySelector('.trackpos-hero-lightbox');
    if (mainLink) {
      mainLink.onclick = function (event) {
        if (event) {
          event.preventDefault();
          event.stopPropagation();
        }
        openViewer(gallery, gallery._trackposIndex || 0);
      };
    }

    btnPrev.onclick = function () {
      scrollByDir(-1);
    };
    btnNext.onclick = function () {
      scrollByDir(1);
    };

    scroller.onscroll = updateRail;
    if (rail._trackposResize) {
      window.removeEventListener('resize', rail._trackposResize);
    }
    rail._trackposResize = updateRail;
    window.addEventListener('resize', updateRail);

    scroller.querySelectorAll('img').forEach(function (img) {
      if (!img.complete) img.addEventListener('load', updateRail, { once: true });
    });
    requestAnimationFrame(updateRail);
    setTimeout(updateRail, 120);
  }

  function cleanupExtras(gallery) {
    gallery.querySelectorAll('.trackpos-hero-gallery__extra').forEach(function (el) {
      el.remove();
    });
  }

  function renderGallery(gallery, images) {
    if (!images.length) return;

    gallery._trackposImages = images;
    gallery._trackposIndex = 0;

    cleanupExtras(gallery);
    setMainImage(gallery, images[0], 0, images.length);

    var caption = gallery.querySelector('.trackpos-hero-gallery__caption');
    if (caption) {
      caption.textContent =
        images.length > 1
          ? 'Product screenshots (' +
            images.length +
            ') — click a thumbnail or the image to view full size.'
          : 'Product screenshot — click to enlarge.';
    }

    var thumbs = ensureThumbsHost(gallery);
    thumbs.innerHTML = images
      .map(function (img, index) {
        var active = index === 0 ? ' is-active' : '';
        return (
          '<li>' +
          '<button type="button" class="trackpos-hero-thumbs__link trackpos-hero-thumbs__link--image-only' +
          active +
          '" data-trackpos-gallery-index="' +
          index +
          '" aria-label="View ' +
          escapeHtml(titleFromFile(img.file)) +
          ' screenshot">' +
          '<img src="' +
          escapeHtml(img.url) +
          '" width="160" height="90" alt="" loading="lazy" decoding="async">' +
          '</button>' +
          '</li>'
        );
      })
      .join('');

    bindThumbsRail(gallery);
  }

  function initGallery(gallery) {
    var industry = gallery.getAttribute('data-trackpos-gallery-industry');
    if (!industry) return;

    ensureThumbsHost(gallery);
    gallery._trackposImages = imagesFromDom(gallery);
    cleanupExtras(gallery);
    bindThumbsRail(gallery);

    fetchImages(industry)
      .then(function (images) {
        renderGallery(gallery, images);
      })
      .catch(function () {
        if (gallery._trackposImages && gallery._trackposImages.length) {
          renderGallery(gallery, gallery._trackposImages);
        } else {
          bindThumbsRail(gallery);
        }
      });
  }

  function boot() {
    document.querySelectorAll('.trackpos-hero-gallery').forEach(initGallery);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
