---
id: HU-CAL-01
titulo: Bloqueos de agenda y vista semanal
spec: SPEC-24
fase: 1
hito: "1"
workstream: Agenda
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, diferenciacion]
req: [REQ-CAL-01]
dependencias: []
skills: ["agentcore-conventions", "frontend-design", "backend-design:security-discipline"]
estado: terminada
---

# HU-CAL-01 · Bloqueos de agenda y vista semanal

> Estado SDD: Terminada — implementada 2026-10-04.

**ID:** HU-CAL-01

**Título:** Bloqueos de agenda y vista semanal

**Workstream:** Agenda

**Historia:** Como dueño de un negocio quiero bloquear días, franjas o el almuerzo en mi agenda interna y ver de un vistazo mi semana, para que el asistente no agende citas cuando no puedo atender y para operar mi agenda sin depender de Google Calendar.

**Por qué importa (valor empresarial):** El pack ya agenda sobre la agenda interna (ADR-0084) con horarios y tipos de cita, pero sin bloqueos el asistente ofrece citas en vacaciones, feriados o el almuerzo. Es la pieza que cierra el ciclo de la vertical Agenda (restaurantes, retail, cobranza, suscripciones) y la base para recordatorios y multi-sede de la Fase 2.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-CAL-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Crear bloqueo.** Dado un negocio con agenda interna, cuando el dueño crea un bloqueo con inicio, fin y motivo, entonces aparece en la lista de bloqueos y `check_availability` deja de ofrecer esos horarios.
- **Día completo.** Dado un día con un bloqueo que cubre todo el horario de atención, cuando el asistente consulta disponibilidad, entonces no devuelve ningún horario libre ese día.
- **Editar/eliminar.** Dado un bloqueo existente, cuando el dueño lo elimina, entonces vuelve a estar disponible esa franja en la consulta de disponibilidad.
- **Vista semanal.** Dado un rango de una semana, cuando el dueño abre Citas, entonces ve citas y bloqueos juntos, ordenados por fecha, sin mostrar datos de otro negocio.
- **Solo interno.** Dado un negocio en modo `google`, cuando abre Bloqueos, entonces la pantalla explica que los bloqueos aplican solo a la agenda interna.

**Evidencia / Definición de Terminado:**
- API `GET/POST/DELETE /api/v1/pack/calendar/blocks` con permiso `pack_calendar:bloqueos`, RLS forzada y tenant scope; sección `pack_calendar:bloqueos` en `admin_menu` y en el menú del panel; página `/calendario/bloqueos` con formulario de rango y tabla; vista semanal en `/calendario/citas` con citas + bloqueos; tests de capa/RLS y del cálculo "día bloqueado → 0 slots"; evidencias en test.

**Implementada (2026-10-04):** backend ([core #210](https://github.com/devrochy/agent-core/pull/210)): `GET/POST/DELETE /api/v1/pack/calendar/blocks` sobre `pack_calendar_blocks` (RLS forzada, permiso `pack_calendar:bloqueos`, validación `fin>inicio`), `GET /api/v1/pack/calendar/week?start=` (citas + bloqueos + horario del día), sección `pack_calendar:bloqueos` en `admin_menu`; sin migración nueva. Panel ([panel #21](https://github.com/devrochy/solvershub-panel/pull/21)): página `/calendario/bloqueos` (alta de rango + motivo, tabla, eliminar), ítem **Bloqueos** en el menú y vista semanal en `/calendario/citas`. Tests: CRUD por API con aislamiento cross-tenant (RLS), rango inválido → 400 y "día totalmente bloqueado → 0 slots".

**Verificado en test (2026-10-04):** `GET /pack/calendar/blocks` 200, `GET /pack/calendar/week` 200 (L-V 09:00-19:00, sáb 09:00-13:00, dom cerrado); crear bloqueo 12:00-13:00 → `check_availability` **omite las 12:00** (asistente responde "9:00, 10:00, 11:00, 1:00 …"); eliminar → 204 y la franja vuelve; panel `/calendario/bloqueos` y `/calendario/citas` sirven (307 → login sin sesión).

**Riesgos/Notas:**
- Reutiliza `pack_calendar_blocks` (sin migración). La UI sigue el patrón de las pantallas existentes del pack (tipos/horario), no el descriptor genérico de [SPEC-16](../../SPEC-16-habilidades-como-plataforma/spec.md) (decisión D-SPEC-24-2).
