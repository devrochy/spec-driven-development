---
id: HU-CAL-02
titulo: Agendar, reagendar y cancelar demos con correo
spec: SPEC-24
fase: 1
hito: "1"
workstream: Agenda
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, operacion]
req: [REQ-CAL-01]
dependencias: [HU-CAL-01]
skills: ["agentcore-conventions", "backend-design:security-discipline", "backend-design:testing-with-discernment"]
estado: terminada
---

# HU-CAL-02 · Agendar, reagendar y cancelar demos con correo

> Estado SDD: Terminada — implementada 2026-10-04.

**ID:** HU-CAL-02

**Título:** Agendar, reagendar y cancelar demos con correo

**Workstream:** Agenda

**Historia:** Como dueño de un negocio quiero que el asistente agende, reagende y cancele demos sobre el calendario interno —sin doble reserva y avisando al cliente y a mis colaboradores por correo— para operar mi agenda sin depender de Google ni de que el modelo "se acuerde" de avisar.

**Por qué importa (valor empresarial):** El pack ya agenda sobre la agenda interna (ADR-0084) y notifica por WhatsApp, pero la validación de choques vive solo en la cabeza del LLM (puede crear doble reserva), el correo no es determinista (depende de que el modelo llame `send_email`) y no hay rastro de quién creó la cita. Cerrar esto convierte el calendario interno en una agenda confiable para vender demos —el ingreso directo de SolversHub— y es la base del calendario visual de [HU-CAL-03](HU-CAL-03-calendario-visual.md).

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-CAL-01

**Dependencias:** [HU-CAL-01](HU-CAL-01-bloqueos-de-agenda.md)

**Criterios de aceptación (Gherkin):**
- **Agendar sin choque.** Dado un negocio con agenda interna y un horario libre, cuando el asistente crea la demo, entonces la cita queda `scheduled`, con `created_by=assistant` y su zona horaria, y se encola el correo de confirmación al cliente y a los colaboradores con permiso de notificaciones.
- **Doble reserva.** Dado un horario ya ocupado por otra cita o un bloqueo, cuando el asistente intenta crear (o mover) una cita ahí, entonces la tool devuelve `occupied` y NO se crea ni se mueve nada.
- **Fuera de horario o en el pasado.** Dado un horario fuera del horario de atención o una fecha pasada, cuando se intenta agendar, entonces la tool devuelve `outside_hours` o `in_past` y no persiste.
- **Reagendar.** Dado una cita existente, cuando el asistente la mueve a un horario libre, entonces se actualiza (no se duplica), se registra `reprogramada` con `actor` y se envía el correo de reagenda a cliente y colaboradores.
- **Cancelar.** Dado una cita existente, cuando el asistente la cancela, entonces queda `cancelled`, se registra `cancelada` y se envía el correo de cancelación.
- **Sin proveedor de correo.** Dado un negocio sin conexión SMTP activa (o un cliente sin email), cuando se agenda/reagenda/cancela, entonces la acción se completa igual y queda registrada con `notified=false` y el motivo.
- **Colaboradores.** Dado un colaborador con el permiso `pack_calendar:notificaciones`, cuando se agenda una demo, entonces recibe copia del correo; un colaborador sin ese permiso no la recibe.
- **Aislamiento.** Dado otro negocio, cuando lista citas o actividades, entonces nunca ve las del primero (RLS).

**Evidencia / Definición de Terminado:**
- Migración `0003_calendar` (RLS forzada) con `created_by` y `timezone` en la cita; validación dura de solapamiento/horario/fecha en `create_event`/`update_event`; helper de correo determinista (cliente + colaboradores con `pack_calendar:notificaciones`) con fallback registrado; API `GET /events`, `POST/PATCH /appointments`, `GET /appointments/{id}/activities`, `PATCH /blocks/{id}`; permiso `pack_calendar:notificaciones` en el catálogo; tests unitarios e integración (incluye cross-tenant) y verificación en test.


