# Cumplimiento RGPD (GDPR) para sitios web — hallazgos y guía operativa

*Referencia portable del skill `gdpr-website-compliance`: mantener este archivo en `references/` junto a `SKILL.md` al copiar el skill a otro repositorio.*

Documento de síntesis para equipos de producto, diseño y desarrollo. **No constituye asesoría legal.** La aplicación del Reglamento depende del caso concreto (ubicación del responsable, usuarios, sector y tipo de datos).

---

## 1. Resumen ejecutivo

El **Reglamento (UE) 2016/679 (RGPD / GDPR)** regula el tratamiento de **datos personales** de personas físicas en el Espacio Económico Europeo (EEE), con principios de licitud, lealtad, transparencia, limitación de la finalidad, minimización, exactitud, limitación del plazo de conservación, integridad y confidencialidad, y responsabilidad proactiva (*accountability*).

En sitios web, el RGPD impacta de forma habitual en:

- Formularios, cuentas de usuario, newsletters y cualquier recogida voluntaria de datos.
- **Cookies, almacenamiento local y tecnologías similares** que acceden al dispositivo del usuario o procesan datos personales en ese contexto.

Para cookies y señalización en el dispositivo, además del RGPD suele aplicarse la **Directiva 2002/58/CE (ePrivacy)**, transuesta en cada Estado miembro: en la práctica se habla de cumplimiento **dual** (ePrivacy para *cuándo* se exige consentimiento u otra base; RGPD para *cómo* debe ser un consentimiento válido cuando esa es la base legal).

```mermaid
flowchart LR
  visitor[Visitante]
  site[SitioWeb]
  third[SaaSTerceros]
  visitor -->|datos_y_cookies| site
  site -->|encargos_y_transferencias| third
```

---

## 2. Ámbito y conceptos clave

| Concepto | Idea práctica en web |
|----------|----------------------|
| **Responsable del tratamiento** | Quien decide **por qué** y **cómo** se usan los datos (p. ej. la empresa titular del sitio). Debe identificarse claramente en la política de privacidad y en los puntos de recogida. |
| **Encargado del tratamiento** | Trata datos **por cuenta del responsable** (p. ej. proveedor de email transaccional, hosting con acceso a datos). Requiere contrato tipo Art. 28 RGPD. |
| **Tratamiento** | Operaciones como recogida, registro, organización, conservación, consulta, comunicación, supresión, etc. |
| **Dato personal** | Cualquier información sobre una persona identificada o identificable (nombre, email, IP en muchos contextos, IDs en cookies, etc.). |
| **Interesado** | La persona física a la que corresponden los datos. |

**Sitio “solo informativo”** frente a **sitio con interacción**: aun sin formularios, pueden existir tratamientos (logs del servidor, cookies analíticas o de terceros, CDNs, reproductores embebidos). La minimización y la transparencia siguen siendo relevantes.

---

## 3. Bases legales (Art. 6 RGPD)

Todo tratamiento necesita **al menos una** base legal del Art. 6. Las seis bases son: **consentimiento**, **ejecución de contrato**, **obligación legal**, **intereses vitales**, **misión de interés público** e **interés legítimo** (*legitimate interest*).

### Enfoque práctico en web

| Escenario típico | Bases que suelen evaluarse | Notas |
|------------------|----------------------------|--------|
| Formulario de contacto para responder una solicitud | Contrato medidas precontractuales (Art. 6(1)(b)) o interés legítimo (Art. 6(1)(f)) | Depende del contenido del mensaje y de la relación; documentar la elección. |
| Newsletter / marketing por correo | Consentimiento (Art. 6(1)(a)) u otra base según derecho local de comunicaciones electrónicas | En muchos casos el marketing requiere consentimiento explícito o base específica sectorial. |
| Facturación, obligaciones fiscales | Obligación legal (Art. 6(1)(c)) | Conservación según plazos legales. |
| Cookies no esenciales / publicidad comportamental | Consentimiento (Art. 6(1)(a)) + ePrivacy | No usar “contrato” o “interés legítimo” como sustituto arbitrario del consentimiento cuando la ley exige consentimiento previo para almacenamiento en el terminal. |

