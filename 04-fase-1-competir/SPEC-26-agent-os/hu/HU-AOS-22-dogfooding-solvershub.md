---
id: HU-AOS-22
titulo: "Dogfooding: SolversHub con Ventas, Agenda y Suscripciones"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-AOS-12, REQ-AOS-07]
dependencias: [HU-AOS-16, HU-AOS-19, HU-AOS-21, HU-SH-08]
skills: ["onboard-tenant", "customizer", "eval-runner", "desplegar-test-agent-core"]
estado: borrador
---

# HU-AOS-22 · Dogfooding: SolversHub con Ventas, Agenda y Suscripciones

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-22

**Título:** Dogfooding: SolversHub con Ventas, Agenda y Suscripciones

**Workstream:** Agent OS

**Historia:** Como SolversHub quiero atender a mis prospectos con agentes especialistas en una conexión real, para probar el Agent OS en mi propio negocio antes de venderlo.

**Por qué importa (valor empresarial):** Da evidencia real y una demo viva, y detecta fallas antes que los clientes.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-12, REQ-AOS-07

**Dependencias:** [HU-AOS-16](HU-AOS-16-habilidades-con-procedimientos-y-scope.md), [HU-AOS-19](HU-AOS-19-handoff-delegacion-y-consulta.md), [HU-AOS-21](HU-AOS-21-gate-de-release-pass-k.md), [HU-SH-08](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md)

**Criterios de aceptación (Gherkin):**
- **Agentes del negocio.** Dado la conexión de WhatsApp de `solvershub`, cuando se publica, entonces tiene Coordinador, Ventas, Agenda, Suscripciones y General con sus permisos.
- **Consistencia.** Dado el nightly, cuando corre tres noches, entonces pass^4 ≥ 0,85 y pass@1 ≥ 95 %.
- **Operación real.** Dado 14 días de tráfico real, cuando se revisan, entonces no hay incidentes P1 ni datos perdidos al cambiar de agente.

**Evidencia / Definición de Terminado:**
- Release publicada en test y, cuando exista, en producción; reporte de 14 días.

**Riesgos/Notas:**
- El tráfico real de `solvershub` es bajo: se complementa con escenarios simulados.
