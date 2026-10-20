---
id: HU-INMO-05
titulo: "Agenda por asesor con referencia y correo opcional"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Agenda
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, diferenciacion]
req: [REQ-INMO-06]
dependencias: [HU-INMO-01]
skills: ["db-migration", "auditor-multitenant", "backend-design:migration-safety", "agentcore-conventions"]
estado: borrador
---

# HU-INMO-05 · Agenda por asesor con referencia y correo opcional

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-05

**Título:** Agenda por asesor con referencia y correo opcional

**Workstream:** Agenda

**Historia:** Como negocio con varios asesores quiero que cada uno tenga su agenda, que la cita diga a qué se refiere y que el correo sea opcional, para agendar visitas en paralelo sin choques.

**Por qué importa (valor empresarial):** La restricción de solape es por negocio (`packages/pack-calendar/alembic/versions/0004_demo_de_punta_a_punta.py:35-40`): dos asesores no pueden tener citas a la misma hora. El correo obligatorio frena el agendamiento por WhatsApp.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-06

**Dependencias:** [HU-INMO-01](HU-INMO-01-adrs-y-dor-del-piloto.md)

**Criterios de aceptación (Gherkin):**
- **Dos asesores a la misma hora.** Dado dos citas a la misma hora con `agenda_admin_id` distintos, cuando se agendan, entonces ambas quedan y la restricción solo rechaza solapes de la misma agenda.
- **Sin agenda por asesor.** Dado un negocio que no usa `agenda_admin_id` (nulo), cuando agenda, entonces la conducta es la de hoy (una agenda por negocio).
- **Correo opcional.** Dado un tipo de cita con `email_obligatorio: false`, cuando el cliente no da correo, entonces la cita se crea y el aviso sale por WhatsApp.
- **Sin confirmación doble.** Dado una cita creada por el asistente con la ventana abierta, cuando se emite `appointment.confirmed` con `origen=asistente`, entonces no sale un segundo aviso de texto.

**Evidencia / Definición de Terminado:**
- Columnas nullable `agenda_admin_id` en citas y `admin_id` en bloqueos, validadas contra `tenant_user`; exclusión `(tenant_id, coalesce(agenda_admin_id, nil), tstzrange)`; `referencia`.
- Migración en una sola transacción con `lock_timeout` (ADD de la nueva + DROP de la vieja) en ventana de mantenimiento: EXCLUDE no admite `NOT VALID`.
- La exigencia del correo sale de la descripción de la tool (`pack_calendar/skills.py:380-383`) y queda en `execute` y en el playbook. ADR nuevo que enmienda ADR-0084.

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- Sin tabla de recursos: se agrega cuando un segundo caso real (clínica con consultorio) la pida.
