# SPEC-12 · Diseño

## Componentes y flujo

- El menú v2 sale de `NAV_GROUPS` en `apps/panel-web/components/shell/nav.ts` ([HU-UX-02](hu/HU-UX-02-menu-v2.md)).
  Las migas, las pestañas de sección y la paleta de comandos (`paleta.ts`, `ATAJOS_IR`) ya se derivan de
  `nav.ts` (DS-04 y DS-05), así que un solo cambio se propaga. Con
  [HU-FWK-05](../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-05-manifiesto-de-menu.md) pasará a construirse
  desde el manifiesto del backend.
- Una entrada de primer nivel por tarea, en 4 grupos: **Operación** (Resumen, Conversaciones, Clientes), **Tu
  asistente** (Agentes, Conexiones), **Negocio** (Agenda, Ventas, Cobranza) y **Cuenta** (Consumo y plan, Equipo,
  Configuración), más **Plataforma** solo para master. Lo que hoy son hermanas de menú (Escalaciones, las 14 de
  Cobranza, las 5 de Comercio y las 5 de Calendario) pasan a **pestañas** de una sola entrada. `lib/shell/navegacion.ts` deja de calcular las
  pestañas a partir de las hermanas del menú y las toma de un campo `tabs` del ítem.
- **Fichas por objeto**: el agente (`/agentes/[id]`) y la conexión (`/conexiones/[id]`) tienen su ficha con
  pestañas, y se enlazan entre sí. Las páginas usan las plantillas de `components/templates/` (ListPage,
  DetailPage, SettingsPage) y el kit de `components/ui` ([SPEC-29](../SPEC-29-sistema-de-diseno-unificado/spec.md): solo tokens).
- `Tooltip` accesible (teclado y táctil) y modal "¿Qué es esto?" por sección, con textos en `lib/copy.ts`.
- Estados vacíos: componente `EmptyState` con acción primaria obligatoria.
- Permisos: el backend expone las acciones permitidas por vista y el panel oculta lo no permitido
  (nunca un 403 por diseño).
- Guías por habilidad: cada pack declara su checklist en sus metadatos ([HU-FWK-04](../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md)).

## Datos (tablas, migraciones, RLS)

- Sin tablas nuevas en el core. La relación Agentes ↔ Conexiones ya existe (`ConnectionAgentInstance`: rol,
  prioridad, por defecto) y la exponen `/admin/agents/overview` (cada agente con sus conexiones) y
  `/admin/connections/{id}/agents`.
- **Única posible migración**: color o identificador del tipo de cita en `pack_calendar`, si el tipo no lo tiene
  ([HU-UX-08](hu/HU-UX-08-agenda-unificada.md)). Columna nueva con valor por defecto; reversible.

## API

- Se consumen endpoints que ya existen en `origin/develop`: `/admin/agents/overview`, `/admin/connections/{id}/agents`,
  `/admin/me` (sección `agents`) y `/subscriptions/lista` (Suscripciones, ya etiquetada en `lib/labels.ts`).
- Corrección de permisos de Agenda: el panel usa `pack_calendar:conexion` para el horario y el backend define
  `pack_calendar:configuracion` («Horarios y calendario», `packages/pack-calendar/pack_calendar/module.py:360`).
  El menú v2 ([HU-UX-02](hu/HU-UX-02-menu-v2.md)) ya usa la clave del backend para Horario.

## UI

### Agentes ↔ Conexiones

- Relación de muchos a muchos: un agente corre en una o más conexiones y una conexión puede tener varios agentes
  (el Coordinador enruta). Por eso **no se anida una dentro de la otra: se enlazan en las dos direcciones**.
  - La ficha del agente suma la pestaña **Conexiones**: conexión, tipo, rol, prioridad, si es la conexión por
    defecto y estado. Cada fila lleva a la ficha de la conexión.
  - La ficha de la conexión tiene la pestaña **Agentes** (la lista que hoy muestra la consola de
    [HU-AOS-23](../SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md)). Cada fila lleva a la ficha del agente.
