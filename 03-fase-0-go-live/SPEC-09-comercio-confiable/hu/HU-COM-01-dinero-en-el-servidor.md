---
id: HU-COM-01
titulo: El dinero del pedido se calcula en el servidor
spec: SPEC-09
fase: 0
hito: 0A
workstream: Comercio y suscripciones
prioridad: P0
critico: true
estimacion: S
impacto: [ingreso, confianza]
req: [REQ-COM-01, REQ-PLUS-01]
dependencias: []
skills: ["new-tool", "backend-design:idempotency-and-side-effects", "/codex:adversarial-review", "eval-author"]
ola: 1
estado: terminada
---

# HU-COM-01 · El dinero del pedido se calcula en el servidor

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-09](../spec.md) (D-SPEC-09-1).

**ID:** HU-COM-01

**Título:** El dinero del pedido se calcula en el servidor

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de una tienda quiero que el link de pago de un pedido siempre tenga el total exacto calculado por el sistema y se actualice si el cliente agrega productos para que nunca se cobre un monto equivocado.

**Por qué importa (valor empresarial):** Hoy el LLM elige el monto y la referencia del link (`pack_payments/skills.py:52-129`) y, tras agregar ítems, se reutiliza el link viejo. Un cobro equivocado es un reclamo, una devolución y, si es a la baja, dinero perdido. Es el defecto más grave del comercio.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-COM-01, REQ-PLUS-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Monto del servidor.** Dado un pedido de COP 185.000, cuando el asistente llama `confirmar_pago_pedido(order_id)`, entonces el link es por COP 185.000 con la referencia del pedido, sin que el LLM pase monto ni referencia.
- **Ítems agregados.** Dado un pedido con link vigente, cuando el cliente agrega un producto, entonces el link anterior se expira y se crea uno nuevo (`-r2`) por el total nuevo.
- **Webhook validado.** Dado un `payment.confirmed` con un monto distinto al total, cuando llega, entonces el pedido no se marca pagado y se alerta al negocio.
- **Rechazo tardío.** Dado un pedido pagado, cuando llega un "rechazado" tardío, entonces no cambia el estado.
- **Mínimo del proveedor.** Dado un total bajo el mínimo del proveedor, cuando se pide el link, entonces la tool responde `monto_bajo_minimo` (sin apagar el pack) y el asistente ofrece transferencia.

**Evidencia / Definición de Terminado:**
- Tool `confirmar_pago_pedido` y retiro de `generar_link_pago` del flujo de comercio; tests de los cinco escenarios; ADR "Camino del dinero en comercio".

**Implementada (2026-10-02, PR #183 en `devrochy/agent-core`):**
- Migración `crm_0007`: `Order.payment_reference`, `payment_link_url`, `payment_link_version`.
- Tool `confirmar_pago_pedido(order_id)`: arma el link desde `Order.total` vía `payment_registry` del core; el LLM solo pasa el `order_id`.
- `agregar_item_pedido` sube la versión → el link viejo (`OC-0001`) deja de valer y el próximo es `-r1`.
- Webhook: `payment.confirmed` con monto distinto no marca pagado; `rejected` tardío no cambia un pedido pagado.
- Monto bajo el mínimo → error de negocio `monto_bajo_minimo` (no apaga el pack).
- Playbook `ventas.md` y guardrail de completion actualizados; ADR-0087.
- 5 tests de integración (los 5 escenarios Gherkin) pasan; `pytest` 672 passed (unit); gate de CI verde.

**Observación:** la numeración `order_seq` colisiona si un tenant ya tenía pedidos y su contador se reinicia (defecto preexistente, `test_numeracion_independiente_por_tenant`); pertenece a [HU-COM-03](HU-COM-03-numeracion-y-datos-por-producto.md).

**Riesgos/Notas:**
- Es dependencia del journey E2E de suscripciones (HU-SUB-12): el plan se paga como un pedido.
