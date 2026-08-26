/**
 * QubexTrack contact form — timestamp, reCAPTCHA (v2 checkbox or Enterprise button), AJAX submit.
 */
(function () {
  "use strict";

  var form = document.querySelector("form.contact-form");
  if (!form) return;

  var messagesEl = form.querySelector(".messages");
  var submitBtn = form.querySelector(".btn-send, [type='submit'], button.btn-send");
  var recaptchaMount = document.getElementById("trackpos-recaptcha");
  var loadedAtInput = form.querySelector('input[name="form_loaded_at"]');
  var recaptchaEnterprise = false;
  var recaptchaV3 = false;
  var recaptchaV3SiteKey = "";
  var recaptchaRequired = false;

  if (loadedAtInput) {
    loadedAtInput.value = String(Math.floor(Date.now() / 1000));
  }

  function processFormSubmit() {
    if (!form.checkValidity()) {
      form.classList.add("was-validated");
      var firstInvalid = form.querySelector(":invalid");
      if (firstInvalid && typeof firstInvalid.focus === "function") {
        firstInvalid.focus();
      }
      return;
    }

    form.classList.add("was-validated");

    if (recaptchaV3) {
      setSubmitting(true);
      executeRecaptchaV3()
        .then(function (token) {
          setRecaptchaToken(token);
          ajaxSubmit();
        })
        .catch(function () {
          showAlert(
            "danger",
            "Security check (reCAPTCHA) could not run. Please refresh and try again."
          );
          setSubmitting(false);
        });
      return;
    }

    ajaxSubmit();
  }

  function showAlert(type, text) {
    if (!messagesEl || !text) return;
    var alertClass = type === "success" ? "alert-success" : "alert-danger";
    messagesEl.innerHTML =
      '<div class="alert ' +
      alertClass +
      ' alert-dismissible fade show" role="alert">' +
      '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
      text +
      "</div>";
    messagesEl.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  function setSubmitting(busy) {
    if (!submitBtn) return;
    submitBtn.disabled = busy;
    submitBtn.setAttribute("aria-busy", busy ? "true" : "false");
  }

  function setRecaptchaToken(token) {
    var hid = form.querySelector('input[name="g-recaptcha-response"]');
    if (!hid) {
      hid = document.createElement("input");
      hid.type = "hidden";
      hid.name = "g-recaptcha-response";
      form.appendChild(hid);
    }
    hid.value = token;
  }

  function resetRecaptcha() {
    if (!window.grecaptcha) return;
    if (recaptchaEnterprise && window.grecaptcha.enterprise) {
      window.grecaptcha.enterprise.reset();
      return;
    }
    if (!recaptchaMount) return;
    var widgetId = recaptchaMount.getAttribute("data-widget-id");
    if (widgetId !== null && widgetId !== "") {
      window.grecaptcha.reset(parseInt(widgetId, 10));
    }
  }

  function hasRecaptchaToken() {
    var el = form.querySelector('textarea[name="g-recaptcha-response"]');
    if (el && el.value) return true;
    el = form.querySelector('input[name="g-recaptcha-response"]');
    return !!(el && el.value);
  }

  function ajaxSubmit() {
    if (recaptchaRequired && !hasRecaptchaToken()) {
      showAlert(
        "danger",
        "Please complete the security check (reCAPTCHA) before sending."
      );
      return;
    }

    setSubmitting(true);
    if (messagesEl) messagesEl.innerHTML = "";

    var action = form.getAttribute("action") || "./assets/php/contact.php";
    var data = new FormData(form);

    fetch(action, {
      method: "POST",
      body: data,
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then(function (res) {
        return res.text().then(function (text) {
          var payload = null;
          try {
            payload = JSON.parse(text);
          } catch (e) {
            var start = text.indexOf("{");
            var end = text.lastIndexOf("}");
            if (start !== -1 && end > start) {
              try {
                payload = JSON.parse(text.slice(start, end + 1));
              } catch (e2) {
                payload = null;
              }
            }
          }
          if (payload && typeof payload === "object") {
            return payload;
          }
          return {
            type: res.ok ? "success" : "danger",
            message:
              (text && text.replace(/<[^>]+>/g, " ").trim()) ||
              "Something went wrong. Please try again.",
          };
        });
      })
      .then(function (payload) {
        showAlert(payload.type || "danger", payload.message || "Something went wrong.");
        if (payload.type === "success") {
          form.reset();
          form.classList.remove("was-validated");
          if (loadedAtInput) {
            loadedAtInput.value = String(Math.floor(Date.now() / 1000));
          }
          resetRecaptcha();
        } else {
          // Keep field values; drop Bootstrap "invalid" chrome after a server-side failure.
          form.classList.remove("was-validated");
        }
      })
      .catch(function () {
        form.classList.remove("was-validated");
        showAlert(
          "danger",
          "Network error. Please try again or email support@qubextrack.com."
        );
      })
      .finally(function () {
        setSubmitting(false);
      });
  }

  /** Google Enterprise “On an HTML button” callback (see reCAPTCHA admin setup). */
  window.trackposEnterpriseRecaptchaCallback = function (token) {
    if (!form.checkValidity()) {
      form.classList.add("was-validated");
      resetRecaptcha();
      return;
    }
    form.classList.add("was-validated");
    setRecaptchaToken(token);
    ajaxSubmit();
  };

  function loadRecaptchaScriptV2() {
    return new Promise(function (resolve, reject) {
      if (window.grecaptcha && !window.grecaptcha.enterprise) {
        resolve();
        return;
      }
      if (document.querySelector('script[src*="recaptcha/api.js"]')) {
        var wait = setInterval(function () {
          if (window.grecaptcha) {
            clearInterval(wait);
            resolve();
          }
        }, 50);
        setTimeout(function () {
          clearInterval(wait);
          reject(new Error("reCAPTCHA timeout"));
        }, 10000);
        return;
      }
      var script = document.createElement("script");
      script.src =
        "https://www.google.com/recaptcha/api.js?onload=trackposRecaptchaOnload&render=explicit";
      script.async = true;
      script.defer = true;
      window.trackposRecaptchaOnload = function () {
        resolve();
      };
      script.onerror = function () {
        reject(new Error("reCAPTCHA failed to load"));
      };
      document.head.appendChild(script);
    });
  }

  function loadRecaptchaScriptEnterprise(siteKey) {
    return new Promise(function (resolve, reject) {
      if (window.grecaptcha && window.grecaptcha.enterprise) {
        resolve();
        return;
      }
      var existing = document.querySelector('script[src*="recaptcha/enterprise.js"]');
      if (existing) {
        var wait = setInterval(function () {
          if (window.grecaptcha && window.grecaptcha.enterprise) {
            clearInterval(wait);
            resolve();
          }
        }, 50);
        setTimeout(function () {
          clearInterval(wait);
          reject(new Error("reCAPTCHA Enterprise timeout"));
        }, 10000);
        return;
      }
      var script = document.createElement("script");
      script.src =
        "https://www.google.com/recaptcha/enterprise.js?render=" +
        encodeURIComponent(siteKey);
      script.async = true;
      script.defer = true;
      script.onload = function () {
        resolve();
      };
      script.onerror = function () {
        reject(new Error("reCAPTCHA Enterprise failed to load"));
      };
      document.head.appendChild(script);
    });
  }

  function ensureRecaptchaMount() {
    var wrap = document.getElementById("trackpos-recaptcha-wrap");
    if (!wrap) return null;
    var mount = document.getElementById("trackpos-recaptcha");
    if (!mount) {
      mount = document.createElement("div");
      mount.id = "trackpos-recaptcha";
      wrap.appendChild(mount);
    }
    recaptchaMount = mount;
    return mount;
  }

  function renderRecaptchaV2(siteKey) {
    var mount = ensureRecaptchaMount();
    if (!mount || !window.grecaptcha) return;
    var wrap = document.getElementById("trackpos-recaptcha-wrap");
    if (wrap) {
      wrap.style.display = "";
      wrap.classList.remove("trackpos-recaptcha-wrap--v3");
    }
    if (mount.getAttribute("data-widget-id")) return;
    var id = window.grecaptcha.render(mount, {
      sitekey: siteKey,
      theme: "light",
    });
    mount.setAttribute("data-widget-id", String(id));
  }

  function ensureSubmitButton() {
    if (!submitBtn || submitBtn.tagName !== "INPUT") return submitBtn;
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = submitBtn.className;
    btn.textContent = submitBtn.value || "Send message";
    submitBtn.parentNode.replaceChild(btn, submitBtn);
    return btn;
  }

  function initRecaptchaEnterprise(siteKey) {
    recaptchaEnterprise = true;
    recaptchaV3 = false;
    var wrap = document.getElementById("trackpos-recaptcha-wrap");
    if (wrap) wrap.style.display = "none";

    return loadRecaptchaScriptEnterprise(siteKey).then(function () {
      submitBtn = ensureSubmitButton();
      if (!submitBtn) return;
      submitBtn.classList.add("g-recaptcha");
      submitBtn.setAttribute("data-sitekey", siteKey);
      submitBtn.setAttribute("data-callback", "trackposEnterpriseRecaptchaCallback");
      submitBtn.setAttribute("data-action", "contact_submit");
    });
  }

  function initRecaptchaV2(siteKey) {
    recaptchaEnterprise = false;
    recaptchaV3 = false;
    return loadRecaptchaScriptV2().then(function () {
      renderRecaptchaV2(siteKey);
    });
  }

  function loadRecaptchaScriptV3(siteKey) {
    return new Promise(function (resolve, reject) {
      if (window.grecaptcha && typeof window.grecaptcha.execute === "function") {
        resolve();
        return;
      }
      var src =
        "https://www.google.com/recaptcha/api.js?render=" + encodeURIComponent(siteKey);
      if (document.querySelector('script[src*="recaptcha/api.js?render="]')) {
        var wait = setInterval(function () {
          if (window.grecaptcha && window.grecaptcha.execute) {
            clearInterval(wait);
            resolve();
          }
        }, 50);
        setTimeout(function () {
          clearInterval(wait);
          reject(new Error("reCAPTCHA v3 timeout"));
        }, 10000);
        return;
      }
      var script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.defer = true;
      script.onload = function () {
        resolve();
      };
      script.onerror = function () {
        reject(new Error("reCAPTCHA v3 failed to load"));
      };
      document.head.appendChild(script);
    });
  }

  function initRecaptchaV3(siteKey) {
    recaptchaEnterprise = false;
    recaptchaV3 = true;
    recaptchaV3SiteKey = siteKey;
    var wrap = document.getElementById("trackpos-recaptcha-wrap");
    if (wrap) {
      wrap.style.display = "";
      wrap.classList.add("trackpos-recaptcha-wrap--v3");
      var box = wrap.querySelector("#trackpos-recaptcha");
      if (box) box.remove();
      recaptchaMount = null;
      if (!wrap.querySelector(".trackpos-recaptcha-v3-note")) {
        wrap.innerHTML =
          '<p class="trackpos-recaptcha-v3-note !mb-0">This site is protected by reCAPTCHA. Google <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer">Privacy Policy</a> and <a href="https://policies.google.com/terms" target="_blank" rel="noopener noreferrer">Terms of Service</a> apply.</p>';
      }
    }
    return loadRecaptchaScriptV3(siteKey);
  }

  function executeRecaptchaV3() {
    return new Promise(function (resolve, reject) {
      if (!window.grecaptcha || !window.grecaptcha.execute) {
        reject(new Error("reCAPTCHA v3 not loaded"));
        return;
      }
      window.grecaptcha.ready(function () {
        window.grecaptcha
          .execute(recaptchaV3SiteKey, { action: "contact_submit" })
          .then(resolve)
          .catch(reject);
      });
    });
  }

  function readFormRecaptchaConfig() {
    var siteKey = (form.getAttribute("data-recaptcha-site-key") || "").trim();
    var version = (form.getAttribute("data-recaptcha-version") || "").toLowerCase();
    var useAttr = form.getAttribute("data-recaptcha-use");
    return {
      recaptchaUse: useAttr === "false" ? false : siteKey !== "",
      recaptchaSiteKey: siteKey,
      recaptchaVersion: version === "v2" || version === "v3" ? version : "",
      recaptchaEnterprise: form.getAttribute("data-recaptcha-enterprise") === "true",
    };
  }

  function resolveSiteKey(cfg) {
    if (!cfg || cfg.recaptchaUse === false) {
      return "";
    }
    if (cfg.recaptchaUse && cfg.recaptchaSiteKey) {
      return cfg.recaptchaSiteKey;
    }
    return "";
  }

  function initFromConfig(cfg) {
    var siteKey = resolveSiteKey(cfg);
    recaptchaRequired = !!(cfg && cfg.recaptchaUse && siteKey);
    if (!siteKey) {
      recaptchaRequired = false;
      recaptchaV3 = false;
      recaptchaEnterprise = false;
      var wrap = document.getElementById("trackpos-recaptcha-wrap");
      if (wrap) wrap.style.display = "none";
      return Promise.resolve();
    }
    var version = (cfg && cfg.recaptchaVersion) || "v3";
    if (cfg && cfg.recaptchaEnterprise) {
      version = "enterprise";
    }
    if (version === "v3") {
      return initRecaptchaV3(siteKey);
    }
    if (version === "enterprise") {
      return initRecaptchaEnterprise(siteKey);
    }
    return initRecaptchaV2(siteKey);
  }

  // Load reCAPTCHA only from server config (avoids invalid hardcoded keys / domain errors).
  fetch("./assets/php/contact-public.php", { credentials: "same-origin" })
    .then(function (r) {
      if (!r.ok) throw new Error("config unavailable");
      return r.json();
    })
    .then(function (serverCfg) {
      return initFromConfig(serverCfg);
    })
    .catch(function () {
      var wrap = document.getElementById("trackpos-recaptcha-wrap");
      if (wrap) wrap.style.display = "none";
      recaptchaRequired = false;
    });

  form.addEventListener(
    "submit",
    function (event) {
      if (!form.classList.contains("contact-form")) return;

      event.preventDefault();
      event.stopPropagation();
      event.stopImmediatePropagation();

      if (recaptchaEnterprise) {
        return;
      }

      processFormSubmit();
    },
    true
  );

  if (submitBtn) {
    submitBtn.addEventListener("click", function (event) {
      if (submitBtn.type === "button") {
        event.preventDefault();
        processFormSubmit();
      }
    });
  }
})();
