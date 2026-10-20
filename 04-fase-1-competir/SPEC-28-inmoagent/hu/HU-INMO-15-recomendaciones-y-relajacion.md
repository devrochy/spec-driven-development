---
id: HU-INMO-15
titulo: "Recomendaciones explicadas y relajación de filtros"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, diferenciacion]
req: [REQ-INMO-04]
dependencias: [HU-INMO-14]
skills: ["new-tool", "eval-author", "optimizer"]
estado: borrador
---

# HU-INMO-15 · Recomendaciones explicadas y relajación de filtros

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-15

**Título:** Recomendaciones explicadas y relajación de filtros

**Workstream:** Verticales

**Historia:** Como cliente quiero que el asistente me diga por qué me recomienda cada inmueble y qué ajustar cuando no hay nada, para decidir rápido y no quedarme sin opciones.

**Por qué importa (valor empresarial):** Una lista sin razones parece un portal; una búsqueda sin resultados es una conversación perdida.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-04

**Dependencias:** [HU-INMO-14](HU-INMO-14-busqueda-con-filtros-y-geo.md)

**Criterios de aceptación (Gherkin):**
- **Explicación.** Dado 5 resultados, cuando se presentan, entonces cada uno trae 2 o 3 razones con valores del servidor.
- **Relajación.** Dado 0 resultados, cuando se responde, entonces se ofrecen relajaciones con conteos reales y nunca se relaja lo indispensable.
- **Sin repetir.** Dado un inmueble marcado "no me interesa", cuando se vuelve a buscar, entonces no aparece.

**Evidencia / Definición de Terminado:**
- Scoring y escalera de relajación configurables; tests de cada paso; escenarios golden.

**Riesgos/Notas:**
- Fase INMO 2 · Búsqueda y geo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
