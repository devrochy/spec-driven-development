---
id: HU-APP-09
titulo: "Negocio móvil: plan, consumo y costos"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, operacion]
req: [REQ-APP-07]
dependencias: [HU-APP-03, HU-APP-04]
skills: [panel-ui]
estado: terminada
---

# HU-APP-09 · Negocio móvil: plan, consumo y costos

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-09

**Título:** Negocio móvil: plan, consumo y costos

**Workstream:** App móvil

**Historia:** Como dueño de un negocio quiero ver desde la app mi plan actual, el consumo de créditos, los costos de IA y WhatsApp, y suscribirme o cambiar de plan, para controlar el gasto de mi negocio desde cualquier lugar.

**Por qué importa (valor empresarial):** El consumo y el plan son el motor de ingreso de SolversHub (transparencia de costos es principio de la constitución §1.2). Que el dueño vea el estado de su suscripción en el bolsillo reduce cancelaciones y facilita upsell en el momento justo.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-03](HU-APP-03-navegacion-por-permisos.md), [HU-APP-04](HU-APP-04-dashboard-con-kpis.md)

**Criterios de aceptación (Gherkin):**
- **Plan.** Dado un dueño logueado, cuando abre Negocio, entonces ve su plan con días restantes, barras de consumo y el catálogo de planes del panel.
- **Costos.** Dado un dueño con uso registrado, cuando abre Costos, entonces ve los KPIs del panel (hoy/30d/turnos, por modelo y por conversación) con el mismo desglose del web.
- **Suscripción.** Dado un dueño que elige un plan, cuando toca suscribirse, entonces se abre el checkout en webview seguro (Wompi) y al volver la app refleja el nuevo estado.
- **Solo lectura por permiso.** Dado un colaborador sin permiso de plan, cuando abre la app, entonces no ve la sección Negocio.

**Evidencia / Definición de Terminado:**
- `modules/negocio/` (plan, costos) contra `/api/v1/admin/plan` y `/api/v1/admin/costs`; webview de checkout con esquema de retorno; tests de formateo de moneda (`lib/format` equivalente) y render; captura en dev client.

**Implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — negocio móvil (plan, consumo y costos).

**Riesgos/Notas:**
- El checkout de Wompi en webview debe usar la misma sesión/token que el panel (se evalúa URL firmada de retorno); si el proveedor bloquea webview, se cae a navegador externo.
- Costos Meta desglosados (por número/país) se incluyen como vistas de lectura; la sincronización de precios sigue siendo acción del panel.

**App implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — `modules/negocio`: plan y consumo (barras por métrica, planes) y costos IA (hoy/mes/turnos, por modelo). Checkout Wompi queda en el panel web (deuda documentada). 3 tests.
