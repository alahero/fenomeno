# Fenomeno Agent Context

Repositorio con **marca, skills de agente**, **sitio estático en la raíz** (`index.html`, `assets/`, legales, contacto), activos en `brand-sources/` y diseño canónico de pantallas en **Stitch** (MCP).

## Fase actual

- **Sitio público:** HTML estático en la **raíz del repo** (`index.html`, carpeta `assets/`, `contacto.html`, páginas legales). Despliegue directo (p. ej. Vercel con raíz = repositorio, sin subcarpeta). Vista local: `python -m http.server` en la raíz o doble clic en `serve.cmd`.
- **Diseño UI:** [Stitch — proyecto Fenómeno](https://stitch.withgoogle.com/projects/1368868296218482267). Detalles en [`docs/stitch.md`](docs/stitch.md).
- **Regenerar legales:** [`scripts/stitch-legal/_build_legal_pages.py`](scripts/stitch-legal/README.md) (fuentes en la misma carpeta).
- **Marca y copy:** [`@.agent/skills/fenomeno-brand-guidelines/SKILL.md`](.agent/skills/fenomeno-brand-guidelines/SKILL.md) y [`references/fenomeno-brand-foundation.md`](.agent/skills/fenomeno-brand-guidelines/references/fenomeno-brand-foundation.md).
- **Activos:** [`brand-sources/README.md`](brand-sources/README.md) (brandbook PNG/PDF, referencias sociales).
- **Especificaciones:** [`openspec/specs/README.md`](openspec/specs/README.md) y propuestas en `openspec/changes/` cuando apliquen.

## Stack web

**Decisión actual:** el producto web es **HTML + Tailwind CDN + JS mínimo** en la raíz; **no** hay aplicación React ni Vite en curso.

La carpeta [`web/`](web/README.md) queda solo como referencia opcional si algún día se migrara a un bundler o framework; no es requisito del proyecto.

## MCP y Cursor

- Stitch: `@_davideast/stitch-mcp` vía [`.cursor/mcp.json`](.cursor/mcp.json); credenciales en `.env` (ver [`.env.example`](.env.example)).
- **Skill UI/UX:** [`.cursor/skills/ui-ux-pro-max/SKILL.md`](.cursor/skills/ui-ux-pro-max/SKILL.md) se **mantiene en el repo** para reproducibilidad del entorno. Si necesitas un clon más liviano, puedes eliminar esa carpeta e instalar el skill desde otra fuente; actualiza entonces esta nota.

## Security Boundaries

- Never modify or create files in `/secrets`, `/credentials`, or any environment key store.
- Never commit API keys, tokens, passwords, or raw private exports.
- Redact personal data before moving social media exports into reusable references.

## Operating Rules

- Keep root instructions lean and delegate details through targeted modules.
- Follow `@.agent/rules/web-implementation.md` **solo cuando** haya código web en curso en el repo (p. ej. scaffold en `web/`).
- Trigger `@.agent/skills/brand-guidelines-creator/SKILL.md` when brand analysis or guideline synthesis is requested.
- Trigger `@.agent/skills/fenomeno-brand-guidelines/SKILL.md` when implementing Fenomeno-specific copy, sections, or UI decisions (Stitch o web).
- Trigger `@.agent/skills/gdpr-website-compliance/SKILL.md` when auditing or implementing privacy, cookies, forms, third-party integrations, or international data flows for web (RGPD/GDPR + ePrivacy). Full guide (portable): [`.agent/skills/gdpr-website-compliance/references/gdpr-website-compliance.md`](.agent/skills/gdpr-website-compliance/references/gdpr-website-compliance.md). [`docs/gdpr-website-compliance.md`](docs/gdpr-website-compliance.md) is a short pointer to that path.
- For UI/UX system recommendations, use `@.cursor/skills/ui-ux-pro-max/SKILL.md`.
- Keep future brand-specific skill content focused and source-backed.
