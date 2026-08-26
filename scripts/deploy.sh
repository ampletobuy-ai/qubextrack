#!/usr/bin/env bash
# Server-side helper for the qubextrack marketing site.
# Install on VPS as /opt/marketing-site/scripts/deploy.sh (optional).

set -euo pipefail

ROOT="${MARKETING_ROOT:-/opt/marketing-site}"
cd "$ROOT"

if [ -f docker-compose.yml ]; then
  echo "==> Ensuring marketing nginx + PHP-FPM are running..."
  docker compose up -d --build
  docker compose ps
else
  echo "No docker-compose.yml in ${ROOT} — files sync only."
fi

echo "Marketing site deploy helper finished."
