# SPEC-09 · Comercio confiable (barrido `agent-sale` → `pack-commerce`)

> Estado SDD: Diseño aprobado · Fase 0 · Hitos 0A (COM-01 a 03) y 0B (COM-04 a 09) · Workstream Comercio y suscripciones

## Problema

El barrido del 2026-10-01 ([comercio-agent-sale-vs-pack-commerce.md](../../01-revalidacion/comercio-agent-sale-vs-pack-commerce.md))
encontró 18 defectos confirmados y una mitad del flujo del pedido sin portar:

- **D1**: el monto y la referencia del link de pago los pone el LLM; tras agregar ítems se reutiliza el
  link viejo; el webhook no valida el monto.
- **D2**: el guardrail de montos bloquea todo valor ≥ 1.000.000 (no se puede vender Empresarial).
- **D3**: el chequeo de cierre cuenta llamadas viejas o fallidas.
- **D4**: los números de pedido colisionan desde el 10.000.
- **D17**: se exigen datos de domicilio para planes y retiros, y se guardan sin consentimiento.
- D5–D16 y D18: crons que nunca envían, plantillas que tumban el pack, estados sin reglas, stock no
  atómico, stock exacto enviado al LLM, promociones, segmentos, KPIs, categorías y formato de moneda.
- Falta todo lo posterior al pedido: avisos por estado, marcar pagos a mano, comprobantes, cancelar,
  cambiar dirección, guía, expiración, alertas al equipo.

## Por qué importa (valor empresarial)

Comercio es el mercado grande (tiendas, restaurantes) y el canal por el que SolversHub vende sus
propios planes. **Un asistente que cobra un monto inventado o confirma un pedido inexistente es un
riesgo legal y de reputación inaceptable.** Arreglar el camino del dinero es también lo que permite
afirmar "IA confiable" frente a la competencia.

## Alcance

| HU | Qué | Hito |
|---|---|---|
| [HU-COM-01](hu/HU-COM-01-dinero-en-el-servidor.md) ★ | El dinero se calcula en el servidor (D1) | 0A |
| [HU-COM-02](hu/HU-COM-02-guardrails-correctos.md) ★ | Guardrails correctos (D2, D3) | 0A |
| [HU-COM-03](hu/HU-COM-03-numeracion-y-datos-por-producto.md) ★ | Numeración y datos según el tipo de producto (D4, D17) | 0A |
| [HU-COM-04](hu/HU-COM-04-barrido-de-defectos.md) | Barrido de defectos D5–D16 y D18 | 0B |
| [HU-COM-05](hu/HU-COM-05-estados-del-pedido.md) | Máquina de estados del pedido, avisos y eventos | 0B |
| [HU-COM-06](hu/HU-COM-06-operacion-de-pagos.md) | Operación de pagos y comprobantes | 0B |
| [HU-COM-07](hu/HU-COM-07-catalogo-menus-y-retail.md) | Catálogo para menús y retail | 0B |
| [HU-COM-08](hu/HU-COM-08-domicilios.md) | Domicilios | 0B |
| [HU-COM-09](hu/HU-COM-09-modificar-pedido.md) | Tools para modificar el pedido | 0B |

## Decisiones

### D-SPEC-09-1 · Generación del link de pago de un pedido

| Opción | Pros | Contras |
|---|---|---|
| **A. Tool `confirmar_pago_pedido(order_id)`: el servidor genera o reutiliza el link desde `Order.total` vía `payment_registry` y lo regenera si el total cambió** | El LLM nunca toca el dinero; proveedor agnóstico | Cambia el contrato de la tool actual |
| B. Mantener `generar_link_pago(reference, amount)` y validar el monto contra el pedido | Cambio menor | El LLM sigue eligiendo la referencia; validación frágil |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): `confirmar_pago_pedido(order_id)` con el link armado en el servidor.

### D-SPEC-09-2 · Datos del cliente en el checkout

| Opción | Pros | Contras |
|---|---|---|
| **A. Campos configurables por negocio y por tipo de entrega o producto, con captura progresiva (`faltan_datos_cliente`) y guardado solo con consentimiento** | Restaurante, retail y planes piden lo justo; cumple Habeas Data | Más configuración |
| B. Campos fijos obligatorios (hoy) | Simple | Planes y retiros piden dirección; datos sin consentimiento |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): campos configurables por negocio y tipo de entrega, captura progresiva y consentimiento.

## Fuera de alcance

Proactividad v2, promociones v2, KPIs avanzados, búsqueda, modificadores y sucursales ([SPEC-18](../../04-fase-1-competir/SPEC-18-pack-commerce-v2/spec.md) y
[SPEC-22](../../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/spec.md)). La lista de lo que **no** se porta de `agent-sale` está en la re-validación.

## Métricas de éxito

- 0 links de pago con monto distinto al total del pedido.
- Golden set de comercio ≥95 % ([HU-ARCH-16](../SPEC-02-agente-confiable/hu/HU-ARCH-16-golden-set-comercio.md)).
- Primer restaurante en producción con pedidos, domicilio y pagos manuales (Hito 0B).

## Requerimientos cubiertos

REQ-COM-01 a REQ-COM-05, REQ-PLUS-01.