**Regla de gobernanza:** la base legal debe **definirse antes** de tratar y **documentarse**; cambiar de base *a posteriori* suele ser problemático. Véase la guía del ICO sobre bases legales y documentación en las referencias.

---

## 4. Consentimiento (Arts. 4(11) y 7 RGPD)

Cuando el consentimiento es la base legal, debe ser:

- **Libre**: sin condicionar de forma indebida el acceso al servicio al aceptar cookies no necesarias (los “cookie walls” han sido cuestionados por autoridades y el EDPB).
- **Específico**: por finalidad (p. ej. analítica separada de publicidad).
- **Informado**: información clara antes de aceptar.
- **Unívoco**: acción afirmativa clara; **no** usar casillas pre-marcadas para opciones no esenciales.

**Art. 7:** Debe poder **demostrarse** que el interesado consintió; el interesado puede **retirar** el consentimiento con la misma facilidad con que lo dio; la retirada no afecta la licitud del tratamiento previo.

**Buenas prácticas en UI:** enlaces a política/cookies al mismo nivel que el banner; centro de preferencias; conservar registro de la prueba de consentimiento donde corresponda.

---

## 5. Transparencia: política de privacidad y capas (Arts. 13 y 14 RGPD)

### Art. 13 — Datos obtenidos **directamente** del interesado (p. ej. formulario en el sitio)

Información mínima (adaptar redacción al caso), incluyendo de forma concisa y accesible:

| Tema | Contenido típico |
|------|------------------|
| Identidad y datos de contacto | Responsable, DPO si aplica. |
| Fines y base legal | Por cada tratamiento. |
| Interés legítimo | Si se usa Art. 6(1)(f), cuál es y la evaluación de equilibrio en líneas generales. |
| Destinatarios | Quién recibe los datos (interno, encargados, categorías de terceros). |
| Transferencias | Países terceros, garantías (SCC, adecuación, DPF, etc.). |
| Plazo de conservación | O criterios para determinarlo. |
| Derechos | Acceso, rectificación, supresión, limitación, portabilidad, oposición; retirada del consentimiento si aplica; reclamación ante autoridad de control. |
| Obligatoriedad | Si la comunicación de datos es obligatoria o contractual y consecuencias de no facilitarlos. |
| Decisiones automatizadas | Si existen, con la información del Art. 22. |

### Art. 14 — Datos **no** obtenidos del interesado

Aplica cuando los datos vienen de otra fuente (p. ej. listas B2B, partners): información similar más categorías de datos y fuentes, en los plazos del Art. 14.

**Capas (*layered notice*):** resumen visible en el punto de recogida + enlace a política completa mejora la usabilidad sin sustituir el contenido obligatorio.

