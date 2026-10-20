---
id: HU-UX-01
titulo: ADR de arquitectura de información y glosario del panel
spec: SPEC-12
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: S
impacto: [diferenciacion]
req: [REQ-UX-01]
dependencias: []
skills: ["adr", "doc-coauthoring", "figma-generate-diagram", "panel-ui"]
estado: terminada
---

# HU-UX-01 · ADR de arquitectura de información y glosario del panel

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-12](../spec.md).

**ID:** HU-UX-01

**Título:** ADR de arquitectura de información y glosario del panel

**Workstream:** UX/Onboarding

**Historia:** Como responsable del producto quiero fijar por escrito los grupos del menú, los nombres de cada sección y el glosario para que todas las pantallas, packs y textos usen el mismo idioma de negocio.

**Por qué importa (valor empresarial):** Sin una decisión escrita, cada pack nuevo agrega su propio término técnico y el panel vuelve a ser incomprensible. El glosario alinea panel, asistente, landing y material comercial con el manual de marca.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-UX-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Decisión.** Dado el ADR, cuando se acepta, entonces fija los grupos del menú, el mapeo de rutas y el glosario de la propuesta.
- **Regla para packs.** Dado un pack nuevo, cuando declara su menú, entonces el ADR dice en qué grupo va y cómo se nombra.

**Evidencia / Definición de Terminado:**
- ADR aceptado en `solvershub-panel` y glosario enlazado desde `DESIGN.md`.

**Implementada (2026-10-03):** ADR-0001 en `solvershub-panel/docs/adr/0001-arquitectura-de-informacion.md` (grupos del menú, mapeo de rutas, glosario del manual de marca §9.3), enlazado desde `DESIGN.md`. PR [panel #15](https://github.com/devrochy/solvershub-panel/pull/15).

**Riesgos/Notas:**
- Base: `manual-de-marca.md` §9.3.
