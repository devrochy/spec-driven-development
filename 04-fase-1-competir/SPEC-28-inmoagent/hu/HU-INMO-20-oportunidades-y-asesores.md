---
id: HU-INMO-20
titulo: "Oportunidades, asesores y leads"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, operacion]
req: [REQ-INMO-07]
dependencias: [HU-INMO-07, HU-INMO-10]
skills: ["panel-ui", "db-migration", "agentcore-conventions"]
estado: borrador
---

# HU-INMO-20 · Oportunidades, asesores y leads

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-20

**Título:** Oportunidades, asesores y leads

**Workstream:** Verticales

**Historia:** Como gerente quiero ver cada cliente como una oportunidad con etapa y asesor, asignada sola por zona o por rotación, para no perder negocios.

**Por qué importa (valor empresarial):** Sin pipeline, los leads del asistente se pierden entre asesores; con asignación automática el relevo llega a la persona correcta.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-07

**Dependencias:** [HU-INMO-07](HU-INMO-07-escalamiento-al-responsable.md), [HU-INMO-10](HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md)

**Criterios de aceptación (Gherkin):**
- **Asignación.** Dado un cliente nuevo que busca en Chapinero, cuando se crea la oportunidad, entonces se asigna al asesor de esa zona, o por rotación si hay varios.
- **Etapas.** Dado una visita confirmada, cuando se registra, entonces la oportunidad pasa a "visita" y queda un evento en `oportunidad_eventos`.
- **Leads globales.** Dado la vista global de leads, cuando se abre, entonces muestra la etapa y el asesor de la vertical (ADR-0056).

**Evidencia / Definición de Terminado:**
- Tablas de oportunidades; asesores con zonas; tablero en el panel; enrutamiento de escalamientos con [HU-INMO-07](HU-INMO-07-escalamiento-al-responsable.md).

**Riesgos/Notas:**
- Fase INMO 3 · Captación y visitas.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
