#!/usr/bin/env bash
# Post-deploy helper for aaPanel PHP sites (e.g. /www/wwwroot/qubextrack.com).
# Called from GitHub Actions after files are synced.

set -euo pipefail

DEPLOY_PATH="${1:-/www/wwwroot/qubextrack.com}"
PHP_STORAGE="${DEPLOY_PATH}/assets/php/storage/rate-limit"
CONFIG_FILE="${DEPLOY_PATH}/assets/php/contact.config.php"

mkdir -p "${PHP_STORAGE}"
chmod 775 "${PHP_STORAGE}" 2>/dev/null || chmod 755 "${PHP_STORAGE}"

if id www >/dev/null 2>&1; then
  chown -R www:www "${DEPLOY_PATH}/assets/php/storage" 2>/dev/null || true
fi

if [ ! -f "${CONFIG_FILE}" ]; then
  echo "::warning::${CONFIG_FILE} missing — upload contact.config.php on the server for the contact form to send email."
fi

echo "aaPanel post-deploy finished for ${DEPLOY_PATH}"
