# SPEC-24 · Agenda y citas

> Estado SDD: Verificada · Fase 1 · Workstream Agenda

## Problema

El pack de Calendario ya agenda sobre una **agenda interna** (ADR-0084) sin depender de Google:
`CalendarConfig.source=interno`, horarios de atención, tipos de cita y citas viven en Postgres y la
disponibilidad se calcula contra ellos (`pack_calendar_blocks`, `_local_busy`). Pero la superficie de
configuración quedó a medias: el dueño puede definir horario y tipos de cita, y ver/cancelar citas,
pero **no puede bloquear la agenda** (vacaciones, ausencia, feriados, almuerzo) aunque el modelo
`CalendarBlock` y el cálculo de disponibilidad ya lo soportan. Tampoco hay una vista única que
responda "¿qué tengo esta semana?" con citas y bloqueos juntos. El negocio real necesita cerrar días
enteros o franjas sin dejar de ofrecer las franjas libres restantes.

### Ampliación 2026-10-04: agendamiento conversacional confiable

Con [HU-CAL-01](hu/HU-CAL-01-bloqueos-de-agenda.md)/02/03 terminadas, las pruebas reales con dos prospectos en test (Rob y Juanita,
2026-10-04/05) destaparon que el asistente **agenda mal aunque la agenda esté bien**. Rutas del
backend en `develop` @ `f7820ab`:

| # | Falla observada | Causa verificada |
|---|---|---|
| 1 | "El próximo miércoles" se agendó el 21-oct (era el 7-oct) | Ningún bloque del system prompt trae la fecha actual (`core/llm/prompt_builder.py:78-137`) |
| 2 | `check_availability` consultado con 2026-02-19 y 2026-08-19 | La tool no rechaza fechas pasadas y además ofrece horas ya pasadas de hoy (`packages/pack-calendar/pack_calendar/skills.py:1206-1260`; `_free_slots` en 79-115 no compara con "ahora") |
| 3 | "Moví tu demo al 7" sin llamar `update_calendar_event` | La regex del claim `reagendada` no cubre "moví tu demo" (`pack_calendar/module.py:49-57`) |
| 4 | Confirmaciones falsas | El guardrail mide éxito con `_ok`, que solo mira la clave `error` (`core/orchestrator/loop.py:450-457`): `rejected` y `not_found` cuentan como éxito (`module.py:217-223`) |
| 5 | Escalamientos constantes (11 por `calendar_completion_check`, 1 por `persona_max_length`, 28 por `send_failed`) | Al agotar los reintentos del guardrail siempre se escala (`loop.py:500-514`), con un solo reintento por defecto (`core/orchestrator/guardrails.py:25`). Los 28 `send_failed` son de la infraestructura waweb y quedan fuera de esta spec |
| 6 | El modelo le dijo al cliente "No prometí ningún envío de correo" | Parafraseó la instrucción interna `[SISTEMA]` del reintento (`module.py:241-253`); el texto no existe en el repo |
| 7 | Correos en `queued`/`failed` | SMTP de test roto ("Connection unexpectedly closed"); es configuración, no código |
| 8 | El panel no avisa por WhatsApp al reagendar y no avisa nada al cancelar | `PATCH /appointments/{id}` solo manda correo (`pack_calendar/admin_api.py:663-744`); `POST …/cancel` no avisa ni registra la actividad (`admin_api.py:207-248`). El panel SSR legado sí avisaba (`pack_calendar/admin.py:594-626`) |
| 9 | En modo interno el cliente no recibe link de la cita | El link solo existe en modo Google (`htmlLink`, `skills.py:581,934`); en interno queda vacío |

Además, el claim `correo_enviado` exige `send_email` y su reintento le pide al modelo llamarlo
aunque el servidor ya haya enviado el correo determinista (`module.py:67-74`): riesgo de **doble
correo**. Esta ampliación ([HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md)/05/06) deja el agendamiento conversacional completo, coherente
y con el mínimo de escalamientos.

### Conexión con Google desde el panel nuevo (2026-10-05)

Durante el E2E de [HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) el usuario intentó conectar Google Calendar desde el panel nuevo y no
pudo: primero `redirect_uri_mismatch` y, al registrar en Google la URI que manda la app, un 404.

