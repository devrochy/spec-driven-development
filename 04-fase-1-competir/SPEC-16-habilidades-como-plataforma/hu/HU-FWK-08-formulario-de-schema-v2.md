---
id: HU-FWK-08
titulo: Formulario de configuración por schema v2
spec: SPEC-16
fase: 1
hito: "1"
workstream: Framework/Plugins
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-FWK-05]
dependencias: [HU-UI-01]
skills: ["frontend-design", "built-in-browser"]
estado: terminada
---

# HU-FWK-08 · Formulario de configuración por schema v2

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-16](../spec.md).

**ID:** HU-FWK-08

**Título:** Formulario de configuración por schema v2

**Workstream:** Framework/Plugins

**Historia:** Como dueño de un negocio quiero configurar cada habilidad con un formulario claro, con listas, campos agrupados y errores al lado de cada campo, para no equivocarme ni escribir JSON.

**Por qué importa (valor empresarial):** Cada pack se configura con este formulario: si es confuso, el negocio deja habilidades mal configuradas que luego responden mal a sus clientes.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FWK-05

**Dependencias:** [HU-UI-01](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-01-bugs-visibles.md)

**Criterios de aceptación (Gherkin):**
- **Tipos.** Dado un schema con `anyOf` nulos, enums con etiqueta, arreglos y objetos anidados, cuando se dibuja, entonces cada uno tiene su control.
- **Agrupación.** Dado `x-group` y `x-widget`, cuando se dibuja, entonces los campos se agrupan y usan el control indicado.
- **Errores por campo.** Dado un error del backend en un campo, cuando guardo, entonces aparece junto a ese campo.

**Evidencia / Definición de Terminado:**
- Componente con tests por tipo de campo.

**Implementada (2026-10-03):**
- Panel (PR [#17](https://github.com/devrochy/solvershub-panel/pull/17)): `json-schema-form` v2 con `anyOf` nullable, arrays (una por línea), objetos JSON validados, enums con `x-enumLabels`, `x-widget`, agrupación `x-group` y errores por campo. 9 tests.
- Backend (PR [#200](https://github.com/devrochy/agent-core/pull/200)): `PluginConfigError`/`ApiError` llevan `fields`; el endpoint los devuelve.
- Desbloquea FWK-09.

**Riesgos/Notas:**
- Reemplaza `components/domain/json-schema-form.tsx`.
