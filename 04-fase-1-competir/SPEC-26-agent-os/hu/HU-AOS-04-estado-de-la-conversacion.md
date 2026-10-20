---
id: HU-AOS-04
titulo: "Estado de la conversación: tareas event-sourced y tarjeta de estado"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [calidad_ia, confianza]
req: [REQ-AOS-04]
dependencias: [HU-AOS-02]
skills: ["backend-design:data-modeling-discipline", "backend-design:idempotency-and-side-effects", "auditor-multitenant"]
estado: terminada
---

# HU-AOS-04 · Estado de la conversación: tareas event-sourced y tarjeta de estado

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-04

**Título:** Estado de la conversación: tareas event-sourced y tarjeta de estado

**Workstream:** Agent OS

**Historia:** Como agente, y como persona que toma una conversación, quiero ver en cada turno qué tarea está en curso, qué datos ya dio el cliente y qué falta, para no pedir lo mismo dos veces ni contradecir lo hecho.

**Por qué importa (valor empresarial):** Hoy la coherencia entre turnos depende de que el modelo relea el historial. Con un estado único, el cliente no repite datos y el relevo humano es inmediato.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-04

**Dependencias:** [HU-AOS-02](HU-AOS-02-esquema-aditivo.md)

**Criterios de aceptación (Gherkin):**
- **Tarea y eventos.** Dado un comando que inicia un procedimiento o fija un dato, cuando se aplica, entonces se escribe un `task_event` y la proyección `conversation_tasks` se actualiza en la misma transacción.
- **Reconstrucción.** Dado los eventos de una tarea, cuando se reconstruye la proyección, entonces el resultado es idéntico al guardado.
- **Tarjeta de estado.** Dado una conversación con una tarea en foco y otra en pausa, cuando empieza el turno, entonces el prompt recibe la tarjeta en el bloque dinámico, justo antes de la fecha y hora, que sigue siendo lo último (ADR-0091), sin romper la caché del prefijo; sus rótulos salen de un playbook del core y los valores van delimitados y escapados (invariantes 3 y 7).
- **Tareas de un episodio anterior.** Dado una tarea abierta sin actividad durante todo el episodio anterior, cuando empieza un episodio nuevo, entonces se escribe el evento `episode_expired`, la tarea queda `cancelled` con ese motivo y conserva sus datos y sus eventos. (Pasar sus datos válidos a `memory_facts` con procedencia se movió a [HU-AOS-36](HU-AOS-36-memoria-por-scope.md): sin lector, purga ni retención sería PII huérfana; revisión del arquitecto, agent-core #426.)
- **Confirmación en la tarea.** Dado una etapa que espera confirmación, cuando se pide, entonces queda como `confirmation_requested` en la tarea y no en `conversations.state.pending_confirmation`, que se usa solo para acciones fuera de procedimiento.
- **Purga.** Dado una purga de cliente (`purge_memory`, ADR-0053), cuando se ejecuta, entonces sus tareas quedan intactas como registro del negocio, igual que `messages`, y solo `purge_tenant` las borra.

**Evidencia / Definición de Terminado:**
- Módulo de estado en el kernel (`core/kernel/state.py`); `conversations.episode_started_at`; `task_events` con la versión de esquema del procedimiento en `data`; API `/conversations/{id}/tasks` y eventos; tests de aislamiento y de reconstrucción entre versiones.

**Terminada (2026-10-11):** PRs agent-core [#426](https://github.com/devrochy/agent-core/pull/426).

**Riesgos/Notas:**
- Datos personales en eventos append-only: siguen la regla de `messages` (ADR-0053); si un pedido legal exige borrar también las tareas de un cliente, hace falta otro ADR.
