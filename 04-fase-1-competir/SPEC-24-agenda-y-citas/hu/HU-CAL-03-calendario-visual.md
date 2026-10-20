---
id: HU-CAL-03
titulo: Calendario visual tipo Google Calendar
spec: SPEC-24
fase: 1
hito: "1"
workstream: Agenda
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, diferenciacion]
req: [REQ-CAL-01]
dependencias: [HU-CAL-01, HU-CAL-02]
skills: ["frontend-design", "agentcore-conventions"]
estado: terminada
---

# HU-CAL-03 · Calendario visual tipo Google Calendar

> Estado SDD: Terminada — implementada 2026-10-04.

**ID:** HU-CAL-03

**Título:** Calendario visual tipo Google Calendar

**Workstream:** Agenda

**Historia:** Como dueño de un negocio quiero ver y editar mi agenda en una grilla de mes/semana/día —mover citas arrastrando y crear bloqueos de "fuera de oficina" ahí mismo— para operar como en Google Calendar pero con el calendario interno de SolversHub.

**Por qué importa (valor empresarial):** La vista de citas del panel nuevo es una tabla; el negocio ya usa la grilla FullCalendar del panel viejo en producción y espera la misma experiencia. Una agenda visual reduce errores de operación, hace evidente la ocupación real y convierte los bloqueos y la reagenda en acciones de un clic.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-CAL-01

**Dependencias:** [HU-CAL-01](HU-CAL-01-bloqueos-de-agenda.md), [HU-CAL-02](HU-CAL-02-agendar-reagendar-cancelar.md)

**Criterios de aceptación (Gherkin):**
- **Grilla.** Dado un negocio con citas y bloqueos, cuando abre Citas, entonces ve una grilla de mes/semana/día con citas y bloqueos diferenciados por color.
- **Mover con confirmación.** Dado una cita en la grilla, cuando el dueño la arrastra a un horario libre, entonces se le pide confirmar si avisar al cliente y a los colaboradores, y al aceptar se reagenda y se envía el correo.
- **Mover a horario ocupado.** Dado una cita, cuando el dueño la arrastra a un horario ocupado, entonces el movimiento se rechaza con un mensaje claro y la cita queda donde estaba.
- **Crear.** Dado un hueco libre, cuando el dueño hace clic, entonces se abre el formulario (título, tipo, email, inicio/fin, notas, avisar) y al guardar aparece en la grilla.
- **Bloqueo.** Dado un día o franja, cuando el dueño crea un bloqueo de "fuera de oficina", entonces aparece en la grilla y el asistente deja de ofrecer esos horarios.
- **Historial.** Dado una cita, cuando el dueño abre su detalle, entonces ve el historial de actividades (programada, reprogramada, cancelada) con su actor.

**Evidencia / Definición de Terminado:**
- `/calendario/citas` con FullCalendar (mes/semana/día), drag&drop y resize con confirmación antes de notificar, modal de crear/editar y detalle con historial, cancelar, y bloqueos en la misma grilla; permiso `pack_calendar:notificaciones` en el selector de colaboradores; typecheck y lint limpios; verificación en test.


**Implementada (2026-10-04):** panel ([#22](https://github.com/devrochy/solvershub-panel/pull/22)): `/calendario/citas` con FullCalendar (mes/semana/día), arrastrar/estirar con confirmación de aviso, modal de detalle/edición/alta con tipo, email, notas e historial de actividades, cancelar, y bloqueos en la misma grilla. Permiso `pack_calendar:notificaciones` disponible en el selector de colaboradores. `typecheck` y `lint` limpios.

**Riesgos/Notas:**
- Replica la UX del panel viejo (`templates/calendar/citas.html`) para no perder lo que el negocio ya conoce.
- Consume la API de [HU-CAL-02](HU-CAL-02-agendar-reagendar-cancelar.md); sin migración nueva.
