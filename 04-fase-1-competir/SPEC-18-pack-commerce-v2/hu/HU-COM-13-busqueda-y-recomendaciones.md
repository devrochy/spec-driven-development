---
id: HU-COM-13
titulo: Búsqueda tolerante y recomendaciones comprados juntos
spec: SPEC-18
fase: 1
hito: "1"
workstream: Comercio y suscripciones
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, calidad_ia]
req: [REQ-COM-07]
dependencias: [HU-COM-07]
skills: ["backend-design:query-discipline", "/backend-design:explain-this-query"]
estado: parqueada
---

# HU-COM-13 · Búsqueda tolerante y recomendaciones "comprados juntos"

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-18](../spec.md).

**ID:** HU-COM-13

**Título:** Búsqueda tolerante y recomendaciones comprados juntos

**Workstream:** Comercio y suscripciones

**Historia:** Como cliente quiero que el asistente encuentre lo que busco aunque escriba sin tildes o con otro nombre, y que me sugiera lo que otros compraron junto, para comprar más fácil.

**Por qué importa (valor empresarial):** En catálogos grandes, una búsqueda que no encuentra es una venta perdida; la recomendación aumenta el ticket promedio sin configuración.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-COM-07

**Dependencias:** [HU-COM-07](../../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-07-catalogo-menus-y-retail.md)

**Criterios de aceptación (Gherkin):**
- **Sin tildes.** Dado "cafe", cuando busco, entonces encuentra "Café".
- **Sinónimos.** Dado sinónimos del negocio, cuando busco "gaseosa", entonces encuentra "refresco".
- **Comprados juntos.** Dado un producto, cuando el asistente recomienda, entonces sugiere los más comprados con él y en stock.

**Evidencia / Definición de Terminado:**
- Extensiones `unaccent` y `pg_trgm`; índices; tests.

**Riesgos/Notas:**
- Embeddings opcionales en la Fase 2.
