<?php
/**
 * List product screenshots for an industry folder.
 * GET ?industry=retail|jewellery|hotel|restaurant|hospital
 */
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('Access-Control-Allow-Origin: *');

$allowed = ['retail', 'jewellery', 'hotel', 'restaurant', 'hospital'];
$industry = strtolower(trim((string) ($_GET['industry'] ?? '')));

if (!in_array($industry, $allowed, true)) {
    http_response_code(400);
    echo json_encode(['ok' => false, 'error' => 'Invalid industry', 'images' => []]);
    exit;
}

$dir = realpath(__DIR__ . '/../img/photos/' . $industry);
$photosRoot = realpath(__DIR__ . '/../img/photos');

if ($dir === false || $photosRoot === false || strpos($dir, $photosRoot) !== 0 || !is_dir($dir)) {
    http_response_code(404);
    echo json_encode(['ok' => false, 'error' => 'Folder not found', 'images' => []]);
    exit;
}

$exclude = '/(necklace|rings|atmosphere|hero|blurry|manifest)/i';
$images = [];

foreach (scandir($dir) ?: [] as $file) {
    if ($file === '.' || $file === '..') {
        continue;
    }
    $path = $dir . DIRECTORY_SEPARATOR . $file;
    if (!is_file($path)) {
        continue;
    }
    if (!preg_match('/\.(png|jpe?g|webp|gif)$/i', $file)) {
        continue;
    }
    if (preg_match($exclude, $file)) {
        continue;
    }
    $images[] = [
        'file' => $file,
        'url' => './assets/img/photos/' . $industry . '/' . rawurlencode($file),
        'mtime' => filemtime($path) ?: 0,
    ];
}

usort($images, static function ($a, $b) {
    // Prefer POS / dashboard first, then alphabetical.
    $score = static function ($name) {
        $n = strtolower($name);
        if (strpos($n, 'pos') !== false) {
            return 0;
        }
        if (strpos($n, 'dashboard') !== false || strpos($n, 'availability') !== false) {
            return 1;
        }
        return 2;
    };
    $sa = $score($a['file']);
    $sb = $score($b['file']);
    if ($sa !== $sb) {
        return $sa <=> $sb;
    }
    return strcasecmp($a['file'], $b['file']);
});

echo json_encode([
    'ok' => true,
    'industry' => $industry,
    'count' => count($images),
    'images' => $images,
], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
