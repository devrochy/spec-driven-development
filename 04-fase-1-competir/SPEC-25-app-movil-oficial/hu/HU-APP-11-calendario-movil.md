---
id: HU-APP-11
titulo: "Calendario móvil: citas, tipos, bloqueos y horario"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [operacion]
req: [REQ-APP-07]
dependencias: [HU-APP-03]
skills: [frontend-design, panel-ui]
estado: terminada
---

# HU-APP-11 · Calendario móvil: citas, tipos, bloqueos y horario

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-11

**Título:** Calendario móvil: citas, tipos, bloqueos y horario

**Workstream:** App móvil

**Historia:** Como dueño con agenda quiero ver mis citas del día y de la semana, crear/reagendar/cancelar citas, administrar tipos de cita, bloqueos y horario desde la app, para operar mi agenda sin depender de Google ni del escritorio.

**Por qué importa (valor empresarial):** La agenda es el argumento de las verticales sin Google ([SPEC-24](../../SPEC-24-agenda-y-citas/spec.md)) y el agendamiento conversacional ya es confiable. Llevarla al móvil cierra el flujo "el asistente agenda, el dueño opera desde el celular", que es el uso real de una tienda o consultorio.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-03](HU-APP-03-navegacion-por-permisos.md)

**Criterios de aceptación (Gherkin):**
- **Vista móvil.** Dado un negocio con citas, cuando abre Calendario, entonces ve una lista día/semana (no la grilla de escritorio) con citas y bloqueos juntos, filtrable por día.
- **Cita.** Dado un hueco libre, cuando el dueño crea una cita (tipo, duración, cliente), entonces la cita aparece y el asistente deja de ofrecer ese horario (fuente de verdad `_local_busy`).
- **Bloqueos y tipos.** Dado un dueño, cuando crea o elimina un bloqueo o un tipo de cita, entonces la disponibilidad se actualiza con las mismas reglas del panel ([SPEC-24](../../SPEC-24-agenda-y-citas/spec.md)).
- **Mover/estirar.** Dado un dueño que toca largo una cita, cuando la mueve o cambia su duración, entonces se usa el menú móvil equivalente al drag de escritorio y se confirma antes de aplicar.

**Evidencia / Definición de Terminado:**
- `modules/calendario/` (lista día/semana, diálogo de cita, tipos, bloqueos, horario) contra `/api/v1/pack/calendar/*`; escritura encolada para mover/cancelar; tests unitarios y de render; captura en dev client.

**Implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — calendario móvil (citas, tipos, bloqueos y horario).

**Riesgos/Notas:**
- No se porta FullCalendar (web): se usa lista nativa con navegación por días y gesto largo para mover (accesible y probado en E2E).
- La conexión con Google sigue siendo acción del panel (OAuth de escritorio); la app muestra el estado de la conexión.

**App implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — `modules/calendario`: semana (citas+bloqueos ordenados vía `/pack/calendar/week`), tipos de cita y bloqueos. Crear/mover desde móvil queda para iteración (deuda). 3 tests.
