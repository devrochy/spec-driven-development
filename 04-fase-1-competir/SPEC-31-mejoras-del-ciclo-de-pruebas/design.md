# SPEC-31 · Diseño

Rutas del panel relativas a `solvershub-panel/apps/panel-web/` (`main` en `cc6af39`). Rutas del core relativas a `solvershub-backend/` (`develop` en `5657885`). Rutas de agent-sale relativas a `agent-sale/` (`develop`).

## Inventario

Cada fila es una nota del dueño (`master@demo.test`), con el nombre de la prueba del catálogo v5. «Resuelto» quiere decir corregido y desplegado en test al 2026-10-19.

### Resuelto antes de esta spec

| Nota (prueba) | Dónde se resolvió |
|---|---|
| Suspendido que entra, permisos que no se aplican, cuenta desactivada con sesión, data del negocio anterior, propietario invitado | core #468 (ADR-0136, migración 0090), panel #79 |
| Negativos aceptados, toggle al tope del plan en «on», candado horario de plantillas, «Invalid Parameter» al eliminar, límite de números | core #467, panel #79 |
| Chat web que no se encuentra en la landing | landing #13 |
| Alta automática visible para todos | panel #79 (Plataforma, solo master) |
| Colaboradores: slug solo para master con autocompletado, filtro por negocio, desvincular | panel #79 |
| Packs no habilitados en gris en la barra plegada; menú largo | menú v2, panel #89 ([HU-UX-02](../SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md)) |
| Planes por agentes, colaboradores y crédito | core #483 + panel #87 (HU-BILL-05) |
| Agentes por fin (ventas, cobranza, agenda, suscripciones) | plantillas de [HU-AOS-24](../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) y presets v2 de [HU-AOS-46](../SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) |

### Lo que entra en SPEC-31

