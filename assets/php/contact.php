<?php

use PHPMailer\PHPMailer\Exception;
use PHPMailer\PHPMailer\PHPMailer;

require __DIR__ . '/PHPMailer/src/Exception.php';
require __DIR__ . '/PHPMailer/src/PHPMailer.php';
require __DIR__ . '/PHPMailer/src/SMTP.php';

require __DIR__ . '/contact-load-config.php';

$loaded = contactLoadConfig();
$config = $loaded['config'];
if ($loaded['status'] !== 'ok') {
    respond(
        'danger',
        'Contact form is not configured on the server (config file missing or invalid). Please email support@qubextrack.com.'
    );
}

$okMessage = 'Thank you! We have received your message and will contact you within 24 hours.';
$genericError = 'We could not send your message. Please try again later or email support@qubextrack.com.';

$fields = [
    'name'       => 'First name',
    'surname'    => 'Last name',
    'email'      => 'Email',
    'department' => 'How can we help?',
    'message'    => 'Message',
];

error_reporting(E_ALL & ~E_NOTICE);

try {
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        throw new Exception('Invalid request.');
    }

  // --- Anti-spam: honeypot ---
    $honeypot = $config['honeypotField'] ?? 'company_website';
    if (!empty($_POST[$honeypot])) {
        // Pretend success so bots do not adapt.
        respond('success', $okMessage);
    }

  // --- Anti-spam: minimum time on page ---
    $minSeconds = (int) ($config['minSubmitSeconds'] ?? 4);
    $loadedAt = isset($_POST['form_loaded_at']) ? (int) $_POST['form_loaded_at'] : 0;
    if ($loadedAt <= 0 || (time() - $loadedAt) < $minSeconds) {
        throw new Exception('Please wait a moment and try again.');
    }

  // --- Anti-spam: rate limit by IP ---
    $maxPerHour = (int) ($config['maxSubmissionsPerHour'] ?? 5);
    if ($maxPerHour > 0 && !rateLimitAllow(clientIp(), $maxPerHour)) {
        throw new Exception('Too many submissions from your network. Please try again in an hour or call +91-9348457123.');
    }

  // --- reCAPTCHA (when secret key is configured) ---
    $recaptchaSecret = trim((string) ($config['recaptchaSecret'] ?? ''));
    if ($recaptchaSecret !== '') {
        require __DIR__ . '/recaptcha/src/autoload.php';
        if (empty($_POST['g-recaptcha-response'])) {
            throw new Exception('Please complete the security check (reCAPTCHA).');
        }
        $recaptcha = new ReCaptcha\ReCaptcha($recaptchaSecret, new ReCaptcha\RequestMethod\CurlPost());
        $version = strtolower(trim((string) ($config['recaptchaVersion'] ?? 'v2')));
        if (!empty($config['recaptchaEnterprise'])) {
            $version = 'enterprise';
        }
        if ($version === 'v3') {
            $threshold = (float) ($config['recaptchaScoreThreshold'] ?? 0.5);
            $recaptcha->setScoreThreshold($threshold);
        }
        $verify = $recaptcha->verify($_POST['g-recaptcha-response'], clientIp());
        if (!$verify->isSuccess()) {
            $codes = $verify->getErrorCodes();
            $debug = '';
            if (!empty($config['debugContact'])) {
                $debug = ' [' . implode(', ', $codes) . ']';
                if ($version === 'v3' && method_exists($verify, 'getScore')) {
                    $debug .= ' score=' . $verify->getScore();
                }
            }
            throw new Exception(
                'Security verification failed. Please try again.' . $debug
            );
        }
    }

  // --- Validate allowed fields ---
    $name = trim((string) ($_POST['name'] ?? ''));
    $surname = trim((string) ($_POST['surname'] ?? ''));
    $email = trim((string) ($_POST['email'] ?? ''));
    $department = trim((string) ($_POST['department'] ?? ''));
    $message = trim((string) ($_POST['message'] ?? ''));

    if ($name === '' || $surname === '' || $email === '' || $department === '' || $message === '') {
        throw new Exception('Please fill in all required fields.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new Exception('Please enter a valid email address.');
    }

    if (strlen($name) > 80 || strlen($surname) > 80 || strlen($department) > 120) {
        throw new Exception('One or more fields are too long.');
    }

    if (strlen($message) > 5000) {
        throw new Exception('Message is too long (maximum 5000 characters).');
    }

    if (preg_match_all('/https?:\/\//i', $message) > 3) {
        throw new Exception('Your message contains too many links.');
    }

    $allowedDepartments = ['Free Trial', 'Demo', 'Book Demo', 'Sales Enquiry', 'Support'];
    if (!in_array($department, $allowedDepartments, true)) {
        throw new Exception('Please select how we can help.');
    }

    $data = [
        'name'       => $name,
        'surname'    => $surname,
        'email'      => $email,
        'department' => $department,
        'message'    => $message,
    ];

    $sendTo = $config['sendToEmail'] ?? 'support@qubextrack.com';
    $sendToName = $config['sendToName'] ?? 'QubexTrack';
    if ($department === 'Support' && !empty($config['supportEmail'])) {
        $sendTo = $config['supportEmail'];
        $sendToName = 'QubexTrack Support';
    }

    $emailHtml = buildEmailHtml($fields, $data, clientIp());

    $mail = new PHPMailer(true);
    $mail->CharSet = 'UTF-8';
    $mail->setFrom($config['fromEmail'] ?? 'support@qubextrack.com', $config['fromName'] ?? 'QubexTrack Website');
    $mail->addAddress($sendTo, $sendToName);
    $mail->addReplyTo($email, $name . ' ' . $surname);
    $mail->isHTML(true);
    $mail->Subject = ($config['subject'] ?? 'Website inquiry') . ' — ' . $department;
    $mail->Body = $emailHtml;
    $mail->AltBody = buildPlainText($data);

    if (!empty($config['smtpUse'])) {
        $smtpPassword = smtpPassword($config);
        if ($smtpPassword === '') {
            throw new Exception(
                'Contact email is not fully configured. Please email support@qubextrack.com directly.'
            );
        }
        $mail->isSMTP();
        $mail->Host = $config['smtpHost'] ?? '';
        $mail->SMTPAuth = true;
        $mail->Username = $config['smtpUsername'] ?? '';
        $mail->Password = $smtpPassword;
        $mail->SMTPSecure = $config['smtpSecure'] ?? 'tls';
        $mail->SMTPAutoTLS = !empty($config['smtpAutoTLS']);
        $mail->Port = (int) ($config['smtpPort'] ?? 587);
        $mail->SMTPDebug = 0;
    }

    if (!$mail->send()) {
        $detail = trim((string) $mail->ErrorInfo);
        if (!empty($config['debugContact']) && $detail !== '') {
            throw new Exception('Email could not be sent: ' . $detail);
        }
        throw new Exception($genericError);
    }

    rateLimitRecord(clientIp());
    respond('success', $okMessage);
} catch (Exception $e) {
    respond('danger', $e->getMessage() ?: $genericError);
}

