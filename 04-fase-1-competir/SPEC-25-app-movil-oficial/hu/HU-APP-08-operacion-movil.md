---
id: HU-APP-08
titulo: "Operación móvil: conversaciones, escalaciones y leads"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, diferenciacion]
req: [REQ-APP-07]
dependencias: [HU-APP-03, HU-APP-04]
skills: [frontend-design, panel-ui]
estado: terminada
---

# HU-APP-08 · Operación móvil: conversaciones, escalaciones y leads

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-08

**Título:** Operación móvil: conversaciones, escalaciones y leads

**Workstream:** App móvil

**Historia:** Como dueño o colaborador con permiso de Operación quiero ver y atender conversaciones (responder como humano, pausar/reanudar el agente, resolver), revisar escalaciones y consultar leads desde el teléfono, para que la bandeja no dependa del escritorio.

**Por qué importa (valor empresarial):** La operación es el corazón diario del panel: una escalación atendida desde el celular puede salvar una venta. Es el primer módulo que demuestra la réplica del panel en móvil y el de mayor frecuencia de uso del dueño.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-03](HU-APP-03-navegacion-por-permisos.md), [HU-APP-04](HU-APP-04-dashboard-con-kpis.md)

**Criterios de aceptación (Gherkin):**
- **Lista.** Dado un usuario con permiso de conversaciones, cuando abre Operación, entonces ve la lista paginada con búsqueda y filtro de estado (mismos criterios del panel `/admin/conversations`).
- **Hilo.** Dado un usuario que abre una conversación, cuando llegan mensajes nuevos, entonces el hilo se actualiza y puede responder como humano, pausar/reanudar el agente y resolver con confirmación para acciones irreversibles.
- **Escalaciones y leads.** Dado un usuario con permiso, cuando abre Escalaciones o Leads, entonces ve las listas del panel con sus filtros y enlace a la conversación.
- **Permisos.** Dado un usuario sin permiso de una de estas secciones, cuando navega, entonces esa sección no aparece y la ruta profunda no expone datos.

**Evidencia / Definición de Terminado:**
- `modules/operacion/` con listas, detalle de hilo y acciones (contrato `/api/v1/admin/conversations`, `escalations`, `leads`); TanStack Query con paginación por cursor; estados vacío/error/offline; tests unitarios y de render; captura en dev client.

**Implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — operación móvil (conversaciones, escalaciones y leads).

**Riesgos/Notas:**
- El panel tiene bandeja de dos paneles ([HU-UI-06](../../SPEC-13-vistas-profesionales/hu/HU-UI-06-bandeja-dos-paneles.md)); en móvil se usa lista→detalle con acciones en sheet inferior, sin intentar replicar el layout de escritorio.
- La ficha lateral del cliente en la conversación se adapta como sheet con los datos que ya devuelve la API.

**App implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — `modules/operacion`: conversaciones (búsqueda, filtros de estado, paginación), detalle con hilo, responder como humano, pausar/reanudar el asistente y resolver con confirmación; escalaciones y clientes (leads). 7 tests.
