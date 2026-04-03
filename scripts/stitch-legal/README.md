# scripts/stitch-legal — fuentes para páginas legales

Fragmentos HTML extraídos y scripts que **regeneran** `privacidad.html`, `faqs.html` y `terminos.html` en la **raíz del repositorio**. No forman parte del sitio servido al público; solo el taller de contenido legal.

- **`_build_legal_pages.py`** — ensambla las tres páginas legales en la raíz del repo (lee los `_extracted_*` y `_faq_sections.html` de esta carpeta). `contacto.html` no lo genera; edítalo a mano.
- **`_extract_mandala.py`**, **`_transform_faq.py`** — utilidades puntuales usadas al importar textos (rutas locales al autor; revisar antes de ejecutar).
- Captura de referencia de la landing en Stitch: [`../../docs/stitch/0aa97d51fa3041f4ba93bdb5b665fdde-fullpage-screenshot.png`](../../docs/stitch/0aa97d51fa3041f4ba93bdb5b665fdde-fullpage-screenshot.png).

Desde la raíz del repo:

```bash
python scripts/stitch-legal/_build_legal_pages.py
```
