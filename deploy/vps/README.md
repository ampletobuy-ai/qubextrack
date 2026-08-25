# VPS marketing site (static HTML behind Traefik)

| Item | Path / note |
|------|-------------|
| Compose + nginx | Copy to `/opt/marketing-site/` |
| Public HTML | `/opt/marketing-site/public/` (CI/CD syncs here) |
| Optional helper | `/opt/marketing-site/scripts/deploy.sh` |

**CI/CD:** [CICD_SETUP_GUIDE.md](../../doc/CICD_SETUP_GUIDE.md)

One-time install on the VPS:

```bash
sudo mkdir -p /opt/marketing-site/public /opt/marketing-site/scripts
sudo cp deploy/vps/docker-compose.yml deploy/vps/nginx.conf /opt/marketing-site/
sudo cp scripts/deploy.sh /opt/marketing-site/scripts/
sudo chmod +x /opt/marketing-site/scripts/deploy.sh
sudo chown -R deploy:deploy /opt/marketing-site
cd /opt/marketing-site && docker compose up -d
```

Adjust Traefik `Host(...)` labels in `docker-compose.yml` for staging (e.g. `ampletobuy.com`) vs production (`qubextrack.com`).
