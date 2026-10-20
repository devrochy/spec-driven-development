---
id: HU-AOS-06
titulo: "Comandos del hilo y verificador sobre el estado"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, confianza]
req: [REQ-AOS-03, REQ-ARCH-21]
dependencias: [HU-AOS-05, HU-ARCH-29]
skills: ["new-tool", "agentcore-conventions", "backend-design:testing-with-discernment"]
estado: terminada
---

# HU-AOS-06 · Comandos del hilo y verificador sobre el estado

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-06

**Título:** Comandos del hilo y verificador sobre el estado

**Workstream:** Agent OS

**Historia:** Como agente quiero comandos estructurados para iniciar, completar, pausar o cancelar tareas, y que el verificador use el estado de la tarea como evidencia, para que lo que digo coincida siempre con lo que el sistema registró.

**Por qué importa (valor empresarial):** Une el lenguaje del modelo con el estado del kernel mediante un contrato estrecho y elimina las afirmaciones sin respaldo.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-03, REQ-ARCH-21

**Dependencias:** [HU-AOS-05](HU-AOS-05-motor-de-procedimientos.md), [HU-ARCH-29](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md)

**Criterios de aceptación (Gherkin):**
- **Comandos tipados.** Dado `iniciar_procedimiento` con un id fuera de los candidatos, cuando se ejecuta, entonces se rechaza sin crear la tarea.
- **Resultado con tarjeta.** Dado un comando aplicado, cuando vuelve al modelo, entonces trae la tarjeta actualizada y las acciones permitidas de la nueva etapa.
- **Verificación con estado.** Dado una tarea con `pedido_id`, cuando el borrador dice "tu pedido OC-0042 quedó creado", entonces pasa; y cuando cita otro número, entonces falla.

**Evidencia / Definición de Terminado:**
- Comandos como acciones del core con JSON Schema; el verificador de `core/orchestrator/verificador/` (ADR-0119) extendido con el estado de las tareas, sin un segundo verificador en `core/kernel/`; tests.

**Terminada (2026-10-11):** PRs agent-core [#443](https://github.com/devrochy/agent-core/pull/443).

**Riesgos/Notas:**
- Demasiados comandos confunden al modelo: solo se ofrecen los que aplican a la etapa.
