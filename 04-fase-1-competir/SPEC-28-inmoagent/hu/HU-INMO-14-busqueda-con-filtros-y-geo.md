---
id: HU-INMO-14
titulo: "Búsqueda con filtros y consultas geoespaciales"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, calidad_ia]
req: [REQ-INMO-02, REQ-INMO-03]
dependencias: [HU-INMO-12, HU-INMO-13]
skills: ["new-tool", "data:sql-queries", "backend-design:query-discipline", "eval-author"]
estado: borrador
---

# HU-INMO-14 · Búsqueda con filtros y consultas geoespaciales

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-14

**Título:** Búsqueda con filtros y consultas geoespaciales

**Workstream:** Verticales

**Historia:** Como cliente quiero buscar por operación, tipo, precio, habitaciones, baños, área, características, texto libre, zona, radio, rango y cercanía, para ver solo lo que me sirve.

**Por qué importa (valor empresarial):** Es el corazón de la vertical: resultados reales y precisos son lo que convierte una consulta en visita.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-INMO-02, REQ-INMO-03

**Dependencias:** [HU-INMO-12](HU-INMO-12-geocodificacion-y-zonas.md), [HU-INMO-13](HU-INMO-13-puntos-de-interes-y-cercanias.md)

**Criterios de aceptación (Gherkin):**
- **Radio.** Dado "a menos de 1 km de la Calle 63", cuando se busca, entonces solo aparecen inmuebles a ≤ 1000 m y cada uno trae su distancia calculada por el servidor.
- **Rango.** Dado "entre 1 y 3 km de mi oficina" con pin, cuando se busca, entonces no aparece ninguno a menos de 1 km.
- **Combinación.** Dado precio, habitaciones, mascotas y cercanía a transporte, cuando se busca, entonces se cumplen todos los filtros duros.
- **Rendimiento.** Dado 10⁴ inmuebles en el negocio, cuando se busca, entonces el p95 en base es < 300 ms.

**Evidencia / Definición de Terminado:**
- Acción `inmo_buscar`; los cuatro ejemplos de design.md como tests; escenarios golden de búsqueda.
- Sin evadir RLS por rendimiento: `EXPLAIN` como `app_runtime` con `app.tenant_id` fijado; si no alcanza, ADR.

**Riesgos/Notas:**
- Fase INMO 2 · Búsqueda y geo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
