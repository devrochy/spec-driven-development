---
id: HU-INMO-04
titulo: "Avisos por evento abiertos a las habilidades"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Canales y conexiones
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, diferenciacion]
req: [REQ-INMO-10]
dependencias: [HU-INMO-01]
skills: ["meta-whatsapp", "agentcore-conventions", "adr"]
estado: borrador
---

# HU-INMO-04 · Avisos por evento abiertos a las habilidades

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-04

**Título:** Avisos por evento abiertos a las habilidades

**Workstream:** Canales y conexiones

**Historia:** Como habilidad quiero declarar mis propios eventos de aviso al cliente, con sus variables, para que el negocio los mapee a plantillas sin cambiar el core.

**Por qué importa (valor empresarial):** Los avisos por evento son una lista fija del core (`core/gateway/event_notices.py`, `core/events/core_handlers.py`), que además arma variables de dominio (`cita`, `cargo`). Con un registro, cada habilidad declara sus avisos y manda sus variables.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-10

**Dependencias:** [HU-INMO-01](HU-INMO-01-adrs-y-dor-del-piloto.md)

**Criterios de aceptación (Gherkin):**
- **Declaración.** Dado un pack que declara `inmobiliario.visita_realizada` con sus rutas permitidas y su clave de deduplicación, cuando se activa, entonces el evento aparece en "Plantillas por evento" sin tocar `EVENTOS`.
- **Envío.** Dado el evento mapeado a una plantilla y la ventana cerrada, cuando el pack lo emite con sus variables en el payload, entonces un solo handler genérico envía la plantilla.
- **Deduplicación.** Dado el mismo evento emitido dos veces con la misma clave, cuando se procesa, entonces sale un solo aviso.
- **Compatibilidad.** Dado los eventos actuales `subscription.*` y `appointment.*`, cuando se despliega, entonces siguen funcionando igual.

**Evidencia / Definición de Terminado:**
- Registro de avisos en el core con un handler genérico; ADR nuevo que enmienda ADR-0108; tests.
- Sin cabecera con imagen ni botones de plantilla (fuera de ADR-0108 v1).

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- Cuando llegue, conviene migrar a este registro los avisos de calendar y suscripciones.
