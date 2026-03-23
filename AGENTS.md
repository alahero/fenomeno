# Fenomeno Agent Context

Build a static website for Fenomeno, a bar in Madrid, using a brand-first workflow grounded in extracted source assets.

## Stack And Tooling
- Use static HTML, CSS, and JavaScript as the baseline stack until a framework is selected.
- Use `npm` as the package manager when Node-based tooling is added.
- Treat the current repository state as bootstrap mode (no detected app files yet).

## Run Commands
- Run local preview with `python -m http.server 4173`.
- Run temporary build placeholder with `powershell -Command "Write-Output 'No build step configured yet'"`.
- Run temporary test placeholder with `powershell -Command "Write-Output 'No automated tests configured yet'"`.

## Security Boundaries
- Never modify or create files in `/secrets`, `/credentials`, or any environment key store.
- Never commit API keys, tokens, passwords, or raw private exports.
- Redact personal data before moving social media exports into reusable references.

## Operating Rules
- Keep root instructions lean and delegate details through targeted modules.
- Follow `@.agent/rules/web-implementation.md` for implementation patterns.
- Trigger `@.agent/skills/brand-guidelines-creator/SKILL.md` when brand analysis or guideline synthesis is requested.
- Trigger `@.agent/skills/fenomeno-brand-guidelines/SKILL.md` when implementing Fenomeno-specific copy, sections, or UI decisions.
- Keep future brand-specific skill content focused and source-backed.
