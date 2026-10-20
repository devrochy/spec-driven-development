---
id: HU-AOS-05
titulo: "Motor de procedimientos: etapas, datos validados, precondiciones, confirmación y cierre"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [calidad_ia, confianza, ingreso]
req: [REQ-AOS-03]
dependencias: [HU-AOS-03, HU-AOS-04]
skills: ["agentcore-conventions", "backend-design:think-before-coding", "backend-design:idempotency-and-side-effects"]
estado: terminada
---

# HU-AOS-05 · Motor de procedimientos: etapas, datos validados, precondiciones, confirmación y cierre

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-05

**Título:** Motor de procedimientos: etapas, datos validados, precondiciones, confirmación y cierre

**Workstream:** Agent OS

**Historia:** Como dueño de un negocio quiero que el asistente siga cada superpoder paso a paso, con datos validados por el sistema y confirmación antes de lo irreversible, para que la venta o la cita salga bien siempre y no solo a veces.

**Por qué importa (valor empresarial):** Convierte "el prompt lo sugiere" en "el sistema lo garantiza": acciones solo en su etapa, datos del servidor y cierre por evento de dominio.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-03

**Dependencias:** [HU-AOS-03](HU-AOS-03-contrato-de-procedimientos.md), [HU-AOS-04](HU-AOS-04-estado-de-la-conversacion.md)

**Criterios de aceptación (Gherkin):**
- **Acciones por etapa.** Dado una tarea en la etapa "Datos", cuando el modelo intenta `crear_pedido`, entonces la acción no se ofrece y, si llega igual, se deniega con un error de negocio.
- **Datos validados.** Dado `actualizar_tarea` con un plan inexistente, cuando se valida con el *resolver*, entonces vuelve un error en lenguaje claro y el dato no se guarda.
- **Confirmación.** Dado una etapa con confirmación por botón, cuando el cliente escribe "dale" sin tocar el botón y el clasificador no tiene confianza alta, entonces la tarea no avanza y se vuelve a pedir la confirmación.
- **Cierre por evento.** Dado `pago_confirmado` del pedido de la tarea, cuando llega por el outbox, entonces la tarea pasa a `completed` y devuelve el control.
- **Datos sin LLM.** Dado un dato con `setBy` de un payload interactivo, una condición por tipo de contenido o candidatos para elegir (contrato de [HU-AOS-03](HU-AOS-03-contrato-de-procedimientos.md)), cuando el cliente toca el botón o envía ese contenido, entonces el motor llena el dato sin pasar por el LLM.
- **Modo sombra.** Dado un negocio con el motor en sombra, cuando atiende con el flujo actual, entonces el motor calcula transiciones y comprobaciones y registra las diferencias sin responder.

**Evidencia / Definición de Terminado:**
- Motor en el kernel integrado con el loop actual; bandera `AOS_PROCEDURES` por negocio, en base de datos y editable solo por el master, que exige `AOS_RUNTIME = v3` (ADR-0112): en R1 el motor se mide en evals y en modo sombra, y se enciende en producción en [HU-AOS-15](HU-AOS-15-migracion-sin-regresion.md); tests por regla.

**Terminada (2026-10-11):** PRs agent-core [#440](https://github.com/devrochy/agent-core/pull/440), [#441](https://github.com/devrochy/agent-core/pull/441).

**Riesgos/Notas:**
- Rigidez: cada etapa tiene un objetivo flexible y digresiones con la pila; el agente General conserva procedimientos abiertos de respaldo.
