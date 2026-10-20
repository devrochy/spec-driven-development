---
id: HU-GTM-10
titulo: Páginas de integraciones, casos de uso y SEO por vertical
spec: SPEC-20
fase: 1
hito: "1"
workstream: GTM
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso]
req: [REQ-COMP-04, REQ-FIX-05]
dependencias: [HU-GTM-05]
skills: ["marketing:seo-audit", "marketing:draft-content", "frontend-design", "web-perf"]
estado: terminada
---

# HU-GTM-10 · Páginas de integraciones, casos de uso y SEO por vertical

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-20](../spec.md).

**ID:** HU-GTM-10

**Título:** Páginas de integraciones, casos de uso y SEO por vertical

**Workstream:** GTM

**Historia:** Como prospecto que busca "asistente de WhatsApp para restaurantes" quiero encontrar una página de SolversHub para mi caso con las integraciones reales para evaluar si me sirve.

**Por qué importa (valor empresarial):** Todos los competidores tienen páginas de integraciones e industrias; el sitemap actual tiene 6 URL. El SEO por vertical es adquisición de bajo costo.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-COMP-04, REQ-FIX-05

**Dependencias:** HU-GTM-05

**Criterios de aceptación (Gherkin):**
- **Integraciones.** Dado la página de integraciones, cuando la reviso, entonces solo lista las que existen y marca "próximamente" el resto.
- **Verticales.** Dado restaurantes, retail, cobranza y negocios con suscripción, cuando busco, entonces cada uno tiene su página con su preset.
- **SEO.** Dado el sitemap, cuando se publica, entonces incluye las páginas nuevas con metadatos y datos estructurados.

**Evidencia / Definición de Terminado:**
- Páginas en `solvershub-landing`; sitemap actualizado.

**Implementada (2026-10-03, PR [landing #3](https://github.com/devrochy/solvershub-landing/pull/3)):** páginas `/integraciones` (hub + detalle) y `/para` (hub + restaurantes/retail/cobranza/suscripciones); sitemap con las rutas nuevas y JSON-LD de migas; Footer enlazado. Claims honestos (lo no disponible, "próximamente").

**Riesgos/Notas:**
- Respetar los claims verificados (HU-GTM-05).
