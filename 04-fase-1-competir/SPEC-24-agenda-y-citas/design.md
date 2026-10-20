# SPEC-24 · Diseño

| Paso | Backend | Panel |
|---|---|---|
| Bloqueos CRUD | `GET/POST/DELETE /api/v1/pack/calendar/blocks` (permiso `pack_calendar:bloqueos`) sobre `CalendarBlock` (RLS forzada) | Página `/calendario/bloqueos` con formulario de rango (inicio/fin/motivo) y tabla |
| Vista semanal | `GET /api/v1/pack/calendar/week?start=YYYY-MM-DD` (citas + bloqueos + horario del día) | `/calendario/citas` muestra citas y bloqueos en la misma línea de tiempo |
| Menú | Nueva entrada `admin_menu` `pack_calendar:bloqueos` | `nav.ts` ítem "Bloqueos" bajo Calendario |
| Disponibilidad | `_local_busy` ya suma `pack_calendar_blocks`; sin cambios en `skills.py` | — |
| Contratos | Tests de capa + RLS del CRUD de bloqueos; test de "día totalmente bloqueado → 0 slots" | Tests de serialización y estado vacío |

Tablas afectadas: `pack_calendar_blocks` (existente, migración `0002_calendar_interno`). No requiere
migración nueva.

Pantallas del pack tras esta spec: Conexión · Horario · Tipos de cita · Bloqueos · Citas.

---

# Ampliación · Agendamiento conversacional confiable (HU-CAL-04/05/06)