| # | Causa verificada |
|---|---|
| 1 | `api_redirect_uri()` arma `…/api/v1/pack/pack_calendar/oauth/callback`, pero el router de la API está en `/api/v1/pack/calendar` (`pack_calendar/oauth.py:50-52`, `admin_api.py`) |
| 2 | En `test.solvershub.site` el túnel manda a la API solo `/webhooks`, `/healthz` y `/api/pack/pack_cobranza`; todo `/api/v1/*` va al panel (`docs/despliegue-coolify.md:52-55`), que no tiene ruta de callback |
| 3 | El callback de la API llega sin sesión ni `X-Tenant-Id`: `load_config` y `save_tokens` no saben a qué negocio guardar los tokens |
| 4 | El flujo no usa `state`: un tercero podría hacer que un administrador vincule una cuenta de Google ajena (CSRF de OAuth) |
| 5 | Poner el calendario en modo `google` sin conexión oculta todas las tools de agenda (ADR-0072) y el asistente escala |

La URL del callback ya se había movido al retirar el panel clásico, en contra de ADR-0070; [HU-CAL-07](hu/HU-CAL-07-google-desde-el-panel.md)
lo formaliza con ADR-0093.

## Por qué importa (valor empresarial)

Un asistente de agendamiento que no puede bloquear días produce citas en feriados, en días de
vacaciones o en el almuerzo: el cliente queda mal y el negocio pierde credibilidad. La agenda interna
es además el argumento de venta de las verticales sin Google (restaurantes, retail, cobranza,
suscripciones) y la base para recordatorios y multi-sede de la Fase 2. Cerrar bien este ciclo es
condición para vender Calendario como habilidad de primera clase.

La ampliación ataca la otra mitad: un asistente que agenda el día equivocado, dice "listo" sin que
la cita exista o escala por un fallo técnico pierde la demo, que es el ingreso directo de
SolversHub, y quema la confianza del prospecto en la primera conversación. Cada escalamiento
innecesario además le cuesta tiempo humano al negocio.

## Alcance

| HU | Qué |
|---|---|
| [HU-CAL-01](hu/HU-CAL-01-bloqueos-de-agenda.md) | Bloqueos de agenda y vista semanal de citas + bloqueos |
| [HU-CAL-02](hu/HU-CAL-02-agendar-reagendar-cancelar.md) | Agendar, reagendar y cancelar demos con correo (validación dura + notificación) |
| [HU-CAL-03](hu/HU-CAL-03-calendario-visual.md) | Calendario visual tipo Google Calendar |
| [HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md) | Fecha actual en el prompt, zona horaria del negocio y respuesta neutral al agotar el guardrail (core + panel) |
| [HU-CAL-05](hu/HU-CAL-05-pack-de-agendamiento-definitivo.md) | Pack de agendamiento definitivo: fechas futuras, `find_next_available`, guardrail con evidencia real, link de la cita y avisos desde el panel |
| [HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) | Afinado del asistente de la agencia (configuración + artefacto) y E2E del agendamiento en test |
| [HU-CAL-07](hu/HU-CAL-07-google-desde-el-panel.md) | Conectar Google Calendar desde el panel nuevo (callback en el panel, `state` anti-CSRF, ADR-0093) |

## Métricas de éxito

| Métrica | Meta | Cómo se mide |
|---|---|---|
| Escalamientos por guardrail en flujos normales de agendamiento | 0 | `escalations` con `reason='guardrail'` por conversación en el E2E de [HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) |
| Fechas pasadas ofrecidas o consultadas | 0 | `audit_log` de `check_availability` / `find_next_available` en el E2E |
| Confirmaciones sin evidencia (`created`/`updated`/`cancelled` en el mismo turno) | 0 | Guardrail `calendar_completion_check` + revisión de `messages` |
| Correos de agendamiento entregados | `sent` (no `queued`/`failed`) | Estado del outbox de correo en test |
| Mensajes con instrucciones internas filtradas | 0 | Revisión de `messages` del asistente en el E2E |

## Requerimientos cubiertos

REQ-CAL-01 ([HU-CAL-01](hu/HU-CAL-01-bloqueos-de-agenda.md)/02/03/05), REQ-CAL-02 ([HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md)/05/06) y REQ-CAL-03 ([HU-CAL-07](hu/HU-CAL-07-google-desde-el-panel.md)).

