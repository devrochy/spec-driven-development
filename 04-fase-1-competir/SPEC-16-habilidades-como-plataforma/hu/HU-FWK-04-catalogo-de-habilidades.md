---
id: HU-FWK-04
titulo: Catálogo de habilidades con metadatos
spec: SPEC-16
fase: 1
hito: "1"
workstream: Framework/Plugins
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-FWK-04, REQ-PLUS-05]
dependencias: []
skills: ["new-pack", "agentcore-conventions"]
estado: terminada
---

# HU-FWK-04 · Catálogo de habilidades con metadatos

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-16](../spec.md).

**ID:** HU-FWK-04

**Título:** Catálogo de habilidades con metadatos

**Workstream:** Framework/Plugins

**Historia:** Como dueño de un negocio quiero un catálogo de habilidades con lo que hace cada una, qué necesita y desde qué plan está disponible para elegir qué agregarle a mi asistente.

**Por qué importa (valor empresarial):** Hoy las tarjetas muestran `id · versión` en monoespaciado. Un catálogo claro es la vitrina de la expansión: cada habilidad activada es valor percibido y razón para subir de plan.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FWK-04, REQ-PLUS-05

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Metadatos.** Dado cada pack, cuando se registra, entonces declara nombre visible, descripción, categoría, conexiones requeridas, plan mínimo, resumen de acciones y guía de configuración.
- **Catálogo.** Dado Habilidades, cuando la abro, entonces veo tarjetas con esa información y el estado (activa, disponible, requiere plan superior).
- **Activar con guía.** Dado una habilidad disponible, cuando la activo, entonces se abre su guía ([HU-UX-05](../../SPEC-12-arquitectura-de-informacion/hu/HU-UX-05-guias-por-habilidad.md)).

**Evidencia / Definición de Terminado:**
- Campos de metadatos en `BaseModule`; API y página del catálogo; tests.

**Implementada (2026-10-03):**
- Backend (PR [#199](https://github.com/devrochy/agent-core/pull/199)): `BaseModule` con `display_name`, `category`, `required_connections`, `min_plan`, `action_summary`, `setup_guide`; los 5 packs los declaran; `/admin/plugins` los expone.
- Panel (PR [#16](https://github.com/devrochy/solvershub-panel/pull/16)): la tarjeta muestra nombre, categoría, descripción, acciones, conexiones y plan.
- Desbloquea FWK-05/06/07/10/11/13 y UX-05.

**Riesgos/Notas:**
- Base del manifiesto ([HU-FWK-05](HU-FWK-05-manifiesto-de-menu.md)) y de las guías.
