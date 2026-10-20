---
id: HU-CAL-05
titulo: Pack de agendamiento definitivo
spec: SPEC-24
fase: 1
hito: "1"
workstream: Agenda
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, calidad_ia, operacion]
req: [REQ-CAL-01, REQ-CAL-02]
dependencias: [HU-CAL-02, HU-CAL-04]
skills: ["new-tool", "agentcore-conventions", "backend-design:idempotency-and-side-effects", "backend-design:testing-with-discernment", "eval-author", "auditor-multitenant", "desplegar-test-agent-core"]
estado: terminada
---

# HU-CAL-05 · Pack de agendamiento definitivo

> Estado SDD: Terminada — implementada y verificada en test 2026-10-05 · issue [core #222](https://github.com/devrochy/agent-core/issues/222) · diseño en [design.md](../design.md#hu-cal-05--pack-de-agendamiento-definitivo) (D-SPEC-24-8, 9 y 10).

**ID:** HU-CAL-05

**Título:** Pack de agendamiento definitivo

**Workstream:** Agenda

**Historia:** Como dueño de un negocio quiero que el asistente solo ofrezca fechas futuras, proponga los días más cercanos cuando el cliente no da fecha, confirme únicamente lo que de verdad quedó agendado, movido o cancelado, le mande al cliente el link para agregar la cita a su calendario y que mis cambios desde el panel también le lleguen por WhatsApp, para que cada demo agendada sea real y el cliente siempre sepa cuándo es.

**Por qué importa (valor empresarial):** La prueba real mostró consultas de fechas pasadas (`check_availability` no las rechaza, `packages/pack-calendar/pack_calendar/skills.py:1206-1260`), un "moví tu demo" sin llamar la tool (`pack_calendar/module.py:49-57`), confirmaciones falsas porque `rejected`/`not_found` cuentan como éxito (`module.py:217-223`), cancelaciones desde el panel que no avisan a nadie (`pack_calendar/admin_api.py:207-248`) y citas internas sin link. Cada una cuesta una demo o la confianza del prospecto; juntas impiden vender Calendario como habilidad de primera clase.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-CAL-01, REQ-CAL-02

**Dependencias:** [HU-CAL-02](HU-CAL-02-agendar-reagendar-cancelar.md), [HU-CAL-04](HU-CAL-04-fecha-actual-y-anti-escalamiento.md)

**Criterios de aceptación (Gherkin):**
- **Fecha pasada.** Dado hoy 2026-10-07 en la zona del negocio, cuando el asistente llama `check_availability` con `2026-08-19`, entonces la tool devuelve `status: in_past` con `today: 2026-10-07` y no ofrece horarios.
- **Horas pasadas de hoy.** Dado hoy a las 15:10 con horario hasta las 18:00, cuando se consulta la disponibilidad de hoy, entonces `free_slots` no incluye ninguna hora anterior a las 15:10.
- **Sin fecha.** Dado un cliente que pide "lo más pronto posible", cuando el asistente consulta, entonces llama `find_next_available` y recibe hasta 5 días con cupo, ordenados desde hoy, sin días cerrados ni bloqueados.
- **"Moví tu demo" sin tool.** Dado un turno sin `update_calendar_event`, cuando el borrador dice "moví tu demo al 7", entonces el guardrail lo rechaza y pide llamar la tool.
- **Rechazo no es éxito.** Dado un `create_calendar_event` que devolvió `rejected` o `needs_data`, cuando el borrador dice "tu cita quedó agendada", entonces el guardrail lo rechaza y el reintento cita el motivo y pide el dato que falta.
- **Correo con evidencia.** Dado un `create_calendar_event` con `status: created` y `email_sent: true`, cuando el asistente dice "te envié la confirmación", entonces el guardrail lo acepta sin `send_email`; y si `email_sent` fue `false`, entonces el reintento dice que el correo no salió y nunca pide `send_email`.
- **Descripción verificada.** Dado un turno con `list_client_appointments` OK y sin create, cuando el asistente describe "tu demo quedó agendada para el 7", entonces el guardrail lo acepta.
- **Link de la cita.** Dado el modo interno, cuando el asistente crea o reagenda una cita, entonces la respuesta al cliente trae el link `calendar.google.com/calendar/render?action=TEMPLATE…` con la fecha local y `ctz`, y el correo de confirmación/reagenda incluye el mismo link.
- **Aviso desde el panel.** Dado una cita creada por el asistente en una conversación activa, cuando el dueño la mueve desde el panel con `notify`, entonces el cliente recibe WhatsApp y correo; y cuando la cancela con `notify`, entonces recibe ambos avisos, se registra la actividad `cancelada` y la respuesta informa `notification` con el resultado real.
- **Aislamiento.** Dado otro negocio con citas en el mismo horario, cuando se consulta `find_next_available` o `check_availability`, entonces esas citas no ocupan horarios del primero (RLS).

**Evidencia / Definición de Terminado:**
- `check_availability` con `in_past`, filtro de horas pasadas y `status`/`today`; tool nueva `find_next_available` registrada en `get_tools()`, `flow.json` y `citas.md`; `_calendar_link` en create/update del modo interno; `{link}` en el correo con formato seguro.
- Guardrail `calendar_completion_check` con evidencia por `status` real y patrones afirmativo/negativo; reintento que nunca pide `send_email`.
- `admin_api`: PATCH y cancel con correo + WhatsApp + `notification`; cancel registra `cancelada`; OpenAPI regenerado. Panel (`solvershub-panel`): muestra el resultado real del aviso.
- `citas.md` y propósitos de `flow.json` con el texto definitivo de [design.md](../design.md#hu-cal-05--pack-de-agendamiento-definitivo).
- Tests: `test_calendar_slots.py`, `test_pack_calendar_completion_guardrail.py`, `test_pack_calendar_claims_dsl.py` e integración `test_calendar_interno.py` (con cross-tenant) en verde, conteos en esta HU; eval golden "sin fecha" y "fecha pasada"; `auditor-multitenant` sobre el diff.
- Deploy a test verificado y `packages/pack-calendar/CALENDAR.md`, `CHANGELOG.md` al día.

**Implementada (2026-10-05):** backend [core #226](https://github.com/devrochy/agent-core/pull/226) — `check_availability` con `in_past` y sin horas ya pasadas de hoy; tool `find_next_available`; link "agregar a mi calendario" (`_calendar_link`) en create/update del modo interno y en el correo (`{link}` con línea de respaldo); plantillas con formato seguro; guardrail con evidencia por `status` real y patrones afirmativo/negativo (preguntas y propuestas ya no disparan; el reintento de correo nunca pide `send_email`); PATCH y cancel del panel con correo + WhatsApp + `notification` (cancel registra `cancelada`, es idempotente y responde 200); `citas.md` y `flow.json` definitivos. Panel [#24](https://github.com/devrochy/solvershub-panel/pull/24) — el panel muestra el resultado real del aviso. Correcciones del E2E de [HU-CAL-06](HU-CAL-06-afinado-del-tenant-y-e2e.md): [core #227](https://github.com/devrochy/agent-core/pull/227) (citas en hora local con fecha escrita; el guardrail reconoce enumeraciones y descripciones de citas sin listar; las preguntas `¿…?` no cuentan) y [core #228](https://github.com/devrochy/agent-core/pull/228) (claim `disponibilidad`: afirmar horarios libres u ocupados exige consultar).

**Verificado en test (2026-10-05):** `check_availability` de una fecha pasada → `in_past`; `find_next_available` → próximos días sin horas pasadas; E2E de [HU-CAL-06](HU-CAL-06-afinado-del-tenant-y-e2e.md): listado con la fecha real (caso 1), reagenda con `update_calendar_event` → `updated` + aviso por WhatsApp + correo encolado con link (caso 3), reagenda desde el panel con actividad `actor=panel`, WhatsApp y 3 correos con link, y el mensaje real del aviso en el panel (caso 5), link en la confirmación (caso 6), agendamiento de un cliente simulado sin escalar (caso 7), `find_next_available` sin fecha (caso 9), 0 escalamientos por guardrail (caso 10). La **entrega** de WhatsApp (tope diario de waweb) y de correo (SMTP de test) quedó bloqueada por infraestructura, no por el pack. Tests: 783 unit + 21 integración de calendario al mergear; con las correcciones, 804 unit + 22 integración. Los escenarios golden de calendario pasaron al golden set del tenant (el spec de evals del framework solo habilita `pack_commerce`). El subagente `auditor-multitenant` no estaba disponible en la sesión: el aislamiento quedó cubierto por el test cross-tenant de disponibilidad.

**Observaciones para backlog:** cuando el asistente reagenda en la misma conversación sale además el aviso automático "Tu cita fue reprogramada…" (mensaje duplicado); `email_sent: true` significa "encolado", no "entregado"; el alta de citas desde el panel no avisa al cliente.

**Riesgos/Notas:**
- El nombre `find_next_available` sigue el inglés del resto de tools del pack (excepción heredada que admite la skill `new-tool`).
- La "hoy" del pack sale de `CalendarConfig.timezone`; debe coincidir con la del negocio ([HU-CAL-06](HU-CAL-06-afinado-del-tenant-y-e2e.md) lo verifica).
- En modo Google `find_next_available` puede hacer hasta 14 consultas; la disponibilidad Google sigue pidiendo el día en UTC (deuda anotada en la spec).
- Los tenants con `flow.json` propio no reciben los propósitos nuevos hasta editarlos ([HU-CAL-06](HU-CAL-06-afinado-del-tenant-y-e2e.md) lo hace en `solvershub`).