## Decisiones

### D-SPEC-24-1 · Cómo se modela un bloqueo

| Opción | Pros | Contras |
|---|---|---|
| **A. Rango `start_at`/`end_at` con motivo libre (tabla `pack_calendar_blocks`)** | Ya existe el modelo y el cálculo de disponibilidad; un bloqueo cubre desde una hora hasta varios días; sin estructura extra | No distingue por tipo (vacación vs feriado) salvo por el texto del motivo |
| B. Evento "todo el día" booleano + rango | Semántica de calendario clásica | Obliga a compatibilidad con rangos parciales; más campos y estados |
| C. Recurrentes (cada semana/mes) | Cubre almuerzos y cierres fijos | Complejidad de expansión y reglas; se puede resolver con varios bloqueos puntuales en Fase 1 |

**Recomendación: A**, reutilizando `pack_calendar_blocks`. Los recurrentes (C) quedan para Fase 2 como
HU nueva si la demanda lo pide.

### D-SPEC-24-2 · Dónde vive la UI de bloqueos

| Opción | Pros | Contras |
|---|---|---|
| **A. Página propia en el pack (`/calendario/bloqueos`), escrita a mano como tipos y horario** | Coherente con las pantallas existentes del pack; control total del calendario y los rangos | Una sección más en el menú del pack |
| B. Descriptor genérico de [SPEC-16](../SPEC-16-habilidades-como-plataforma/spec.md) (`kind: "crud"`) | Menos código por pantalla | El rango fecha-hora y la vista semanal no encajan bien en el descriptor; migrar después es barato |

**Recomendación: A**. Cuando [SPEC-16](../SPEC-16-habilidades-como-plataforma/spec.md) madure, una pantalla como esta puede migrar a descriptor sin
cambiar el contrato del API.

### D-SPEC-24-3 · Cómo se mantiene sincronizada la disponibilidad

| Opción | Pros | Contras |
|---|---|---|
| **A. Reutilizar `_local_busy` (citas + bloqueos en la misma consulta)** | Una sola fuente de verdad; el agente no cambia; ya probado | El cálculo es por día; rangos multi-día se resuelven con el índice `(tenant_id, start_at)` |
| B. Materializar la agenda ocupada en una tabla aparte | Consultas más rápidas | Dos escrituras que se pueden desincronizar; más código y migraciones |

**Recomendación: A**. El agente no cambia: `check_availability` y `create_calendar_event` siguen
consultando `_local_busy`, que suma citas y bloqueos. La corrección se cubre con un test nuevo de
"bloqueo total del día → cero horarios libres".

### D-SPEC-24-4 · Quién recibe el correo de agendamiento

| Opción | Pros | Contras |
|---|---|---|
| **A. Permiso de sección dedicado `pack_calendar:notificaciones`: el cliente (`attendee_email`) + los colaboradores a los que el owner les otorgue ese permiso** | Granular; reutiliza RBAC (`AdminPermission`+`TenantUser`) sin tabla nueva; el owner lo controla | Un permiso más en el catálogo |
| B. Reusar el permiso existente `pack_calendar:citas` | Sin permiso nuevo | Menos granular: quien ve citas recibe correos aunque no quiera |
| C. Tabla nueva de destinatarios por email suelto | No exige ser colaborador | Más superficie y otra tabla que mantener |

**Recomendación: A**. El correo determinista se dispara desde el servidor al crear/reagendar/cancelar
(no depende de que el modelo llame `send_email`); el envío usa el canal SMTP (ADR-0071) y, si no hay
conexión o email, registra `notified=false` con el motivo.

### D-SPEC-24-5 · Dónde vive la zona horaria del negocio

| Opción | Pros | Contras |
|---|---|---|
| **A. Columna `app_settings.timezone` (default `America/Bogota`, migración core 0050)** | Una zona por negocio para todo el core (prompt, horario de atención); se edita en Configuración → Identidad; no depende de tener un pack activo | Convive con `CalendarConfig.timezone` del pack: hay que mantenerlas alineadas |
| B. Reusar `CalendarConfig.timezone` del pack | Ya existe y la usa el cálculo de slots | El core no puede depender de un pack (invariante 5); sin pack de calendario no habría fecha correcta |
| C. Reusar `escalation_config.business_hours.tz` | Ya se edita en el panel | Solo se guarda si hay rangos de atención (`core/api/routers/settings.py:321-324`); sin rangos se descarta en silencio |

