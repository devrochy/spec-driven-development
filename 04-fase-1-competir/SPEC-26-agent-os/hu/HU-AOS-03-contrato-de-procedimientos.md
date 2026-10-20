---
id: HU-AOS-03
titulo: "Contrato procedure/1, linter y conversión de flujos"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, diferenciacion]
req: [REQ-AOS-03]
dependencias: [HU-AOS-01]
skills: ["agentcore-conventions", "new-pack", "backend-design:data-modeling-discipline"]
estado: terminada
---

# HU-AOS-03 · Contrato procedure/1, linter y conversión de flujos

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-03

**Título:** Contrato procedure/1, linter y conversión de flujos

**Workstream:** Agent OS

**Historia:** Como autor de una habilidad quiero declarar procedimientos con un contrato validado y convertir los flujos actuales en procedimientos abiertos, para que el recorrido de cada superpoder sea un dato verificable y no texto del prompt.

**Por qué importa (valor empresarial):** Un playbook sin validar tumbó el primer turno de los negocios (core #305). Un linter en CI evita llevar a producción un recorrido roto.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-03

**Dependencias:** [HU-AOS-01](HU-AOS-01-adrs-del-agent-os.md)

**Criterios de aceptación (Gherkin):**
- **Contrato válido.** Dado un procedimiento con datos, etapas, acciones, confirmaciones y afirmaciones, cuando pasa por `/procedures/validate`, entonces se acepta sin errores.
- **Linter.** Dado un procedimiento con una acción inexistente, una etapa inalcanzable o una acción irreversible sin confirmación, cuando corre el linter, entonces falla con un mensaje claro por cada problema.
- **Datos desde lo que toca o envía el cliente.** Dado un dato con `setBy` de un payload interactivo, una condición por tipo de contenido (ubicación, imagen) o un dato con candidatos para elegir, cuando pasa por el validador, entonces se acepta. (Que el motor lo llene sin pasar por el LLM se verifica en [HU-AOS-05](HU-AOS-05-motor-de-procedimientos.md), porque depende del formato del payload en el ingreso del kernel.)
- **Conversión.** Dado el flujo compuesto de un negocio, cuando se convierte, entonces cada sección queda como procedimiento abierto (una etapa con sus acciones) sin cambiar qué acciones se ofrecen; la confirmación se hereda del binding v2 (`requiresConfirmation`) y el procedimiento convertido pasa el linter.

**Evidencia / Definición de Terminado:**
- Modelo `procedure/1` en los contratos (minor 2.1.0: es aditivo; el major 3.0.0 llega con AgentSpec v3 en [HU-AOS-12](HU-AOS-12-agentes-versionados.md), ADR-0113); acciones de otra habilidad por nombre con la dependencia declarada (`requires`); el mismo linter y validador en el CLI, en CI y en la API (al guardar un borrador o publicar una release, lo inválido no se guarda); las afirmaciones se compilan a `Afirmacion` y se registran por `register_afirmaciones` (ADR-0119); conversor de `flow.json` v2; tests.

**Terminada (2026-10-11):** PRs agent-core [#405](https://github.com/devrochy/agent-core/pull/405).

**Riesgos/Notas:**
- El contrato nace con lo mínimo que usan los 4 procedimientos críticos; lo demás se agrega con ADR.
- Entran en `procedure/1` desde el inicio (ADR-0113, aceptado el 2026-10-09) tres extensiones con al menos dos casos reales: dato llenado desde un payload interactivo (`plan:` de comercio, listas de agenda), condición por tipo de contenido (comprobantes de [HU-MEDIA-04](../../../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md), ubicación) y dato con candidatos para elegir. Salieron de la revisión de [SPEC-28](../../SPEC-28-inmoagent/design.md#lo-que-el-agent-os-planificado-no-alcanza-para-la-vertical).