Diseño de las decisiones D-SPEC-24-5 a D-SPEC-24-10 ([spec.md](spec.md#d-spec-24-5--dónde-vive-la-zona-horaria-del-negocio)).
Rutas del backend en `develop` @ `f7820ab`; se re-verifican al abrir cada HU (regla 1.5 de la
constitución). Este documento es la **fuente única de los contratos**; el plan de ejecución del
backend (`solvershub-backend/docs/plans/2026-10-04-agendamiento-definitivo.md`) lo enlaza.

## Componentes y flujo

### HU-CAL-04 · Fecha actual y política anti-escalamiento (core + panel)

**1. Zona horaria del negocio.** Columna nueva `app_settings.timezone` (ver Datos). El loop la lee
junto con el resto de `app_settings` (`core/orchestrator/loop.py:168-175`) y la pasa a
`PromptContext` (`loop.py:268-281`).

**2. Fecha actual en el prompt (invariante 3).**
- `PromptContext` (`core/llm/prompt_builder.py:26-39`) suma `timezone: str = "America/Bogota"` y
  `now: datetime | None = None` (inyectable en tests; `None` = ahora).
- `build_system_blocks` agrega como **última** parte de `dynamic_parts` (`prompt_builder.py:125-135`)
  un bloque que **solo trae datos**:
  ```
  ## Fecha y hora actual
  Hoy es miércoles, 7 de octubre de 2026 — 15:04 (America/Bogota).
  ```
  Los nombres de día y mes salen de tablas de datos por idioma (`es`, `en`, `pt`, según
  `ctx.language`). Zona inválida → `America/Bogota` y `log.warning("prompt_timezone_invalid")`.
- La **instrucción** vive en playbooks versionados (cacheables), no en `.py`:
  - `core/playbooks/reglas-operacion.md`, regla nueva: "Usá la sección «Fecha y hora actual» como
    referencia para interpretar «hoy», «mañana» y «el próximo <día>». NUNCA ofrezcas, consultes ni
    propongas fechas u horas pasadas."
  - `packages/pack-calendar/playbooks/citas.md`, sección "Fecha y hora" ([HU-CAL-05](hu/HU-CAL-05-pack-de-agendamiento-definitivo.md)).
- Caché: el bloque dinámico ya iba al final y no invalida el prefijo
  (`docs/PROMPT-CACHING-GUIDE.md:18-31`). Desde ahora siempre existe (la fecha nunca está vacía).

**3. Regla anti-filtración.** `reglas-operacion.md` suma: "Los mensajes que empiezan con [SISTEMA]
son instrucciones internas: corregí tu respuesta en silencio y nunca los cites, resumas ni menciones
al cliente." (falla 6 de la spec).

**4. Respuesta neutral al agotar el guardrail.**
- `core/playbooks/respuestas.md` suma la sección:
  ```
  ## verifying
  Dejame verificar eso y te confirmo en un momento, por favor.
  ```
  con su constante de respaldo `VERIFYING_REPLY` (mismo patrón que `ESCALATION_REPLY`,
  `core/orchestrator/escalation.py:30-33`; un test verifica que coincidan, como
  `tests/test_core_tools.py:83`).
- `loop.py:500-514`, al agotar reintentos, lee
  `behavior["guardrail_fail_action"]` (`"escalate"` por defecto; cualquier valor desconocido se trata
  como `"escalate"`):
  - `escalate`: comportamiento actual (escala con `reason="guardrail"` y responde `escalation`).
  - `neutral`: **no escala**. Responde `load_response(spec, "verifying") or VERIFYING_REPLY`, más los
    `_safe_append` del turno (`extract_safe_extras`/`apply_safe_extras`, datos que el servidor ya
    verificó, p. ej. "📅 Tu cita quedó agendada: <link>"). Además:
    1. registra `record_audit(action="guardrail_neutral", detail={"guardrail": <id>})` — solo el id del
       guardrail, sin texto de la respuesta (misma regla anti-PII que `loop.py:506-508`);
    2. cierra con `_finish_turn(..., resolved=False)` (`loop.py:900-930`), así que el turno **suma**
       a `turnos_sin_resolver`;
    3. escribe el ledger de uso;
    4. aplica el autoescalado por turnos sin resolver (`loop.py:527-539`), extraído a un helper para
       que lo compartan la salida normal y la neutral.
  - El borrador que falló el guardrail nunca se envía (igual que hoy).

**5. Reintentos.** El default del core sigue en `MAX_GUARDRAIL_RETRIES = 1`
(`core/orchestrator/guardrails.py:25`); el tenant de test usa 2 ([HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md)). La API alinea su
validación con el loop (0-5; hoy solo hace `max(0, …)` en `core/api/routers/settings.py:310`).

### HU-CAL-05 · Pack de agendamiento definitivo

**1. "Hoy" del pack.** Helper `_now_local(config)` = `datetime.now(ZoneInfo(config.timezone))`
(`CalendarConfig.timezone`, `pack_calendar/config.py:78`). Lo usan `check_availability`,
`find_next_available` y el filtro de horas pasadas.

**2. `check_availability`** (`pack_calendar/skills.py:1206-1260`):
- `date` < hoy → `{"status": "in_past", "today": "YYYY-MM-DD", "message": "Esa fecha ya pasó; hoy es <miércoles 7 de octubre>."}`
  sin consultar nada más.
- `date` == hoy → `free_slots` sin las horas que ya empezaron.
- La respuesta normal suma `"status": "ok"` y `"today"` (aditivo; el resto de claves no cambia).
- El cálculo por día se extrae a `_day_free_slots(date, duration, config)` para que
  `find_next_available` use exactamente la misma lógica (`_open_window`, `_local_busy` o Google,
  `_free_slots`).

**3. Tool nueva `find_next_available`** (skill `new-tool`). Mantiene el nombre en inglés de las
demás tools del pack (excepción heredada que la skill admite) y el mismo `connection_predicate`.

| Campo | Contrato |
|---|---|
| Descripción | "Próximos días con horarios libres desde hoy. Usala cuando el cliente no da fecha o pide lo más pronto. No la uses si el cliente ya dijo un día: usá check_availability." |
| Parámetros | `days` entero 1-14 (default 7); `duration_minutes` entero opcional (default `CalendarConfig.event_duration_minutes`) |
| Comportamiento | Recorre desde hoy (zona del negocio) hasta `days` días; salta días cerrados (`_open_window` = `""`) y días sin libres; corta al llegar a **5 días con disponibilidad**; hoy sin las horas ya pasadas |
| Respuesta OK | `{"status": "ok", "today": "YYYY-MM-DD", "days": [{"date": "YYYY-MM-DD", "weekday": "miércoles", "free_slots": ["15:00", "16:00"]}], "total_days": 2}` ordenado por fecha |
| Sin cupo | `{"status": "no_availability", "today": "…", "message": "No hay horarios libres en los próximos N días."}` |
| Errores | Parámetros fuera de rango → `{"error": …, "mensaje": …}` (nunca excepción, [HU-ARCH-18](../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-18-errores-de-negocio-no-apagan-packs.md)) |
| Registro | `get_tools()` + `flow.json` (sección `agendamiento`) + `citas.md` |

**4. Link "agregar al calendario"** (D-SPEC-24-9). Helper puro
`_calendar_link(start, end, title, details, tz) -> str`:
```
https://calendar.google.com/calendar/render?action=TEMPLATE
  &text=<title>&dates=<YYYYMMDDTHHMMSS>/<YYYYMMDDTHHMMSS>&ctz=<tz>&details=<details>
```
- Fechas en hora **local** de `tz` (Google las interpreta con `ctz`); todo con `urllib.parse.urlencode`.
- Modo interno: `create_event` y `update_event` lo ponen en `_safe_append` (hoy
  `skills.py:616` y `980-984`, que ya contemplan un `link`). Modo Google: sigue `htmlLink`.
- El link **no** se expone como clave aparte al modelo (el `_safe_append` se oculta al LLM,
  `core/orchestrator/safe_renderer.py:66-68`), para que no lo duplique en su texto.

**5. Correo con link** (`_notify_appointment_email`, `skills.py:807-869`):
- `values` suma `link`. Si la plantilla del tenant no tiene `{link}` y hay link, se agrega al final
  "Agregá la cita a tu calendario: {link}" (no en cancelaciones).
- Defaults de `config.py:39-58`: `email_body_confirmed` y `email_body_moved` incluyen esa línea.
- **Formato seguro:** las plantillas (correo y WhatsApp) se rellenan con `format_map` sobre un dict
  que deja literal un placeholder desconocido, en vez de `.format` (hoy un placeholder desconocido
  lanza `KeyError` sin capturar, `skills.py:842` y `798`). `{link}` también queda disponible en las
  plantillas de WhatsApp.

**6. Guardrail con evidencia real** (`pack_calendar/module.py:39-96, 198-258`, D-SPEC-24-8). Cada
claim pasa a tener un patrón **afirmativo** y uno **negativo**, evaluados contra los resultados del
**turno actual** (`_current_turn`):

| Claim | Afirmación respaldada si… | Negación ("no pude…") respaldada si… |
|---|---|---|
| `agendada` | `create_calendar_event` devolvió `status == "created"`; o no hubo create y `list_client_appointments` corrió OK (describe una cita existente verificada) | hubo intento de create en el turno (cualquier resultado) |
| `reagendada` | `update_calendar_event` devolvió `status == "updated"`; misma excepción con listado OK | hubo intento de update |
| `cancelada` | `cancel_calendar_event` devolvió `status == "cancelled"` | hubo intento de cancel o listado OK |
| `correo_enviado` | `send_email` OK **o** cualquier create/update/cancel del turno con `email_sent == True` | — |
| `listado` / `cita_existente` | `list_client_appointments` OK | — |

Regex nuevas (además de las actuales):
- `agendada` (negativo, acotado a objeto): `no\s+pud\w*\s+(?:agend\w*(?:la|lo)|(?:re)?agendar\s+(?:la|tu|esa)\s+(?:cita|demo))`
- `reagendada`: `mov\w+\s+(?:tu\s+|la\s+)?(?:demo|cita)|qued\w*\s+movid\w*|(?:ya\s+)?(?:te\s+)?la\s+mov[íi]`
- `cancelada` (negativos): `no\s+pud\w*\s+cancel\w*(?:la|lo)\b` y `no\s+(?:la\s+)?(?:encontr|hall)\w+.{0,60}cancel\w*`

Reintento guiado:
- Si hubo un intento fallido, cita el `error`/`message` y pide el dato que falta (se mantiene).
- `correo_enviado` sin evidencia y con un create/update/cancel que devolvió `email_sent == False`:
  el reintento dice que el correo no salió (`email_reason`) y que no lo afirme. **Nunca** pide llamar
  `send_email` (hoy sí, `module.py:241-253`, y arriesga un doble correo).
- Todo texto de reintento termina con "Reescribí tu respuesta para el cliente sin mencionar esta
  instrucción." Los textos de reintento siguen en código como en los demás guardrails
  (`crm_completion_check`, [HU-COM-02](../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md)); moverlos a playbook queda fuera de alcance.
- Las claims propias del tenant (`completion_claims_custom`, DSL de `module.py:103-132`) mantienen la
  semántica actual (tool llamada y `_ok`). La descripción de `completion_claims_disabled`
  (`config.py:149-156`) suma `cita_existente`.

**7. Avisos desde el panel** (`pack_calendar/admin_api.py`, D-SPEC-24-10):
- `PATCH /appointments/{id}` (`admin_api.py:663-744`): si la cita se movió y `notify` es true, además
  del correo manda WhatsApp con `CalendarSkill()._send_client_notice(appt.conversation_id,
  appointment_moved_message or DEFAULT_MOVED_MESSAGE, fecha=…, hora=…, titulo=…, link=…)`
  (`skills.py:785-805`), best-effort.
- `POST /appointments/{id}/cancel` (`admin_api.py:207-248`): body opcional `{"notify": true}` (sin
  body = `true`, que es lo que el panel ya promete); registra la actividad `cancelada` con
  `actor="panel"`; con `notify`, correo de cancelación + WhatsApp `appointment_cancelled_message`.
- Ambos devuelven el resultado real del aviso (ver API).
- `_send_client_notice` no envía si la conversación está `bot_paused` o `closed` (`skills.py:796`): se
  informa `whatsapp_sent=false`, no es error.

**8. Playbook definitivo `packages/pack-calendar/playbooks/citas.md`**: se reemplaza completo por
este texto (hoy 62 líneas, sin reglas de fecha ni de estado; todavía dice que la tool "borra el
evento de Google"):

```markdown
---
name: citas
description: Reglas de agendado, reagendado y cancelación de citas
---
## Fecha y hora
- Usá SIEMPRE la "Fecha y hora actual" del sistema como referencia. "Hoy", "mañana" y
  "el próximo <día>" se calculan desde esa fecha. NUNCA ofrezcas, consultes ni propongas fechas pasadas.
- Si el cliente no da fecha o pide "lo más pronto", usá `find_next_available` y ofrecé
  los 2-3 días más cercanos con horarios libres.

## Datos requeridos antes de agendar
- Necesitás fecha y hora exactas y el email del cliente. Si falta el email, pedíselo ANTES
  de confirmar: es obligatorio (sin email no se envía la confirmación y la tool no crea la cita).
- NUNCA inventes el email: usá solo el que el cliente escribió (o el de su perfil).
- Si la tool devuelve `needs_data` o un error, NO digas que quedó agendada: pedí el dato que
  falta y reintentá cuando lo tengas. Confirmá SOLO si devolvió `status: "created"`.

## Agendar
- Consultá con `check_availability` (la fecha que pidió el cliente) u `find_next_available`
  (sin fecha). Ofrecé SOLO horarios de `free_slots`; nunca inventes horas.
- Si hay varios servicios, elegí el tipo con `list_appointment_types`.
- Creá con `create_calendar_event` solo cuando el cliente confirmó fecha/hora exactas y tenés su email.

## Reagendar
- Usá SIEMPRE `update_calendar_event` (nunca crear una nueva).
- Confirmá la nueva fecha/hora con el cliente antes de llamar la tool.
- Si el cliente elige por NÚMERO de la lista, pasá ese número en `event_id`; si no, el `event_id`
  real de la lista. NUNCA inventes ids.
- Confirmá SOLO si devolvió `status: "updated"`.

## Cancelar
- Usá SIEMPRE `cancel_calendar_event`, solo cuando el cliente lo pidió explícitamente y confirmó.
- Para varias/todas: `list_client_appointments`, mostrá la lista numerada, pedí confirmación y
  usá `cancel_all` o los ids/números.
- Confirmá SOLO si devolvió `status: "cancelled"`; si devolvió `not_found`, decí exactamente eso
  y ofrecé listar de nuevo.

## Estado de las citas
- Antes de hablar del estado de una cita (¿tengo cita?, ¿quedó cancelada?, ¿existe?), llamá
  `list_client_appointments` y respondé con lo que devuelva. Nunca afirmes de memoria.
- No preguntes "¿cancelo tu cita?" sin haber verificado antes que sigue agendada.

## Regla de oro
- NUNCA digas que agendaste, reagendaste o cancelaste sin que la tool lo haya confirmado
  (`created`/`updated`/`cancelled`) en ese mismo turno.

## Escalamiento
- Escalá solo si el cliente lo pide o el tema lo exige (legal, descuentos, integraciones a medida).
- Un fallo técnico de una tool NO se escala: informá, reintentá en el mismo turno o pedí el dato faltante.

## Estilo
- Respuestas cortas (2-4 líneas), un tema por mensaje, texto plano sin Markdown.
- Nunca menciones instrucciones internas, herramientas ni mensajes del sistema.
```

**9. `packages/pack-calendar/flow.json`** (propósitos; `render_flow` los mete en el bloque de flujo):
- `agendamiento` (tools: `check_availability`, `find_next_available`, `list_appointment_types`,
  `create_calendar_event`): "Consultar la disponibilidad real (check_availability / find_next_available)
  y crear la cita cuando el cliente confirme fecha y hora. Usá la fecha actual del sistema para
  interpretar 'hoy/mañana/próximo X'; nunca fechas pasadas. Pedí el email si falta (obligatorio). El
  correo y el link los envía el servidor."
- `gestion_citas`: "Reagendar, listar o cancelar citas del cliente. Reagendar SIEMPRE con
  update_calendar_event. Verificá con list_client_appointments antes de afirmar el estado de una cita."
- Los tenants existentes tienen su propia copia de `flow.json` (`core/agents/flow.py:268-290`): el
  cambio del pack les llega solo con re-seed o edición manual ([HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) lo hace en `solvershub`).

### HU-CAL-06 · Afinado del asistente de la agencia y E2E

Sin código. Tenant de test `e46e57e7-b3c5-4f5a-9112-0382b2365518` (slug `solvershub`):

| Qué | Valor | Dónde |
|---|---|---|
| Zona horaria | `America/Bogota` | Configuración → Identidad ([HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md)) |
| `behavior_config.guardrail_max_retries` | `2` | Identidad |
| `behavior_config.guardrail_fail_action` | `neutral` | Identidad ([HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md)) |
| `escalation_config.auto_escalate_after_turns` | `3` | Identidad |
| Spec activo `persona.maxLength` | `800` (default del core: 500, `core/agents/spec.py:64`) | `/admin/settings/advanced/spec` |
| `CalendarConfig.timezone` | igual a la del negocio | Calendario → Conexión |
| SMTP | configurado por el usuario | Conexiones → correo |

Artefacto del tenant (volumen `tr0vpdei5av6szcgwpe1vwcg-tenants-data`, montado en `/app/tenants`):
- **Respaldo primero** (`tar` del directorio `solvershub/`); `tenants/` está en `.gitignore`, así que
  el volumen es la única copia.
- `flow.json`: propósitos de `agendamiento`/`gestion_citas` del punto 9; en `agendamiento` agregar
  `find_next_available` y **quitar `send_email`** (la copia local aún lo tiene: doble correo);
  verificar que el id sea `gestion_citas` (con guion bajo; con guion se descarta, ver [HU-CAL-02](hu/HU-CAL-02-agendar-reagendar-cancelar.md)).
- `playbooks/ventas.md`, "REGLA DURA (demo)": cambiar "con una fecha próxima si no la especificó" por
  "usá find_next_available y ofrecé los días más cercanos; usá la fecha actual del sistema, nunca
  fechas pasadas".
- Revisar si el tenant sobrescribe `reglas-operacion.md`, `respuestas.md` o `citas.md` (ADR-0026): si
  lo hace, no le llegan las reglas nuevas y hay que alinearlos.
- Los artefactos se leen en cada turno (`core/orchestrator/loop.py:253`): no hace falta reiniciar.

E2E: los 10 casos de la HU, publicando inbounds en `agent_core:inbound` y leyendo `messages`,
`audit_log` y `escalations`. El runbook (comandos, ids de conversación) está en el plan del backend.

## Datos (tablas, migraciones, RLS)

- **Core `alembic/versions/0050_app_settings_timezone.py`** (`revision="0050"`, `down_revision="0049"`),
  patrón de `0045_app_settings_currency.py`:
  `op.add_column("app_settings", sa.Column("timezone", sa.Text(), nullable=False, server_default="America/Bogota"))`;
  downgrade `op.drop_column("app_settings", "timezone")`. Postgres llena las filas existentes con el
  default sin reescribir la tabla. No crea tabla: RLS y la guarda de migraciones no cambian.
- `core/db/models.py:105` (junto a `language`): `AppSettings.timezone`.
- `behavior_config` suma la clave `guardrail_fail_action` (JSONB, sin migración).
- El pack no tiene migración nueva.

## API

| Ruta | Cambio | Compatibilidad |
|---|---|---|
| `GET /admin/settings` → `identity` | suma `timezone: str` y `guardrail_fail_action: "escalate" \| "neutral"` | aditivo |
| `PUT /admin/settings/identity` | `timezone: str \| None = None` (validado con `ZoneInfo`; inválida → 422) y `guardrail_fail_action: Literal[…] \| None = None`; `None` = no cambiar (un panel viejo no pisa la zona); `guardrail_max_retries` validado 0-5; el horario de atención usa `business_tz` o, si viene vacío, `timezone` (hoy cae a `"UTC"`, `settings.py:323`) | aditivo |
| `PATCH /api/v1/pack/calendar/appointments/{id}` | la respuesta suma `notification: {email_sent, email_reason, whatsapp_sent} \| null` | aditivo |
| `POST /api/v1/pack/calendar/appointments/{id}/cancel` | body opcional `{"notify": bool}` (default `true`); responde 200 `{"status": "cancelled", "notification": {…}}` en vez de 204 | el panel solo mira `res.ok` |

OpenAPI regenerado con `uv run --extra dev python scripts/export_openapi.py` y tipos del panel con
`make api-types`.

## UI

- **Configuración → Identidad** (`solvershub-panel/apps/panel-web/app/(app)/configuracion/_components/identity-form.tsx`):
  - el input libre "Zona horaria" (`:270-276`, `business_tz`) pasa a un Select "Zona horaria del
    negocio" ligado a `timezone` (patrón del Select de moneda, `:28-33` y `:238-254`), con las zonas
    de LatAm más usadas + `UTC`; también se envía como `business_tz`;
  - Select "Si el asistente no logra corregir su respuesta" → "Escalar a una persona" / "Responder
    que va a verificar" (`guardrail_fail_action`), junto a "Reintentos".
- **Calendario → Citas** (`citas/_components/appointment-panel.tsx`): reemplazar el texto fijo
  "Guardado y avisado." (`:82`) por el resultado real ("Avisado por correo y WhatsApp", "Correo no
  enviado: sin conexión SMTP", …); cancelar (`:105-115`) muestra el mismo resumen.
- Repo `solvershub-panel`, rama base `main`; CI: typecheck, lint, build y gitleaks.

## ADR a crear o enmendar

| ADR (backend `docs/adr/`) | Decisión | HU |
|---|---|---|
| ADR-0091 · Fecha actual en el prompt y zona horaria del negocio | `app_settings.timezone`; instrucción en playbook y dato en el bloque dinámico final; relación con `CalendarConfig.timezone` y `business_hours.tz` | [HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md) |
| ADR-0092 · Fallo de guardrail con respuesta neutral configurable | `guardrail_fail_action`; turno no resuelto, audit y autoescalado como red | [HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md) |

Se apoyan en ADR-0084 (calendario interno), ADR-0050/0051 (persona y autoescalado) y ADR-0026
(override de playbooks por tenant). Ninguno cambia contratos de `agentcore_contracts`.

## Pruebas por HU

| HU | Unitarias | Integración (`AGENT_CORE_INTEGRATION=1`) | Evals |
|---|---|---|---|
| [HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md) | bloque de fecha (día/mes por idioma, zona inválida, siempre último bloque) en `tests/test_agent_spec.py`; `verifying` = constante | `test_guardrail_retries_per_tenant.py`: con `neutral` responde `verifying`, no crea `escalations`, deja audit `guardrail_neutral` y suma `turnos_sin_resolver`; con `escalate` (y sin clave) escala como hoy; autoescalado tras N turnos neutrales; API: `timezone` inválida → 422, `None` no pisa; migración `0050` sube y baja | — |
| [HU-CAL-05](hu/HU-CAL-05-pack-de-agendamiento-definitivo.md) | `tests/test_calendar_slots.py`: filtro de horas pasadas y `_calendar_link` (codificación, `ctz`); `tests/test_pack_calendar_completion_guardrail.py`: "moví tu demo" sin tool falla; create `rejected`/`needs_data` no respalda; correo respaldado por `email_sent`; listado respalda la descripción; negativo con intento fallido pasa; el reintento de correo nunca nombra `send_email`; `tests/test_pack_calendar_claims_dsl.py` con `cita_existente` | `tests/integration/test_calendar_interno.py`: fecha pasada → `in_past`; `find_next_available` ordenado, salta cerrados y bloqueados, tope de 5; link en el `_safe_append` de create/update; cuerpo del correo con link; PATCH/cancel del panel con `notify` → correo + intento de WhatsApp + actividad `cancelada`; **cross-tenant** (las citas de otro negocio no ocupan horarios) | golden "sin fecha → `find_next_available`" y "fecha pasada no se ofrece" (`eval-author`) |
| [HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) | — | — | E2E en test (10 casos) + `eval-runner` sobre el golden del tenant |

## Migración, despliegue y reversa

1. **[HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md)**: PR backend → merge a `develop` → deploy a test con `desplegar-test-agent-core`
   (verificar `alembic_version = 0050`, healthz y login) → PR panel → deploy del panel de test con
   `desplegar-test`.
2. **[HU-CAL-05](hu/HU-CAL-05-pack-de-agendamiento-definitivo.md)**: PR backend (pack + OpenAPI) → deploy a test → PR panel (resultado del aviso) → deploy.
3. **[HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md)**: configuración y artefacto del tenant, SMTP, E2E y cierre documental.

Reversa:
- [HU-CAL-04](hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md): el modo neutral se apaga por configuración (`guardrail_fail_action=escalate`); la columna
  se quita con `alembic downgrade 0049` solo **después** de revertir el código que la lee.
- [HU-CAL-05](hu/HU-CAL-05-pack-de-agendamiento-definitivo.md): `git revert` del PR (sin migración).
- [HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md): restaurar el `tar` de respaldo del artefacto y los valores previos de configuración.
- Producción (`ggzjdyc7zsemt6kzafx5rg7m`) no se toca en ninguna de las tres HU; llega con la skill
  `release`.

## Riesgos de la ampliación

| Riesgo | Mitigación |
|---|---|
| Con `neutral` el cliente recibe "déjame verificar" y nadie hace seguimiento proactivo | Autoescalado tras 3 turnos sin resolver; audit `guardrail_neutral` para medirlo; queda como mejora un aviso interno sin pausar el bot |
| El autoescalado cuenta como "no resuelto" todo turno sin tools (saludo, pedir el email): una charla de 3 turnos sin tools escala | Medirlo en el E2E (caso 10); si pasa en flujos normales, subir el umbral en el tenant |
| La zona del pack (`CalendarConfig.timezone`) y la del negocio (`app_settings.timezone`) difieren y "hoy" no coincide entre prompt y tools | [HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) las verifica iguales; ADR-0091 documenta la precedencia |
| Un tenant con `reglas-operacion.md`/`respuestas.md` propios no recibe las reglas nuevas | La regla de fecha también va en `citas.md`; `VERIFYING_REPLY` de respaldo; [HU-CAL-06](hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) revisa los overrides |
| Anthropic: el proveedor pone `cache_control` en **cada** bloque (`core/llm/anthropic_provider.py:56-61`) y la API acepta como máximo 4; con 4 playbooks + voz + flujo + bloque dinámico se pasa del límite | Fuera de alcance (el modelo por defecto es DeepSeek); verificar antes de activar Anthropic en un tenant |
| `find_next_available` en modo Google hace hasta 14 consultas a la API | Tope `days ≤ 14`; corta en 5 días con cupo |
| Panel-triggered WhatsApp a una conversación pausada no sale | Se informa `whatsapp_sent=false` en la respuesta y en el panel |

## Conexión con Google desde el panel (HU-CAL-07)

Decisiones D-SPEC-24-11 (callback en el panel) y D-SPEC-24-12 (`state` anti-CSRF). ADR-0093
supersede la parte de ADR-0070 que fijaba el callback en `/admin/plugins/pack_calendar/oauth/callback`.

### Flujo

```
Panel  /calendario  "Conectar con Google"
  └─▶ GET /api/calendar/oauth?next=/calendario            (BFF del panel, con sesión)
        └─▶ GET API /api/v1/pack/calendar/oauth/start     (Bearer + X-Tenant-Id)
              · genera state aleatorio; Set-Cookie oauth_state + oauth_next (httponly, Lax, 10 min, path=/)
              · 302 → accounts.google.com …&redirect_uri=<PANEL>/api/calendar/oauth/callback&state=…
Google (el usuario autoriza o cancela)
  └─▶ GET <PANEL>/api/calendar/oauth/callback?code=…&state=…   (BFF del panel, NUEVO)
        · el navegador trae panel_session + panel_tenant + oauth_state + oauth_next (mismo dominio)
        · sin sesión → 302 /login?next=/calendario (no se procesa nada)
        └─▶ GET API /api/v1/pack/calendar/oauth/callback?code&state&error
              (Bearer + X-Tenant-Id + Cookie: oauth_state, oauth_next)
              · exige principal pack_calendar:conexion (escritura) → tenant_scope del negocio
              · state ≠ cookie (comparación en tiempo constante) o sin cookie → google=error, sin intercambio
              · error/cancelado → google=cancelado
              · exchange_code(redirect_uri=<PANEL>/api/calendar/oauth/callback) + save_tokens (conexión del negocio)
              · borra oauth_state y oauth_next; 302 → <PANEL><next>?google=ok|error|cancelado
        · el BFF propaga el 302 y los Set-Cookie al navegador
```

### Cambios

| Dónde | Cambio |
|---|---|
| `packages/pack-calendar/pack_calendar/oauth.py` | `panel_redirect_uri()` = `{PANEL_BASE_URL or PUBLIC_BASE_URL}/api/calendar/oauth/callback` (reemplaza `api_redirect_uri()`, que apuntaba a una ruta inexistente); `build_authorization_url(..., state=…)` |
| `packages/pack-calendar/pack_calendar/admin_api.py` | `/oauth/start`: `state = secrets.token_urlsafe(32)`, cookie `oauth_state`; `/oauth/callback`: `Depends(require("pack_calendar:conexion", write=True))`, validación del `state` con `hmac.compare_digest`, borrado de cookies, mismos destinos `google=ok|error|cancelado` |
| `solvershub-panel` `app/api/calendar/oauth/callback/route.ts` (nuevo) | GET: sin `panel_session` → login; si no, reenvía la query a la API con `Authorization`, `X-Tenant-Id` y `Cookie` (solo `oauth_state`/`oauth_next`), `redirect: "manual"`; propaga `Location` y `Set-Cookie` |
| `docs/openapi.json` | regenerado (el callback ahora exige autenticación) |
| `packages/pack-calendar/CALENDAR.md` | URI a registrar por entorno y pasos en Google Cloud Console |

URIs a registrar en Google Cloud Console (cliente OAuth del negocio → "URIs de redireccionamiento
autorizados"): test `https://test.solvershub.site/api/calendar/oauth/callback`; producción
`https://app.solvershub.site/api/calendar/oauth/callback` (o el dominio del panel de producción si
`PANEL_BASE_URL` difiere).

### Pruebas

| Tipo | Casos |
|---|---|
| Unitarias | `panel_redirect_uri()` con y sin `PANEL_BASE_URL`; la URL de autorización lleva `redirect_uri` del panel y `state` |
| Integración (`AGENT_CORE_INTEGRATION=1`) | start → setea `oauth_state` y el `state` de la URL coincide; callback sin `state`/con `state` distinto → `google=error` sin llamar a Google; callback correcto con `exchange_code` simulado → conexión `google_calendar` en el negocio del principal y no en otro (cross-tenant); `error=access_denied` → `google=cancelado`; sin autenticación → 401 |
| Panel | typecheck/lint/build; prueba manual en test con la cuenta del usuario |

### Despliegue y riesgos

- Orden: backend → panel → registrar la URI en Google Cloud Console → probar en test con el calendario
  en modo `interno` (cambiar a `google` solo después de conectar).
- Riesgo: si `PANEL_BASE_URL` y `PUBLIC_BASE_URL` apuntan a dominios distintos, la URI registrada
  debe ser la del panel. Se verifica en cada entorno antes de registrar.
- Riesgo: navegadores que bloquean cookies de primera parte en redirecciones → `google=error`; el
  panel lo muestra con el texto de reintento existente.
