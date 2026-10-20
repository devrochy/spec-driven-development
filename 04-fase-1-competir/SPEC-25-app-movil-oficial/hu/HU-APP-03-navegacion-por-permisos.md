---
id: HU-APP-03
titulo: Navegación por permisos y roles
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-APP-03]
dependencias: [HU-APP-01]
skills: [frontend-design, backend-design:security-discipline]
estado: terminada
---

# HU-APP-03 · Navegación por permisos y roles

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-03

**Título:** Navegación por permisos y roles

**Workstream:** App móvil

**Historia:** Como dueño, colaborador o gestor quiero que la navegación de la app muestre solo los módulos y acciones que mis permisos me permiten, para que nunca vea pantallas a las que no puedo acceder (nunca un 403 por diseño).

**Por qué importa (valor empresarial):** La app replica el panel completo, pero cada negocio y cada rol ve solo lo suyo. Si la navegación no respeta los permisos, la app expone superficie no autorizada y pierde confianza; si los respeta, cada perfil (dueño, colaborador de sección, gestor de campo, master) obtiene una app a su medida sin trabajo de configuración.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-03

**Dependencias:** [HU-APP-01](HU-APP-01-nucleo-modular-de-la-app.md)

**Criterios de aceptación (Gherkin):**
- **Shell por rol.** Dado un usuario logueado, cuando se resuelven sus permisos, entonces el gestor ve el FieldShell (Diario, Carteras, Clientes, Notificaciones, Perfil) y el dueño/colaborador ve el PanelShell (tabs + drawer) según `MeResponse.permissions`.
- **Sección sin permiso.** Dado un colaborador sin permiso de una sección (p. ej. `pack_cobranza:carteras`), cuando arma la navegación, entonces esa sección no aparece y su ruta profunda redirige a la pantalla de acceso denegado.
- **Gestor con permisos finos.** Dado un gestor sin permiso de registrar pagos, cuando usa la app, entonces las acciones de pago no se muestran ni se pueden invocar.
- **Master.** Dado un admin master de plataforma, cuando abre la app, entonces ve la sección de negocios y nadie más la ve.

**Evidencia / Definición de Terminado:**
- `src/navigation/AppNavigator` compuesto por navigators de módulos; armado del shell desde permisos en un solo lugar; gating por pack (ADR-0019) reutilizando `/admin/plugins`; tests de armado de navegación por rol y por permiso; captura en dev client con 3 perfiles distintos.

**Implementada (2026-10-06):** [solvershub-apk #109](https://github.com/devrochy/solvershub-apk/pull/109) — shells por rol y permisos.

**Riesgos/Notas:**
- Las claves de permiso son las mismas que usa el sidebar del panel (`pack_cobranza:*`, secciones core), no un catálogo nuevo.
- El gestor no consume el panel: sus permisos finos (14) mandan sobre el FieldShell completo.

**App implementada (2026-10-05):** [solvershub-apk #109](https://github.com/devrochy/solvershub-apk/pull/109) — shells por rol en `App.tsx` (gestor → campo legado; propietario/master/panel-only → PanelShell), PanelShell con tabs + menú armados desde `MeResponse.permissions` (Plataforma solo master, placeholders hasta las HUs de cada módulo), selector admin multi-negocio y `AdminSessionContext.seleccionarNegocio`; 536/536 tests (19 nuevos). Deuda registrada: los 14 permisos finos del gestor se entregaban por cartera en `/gestor/mis-carteras`; **deuda cerrada (2026-10-07)** con [agent-core #258](https://github.com/devrochy/agent-core/pull/258), que además expone `permisos` en el login/exchange de campo. FieldShell con tabs llega en [HU-APP-07](HU-APP-07-cobranza-al-nucleo-sin-regresion.md); deep links en [HU-APP-05](HU-APP-05-notificaciones-push.md).
