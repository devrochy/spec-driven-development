---
id: HU-AOS-33
titulo: "Feedback y propuestas de mejora con aprobación humana"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia]
req: [REQ-AOS-12]
dependencias: [HU-AOS-31]
skills: ["eval-author", "panel-ui"]
estado: borrador
---

# HU-AOS-33 · Feedback y propuestas de mejora con aprobación humana

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-33

**Título:** Feedback y propuestas de mejora con aprobación humana

**Workstream:** Agent OS

**Historia:** Como dueño quiero marcar respuestas malas y recibir propuestas de mejora de frases y textos que pasan por pruebas antes de aprobarlas, para que el asistente mejore sin perder el control.

**Por qué importa (valor empresarial):** Auto-mejora con freno: el sistema propone, las pruebas filtran y una persona decide.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-12

**Dependencias:** [HU-AOS-31](HU-AOS-31-auditor-de-calidad.md)

**Criterios de aceptación (Gherkin):**
- **Marcar.** Dado un turno, cuando lo marca como malo, entonces queda en `turn_feedback` y puede convertirse en prueba.
- **Propuesta acotada.** Dado una propuesta, cuando se genera, entonces solo cambia frases o textos y nunca etapas, datos, acciones, permisos ni presupuestos.
- **Aprobación.** Dado una propuesta con pruebas aprobadas, cuando el master la aprueba, entonces se crea una release candidata.

**Evidencia / Definición de Terminado:**
- `improvement_proposals`; vistas en Calidad; flujo de aprobación.

**Riesgos/Notas:**
- Propuestas de baja calidad: se exigen pruebas antes de mostrarlas.
