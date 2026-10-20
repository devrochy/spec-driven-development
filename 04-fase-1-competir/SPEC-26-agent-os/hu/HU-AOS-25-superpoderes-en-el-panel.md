---
id: HU-AOS-25
titulo: "Superpoderes en el panel: recorrido, frases, textos y confirmaciones"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion]
req: [REQ-AOS-03, REQ-AOS-13]
dependencias: [HU-AOS-24]
skills: ["panel-ui", "frontend-design"]
estado: borrador
---

# HU-AOS-25 · Superpoderes en el panel: recorrido, frases, textos y confirmaciones

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-25

**Título:** Superpoderes en el panel: recorrido, frases, textos y confirmaciones

**Workstream:** Agent OS

**Historia:** Como dueño quiero ver el recorrido de cada superpoder y ajustar sus frases, textos y confirmaciones, para adaptarlo a mi negocio sin tocar su estructura.

**Por qué importa (valor empresarial):** Reemplaza al editor de flujo de [SPEC-15](../../SPEC-15-editor-visual-de-flujo/spec.md) con algo seguro para no técnicos (P-21).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-03, REQ-AOS-13

**Dependencias:** [HU-AOS-24](HU-AOS-24-editor-de-agentes.md)

**Criterios de aceptación (Gherkin):**
- **Recorrido.** Dado "Contratar un plan", cuando lo abre, entonces ve sus pasos con lo obligatorio y lo de riesgo alto marcados.
- **Ajuste seguro.** Dado un cambio de frases, cuando lo guarda, entonces queda en el borrador del agente y solo llega a los clientes con una release con pruebas.
- **Estructura bloqueada.** Dado un paso con confirmación obligatoria, cuando intenta quitarla, entonces la opción no está disponible.

**Evidencia / Definición de Terminado:**
- Vistas con `ProcedureSteps`; overrides en el AgentSpec v3; tests.

**Riesgos/Notas:**
- El cambio de estructura queda para la Fase 2 ([HU-AOS-45](../../../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md)).
