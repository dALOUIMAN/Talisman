# Wonderwoman (ASUS2)

Doel:
- Next-gen AI/agents framework (future-ready) met optionele RTX/Omniverse integraties.
- Modulair agent-beheer (lifecycle, events, messaging).
- Sterke security met rol "Chief" (superuser) = @dALOUIMAN.
- Cloud back-ups en audit logging.

ASUS2 Target (Local):
- Primair bedoeld om lokaal te draaien op jouw ASUS-2 Windows machine.
- PowerShell-scripts meegeleverd voor snelle setup, backup en (optionele) browser start.

Snel starten (Windows/PowerShell):
1. Open PowerShell als Admin in de repo-root.
2. `./scripts/deploy.ps1 -Environment dev`
3. `./scripts/backup.ps1 -DryRun` om de backup-stroom te testen.
4. `./scripts/open-dashboard.ps1` (optioneel) om een lokale dashboard-URL te openen zodra beschikbaar.

Beveiliging:
- Chief = @dALOUIMAN (volledige rechten).
- Policies zie SECURITY.md.
- Secrets via GitHub Secrets (nooit in code).

Ops:
- CI draait lint/build placeholders.
- Nightly backup workflow draait alleen als benodigde secrets gezet zijn.