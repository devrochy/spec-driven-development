# SPEC-08 · Diseño

## Resolver de credenciales (HU-CONN-01)

```python
@dataclass
class MetaCredentials:
    origin: Literal["byok", "embedded_signup", "manual"]   # guardado, no adivinado
    access_token: str
    app_id: str
    app_secret: str          # BYOK: el suyo; ES y manual: el de la plataforma
    waba_id: str | None
    business_id: str | None

def credentials_for(connection: MetaConnection) -> MetaCredentials
```

Todas las llamadas a la Graph API (números, plantillas, salud, suscripciones, precios, créditos,
token, descarga de media, envío) reciben `MetaCredentials` en vez de buscar "el" token del negocio.
El `appsecret_proof` se calcula con el secreto de esa conexión.

## Estados de una conexión

| Estado | Significado | Recibe y envía |
|---|---|---|
| `borrador` | Wizard sin terminar | No |
| `pendiente` | Esperando un paso de Meta (PIN, verificación) | No |
| `conectada` | Operativa | Sí |
| `degradada` | Operativa con advertencias (token por vencer, plantillas rechazadas) | Sí |
| `pausada` | Desactivada por el negocio | **No** (sender y ruteo de entrada lo verifican) |
| `error` | Falla que impide operar | No |
| `revocada` | Eliminada (soft-delete, tokens revocados) | No |

"Activar" solo vuelve a `conectada` una conexión que estaba `pausada` y pasa el diagnóstico.

## Webhook por conexión (HU-CONN-05)

- Ruta `/webhooks/whatsapp/<slug>/<connection_ref>` (o por `phone_number_id` en el payload).
- El secreto se resuelve **de la conexión dueña del `phone_number_id`**, no de la más reciente.
- Registrar o re-suscribir el webhook usa la app de esa conexión (BYOK: la suya; ES: la de la
  plataforma, solo por el master).

## Hub de WhatsApp-Meta (HU-CONN-08)

```
Conexiones ▸ WhatsApp · Tienda Centro                       [Producción] ● Conectada
┌──────────┬─────────┬────────────┬─────────┬────────────┬─────────┐
│ Resumen  │ Números │ Plantillas │ Webhook │ Producción │ Costos  │
└──────────┴─────────┴────────────┴─────────┴────────────┴─────────┘
 Salud: ✔ token (vence en 52 días)  ✔ WABA suscrita  ✔ webhook  ⚠ 2 plantillas rechazadas
 [Diagnosticar]  [Enviar mensaje de prueba]  [Renovar token]
```

- La lista general muestra: icono **por tipo** de conexión, nombre editable, estado con motivo,
  badge de entorno (Prueba/Producción), "Abrir" (al hub) y solo las acciones que el backend permite
  para esa fila (`allowed_actions`).
- El wizard empieza con tres caminos: "Prueba (mi app de Meta, número de prueba)", "Producción
  (Conectar con Facebook)" y "Producción (mi app de Meta)".

## Costos de Meta (HU-CONN-09)

Flag `costs.meta_enabled` por conexión; job diario por conexión con sus credenciales; última
sincronización y último error guardados; "Verificar" hace una consulta de prueba del día anterior.
En sandbox se explica que los números de prueba no generan cobros.

## ADR

- **Enmienda a ADR-0069/0080**: credenciales y webhook por conexión, estados y acciones permitidas.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Migrar conexiones existentes sin `origin` | Script que lo deduce una vez con revisión manual de los casos dudosos |
| Re-registrar el webhook de la app de la plataforma por error | Solo el master puede tocar la app de la plataforma |
