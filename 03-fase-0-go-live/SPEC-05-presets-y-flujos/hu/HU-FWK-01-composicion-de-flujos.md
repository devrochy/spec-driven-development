---
id: HU-FWK-01
titulo: Composición correcta de flujos multi-pack
spec: SPEC-05
fase: 0
hito: 0A
workstream: Framework/Plugins
prioridad: P0
critico: true
estimacion: M
impacto: [calidad_ia, operacion]
req: [REQ-FWK-01]
dependencias: []
skills: ["agentcore-conventions", "arquitecto", "eval-runner", "adr"]
ola: 2
estado: terminada
---

# HU-FWK-01 · Composición correcta de flujos multi-pack

> Estado SDD: Terminada — implementada y desplegada en test 2026-10-08 (issue [core #279](https://github.com/devrochy/agent-core/issues/279)).

**ID:** HU-FWK-01

**Título:** Composición correcta de flujos multi-pack

**Workstream:** Framework/Plugins

**Historia:** Como dueño de un negocio con varias habilidades quiero que el flujo del asistente combine las de todos los packs sin ocultar tools ni borrar lo que configuré para que agregar una habilidad nunca rompa otra.

**Por qué importa (valor empresarial):** El "superpoder" es combinar packs (demo + plan + cobro). Si combinar packs oculta tools o un re-seed borra la configuración del negocio, el asistente falla justo en los negocios más valiosos, los que usan varias habilidades.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-FWK-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Sin tools ocultas.** Dado un negocio con commerce, calendar y cobranza, cuando se compone el flujo, entonces todas las tools habilitadas de los tres packs y las del core (memoria, escalamiento) están disponibles.
- **Sin choques.** Dado dos packs que traen una sección "saludo", cuando se componen, entonces queda una sola sección `core:saludo`.
- **Secciones propias protegidas.** Dado una sección `tenant` del negocio, cuando se re-siembra el flujo de commerce, entonces la sección propia sigue igual.
- **Re-seed sin duplicados.** Dado un re-seed repetido, cuando termina, entonces no hay secciones duplicadas.
- **Migración.** Dado el tenant `solvershub` con secciones propias etiquetadas `pack_commerce`, cuando se migra, entonces pasan a `tenant` y sus evals siguen pasando.

**Evidencia / Definición de Terminado:**
- Tests de composición con 1, 2 y 3 packs; migración de flujos con diff por negocio.
- ADR-0054 enmendado (espacios de nombres, sección `tenant`, tools siempre disponibles).

**Hallazgos al aprobar la spec (2026-10-08, `develop`):**
- Con flujo declarado, `loop.py` ofrece solo las tools del flujo: `update_customer_profile`, `remember_fact`, `send_email` y las `sub_*` del core quedan ocultas.
- `saludo` está en `pack_commerce` y `pack_cobranza`; gana el primero por orden alfabético (cobranza), así que un negocio con ambos pierde `crear_lead`, `consultar_inventario`, etc.
- El `flow.json` del negocio es autoritativo: un pack activado después no aporta secciones.
- Las `sub_*` son del core con predicado (proveedor habilitado): se ofrecen según el predicado, no siempre.

**Implementada (2026-10-08):** [agent-core #280](https://github.com/devrochy/agent-core/pull/280) (ADR-0109, enmienda ADR-0054), desplegada en test (`e0376d7`). Flujo compuesto: `core/flow.json` (`core:saludo`, `core:escalamiento`) + secciones de todos los packs habilitados (`pack_x:id`) + secciones `tenant`; el `flow.json` del negocio deja de ser autoritativo y una copia vieja de pack se ignora. `MCPTool.always_available` en las tools del core (incluidas las `sub_*`). commerce `saludo` → `descubrimiento`, cobranza `saludo` → `verificacion`. `agent-core flow migrate <slug> [--apply]`. 26 tests (los 5 Gherkin, 1/2/3 packs, overrides, migración); suite 1084.

**Migración en test (2026-10-08, con respaldo `flow.json.respaldo-20261008060213-fwk01`):** `solvershub` 8 secciones → 1 propia (`tenant:planes`); `demo-cobranza` y `demo-cobranza-norte` 6 → 0 (eran copias). Flujo resuelto sin tools desconocidas (`solvershub` 30 tools, `demo-cobranza` 35). Golden de `solvershub` en local: los mismos 6 escenarios comparables pasan antes (código de `develop`), después sin migrar y después migrado, incluidos los 4 de agendamiento de #257; los de comercio no se pudieron comparar en local por el defecto de `crm_0009` ([core #281](https://github.com/devrochy/agent-core/pull/281)) y el 08 usa un nombre anterior a HU-SUB-01.

**Pendiente menor:** `agent-core flow validate` no cuenta las `sub_*` del core como disponibles (falso negativo de la CLI; el runtime las resuelve).

**Riesgos/Notas:**
- El editor visual ([SPEC-15](../../../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md)) construye sobre esta composición.
