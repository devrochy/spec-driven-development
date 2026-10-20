---
id: HU-FLOW-05
titulo: Probar el borrador, publicar y revertir
spec: SPEC-15
fase: 1
hito: "1"
workstream: Flujo visual
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, confianza]
req: [REQ-FLOW-03]
dependencias: [HU-FLOW-04, HU-ARCH-14]
skills: ["eval-runner", "backend-design:testing-with-discernment"]
estado: parqueada
---

# HU-FLOW-05 · Probar el borrador, publicar y revertir

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-15](../spec.md).

**ID:** HU-FLOW-05

**Título:** Probar el borrador, publicar y revertir

**Workstream:** Flujo visual

**Historia:** Como dueño de un negocio quiero probar mi flujo editado en el simulador antes de publicarlo y poder volver atrás para no afectar a mis clientes con un cambio malo.

**Por qué importa (valor empresarial):** Sin prueba previa, el editor visual es una forma rápida de romper el asistente en producción. La prueba con sandbox y la reversa hacen seguro el autoservicio.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FLOW-03

**Dependencias:** [HU-FLOW-04](HU-FLOW-04-editor-visual.md), [HU-ARCH-14](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-14-playground-sandbox.md)

**Criterios de aceptación (Gherkin):**
- **Probar.** Dado un borrador, cuando pulso "Probar", entonces converso con el asistente usando el borrador y las tools con efectos simulados.
- **Evals.** Dado publicar, cuando el negocio tiene golden set, entonces se corre un subconjunto y se avisa si baja del umbral.
- **Publicar y revertir.** Dado publicar, cuando confirmo, entonces se crea una versión con `audit_log`; dado revertir, entonces vuelve la anterior.

**Evidencia / Definición de Terminado:**
- Integración con el playground y el canary de evals; tests.

**Riesgos/Notas:**
- El canary reutiliza lo construido en [HU-SH-08](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md).
