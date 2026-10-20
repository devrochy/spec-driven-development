---
id: HU-SH-02
titulo: Demo agendada de punta a punta
spec: SPEC-07
fase: 0
hito: 0A
workstream: Asistente SolversHub
prioridad: P0
critico: true
estimacion: L
impacto: [ingreso, confianza]
req: [REQ-SH-02]
dependencias: [HU-ARCH-13]
skills: ["new-tool", "backend-design:idempotency-and-side-effects", "eval-author", "customizer"]
ola: 3
estado: terminada
---

# HU-SH-02 · Demo agendada de punta a punta

> Estado SDD: Terminada — implementada y desplegada en test el 2026-10-08 (issue [core #315](https://github.com/devrochy/agent-core/issues/315)).

**ID:** HU-SH-02

**Título:** Demo agendada de punta a punta

**Workstream:** Asistente SolversHub

**Historia:** Como prospecto quiero agendar una demo por WhatsApp, recibir la confirmación con fecha y hora y un recordatorio antes, y como equipo de SolversHub quiero enterarme de cada demo para que ninguna demo se pierda.

**Por qué importa (valor empresarial):** La demo es el paso de mayor conversión del embudo B2B. Una demo olvidada, a una hora que ya pasó o duplicada con otra es un cliente perdido. Además, todo lo que se construye aquí sirve a cualquier negocio que agenda (clínicas, asesorías, inmobiliarias).

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** L

**REQ mapeados:** REQ-SH-02

**Dependencias:** [HU-ARCH-13](../../SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md)

**Criterios de aceptación (Gherkin):**
- **Sin horas pasadas.** Dado que hoy son las 15:00, cuando el prospecto pide horarios para hoy, entonces solo se ofrecen horas posteriores.
- **Sin doble reserva.** Dado dos prospectos que eligen el mismo horario a la vez, cuando se crean las citas, entonces una se confirma y la otra recibe alternativas.
- **Confirmación.** Dado una demo creada, cuando se confirma, entonces el mensaje trae fecha, hora, zona horaria y enlace de la reunión configurado.
- **Recordatorios.** Dado una demo, cuando faltan 24 h y 1 h, entonces el prospecto recibe recordatorios (plantilla si la ventana está cerrada).
- **Aviso al equipo.** Dado una demo nueva, reagendada o cancelada, cuando ocurre, entonces el colaborador asignado recibe el aviso.
- **Asistencia.** Dado una demo pasada, cuando el equipo la marca `asistio` o `no_asistio`, entonces al `no_asistio` el asistente ofrece reagendar.
- **Panel en modo interno.** Dado un negocio con agenda interna, cuando se crea o cancela una cita desde el panel, entonces no se llama a Google y el cliente recibe el aviso.

**Evidencia / Definición de Terminado:**
- Jobs de recordatorio; estados de asistencia con migración; tests con reloj simulado; arreglo de `pack_calendar/admin_api.py:281-297`.

**Terminada (2026-10-08):** [agent-core #317](https://github.com/devrochy/agent-core/pull/317) + [panel #46](https://github.com/devrochy/solvershub-panel/pull/46). Desplegada en test (`1e2ce37`, panel `05fde0d`, migración `pack_calendar` `0004`).

- **Sin horas pasadas:** ya estaba cubierto y tenía test.
- **Sin doble reserva:** restricción de exclusión en la base (`btree_gist`). Si dos prospectos eligen el mismo horario a la vez, uno queda y el otro recibe alternativas, también al reagendar y desde el panel.
- **Confirmación:** lleva fecha, hora, zona y enlace de la reunión (por tipo de cita o el general).
- **Recordatorios:** a 24 h y 1 h, una vez cada uno, por el outbox (plantilla si la ventana está cerrada).
- **Aviso al equipo:** al responsable del tipo de cita o a los dueños, cuando una cita es nueva, se reagenda o se cancela.
- **Asistencia:** se marca `asistio` / `no_asistio`; con `no_asistio` se le ofrece reagendar al cliente.
- **Panel en modo interno:** al crear una cita le avisa al cliente y al equipo. El arreglo de `admin_api.py:281-297` ya estaba hecho.

**Auditoría multi-tenant:** sin fugas entre negocios. Corregido:
- el asistente ya no ve ni toca citas de **otros clientes** del negocio (era anterior a la rama);
- la consulta de disponibilidad no muestra títulos ajenos;
- el aviso a un ex colaborador va a los dueños.

En la misma tanda llegaron #318, #319 y #320 (Google con `ScopedHttp`).

**Antes de producción:** verificar que no haya citas internas solapadas; si las hay, la migración `0004` falla. En test no hay ninguna.

**Riesgos/Notas:**
- `.ics` por correo queda opcional (necesita conexión SMTP).
