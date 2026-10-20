---
id: HU-UI-04
titulo: Calidad del panel con tests en CI y control de deriva de la API
spec: SPEC-10
fase: 0
hito: 0B
workstream: UX/Onboarding
prioridad: P0
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-UX-06]
dependencias: []
skills: ["backend-design:testing-with-discernment", "built-in-browser", "web-perf", "panel-ui"]
estado: en-curso
---

# HU-UI-04 · Calidad del panel con tests en CI y control de deriva de la API

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-10](../spec.md).

**ID:** HU-UI-04

**Título:** Calidad del panel con tests en CI y control de deriva de la API

**Workstream:** UX/Onboarding

**Historia:** Como responsable del panel quiero que los tests corran en cada PR, que los tipos de la API no se desalineen del backend y que la accesibilidad se verifique sola para que las mejoras no rompan lo que ya funciona.

**Por qué importa (valor empresarial):** El panel tiene ~16 mil líneas y 12 tests que el CI no corre: cada cambio es una apuesta. Con una sola persona y agentes de IA escribiendo código, los tests automáticos son la única red de seguridad.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-UX-06

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Tests en CI.** Dado un PR del panel, cuando corre el CI, entonces ejecuta `npm run test` y falla si un test falla.
- **Componentes.** Dado los componentes base (tabla, formulario de schema, kit de feedback), cuando se prueban con Testing Library, entonces cubren sus estados principales.
- **Deriva de tipos.** Dado un cambio en `openapi.json` del backend, cuando los tipos del panel no se regeneraron, entonces el CI falla con la diferencia.
- **Accesibilidad.** Dado las páginas principales, cuando corre axe, entonces no hay errores críticos.

**Evidencia / Definición de Terminado:**
- `ci.yml` actualizado; `vitest.config.mts` con jsdom para componentes; reporte de cobertura.

**Riesgos/Notas:**
- El smoke E2E entre repos es de [HU-ARCH-09](../../SPEC-01-produccion-segura/hu/HU-ARCH-09-release-y-e2e-entre-repos.md).
