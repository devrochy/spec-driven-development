---
id: HU-CAL-04
titulo: Fecha actual en el prompt y política anti-escalamiento
spec: SPEC-24
fase: 1
hito: "1"
workstream: Agenda
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, calidad_ia]
req: [REQ-CAL-02]
dependencias: [HU-CAL-02]
skills: ["agentcore-conventions", "db-migration", "backend-design:migration-safety", "adr", "panel-ui", "backend-design:testing-with-discernment", "desplegar-test-agent-core"]
estado: terminada
---

# HU-CAL-04 · Fecha actual en el prompt y política anti-escalamiento

> Estado SDD: Terminada — implementada y verificada en test 2026-10-05 · issue [core #221](https://github.com/devrochy/agent-core/issues/221) · diseño en [design.md](../design.md#hu-cal-04--fecha-actual-y-política-anti-escalamiento-core--panel) (D-SPEC-24-5, 6 y 7).

**ID:** HU-CAL-04

**Título:** Fecha actual en el prompt y política anti-escalamiento

**Workstream:** Agenda

**Historia:** Como dueño de un negocio quiero que el asistente sepa qué día y hora es en la zona de mi negocio y que, cuando no logra corregir una respuesta, le diga al cliente que va a verificar en vez de pasarle la conversación a una persona, para que agende en la fecha correcta y no pause el bot por un fallo que un reintento resuelve.

**Por qué importa (valor empresarial):** En la prueba real el asistente agendó "el próximo miércoles" dos semanas tarde porque ningún bloque del prompt trae la fecha actual (`core/llm/prompt_builder.py:78-137`), y escaló 11 veces por el guardrail de calendario porque al agotar el único reintento siempre escala (`core/orchestrator/loop.py:500-514`, `core/orchestrator/guardrails.py:25`). Cada escalamiento pausa el bot y le pasa a una persona una demo que el asistente podía cerrar: es ingreso directo que se pierde y tiempo humano que se gasta.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-CAL-02

**Dependencias:** [HU-CAL-02](HU-CAL-02-agendar-reagendar-cancelar.md)

**Criterios de aceptación (Gherkin):**
- **Fecha en el prompt.** Dado un negocio con `app_settings.timezone = America/Bogota` y el reloj en el martes 2026-10-06 10:00 de Bogotá, cuando se arma el system prompt de un turno, entonces el último bloque contiene "Hoy es martes, 6 de octubre de 2026 — 10:00 (America/Bogota)" y ningún bloque anterior cambia entre dos turnos del mismo día.
- **Próximo día relativo.** Dado ese mismo martes, cuando el cliente pide una demo "el próximo miércoles", entonces el asistente consulta la disponibilidad del 2026-10-07 y no la de otra semana.
- **Zona configurable.** Dado el formulario de Identidad, cuando el dueño guarda `America/Mexico_City`, entonces `GET /admin/settings` la devuelve y el siguiente turno usa esa zona; cuando guarda una zona inexistente, entonces la API responde 422 y no cambia nada.
- **PUT sin zona no la pisa.** Dado un negocio con zona `America/Lima`, cuando un cliente de la API guarda Identidad sin enviar `timezone`, entonces la zona sigue en `America/Lima`.
- **Modo neutral.** Dado `guardrail_fail_action = neutral` y `guardrail_max_retries = 2`, cuando la respuesta falla el guardrail en los 3 intentos, entonces el cliente recibe la sección `verifying` de `respuestas.md` (más los `_safe_append` del turno), no se crea fila en `escalations`, el bot no queda pausado, se registra `audit_log` `guardrail_neutral` con el id del guardrail y `turnos_sin_resolver` aumenta en 1.
- **Modo escalar (default).** Dado un negocio sin `guardrail_fail_action` o con `escalate`, cuando se agotan los reintentos, entonces escala con `reason = guardrail` igual que hoy.
- **Red de autoescalado.** Dado `neutral` y `auto_escalate_after_turns = 3`, cuando tres turnos seguidos terminan sin resolver (incluidos los neutrales), entonces la conversación escala con `reason = turns_unresolved`.
- **Sin filtración.** Dado un reintento del guardrail con una instrucción `[SISTEMA]`, cuando el asistente reescribe la respuesta, entonces el texto al cliente no cita ni menciona la instrucción (regla en `reglas-operacion.md`).

**Evidencia / Definición de Terminado:**
- Migración core `0050_app_settings_timezone` (sube y baja), `AppSettings.timezone`, API de Identidad con `timezone` y `guardrail_fail_action` (validados), `guardrail_max_retries` validado 0-5, OpenAPI regenerado.
- `PromptContext.timezone` + bloque de fecha al final de `dynamic_parts`; instrucciones de fecha y anti-filtración en `core/playbooks/reglas-operacion.md`; sección `## verifying` en `core/playbooks/respuestas.md` con constante de respaldo.
- Modo `neutral` en `loop.py` con `_finish_turn(resolved=False)`, audit y autoescalado compartido.
- Panel (`solvershub-panel`): Select de zona horaria y de "si el guardrail falla" en Configuración → Identidad.
- ADR-0091 y ADR-0092 enlazados en el PR.
- Tests unitarios e integración en verde (conteos en esta HU), deploy a test verificado (`alembic_version = 0050`, healthz, login) y criterios Gherkin verificados a mano.
- `CHANGELOG.md`, `ROADMAP` y `BACKLOG` del backend al día.

**Implementada (2026-10-04/05):** backend [core #225](https://github.com/devrochy/agent-core/pull/225) — migración `0050` (`app_settings.timezone`, default `America/Bogota`), API de Identidad con `timezone` (422 si es inválida; omitida no pisa) y `guardrail_fail_action`, `guardrail_max_retries` validado 0-5, fecha y hora del negocio como dato al final del bloque dinámico, regla de fecha y anti-filtración de `[SISTEMA]` en `reglas-operacion.md`, sección `verifying` en `respuestas.md` y salida `neutral` en el loop (no escala, audita `guardrail_neutral`, cuenta el turno como no resuelto; cierre de turno compartido en `_close_turn`); ADR-0091 y ADR-0092. Panel [#23](https://github.com/devrochy/solvershub-panel/pull/23) — selects de zona horaria y de "Si el asistente no logra corregir su respuesta". Ajuste tras el E2E de [HU-CAL-06](HU-CAL-06-afinado-del-tenant-y-e2e.md): [core #228](https://github.com/devrochy/agent-core/pull/228) suma al bloque de fecha la lista de los 7 próximos días ("el próximo miércoles" se resolvía a la semana equivocada).

**Verificado en test (2026-10-05):** `alembic_version = 0050` y columna `timezone` en la BD de test; el prompt real del tenant `solvershub` termina en "Hoy es lunes, 5 de octubre de 2026 — 07:34 (America/Bogota)." y trae la regla de fecha; `verifying` sale del playbook. En el E2E de [HU-CAL-06](HU-CAL-06-afinado-del-tenant-y-e2e.md) (tenant con `neutral`, 2 reintentos y autoescalado a 3 turnos): "el próximo miércoles" se resolvió al miércoles 7 con un cliente nuevo; el autoescalado actuó como red (`turns_unresolved`) cuando el asistente quedó anclado en un historial viejo; 0 escalamientos por guardrail y 0 de 14 respuestas con instrucciones internas. La salida `neutral` no llegó a dispararse en el E2E (el guardrail nunca agotó los reintentos); está cubierta por los tests de integración (`test_guardrail_retries_per_tenant.py`: responde `verifying`, no escala, audita y suma el turno; con `escalate` o sin clave escala como antes; autoescalado tras N turnos neutrales) y los 5 de `test_settings_timezone.py`. La configuración del tenant se aplicó por SQL (decisión del usuario), así que los selects del panel no se usaron en el E2E. Tests al mergear: 756 unit + 15 integración afectada en verde.

**Riesgos/Notas:**
- Con `neutral` nadie hace seguimiento proactivo: la red es el autoescalado por turnos sin resolver (ver [riesgos](../design.md#riesgos-de-la-ampliación)).
- El default del core no cambia (`escalate`, 1 reintento): solo cambia el negocio que lo active.
- Un tenant que sobrescribe `reglas-operacion.md` o `respuestas.md` (ADR-0026) no recibe las reglas nuevas; la regla de fecha también va en `citas.md` ([HU-CAL-05](HU-CAL-05-pack-de-agendamiento-definitivo.md)) y `verifying` tiene respaldo en código.
- Con Anthropic el bloque dinámico ahora siempre existe y suma un `cache_control`; el límite de 4 se verifica antes de activar Anthropic en un tenant (fuera de alcance).
