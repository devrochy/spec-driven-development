---
id: HU-INMO-29
titulo: "Procedimientos tipados inmobiliarios"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: L
impacto: [calidad_ia, confianza]
req: [REQ-INMO-11]
dependencias: [HU-INMO-25, HU-INMO-27]
skills: ["eval-author", "new-tool", "agentcore-conventions"]
estado: borrador
---

# HU-INMO-29 · Procedimientos tipados inmobiliarios

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-29

**Título:** Procedimientos tipados inmobiliarios

**Workstream:** Verticales

**Historia:** Como negocio quiero que buscar, agendar, captar y pagar sigan procedimientos que el sistema hace cumplir, para que el asistente sea consistente en cada conversación.

**Por qué importa (valor empresarial):** Pasa la vertical del motor v2 a procedimientos verificables (D-SPEC-28-3) sin tirar tablas ni acciones.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-INMO-11

**Dependencias:** [HU-INMO-25](HU-INMO-25-preset-golden-y-journeys.md), [HU-INMO-27](HU-INMO-27-procedimientos-1-1.md)

**Criterios de aceptación (Gherkin):**
- **Linter.** Dado los procedimientos de la tabla de design.md, cuando corre el linter, entonces todas las etapas son alcanzables, toda acción irreversible tiene confirmación y todo monto, distancia o link tiene fuente.
- **Gate.** Dado los escenarios de cada procedimiento, cuando corre el gate, entonces pass^4 ≥ 0,85 por procedimiento.
- **Sin regresión.** Dado los journeys `inmobiliaria` del motor v2, cuando se activan los procedimientos, entonces siguen en verde.

**Evidencia / Definición de Terminado:**
- Procedimientos en el manifiesto del pack; resolvers; escenarios por procedimiento. La visita es la etapa final de `buscar_inmuebles` (o tarea propia si se llega directo), para dejar lugar en la pila.

**Riesgos/Notas:**
- Fase INMO 5 · Agent OS nativo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
