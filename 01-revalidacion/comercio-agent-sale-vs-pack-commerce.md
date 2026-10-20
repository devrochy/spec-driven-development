# Comercio: `agent-sale` contra `pack-commerce`

Fuente: barrido del 2026-10-01. Prefijos: `AS` = `Proyectos/agent-sale`, `PC` =
`solvershub-backend/packages/pack-commerce/pack_commerce`, `PP` = `…/pack-payments/pack_payments`,
`PS` = `…/pack-subscriptions/pack_subscriptions`, `CORE` = `solvershub-backend/core`.

## En una frase

`pack-commerce` portó el modelo de datos de `agent-sale` (catálogo con variantes, cotizaciones
inmutables, pedidos con dos ejes de estado, promociones, 5 segmentos) y lo mejoró en multi-tenancy,
leads y planes como productos, **pero solo portó la primera mitad del flujo del pedido**: lo que
pasa después de crear el pedido (resolver el pago, cancelar, cambiar dirección, guía, avisos al
cliente, comprobantes, expiración, alertas al equipo) no existe.

## Donde `pack-commerce` ya está adelante (se conserva)

- Seguridad multi-tenant: RLS forzado, config y numeración por negocio.
- Leads: `crear_lead`, `calificar_lead`, `actualizar_lead` y API pública de intake con secreto,
  Turnstile y límite de tasa (`PC/skills.py:227-392`, `PC/api.py:115-226`).
- Planes como productos con activación de la suscripción al pagar (`PC/module.py:1193-1244`).
- Entradas tolerantes (SKU o id), DSL de claims de cierre por negocio (ADR-0025), confirmación
  humana del core, horario del core.

## Defectos encontrados (D1–D18)

| ID | Dónde | Defecto e impacto | Tamaño | HU |
|---|---|---|---|---|
| **D1** | `PP/skills.py:52-129`, `PC/module.py:1149-1191` | **El monto y la referencia del link de pago los pone el LLM.** Tras agregar ítems se devuelve el link viejo; `payment.confirmed` no valida el monto; un "rechazado" tardío puede pisar "pagado" | S | [HU-COM-01](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md) |
| **D2** | `PC/module.py:1254-1277` | Reproducido: **todo monto ≥ 1.000.000 se bloquea** (`1.5e+06`); `$15` pasa si se conoce `150000`; `$12.50` se bloquea; solo detecta `$` | S | [HU-COM-02](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md) |
| **D3** | `CORE/orchestrator/loop.py:466-487`, `PC/module.py:1316-1321` | El chequeo de cierre cuenta llamadas históricas y fallidas: "pedido confirmado" pasa tras cualquier intento anterior | S | [HU-COM-02](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md) |
| **D4** | `PC/models.py:226-229`, `PC/skills.py:1388-1394` | **Los números de pedido se truncan a partir de 10.000**, sin índice único; el prefijo `OC-` es igual para todos los negocios | S | [HU-COM-03](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-03-numeracion-y-datos-por-producto.md) |
| D5 | `PC/jobs.py:139-146` | La ventana de seguimiento de cotizaciones es imposible (`< now-20h AND > now-3h`): nunca envía | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| D6 | `PC/jobs.py:67-81` | La ventana de seguimiento de leads queda vacía con el valor por defecto: nunca envía | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| D7 | `PC/jobs.py:96-108,156-164` | Se marca "enviado" aunque no se envió; una plantilla mala de un negocio aborta el cron para todos | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| D8 | `PC/skills.py:1287-1302`, `CORE/mcp/host.py:147-152` | Una plantilla de mensaje editada por el negocio puede lanzar `KeyError`, y el core **auto-deshabilita el pack** | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md), [HU-ARCH-18](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-18-errores-de-negocio-no-apagan-packs.md) |
| D9 | `PC/admin_api.py:684-703` | Cualquier estado pasa a cualquier otro; sin liberar stock; sin estado de pago | S | [HU-COM-05](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md) |
| D10 | `PC/skills.py:1449-1463` | Descuento de stock no atómico: sobreventa con pedidos concurrentes | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| D11 | `PC/skills.py:520-521` | Se envía el stock exacto al LLM | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| D12 | `PC/skills.py:1052-1077` | Se ignora la bandera de subcategorías; el ítem gratis se aproxima con dinero | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| D13 | `PC/skills.py:131-137` | Segmentación distinta a la acordada (1 pedido = "ocasional") | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| D14 | `PC/admin_api.py:75-89` | El KPI de pedidos llega como máximo a 5 | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| D15 | `PC/admin_api.py:330-374` | Las categorías de la API no validan ciclos ni hijos al borrar | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| D16 | `PC/module.py:1233`, `PS/module.py:43-44`, `PS/jobs.py:51-52` | COP fijo en la activación de planes; siempre +30 días aunque el plan sea anual | S | HU-SUB-04 |
| **D17** | `PC/skills.py:220-223,1200-1210` | **Datos de domicilio obligatorios aun para retiro y para planes**; se guardan en memoria sin consentimiento | S | [HU-COM-03](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-03-numeracion-y-datos-por-producto.md) |
| D18 | `PC/skills.py:61-62`, `PC/jobs.py:157` | Dinero formateado como `$60,000` con `$` fijo (en Colombia es `$60.000`); ignora el símbolo de la config | S | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |

## Ideas de contrato que vale la pena portar

Principalmente de `AS/docs/fase-15-datos-cliente-flujo-pedidos/contratos-tools-v3.md`:

