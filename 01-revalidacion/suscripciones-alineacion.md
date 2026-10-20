# Suscripciones: alineación con lo implementado (PR #164–#170)

Revisión del 2026-10-01 sobre `origin/develop` `b0f54d3` de `solvershub-backend`. Contrasta lo
construido con las decisiones D-11 a D-14 y deriva D-15 y D-16.

## Hecho y alineado con el plan

| Pieza | Evidencia | HU que lo completa |
|---|---|---|
| Registro `SubscriptionCapability` en el core, mismo molde que `payment_registry` (patrón de D-11) | `core/subscriptions/__init__.py`: protocolo `activate_for_customer(customer_id, variant_id, plan, reference)`, `SubscriptionRegistry.capability_for(enabled)` | HU-SUB-01 |
| Plan = variante de comercio con `billing_period`, `trial_days` y `entitlements`; tool `informar_plan`; `consultar_inventario` expone la recurrencia | Migración `crm_0006`, `pack_commerce/skills.py` | HU-SUB-10 |
| Pedido pagado → `subscription_registry.activate_for_customer` con snapshot del servidor (monto de la variante, no del LLM) y sin imports entre packs | `pack_commerce/module.py::_activate_plans_for_order` | HU-SUB-09 |
| Cargo por período con link vía `PaymentCapability`; `payment.confirmed` marca el cargo pagado; tools `sub_*` y guardrail de claims | `packages/pack-subscriptions/` (`jobs.py::generar_cargos`, cron `15 3 * * *`) | HU-SUB-04, HU-SUB-05 |
| Hook genérico `BaseModule.seed_data` + `seed_pack_plugins` | `core/mcp/types.py` | [HU-FWK-03](../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md) (ningún pack lo implementa todavía) |
| `create_link` con `idempotency_key`, log de eventos y guard de habilitación en cobranza | `72ae35f` | HU-SUB-03 |
| `brand_voice` obligatoria, claims de calendar parametrizables, evals 34–35/35 | — | — |

## Divergencias con las decisiones

1. **Hay dos motores de suscripción.** D-11 decía "cobranza primer proveedor; ADR-0083 diferido". Se
   construyó `pack_subscriptions` como proveedor del registro (ADR-0083) y, en paralelo, un modelo
   `Suscripcion` propio en cobranza (ADR-0082) **sin conexión al registro ni a comercio**. Cada motor
   tiene su modelo, estados y ciclo. El tenant `solvershub` usa `pack_subscriptions` y no tiene
   cobranza. → **D-15**: dos proveedores con un contrato único.
2. **Comercio no es agnóstico al proveedor**: fija `if "pack_subscriptions" not in enabled: return`
   en `pack_commerce/module.py`. → HU-SUB-09.
3. **Los ADR no describen lo construido**: ADR-0082 pone la modalidad en `Cartera`; ADR-0083 habla de
   tablas `Plan/Subscription/Charge` y de una tool `sub_informar_planes` que no existe. → HU-SUB-01.

## Defectos en el código nuevo

