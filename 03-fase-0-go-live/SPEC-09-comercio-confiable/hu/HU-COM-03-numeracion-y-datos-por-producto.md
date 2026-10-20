---
id: HU-COM-03
titulo: Numeración única y datos del cliente según el tipo de producto
spec: SPEC-09
fase: 0
hito: 0A
workstream: Comercio y suscripciones
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, legal]
req: [REQ-COM-02]
dependencias: []
skills: ["db-migration", "backend-design:data-modeling-discipline", "new-tool"]
ola: 2
estado: terminada
---

# HU-COM-03 · Numeración única y datos del cliente según el tipo de producto

> Estado SDD: Terminada — implementada 2026-10-07; verificada en test 2026-10-08 (issue [core #264](https://github.com/devrochy/agent-core/issues/264)).

**ID:** HU-COM-03

**Título:** Numeración única y datos del cliente según el tipo de producto

**Workstream:** Comercio y suscripciones

**Historia:** Como cliente que compra un plan o recoge en tienda quiero que solo me pidan los datos necesarios, y como negocio quiero números de pedido únicos con mi prefijo, para comprar rápido y encontrar cada pedido sin confusiones.

**Por qué importa (valor empresarial):** Pedir dirección de domicilio para comprar un plan de software espanta al cliente y guardar datos sin consentimiento viola la Ley 1581. Y un número de pedido repetido hace que un pago se aplique al pedido equivocado.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-COM-02

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Planes sin domicilio.** Dado un pedido cuyo único ítem es un plan recurrente, cuando se crea, entonces solo se piden nombre, correo y documento (o lo que configure el negocio), sin dirección.
- **Retiro sin domicilio.** Dado un pedido para retirar en tienda, cuando se crea, entonces no se pide dirección.
- **Captura progresiva.** Dado datos faltantes, cuando el asistente llama `crear_pedido`, entonces recibe `faltan_datos_cliente` con los campos que faltan y los que ya se conocen, y los pide uno a uno.
- **Consentimiento.** Dado datos del cliente, cuando se van a guardar para la próxima compra, entonces solo se guardan si el cliente aceptó.
- **Número único.** Dado el pedido 10.000 de un negocio, cuando se crea, entonces su número no se trunca ni choca con el 1.000; el prefijo es el del negocio y existe un índice único.

**Evidencia / Definición de Terminado:**
- Config `checkout_fields`; migración del índice único y del número público; tests de los cinco escenarios.

**Implementada (2026-10-07):** [agent-core #265](https://github.com/devrochy/agent-core/pull/265) — `public_order_number` regular con prefijo del negocio (`order_prefix`), sin truncar desde el pedido 10.000 e índice único `(tenant_id, public_order_number)` (migración `crm_0009` con backfill); `checkout_fields` por tipo de entrega y producto (planes y retiro sin dirección), `crear_pedido` con `faltan_datos_cliente` (`missing_fields` + `existing_data`) y guardado de perfil solo con `guardar_datos_cliente=true` (Ley 1581). 8 tests nuevos · suite unit 993.

**Verificada en test (2026-10-08, `develop` `293f070`):** migración `crm_0009` aplicada (`alembic_version_pack_commerce = crm_0009`) con el índice único `uq_crm_orders_tenant_number (tenant_id, public_order_number)`; el número público usa el prefijo del negocio (`OC-0001`). Los cinco escenarios (planes y retiro sin domicilio, captura progresiva, consentimiento y número único) están cubiertos por `tests/test_pack_commerce_checkout.py` y los de integración de #265 (CI verde).

**Riesgos/Notas:**
- D4 y D17 del barrido.
