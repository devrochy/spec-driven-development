---
id: HU-AOS-41
titulo: "Auto-mejora asistida: de fallas a versión candidata"
spec: SPEC-27
fase: 2
hito: "2"
workstream: Agent OS
prioridad: P2
critico: false
estimacion: L
impacto: [calidad_ia, operacion]
req: [REQ-AOS-12]
dependencias: [HU-AOS-32, HU-AOS-33]
skills: ["eval-author", "optimizer"]
estado: borrador
---

# HU-AOS-41 · Auto-mejora asistida: de fallas a versión candidata

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-27](../spec.md).

**ID:** HU-AOS-41

**Título:** Auto-mejora asistida: de fallas a versión candidata

**Workstream:** Agent OS

**Historia:** Como dueño quiero que el sistema proponga por sí mismo mejoras de frases y textos a partir de las fallas, con pruebas y canary, y que yo solo apruebe.

**Por qué importa (valor empresarial):** Mejora continua con menos trabajo manual y el mismo control.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-AOS-12

**Dependencias:** [HU-AOS-32](../../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-32-canary-y-auto-rollback.md), [HU-AOS-33](../../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-33-feedback-y-propuestas.md)

**Criterios de aceptación (Gherkin):**
- **Propuesta automática.** Dado fallas agrupadas por superpoder, cuando corre el análisis semanal, entonces se genera una propuesta acotada a frases o textos.
- **Pruebas obligatorias.** Dado una propuesta, cuando no pasa pass^k, entonces se descarta con su motivo.
- **Canary.** Dado una propuesta aprobada, cuando se publica, entonces entra por canary con no-inferioridad.

**Evidencia / Definición de Terminado:**
- Análisis semanal; generación de propuestas; integración con canary.

**Riesgos/Notas:**
- Nunca toca estructura, permisos ni presupuestos.