**Recomendación: A.** · **Estado:** ✅ tomada (confirmada por el usuario, 2026-10-04). El input libre
"Zona horaria" del panel (`business_tz`) se reemplaza por un selector ligado a `app_settings.timezone`
y el horario de atención la reutiliza. `CalendarConfig.timezone` sigue mandando dentro del pack;
[HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) verifica que ambas coincidan en el tenant. Se registra en ADR-0091.

### D-SPEC-24-6 · Cómo llega la fecha actual al modelo

| Opción | Pros | Contras |
|---|---|---|
| **A. La instrucción ("usá esta fecha… nunca fechas pasadas") en playbooks versionados (`core/playbooks/reglas-operacion.md` y `citas.md`) y solo el dato ("Hoy es miércoles, 7 de octubre de 2026 — 15:04 (America/Bogota).") en el bloque dinámico final** | Cumple la invariante 3; la instrucción queda en el prefijo cacheable; el dato va al final y no invalida el caché (`docs/PROMPT-CACHING-GUIDE.md:18-31`) | La regla de `reglas-operacion` no llega a un tenant que sobrescribió ese playbook (por eso también va en `citas.md`) |
| B. Bloque completo con instrucciones armado en `prompt_builder.py` | Un solo lugar; es lo que proponía la misión | Rompe la invariante 3 (texto de instrucción al LLM en `.py`) |
| C. Interpolar la fecha en un playbook estático | Simple | Cambia el prefijo cada minuto: rompe el prompt caching |

**Recomendación: A.** · **Estado:** ✅ tomada (2026-10-04). Se registra en ADR-0091.

### D-SPEC-24-7 · Qué hacer cuando se agotan los reintentos del guardrail

| Opción | Pros | Contras |
|---|---|---|
| **A. `behavior_config.guardrail_fail_action`: `escalate` (default, comportamiento actual) o `neutral` (responde la sección `verifying` de `respuestas.md`, no escala y cuenta el turno como no resuelto)** | Por negocio; no cambia a nadie que no lo active; el autoescalado por turnos sin resolver sigue de red | Con `neutral` el cliente recibe "déjame verificar" sin que nadie haga seguimiento proactivo hasta su siguiente mensaje o el autoescalado |
| B. Siempre escalar (hoy) | Conservador | 11 escalamientos por `calendar_completion_check` en la prueba: el bot se pausa por un fallo que un reintento resolvía |
| C. Nunca escalar | Cero escalamientos | Un fallo persistente deja al cliente sin salida |

**Recomendación: A**, con `guardrail_max_retries=2` y `auto_escalate_after_turns=3` en el tenant de
test. · **Estado:** ✅ tomada (confirmada por el usuario, 2026-10-04). Se registra en ADR-0092.

### D-SPEC-24-8 · Qué cuenta como evidencia en el guardrail de calendario

| Opción | Pros | Contras |
|---|---|---|
| **A. El `status` real del resultado del turno, por claim (`created`, `updated`, `cancelled`, `email_sent`, listado OK)** | Una confirmación solo pasa si la acción ocurrió de verdad; `rejected`/`not_found`/`needs_data` no respaldan nada | Acopla el guardrail a los `status` de las tools del propio pack (aceptable: mismo pack) |
| B. `_ok` genérico (hoy) | Uniforme entre packs | `rejected` y `not_found` cuentan como éxito |
| C. Solo el nombre de la tool llamada | Muy simple | Llamar y fallar pasa como si hubiera funcionado |

**Recomendación: A.** · **Estado:** ✅ tomada (2026-10-04).

### D-SPEC-24-9 · Link de la cita en modo interno

| Opción | Pros | Contras |
|---|---|---|
| **A. URL de plantilla de Google Calendar (`calendar.google.com/calendar/render?action=TEMPLATE…`)** | Sin infraestructura nueva; funciona en WhatsApp y en correo; el cliente agrega la cita a su calendario en un clic | Pensado para Google; en otros calendarios abre la web de Google |
| B. Archivo `.ics` adjunto al correo | Estándar, sirve para cualquier calendario | No llega por WhatsApp; requiere adjuntos en el outbox de correo |
| C. Página pública propia de la cita | Control total, permite reagendar | Endpoint público nuevo, firma de enlaces y superficie de seguridad |

