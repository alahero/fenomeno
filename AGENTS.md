# Fenomeno Agent Context

Build a static website for Fenomeno, a bar in Madrid, using a brand-first workflow grounded in extracted source assets.

## Stack And Tooling

- **Primary:** Vite + React + Tailwind CSS (`src/App.jsx`, `npm run dev` / `npm run build`).
- **Legacy (sin build):** HTML/CSS en [`legacy/index.html`](legacy/index.html) y [`legacy/styles.css`](legacy/styles.css).
- Package manager: `npm`.

## Run Commands

- Run dev server: `npm run dev`
- Run production build: `npm run build`
- Preview build: `npm run preview`
- Legacy static preview (sin Node): `python -m http.server 4173` desde la carpeta `legacy/` (o sirve `legacy/` como raíz).

## Security Boundaries

- Never modify or create files in `/secrets`, `/credentials`, or any environment key store.
- Never commit API keys, tokens, passwords, or raw private exports.
- Redact personal data before moving social media exports into reusable references.

## Operating Rules

- Keep root instructions lean and delegate details through targeted modules.
- Follow `@.agent/rules/web-implementation.md` for implementation patterns.
- Trigger `@.agent/skills/brand-guidelines-creator/SKILL.md` when brand analysis or guideline synthesis is requested.
- Trigger `@.agent/skills/fenomeno-brand-guidelines/SKILL.md` when implementing Fenomeno-specific copy, sections, or UI decisions.
- For UI/UX system recommendations, use `@.cursor/skills/ui-ux-pro-max/SKILL.md`.
- Keep future brand-specific skill content focused and source-backed.
