# Stitch Prototype — export local

Origen: API Stitch (MCP `get_screen`), descargado con `curl -L` el **2026-04-01**.

| Campo | Valor |
|--------|--------|
| Proyecto | Landing Page - Fenómeno (Madrid) |
| `projectId` | `1368868296218482267` |
| Pantalla | Landing Page - Fenómeno (Sin Reproductor) |
| `screenId` | `0aa97d51fa3041f4ba93bdb5b665fdde` |

## Archivos

- `0aa97d51fa3041f4ba93bdb5b665fdde.html` — HTML exportado (baseline Stitch); las etiquetas `<img>` apuntan a **`assets/img-01.jpg` … `img-06.jpg`** (rutas relativas para uso local).
- `0aa97d51fa3041f4ba93bdb5b665fdde-brand-aligned.html` — **variante comparación**: misma base + meta/OG, saltar al contenido, `focus-visible`, anclas de navegación, formulario con `label`/`autocomplete`, líneas de placa 18 en manifiesto y pie, CTAs más cercanos al tono marca, contraste de texto un poco más alto, © 2026; **franja de cinco colores del hero intacta**; **azul limitado** (solo en esa franja + tokens Tailwind internos; tarjeta 03 y pie sin acento azul decorativo).
- `0aa97d51fa3041f4ba93bdb5b665fdde-fullpage-screenshot.png` — captura completa de la pantalla en Stitch (PNG).
- `assets/` — imágenes embebidas de `lh3.googleusercontent.com` descargadas con `curl -L`.

**Comparar en local** (desde esta carpeta, p. ej. `python -m http.server 8765`):

- Original: `http://127.0.0.1:8765/0aa97d51fa3041f4ba93bdb5b665fdde.html`
- Revisión marca: `http://127.0.0.1:8765/0aa97d51fa3041f4ba93bdb5b665fdde-brand-aligned.html`

El HTML sigue cargando **Tailwind CDN**, **Google Fonts** y **Material Symbols** desde la red; sin conexión solo fallará ese bloque.
