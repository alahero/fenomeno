# Sitio público estático (Fenómeno)

HTML listo para producción: landing (`index.html`), contacto y páginas legales, con **`assets/`** en la misma carpeta. No incluye el nombre ni la estructura de “prototipo”; es el directorio que debes publicar.

## Despliegue (p. ej. Vercel)

En el proyecto de Vercel, configura **Root Directory** como `site` (raíz del repo = carpeta del repositorio; el “root” del deploy = esta carpeta). Así la URL sirve `/` → `index.html` sin prefijos tipo `Stitch Prototype/`.

Vista local desde aquí:

```bash
python -m http.server 8765
```

Abre `http://127.0.0.1:8765/`.

## Origen del contenido

Las páginas legales se pueden regenerar desde [`Stitch Prototype/_build_legal_pages.py`](../Stitch%20Prototype/_build_legal_pages.py) (fuentes parciales en esa carpeta). `contacto.html` se mantiene editado a mano salvo que decidas volver a integrarlo al script.
