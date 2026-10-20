---
id: HU-UX-03
titulo: Ayuda contextual y lenguaje claro
spec: SPEC-12
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, operacion]
req: [REQ-UX-03]
dependencias: [HU-UX-01]
skills: ["frontend-design", "marketing:brand-review", "panel-ui"]
estado: terminada
---

# HU-UX-03 · Ayuda contextual y lenguaje claro

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-12](../spec.md).

**ID:** HU-UX-03

**Título:** Ayuda contextual y lenguaje claro

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero una explicación breve de cada sección y de cada campo difícil, en mi idioma y sin jerga, para configurar sin llamar a soporte.

**Por qué importa (valor empresarial):** Hoy se ven "Fernet", ".env", "WABA" y rutas de API. Cada término sin explicar es un ticket o un abandono; la ayuda en contexto es la forma más barata de soporte.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-03

**Dependencias:** [HU-UX-01](HU-UX-01-adr-arquitectura-de-informacion.md)

**Criterios de aceptación (Gherkin):**
- **¿Qué es esto?** Dado cada sección principal, cuando pulso "¿Qué es esto?", entonces un modal explica para qué sirve y qué hacer primero.
- **Tooltip accesible.** Dado un campo con ayuda, cuando lo enfoco con teclado o lo toco en el celular, entonces veo la ayuda (no solo con `title`).
- **Sin jerga.** Dado los textos del panel, cuando se revisan contra el glosario, entonces no aparecen términos técnicos sin explicación.

**Evidencia / Definición de Terminado:**
- Componente `Tooltip`; textos en `lib/copy.ts`; revisión de textos con checklist.

**Implementada (2026-10-03, PR [panel #18](https://github.com/devrochy/solvershub-panel/pull/18)):** `Tooltip` accesible (teclado/táctil), `ColumnInfo` sin depender de `title`, `lib/copy.ts` con "¿Qué es esto?" y primeros pasos por sección (sin jerga) y `SectionHelpButton` en el `PageHeader`; 32 tests del panel.

**Riesgos/Notas:**
- Sin i18n completo todavía; el idioma y la moneda salen del negocio.
