---
id: HU-SH-09
titulo: De la landing al asistente con atribución
spec: SPEC-07
fase: 0
hito: 0B
workstream: GTM
prioridad: P0
critico: false
estimacion: S
impacto: [ingreso]
req: [REQ-SH-07, REQ-COMP-07]
dependencias: [HU-SH-01]
skills: ["backend-design:data-modeling-discipline", "marketing:performance-report"]
estado: borrador
---

# HU-SH-09 · De la landing al asistente con atribución

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-07](../spec.md).

**ID:** HU-SH-09

**Título:** De la landing al asistente con atribución

**Workstream:** GTM

**Historia:** Como responsable de marketing quiero saber de qué campaña o página viene cada prospecto que habla con el asistente para invertir en los canales que traen clientes.

**Por qué importa (valor empresarial):** Sin atribución no se puede calcular el costo de adquisición por canal ni decidir dónde invertir el presupuesto de marketing (Fase 1, GTM-07). Es barato de hacer y su valor crece con cada campaña.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** S

**REQ mapeados:** REQ-SH-07, REQ-COMP-07

**Dependencias:** [HU-SH-01](HU-SH-01-tenant-reproducible.md)

**Criterios de aceptación (Gherkin):**
- **UTM al lead.** Dado un enlace "Habla con el agente" con UTM, cuando el prospecto escribe, entonces el lead guarda fuente, medio y campaña.
- **Formulario.** Dado el formulario de la landing, cuando se envía, entonces el lead llega con su UTM y el asistente continúa la conversación por WhatsApp.
- **Reporte.** Dado el panel del tenant `solvershub`, cuando filtro por campaña, entonces veo leads, demos y ventas por fuente.

**Evidencia / Definición de Terminado:**
- Cambio en la landing y en el intake de commerce; filtro en Clientes.

**Riesgos/Notas:**
- El texto prellenado del enlace de WhatsApp lleva un código corto, no la UTM completa.
