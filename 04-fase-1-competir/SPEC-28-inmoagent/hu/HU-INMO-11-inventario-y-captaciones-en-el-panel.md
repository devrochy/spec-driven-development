---
id: HU-INMO-11
titulo: "Inventario y captaciones en el panel, con importación"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, ingreso]
req: [REQ-INMO-01, REQ-INMO-05]
dependencias: [HU-INMO-10, HU-FWK-07, HU-MEDIA-02]
skills: ["panel-ui", "migrator", "frontend-design"]
estado: borrador
---

# HU-INMO-11 · Inventario y captaciones en el panel, con importación

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-11

**Título:** Inventario y captaciones en el panel, con importación

**Workstream:** Verticales

**Historia:** Como asesor quiero cargar, importar, corregir y publicar inmuebles y validar captaciones desde el panel, con mapa y fotos, para mantener el inventario al día.

**Por qué importa (valor empresarial):** Sin inventario confiable la búsqueda no sirve; el negocio ya tiene sus inmuebles en hojas de cálculo o en su software.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-INMO-01, REQ-INMO-05

**Dependencias:** [HU-INMO-10](HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md), [HU-FWK-07](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-07-descriptor-view.md), [HU-MEDIA-02](../../../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md)

**Criterios de aceptación (Gherkin):**
- **Importación.** Dado un CSV exportado por el negocio con 300 inmuebles, cuando se importa, entonces se crean los válidos, se informa fila por fila lo inválido y nada se duplica al reimportar.
- **Pin en el mapa.** Dado un inmueble sin ubicación confirmada, cuando el asesor pone el pin, entonces queda con `ubicacion_fuente = panel` y confirmada.
- **Validar captación.** Dado una captación enviada, cuando el asesor la aprueba, entonces se crea el inmueble en borrador con sus fotos y se emite `captacion_aprobada`.

**Evidencia / Definición de Terminado:**
- Vistas por descriptor; rol `asesor`; importación idempotente por código; fotos con [HU-MEDIA-02](../../../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md).

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
