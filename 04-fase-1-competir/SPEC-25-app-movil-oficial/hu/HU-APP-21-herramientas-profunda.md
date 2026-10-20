---
id: HU-APP-21
titulo: "Herramientas profundas móvil"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, diferenciacion]
req: [REQ-APP-07]
dependencias: [HU-APP-08, HU-APP-12, HU-APP-14]
skills: [frontend-design, panel-ui]
estado: terminada
---

# HU-APP-21 · Herramientas profundas móvil

> Estado SDD: Terminada — implementada 2026-10-07.

**ID:** HU-APP-21

**Título:** Herramientas profundas móvil

**Workstream:** App móvil

**Historia:** Como dueño de un negocio quiero desde la app el playground del asistente, el plan y su suscripción (con purga de negocio para el master), las plantillas Meta de mis conexiones, el opt-out de notificaciones y que los resultados de búsqueda me lleven directo a su módulo, para cerrar la brecha restante con el panel y controlar mi experiencia móvil.

**Por qué importa (valor empresarial):** Es la última HU de la iteración 2 previa al release: sin ella, plan/purga y plantillas obligan a escritorio, el opt-out de push es un requisito de confianza del usuario y los resultados de búsqueda sin destino son una calle sin salida.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-08](HU-APP-08-operacion-movil.md), [HU-APP-12](HU-APP-12-configuracion-movil.md), [HU-APP-14](HU-APP-14-busqueda-global.md)

**Criterios de aceptación (Gherkin):**
- **Playground.** Dado un dueño, cuando abre Playground en Operación, entonces ve la conversación de demostración, envía mensajes y puede reiniciarla.
- **Plan.** Dado un dueño, cuando abre Plan en Configuración, entonces ve su plan y puede suscribirse a otro; dado el master, entonces puede purgar el negocio con doble confirmación.
- **Plantillas.** Dado un dueño, cuando toca una conexión, entonces ve sus plantillas Meta y puede sincronizarlas o borrarlas.
- **Push.** Dado un usuario, cuando apaga "Notificaciones push", entonces la app se da de baja del registro y no vuelve a pedir permiso.
- **Búsqueda.** Dado un usuario, cuando toca un resultado de búsqueda, entonces la app navega al tab del módulo correspondiente.

**Evidencia / Definición de Terminado:**
- Playground (`/admin/playground*`), plan (`/admin/plan{,/subscribe}`, purge master `/admin/platform/tenants/{id}/purge`), plantillas (`/admin/meta/connections/{id}/templates*`), opt-out local (tabla `ajuste_local` + `PushProvider`) y deep links de búsqueda (bus `@shared/navegacion-evento` + `navigationRef` en PanelShell); 5 tests nuevos.

**Implementada (2026-10-07):** [solvershub-apk #127](https://github.com/devrochy/solvershub-apk/pull/127) — playground en Operación, plan/purge/plantillas/opt-out en Configuración y navegación por resultado de búsqueda. 627/627 tests.

**Riesgos/Notas:**
- Las plantillas se crean en Meta Business; la app solo lista/sincroniza/borra (así lo define el contrato del backend).
