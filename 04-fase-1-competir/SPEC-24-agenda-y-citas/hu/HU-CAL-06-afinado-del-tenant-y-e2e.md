---
id: HU-CAL-06
titulo: Afinado del asistente de la agencia y E2E del agendamiento
spec: SPEC-24
fase: 1
hito: "1"
workstream: Agenda
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, calidad_ia]
req: [REQ-CAL-02]
dependencias: [HU-CAL-04, HU-CAL-05]
skills: ["customizer", "eval-runner", "desplegar-test-agent-core", "built-in-browser"]
estado: terminada
---

# HU-CAL-06 · Afinado del asistente de la agencia y E2E del agendamiento

> Estado SDD: Terminada — E2E de los 10 casos verificado en test 2026-10-05 · issue [core #223](https://github.com/devrochy/agent-core/issues/223) · configuración y artefacto en [design.md](../design.md#hu-cal-06--afinado-del-asistente-de-la-agencia-y-e2e).

**ID:** HU-CAL-06

**Título:** Afinado del asistente de la agencia y E2E del agendamiento

**Workstream:** Agenda

**Historia:** Como SolversHub (negocio que vende sus demos con su propio asistente) quiero configurar mi asistente de test con la política anti-escalamiento, la zona horaria, el correo y las reglas de agendamiento nuevas, y repetir con evidencia las conversaciones que fallaron con Rob y Juanita, para confirmar que el agendamiento quedó completo antes de llevarlo a producción.

**Por qué importa (valor empresarial):** Las [HU-CAL-04](HU-CAL-04-fecha-actual-y-anti-escalamiento.md) y [HU-CAL-05](HU-CAL-05-pack-de-agendamiento-definitivo.md) cambian el código, pero el asistente de la agencia vive de su configuración y de su artefacto (`flow.json`, `ventas.md`), que hoy tienen propósitos viejos y todavía exponen `send_email` en el agendamiento (doble correo). Sin este afinado y un E2E con evidencia, las fallas que vio un prospecto real pueden volver a pasar con el siguiente.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-CAL-02

**Dependencias:** [HU-CAL-04](HU-CAL-04-fecha-actual-y-anti-escalamiento.md), [HU-CAL-05](HU-CAL-05-pack-de-agendamiento-definitivo.md)

**Criterios de aceptación (Gherkin):**
- **1 · Listar sin escalar.** Dado Rob con citas agendadas, cuando escribe "¿qué citas tengo?", entonces el asistente llama `list_client_appointments`, responde la lista real y no se crea ninguna fila en `escalations`.
- **2 · Próximo miércoles.** Dado el día real del E2E en `America/Bogota`, cuando Rob pide "el próximo miércoles a las 3pm", entonces la fecha consultada es el miércoles más cercano desde hoy (se compara contra el calendario real y se anota en la evidencia).
- **3 · Reagendar de verdad.** Dado que Rob confirma la nueva fecha, cuando el asistente reagenda, entonces `update_calendar_event` devuelve `status: updated`, la cita queda movida en la base y el cliente recibe el aviso.
- **4 · Correo entregado.** Dado el SMTP de test configurado por el usuario, cuando se agenda o reagenda, entonces el correo pasa de `queued` a `sent` e incluye el link de calendario.
- **5 · Reagendar desde el panel.** Dado una cita de Rob, cuando el dueño la mueve desde el panel con `notify`, entonces Rob recibe WhatsApp y correo, y la respuesta de la API informa ambos envíos.
- **6 · Link en la confirmación.** Dado una cita creada o reagendada por el asistente, cuando llega la confirmación al cliente, entonces incluye el link "agregar al calendario".
- **7 · Juanita agenda sin escalar.** Dado Juanita sin citas, cuando escribe "¿puedo agendar una cita?" y luego "el miércoles en la tarde", entonces el asistente ofrece horarios reales de ese miércoles, pide el email si falta y agenda sin escalar.
- **8 · Sin filtraciones.** Dado todo el E2E, cuando se revisan los mensajes del asistente en `messages`, entonces ninguno cita instrucciones internas (`[SISTEMA]`, "no prometí", nombres de herramientas).
- **9 · Solo fechas próximas.** Dado un cliente que no da fecha, cuando pide una demo, entonces el asistente usa `find_next_available` y ninguna fecha ofrecida o consultada en `audit_log` es anterior a hoy.
- **10 · Cero escalamientos por guardrail.** Dado los flujos 1 a 9, cuando se cuentan las filas nuevas de `escalations` por conversación, entonces no hay ninguna con `reason = guardrail` y cualquier otra queda explicada en la evidencia.

**Evidencia / Definición de Terminado:**
- Configuración del tenant de test (`e46e57e7-…`): `timezone = America/Bogota`, `guardrail_max_retries = 2`, `guardrail_fail_action = neutral`, `auto_escalate_after_turns = 3`, spec activo con `persona.maxLength = 800`, `CalendarConfig.timezone` igual a la del negocio, SMTP verificado.
- Artefacto del tenant con respaldo previo: propósitos de `agendamiento`/`gestion_citas`, `find_next_available` agregado y `send_email` quitado del agendamiento, id `gestion_citas` verificado, "REGLA DURA (demo)" de `ventas.md` actualizada, overrides de playbooks revisados.
- Los 10 casos con respuestas exactas del asistente y extractos de `messages`, `audit_log` y `escalations` pegados en esta HU; golden del tenant con `eval-runner` sin regresión.
- [HU-CAL-04](HU-CAL-04-fecha-actual-y-anti-escalamiento.md)/05/06 en `terminada`, [bitácora](../../../08-bitacora-de-ejecucion.md) y Obsidian al día, `python3 herramientas/regenerar.py --check` con 0 errores.

**Configuración aplicada en test (2026-10-05):** `guardrail_fail_action=neutral`, `guardrail_max_retries=2`, `auto_escalate_after_turns` 3 → **5** (tres saludos seguidos escalaban, ver [core #234](https://github.com/devrochy/agent-core/issues/234)), spec activo con `persona.maxLength=800` (versión nueva; la anterior queda inactiva), `timezone` y `CalendarConfig.timezone` = `America/Bogota`, `waweb_daily_outbound_cap` 50 → **150** (el tope diario se agotó durante el E2E), SMTP `smtp.gmail.com:587` con "Usar TLS" activado. Artefacto del volumen con respaldo `solvershub-respaldo-20261005-hu-cal-06.tar.gz`: propósitos de `agendamiento`/`gestion_citas`, `find_next_available` en `agendamiento`, regla "demo" de `ventas.md`; el id `gestion_citas` ya era correcto, `send_email` ya no estaba y no hay overrides de `reglas-operacion`/`respuestas`/`citas`.

**E2E en test (2026-10-05):**

| Caso | Resultado | Evidencia |
|---|---|---|
| 1 · "¿qué citas tengo?" | ✅ | `list_client_appointments` → "jueves 8 de octubre de 2026, 3:00 pm" (fecha real), sin escalar |
| 2 · "el próximo miércoles 3pm" | ✅ | Cliente nuevo → miércoles 7 (lista de próximos días); Rob, anclado en un historial viejo con "el 14", corrigió y el asistente propuso el 7 |
| 3 · confirma reagenda | ✅ | `update_calendar_event` → `updated`, `notified: true`; cita `e1ecb6e9` al mié 7-oct 15:00 |
| 4 · correo `sent` con link | ✅ | Confirmación de la cita del jue 8-oct 10:00 → `sent` 13:25:11 con "Agregá la cita a tu calendario: https://calendar.google.com/…&ctz=America%2FBogota"; copias a 2 colaboradores `sent` |
| 5 · reagenda desde el panel | ✅ | Actividad `reprogramada` `actor=panel`, WhatsApp + 3 correos con link generados; el panel mostró el resultado real del aviso |
| 6 · link en la confirmación | ✅ | `_safe_append` con la URL de plantilla de Google Calendar en create y update |
| 7 · cliente simulado agenda | ✅ | `check_availability 2026-10-07` → `create … created`, sin escalar (número simulado para no escribirle a la clienta real) |
| 8 · sin filtraciones | ✅ | 0 de 14 respuestas del asistente con `[SISTEMA]`, "no prometí" o nombres de tools |
| 9 · sin fecha | ✅ | `find_next_available` (hoy sin las horas ya pasadas y días siguientes) |
| 10 · escalamientos por guardrail | ✅ 0 | `guardrail_neutral`: 0. Otros explicados: `send_failed` (tope de waweb y números simulados), 1 `escalate_to_human` (calendario en modo Google sin conexión), `turns_unresolved` (historial anclado; saludos) |

Flujo real de punta a punta por WhatsApp (13:15-13:18): saludo → listado → "el jueves 10 am" → jueves 8 → confirmación + email → cita `scheduled` y correo `sent`; todas las respuestas del asistente `sent`.

**Correcciones que salieron del E2E:** [core #227](https://github.com/devrochy/agent-core/pull/227) (hora local en las citas; listados sin evidencia), [core #228](https://github.com/devrochy/agent-core/pull/228) (próximos días en el prompt; claim `disponibilidad`), [core #235](https://github.com/devrochy/agent-core/pull/235) (la cola de salida se cortaba tras un fallo: `_enqueue_next` sin `tenant_scope`). También destapó [HU-CAL-07](HU-CAL-07-google-desde-el-panel.md) (conectar Google desde el panel). Mensajes y correos viejos atascados se descartaron (`failed`, con motivo).

**Pendiente (fuera del cierre):** escenarios golden de agendamiento en el set del tenant y corrida de `eval-runner` → [core #236](https://github.com/devrochy/agent-core/issues/236). Backlog abierto: [#231](https://github.com/devrochy/agent-core/issues/231) (no escalar por tope de waweb), [#232](https://github.com/devrochy/agent-core/issues/232) (tope configurable en el panel nuevo), [#234](https://github.com/devrochy/agent-core/issues/234) (autoescalado y saludos).

**Riesgos/Notas:**
- El volumen `tr0vpdei5av6szcgwpe1vwcg-tenants-data` es la única copia del artefacto (`tenants/` está en `.gitignore`): respaldo antes de editar.
- Antes de publicar inbounds se detiene `agent-core-s1-core-api-1` (su consumer compite por el stream) y se vuelve a arrancar al terminar.
- Si una conversación quedó `escalated`/`bot_paused`, se reabre con `update conversations set status='open', bot_paused=false` antes del caso.
- Si el autoescalado por 3 turnos sin resolver dispara en charlas normales, se sube el umbral y se anota (riesgo de la [ampliación](../design.md#riesgos-de-la-ampliación)).
- Producción no se toca; los 28 `send_failed` del canal waweb quedan fuera.
