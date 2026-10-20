---
id: HU-UX-19
titulo: Centro de notificaciones en el panel y la app
spec: SPEC-31
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, diferenciacion]
req: [REQ-UX-22]
dependencias: [HU-UX-14]
skills: ["panel-ui", "frontend-design", "db-migration", "arquitecto", "auditor-multitenant", "adr"]
estado: borrador
---

# HU-UX-19 · Centro de notificaciones en el panel y la app

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-UX-19

**Título:** Centro de notificaciones en el panel y la app

**Workstream:** UX/Onboarding

**Historia:** Como usuario del panel o de la app quiero una campana con las notificaciones de lo que pasó (creaciones, ejecuciones, reportes generados, descargas, pagos y escalaciones), para enterarme sin estar mirando cada sección.

**Por qué importa (valor empresarial):** El dueño lo pidió para «todos esos reportes de modificación, creación, ejecución, generación, descarga». Hoy un aviso se pierde si se cambia de página, y la app solo tiene push sueltos.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-22

**Dependencias:** [HU-UX-14](HU-UX-14-shell-v2-y-perfil.md)

**Criterios de aceptación (Gherkin):**
- **Campana con contador.** Dado que se generó un reporte o se resolvió un pago, cuando miro la campana del panel, entonces veo el contador de no leídas y la notificación arriba.
- **Ir a lo que pasó.** Dado una notificación, cuando la abro, entonces llego a la página del evento y queda como leída.
- **Marcar todas.** Dado varias notificaciones sin leer, cuando elijo «Marcar todas como leídas», entonces el contador queda en cero.
- **Solo lo mío.** Dado dos negocios, cuando miro mis notificaciones, entonces solo veo las del negocio activo y las dirigidas a mí.
- **En la app.** Dado la app, cuando abro las notificaciones, entonces veo la misma lista y, si activé el push, recibo las nuevas en el teléfono.

**Evidencia / Definición de Terminado:**
- ADR de notificaciones (modelo, emisión desde el outbox, retención, push).
- Core: tabla `notifications` con `tenant_id`, RLS forzada y policy con `nullif`; emisión desde el outbox para los eventos acordados; `GET /admin/notifications`, `POST …/{id}/read`, `POST …/read-all`; tests de aislamiento.
- Panel: campana en la topbar con `ui/popover.tsx` o `ui/sheet.tsx`, polling liviano del contador.
- APK: pantalla de notificaciones y push opcional con el FCM existente.

**Riesgos/Notas:**
- Nota que lo motiva: ítem 21 del [inventario de SPEC-31](../design.md#inventario).
- Retoma la parte de notificaciones de [HU-UI-13](../../SPEC-13-vistas-profesionales/hu/HU-UI-13-cuenta-y-notificaciones.md) (parqueada por D-35) sin reabrir [SPEC-13](../../SPEC-13-vistas-profesionales/spec.md).