- Se respeta D-35: un agente publicado tiene al menos una conexión; la consola ya avisa de «agentes publicados sin conexión».
- **Estado actual**: el backend lo resuelve y la ficha del agente
  ([HU-AOS-47](../SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md), terminada en panel #82) ya muestra
  «Atiende en …» con los nombres de sus conexiones (`app/(app)/agentes/[id]/page.tsx`). Lo que falta (la pestaña
  Conexiones con la tabla de rol, prioridad, principal y estado, con enlace a cada ficha, y la pestaña
  Superpoderes) va en [HU-UX-09](hu/HU-UX-09-ficha-de-conexion-por-tipo.md).
- «Habilidades» deja de nombrar dos cosas: la pestaña de herramientas del agente se llama **Superpoderes** (D-35)
  y «Habilidades» queda solo para los packs, en Configuración. «Probar asistente» (`/asistente`) pasa a la ficha del agente.

### Conexiones

Cada fila de la lista abre una ficha `/conexiones/[id]` con pestañas que dependen del tipo
([HU-UX-09](hu/HU-UX-09-ficha-de-conexion-por-tipo.md)):

| Tipo | Pestañas de la ficha | Qué se mueve ahí |
|---|---|---|
| WhatsApp oficial (Meta: Embedded Signup o app propia) | Salud · Números · Plantillas · Webhook · Producción · Costos · Agentes | `conexiones/meta/_components/meta-health-actions.tsx`, `meta-health-checks.tsx`, `webhook-register.tsx`; las páginas de `conexiones/meta/[connectionId]/` (números, plantillas, producción, pasar a producción); `/plantillas` |
| WhatsApp Web (QR, no oficial) | Vinculación · Estado · Agentes | QR, reiniciar vínculo y aviso de riesgo (hoy en `/conexiones/waweb`). Sin Salud de Meta, plantillas ni producción |
| Google Calendar | Cuenta · Agentes | La conexión con Google que hoy vive en `/calendario` |
| Wompi | Credenciales · Agentes | Lo que hoy vive en `/habilidades/pack_payments` |
| Chat web | Apariencia · Instalación · Agentes | Lo que hoy vive en Configuración |
| SMTP | Credenciales · Agentes | — |

- **«Salud» solo existe en las conexiones Meta.** «Salud de Meta» deja de ser una página global y pasa a la
  pestaña Salud de cada conexión Meta; en la lista queda solo un indicador de salud en las filas Meta.
- El botón global «WhatsApp Web» de la lista desaparece: se crea desde «Agregar conexión» → WhatsApp Web y se
  gestiona en su ficha.
- Se disuelve «Herramientas»: Plantillas y Producción pasan a la ficha; Requisitos de Meta a Plataforma → App de
  Meta; Bandeja de fallos a Configuración → Mensajes fallidos; Probar asistente a la ficha del agente.
- **Defecto del diálogo «Agregar conexión»**: `conexiones/_components/new-connection-dialog.tsx` (hoy ~153-156 en
  `main`) comprueba `type.url` pero enlaza siempre a `/conexiones/whatsapp`, así que chat web y Google acaban en el
  asistente de WhatsApp. Se corrige para que use `type.url` de cada tipo.

### Agenda

Las 5 entradas del calendario pasan a **una**, con tres pestañas ([HU-UX-08](hu/HU-UX-08-agenda-unificada.md)):

- **Calendario**: la vista FullCalendar de `calendario/citas/_components/calendar-grid.tsx`.
  - Al seleccionar un hueco se elige «Cita» o «Bloqueo» (hoy los bloqueos se crean en `/calendario/bloqueos`).
  - Los bloqueos se ven como eventos de fondo y se pueden arrastrar para moverlos.
  - Cada tipo de cita tiene un color o identificador visible en el evento.
  - Sale la tabla duplicada de próximas citas de `/calendario`.
- **Tipos de cita**: suma color e identificador (campo nuevo en `pack_calendar` si hace falta).
- **Horario**: el horario de agendamiento (`business_hours` de la configuración del pack), con la clave de permiso
  `pack_calendar:configuracion`.
- La conexión con Google sale de Agenda y va a Conexiones (ficha Google Calendar).

### Cobranza y Ventas

- **Cobranza** pasa de 14 entradas a 1 ([HU-UX-10](hu/HU-UX-10-cobranza-y-ventas-en-pestanas.md)). Su Resumen
  tiene accesos rápidos y las páginas se agrupan en pestañas por los subgrupos de hoy: **Operación** (Gestores,
  Carteras, Clientes, Cobros, Promesas, Propietario, Reportes), **Monitoreo** (Monitoreo IA, Reglas de
  negociación) y **Seguridad** (Alertas de acceso, Auditoría, Dispositivos). «Cobros al propietario» y «Pagos de
  clientes», que comparten `pack_cobranza:cobros`, quedan como dos pestañas de una sola página.
- **Ventas**: Comercio con sus pestañas (Resumen, Productos, Categorías, Promociones, Pedidos) y **Suscripciones**,
  que el backend ya declara (`/subscriptions/lista`) y hoy no tiene entrada.

### Configuración

- Ya tiene pestañas; absorbe **Mensajes fallidos** (ex DLQ, `/dlq`) y **Habilidades** (packs, `/habilidades`).
- Este rediseño **toma el objetivo de [HU-UI-09](../SPEC-13-vistas-profesionales/hu/HU-UI-09-configuracion-por-pestanas.md)**
  (configuración por pestañas, parqueada por D-35); queda registrado en [SPEC-13](../SPEC-13-vistas-profesionales/spec.md) para no duplicar.

### App móvil

- El cajón lateral del panel en la app (D-34, `solvershub-apk/src/navigation/menu-panel.ts`) replica la lista del
  menú v2 con los mismos grupos y nombres ([HU-UX-11](hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md)). Hasta esa HU
  la app queda desalineada (no hay OTA ni build en la entrega del menú web).

## ADR a crear o enmendar

- **ADR-0001** del panel (`solvershub-panel/docs/adr/0001-arquitectura-de-informacion.md`, de [HU-UX-01](hu/HU-UX-01-adr-arquitectura-de-informacion.md)):
  se enmienda con el árbol v2, las fichas por objeto y la regla «una entrada por tarea; lo demás, pestañas».
- **ADR-APP-07** de la app: se enmienda con [HU-UX-11](hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md) (la lista del cajón sigue al menú v2).

## Migración, despliegue y reversa

[HU-UX-02](hu/HU-UX-02-menu-v2.md) **solo reagrupa el menú: ninguna URL cambia** y no lleva redirecciones. Rutas
como `/escalaciones`, `/leads`, `/costos`, `/plan`, `/dlq`, `/habilidades` y `/tenants` siguen iguales; solo cambian
de grupo o pasan a mostrarse como pestaña. Las redirecciones llegan con las HU que mueven rutas: cada fila tiene su
caso en el test de redirecciones y se implementa en `next.config` (`redirects`) o en `app/legacy/[...path]/route.ts`.
Esta tabla reemplaza la de [arquitectura-informacion-panel.md](../../02-vision-y-decisiones/arquitectura-informacion-panel.md#mapeo-y-redirecciones).

| Ruta actual | Destino v2 | HU |
|---|---|---|
| `/asistente` | Ficha del agente (General), «Probar» | UX-09 |
| `/conexiones/meta` | Conexiones (indicador de salud en las filas Meta) | UX-09 |
| `/conexiones/meta/[id]`, `/conexiones/meta/[id]/numeros`, `…/plantillas`, `…/produccion`, `…/pasar-a-produccion` | `/conexiones/[id]` con la pestaña equivalente | UX-09 |
| `/plantillas`, `/plantillas/eventos` | Pestaña Plantillas de la conexión Meta (si hay una sola; si hay varias, la lista de Conexiones) | UX-09 |
| `/conexiones/waweb` | `/conexiones/[id]`, pestaña Vinculación (o «Agregar conexión» → WhatsApp Web si no existe) | UX-09 |
| `/conexiones/requisitos`, `/conexiones/produccion` | Plataforma → App de Meta (master); Conexiones para el resto | UX-09 |
| `/calendario` | Agenda → Calendario | UX-08 |
| `/calendario/citas`, `/calendario/bloqueos` | Agenda → Calendario | UX-08 |
| `/calendario/tipos` | Agenda → Tipos de cita | UX-08 |
| `/calendario/horario` | Agenda → Horario | UX-08 |
| `/cobranza/*` | Cobranza, pestaña equivalente | UX-10 |
| `/comercio/*` | Ventas → Comercio, pestaña equivalente | UX-10 |

**Reversa**: el menú v2 es un cambio de `nav.ts` sin rutas nuevas; se revierte con su PR. Las redirecciones de
UX-08, UX-09 y UX-10 se quedan aunque se revierta una de esas HU, porque llevan a páginas que siguen existiendo.

## Riesgos

- Las fichas v2 se construyen sobre lo que entregó la tanda 7 del Agent OS ([HU-AOS-23](../SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md), [HU-AOS-24](../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) y [HU-AOS-47](../SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md), panel #80, #81 y #82).
- La regla de no abrir HU del 0B se cumple porque [HU-UX-02](hu/HU-UX-02-menu-v2.md) deja de depender de [HU-CONN-08](../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md).
- Enlaces guardados por los clientes (correo, app): el menú v2 no cambia URLs; las HU que sí las mueven traen la redirección y su test.
- La app queda desalineada con el panel web hasta [HU-UX-11](hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md).
