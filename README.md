# Fenómeno — marca, agentes y sitio estático

Repositorio con **marca**, **skills para agentes**, **diseño en Stitch** y **sitio web estático** servible desde la raíz (`index.html`, `assets/`, contacto y legales).

## Qué hay

- **[`AGENTS.md`](AGENTS.md)** — contexto para asistentes y límites del proyecto.
- **Sitio público (raíz):** `index.html`, `assets/`, `contacto.html`, páginas legales. Despliegue: raíz del repo en Vercel u otro host estático. Local: `python -m http.server` en la raíz o `serve.cmd`.
- **[`brand-sources/`](brand-sources/)** — brandbook PNG/PDF y referencias de redes.
- **[`docs/stitch.md`](docs/stitch.md)** — proyecto Stitch, MCP e IDs de pantalla.
- **[`scripts/stitch-legal/`](scripts/stitch-legal/README.md)** — fuentes y script para regenerar avisos legales en la raíz.
- **[`.agent/`](.agent/)** — skills y reglas (Fenómeno, RGPD, implementación opcional).
- **[`.cursor/mcp.json`](.cursor/mcp.json)** — servidor MCP de Stitch.
- **[`openspec/`](openspec/)** — especificaciones (OpenSpec).
- **[`web/README.md`](web/README.md)** — carpeta opcional si algún día hubiera bundler/framework (hoy no se usa).

## Limpieza local (posibles restos)

Si ves **`node_modules/`** o **`dist/`** en la raíz, son restos viejos; puedes borrarlos.

## Enlaces

- Stitch: [proyecto 1368868296218482267](https://stitch.withgoogle.com/projects/1368868296218482267)
