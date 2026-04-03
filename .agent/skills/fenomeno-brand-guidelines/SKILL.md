---
name: fenomeno-brand-guidelines
description: Use when implementing Fenomeno (bar Hi-Fi, Madrid) site sections, copy in Spanish, layout, design tokens, or UI decisions. Enforces the brandbook distilled in fenomeno-brand-foundation.md; typography licenses are handled separately by the team.
---

# Guía rápida — Fenomeno

## Fuente de verdad

1. Leer y seguir **[`references/fenomeno-brand-foundation.md`](references/fenomeno-brand-foundation.md)** — inventario de placas en `brand-sources/brandbook-png/`, HEX de acento, tipografía citada, frases (placa 18) y voz (placa 19).
2. Implementación web actual: **HTML estático en la raíz del repo** (`index.html`, Tailwind CDN, mismos tokens que Stitch). Si en el futuro hubiera bundler o framework, alinear con [`@.agent/rules/web-implementation.md`](../../rules/web-implementation.md).
3. **Coming Soon** (`brand-sources/brandbook-png/Fenomento_ComingSoon_Website.png`) y **`brand-sources/social-reference/`** son referencia visual y ambiente; **si hay conflicto con el brandbook (placas 01–43), mandan el brandbook y la foundation**, no una captura suelta ni un mood de red social aislado.

## Checklist de implementación

### Color

- Acentos canónicos: **`#E63912`** (rojo), **`#F5C412`** (amarillo), **`#1266AB`** (azul). Detalle en la tabla de la foundation.
- Modo habitual en web: **fondo muy oscuro** (`#131012`, alineado a Stitch), **texto crema** (`#e2dcc6` y derivados para jerarquía), **bordes hairline** (`#3a322f`). Los neutros exactos pueden afinarse cuando el manual fije HEX adicionales.
- **Jerarquía de acento:** un bloque = **un acento dominante** (rojo *o* amarillo *o* azul en primer plano). Evita empatar los tres en el mismo componente pequeño (botón, chip, badge).
- El rojo sostiene **impacto editorial** (titulares, énfasis); el amarillo **contraste y etiquetas**; el azul **bloques y contrapeso** frente al calor del rojo/amarillo.

### Tipografía

- Familias del manual: **Pitch**, **Urbane**, **Corporate A**, **Aston Script**. **Licencia y archivos web:** los gestiona el equipo; hasta entonces, la app usa **fallbacks** documentados en la foundation (p. ej. Bebas Neue / Cormorant Garamond / Inter).
- Cuando lleguen las fuentes oficiales, sustituir por pesos y roles que indiquen las **placas tipográficas del brandbook** (no asumir mapeos 1:1 sin revisar PNG).
- Display / marca: fuerte, **mayúsculas o muy contrastadas**, buen aire; cuerpo: **legible**, sin densidad de “folleto corporativo”. La voz es refinada, no gritona.

### Trazos, radios y layout

- Separación de secciones: bordes **`1px`** y bloques bien delimitados encajan con el manual tipo **club / cabina / escena**.
- **Radios:** CTAs tipo **pill** (`border-radius` completo), tarjetas y mocks **16–24px** (subir con `clamp` en desktop si el layout lo pide), contenedores principales coherentes entre sí (no mezclar “todo cuadrado” y “todo redondo” sin intención).
- Cabecera: puede ser **sticky** con fondo semitransparente y **backdrop blur** si se mantiene legibilidad sobre el hero.
- **Área de respeto del logotipo/isotipo:** según placa correspondiente en el export PNG; si no está numerada en foundation, revisar placas de logo en `brand-sources/brandbook-png/` antes de encajar en web.

### Tono y copy (TOV)

- **Español** para copy de marca (Madrid, público local y visitante). Tono: **cercano y refinado**, **cosmopolita**, con conocimiento **sin sobreexplicar** (placa 19).
- **Personalidad:** sofisticada y accesible, culta sin pretensiones, **obsesión sana por el detalle**.
- **Palabras puente:** sofisticado, detalle, carácter, ritmo, estilo, arte — usar con naturalidad, no como lista en cada párrafo.
- **Pool de líneas autorizadas** (placa 18): usar texto **tal cual** en hero, redes o piezas salvo brief explícito de adaptación; están en la foundation numeradas.
- CTAs: **invitar al descubrimiento** más que “vender a presión”; preferir verbos que sugieran **experiencia y escena** (noche, sonido, espacio) alineados al manual.

### Imagen y redes

- **`brand-sources/social-reference/`** aporta **ritmo, bocados, copas, vinilo, ambiente**; úsalo para coherencia de **atmósfera**, no para contradecir tipografía/color definidos en brandbook.
- Tratamiento visual (luz baja, calidez, detalle) debe **honrar** “el detalle suena más fuerte que el ruido” sin volverse kitsch.

### Qué evitar

- **Tres acentos fuertes** compitiendo en un mismo módulo pequeño.
- Copy genérico de bar (“la mejor fiesta”, “número uno”) que **apague** la voz culta y precisa del manual.
- **Sobrerrevelar** (explicar de más): contradice la voz de placa 19.
- Tratar **Coming Soon** o **una sola story de Instagram** como manual completo: siempre contrastar con **placas 01–43**.

## Si falta dato

- No inventar reglas que **contradigan** `fenomeno-brand-foundation.md` o las placas.
- Marcar en código, comentarios o tareas lo **pendiente** (p. ej. tokens neutros finales, mapeo exacto Pitch/Urbane por nivel tipográfico tras entrega de fuentes).