**Recomendación: A**, también en el correo. · **Estado:** ✅ tomada (confirmada por el usuario, 2026-10-04).

### D-SPEC-24-10 · Aviso al cliente cuando el negocio mueve o cancela desde el panel

| Opción | Pros | Contras |
|---|---|---|
| **A. Correo + WhatsApp best-effort cuando `notify` es true, también al cancelar (paridad con el panel legado)** | El cliente se entera por el canal donde conversa; reutiliza `_send_client_notice` y `_notify_appointment_email` | Si la conversación está pausada o cerrada no sale el WhatsApp (se informa en la respuesta) |
| B. Solo correo (hoy, y solo al mover) | Sin cambios | Al cancelar no avisa nada, aunque el panel promete el correo |
| C. Sin aviso | Mínimo | El cliente llega a una cita que ya no existe |

**Recomendación: A.** · **Estado:** ✅ tomada (2026-10-04).

### D-SPEC-24-11 · Dónde se recibe el retorno de Google (callback OAuth)

| Opción | Pros | Contras |
|---|---|---|
| **A. Ruta BFF del panel `/api/calendar/oauth/callback`, que reenvía a la API con la sesión y el negocio del panel** | Llega por el mismo dominio que el panel (sin tocar el túnel); el navegador trae la cookie de sesión (`SameSite=Lax`), así que la API sabe el negocio; mismo patrón que el `start` actual | Una ruta más en el panel; la API ve el callback como una petición autenticada del BFF |
| B. Regla del túnel que mande `/api/v1/pack/calendar/oauth/callback` a la API | Sin código en el panel | Depende de la configuración de Cloudflare en cada entorno; el callback sigue sin sesión (no resuelve el negocio) |
| C. Volver a la ruta clásica `/admin/plugins/pack_calendar/oauth/callback` | Es la URI que ADR-0070 suponía registrada | El panel SSR se retiró (ADR-0076); revivirlo solo para esto y sigue sin resolver el negocio |

**Recomendación: A.** · **Estado:** ✅ tomada (confirmada por el usuario, 2026-10-05). Se registra en
ADR-0093 (supersede la parte de ADR-0070 que fijaba la URL del callback).

### D-SPEC-24-12 · Cómo se protege el OAuth contra CSRF

| Opción | Pros | Contras |
|---|---|---|
| **A. `state` aleatorio en `/oauth/start`, guardado en cookie `oauth_state` (httponly, `SameSite=Lax`, 10 min) y comparado en el callback** | Es lo que pide el estándar OAuth 2.0; barato; no requiere tabla | El callback falla si el navegador bloquea cookies (se informa como `google=error`) |
| B. Solo la cookie `oauth_next` (hoy) | Ya existe | No liga el retorno con quien inició el flujo |
| C. `state` firmado (HMAC) con el negocio y la fecha, sin cookie | Sin cookie | Hay que manejar la clave y su rotación; más código para el mismo resultado |

**Recomendación: A.** · **Estado:** ✅ tomada (2026-10-05).

## Riesgos y notas

- Reutiliza `pack_calendar_blocks` (sin migración nueva); el riesgo es de UI, no de datos.
- El modo `google` no usa bloqueos internos: la pantalla debe explicarlo, no deshabilitarse en silencio.
- La vista semanal debe respetar RLS y no exponer datos de otro negocio (test cross-tenant).
- **Ampliación ([HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md)/05/06):** la única migración es core `0050` (columna en `app_settings`,
  sin tabla nueva). Los riesgos de conducta (modo `neutral` sin seguimiento proactivo, umbral de 3
  turnos sin resolver en charlas sin tools, zona del pack distinta de la del negocio) están en
  [design.md](design.md#riesgos-de-la-ampliación).

## Fuera de alcance

- Los 28 `send_failed` de la infraestructura waweb (canal), que se tratan aparte.
- La consulta de disponibilidad en modo Google sigue pidiendo el día en UTC (`skills.py:1219-1220`);
  se anota como deuda.
- Recordatorios automáticos antes de la cita y bloqueos recurrentes (Fase 2).