function smtpPassword(array $config): string
{
    $password = trim((string) ($config['smtpPassword'] ?? ''));
    if ($password !== '') {
        return $password;
    }
    $env = getenv('TRACKPOS_SMTP_PASSWORD');
    return $env !== false ? trim((string) $env) : '';
}

function respond(string $type, string $message): void
{
    $payload = ['type' => $type, 'message' => $message];
    $isAjax = !empty($_SERVER['HTTP_X_REQUESTED_WITH'])
        && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest';

    if ($isAjax) {
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode($payload, JSON_UNESCAPED_UNICODE);
    } else {
        header('Content-Type: text/plain; charset=utf-8');
        echo $message;
    }
    exit;
}

function clientIp(): string
{
    $keys = ['HTTP_CF_CONNECTING_IP', 'HTTP_X_FORWARDED_FOR', 'REMOTE_ADDR'];
    foreach ($keys as $key) {
        if (empty($_SERVER[$key])) {
            continue;
        }
        $value = $_SERVER[$key];
        if ($key === 'HTTP_X_FORWARDED_FOR') {
            $value = trim(explode(',', $value)[0]);
        }
        if (filter_var($value, FILTER_VALIDATE_IP)) {
            return $value;
        }
    }
    return '0.0.0.0';
}

function rateLimitPath(string $ip): string
{
    $dir = __DIR__ . '/storage/rate-limit';
    if (!is_dir($dir)) {
        mkdir($dir, 0755, true);
    }
    return $dir . '/' . hash('sha256', $ip) . '.json';
}

function rateLimitAllow(string $ip, int $maxPerHour): bool
{
    $path = rateLimitPath($ip);
    if (!is_readable($path)) {
        return true;
    }
    $data = json_decode((string) file_get_contents($path), true);
    if (!is_array($data) || empty($data['times'])) {
        return true;
    }
    $cutoff = time() - 3600;
    $recent = array_filter($data['times'], static function ($t) use ($cutoff) {
        return $t >= $cutoff;
    });
    return count($recent) < $maxPerHour;
}

function rateLimitRecord(string $ip): void
{
    $path = rateLimitPath($ip);
    $times = [];
    if (is_readable($path)) {
        $data = json_decode((string) file_get_contents($path), true);
        if (is_array($data['times'] ?? null)) {
            $times = $data['times'];
        }
    }
    $cutoff = time() - 3600;
    $times = array_values(array_filter($times, static function ($t) use ($cutoff) {
        return $t >= $cutoff;
    }));
    $times[] = time();
    file_put_contents($path, json_encode(['times' => $times]), LOCK_EX);
}

function e(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function buildEmailHtml(array $labels, array $data, string $ip): string
{
    $rows = '';
    foreach ($labels as $key => $label) {
        if (!isset($data[$key])) {
            continue;
        }
        $rows .= '<tr><th style="text-align:left;padding:8px 12px;background:#f5f5ff;">' . e($label)
            . '</th><td style="padding:8px 12px;">' . nl2br(e($data[$key])) . '</td></tr>';
    }
    $rows .= '<tr><th style="text-align:left;padding:8px 12px;background:#f5f5ff;">Submitted</th><td style="padding:8px 12px;">'
        . e(gmdate('Y-m-d H:i:s') . ' UTC') . '</td></tr>';
    $rows .= '<tr><th style="text-align:left;padding:8px 12px;background:#f5f5ff;">IP</th><td style="padding:8px 12px;">'
        . e($ip) . '</td></tr>';

    return '<!DOCTYPE html><html><body style="font-family:Manrope,Arial,sans-serif;color:#343f52;">'
        . '<h2 style="color:#ff4450;">QubexTrack — contact form</h2>'
        . '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;max-width:600px;">'
        . $rows . '</table></body></html>';
}

function buildPlainText(array $data): string
{
    $lines = [];
    foreach ($data as $key => $value) {
        $lines[] = ucfirst($key) . ': ' . $value;
    }
    return implode("\n", $lines);
}
