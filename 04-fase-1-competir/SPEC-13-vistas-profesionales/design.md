# SPEC-13 · Diseño

## Bandeja de dos paneles

```
┌───────────────────────────────┬──────────────────────────────────────────────┐
│ [Abiertas 12][Por atender 3]  │ Ana Gómez · WhatsApp · ventana 24 h: 3 h 10 m │
│ [Cerradas] 🔍                 │ [Tomar] [Resolver] [Devolver al asistente]    │
│───────────────────────────────│──────────────────────────────────────────────│
│ ● Ana Gómez        hace 2 min │  …hilo con burbujas, media y estado de envío  │
│   "¿Tienen domicilio a…"      │                                              │
│ ○ Juan Pérez      hace 15 min │                                              │
│   🎤 Nota de voz              │ ┌──────────────────────────────────────────┐ │
│                               │ │ Escribe… (Ctrl+Enter)  [Plantilla ▾]     │ │
└───────────────────────────────┴─┴──────────────────────────────────────────┘
```

- Estado en la URL (`?c=&estado=`); orden por última actividad; vista previa del último mensaje.
- Ventana de 24 h visible y botón de plantilla cuando está cerrada ([HU-ARCH-13](../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md)).
- Acciones de ticket con colores de acción: Tomar (advertencia), Resolver (éxito), Devolver (acento).

## Tickets

API nueva: `POST /api/v1/admin/escalations/{id}/take|resolve|return|assign`; los ítems traen id,
asignado, motivo legible y "esperando hace X". Mientras un humano tiene el ticket, el bot está pausado
en esa conversación y el cliente recibe aviso.

## Dashboard

`?period=7|15|30`, series diarias y valores del período anterior; % resuelto sin humano; gráfico SVG
accesible; KPIs enlazados; aviso de cuota; primeros pasos ([HU-SH-06](../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md)).

## Notificaciones a operadores

Preferencias por colaborador (WhatsApp con plantilla, correo, campana del panel) y por tipo de
evento (ticket nuevo, pedido pagado, comprobante por revisar, cuota al 80 %).
