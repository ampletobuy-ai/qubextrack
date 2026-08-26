# Contact form email setup

The contact form on `contact.html` posts to `assets/php/contact.php` (requires **PHP** on your server, e.g. XAMPP, aaPanel/cPanel, or VPS).

## Production (aaPanel)

| Item | Value |
|------|--------|
| Web root | `/www/wwwroot/qubextrack.com` |
| PHP | 8.2 (aaPanel → Site → PHP version) |
| Config file | `/www/wwwroot/qubextrack.com/assets/php/contact.config.php` |
| Rate limit dir | `/www/wwwroot/qubextrack.com/assets/php/storage/rate-limit/` (writable by `www`) |

GitHub Actions **Deploy Production** syncs the site into this folder. Upload `contact.config.php` once on the server (it is not overwritten on deploy).

**Stop Docker from serving the domain** if you still run `/opt/marketing-site` — otherwise `qubextrack.com` may hit static nginx (no PHP) instead of aaPanel:

```bash
cd /opt/marketing-site && docker compose down
```

Verify PHP works: open `https://qubextrack.com/assets/php/contact-public.php` — you should see JSON (`"configStatus":"ok"`), not PHP source code.

## 1. Configure mail

1. Copy `contact.config.example.php` to `contact.config.php` (already present with defaults).
2. **Upload `contact.config.php` to the server** at `assets/php/contact.config.php` (same folder as `contact.php`). It is often omitted from FTP uploads because it contains secrets.

### Check config on the live server

Open: `https://www.qubextrack.com/assets/php/contact-public.php`

**Healthy response:**

```json
{
  "recaptchaUse": true,
  "recaptchaSiteKey": "6LcCaAItAAAAA…",
  "recaptchaVersion": "v3",
  "recaptchaEnterprise": false,
  "configStatus": "ok"
}
```

**Broken (config not loaded):**

```json
{
  "recaptchaUse": false,
  "recaptchaSiteKey": "",
  "recaptchaVersion": "",
  "recaptchaEnterprise": false,
  "configStatus": "missing"
}
```

| `configStatus` | Meaning |
|----------------|---------|
| `ok` | Config loaded |
| `missing` | `contact.config.php` not on server — upload it |
| `not_readable` | File exists but PHP cannot read it (permissions) |
| `parse_error` | Syntax error in `contact.config.php` (fix commas/quotes) |
| `invalid` | File did not return an array |
2. Set `sendToEmail` / `supportEmail` if needed (default: support@qubextrack.com).
3. **HeroSite / magnus.herosite.pro SMTP** (configured in `contact.config.php`):
   - **Outgoing server:** `magnus.herosite.pro` (or `103.86.177.4`)
   - **Port:** `465` with **SSL** (`smtpSecure` => `ssl`, `smtpAutoTLS` => false)
   - **Username:** full email address, e.g. `support@qubextrack.com`
   - **Password:** your mailbox password — set `smtpPassword` in `contact.config.php`, or on the server set environment variable `TRACKPOS_SMTP_PASSWORD` (preferred so the password is not in the repo)
   - Alternate: port **587** with `smtpSecure` => `tls` and `smtpAutoTLS` => true
   - Incoming (for reference only): IMAP `993`, POP `995` — not used by the contact form

## 2. Enable reCAPTCHA (recommended)

### reCAPTCHA v3 (current setup — invisible score)

1. Create **reCAPTCHA v3** keys in [Google reCAPTCHA admin](https://www.google.com/recaptcha/admin).
2. In `contact.config.php` set `recaptchaVersion` => `'v3'`, plus site key and secret.
3. Optional: `recaptchaScoreThreshold` => `0.5` (0.0–1.0; higher = stricter).
4. The form loads `api.js?render=SITE_KEY` and runs `grecaptcha.execute()` on **Send message** (no checkbox).
5. A small reCAPTCHA badge appears on the page (required by Google).

**“Invalid key type”** means the key type does not match `recaptchaVersion` (e.g. v3 keys with v2 checkbox code).

### reCAPTCHA Enterprise (optional)

1. In [Google reCAPTCHA admin](https://www.google.com/recaptcha/admin), create **reCAPTCHA Enterprise** keys for your site.
2. Under **Domains**, add every host that will show the form, e.g. `www.qubextrack.com`, `www.www.qubextrack.com`, and `localhost` for local testing.
3. In `contact.config.php` set:
   - `recaptchaUse` => true
   - `recaptchaEnterprise` => true
   - `recaptchaSiteKey` => site key (e.g. `6LcCaAItAAAAA…`)
   - `recaptchaSecret` => secret key
4. The contact page loads `https://www.google.com/recaptcha/enterprise.js?render=SITE_KEY` and attaches **Send message** as a `g-recaptcha` button (`data-callback`, `data-action`) — same as Google’s **“On an HTML button”** instructions.

If you still see **“This reCAPTCHA is for testing purposes only”**, you are either using Google’s **test keys** (`6LeIxAcT…`) or the **domain is not listed** on the key — fix domains in admin, not the HTML.

### Classic reCAPTCHA v2 checkbox (optional)

Set `recaptchaVersion` => `'v2'`. The form shows the “I’m not a robot” checkbox.

Without reCAPTCHA keys, the form still uses **honeypot**, **minimum time on page**, **rate limiting**, and field validation.

## 3. Server permissions

Ensure PHP can write rate-limit files:

`assets/php/storage/rate-limit/` (chmod 755 or 775)

## 4. Test locally (XAMPP)

1. Copy the `dist` folder into `htdocs`.
2. Open `http://localhost/.../contact.html`.
3. Fill the form, wait at least 4 seconds, submit.
4. Check `support@qubextrack.com` inbox (or Mailhog if you configure SMTP locally).

## Anti-spam layers

| Layer | Description |
|-------|-------------|
| Honeypot | Hidden `company_website` field — bots that fill it get a fake success |
| Time check | Rejects submits faster than 4 seconds |
| Rate limit | Max 5 submissions per IP per hour |
| reCAPTCHA | Optional Google checkbox when keys are set |
| Validation | Email format, field length, link count in message |
