<?php
/**
 * Copy this file to contact.config.php and set your real values.
 * Do not commit contact.config.php if it contains passwords or API secrets.
 */
return [
    // Where inquiries are delivered
    'sendToEmail' => 'support@qubextrack.com',
    'sendToName'  => 'QubexTrack Support',
  // Optional copy for Support enquiries (department = Support)
    'supportEmail' => 'support@qubextrack.com',

    // Use the same address as smtpUsername on cPanel / HeroSite hosts.
    'fromEmail' => 'support@qubextrack.com',
    'fromName'  => 'QubexTrack Website',
    'subject'   => 'New demo / contact request — QubexTrack',

    // HeroSite (magnus.herosite.pro) — SSL SMTP. User = full email address; password = mailbox password.
    'smtpUse'      => true,
    'smtpHost'     => 'magnus.herosite.pro',
    'smtpUsername' => 'support@qubextrack.com',
    'smtpPassword' => 'YOUR_MAILBOX_PASSWORD',
    'smtpSecure'   => 'ssl',
    'smtpPort'     => 465,
    'smtpAutoTLS'  => false,
    // Alternate: port 587 with 'tls' and smtpAutoTLS => true

    // reCAPTCHA — https://www.google.com/recaptcha/admin
    // Domains must include: qubextrack.com, www.qubextrack.com, ampletobuy.com, www.ampletobuy.com
    // Set recaptchaUse => false to disable until keys/domains are valid.
    'recaptchaUse'            => false,
    'recaptchaVersion'        => 'v3',
    'recaptchaSiteKey'        => 'YOUR_RECAPTCHA_SITE_KEY',
    'recaptchaSecret'         => 'YOUR_RECAPTCHA_SECRET_KEY',
    'recaptchaScoreThreshold' => 0.5,
    'recaptchaEnterprise'     => false,

    // Anti-spam (always on)
    'minSubmitSeconds'      => 4,
    'maxSubmissionsPerHour' => 5,
    'honeypotField'         => 'company_website',
];
