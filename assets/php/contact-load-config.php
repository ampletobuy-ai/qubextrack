<?php
/**
 * Load contact.config.php safely (shared by contact.php and contact-public.php).
 *
 * @return array{config: array, status: string}
 */
function contactLoadConfig(): array
{
    $configFile = __DIR__ . '/contact.config.php';

    if (!is_file($configFile)) {
        return ['config' => [], 'status' => 'missing'];
    }

    if (!is_readable($configFile)) {
        return ['config' => [], 'status' => 'not_readable'];
    }

    try {
        $loaded = require $configFile;
    } catch (Throwable $e) {
        return ['config' => [], 'status' => 'parse_error'];
    }

    if (!is_array($loaded)) {
        return ['config' => [], 'status' => 'invalid'];
    }

    return ['config' => $loaded, 'status' => 'ok'];
}