Fuentes: [Art. 13 RGPD (gdpr-info.eu)](https://gdpr-info.eu/art-13-gdpr/), [Art. 14 RGPD (gdpr-info.eu)](https://gdpr-info.eu/art-14-gdpr/).

---

## 6. Cookies, píxeles y almacenamiento local (ePrivacy + RGPD)

### Papel de cada marco

- **ePrivacy (Directiva 2002/58/CE):** reglas específicas sobre acceso al dispositivo del usuario y almacenamiento; en muchos Estados miembros las cookies **no esenciales** requieren **consentimiento previo** salvo excepciones muy acotadas (p. ej. cookies estrictamente necesarias para un servicio explícitamente solicitado).
- **RGPD:** define requisitos de **consentimiento válido** cuando el consentimiento es la base para el tratamiento de datos personales vía cookies u otras tecnologías.

### Clasificación operativa (orientativa)

| Tipo | Ejemplos orientativos | Consentimiento previo (típico) |
|------|------------------------|--------------------------------|
| Estrictamente necesarias | Sesión, carrito, seguridad CSRF, preferencias de consentimiento | No suele requerirse opt-in (siguen siendo transparentes en la política). |
| Preferencias | Idioma, accesibilidad no esencial para el servicio mínimo | Suele requerirse consentimiento. |
| Analíticas | Medición de audiencia, A/B con identificadores | Suele requerirse consentimiento si no son estrictamente necesarias. |
| Marketing / terceros | Píxeles de redes, remarketing | Consentimiento específico. |

### Banners y primer nivel (línea EDPB y práctica de supervisores)

El **European Data Protection Board (EDPB)** ha insistido en que **rechazar** debe ser tan fácil como **aceptar**: en el **primer nivel** del banner deben existir opciones con **igual prominencia** (p. ej. “Aceptar” / “Rechazar todo” sin ocultar el rechazo en un segundo clic forzoso o con contrastes engañosos). Las **Guías 05/2020 sobre consentimiento** desarrollan requisitos de consentimiento bajo el RGPD.

**Prohibido:** casillas pre-marcadas para fines no esenciales; diseño que induzca al error (*dark patterns*).

---

## 7. Integraciones de terceros (SaaS)

Sitios web habituales conectan servicios que tratan datos personales:

- Analítica (con o sin IP anonimizada).
- Mapas, vídeos, fuentes, widgets sociales.
- Chat, CRM, email transaccional, pasarelas de pago.

**Checklist de encargo:**

1. Identificar si el proveedor trata datos **solo por instrucción** del responsable → **Art. 28**: contrato de encargado (DPA), subencargados autorizados o notificación, ayuda al cumplimiento.
2. Si el proveedor es **co-responsable** o determina fines por su cuenta → estructura jurídica distinta (Art. 26).
3. Publicar o mantener actualizada la **lista de encargados** / subencargados cuando sea procedente en la política de privacidad o anexo.

---

## 8. Transferencias internacionales (Arts. 44–49 RGPD)

Si datos personales del EEE se envían a **países sin decisión de adecuación**, el responsable debe asegurar **garantías apropiadas** (p. ej. **Cláusulas Contractuales Tipo — SCC**) y, en muchos casos, **evaluación de riesgo** complementaria según evolución jurisprudencial y guías EDPB.

**EU–US Data Privacy Framework (DPF):** la Comisión Europea adoptó una **decisión de adecuación** que permite flujos hacia organizaciones estadounidenses **certificadas** bajo el marco DPF, sin medidas adicionales típicas de SCC para esos flujos, sujeto a los límites del propio marco y a cambios normativos o judiciales.

Para **cada** herramienta (p. ej. analytics en EE. UU.): verificar si el proveedor está en el **Data Privacy Framework** o si se usan SCC u otro mecanismo, y **documentarlo** en el registro de tratamientos y en la información al interesado.

---

## 9. Derechos del interesado en la práctica web (Arts. 15–22)

| Derecho | Implementación web típica |
|---------|---------------------------|
| Acceso (Art. 15) | Canal email o formulario seguro; identificación razonable del solicitante. |
| Rectificación (Art. 16) | Edición de perfil o proceso manual documentado. |
| Supresión (Art. 17) | “Olvido” con excepciones legales (facturación, litigios). |
| Limitación (Art. 18) | Procedimiento interno para marcar datos como restringidos. |
| Portabilidad (Art. 20) | Exportación en formato estructurado de uso común cuando el tratamiento sea automatizado y basado en consentimiento o contrato. |
| Oposición (Art. 21) | Especialmente para interés legítimo y marketing directo. |

**Plazos:** el RGPD establece **un mes** prorrogable en casos complejos (con información al interesado). Las autoridades locales pueden publicar orientación adicional.

---

## 10. Seguridad y minimización (Arts. 25 y 32 RGPD)

- **Privacidad desde el diseño y por defecto (Art. 25):** solo los datos necesarios; retención acotada; permisos mínimos en backoffice.
- **Medidas técnicas y organizativas (Art. 32):** cifrado en tránsito (HTTPS), controles de acceso, copias de seguridad, registro de accesos donde aplique, gestión de incidentes.
- **Formularios:** validar en servidor; no recoger campos sensibles sin necesidad y sin base legal y medidas reforzadas (Arts. 9–10 si hay categorías especiales).

---

## 11. Registro de actividades de tratamiento (Art. 30)

Organizaciones con más de 250 empleados, o con tratamientos no ocasionales de riesgo, o categorías especiales, etc., deben mantener un **registro** de actividades (salvo excepciones del propio Art. 30).

Para un sitio corporativo típico, el registro suele incluir: web corporativa, CRM, email marketing, analítica, soporte, proveedores, bases legales, conservación, transferencias y medidas de seguridad.

---

## 12. Checklist operativo pre-lanzamiento

- [ ] **Responsable y DPO** (si aplica) identificados en política y pie legal.
- [ ] **Mapa de datos:** qué se recoge en cada formulario, logs, cookies y scripts de terceros.
- [ ] **Bases legales** documentadas por cada finalidad.
- [ ] **Política de privacidad** y, si aplica, **política de cookies** alineadas con Arts. 13–14.
- [ ] **Banner de cookies:** primer nivel con **aceptar / rechazar todo** con igual prominencia; sin pre-tick; centro de preferencias granular.
- [ ] **Carga diferida** de scripts no esenciales hasta consentimiento (implementación técnica).
- [ ] **Contratos Art. 28** con encargados (hosting, email, CRM, analytics).
- [ ] **Transferencias internacionales** identificadas y garantías documentadas.
- [ ] **Procedimiento de derechos** del interesado y plazos internos.
- [ ] **HTTPS**, cabeceras de seguridad razonables, minimización en campos.
- [ ] **Registro Art. 30** actualizado (si aplica).
- [ ] **DPIA (Art. 35)** evaluada para tratamientos de alto riesgo (p. ej. perfilado a gran escala, datos sensibles masivos).

---

## 13. Reino Unido y otros marcos

Tras el Brexit, el **UK GDPR** y la **DPA 2018** regulan el tratamiento en el Reino Unido. Las reglas son **muy similares** al RGPD UE pero la **ICO** publica guía propia y pueden existir diferencias en detalle (p. ej. evolución del “consent or pay” y normativa local). Los sitios con tráfico mixto UE/UK deben valorar ambos marcos con asesoría local.

---

## 14. Descargo de responsabilidad

Este documento resume hallazgos y buenas prácticas de cumplimiento orientadas a sitios web. **No sustituye** asesoría legal cualificada, evaluación de impacto ni interacción con la autoridad de protección de datos competente. Las multas y medidas correctivas dependen del caso y de la jurisdicción.

---

## Referencias (URLs completas)

### Texto y hubs del RGPD

- [Reglamento (UE) 2016/679 — texto consolidado (EUR-Lex)](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32016R0679)
- [GDPR.eu / gdpr-info.eu (texto y artículos comentados en inglés)](https://gdpr-info.eu/)

### Autoridades y guías

- [European Data Protection Board (EDPB)](https://www.edpb.europa.eu/)
- [Guías 05/2020 del EDPB sobre consentimiento bajo el Reglamento 2016/679](https://edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en) — [PDF en inglés](https://edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_202005_consent_en.pdf)
- [ICO (Reino Unido) — Guía sobre bases legales](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/)
- [ICO — Consentimiento](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/consent/)
- [ICO — Cookies y avisos de privacidad (detalle)](https://ico.org.uk/for-organisations/advice-for-small-organisations/privacy-notices-and-cookies/cookies-and-privacy-notices-in-detail)
- [ICO — Documentar la base legal](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/accountability-framework/records-of-processing-and-lawful-basis/documenting-your-lawful-basis)

### Marco de cookies / telecomunicaciones (UE)

- [Directiva 2002/58/CE (ePrivacy) — EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A02002L0058-20091219)

### Transferencias internacionales

- [Comisión Europea — Transferencias de datos UE–EE. UU.](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en)
- [Nota informativa del EDPB sobre la decisión de adecuación UE–EE. UU. (julio 2023, PDF)](https://www.edpb.europa.eu/system/files/2023-07/edpb_informationnoteadequacydecisionus_en.pdf)

---

*Última actualización del documento: abril de 2026 (revisar periódicamente cambios normativos y guías de supervisores).*
