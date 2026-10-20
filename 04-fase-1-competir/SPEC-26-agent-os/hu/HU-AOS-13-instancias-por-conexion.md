---
id: HU-AOS-13
titulo: "Instancias por conexión: Coordinador + General"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, confianza]
req: [REQ-AOS-01, REQ-AOS-05]
dependencias: [HU-AOS-11, HU-AOS-12]
skills: ["db-migration", "auditor-multitenant", "onboard-tenant"]
estado: terminada
---

# HU-AOS-13 · Instancias por conexión: Coordinador + General

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-13

**Título:** Instancias por conexión: Coordinador + General

**Workstream:** Agent OS

**Historia:** Como negocio quiero que cada conexión arranque con un Coordinador y un agente General equivalentes a mi asistente de hoy, para pasar al Agent OS sin notar cambios.

**Por qué importa (valor empresarial):** La migración no cambia la conducta: el riesgo queda acotado antes de sumar especialistas.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-01, REQ-AOS-05

**Dependencias:** [HU-AOS-11](HU-AOS-11-conexion-canonica.md), [HU-AOS-12](HU-AOS-12-agentes-versionados.md)

**Criterios de aceptación (Gherkin):**
- **Uno y solo uno.** Dado una conexión activa, cuando se intenta crear un segundo Coordinador, entonces el índice único lo rechaza; y cuando se intenta activarla sin Coordinador, entonces el trigger diferido lo impide.
- **Backfill.** Dado los negocios existentes, cuando corre el backfill, entonces cada conexión conversacional tiene Coordinador (KernelSpec derivado de la `persona` v2) y General (el AgentSpec v2 activo, en **cada** conexión) y no se crean agentes para integraciones.
- **Equivalencia.** Dado un negocio migrado, cuando corre su golden, entonces el resultado es igual al de antes.

**Evidencia / Definición de Terminado:**
- Backfill idempotente; API de instancias; tests.

**Terminada (2026-10-11):** PRs agent-core [#436](https://github.com/devrochy/agent-core/pull/436), [#442](https://github.com/devrochy/agent-core/pull/442).

**Riesgos/Notas:**
- Conexiones legacy sin `type_id`: el backfill de [HU-AOS-11](HU-AOS-11-conexion-canonica.md) las completa antes.
