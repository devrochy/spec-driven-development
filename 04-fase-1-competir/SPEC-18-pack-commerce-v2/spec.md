# SPEC-18 · Pack-commerce v2

> Estado SDD: Parqueada (2026-10-17, D-35) · Fase 1 · Workstream Comercio y suscripciones

**Parqueada (2026-10-17, [D-35](../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes)):** el comercio v2 se vendía como pack; ahora es la habilidad del agente de Ventas. La proactividad ([HU-COM-10](hu/HU-COM-10-proactividad-v2.md)) pasa a los agentes de back-office ([HU-AOS-30](../SPEC-26-agent-os/hu/HU-AOS-30-agentes-de-back-office.md)) y el flujo de ventas a los procedimientos de comercio ([HU-AOS-07](../SPEC-26-agent-os/hu/HU-AOS-07-procedimientos-de-comercio.md)); promociones, KPIs, búsqueda, lead ↔ pedido y modificadores se retoman cuando un cliente de pago los pida, como habilidad del agente.

## Problema

Después de [SPEC-09](../../03-fase-0-go-live/SPEC-09-comercio-confiable/spec.md) el comercio es confiable, pero le falta el resto del barrido de `agent-sale`:
proactividad (expiración, recordatorios, reenganche, encuestas), promociones v2, KPIs de ventas,
búsqueda y recomendaciones, vínculo lead ↔ pedido y modificadores de menú. La lista de lo que **no**
se porta está en [la re-validación](../../01-revalidacion/comercio-agent-sale-vs-pack-commerce.md#lo-que-no-se-porta).

## Por qué importa (valor empresarial)

Es lo que convierte al asistente de ventas en un vendedor que **recupera** ventas y no solo las
atiende: cada pedido impago recordado, cada carrito reenganchado y cada promoción bien aplicada es
ingreso directo del cliente, y por lo tanto retención de SolversHub.

## Alcance

| HU | Qué |
|---|---|
| [HU-COM-10](hu/HU-COM-10-proactividad-v2.md) | Proactividad v2 |
| [HU-COM-11](hu/HU-COM-11-promociones-v2.md) | Promociones v2 |
| [HU-COM-12](hu/HU-COM-12-kpis-de-ventas.md) | KPIs de ventas y reporte al equipo |
| [HU-COM-13](hu/HU-COM-13-busqueda-y-recomendaciones.md) | Búsqueda y recomendaciones |
| [HU-COM-14](hu/HU-COM-14-lead-y-pedido.md) | Vínculo lead ↔ pedido |
| [HU-COM-15](hu/HU-COM-15-modificadores-y-combos.md) | Modificadores y combos |

## Decisiones

### D-SPEC-18-1 · Motor de búsqueda del catálogo

| Opción | Pros | Contras |
|---|---|---|
| **A. Postgres con `unaccent` + trigram y sinónimos por negocio** | Sin infraestructura nueva; respeta RLS; suficiente para catálogos de miles de productos | Menos tolerante a errores que un motor dedicado |
| B. Embeddings semánticos con pgvector | Entiende intención ("algo para el frío") | Costo por indexación y consulta; la memoria semántica está apagada por defecto |
| C. Motor externo (Meilisearch o Typesense) | Muy rápido y tolerante | Otro servicio y otra copia de datos por negocio |

**Recomendación: A**, con B como mejora opcional en la Fase 2. Estado: ⏳ pendiente.

## Requerimientos cubiertos

REQ-COM-04, REQ-COM-06, REQ-COM-07.
