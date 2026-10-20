---
id: HU-INMO-13
titulo: "Puntos de interés y cercanías precalculadas"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion]
req: [REQ-INMO-03]
dependencias: [HU-INMO-10]
skills: ["data:sql-queries", "backend-design:performance-and-scaling"]
estado: borrador
---

# HU-INMO-13 · Puntos de interés y cercanías precalculadas

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-13

**Título:** Puntos de interés y cercanías precalculadas

**Workstream:** Verticales

**Historia:** Como cliente quiero saber qué tan cerca está un inmueble de colegios, transporte, supermercados y parques, para decidir sin abrir un mapa.

**Por qué importa (valor empresarial):** La cercanía a servicios es de los primeros criterios de quien busca vivienda; precalcularla hace la búsqueda rápida y sin costo por consulta.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-03

**Dependencias:** [HU-INMO-10](HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md)

**Criterios de aceptación (Gherkin):**
- **Cercanía.** Dado un inmueble publicado y los POI de su ciudad, cuando corre `recalcular_cercanias`, entonces queda la distancia al POI más cercano de cada categoría dentro de 2 km.
- **Refresco.** Dado un POI que cambia en OSM, cuando corre `refrescar_pois`, entonces se actualiza sin duplicarse.

**Evidencia / Definición de Terminado:**
- Importación OSM por ciudad, crons e índices; tiempo de cálculo medido.

**Riesgos/Notas:**
- Fase INMO 2 · Búsqueda y geo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
