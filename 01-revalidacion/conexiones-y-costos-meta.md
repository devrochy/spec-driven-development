# Conexiones, flujo con Meta y costos de Meta

Fuente: auditoría funcional del 2026-10-01 sobre el panel nuevo y el backend. Prefijos: `P/` =
`solvershub-panel/apps/panel-web/`, `B/` = `solvershub-backend/`.

## Resumen

- **Embedded Signup no funciona en ningún lado.** En el panel nuevo el botón solo crea una sesión
  del wizard; el JS clásico (`B/core/admin/static/embedded_signup.js`) ya no lo carga ninguna página
  y apunta a rutas que no existen.
- **BYOK es el único camino que conecta**, y siempre queda en `sandbox` (re-verificado:
  `B/core/gateway/meta_byok.py:97`). Después de conectar, para BYOK fallan Números, Plantillas,
  Re-suscribir, Diagnosticar, la sincronización de precios y los créditos.
- **8 de los 9 defectos anteriores siguen presentes.**
- **Dos errores 500 nuevos**: Números (`PhoneNumber.status` no existe,
  `B/core/admin/meta_numbers_service.py:91`) y la lista de créditos de Meta (`MetaConnection.label`
  no existe, `B/core/api/routers/costs.py:200`).

## La lista de conexiones (`P/app/(app)/conexiones/page.tsx`)

| Aspecto | Evidencia | Problema |
|---|---|---|
| Icono | `ChannelBadge id={c.channel}` (`page.tsx:36`) | Se elige por canal, no por tipo: Meta BYOK, Meta ES y WhatsApp Web muestran el mismo icono; Google Calendar sale con un enchufe genérico y etiqueta vacía |
| Origen | `B/core/api/routers/connections.py:62,110-114` | Todo aparece "Manual"; ES vs BYOK se **adivina** comparando el `meta_app_id` con el de la plataforma |
| Estado | `connections.py:123` | Solo `connected` es "Activa"; borrador, pendiente, degradada, error y revocada salen todas "Inactiva", sin motivo |
| Filas | `connections.py:79-89` | Aparecen borradores abandonados de Embedded Signup |
| Enlaces | — | Ninguna fila lleva a Números, Plantillas, Salud, el QR o Calendario |

**¿Funciona cada acción para cada tipo?**

| Tipo | Editar | Activar / Desactivar | Principal | Eliminar |
|---|---|---|---|---|
| WhatsApp Meta (BYOK o ES) | No se ofrece | **Parcial**: solo cambia `status`; el sender (`B/core/gateway/sender.py:46-108`) y el ruteo de entrada (`webhook_route_tenant.py:47-58`) lo ignoran, así que **el bot sigue respondiendo**. "Activar" fuerza `connected` en borradores | Deshabilitado (correcto) | **Parcial**: borra en duro números y WABA (`B/core/admin/meta_health_service.py:266-275`), con cascada a `pricing_daily` y `message_templates` (**rompe la invariante 8**); no revoca tokens; sin confirmación |
| WhatsApp Web | **Roto** (404) | OK | OK | OK |
| SMTP | OK | OK | Parcial: se ofrece aunque no aplica | OK |
| Google Calendar | **Roto** (404) | **Parcial**: el siguiente refresh del token la revive (`pack_calendar/oauth.py:221-254`) | Parcial | Parcial: misma resurrección |

Además: "Abrir asistente" de Calendar abre el wizard de WhatsApp (`new-connection-dialog.tsx:153-157`)
y los nombres de conexión no se pueden editar.

## Dónde viven hoy las opciones exclusivas de Meta

| Opción | Ubicación | Alcance |
|---|---|---|
| Salud de conexiones | `/conexiones/meta`, botón en el encabezado de la lista | Global, **incluye conexiones borradas** |
| Suscripciones de webhook | Pie de `/conexiones/meta` | Por canal, no por conexión: el backend elige "la" app |
| Requisitos de Meta | `/conexiones/requisitos`, grupo "Herramientas" del menú | Global |
| Promoción a producción | `/conexiones/produccion`, mismo grupo | Global; usa los mismos 10 pasos que Requisitos y **nunca cambia el entorno de una conexión** |
| Conectar con Embedded Signup | Tarjeta en `/conexiones/whatsapp` | El botón solo crea la sesión |
| Números y Plantillas | `/conexiones/meta/[id]/{numeros,plantillas}` | Por conexión, pero sin enlace desde la lista |

El menú muestra todo esto a cualquier negocio con permiso de conexiones, **aunque no tenga una
conexión de Meta**.

## El recorrido hoy

**Prueba (BYOK), el único que funciona**: el formulario pide App ID, App Secret, WABA ID, Phone
Number ID y token, sin explicar dónde se obtienen ni el límite de 5 destinatarios del número de
prueba. Al guardar, verifica el número, guarda secretos, suscribe la WABA, registra el webhook en
`/webhooks/whatsapp/<slug>` y marca `connected` en `sandbox`. La página solo dice "Conexión BYOK
creada." y se queda ahí, sin mensaje de prueba.

**Producción con Embedded Signup, no implementado**:

| Paso | Estado |
|---|---|
| Cargar el SDK y llamar `FB.login` con `config_id` y `response_type: code` | Falta en el panel |
| Leer el código de `authResponse.code` | Falta; el JS clásico lo leía del evento del popup (probablemente también estaba roto) |
| Escuchar los eventos `WA_EMBEDDED_SIGNUP` | Falta; no hay endpoint de cancelación |
| Sesión y reanudación | La API existe (`B/core/api/routers/meta_wizard.py:68-88`); el panel descarta el id y muestra texto de desarrollador |
| Intercambio del código | La API existe (`meta_wizard.py:100-125`) pero no encadena los pasos automáticos |
| Registro del número + PIN, plantillas, salud | La API existe (`meta_onboarding.py:706-836`); la UI nunca la llama |
| Reiniciar después de 24 h | **Error 500** por el índice único parcial (`meta_onboarding.py:138-173`) |

