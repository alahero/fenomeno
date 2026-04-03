# Fenomeno Agent Context

Repositorio en **fase diseño y especificación**: marca, skills de agente, activos en `brand-sources/`, diseño canónico en **Stitch** (MCP). La **implementación web** no vive en la raíz hasta un milestone explícito.

## Fase actual

- **Diseño UI:** [Stitch — proyecto Fenómeno](https://stitch.withgoogle.com/projects/1368868296218482267). Detalles operativos en [`docs/stitch.md`](docs/stitch.md).
- **Sitio estático desplegable (hasta milestone `web/`):** entrada [`Stitch Prototype/index.html`](Stitch Prototype/README.md) más páginas legales y contacto en la misma carpeta. Es HTML estático listo para hosting (p. ej. Vercel con directorio raíz `Stitch Prototype`); el milestone de implementación en [`web/`](web/README.md) sustituirá esto cuando se active.
- **Marca y copy:** [`@.agent/skills/fenomeno-brand-guidelines/SKILL.md`](.agent/skills/fenomeno-brand-guidelines/SKILL.md) y [`references/fenomeno-brand-foundation.md`](.agent/skills/fenomeno-brand-guidelines/references/fenomeno-brand-foundation.md).
- **Activos:** [`brand-sources/README.md`](brand-sources/README.md) (brandbook PNG/PDF, referencias sociales).
- **Especificaciones:** [`openspec/specs/README.md`](openspec/specs/README.md) y propuestas futuras en `openspec/changes/` cuando apliquen.

## Stack web (futuro, no activo en raíz)

Cuando se abra el milestone de implementación:

- **Previsto:** sitio estático con Vite + React + Tailwind (patrones en [`@.agent/rules/web-implementation.md`](.agent/rules/web-implementation.md)).
- **Ubicación:** carpeta [`web/`](web/README.md) (scaffold pendiente).

No asumir que `npm run dev` existe en la raíz de este repo en la fase actual.

## MCP y Cursor

- Stitch: `@_davideast/stitch-mcp` vía [`.cursor/mcp.json`](.cursor/mcp.json); credenciales en `.env` (ver [`.env.example`](.env.example)).
- **Skill UI/UX:** [`.cursor/skills/ui-ux-pro-max/SKILL.md`](.cursor/skills/ui-ux-pro-max/SKILL.md) se **mantiene en el repo** para reproducibilidad del entorno. Si necesitas un clon más liviano, puedes eliminar esa carpeta e instalar el skill desde otra fuente; actualiza entonces esta nota.

## Security Boundaries

- Never modify or create files in `/secrets`, `/credentials`, or any environment key store.
- Never commit API keys, tokens, passwords, or raw private exports.
- Redact personal data before moving social media exports into reusable references.

## Operating Rules

- Keep root instructions lean and delegate details through targeted modules.
- Follow `@.agent/rules/web-implementation.md` **solo cuando** haya código web en curso en el repo.
- Trigger `@.agent/skills/brand-guidelines-creator/SKILL.md` when brand analysis or guideline synthesis is requested.
- Trigger `@.agent/skills/fenomeno-brand-guidelines/SKILL.md` when implementing Fenomeno-specific copy, sections, or UI decisions (Stitch o web).
- Trigger `@.agent/skills/gdpr-website-compliance/SKILL.md` when auditing or implementing privacy, cookies, forms, third-party integrations, or international data flows for web (RGPD/GDPR + ePrivacy). Full guide (portable): [`.agent/skills/gdpr-website-compliance/references/gdpr-website-compliance.md`](.agent/skills/gdpr-website-compliance/references/gdpr-website-compliance.md). [`docs/gdpr-website-compliance.md`](docs/gdpr-website-compliance.md) is a short pointer to that path.
- For UI/UX system recommendations, use `@.cursor/skills/ui-ux-pro-max/SKILL.md`.
- Keep future brand-specific skill content focused and source-backed.
