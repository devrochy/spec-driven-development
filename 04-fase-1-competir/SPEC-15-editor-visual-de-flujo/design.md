# SPEC-15 · Diseño

```
Asistente ▸ Flujo de conversación                      Borrador (sin publicar)  [Probar] [Publicar]
┌────────── Saludo ─────────┬────────── Ventas ─────────┬──────── Pago ────────┬─ Sin asignar ─┐
│ ▸ crear_lead       [core] │ ▸ consultar_inventario     │ ▸ confirmar_pago_    │ ▸ recomendar_ │
│                           │ ▸ generar_cotizacion       │   pedido   [confirma]│   producto    │
│                           │ ▸ aplicar_promocion        │                      │               │
│ [+ acción]                │ [+ acción]                 │ [+ acción]           │               │
└───────────────────────────┴────────────────────────────┴──────────────────────┴───────────────┘
```

- Cada tarjeta muestra el pack, si requiere conexión, si pide confirmación y sus límites.
- El negocio edita la **estructura** (etapas, orden, tools); el texto de cada etapa (`purpose`) solo
  el master en v1 (P-09).
- Un único validador (`core/agents/flow.py` + esquema JSON) en el backend; el panel muestra sus
  errores.
- Vista previa del bloque de prompt resultante (solo lectura).
- "Probar" corre el borrador en el sandbox del playground ([HU-ARCH-14](../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-14-playground-sandbox.md)); "Publicar" crea una versión del
  AgentSpec con reversa y entrada en `audit_log`.

## ADR

- **ADR "Editor de flujo"**: supersede ADR-0054 §5 y enmienda ADR-0017/0026 (edición en panel con
  borrador y publicación).
