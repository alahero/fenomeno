# Stitch — proyecto Fenómeno

Diseño UI en [Stitch](https://stitch.withgoogle.com/) es la **fuente canónica** de pantallas mientras el repo esté en fase diseño (sin sitio implementado).

## Proyecto

- **URL:** [stitch.withgoogle.com/projects/1368868296218482267](https://stitch.withgoogle.com/projects/1368868296218482267)
- **ID:** `1368868296218482267`

## MCP en Cursor

- Configuración: [`.cursor/mcp.json`](../.cursor/mcp.json) — servidor `stitch` con `@_davideast/stitch-mcp proxy` y `STITCH_USE_SYSTEM_GCLOUD=1`.
- Variables locales: `.env` en la raíz (no commitear). Plantilla: [`.env.example`](../.env.example).
- Autenticación: `npx @_davideast/stitch-mcp init` o `gcloud auth application-default login` (ver `.env.example`).

## Pantallas de referencia (ejemplos)

Los IDs cambian cuando generas variantes; conviene anotar aquí los que uses como “verdad” operativa:

| Uso | `node-id` (fragmento URL) | Notas |
|-----|---------------------------|--------|
| Landing export → sitio estático repo | `0aa97d51fa3041f4ba93bdb5b665fdde` | HTML oficial en repo: [`Stitch Prototype/index.html`](../Stitch%20Prototype/README.md) |
| Landing base (histórica) | `52077d5064c74f45b680f497c2735df8` | Primera landing principal |
| Variante copy + bar abierto | `aa3b6e5eb94246309ea414a3c1e02548` | Referencia de contenido |
| Sin patrón de fondo | `51e4e33ecdf74cf090038cc128ca63bb` | Refinamiento visual |

Actualiza esta tabla cuando fijes entregables nuevos.

## API desde el agente

Herramientas útiles: `list_projects`, `get_project`, `list_screens`, `get_screen`, `generate_variants`. Los favoritos en Stitch aparecen como `isFavourite` en `screenInstances` de `get_project`.
