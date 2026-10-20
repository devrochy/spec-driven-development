---
id: HU-FLOW-01
titulo: ADR del editor visual de flujo
spec: SPEC-15
fase: 1
hito: "1"
workstream: Flujo visual
prioridad: P1
critico: false
estimacion: S
impacto: [diferenciacion]
req: [REQ-FLOW-01, REQ-FIX-03]
dependencias: [HU-FWK-01]
skills: ["adr", "arquitecto", "doc-coauthoring"]
estado: parqueada
---

# HU-FLOW-01 · ADR del editor visual de flujo

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-15](../spec.md) (D-SPEC-15-1, P-09).

**ID:** HU-FLOW-01

**Título:** ADR del editor visual de flujo

**Workstream:** Flujo visual

**Historia:** Como responsable técnico quiero decidir por escrito dónde vive el flujo, quién edita qué y cómo se publica para que el editor no rompa los contratos congelados ni la calidad del asistente.

**Por qué importa (valor empresarial):** El editor toca tres ADR aceptados (0017, 0026, 0054). Sin un ADR nuevo, la regla dura de `WORKFLOW.md` impide implementarlo; con él, el diferencial queda sobre bases seguras.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-FLOW-01, REQ-FIX-03

**Dependencias:** [HU-FWK-01](../../../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md)

**Criterios de aceptación (Gherkin):**
- **Decisiones.** Dado el ADR, cuando se acepta, entonces fija almacenamiento, borrador, permisos (estructura vs. texto), validador único, publicación y reversa.
- **ADR afectados.** Dado ADR-0017, 0026 y 0054, cuando se acepta el nuevo, entonces quedan marcados como enmendados o superseded en lo que corresponde.

**Evidencia / Definición de Terminado:**
- ADR aceptado en `solvershub-core/docs/adr/`.

**Riesgos/Notas:**
- Depende de la composición multi-pack de [HU-FWK-01](../../../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md).
