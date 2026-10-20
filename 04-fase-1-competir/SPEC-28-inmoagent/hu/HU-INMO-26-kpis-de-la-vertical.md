---
id: HU-INMO-26
titulo: "KPIs de la vertical"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, ingreso]
req: [REQ-INMO-12]
dependencias: [HU-INMO-20, HU-INMO-24, HU-FWK-07]
skills: ["kpi-dashboard-design", "data:sql-queries", "panel-ui"]
estado: borrador
---

# HU-INMO-26 · KPIs de la vertical

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-26

**Título:** KPIs de la vertical

**Workstream:** Verticales

**Historia:** Como gerente de la inmobiliaria quiero ver los indicadores de búsqueda, visitas, captación y recaudo, para saber si el asistente me está haciendo vender y cobrar más.

**Por qué importa (valor empresarial):** Sin medición no hay renovación del cliente ni caso de estudio para vender la vertical.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-12

**Dependencias:** [HU-INMO-20](HU-INMO-20-oportunidades-y-asesores.md), [HU-INMO-24](HU-INMO-24-mora-e-incremento-del-canon.md), [HU-FWK-07](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-07-descriptor-view.md)

**Criterios de aceptación (Gherkin):**
- **Tablero.** Dado un mes de operación, cuando el gerente abre los KPIs, entonces ve consulta → visita, búsquedas sin resultado, precisión, asistencia, embudo, recaudo a tiempo, mora y captaciones, cada uno con su definición.
- **Consistencia.** Dado el mismo período, cuando se compara con las tablas, entonces cada cifra coincide con la consulta documentada en design.md.

**Evidencia / Definición de Terminado:**
- Vista de KPIs por descriptor; consultas documentadas y probadas sobre tablas del pack (el recaudo usa el espejo de `contratos`).

**Riesgos/Notas:**
- Fase INMO 4 · Arriendos y medición.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