**Implementada (2026-10-04):** backend ([core #211](https://github.com/devrochy/agent-core/pull/211)): validación DURA de solapamiento/horario/fecha pasada en `create_event`/`update_event`; migración `0003_calendar` (RLS) con `created_by` y `timezone`; correo determinista (cliente + colaboradores con `pack_calendar:notificaciones`) vía `queue_outbound_email` con fallback registrado; API `GET /events`, `PATCH /appointments/{id}`, `GET /appointments/{id}/activities`; permiso `pack_calendar:notificaciones` sin pantalla (`BaseModule.section_keys`). Panel de la grilla en [panel #22](https://github.com/devrochy/solvershub-panel/pull/22).

**Fixes de bug encontrados al probar:** `flow.json` usaba `gestion-citas` (guion) → la sección se descartaba y el asistente NO tenía `update_calendar_event`/`cancel_calendar_event`; el panel intentaba Google aunque `source=interno`; doble correo (el LLM mandaba además del determinista → se quitó `send_email` de la sección de agendamiento).

**Verificado en test (2026-10-04, con el asistente):** agendar → cita `scheduled` con `created_by=assistant` + correo "confirmada"; reagendar → cita movida e historial `reprogramada` + correo "reagendada"; cancelar → `cancelled` + historial `cancelada` + correo "cancelada"; intento de doble reserva → rechazado. Tests: 735 unit + 8 integración en verde.


**Correcciones post-prueba (2026-10-05):** la prueba real del usuario en test destapó 4 fallas que se corrigieron en el mismo día:
1. **Cancelar decía "no encontré" con la cita existente** (el modelo pasaba `event_id` inventados/viejos, p. ej. `demo-robinson-2026-10-05-16`). Fallback por conversación/título/email ([core #217](https://github.com/devrochy/agent-core/pull/217)) y luego resolución por **número de lista** (`event_id: "2"` = 2ª cita futura): con varias citas, un id no reconocido **no cancela a ciegas** — devuelve `not_found` para pedir aclaración (commit en `develop`, corrección del E2E que canceló la cita equivocada).
2. **No pedía el email al agendar.** Ahora es **obligatorio**: la tool devuelve `needs_data` sin crear ([core #217](https://github.com/devrochy/agent-core/pull/217)). Además se verifica la **procedencia** ([core #218](https://github.com/devrochy/agent-core/pull/218)): el email debe aparecer en un mensaje del cliente o en su perfil — el modelo había **inventado** `rob@example.com` y la cita se creó con un correo falso.
3. **El guardrail no cubría los fallos**: ahora cuenta solo resultados del turno actual y exitosos (`_current_turn`/`_ok`, patrón [HU-COM-02](../../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md)), agrega el claim `cita_existente` (afirmar que el cliente ya tiene cita exige listar) y cubre los **fallos negativos** ("no pude cancelarla", "no encontré la cita") que también exigen llamar la tool ([core #217](https://github.com/devrochy/agent-core/pull/217), [#219](https://github.com/devrochy/agent-core/pull/219)). El reintento del guardrail guía a **pedir el dato que falta** en vez de escalar (commit en `develop`).
4. **Playbook `citas.md`**: pedir el email antes de crear, no inventarlo, no confirmar si la tool devolvió `needs_data`/error, y usar el número de la lista si el cliente elige por número.

**Verificado en test (2026-10-05, E2E con el asistente):** agendar sin email → **pide el email** (no lo inventa); con email real → crea la cita (`scheduled`, correo encolado); cancelar la del 13-oct eligiendo "la número 2" → cancela `efd4b844` (la correcta) y la del 5-oct queda `scheduled`; id inventado con varias citas → `not_found` sin cancelar nada. Tests: 746 unit + 13 integración de calendario + 19 del guardrail en verde.

**Riesgos/Notas:**
- Google sigue funcionando si está configurado (`source=google`): la validación dura aplica al modo interno y no rompe la ruta Google existente.
- El correo reutiliza el canal SMTP (ADR-0071) y la cola de `outbound_send`; sin servicios nuevos.
