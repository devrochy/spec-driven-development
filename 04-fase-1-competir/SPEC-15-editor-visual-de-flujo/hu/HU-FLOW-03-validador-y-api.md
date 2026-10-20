---
id: HU-FLOW-03
titulo: Esquema, validador único, API y catálogo de acciones del flujo
spec: SPEC-15
fase: 1
hito: "1"
workstream: Flujo visual
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia]
req: [REQ-FLOW-02]
dependencias: [HU-FLOW-02]
skills: ["backend-design:error-handling-as-design", "backend-design:testing-with-discernment"]
estado: parqueada
---

# HU-FLOW-03 · Esquema, validador único, API y catálogo de acciones del flujo

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-15](../spec.md).

**ID:** HU-FLOW-03

**Título:** Esquema, validador único, API y catálogo de acciones del flujo

**Workstream:** Flujo visual

**Historia:** Como editor del flujo quiero que el sistema me ofrezca solo las acciones de mis habilidades activas y me impida guardar un flujo inválido para no dejar al asistente sin herramientas.

**Por qué importa (valor empresarial):** Un flujo inválido deja al asistente sin poder vender o cobrar. Validar en el backend con una sola regla evita que el panel y el motor discrepen.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FLOW-02

**Dependencias:** [HU-FLOW-02](HU-FLOW-02-flujo-en-agentspec.md)

**Criterios de aceptación (Gherkin):**
- **Catálogo.** Dado mis habilidades activas, cuando pido el catálogo, entonces recibo sus acciones con pack, conexión requerida, confirmación y límites.
- **Validación.** Dado un flujo con más de 20 etapas, una tool inexistente o una etapa vacía, cuando lo guardo, entonces la API lo rechaza con el error por etapa.
- **API.** Dado `GET/PUT /api/v1/admin/flow` (borrador) y `POST /publish`, cuando los uso, entonces respetan permisos y quedan auditados.

**Evidencia / Definición de Terminado:**
- Esquema JSON publicado en OpenAPI; tests del validador con casos límite.

**Riesgos/Notas:**
- Límites actuales del ADR-0054: 20 secciones, 40 tools, 600 caracteres de `purpose`.