| # | Sev. | Defecto | Evidencia | HU |
|---|---|---|---|---|
| 1 | 🔴 | **El pago en línea de una cuota de suscripción de cobranza se pierde.** `_on_payment_confirmed` inserta `Pago(prestamo_id=None)` pero `pack_cobranza_pagos.prestamo_id` sigue NOT NULL (la migración `0013` solo cambió cuotas). El bus traga la excepción: el pago no se registra, la cuota queda pendiente y el link no se marca usado. Sin test de ese camino | `pack_cobranza/pagos.py`, `alembic/versions/0013_suscripciones.py`, `tests/integration/test_cobranza_suscripcion.py` | HU-SUB-02 |
| 2 | 🔴 | **`pack_subscriptions` no gestiona la mora**: el cron pone `estado="activa"` al generar el cargo, se pague o no; nunca pasa a `vencida`; el link no se le envía al cliente (queda en `cargo.referencia`) | `jobs.py::generar_cargos` | HU-SUB-04, HU-SUB-05 |
| 3 | 🟠 | Período fijo de 30 días (`_proximo`) que ignora `periodicidad` (anual) y `trial_dias`; `SubscriptionConfig` no se usa | `module.py`, `jobs.py`, `config.py` | HU-SUB-04 |
| 4 | 🟠 | **Prueba y planes gratis**: solo se activa con un pedido "pagado", así que una prueba exige pagar antes; Free ($0) no se puede pagar por link (mínimo de Wompi) y **nunca se activa**; contra entrega queda "pagado" sin activar | `pack_commerce/module.py` | HU-SUB-06 |
| 5 | 🟠 | Una suscripción viva por cliente; otra compra devuelve la existente **sin cambiar de plan**; no se guarda la `reference` del pedido; no existe cambio de plan | `crear_suscripcion_para` | HU-SUB-07 |
| 6 | 🟠 | `payment.confirmed` no valida el monto contra el cargo ni reactiva una suscripción vencida | — | HU-SUB-04 |
| 7 | 🟠 | Sin outbox: la activación ocurre dentro del handler de pago y, si falla, se pierde | `core/shared/events.py:58-65` | HU-SUB-03 |
| 8 | 🟡 | **El panel no puede ver suscripciones**: la API solo tiene `POST /suscripciones`; `admin_menu` apunta a `/subscriptions/lista`, que no tiene router | `admin_api.py`, `module.py` | HU-SUB-08 |
| 9 | 🟡 | Moneda COP fija en el snapshot; `billing_period` sin validar | — | HU-SUB-10 |
| 10 | 🟡 | Tenant `solvershub` incoherente: Free con prueba 0 y Basic/Premium/Empresarial con 30 días (en `core/billing` solo Free la tiene); secciones de flujo propias etiquetadas `pack_commerce` | `tenants/solvershub/catalog.json`, `flow.json` | HU-SUB-06, [HU-SH-01](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-01-tenant-reproducible.md) |
| 11 | 🟡 | El manifiesto declara la tabla `pack_subscriptions_plans` (eliminada en `0002`) y un campo `plan_id` que no existe | `packages/pack-subscriptions/pyproject.toml:18-21` | HU-SUB-01 |
| 12 | 🔴 | `sub_link_pago` llama a `create_link` **sin capturar `PaymentCapabilityError`** (por ejemplo, monto bajo el mínimo de Wompi): toda excepción no controlada de una tool **auto-deshabilita el pack completo para el negocio** (re-verificado: `core/orchestrator/loop.py:670-675`, ADR-0024). `cob_link_suscripcion` tiene la misma falla. Además crea el cargo con el **mes actual** (riesgo de cobro anticipado o duplicado frente al cron) y cobra durante la prueba | `pack_subscriptions/skills.py:183-244` | [HU-ARCH-18](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-18-errores-de-negocio-no-apagan-packs.md), HU-SUB-04 |
| 13 | 🔴 | **En cobranza el precio de la suscripción lo pone el LLM**: `cob_crear_suscripcion` recibe `valor` como parámetro; la única protección es "No inventes el valor" en la descripción | `pack_cobranza/skills.py` | HU-SUB-15 |

## Sin empezar (esperado)

Aprovisionamiento automático (D-12), dos canales con fuente única (D-13), Embedded Signup real,
onboarding autoservicio, plantillas fuera de 24 h, eventos durables y seeds de calendar ("Demo") y
subscriptions.

## Decisiones que salieron de esta revisión

- **D-15**: dos proveedores con un contrato único; comercio no sabe cuál hay detrás; cada negocio
  elige.
- **D-16**: solo Free tiene prueba (30 días); los planes pagos se cobran desde el primer día; Free se
  activa al confirmar el pedido, sin cobro.
