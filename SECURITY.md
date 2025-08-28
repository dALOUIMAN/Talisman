# Security Policy

Roles
- Chief (Superuser): @dALOUIMAN – volledige rechten.
- Maintainers: write/review, geen secret-rotaties.
- Runners: uitvoeren van workflows, geen secret toegang.

Practices
- Geen secrets in code. Gebruik GitHub Secrets/Environments.
- Minimaal benodigde rechten voor workflows (GITHUB_TOKEN: permissions minimaal).
- Review vereist voor PR naar main. Chief kan nood-override.