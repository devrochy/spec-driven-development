---
id: HU-AOS-12
titulo: "Agentes con versiones inmutables: AgentSpec v3 y KernelSpec"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, calidad_ia]
req: [REQ-AOS-05]
dependencias: [HU-AOS-03]
skills: ["agentcore-conventions", "backend-design:data-modeling-discipline", "adr"]
estado: terminada
---

# HU-AOS-12 · Agentes con versiones inmutables: AgentSpec v3 y KernelSpec

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-12

**Título:** Agentes con versiones inmutables: AgentSpec v3 y KernelSpec

**Workstream:** Agent OS

**Historia:** Como dueño quiero definir agentes (Coordinador, especialistas y de back-office) con versiones que no cambian una vez publicadas, para poder probar, publicar y volver atrás sin sorpresas.

**Por qué importa (valor empresarial):** Da identidad y versión a cada agente: es la base de las releases, de las evals por agente y de reutilizar un agente en varias conexiones.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-05

**Dependencias:** [HU-AOS-03](HU-AOS-03-contrato-de-procedimientos.md)

**Criterios de aceptación (Gherkin):**
- **Borrador y publicación.** Dado un borrador de agente, cuando se publica, entonces nace una versión inmutable con hash y el borrador sigue editable.
- **Concurrencia.** Dado dos personas editando el mismo borrador, cuando la segunda guarda con un `lock_version` viejo, entonces recibe 409.
- **Lector tolerante.** Dado el AgentSpec v2 activo de un negocio, cuando se carga como v3, entonces queda el agente General de cada conexión conversacional con los procedimientos abiertos equivalentes y en sus `tools` las acciones que hoy ofrece el loop (flujo v2, `always_available` y las declarativas de las secciones `tenant`); hasta la release 1, el KernelSpec se deriva en memoria de la `persona` v2.
- **Campo por campo.** Dado cada campo del AgentSpec v2 (incluidos `extensions.guardrails` y `extensions.tools`), cuando se convierte, entonces queda en su lugar de v3 según la tabla de ADR-0113 (`maxToolCallsPerTurn` en el agente, `budgetUsdPerConversation` en el KernelSpec) y nada se pierde.
- **Tools declarativas sin secretos.** Dado una tool declarativa v2 con un header `Authorization` literal, cuando el lector tolerante la convierte, entonces el valor pasa cifrado a la instalación `core` del scope y la tool queda con `{"secret": "<nombre>"}` antes de crear la primera `agent_version`; y dado un borrador nuevo con un valor literal en `Authorization`, `Cookie` o `X-Api-Key`, cuando se guarda, entonces el validador lo rechaza.
- **Validación al guardar.** Dado un AgentSpec o KernelSpec inválido, cuando se guarda el borrador por la API, entonces se rechaza con los errores del contrato (el mismo validador del CLI y de CI).

**Evidencia / Definición de Terminado:**
- Contratos `agentspec/3` y `kernelspec/1` (ADR-0113): `kind` vive en `agents` y la identidad la da la fila; `agentcore-contracts` (Python) a v3.0.0 y se retira el espejo TS de `packages/contracts/src/`.
- Tablas y API de agentes; ruta en `/api/v1` del editor de tools declarativas (hoy solo en SSR) con los secretos por referencia; headers sensibles resueltos en `core/mcp/declarative.py` desde la configuración cifrada; tests de contrato.

**Terminada (2026-10-11):** PRs agent-core [#425](https://github.com/devrochy/agent-core/pull/425), [#429](https://github.com/devrochy/agent-core/pull/429).

**Riesgos/Notas:**
- Major de contrato: las habilidades y el plugin del negocio se migran en el mismo PR.
