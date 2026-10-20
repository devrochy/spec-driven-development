---
id: HU-FLOW-06
titulo: Flujo semilla por preset con diff al aplicar
spec: SPEC-15
fase: 1
hito: "1"
workstream: Flujo visual
prioridad: P1
critico: false
estimacion: S
impacto: [diferenciacion]
req: [REQ-FLOW-04]
dependencias: [HU-FLOW-02, HU-FWK-10]
skills: ["new-pack", "eval-runner"]
estado: parqueada
---

# HU-FLOW-06 · Flujo semilla por preset con diff al aplicar

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-15](../spec.md).

**ID:** HU-FLOW-06

**Título:** Flujo semilla por preset con diff al aplicar

**Workstream:** Flujo visual

**Historia:** Como dueño de un negocio que aplica un preset quiero ver qué cambiará en mi flujo antes de aceptarlo para no perder las etapas que ya ajusté.

**Por qué importa (valor empresarial):** Aplicar un preset sobre un negocio existente es la forma de "agregar superpoderes" a clientes actuales (expansión). Sin diff, el miedo a perder lo configurado frena la venta.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-FLOW-04

**Dependencias:** [HU-FLOW-02](HU-FLOW-02-flujo-en-agentspec.md), [HU-FWK-10](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-10-aplicar-preset-desde-panel.md)

**Criterios de aceptación (Gherkin):**
- **Diff.** Dado un preset nuevo para mi negocio, cuando lo previsualizo, entonces veo etapas y acciones que se agregan, cambian o quedan igual.
- **Respeta lo propio.** Dado mis secciones `tenant`, cuando aplico el preset, entonces no se modifican.

**Evidencia / Definición de Terminado:**
- Diff en la UI de aplicar preset ([HU-FWK-10](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-10-aplicar-preset-desde-panel.md)); tests.

**Riesgos/Notas:**
- —
