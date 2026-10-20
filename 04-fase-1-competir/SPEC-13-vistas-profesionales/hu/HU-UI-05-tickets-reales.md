---
id: HU-UI-05
titulo: Tickets reales en Por atender
spec: SPEC-13
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, diferenciacion]
req: [REQ-UX-04, REQ-FIX-04]
dependencias: [HU-UI-02]
skills: ["frontend-design", "backend-design:auth-and-authorization", "db-migration", "panel-ui"]
estado: parqueada
---

# HU-UI-05 · Tickets reales en "Por atender"

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md).

**ID:** HU-UI-05

**Título:** Tickets reales en Por atender

**Workstream:** UX/Onboarding

**Historia:** Como operador quiero tomar una escalación, resolverla o devolverla al asistente, ver a quién está asignada y cuánto lleva esperando para que ningún cliente que pidió un humano quede sin respuesta.

**Por qué importa (valor empresarial):** Hoy las escalaciones son de solo lectura: el flujo humano central no existe en el panel. El modelo ya tiene `assigned_admin_id` (`core/db/models.py:504-521`). Es lo que Zendesk y Respond.io venden como núcleo.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-04, REQ-FIX-04

**Dependencias:** [HU-UI-02](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md)

**Criterios de aceptación (Gherkin):**
- **Tomar.** Dado una escalación abierta, cuando la tomo, entonces queda asignada a mí, el bot se pausa en esa conversación y el cliente recibe "te atiende una persona".
- **Resolver y devolver.** Dado un ticket tomado, cuando lo resuelvo o lo devuelvo al asistente, entonces cambia su estado, el bot se reactiva al devolver y queda auditado.
- **Espera.** Dado la lista, cuando la veo, entonces cada ticket muestra motivo legible, asignado y "esperando hace X", con pestañas y contadores por estado.
- **Asignar.** Dado un supervisor, cuando asigna un ticket a un colaborador, entonces el colaborador recibe la notificación.

**Evidencia / Definición de Terminado:**
- Endpoints `take/resolve/return/assign` con tests de permisos y aislamiento; vista migrada.

**Riesgos/Notas:**
- Las notificaciones al colaborador usan [HU-UI-13](HU-UI-13-cuenta-y-notificaciones.md) cuando exista; antes, correo.
