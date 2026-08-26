# QubexTrack marketing site — CI/CD Setup Guide

Same branch model as **retail-pos**: `features` for staging, `main` for production. This repo is static HTML (no GHCR images).

**Related VPS layout:** [deploy/vps/README.md](../deploy/vps/README.md)

---

## What you get

```text
Push to features
       │
       ▼
┌─────────────────────────────┐
│  CI (ci.yml)                │  HTML / file checks
└─────────────┬───────────────┘
              │ success + commit has deploy marker
              ▼
┌─────────────────────────────┐
│  Deploy Features            │  SSH → staging VPS → /opt/marketing-site/public
└─────────────────────────────┘

Merge to main → Actions → Deploy Production (manual)
              ▼
┌─────────────────────────────┐
│  Deploy Production          │  SSH → production VPS → /www/wwwroot/qubextrack.com
└─────────────────────────────┘
```

| Piece | File | When it runs |
|-------|------|----------------|
| Checks | `.github/workflows/ci.yml` | Push / PR to `features` |
| Staging deploy | `.github/workflows/deploy.yml` | After CI on `features` **with deploy marker**, or manual |
| Production deploy | `.github/workflows/deploy-production.yml` | Manual only from `main` |
| Server helper | `scripts/deploy.sh` | Optional on VPS after sync |

### Deploy markers (same as retail-pos)

Include one of these in the **commit message** (features branch) to auto-deploy staging:

- ` - deploy`
- `[deploy]`
- `#deploy`

Example: `Update pricing page - deploy`

Without a marker, CI still runs; deploy is skipped.

---

## Prerequisites

- [ ] Repo: `ampletobuy-ai/qubextrack`
- [ ] Branches: `features`, `main`
- [ ] Production: aaPanel site at `/www/wwwroot/qubextrack.com` with PHP 8.2
- [ ] Staging (optional): Docker `/opt/marketing-site` with `docker-compose.yml`, `nginx.conf`, `public/`
- [ ] SSH access as `root` or `deploy` (must be able to write the web root)

---

## Phase 1 — One-time VPS layout

```bash
sudo mkdir -p /opt/marketing-site/public /opt/marketing-site/scripts
# From a machine with this repo:
scp deploy/vps/docker-compose.yml deploy/vps/nginx.conf deploy@VPS_IP:/opt/marketing-site/
scp scripts/deploy.sh deploy@VPS_IP:/opt/marketing-site/scripts/
ssh deploy@VPS_IP 'chmod +x /opt/marketing-site/scripts/deploy.sh && cd /opt/marketing-site && docker compose up -d'
```

Staging VPS: set Traefik hosts to `ampletobuy.com` / `www.ampletobuy.com`.  
Production VPS: keep `qubextrack.com` / `www.qubextrack.com` (defaults in repo compose).

---

## Phase 2 — GitHub Environments & secrets

Create Environments: **`features`** and **`production`**.

For each environment, set:

| Name | Type | Value |
|------|------|--------|
| `VPS_HOST` | secret or var | VPS IPv4 |
| `VPS_USER` | secret or var | `deploy` |
| `VPS_SSH_KEY` | secret | private key for GitHub Actions |
| `DEPLOY_PATH` | optional | staging `/opt/marketing-site/public` · prod `/www/wwwroot/qubextrack.com` (aaPanel) |
| `DEPLOY_HEALTHCHECK_URL` | optional | staging `https://ampletobuy.com/` · prod `https://qubextrack.com/` |

You can reuse the same SSH key pattern as retail-pos (`github-actions-…-deploy`), or a dedicated key limited to `/opt/marketing-site`.

Recommended:

- Environment `features` → deployment branches: `features`
- Environment `production` → deployment branches: `main` (+ optional required reviewers)

---

## Phase 3 — Day-to-day usage

### Staging (features)

```bash
git checkout features
# … edit site …
git commit -m "Copy tweak - deploy"
git push origin features
```

CI runs → Deploy Features runs automatically when the marker is present.

Manual: **Actions → Deploy Features → Run workflow** (branch `features`).

### Production (main)

```bash
git checkout main
git merge features
git push origin main
```

Then **Actions → Deploy Production → Run workflow** (branch `main`). No auto-deploy on production.

---

## Troubleshooting

| Symptom | Check |
|---------|--------|
| Deploy skipped | Commit message missing ` - deploy` / `[deploy]` / `#deploy` |
| `VPS_HOST is empty` | Environment secrets on `features` / `production` (not only repo-level) |
| Site not updating | Confirm sync target is `/opt/marketing-site/public` and Traefik points at `marketing-nginx` |
| 502 / no TLS | Traefik + `edge` network; compose labels Host rule matches DNS |

---

## Difference from retail-pos

| | retail-pos | qubextrack (this repo) |
|--|------------|-------------------------|
| Artifact | GHCR Docker images | Tar of static HTML/assets |
| Auto chain | CI → Docker → Deploy | CI → Deploy |
| Production | Manual Deploy Production | Manual Deploy Production |
| Deploy marker | Same | Same |
| Environments | `features` / `production` | `features` / `production` |
