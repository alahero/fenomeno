---
name: gdpr-website-compliance
description: >-
  Use when auditing or implementing RGPD/GDPR alignment for websites—privacy notices,
  cookie banners and consent, forms and newsletters, SaaS processors, international
  transfers, security/minimization, records of processing (Art. 30), and DPIA/DPO
  triggers. Pairs ePrivacy (cookies/device storage) with GDPR lawful basis and consent.
  Not legal advice; Spanish (Mexico) for project outputs unless the user requests otherwise.
---

# Skill — Cumplimiento RGPD para sitios web

## Fuente de verdad

1. **Leer primero** la guía completa (tablas, checklist, URLs oficiales): [`references/gdpr-website-compliance.md`](references/gdpr-website-compliance.md). Vive **en esta carpeta** para que puedas copiar todo el directorio `gdpr-website-compliance/` ( `SKILL.md` + `references/` ) a cualquier otro repositorio sin depender de `docs/`.
2. En otros proyectos, coloca el skill bajo la ruta que uses para skills (p. ej. `.agent/skills/gdpr-website-compliance/` o `.cursor/skills/gdpr-website-compliance/`) y conserva la misma estructura de archivos.

## Cuándo invocar este skill

- Nuevo sitio, landing, app web o **cambio** en formularios, registro, pagos o marketing por correo.
- **Cookies**, píxeles, analítica, embeds (mapas, vídeo, redes), chat, CDNs o cualquier script de terceros.
- Redacción o revisión de **política de privacidad**, **política de cookies** o textos en UI (banners, pies legales).
- **Auditoría rápida** pre-lanzamiento o antes de publicar integraciones nuevas (CRM, email, hosting con acceso a datos).

## Reglas operativas (no negociables en la práctica)

| Área | Qué exigir |
|------|------------|
| Base legal | Cada finalidad con **al menos una** base del Art. 6; **documentada antes** de tratar. |
| Consentimiento | Libre, específico, informado, unívoco; **sin** pre-tick en fines no esenciales; retirada tan fácil como el alta. |
| Cookies / dispositivo | Cumplimiento **dual** ePrivacy + RGPD; solo “estrictamente necesarias” sin opt-in donde la ley lo permita; **rechazar = misma prominencia** que aceptar en el primer nivel del banner (línea EDPB / supervisores). |
| Transparencia | Arts. 13–14: responsable, fines, base, conservación, destinatarios, transferencias, derechos, reclamación. |
| Terceros | Art. 28 (DPA) para encargados; aclarar co-responsabilidad (Art. 26) si aplica. |
| Transferencias | Arts. 44–49: adecuación, DPF para participantes elegibles, SCC + análisis cuando toque. |
| Seguridad | Arts. 25 y 32: HTTPS, minimización, retención acotada, validación en servidor. |

## Flujo de trabajo para el agente

### 1. Inventario

- Enumerar: formularios, auth, newsletters, logs, cookies, `localStorage`, scripts third-party, iframes, analítica, pagos.
- Por cada flujo: **qué dato personal**, **finalidad**, **base legal**, **conservación**, **quién accede** (incl. subencargados), **país** del tratamiento.

### 2. Diseño / copy

- Avisos en **capas**: resumen en el punto de recogida + enlace a política completa.
- Banners: primer nivel con **Aceptar** y **Rechazar todo** visibles y equivalentes; centro de preferencias **granular** por finalidad.

### 3. Implementación técnica

- **Carga diferida** de scripts no esenciales hasta consentimiento (o modo sin cookies según diseño).
- No enviar datos personales a terceros antes del opt-in cuando corresponda.
- Canal documentado para **derechos** (Arts. 15–22) y plazo orientativo de un mes.

### 4. Entrega

- Checklist de la sección 12 del documento de referencia; marcar pendientes explícitos (p. ej. DPO, DPIA, texto legal final).
- Recordar en la salida al usuario: **no es asesoría legal**; validar con abogado y autoridad competente según jurisdicción.

## Convenciones de idioma (repo Fenomeno)

- Comentarios en código y mensajes de commit: **español de México**, según reglas del proyecto.
- Políticas legales pueden ir en el idioma del mercado objetivo; la guía de referencia está en español.

## Coordinación con otras reglas

- Con implementación web en este repo: alinear con [`@.agent/rules/web-implementation.md`](../../rules/web-implementation.md) para estructura del código; este skill gobierna **privacidad y tratamiento de datos**, no el stack en sí.

## Referencias rápidas (profundizar en el MD completo)

- Texto RGPD (EUR-Lex), Arts. 13–14, 28, 30, 35, 44–49.
- EDPB: Guías 05/2020 sobre consentimiento.
- ICO: bases legales, consentimiento, cookies y avisos.
- ePrivacy: Directiva 2002/58/CE; Comisión UE: transferencias UE–EE. UU. / DPF.

Todas las URLs están listadas al final de [`references/gdpr-website-compliance.md`](references/gdpr-website-compliance.md).