1. **Listas cerradas de `status`** en cada resultado, sin errores en texto libre (ya hubo un
   incidente en que un texto de error con "$150.000" disparó el guardrail de montos).
2. **Captura progresiva**: `customer_data` opcional; devolver `faltan_datos_cliente` con
   `existing_data` y `missing_fields`; guardar solo con `save_permanently`.
3. **`confirmar_pago_pedido(order_id)`**: reemplaza el `amount` y `reference` que hoy pone el LLM.
4. `agregar_item_pedido` que regenera el link; `cancelar_pedido` con aprobación si ya está pagado;
   `actualizar_datos_entrega`; `cambiar_metodo_pago`.
5. `consultar_estado_pedido` con guía, transportadora y tiempo estimado; `consultar_inventario` con
   `disponible` (booleano) en vez del stock.
6. Contexto inyectado por el orquestador: llave de idempotencia derivada del id del mensaje
   (`ToolContext.message_id`) y `monto_alto` tratado como estado que el core escala.

## Propuestas ordenadas por valor/esfuerzo

| # | Propuesta | Tamaño | Restaurante go-live | Retail go-live | HU |
|---|---|---|---|---|---|
| 1 | Camino del dinero en el servidor | S | Sí, si hay pagos en línea | Sí | [HU-COM-01](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md) |
| 2 | Guardrails correctos (D2, D3) | S | Sí | Sí | [HU-COM-02](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md) |
| 3 | Barrido D4–D18 | S c/u | Sí | Sí | [HU-COM-03](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-03-numeracion-y-datos-por-producto.md), [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) |
| 4 | Campos de checkout configurables + captura progresiva | S–M | Sí | Sí | [HU-COM-03](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-03-numeracion-y-datos-por-producto.md) |
| 5 | Máquina de estados + avisos + eventos `order.*` | M | Sí | Sí | [HU-COM-05](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md) |
| 6 | Operación de pagos: marcar pagado/rechazado; comprobante adjunto; OCR | S → M → L | Sí (manual) | Sí | [HU-COM-06](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-06-operacion-de-pagos.md), [HU-MEDIA-05](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-05-ocr-comprobantes.md) |
| 7 | Catálogo para menús y retail | M | Sí (disponibilidad, notas, fotos) | Sí (variantes, importación) | [HU-COM-07](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-07-catalogo-menus-y-retail.md) |
| 8 | Domicilio: tarifa, zonas, mínimo, tiempo, horario de pedidos | M | Sí, si hay domicilio | Tarifa plana | [HU-COM-08](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-08-domicilios.md) |
| 9 | Tools para modificar el pedido | S–M | Cancelar | Sí | [HU-COM-09](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-09-modificar-pedido.md) |
| 10 | Proactividad v2 | M | Expiración | Después | [HU-COM-10](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-10-proactividad-v2.md) |
| 11 | Promociones v2 | M | Después | Después | [HU-COM-11](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-11-promociones-v2.md) |
| 12 | KPIs y reporte al equipo | S–M | Básico | Básico | [HU-COM-12](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-12-kpis-de-ventas.md) |
| 13 | Búsqueda y recomendaciones | M | Después | Recomendado | [HU-COM-13](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-13-busqueda-y-recomendaciones.md) |
| 14 | Varias sucursales | L | Después | Después | [HU-COM-16](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-COM-16-multisucursal.md) |
| 15 | Tool siguiente forzada en el core | L | Después | Después | [HU-ARCH-26](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md) |
| 16 | Vínculo lead ↔ pedido | S | Después | Después | [HU-COM-14](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-14-lead-y-pedido.md) |

**Dependencias del core**: enviar plantillas aprobadas ([HU-ARCH-13](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md)), eventos de comercio durables
(HU-SUB-03), notificaciones al equipo por permiso ([HU-UI-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-13-cuenta-y-notificaciones.md) / [HU-COM-05](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md)), media entrante
([SPEC-04](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/spec.md)), guardrails que distingan el turno actual ([HU-COM-02](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md)), `ToolContext.message_id`
([HU-ARCH-12](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md)) y horario accesible para los packs ([HU-COM-08](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-08-domicilios.md)).

## Lo que **no** se porta

| Elemento de `agent-sale` | Por qué no |
|---|---|
| `settings` de un solo tenant y la eliminación de `tenant_id` (ADR-032, migraciones 0035–0036) | Viola la invariante 1 |
| Prompts en código (`systemPrompt.ts`, `toneBlocks.ts`, prompts de visión y OCR) | Invariante 3: van a playbooks |
| Lo específico de motos: razón "compatibilidad técnica", prompt de visión de motos, `allies` obligatorio | No es genérico |
| Nombres de plantilla fijos y la coreografía de 3 botones | Se porta el patrón (claves de plantilla en la config + texto de respaldo) |
| Contra entrega que nace "pagado" | Valor por defecto equivocado, ya copiado en `PC/skills.py:1243`: se deshace |
| Columnas y mínimo de Wompi dentro de comercio | Comercio sigue agnóstico vía `PaymentCapability` |
| Mensajes de texto libre a los teléfonos del equipo, polling de Twilio, node-cron | Fallan fuera de 24 h; el core ya tiene Celery beat y webhooks de estado |
| Guardrail de stock por regex ("quedan N") | Mejor no enviar el stock al LLM |
| `promo_code` que no hace nada | Cupones reales ([HU-COM-11](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-11-promociones-v2.md)) o nada |
| Vista de asesor `/asesor/:token` | El core ya tiene escalaciones en el panel |
| Cédula obligatoria en texto plano | Opcional por negocio y tratada como dato personal |
