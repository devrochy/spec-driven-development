---
id: HU-AOS-24
titulo: "Editor de agentes desde plantillas"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-AOS-05, REQ-AOS-13]
dependencias: [HU-AOS-16, HU-FWK-08]
skills: ["panel-ui", "frontend-design", "customizer"]
estado: terminada
---

# HU-AOS-24 · Editor de agentes desde plantillas

> Estado SDD: Terminada (2026-10-18, tanda 7) — [SPEC-26](../spec.md).

**ID:** HU-AOS-24

**Título:** Editor de agentes desde plantillas

**Workstream:** Agent OS

**Historia:** Como dueño no técnico quiero crear un agente desde una plantilla de mis habilidades, marcar sus superpoderes y revisar sus frases, para tener un especialista sin ayuda técnica.

**Por qué importa (valor empresarial):** "Agent OS" solo se vende si un dueño lo configura solo: es la diferencia frente a construir agentes a mano.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-05, REQ-AOS-13

**Dependencias:** [HU-AOS-16](HU-AOS-16-habilidades-con-procedimientos-y-scope.md), [HU-FWK-08](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-08-formulario-de-schema-v2.md)

**Criterios de aceptación (Gherkin):**
- **Desde plantilla.** Dado la habilidad Comercio instalada, cuando elige la plantilla Ventas, entonces el borrador trae superpoderes y frases sugeridas.
- **Validación.** Dado un superpoder sin las frases mínimas, cuando intenta publicar, entonces ve el error junto al campo y no un JSON.
- **Usabilidad.** Dado 3 dueños no técnicos, cuando crean y publican un agente, entonces lo logran en menos de 15 minutos sin ayuda.

**Evidencia / Definición de Terminado:**
- Editor por pasos; API de borradores; prueba de usabilidad documentada.

**Implementada (2026-10-18, tanda 7):** editor de agentes. PR [core #473](https://github.com/devrochy/agent-core/pull/473) + [panel #81](https://github.com/devrochy/solvershub-panel/pull/81).

**Riesgos/Notas:**
- Demasiadas opciones: lo avanzado queda plegado.
- Pendiente del ciclo de pruebas 2026-10-13 ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)): el selector de modelo muestra el costo estimado **por mensaje** además del de 1000 turnos (`GET /admin/agent-models`). El proveedor sigue siendo el del negocio mientras el dueño no decida D-SPEC-31-3 ([SPEC-31](../../SPEC-31-mejoras-del-ciclo-de-pruebas/spec.md)). El guion de preguntas por plantilla es [HU-AOS-48](../../SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-AOS-48-onboarding-con-guion-por-agente.md).
