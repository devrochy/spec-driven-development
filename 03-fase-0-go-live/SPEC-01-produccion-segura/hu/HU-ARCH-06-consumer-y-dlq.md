---
id: HU-ARCH-06
titulo: Consumer con reclamo de pendientes y DLQ alcanzable
spec: SPEC-01
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, calidad_ia]
req: [REQ-ARCH-08]
dependencias: []
skills: ["backend-design:idempotency-and-side-effects", "backend-design:error-handling-as-design", "backend-design:incident-thinker", "backend-design:observability-by-default"]
ola: 2
estado: terminada
---

# HU-ARCH-06 · Consumer con reclamo de pendientes y DLQ alcanzable

> Estado SDD: Terminada — implementada 2026-10-04.

**ID:** HU-ARCH-06

**Título:** Consumer con reclamo de pendientes y DLQ alcanzable

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de un negocio quiero que ningún mensaje de mis clientes se pierda si el procesamiento falla o el servicio se reinicia para que nadie quede sin respuesta.

**Por qué importa (valor empresarial):** Hoy un mensaje que falla una vez queda pendiente para siempre: la DLQ nunca se alcanza (`core/orchestrator/consumer.py:59,88`). Un cliente que pregunta por su pedido y no recibe respuesta es una venta perdida y un reclamo.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-08

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Reintento.** Dado un mensaje cuyo procesamiento falla una vez por un error transitorio, cuando pasa el tiempo de reclamo, entonces otra réplica lo reclama con `XAUTOCLAIM` y lo procesa.
- **DLQ.** Dado un mensaje que falla 3 veces, cuando se agota el reintento, entonces pasa a `agent_core:inbound:dlq` con el error, se hace `XACK` y aparece en "Mensajes fallidos" del panel.
- **Reinicio.** Dado un reinicio del worker con mensajes en vuelo, cuando vuelve, entonces los pendientes se reclaman y ninguno se pierde.
- **Varias réplicas.** Dado dos réplicas del consumer, cuando procesan, entonces cada una usa un nombre propio y ningún mensaje se procesa dos veces (idempotencia por `external_message_id`, ADR-0007).

**Evidencia / Definición de Terminado:**
- Tests de integración con Redis real para reintento, DLQ y reinicio.
- Métrica de tamaño de la DLQ disponible para [HU-ARCH-07](HU-ARCH-07-observabilidad-prod.md).
- `docs/ROADMAP.md:53` corregido (hoy marca como hecho algo que no funciona).


**Implementada (2026-10-04):** core [#214](https://github.com/devrochy/agent-core/pull/214): reclamo automático con `XAUTOCLAIM` (idle configurable) en `consume_loop`; nombre de consumer único por réplica; claim con estado (`processed_events.completed_at`, migración 0049: `claimed`/`duplicate`/`busy`, claim abandonado revocado); DLQ con `error`/`deliveries`/`failed_at` + `XACK` + revocación del claim; ADR-0090. Incidente que lo motivó: 2026-10-04, mensajes `pending` para siempre en las pruebas E2E del calendario. Tests de integración: reclamo de huérfano, busy/duplicate/abandonado, DLQ con error, nombre único (4 passed). ROADMAP corregido.

**Riesgos/Notas:**
- El nombre del stream (`agent_core:inbound`) no se cambia ([SPEC-00](../../SPEC-00-reestructuracion/spec.md)).
