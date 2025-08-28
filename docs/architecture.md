# Architectuur – Wonderwoman

Hoofdonderdelen
- Core Engine: agent lifecycle, state, scheduler.
- Adapters:
  - IO: files, network, message bus.
  - Compute: CPU/GPU, RTX (optioneel in toekomst).
- Ops:
  - CI/CD via GitHub Actions
  - Backups (S3/Azure/GC Storage) via workflow + scripts
  - Audit logs (GitHub run logs + artefacts)

Security
- RBAC: Chief (superuser), Maintainers (beperkt), Runners (uitvoer).
- Secrets via GitHub Actions Secrets en repo/organizational policies.