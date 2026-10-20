---
id: HU-AOS-10
titulo: "Kernel del Coordinador: políticas, core_decisions, turn_outcomes y trazas"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [confianza, operacion]
req: [REQ-AOS-06, REQ-AOS-08]
dependencias: [HU-AOS-02]
skills: ["agentcore-conventions", "backend-design:observability-by-default", "backend-design:think-before-coding"]
estado: terminada
---

# HU-AOS-10 · Kernel del Coordinador: políticas, core_decisions, turn_outcomes y trazas

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-10

**Título:** Kernel del Coordinador: políticas, core_decisions, turn_outcomes y trazas

**Workstream:** Agent OS

**Historia:** Como operador quiero que las políticas del turno vivan en un kernel único y que cada turno deje registradas su decisión y su resultado, para saber exactamente por qué el asistente hizo lo que hizo.

**Por qué importa (valor empresarial):** Hoy las políticas están repartidas entre el consumer y el loop. Un kernel con registros append-only da trazabilidad de punta a punta y es la base del Coordinador.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-06, REQ-AOS-08

**Dependencias:** [HU-AOS-02](HU-AOS-02-esquema-aditivo.md)

**Criterios de aceptación (Gherkin):**
- **Sin cambio de conducta.** Dado el kernel extraído, cuando corren el golden y los journeys, entonces los resultados son iguales a los de antes.
- **Decisión y resultado.** Dado cualquier turno, cuando termina, entonces existen una fila en `core_decisions` y otra en `turn_outcomes` con el mismo `turn_id` y `trace_id`.
- **Bloqueos.** Dado un negocio pausado o sin cuota, cuando entra un mensaje, entonces la decisión queda `blocked` con su motivo y no se llama al LLM.
- **Conexión pausada.** Dado una conexión pausada (ADR-0122), cuando entra un mensaje, entonces se guarda sin IA, como hoy, y el Coordinador no se ejecuta (`blocked_by = connection_paused`).
- **Trazas.** Dado OTel activo, cuando corre un turno, entonces los spans del kernel, el hilo, las acciones y la salida comparten `trace_id`, también en Celery.

**Evidencia / Definición de Terminado:**
- Ingreso y decisiones en el kernel (`core/kernel/`: `ingress`, `router`, `procedures`, `state`, `a2a`, `egress`, `decisions`); el verificador sigue en `core/orchestrator/verificador/` (ADR-0119), sin un segundo verificador; `turn_id` en mensajes, `usage_ledger` y `audit_log`; sobrecarga p95 del kernel ≤ 50 ms; `CLAUDE.md` (Estructura) y `docs/architecture/c4.md` actualizados; tests.

**Terminada (2026-10-11):** PRs agent-core [#428](https://github.com/devrochy/agent-core/pull/428), [#437](https://github.com/devrochy/agent-core/pull/437), [#451](https://github.com/devrochy/agent-core/pull/451).

**Riesgos/Notas:**
- Es un refactor del corazón del turno: se hace tras el 0A, detrás de una bandera y con golden idénticos.
