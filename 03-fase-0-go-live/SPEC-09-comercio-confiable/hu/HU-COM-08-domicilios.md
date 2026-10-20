---
id: HU-COM-08
titulo: Domicilios con tarifa, zonas, mínimo y horario de pedidos
spec: SPEC-09
fase: 0
hito: 0B
workstream: Comercio y suscripciones
prioridad: P0
critico: false
estimacion: M
impacto: [ingreso, operacion]
req: [REQ-COM-05]
dependencias: [HU-COM-03, HU-COM-07]
skills: ["backend-design:data-modeling-discipline", "new-tool"]
estado: borrador
---

# HU-COM-08 · Domicilios con tarifa, zonas, mínimo y horario de pedidos

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-09](../spec.md).

**ID:** HU-COM-08

**Título:** Domicilios con tarifa, zonas, mínimo y horario de pedidos

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de un restaurante quiero definir zonas de domicilio con su tarifa, pedido mínimo y tiempo estimado, y un horario de pedidos distinto al del chat, para que el total que ve el cliente sea el real y no se reciban pedidos cuando la cocina cerró.

**Por qué importa (valor empresarial):** Sin tarifa de domicilio el total del pedido está mal y el guardrail de montos bloquea la tarifa si el LLM la menciona. Un pedido recibido con la cocina cerrada es un cliente molesto. Ni `agent-sale` ni la competencia directa (ClonAI) lo resuelven bien.

**Prioridad:** P0 go-live (Hito 0B, primer restaurante)

**Estimación:** M

**REQ mapeados:** REQ-COM-05

**Dependencias:** [HU-COM-03](HU-COM-03-numeracion-y-datos-por-producto.md), [HU-COM-07](HU-COM-07-catalogo-menus-y-retail.md)

**Criterios de aceptación (Gherkin):**
- **Tarifa por zona.** Dado zonas configuradas, cuando el cliente da su barrio, entonces la tarifa de esa zona se suma como línea del pedido calculada por el servidor.
- **Mínimo.** Dado un pedido bajo el mínimo de la zona, cuando se intenta crear, entonces el asistente informa cuánto falta.
- **Tiempo estimado.** Dado un pedido confirmado, cuando se informa, entonces incluye el tiempo estimado de la zona.
- **Horario de pedidos.** Dado que la cocina cierra a las 21:00 y el chat sigue abierto, cuando llega un pedido a las 21:30, entonces el asistente ofrece programarlo para mañana o tomarlo como reserva.
- **Tarifa plana.** Dado un retail sin zonas, cuando configura una tarifa plana, entonces se aplica a todos los domicilios.

**Evidencia / Definición de Terminado:**
- Config de zonas y horario de pedidos; cálculo en el servidor; tests.

**Riesgos/Notas:**
- `within_business_hours` debe pasar a `core.shared` porque los packs no pueden importar `core.orchestrator`.