| # | Nota (prueba) | Qué falta hoy (evidencia) | HU |
|---|---|---|---|
| 1 | «la vista de conversaciones … al estilo de WhatsApp Web» y «que los mensajes … se actualicen sin necesidad de refrescar» (Responder fuera de la ventana con una plantilla, paso 1) | `app/(app)/conversaciones/page.tsx` es una tabla. El detalle se refresca con `refresh-button.tsx` (`router.refresh()`). `core/api/routers/conversations.py` devuelve todos los mensajes, sin `after`, y ordena por `started_at` | [UX-15](hu/HU-UX-15-bandeja-de-conversaciones.md) |
| 2 | «no se está visualizando correctamente las conversaciones de las diferentes conexiones» (Conexión desactivada, paso 2) | `ConversationSummary` (`conversations.py:28-36`) no trae la conexión, aunque el modelo tiene `connection_id` y `meta_connection_id` (`core/db/models.py:294,300`). El canal sale crudo («whatsapp_cloud») | UX-15 |
| 3 | «El motivo no es muy claro cuando se menciona una tool … como se hizo en agent-sale»; «puntos suspensivos y … ventana con el texto completo» (Escalaciones y su hilo, paso 1) | `escalaciones/page.tsx` pinta `esc.reason` crudo. `escalacionLabel()` (`lib/labels.ts:115`) no se usa en ninguna página y convierte todo `tool:*` en «Solicitud manual». El bot escribe el motivo libre (`core/tools/core_skill.py:52,176`). `keyword`, `llm_error`, `plugin:<tool>` y `persona_forbidden_phrase` no tienen etiqueta | [UX-17](hu/HU-UX-17-motivos-de-escalacion-legibles.md) |
| 4 | Leads: «solo la información general … con los datos del canal … almacenarlos para no preguntar después … en agent-sale se puede pausar por cliente el bot, ver la clasificación, editar … filtrados de acuerdo a la conexión»; «un buen paginado» (Leads: buscar y paginar, pasos 1 y 3) | `core/api/routers/leads.py` solo acepta `q` y no devuelve `bot_paused`, el perfil ni la conexión. `Customer.bot_paused` existe y se respeta en `core/kernel/ingress.py:147`, pero ningún endpoint lo cambia. La memoria (`memory_facts`, `core/memory/facts.py`) no se muestra. Hay doble paginación: la del servidor más `components/ui/table-enhancer.tsx:160-180` | [UX-16](hu/HU-UX-16-clientes-estilo-agent-sale.md) (paginado en [UX-12](hu/HU-UX-12-arreglos-rapidos-del-ciclo.md)) |
| 5 | «Si vuelve pero la opción de 7 días sigue seleccionada» (Agentes: pestañas y período, ciclo Release 10-17) | `agentes/_components/agent-filters.tsx:26` usa `defaultValue` sin `key` | UX-12 |
| 6 | «si el pago es pendiente no da facilidad de abrir el pago» (El panel no cobra dos veces el mismo período, paso 2) | La tabla de pagos de `plan/page.tsx:37-62` no tiene acción por fila, aunque la API trae `checkout_url` | UX-12 |
| 7 | «No aparece tooltip», «el scroll lateral tapa parte de los iconos» (Barra plegada, pasos 1 y 2); «hay un icono de información pero no sirve» (Colaboradores) | `components/ui/tooltip.tsx` es `absolute`. El `overflow-y-auto` del `nav` plegado (`components/shell/sidebar.tsx`) y el `overflow-hidden` de `data-table.tsx:67` lo recortan, y el clic en la cabecera ordena la columna | UX-12 |
| 8 | «no sale en forma de aviso y tampoco desaparece … con un ícono según el evento», «Aparece en inglés» (Avisos, pasos 1 y 2); captura de «Nuevo colaborador» con «Please enter a part following '@'»; «Avisa en inglés» (SMTP) | `lib/toast-store.ts`: solo éxito y error, y el error no se cierra solo. `lib/api/server.ts:64` pasa el `message` del backend tal cual. Casi todos los formularios usan la validación nativa del navegador, que sale en inglés: solo 3 tienen `noValidate` | [UX-13](hu/HU-UX-13-avisos-y-formularios-en-espanol.md) |
| 9 | «No muestra nada», «Parece mostrar algo, pero no se ve» (Ayuda de los campos con teclado y al tocar) | Mismo recorte del tooltip; además no abre al tocar en el celular | UX-13 |
| 10 | «mejorar … los mensajes de alerta o informativos para … saber por qué no se puede vincular» (Dispositivos y auditoría) | Al vincular el IMEI y el WhatsApp de un gestor, el error no explica la causa | UX-13 |
| 11 | «el icono de plegable vaya al lado del logo» (Barra plegada; Barra plegable, paso 2) | El botón está al pie del sidebar (`sidebar.tsx`, «Plegar menú») | [UX-14](hu/HU-UX-14-shell-v2-y-perfil.md) |
| 12 | «abajo fijo … avatar y nombre de usuario … menú flotante para cerrar sesión, cambiar dark o light, abrir perfil, con opción de editar datos de perfil» | El nombre, el tema y «Salir» están en `components/shell/topbar.tsx`. No hay página de perfil. El core solo expone `/admin/me` | UX-14 |
| 13 | «queremos que [las tabs] estén arriba del título de la subsección» (Migas, pestañas y vista en celular, paso 3; captura de Cobranza › Juana Perez) | `components/ui/page-header.tsx` pinta migas › título › descripción › pestañas | UX-14 |
| 14 | «evitar tanto contenido en esta sección porque queda muy abajo el resumen» (Resumen con indicadores) | `dashboard/page.tsx` pone la Bienvenida y el banner de plantillas antes de las 4 tarjetas | UX-14 |
| 15 | «en la columna de acciones … botones de iconos como en las demás secciones» (Negocios); «botones de iconos para desactivar y cambiar contraseña» (Colaboradores) | Un botón de texto «Acciones» que abre un diálogo (`tenant-actions.tsx`, `collaborator-actions.tsx`). Cobranza ya usa `ui/icon-action.tsx` | UX-14 |
| 16 | Promesas «puede tener filtros de búsqueda y la opción de consultar la promesa en forma de modal»; elegir a «Juana» no abre Promesas (Buscar un cliente desde la paleta, paso 2) | `cobranza/promesas/page.tsx` es una tabla sin filtros ni detalle. `lib/shell/paleta.ts` (`rutaDeResultado`, tipo `promesa`) lleva a la ficha del cliente | [UX-18](hu/HU-UX-18-listas-y-formularios-de-seccion.md) |
| 17 | «Puede ser más interactivo, que no parezca tan largo» (Formulario de configuración por schema) | `components/domain/json-schema-form.tsx` agrupa por `x-group`, pero los schemas de los packs no lo traen | UX-18 |
| 18 | «falta un poco más de información en la sección» (Cobro de la plataforma, dos canales) | La página solo lista los cobros. Falta explicar el canal y el estado de cada cobro | UX-18 |
| 19 | «no se ve donde apagar un guardrail» (Pausar, guardrails y versiones, paso 2) | Están en Configuración › General › Avanzado, sin enlace desde Agentes | UX-18 |
| 20 | «No aparece» el paso de la habilidad sin configurar (Una habilidad sin configurar aparece como paso) | `lib/primeros-pasos.ts` traduce `sin_habilidad`, pero no un paso «configurar la habilidad» activa | UX-18 |
| 21 | «un sistema de notificaciones en el panel y en la apk para todos esos reportes de modificación, creación, ejecución, generación, descarga» (Negocios, paso 2) | No existe ([HU-UI-13](../SPEC-13-vistas-profesionales/spec.md) está parqueada) | [UX-19](hu/HU-UX-19-centro-de-notificaciones.md) |
| 22 | «Queremos que con 10 preguntas se pueda configurar un agente»; «en forma de pop up apenas inicio sesión por primera vez … wizards» (Un usuario sin contexto, pasos 2 y 4) | Las plantillas de AOS-24 traen superpoderes y frases, pero no un guion. La Bienvenida (`components/domain/bienvenida.tsx`) solo lista primeros pasos | [AOS-48](hu/HU-AOS-48-onboarding-con-guion-por-agente.md) |
| 23 | «un pack de rag con la posibilidad de adjuntar conocimiento, configurar el tipo de rag y las variables» (Cerebro, memoria y herramientas, paso 2) | Solo existe `rag_top_k` global en `core/config/settings.py`. No hay ingesta ni búsqueda por agente | [AOS-49](hu/HU-AOS-49-pack-de-conocimiento.md) |
| 24 | «que cada pack tenga sus habilidades internamente y no tener una lista de habilidades en toda la configuración del core» (paso 3) | AOS-16 (parte 1, core #466) instala por conexión, pero no lo dice | Nota en [HU-AOS-16](../SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md) |
| 25 | «un listado de proveedores y de acuerdo al proveedor … un modelo … con el costo … por tokens o por mensaje» (paso 1) | `GET /admin/agent-models` (`core/api/routers/agent_editor.py`) da el precio por Mtok y por 1000 turnos. El proveedor es el del negocio | Nota en [HU-AOS-24](../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) + D-SPEC-31-3 |
| 26 | «mejorar un poco la interacción del agente» (Cancelar o modificar un pedido) | pack_commerce no tiene tools de cancelar ni de modificar | Nota en [HU-COM-09](../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-09-modificar-pedido.md) |
| 27 | APK: Negocios «No tiene búsqueda» y «Solo activar o desactivar»; «No se ven los bloques de precarga»; «No se ve aviso de que pueden estar desactualizados»; «no vi donde agregar notas a una cartera» | `HerramientasScreen.tsx` llama `cargarNegocios(api)` sin `q`. Inicio usa `ActivityIndicator`. La vista admin de cartera no tiene notas, aunque existe `/pack/cobranza/portfolios/{id}/notes` | [UX-20](hu/HU-UX-20-apk-lo-que-falto-del-ciclo.md) |
| 28 | Panel clásico: «No funcionan los estilos», «Aparece not found» | Decisión pendiente: descontinuar o arreglar | D-38 (pregunta al dueño) |
| 29 | Pruebas confusas: alta automática, contraseñas nuevas, tecla A, datos que faltan («queremos que las pruebas sean lo más flexibles posibles, para cualquier tipo de público») | Es del catálogo, no del producto | Catálogo de pruebas: reescritura en lenguaje de usuario con `requiere` |

## Componentes y flujo

### Qué se toma de agent-sale y qué no

agent-sale es el producto anterior del dueño. Su panel es HTML hecho en el servidor (`src/admin/adminPanel.ts`) y **no tiene tiempo real**: cada acción recarga la página, y la conversación elegida va en `?c=` (`:3707-3712`). Por eso «sin refrescar» se construye nuevo. Lo que sí se toma:

| De agent-sale | Evidencia | En SolversHub |
|---|---|---|
| Bandeja de dos columnas: lista de 320 px con nombre, último mensaje (64 caracteres), hora, costo y etiqueta «canal · proveedor»; hilo con burbujas | `adminPanel.ts:3714-3951`, CSS `.inbox` `:1630-1666`, `conversacionCanalChip` `:3680` | UX-15 |
| Tickets: tomar, resolver y devolver al bot; la caja de respuesta solo mientras un humano atiende; ventana con motivo, resumen y asignado | `:3843-3910`; rutas en `src/gateway/server.ts:368-424` | UX-15 (el modelo ya tiene `Escalation.assigned_admin_id`, `models.py:902`, sin uso) |
| Llamadas a herramientas visibles en el hilo; costo y tokens por conversación | `src/advisor/handoffView.ts:51-70`; `adminPanel.ts:3918` | UX-15 |
| Motivos con lista cerrada, etiqueta y color, y filtro | `src/orchestrator/toolDefinitions.ts:299-318`; `HANDOFF_REASON_LABEL/CHIP` `adminPanel.ts:4554-4583`; filtro `:4704` | UX-17 |
| Cliente con identidad por canal, datos que se completan, bot pausado por cliente | migraciones `0046`, `0050`, `0054`; `src/orchestrator/memory.ts:52-70`; `crear_pedido` con `existing_data/missing_fields` | UX-16 (SolversHub ya tiene `Customer.bot_paused`, `attributes` y `memory_facts`) |
| Clasificación nuevo, ocasional, frecuente, fiel o inactivo, calculada al vuelo | `clasificarCliente`, `src/domains/commerce/aplicarPromocion.ts:97-140` | UX-16, la aporta pack_commerce (D-SPEC-31-2) |
| Leads con interruptor del bot, filtros (canal, estado, clasificación, ciudad), edición en ventana y CSV | `renderLeadsPage` `adminPanel.ts:4142-4286`; `server.ts:433-484` | UX-16 |

Lo que no tiene ninguno de los dos, y no se pidió: etiquetas, respuestas rápidas, adjuntos desde el panel y búsqueda dentro del chat. Sí se suman las **notas internas**: el core ya guarda las del bot en `conversation.state.notes` (`set_conversation_note`, `core_skill.py:121-133`), pero el panel no las muestra.

### Bandeja en vivo (UX-15)

```
Panel (cliente)                         BFF Next (/api)                 core
ListaDeChats ──cada 10-15 s──► GET /api/conversations?...──────► GET /admin/conversations (último msg, conexión, orden por actividad)
HiloEnVivo  ──cada 3-5 s, pestaña visible──► GET /api/conversations/{id}/messages?after=ts ─► GET /admin/conversations/{id}/messages?after=
Acciones (tomar/resolver/devolver/nota/responder) ──► POST /api/... ──► POST /admin/conversations/{id}/... y /admin/escalations/{id}/...
```

Se usa `document.visibilityState`: con la pestaña oculta no se consulta. Al volver se trae todo lo que llegó después del último mensaje.

## Datos (tablas, migraciones, RLS)

| HU | Cambio | Migración |
|---|---|---|
| UX-15 | Ninguna tabla nueva. Las notas de personas van en `conversation.state.notes` con `source="human"`. `Escalation.assigned_admin_id` ya existe | No |
| UX-16 | Ninguna tabla nueva. La edición pasa por `core/memory/facts.py` (único escritor de `memory_facts` y `Customer.attributes`) con `source="human"`; `bot_paused` ya existe | No |
| UX-17 | `Escalation.reason` sigue siendo texto: el código se guarda como `tool:<código>`. Opcional: un `CHECK` sobre los prefijos | No (o una chica) |
| UX-14 | `admins.display_name`, si no existe (verificar en `models.py`) | Quizá una chica |
| UX-19 | Tabla `notifications` (`tenant_id`, `admin_id` nullable para «todo el negocio», `tipo`, `titulo`, `cuerpo`, `href`, `leida_en`, `creada_en`) con RLS forzada, policy con `nullif` e índice `(tenant_id, admin_id, leida_en)` | Sí |
| AOS-49 | Tablas del pack: `knowledge_documents` y `knowledge_chunks` con `embedding vector(n)`, ambas con `tenant_id` + RLS y un índice HNSW/IVFFlat | Sí (en el pack) |

## API

| HU | Endpoint |
|---|---|
| UX-15 | `GET /admin/conversations` con `last_message`, `last_message_at`, `connection_label`, `connection_provider`, orden por actividad y `?connection_id=`; `GET /admin/conversations/{id}/messages?after=`; `ConversationDetail` con la escalación activa y las notas; `POST /admin/escalations/{id}/take`, `…/return-to-bot`; `POST /admin/conversations/{id}/notes` |
| UX-16 | `POST /admin/leads/{id}/toggle-bot`; `GET /admin/leads/{id}`; `PATCH /admin/leads/{id}`; `GET /admin/leads?channel=&connection_id=&clasificacion=`; `GET /admin/leads.csv` |
| UX-17 | `escalate_to_human(motivo: enum, detalle: str)`; `EscalationItem.reason_code` y `reason_label`; `GET /admin/escalations?reason_code=` |
| UX-14 | `PATCH /admin/me` (nombre visible); `POST /admin/me/password` (pide la contraseña actual y revoca las otras sesiones, como ADR-0136) |
| UX-19 | `GET /admin/notifications?unread=`; `POST /admin/notifications/{id}/read`; `POST /admin/notifications/read-all`; lo mismo para la app con su token |
| AOS-48 | Las plantillas de `GET /admin/agent-templates` suman `preguntas[]`; `POST /admin/agents/from-script` aplica las respuestas |
| AOS-49 | `POST /admin/agents/{id}/knowledge` (subir), `GET`/`DELETE`; tool `buscar_conocimiento` |

## UI

- **Kit:** todo con `components/ui` y `components/templates`. Nada de hex sueltos ([SPEC-29](../SPEC-29-sistema-de-diseno-unificado/spec.md)).
- **Tooltip:** pasa a portal (UX-12). Lo usan la barra plegada, las cabeceras de tabla y la ayuda de los campos (UX-13).
- **Bandeja:** dos columnas en escritorio y una en celular, como la plantilla `ListPage` pero con la lista y el hilo en paralelo. Burbujas con los tokens de superficie. Las llamadas a herramientas, plegadas.
- **Ficha del cliente:** un `ui/sheet.tsx` reutilizable desde Clientes y desde la bandeja.
- **Bloque de usuario** al pie del sidebar: `ui/avatar.tsx` + `ui/dropdown-menu.tsx`.
- **Campana:** en la topbar, con un panel lateral.
- **APK:** el mismo bloque de usuario en `CajonPanel` y la misma lista de notificaciones. `Skeleton` y `SyncStatus` del kit.

## ADR a crear o enmendar

- **UX-17:** enmienda del ADR de escalaciones con la lista cerrada de motivos.
- **UX-19:** ADR nuevo de notificaciones (modelo, emisión desde el outbox, retención, push).
- **AOS-49:** ADR nuevo del pack de conocimiento (pgvector, ingesta, búsqueda, costo de embeddings).
- **D-SPEC-31-1:** el polling queda en el ADR de la bandeja si se escribe uno; si no, en la HU.

## Migración, despliegue y reversa

- **Ninguna URL cambia.** La bandeja sigue en `/conversaciones` (con `?c=`) y Clientes en `/leads`.
- **Reversa de UX-19 y AOS-49:** sus migraciones se revierten solo con las tablas vacías.
- **Orden de despliegue en test:** primero el core, después el panel y la APK, con la verificación habitual (`desplegar-test-agent-core`).

## Riesgos

- **Polling:** carga extra sobre el core. Se mitiga con la pestaña visible, intervalos de 3–5 s y 10–15 s, `after=` en vez del hilo completo, y un índice `(conversation_id, created_at)` (verificar que exista).
- **Tickets:** chocan con la pausa por conversación. Mientras un humano atiende, el bot queda pausado en esa conversación, como en agent-sale (`adminPanel.ts:3889-3899`).
- **Edición de clientes:** si se salta `facts.py`, rompe la invariante del único escritor. La vigila un test estático.
- **RAG:** el costo de los embeddings. En develop y en las evals va en modo replay; en producción, con un modelo barato y un tope por plan.
