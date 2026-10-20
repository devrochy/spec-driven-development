---
id: HU-FLOW-02
titulo: Flujo versionado dentro del AgentSpec
spec: SPEC-15
fase: 1
hito: "1"
workstream: Flujo visual
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, calidad_ia]
req: [REQ-FLOW-01]
dependencias: [HU-FLOW-01]
skills: ["db-migration", "backend-design:migration-safety", "eval-runner"]
estado: parqueada
---

# HU-FLOW-02 · Flujo versionado dentro del AgentSpec

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-15](../spec.md).

**ID:** HU-FLOW-02

**Título:** Flujo versionado dentro del AgentSpec

**Workstream:** Flujo visual

**Historia:** Como dueño de un negocio quiero que cada cambio de mi flujo quede como una versión que puedo revertir para experimentar sin miedo.

**Por qué importa (valor empresarial):** Versionar el flujo junto al resto del asistente permite volver atrás en segundos si un cambio baja la calidad, que es la red de seguridad de cualquier editor visual.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FLOW-01

**Dependencias:** [HU-FLOW-01](HU-FLOW-01-adr-editor-de-flujo.md)

**Criterios de aceptación (Gherkin):**
- **Migración.** Dado los flujos actuales en archivo, cuando se migran, entonces quedan en `AgentSpec.extensions["flow"]` y el asistente se comporta igual (evals sin regresión).
- **Borrador.** Dado un cambio sin publicar, cuando el asistente atiende, entonces usa la versión publicada.
- **Reversa.** Dado una versión publicada con problemas, cuando vuelvo a la anterior, entonces el asistente la usa de inmediato.

**Evidencia / Definición de Terminado:**
- Migración con verificación por negocio; tests de borrador y reversa.

**Riesgos/Notas:**
- El archivo `flow.json` del pack queda como semilla y exportación.
