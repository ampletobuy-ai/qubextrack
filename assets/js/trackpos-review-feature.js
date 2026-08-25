/**
 * Syncs the large client logo (left column) with the active testimonial slide on about.html.
 */
(function () {
  var bound = false;

  function init() {
    if (bound) return;

    var section = document.querySelector(".trackpos-about-reviews");
    if (!section) return;

    var featureImg = section.querySelector(".trackpos-review-feature__img");
    var swiperEl = section.querySelector(".swiper");
    if (!featureImg || !swiperEl) return;

    function updateFromSlide(slide) {
      if (!slide) return;
      var logo = slide.querySelector(".trackpos-review-logo");
      if (!logo || !logo.src) return;

      if (logo.src === featureImg.src && logo.alt === featureImg.alt) return;

      featureImg.classList.add("is-updating");
      featureImg.src = logo.src;
      featureImg.alt = logo.alt || "";
      window.requestAnimationFrame(function () {
        featureImg.classList.remove("is-updating");
      });
    }

    function bindSwiper(swiper) {
      if (bound) return;
      bound = true;

      updateFromSlide(swiper.slides[swiper.activeIndex]);

      swiper.on("slideChange", function () {
        updateFromSlide(swiper.slides[swiper.activeIndex]);
      });
    }

    if (swiperEl.swiper) {
      bindSwiper(swiperEl.swiper);
      return;
    }

    var attempts = 0;
    var timer = window.setInterval(function () {
      attempts += 1;
      if (swiperEl.swiper) {
        window.clearInterval(timer);
        bindSwiper(swiperEl.swiper);
      } else if (attempts > 100) {
        window.clearInterval(timer);
      }
    }, 50);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
  window.addEventListener("load", init);
})();