**Producción con BYOK**: fijado en sandbox; el modelo de la API no tiene campo de entorno
(`meta_wizard.py:164-170`); no hay promoción ni registro de número + PIN; los chequeos de
producción miran la app de la plataforma. **BYOK y ES en el mismo negocio rompen los mensajes
entrantes de BYOK**: el secreto se toma de la conexión más reciente (`meta_byok.py:311-327`) y el
webhook BYOK se rechaza con 401.

## Defectos anteriores: re-chequeo

| # | Defecto | Estado |
|---|---|---|
| 1 | Las tools de Meta ignoran BYOK (solo leen el token de ES y el secreto de la plataforma; `meta_numbers_service.py:34-36`, `meta_templates_service.py:42`, `meta_health.py:305-307`) | Sigue |
| 2 | "Diagnosticar" da verde falso (`meta_health.py:313-314,347-349`) | Sigue |
| 3 | `health` se sobrescribe y pierde `coexistence` y `billing.manual_status` (`meta_health_service.py:83`, `tasks/meta_health_check.py:58`) | Sigue, y el cron horario también lo hace |
| 4 | "Registrar webhook" mueve BYOK al webhook genérico (`meta_health_service.py:206-216`) | Sigue |
| 5 | "Eliminar" borra en duro números y WABA | Sigue |
| 6 | "Desactivar" no pausa el consumer ni el sender | Sigue |
| 7 | El checklist de producción exige suscripciones de page e Instagram y corre pytest dentro de la imagen (`meta_production_readiness.py:83-90,222-237`) | Sigue: siempre rojo y puede bloquear el event loop hasta 180 s |
| 8 | Páginas que crean filas en un GET | Arreglado para el wizard; quedan Números, Plantillas y Requisitos con efectos en GET |
| 9 | La sincronización de precios necesita token de ES y app secret en la misma conexión (`tasks/meta_pricing_sync.py:58-65`) | Sigue: **ningún flujo produce esa combinación** |

**Defectos nuevos**: los dos 500, los enlaces de reparación de Salud que nunca aparecen
(`P/app/(app)/conexiones/meta/page.tsx:180-185`), acciones sobre conexiones borradas
(`B/core/db/session.py:70-86` no filtra `deleted_at`) y el alta manual sin chequeo de duplicados ni
suscripción de la WABA (`meta_wizard.py:234-264`).

## Costos de Meta: ¿cómo se habilita? ¿solo en producción?

**Respuesta**: no se habilita; **no depende del entorno**. La sección se muestra a cualquiera con
permiso de costos, porque la API siempre devuelve el bloque de Meta (`costs.py:143-150`). Está
vacía por cuatro motivos:

1. La sincronización necesita el token de Embedded Signup y el app secret **en la misma conexión**,
   y ningún flujo de alta produce esa combinación. Falla en silencio.
2. El tráfico de números de prueba no es facturable.
3. BYOK nunca guarda `business_id`, así que no aparece para créditos.
4. La lista de créditos devuelve 500, y la tarjeta dice "Sin conexiones de Meta".

"Sincronizar costos" omite las conexiones sin credenciales, no reporta errores y **muestra
"Costos sincronizados." aunque no sincronizó nada** (`P/app/(app)/costos/_components/meta-costs.tsx:32-35`).

**Propuesta** ([HU-CONN-09](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-09-costos-meta-verificables.md)):
costos de Meta como subsección opcional **dentro de cada conexión de WhatsApp-Meta**, con una flag por
conexión (encendida por defecto en producción, explicada en sandbox), un botón "Verificar" que hace
una consulta de prueba y guarda la última sincronización y el último error, y una tarjeta agregada en
Costos solo si alguna conexión tiene la flag. Depende del resolver de credenciales
([HU-CONN-01](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md)).

## Estructura propuesta: lista genérica + hub por tipo

| Pieza | Ya existe | Falta |
|---|---|---|
| Lista `/conexiones` | Tabla, diálogo de catálogo, diálogo de acciones, formulario por schema | Iconos por tipo, estado real con motivo y badge de entorno, "Abrir" hacia el hub, acciones permitidas por fila según el backend, confirmación al eliminar, nombre editable |
| Hub WhatsApp-Meta `/conexiones/meta/[id]` | Páginas de Números y Plantillas; acciones de Salud; registro de webhook; checklist | La página del hub con pestañas Resumen/Salud · Números · Plantillas · Webhook · Producción · Costos; endpoints por conexión |
| Wizard `/conexiones/whatsapp` | API de sesión, intercambio, número, PIN, BYOK y manual | Paso inicial "Prueba (BYOK)" / "Producción (Embedded Signup)" / "Producción (BYOK)"; SDK de Facebook; lectura del estado y cancelación; pantalla final que lleva al hub con un mensaje de prueba |
| Hubs de WhatsApp Web y Calendar | `/conexiones/waweb`, `/calendario` | Enlaces desde la lista |
| Sección de plataforma (solo master) | Páginas de Requisitos y Producción | Mover ahí los pasos del dueño de la app y los chequeos de infraestructura, como job en segundo plano y sin pytest |
| Prerrequisitos de backend | — | Resolver de credenciales por conexión, origen guardado, salud fusionada, borrado lógico con revocación, estado respetado en sender y ruteo, webhook por conexión, los dos 500, reutilizar el borrador vencido |
