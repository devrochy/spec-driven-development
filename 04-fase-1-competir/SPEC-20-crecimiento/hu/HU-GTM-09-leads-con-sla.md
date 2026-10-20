---
id: HU-GTM-09
titulo: Leads atendidos en menos de 5 minutos con pipeline
spec: SPEC-20
fase: 1
hito: "1"
workstream: GTM
prioridad: P1
critico: false
estimacion: S
impacto: [ingreso]
req: [REQ-GTM-05]
dependencias: [HU-SH-09]
skills: ["marketing:performance-report", "data:analyze"]
estado: borrador
---

# HU-GTM-09 · Leads atendidos en menos de 5 minutos con pipeline

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-20](../spec.md).

**ID:** HU-GTM-09

**Título:** Leads atendidos en menos de 5 minutos con pipeline

**Workstream:** GTM

**Historia:** Como responsable comercial quiero que cada lead reciba respuesta del asistente en menos de 5 minutos y ver el pipeline por etapa para no perder prospectos.

**Por qué importa (valor empresarial):** La velocidad de primera respuesta es el factor que más convierte un lead B2B. El asistente lo cumple 24/7 si se mide.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-GTM-05

**Dependencias:** [HU-SH-09](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-09-landing-con-atribucion.md)

**Criterios de aceptación (Gherkin):**
- **SLA.** Dado un lead de cualquier canal, cuando llega, entonces el asistente responde en menos de 5 minutos y se mide.
- **Pipeline.** Dado el tenant `solvershub`, cuando abro su pipeline, entonces veo leads por etapa (nuevo, demo, propuesta, ganado, perdido).

**Evidencia / Definición de Terminado:**
- Métrica de primera respuesta; vista de pipeline.

**Riesgos/Notas:**
- —
