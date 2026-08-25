<?php
/**
 * Live contact form settings for QubexTrack.
 * Copy from contact.config.example.php and add SMTP + reCAPTCHA keys before production.
 */
return [
    'sendToEmail'  => 'support@qubextrack.com',
    'sendToName'   => 'QubexTrack Support',
    'supportEmail' => 'support@qubextrack.com',

    // Must match the mailbox used for SMTP login (HeroSite / magnus.herosite.pro).
    'fromEmail' => 'support@qubextrack.com',
    'fromName'  => 'QubexTrack Website',
    'subject'   => 'New demo / contact request — QubexTrack',

    // HeroSite outgoing mail (SSL). Host: magnus.herosite.pro or 103.86.177.4 — port 465 (SSL) or 587 (TLS).
    'smtpUse'      => true,
    'smtpHost'     => 'magnus.herosite.pro',
    'smtpUsername' => 'support@qubextrack.com',
    'smtpPassword' => 'Gopal@0047',
    'smtpSecure'   => 'ssl',
    'smtpPort'     => 465,
    'smtpAutoTLS'  => false,

    // reCAPTCHA — version must match key type in Google admin: v2 | v3 | enterprise
    'recaptchaUse'            => true,
    'recaptchaVersion'        => 'v3',
    'recaptchaSiteKey'        => '6LcCaAItAAAAAJjn96TB9EF7Ee0mvZ_VHGs6bpuU',
    'recaptchaSecret'         => '6LcCaAItAAAAADsFcn3zH5jqZefEe1URpm8LUsrl',
    'recaptchaScoreThreshold' => 0.5,
    'recaptchaEnterprise'     => false,

    'minSubmitSeconds'      => 4,
    'maxSubmissionsPerHour' => 5,
    'honeypotField'         => 'company_website',

    // Set true temporarily to show SMTP/reCAPTCHA errors in the form (turn off after fixing).
    'debugContact'          => true,
];
