# Brechas del objetivo: SolversHub vende, cobra y da de alta solo

**Objetivo del cliente**: configurar el tenant `solvershub` como el asistente de SolversHub, que
agenda una demo, vende un plan (producto de `pack-commerce`) y crea una suscripción que genera los
cobros, todo **parametrizable** para que cualquier otro asistente lo replique con los mismos packs.

## El recorrido completo y su estado

| # | Paso | Estado al 2026-10-01 | Brecha principal | HU |
|---|---|---|---|---|
| 1 | Llega un prospecto (WhatsApp o landing) → `crear_lead` / intake | ✅ Existe | Sin atribución UTM | [HU-SH-09](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-09-landing-con-atribucion.md) |
| 2 | Demo: `list_appointment_types` → `check_availability` → `create_calendar_event` | ✅ Funciona con el asistente (ADR-0084) | Agendar desde el panel en modo interno falla (`pack_calendar/admin_api.py:281-297` llama a Google); ofrece horas pasadas; sin re-chequeo de conflictos; confirmación sin fecha; sin recordatorios, aviso al equipo, `.ics` ni no-show | [HU-SH-02](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-02-demo-de-punta-a-punta.md) |
| 3 | Informar el plan: `informar_plan` / `consultar_inventario` | ✅ Existe con metadatos de plan | Recurrencia no editable desde API ni panel | HU-SUB-10 |
| 4 | Comprar: cotización → confirmación → `crear_pedido` → link | ⚠️ Con fricción | Exige domicilio; el LLM pone el monto del link; Empresarial (1.800.000) escala por el umbral de 1.000.000; el guardrail bloquea montos ≥ 1.000.000 | [HU-COM-01](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md), [HU-COM-02](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md), [HU-COM-03](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-03-numeracion-y-datos-por-producto.md) |
| 5 | `payment.confirmed` → pedido "pagado" | ⚠️ No durable | El bus traga errores; sin `tenant_id` en el evento | HU-SUB-03 |
| 6 | Pedido pagado → suscripción | ⚠️ Solo `pack_subscriptions`, fijo | Comercio no es agnóstico; Free nunca se activa | HU-SUB-06, HU-SUB-09 |
| 7 | Cada período: cargo + link + aviso | ⚠️ Parcial | El link no se envía; fuera de 24 h no hay plantillas | HU-SUB-05, [HU-ARCH-13](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md) |
| 8 | Pago del período → cargo pagado | ⚠️ Parcial | En cobranza el pago se pierde (defecto 1) | HU-SUB-02 |
| 9 | Mora: recordatorios → vencida → pausa | ❌ No existe | Sin estado `vencida` ni recordatorios | HU-SUB-04, HU-SUB-05 |
| 10 | Alta del cliente de SolversHub: tenant + plan + preset + invitación | ❌ Solo el master, con sesión humana | Sin identidad de servicio ni consumidor de aprovisionamiento (`core/api/routers/platform.py:114-197`) | [HU-SH-03](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md) |
| 11 | El cliente conecta su WhatsApp | ❌ Embedded Signup no funciona | Ver Conexiones | [HU-SH-05](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md), [SPEC-08](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/spec.md) |
| 12 | Cobro de la plataforma por asistente o por panel sin doble cobro | ❌ No existe | Dos registros (suscripción en el tenant `solvershub` y `TenantSubscription` del nuevo negocio) sin sincronización; `billing_lifecycle` solo marca `past_due` | [HU-SH-04](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md) |

## El tenant `solvershub` hoy

| Elemento | Estado |
|---|---|
| Archivos | `catalog.json`, `flow.json`, `playbooks/{ventas,seguimiento}.md`, `docs/{README,voz-de-marca}.md`, `evals/` (8 escenarios) |
| Packs | commerce, calendar, payments, subscriptions; **sin cobranza** |
| Precios | **Tres fuentes**: `core/billing/plans.py`, `catalog.json` y `voz-de-marca.md` |
| Prueba | `voz-de-marca.md:28`, `playbooks/ventas.md:22` y `seguimiento.md:8` prometen 30 días en todos los planes; el catálogo da 30 días a los pagos y 0 a Free. D-16 dice lo contrario |
| Flujo | Secciones propias etiquetadas `pack_commerce`: un re-seed de comercio las pisa (`core/agents/flow.py:270-280`) |
| Evals | Un solo turno; nada cubre pedido, link, suscripción ni la demo completa |

## Lo que hace "replicable" el comportamiento

Ninguna pieza del recorrido debe ser específica de SolversHub. La regla de diseño:

| Pieza | Dónde se parametriza |
|---|---|
| Tipo de cita "Demo", duración, horario, recordatorios, aviso al equipo | Config de `pack-calendar` + seed por pack |
| Planes (precio, período, prueba, beneficios, código de plan) | Variantes de comercio (catálogo o API) |
| Proveedor de suscripción (en línea o en campo) | Config del negocio / preset |
| Plantillas de cada evento (cargo, recordatorio, mora, activación) | Mapeo evento → plantilla por negocio |
| Qué pasa al activarse (webhook firmado, notificación, aprovisionar) | Acciones post-activación como datos; aprovisionar solo para negocios en la allowlist |
| Todo junto | Preset "Planes y suscripciones" (HU-SUB-11) |

Un gimnasio, un colegio o un software con mensualidad usa el mismo preset sin la acción de
aprovisionamiento: solo SolversHub crea tenants al venderse un plan.
