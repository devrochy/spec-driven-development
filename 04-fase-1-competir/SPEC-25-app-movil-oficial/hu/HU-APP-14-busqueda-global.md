---
id: HU-APP-14
titulo: Búsqueda global
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-APP-08]
dependencias: [HU-APP-03]
skills: [agentcore-conventions, backend-design:query-discipline]
estado: terminada
---

# HU-APP-14 · Búsqueda global

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-14

**Título:** Búsqueda global

**Workstream:** App móvil

**Historia:** Como usuario de la app quiero buscar desde un solo lugar clientes, conversaciones, productos, pedidos, citas y promesas y saltar al resultado tocándolo, para encontrar lo que busco sin saber en qué módulo vive.

**Por qué importa (valor empresarial):** Con 10 módulos, la búsqueda es el atajo principal de la app oficial (equivalente al ⌘K del panel). Un solo endpoint unificado evita buscar módulo por módulo y respeta permisos por sección en el servidor.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-08

**Dependencias:** [HU-APP-03](HU-APP-03-navegacion-por-permisos.md)

**Criterios de aceptación (Gherkin):**
- **Búsqueda unificada.** Dado un usuario que escribe en la barra global, cuando se estabiliza el texto, entonces ve resultados agrupados por sección desde `GET /api/v1/search?q=` con límite por sección.
- **Deep link.** Dado un resultado tocado, cuando se navega, entonces la app abre la entidad en su módulo (conversación, ficha de cliente, producto, cita) con el permiso verificado.
- **Permisos.** Dado un usuario sin permiso sobre una sección, cuando busca, entonces los resultados de esa sección no aparecen (filtrado server-side, no client-side).
- **Offline.** Dado el dispositivo sin conexión, cuando busca, entonces la app ofrece la búsqueda local sobre la caché disponible y lo indica.

**Evidencia / Definición de Terminado:**
- Backend: `GET /api/v1/search` unificado por sección con RBAC, límites de paginación e índices necesarios (tests cross-tenant y de permisos; OpenAPI regenerado).
- App: `modules/busqueda/` con barra global persistente, debounce, agrupación por sección y deep links; búsqueda local sobre SQLite cuando no hay red; tests unitarios y de render.

**Implementada (2026-10-06):** [agent-core #244](https://github.com/devrochy/agent-core/pull/244) + **Implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — búsqueda global (ADR-0096).

**Riesgos/Notas:**
- El alcance de entidades de la v1: clientes, conversaciones, productos, pedidos, citas y promesas; se amplía por demanda.
- La búsqueda local usa la caché del sync ([HU-APP-15](HU-APP-15-sync-offline-por-modulos.md)); antes de esa HU, degrada a "sin resultados offline".

**Backend implementado (2026-10-05):** [agent-core #244](https://github.com/devrochy/agent-core/pull/244) (base: cadena #240→#243) — `GET /api/v1/search` con registro de providers por pack, RBAC por sección (`effective_access`) y resultado uniforme para deep links; providers de conversaciones/clientes (core), clientes/promesas (cobranza), productos/pedidos (comercio) y citas (calendario). ADR-0096. 5 tests de integración en verde. Falta la parte de la app (barra global + búsqueda local sobre SQLite).

**App implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — `modules/busqueda`: barra con debounce y resultados agrupados por sección desde `/api/v1/search` (dentro de Más). Deep links a la entidad pendientes (deuda). 2 tests.
