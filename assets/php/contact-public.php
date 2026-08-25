<?php
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

require __DIR__ . '/contact-load-config.php';

$loaded = contactLoadConfig();
$config = $loaded['config'];
$status = $loaded['status'];

$use = !empty($config['recaptchaUse']) && !empty($config['recaptchaSiteKey']);
$version = 'v2';
if ($use) {
    if (!empty($config['recaptchaEnterprise'])) {
        $version = 'enterprise';
    } else {
        $version = strtolower(trim((string) ($config['recaptchaVersion'] ?? 'v2')));
        if ($version !== 'v3' && $version !== 'v2') {
            $version = 'v2';
        }
    }
}

$payload = [
    'recaptchaUse'        => $use,
    'recaptchaSiteKey'    => $use ? $config['recaptchaSiteKey'] : '',
    'recaptchaVersion'    => $use ? $version : '',
    'recaptchaEnterprise' => $use && $version === 'enterprise',
    'configStatus'        => $status,
];

echo json_encode($payload, JSON_UNESCAPED_SLASHES);
