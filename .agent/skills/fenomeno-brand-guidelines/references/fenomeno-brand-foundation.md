# Fenomeno — fundamento de marca (referencia operativa)

Documento vivo para implementación web. Las afirmaciones de color y cobertura de placas están **confirmadas por el equipo**; el resto deriva del brandbook exportado a PNG.

---

## 1. Inventario de fuentes (repo)

| Origen | Ruta / archivos | Notas |
|--------|-----------------|--------|
| Brandbook (export PNG) | `brand-sources/brandbook-png/Sin título-1-01.png` … `Sin título-1-43.png` | **Placas 01–43 = brandbook completo.** |
| Coming Soon (referencia visual) | `brand-sources/brandbook-png/Fenomento_ComingSoon_Website.png` | Nombre de archivo tal como en export (typo “Fenomento” en el asset). |
| PDF maestro (si aplica) | `brand-sources/brandbook-pdf/` | La **fecha del PDF original no define vigencia**; para trabajo diario manda la **exportación PNG reciente** (actualizada el **30 de marzo de 2026** en el flujo del proyecto). |
| Red social (capturas) | `brand-sources/social-reference/` | Complemento; no sustituye definiciones del brandbook. |

---

## 2. Paleta — acentos oficiales (HEX)

Valores confirmados para implementación (web, piezas digitales):

| Rol en marca | HEX | Uso orientativo |
|--------------|-----|-----------------|
| Rojo / acento principal | `#E63912` | Titulares fuertes, CTAs, énfasis gráfico. |
| Amarillo / acento secundario | `#F5C412` | Franjas, badges, contraste sobre oscuro. |
| Azul / acento frío | `#1266AB` | Bloques de color, contrapeso al rojo/amarillo. |

Neutros (crema, carbón, bordes) se derivan de las placas del brandbook y de tokens usados en Stitch / futura implementación web hasta que el brandbook fije HEX adicionales.

---

## 3. Tipografía (pendiente de activos)

Familias citadas en brandbook: **Pitch**, **Urbane**, **Corporate A**, **Aston Script**.

- **Estado:** sin archivos web ni licencias en repo todavía; el equipo las incorporará después.
- **Hasta entonces:** usar stack con fallback (p. ej. Bebas Neue / Cormorant / Inter en implementación web) y alinear cuando existan `@font-face` o proveedor autorizado.
- **Stitch (diseño canónico UI):** en el export web del proyecto se usan **Epilogue** (titulares), **Work Sans** (cuerpo) y **Newsreader** (étiquetas/itálicas) como interinos coherentes con el tema Stitch; sustituir por Pitch/Urbane/Corporate A/Aston Script cuando el equipo publique activos y mapeo por placa.

---

## 4. Frases — placa 18 (texto de marca)

Usar como **pool autorizado** de líneas (hero, redes, piezas). Mantener redacción exacta salvo brief explícito de adaptación.

1. La aguja cae. El mundo se detiene.
2. El detalle suena más fuerte que el ruido.
3. Un vaso en la mano, un vinilo girando.
4. Aquí, la banda sonora es el guión de la noche.
5. En la escena domina el detalle, el resto lo pone la música.
6. La noche se dirige sola: iluminación justa, la mezcla musical impecable y una atmósfera que te llama de vuelta.
7. La música protagoniza una historia de la que eres parte.
8. Hay escenas que se disfrutan en cámara lenta.

---

## 5. Personalidad, palabras clave y voz — placa 19

### Personalidad

- Sofisticada pero accesible.
- Culta sin ser pretenciosa.
- Apasionada por el detalle.

### Palabras clave

Sofisticado, detalle, carácter, ritmo, estilo y arte.

### Voz

Cercana y refinada, con un aire cosmopolita. Habla con conocimiento, sin caer en la sobreexplicación. Despierta curiosidad e invita al descubrimiento.

---

## 6. Implicaciones para UI web

- Priorizar **legibilidad** y **ritmo editorial** alineados a la voz (p. ej. titulares contundentes + cuerpo claro).
- Acentos de color: rotar **rojo / amarillo / azul** con criterio de jerarquía, no mezclar los tres al mismo nivel en un solo componente pequeño.
- Cualquier nueva sección debe poder justificarse con al menos un ancla del brandbook (placa o Coming Soon).

---

## 7. Preguntas abiertas (actualizar cuando haya datos)

- HEX finos de fondos y textos secundarios si el PDF/placas los documentan con muestra.
- Reglas exactas de pesos Pitch/Urbane por jerarquía tipográfica una vez cargadas las fuentes.
