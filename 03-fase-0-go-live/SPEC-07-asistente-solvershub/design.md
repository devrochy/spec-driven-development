# SPEC-07 · Diseño

El recorrido completo y los dos canales de cobro están en
[arquitectura-objetivo.md](../../02-vision-y-decisiones/arquitectura-objetivo.md#el-recorrido-de-solvershub).

## Tenant `solvershub` como datos

| Pieza | Fuente única |
|---|---|
| Planes y precios | `core/billing/plans.py`; los productos del tenant se generan desde ahí con `entitlements.plan_code` (no se copian precios) |
| Voz de marca y playbooks | `tenants/solvershub/` versionado y persistido en `TENANTS_ROOT` (ADR-0085), coherente con D-16 |
| Flujo | Preset "Planes y suscripciones" + secciones `tenant` propias |
| Demo | Tipo de cita "Demo" (45 min), horario comercial, recordatorios −24 h y −1 h, aviso al equipo |
| Proveedor de suscripción | `pack_subscriptions` (P-03) |

## Consumidor de aprovisionamiento (HU-SH-03)

```
outbox: subscription.activated {tenant_id = solvershub, plan_snapshot.plan_code, customer, reference}
   │
   ▼
core/provisioning/consumer.py
   1. ¿tenant_id en PROVISIONING_SELLER_TENANTS?            no → ignorar
   2. ¿ya existe un alta con esta reference?                 sí → no repetir (idempotente)
   3. antiabuso (HU-SH-07): límites por teléfono/documento   falla → revisión humana
   4. onboard_tenant(slug derivado, plan=plan_code,
                     preset=según vertical declarado)
   5. invitación sin contraseña al owner (correo + WhatsApp)
   6. tenant_subscriptions del negocio nuevo: período y referencia `plat-<slug>-<AAAAMM>`
   7. audit_log con actor = identidad de servicio "provisioning"
```

La identidad de servicio es un principal de tipo `service` que solo existe dentro del core: no
tiene token exportable ni sesión de panel.

## Dos canales de cobro (HU-SH-04)

| Paso | Canal asistente | Canal panel |
|---|---|---|
| Generar cobro del período | Cargo en la suscripción del cliente dentro del tenant `solvershub` | `/plan` → `core/billing.start_subscription` |
| Referencia | `plat-<slug>-<AAAAMM>` | La misma |
| Pago | `payment.confirmed` en el tenant `solvershub` → evento → `apply_payment` en `tenant_subscriptions` | Webhook de billing → `apply_payment` |
| Sincronización inversa | — | Evento → marca pagado el cargo del canal asistente |
| Conciliación | Job diario compara ambos lados y alerta | |

Antes de implementar, verificar el riesgo R-05 (Wompi admite una sola URL de eventos por entorno).

## Demo (HU-SH-02)

- `check_availability` corta horas pasadas y respeta `CalendarBlock` y horario.
- `create_calendar_event` re-verifica disponibilidad dentro de una transacción con bloqueo.
- Confirmación con fecha y hora; recordatorios por job (plantilla fuera de 24 h); aviso al equipo por
  permiso; reagendar y cancelar ya existen; estado `asistio | no_asistio`.
- Arreglo del panel: en modo interno, crear y cancelar citas no llaman a Google.

## Embedded Signup (HU-SH-05)

Componente React del SDK de Facebook (`FB.login` con `config_id`, `response_type: "code"`,
`override_default_response_type: true`), escucha de `WA_EMBEDDED_SIGNUP` (finish y cancel), envío de
`authResponse.code` + `waba_id` + `phone_number_id` al endpoint de intercambio, que **encadena** los
pasos automáticos (suscribir WABA, registrar número con PIN, sincronizar plantillas, verificar salud)
y termina en el hub de la conexión con un mensaje de prueba.

## ADR

- **ADR "Identidad de servicio y aprovisionamiento automático"**.
- **ADR "Dos canales de cobro de plataforma"**.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| R-01 Meta tarda en aprobar a SolversHub como Tech Provider | Iniciar trámites ya; BYOK de producción ([HU-CONN-06](../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-06-byok-produccion.md)) como respaldo para el primer cliente |
| R-05 Wompi con una sola URL de eventos | Verificar en la primera semana |
| Altas fraudulentas | [HU-SH-07](hu/HU-SH-07-antiabuso-y-cumplimiento.md) antes de abrir el canal |
