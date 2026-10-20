---
id: HU-ARCH-27
titulo: Turnos con timeout, cupo justo y observabilidad
spec: SPEC-19
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-ARCH-08, REQ-ARCH-09]
dependencias: [HU-ARCH-06]
skills: ["backend-design:error-handling-as-design", "backend-design:performance-and-scaling", "backend-design:observability-by-default"]
estado: terminada
---

# HU-ARCH-27 · Turnos con timeout, cupo justo y observabilidad

> Estado SDD: Terminada — implementada 2026-10-04.

**ID:** HU-ARCH-27

**Título:** Turnos con timeout, cupo justo y observabilidad

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de un negocio quiero que un turno lento nunca bloquee a los demás mensajes de mis clientes ni quede colgado para siempre, y poder ver cuándo un turno tarda, para que el asistente siga respondiendo aunque el proveedor del modelo esté lento.

**Por qué importa (valor empresarial):** El incidente del 2026-10-04 mostró que un turno puede colgarse minutos (LLM con timeout de 120 s × reintentos × hasta 50 iteraciones por spec) sin cota superior; con `max_turns_per_tenant=2`, dos turnos lentos del mismo tenant bloquean todos los demás y el negocio deja de responder. [HU-ARCH-06](../../../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-06-consumer-y-dlq.md) evita perder mensajes; esta HU evita que se bloqueen y hace visible el problema.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-08, REQ-ARCH-09

**Dependencias:** [HU-ARCH-06](../../../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-06-consumer-y-dlq.md)

**Criterios de aceptación (Gherkin):**
- **Timeout.** Dado un turno que tarda más de `TURN_TIMEOUT_S`, cuando se agota, entonces se corta con `turn_timeout`, el semáforo del tenant se libera y el mensaje queda manejado (respuesta de fallback o DLQ), nunca colgado para siempre.
- **Sin bloqueo del tenant.** Dado un turno colgado de un tenant, cuando llega un mensaje nuevo del mismo tenant, entonces se procesa dentro del cupo en vez de esperar indefinidamente al colgado.
- **Cupo justo.** Dado un tenant con más mensajes que su cupo, cuando esperan el semáforo, entonces la espera tiene un tope y el excedente no bloquea a otros tenants.
- **Observabilidad.** Dado un turno lento, cuando supera el umbral de aviso, entonces se registra `turn_slow` con duración y tenant; y al cortar por timeout se registra `turn_timeout`.
- **Aislamiento.** Dado dos tenants, cuando uno satura su cupo, entonces el otro sigue procesando (test cross-tenant).

**Evidencia / Definición de Terminado:**
- `asyncio.wait_for` con `TURN_TIMEOUT_S` (config) en el camino del consumer y del debounce; espera acotada del semáforo por tenant; logs/métricas `turn_slow`/`turn_timeout`/`turn_wait`; tests de integración con LLM mockeado que saturan y verifican que nada queda colgado; documentación en `docs/` y ajuste de los defaults de [HU-ARCH-06](../../../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-06-consumer-y-dlq.md) si aplica.


**Implementada (2026-10-04):** core [#215](https://github.com/devrochy/agent-core/pull/215): presupuesto total del turno (`turn_timeout_s=180`) con `TurnTimeout` y liberación del semáforo en `finally`; espera acotada del cupo por tenant (`turn_queue_timeout_s=30`) con `TurnQueueTimeout` (el consumer no ackea y el reclamo reintenta; el debounce reprograma el turno con delay 0); observabilidad `turn_slow`/`turn_slow_wait`/`turn_timeout`/`turn_queue_timeout`. Tests unitarios del gate (corte+libera cupo, saturación sin espera infinita, cross-tenant) e integración (queue-timeout no ackea ni reintenta; debounce reprograma). Verificado en test con smoke E2E (claim completado y respuesta normal).

**Riesgos/Notas:**
- Cortar un turno a mitad puede dejar efectos parciales (mensajes ya persistidos): el timeout debe ser mayor que el peor caso razonable de un turno normal y el estado se recupera por idempotencia.
- No confundir con el timeout del proveedor LLM (`httpx`): este es el presupuesto TOTAL del turno.
