# SPEC-09 · Diseño

## Camino del dinero (HU-COM-01)

```
crear_pedido(quote_id, …) ─► Order(total calculado por el servidor)
confirmar_pago_pedido(order_id)
   ├─ método online: payment_registry.capability_for_tenant(t).create_link(
   │        reference = order.public_order_number[-rN], amount = order.total)
   │        • reutiliza el link vigente si el total no cambió
   │        • si agregaron ítems: expira el anterior y crea "-r2"
   │        • mínimo del proveedor → BusinessError "monto_bajo_minimo"
   ├─ transferencia: el sistema adjunta las cuentas del negocio (no el LLM)
   └─ contra entrega: queda pendiente de pago (no nace "pagado")
payment.confirmed (outbox) ─► valida monto == order.total y estado permitido ─► pagado
```

## Estados del pedido (HU-COM-05)

| Eje | Estados | Transiciones permitidas |
|---|---|---|
| Pedido | `nuevo → confirmado → en_preparacion → listo → en_camino → entregado`, `cancelado` | Configurables por negocio (un restaurante no usa `en_camino` si solo hay retiro) |
| Pago | `pendiente → pagado`, `rechazado`, `reembolsado` | Un "rechazado" tardío nunca pisa "pagado" |

Cada transición: actualización con guardia (`UPDATE … WHERE estado = previo`), evento `order.*` en el
outbox, aviso al cliente con el texto del negocio (plantilla fuera de 24 h) y alerta al equipo por
permiso. Cancelar libera stock.

## Datos

| Cambio | HU |
|---|---|
| Índice único `(tenant_id, public_order_number)`, prefijo configurable por negocio, sin truncar | [HU-COM-03](hu/HU-COM-03-numeracion-y-datos-por-producto.md) |
| `order_payment_links` (historial de links por pedido con versión) | [HU-COM-01](hu/HU-COM-01-dinero-en-el-servidor.md) |
| `checkout_fields` en la config (por tipo de entrega y de producto) | [HU-COM-03](hu/HU-COM-03-numeracion-y-datos-por-producto.md) |
| `Product.active`, `track_inventory`, imágenes; `OrderItem.notes` | [HU-COM-07](hu/HU-COM-07-catalogo-menus-y-retail.md) |
| `delivery_zones` (tarifa, mínimo, tiempo) y horario de pedidos | [HU-COM-08](hu/HU-COM-08-domicilios.md) |
| `payment_receipts` adjuntos al pedido | [HU-COM-06](hu/HU-COM-06-operacion-de-pagos.md) |

## Contratos de tools (inspirados en `contratos-tools-v3.md` de `agent-sale`)

Todas devuelven `status` de una lista cerrada (nunca texto libre con montos). Ejemplos:
`confirmar_pago_pedido` → `link_pago_disponible | datos_transferencia_enviados | ya_pagado |
monto_bajo_minimo | pedido_no_abierto`; `crear_pedido` → `confirmado | duplicado |
faltan_datos_cliente(missing_fields, existing_data) | monto_alto`.

## ADR

- **ADR "Camino del dinero en comercio"**: el LLM nunca define montos ni referencias; estados y
  transiciones; listas cerradas de `status`.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Cambiar contratos de tools rompe evals existentes | Actualizar golden set en la misma HU |
| Restaurantes con flujos distintos | Transiciones configurables y preset Restaurante |
