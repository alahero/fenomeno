# Stitch Prototype — sitio estático oficial (pre-`web/`)

Origen: API Stitch (MCP `get_screen`), descargado con `curl -L` el **2026-04-01**. La **entrada desplegable** (p. ej. Vercel con raíz en esta carpeta) es **`index.html`**. El diseño canónico de pantallas sigue en [Stitch](https://stitch.withgoogle.com/projects/1368868296218482267); ver [`docs/stitch.md`](../docs/stitch.md) y [`AGENTS.md`](../AGENTS.md).

| Campo | Valor |
|--------|--------|
| Proyecto | Landing Page - Fenómeno (Madrid) |
| `projectId` | `1368868296218482267` |
| Pantalla de referencia | Landing Page - Fenómeno (Sin Reproductor) |
| `screenId` (export histórico) | `0aa97d51fa3041f4ba93bdb5b665fdde` |

## Archivos

- **`index.html`** — landing oficial: meta/OG, saltar al contenido, `focus-visible`, anclas (`#inicio`, `#manifiesto`, `#curaduria`), CTAs marca, © 2026; imágenes en **`assets/img-01.jpg` … `img-06.jpg`** (rutas relativas).
- `contacto.html`, `privacidad.html`, `faqs.html`, `terminos.html`, `cumplimiento-rgpd.html` — páginas enlazadas desde el pie y la navegación.
- `0aa97d51fa3041f4ba93bdb5b665fdde-fullpage-screenshot.png` — captura completa de la pantalla en Stitch (PNG).
- `assets/` — imágenes embebidas de `lh3.googleusercontent.com` descargadas con `curl -L`.
- `_build_legal_pages.py` — ensambla páginas legales; la plantilla de navegación apunta a `index.html`.

**Vista local** (desde esta carpeta, p. ej. `python -m http.server 8765`):

- Inicio: `http://127.0.0.1:8765/` o `http://127.0.0.1:8765/index.html`

El HTML carga **Tailwind CDN**, **Google Fonts** y **Material Symbols** desde la red; sin conexión solo fallará ese bloque.
