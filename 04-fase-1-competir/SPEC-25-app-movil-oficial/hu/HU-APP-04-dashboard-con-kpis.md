---
id: HU-APP-04
titulo: Dashboard con KPIs
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-APP-04]
dependencias: [HU-APP-03]
skills: [panel-ui, frontend-design]
estado: terminada
---

# HU-APP-04 · Dashboard con KPIs

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-04

**Título:** Dashboard con KPIs

**Workstream:** App móvil

**Historia:** Como dueño de un negocio quiero abrir la app y ver de un vistazo los KPIs de mi negocio (conversaciones, mensajes, escalaciones, cobranza y consumo) y acceder rápido a lo pendiente, para tomar decisiones desde el teléfono sin abrir el panel web.

**Por qué importa (valor empresarial):** El dashboard es la primera pantalla después del login y la demostración de que la app oficial no es "cobranza con más menús" sino la puerta móvil de todo SolversHub. Un dueño que puede ver su negocio desde el celular valora más la suscripción y responde antes a lo urgente.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-04

**Dependencias:** [HU-APP-03](HU-APP-03-navegacion-por-permisos.md)

**Criterios de aceptación (Gherkin):**
- **KPIs core.** Dado un dueño logueado, cuando abre Inicio, entonces ve los KPIs de `/api/v1/admin/dashboard` (conversaciones 7d, mensajes 7d, escalaciones pendientes, costo LLM 30d) con skeleton mientras cargan.
- **Packs habilitados.** Dado un negocio con cobranza habilitada, cuando abre Inicio, entonces ve también los KPIs de cobranza (`summary`) y accesos rápidos a lo pendiente del pack.
- **Offline y error.** Dado el dispositivo sin conexión o un error de red, cuando abre Inicio, entonces la app muestra el último valor cacheado con aviso de desactualización o un estado de error con reintento, nunca una pantalla en blanco.
- **Tema.** Dado un usuario con tema oscuro activado, cuando abre Inicio, entonces los KPIs usan los tokens de marca (navy/cyan) y contraste AA en ambos temas.

**Evidencia / Definición de Terminado:**
- Pantalla `modules/dashboard` con stat cards, estados carga/vacío/error y pull-to-refresh; datos vía TanStack Query; tests unitarios de transformación y de render; captura en dev client (claro y oscuro).

**Implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — dashboard con KPIs.

**Riesgos/Notas:**
- El dashboard del panel usa Server Components; aquí todo es client-side contra la API, con caché TTL corto para KPIs.
- Los gráficos se mantienen simples (sparklines/texto) en esta HU; tendencias ricas son de [HU-UI-07](../../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) (panel web).

**App implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — `modules/dashboard` con KPIs del negocio (`/admin/dashboard`) + resumen de cobranza por permiso, estado del asistente, recientes, pull-to-refresh y error con reintento; tab Inicio del PanelShell. 4 tests.
