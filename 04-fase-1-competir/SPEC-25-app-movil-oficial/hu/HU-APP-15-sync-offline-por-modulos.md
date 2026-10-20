---
id: HU-APP-15
titulo: Sincronización offline-first por módulos
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-APP-09]
dependencias: [HU-APP-06, HU-APP-08]
skills: [backend-design:idempotency-and-side-effects, backend-design:data-modeling-discipline]
estado: terminada
---

# HU-APP-15 · Sincronización offline-first por módulos

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-15

**Título:** Sincronización offline-first por módulos

**Workstream:** App móvil

**Historia:** Como usuario en calle o con mala conexión quiero que la app sirva datos cacheados sin conexión, encolice mis escrituras seguras y sincronice todo al reconectar sin duplicados ni pérdidas, para que la app oficial funcione con conexión intermitente en todos los módulos, no solo en cobranza.

**Por qué importa (valor empresarial):** El offline-first del campo es el diferencial probado de la app. Extenderlo a los módulos del panel (leer caché sin red, escribir con cola) convierte una limitación de conexión en ventaja comercial y justifica "una app para todo" incluso en zonas con conectividad pobre.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-09

**Dependencias:** [HU-APP-06](HU-APP-06-almacenamiento-local-cifrado.md), [HU-APP-08](HU-APP-08-operacion-movil.md)

**Criterios de aceptación (Gherkin):**
- **Sync incremental.** Dado un módulo con datos cacheados, cuando la app reconecta, entonces sincroniza con `GET /api/v1/sync/{entidad}?cursor=` recibiendo `{items, nextCursor, deletedIds}` y aplica altas, cambios y borrados suaves.
- **Escrituras encoladas.** Dado un cambio de estado de pedido o cita sin conexión, cuando la app sincroniza, entonces el evento se envía con idempotencia (ack por evento) y no se duplica aunque se reintente.
- **Conflicto.** Dado un registro cambiado en dos lugares, cuando sincroniza, entonces resuelve por `updated_at` (last-write-wins) y registra la resolución en auditoría local.
- **Matriz offline.** Dado un módulo, cuando se consulta la matriz documentada, entonces se sabe qué es lectura cacheada, qué es escritura encolable y qué exige red (con estado explícito de sin-conexión).

**Evidencia / Definición de Terminado:**
- Backend: `GET /api/v1/sync/{entidad}` genérico con cursor, límites y RBAC por entidad (tablas auditables con `updated_at`/`deleted_at`; tests cross-tenant y de paginación; OpenAPI regenerado).
- App: `src/data/sync-engine/` (cursor por entidad, rehydrate, conflictos LWW, retry con backoff); integración con TanStack Query (hydrate de caché); matriz offline documentada en `docs/arquitectura.md`; tests de integración con simulación de red intermitente.
- Evidencia en test: un viaje pedido→offline→sync→online sin duplicados, medido y grabado.

**Riesgos/Notas:**
- El cursor por entidad requiere `updated_at` en las tablas; si alguna no lo tiene, se incluye la migración aditiva en esta HU.
- El alcance de entidades sincronizables es el de la búsqueda global más carteras y promesas; la sincronización de evidencias (fotos) sigue por demanda como hoy.

**Backend implementado (2026-10-05):** [agent-core #246](https://github.com/devrochy/agent-core/pull/246) (base: cadena #240→#243→#244) — `GET /api/v1/sync/{entidad}` con adapters por pack y contrato `{items, nextCursor, deletedIds}` (borrados avanzan el cursor), migraciones aditivas `updated_at` (cobranza 0015/0016, comercio crm_0008), `POST /api/v1/audit/mobile-events` con `mobile_audit_events` (0053) idempotente por (tenant, event_id). ADR-0097. 6 tests de integración en verde. Falta la parte de la app (`src/data/sync-engine/` + integración con TanStack Query).

**App implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — motor `@data/sync-engine`: cursor por entidad, upsert LWW en `cache_entidad`, `deletedIds`, paginación y corte ante error conservando cursor. **Wire (2026-10-06):** [apk #121](https://github.com/devrochy/solvershub-apk/pull/121) — `SincronizadorProvider` global (sync al arrancar y al reconectar), escrituras encoladas con despachadores por módulo, cambio de estado de pedido offline con aviso, y búsqueda local sobre caché sin red. 595/595 tests. Deuda: hidratación visual de listas offline por pantalla y escrituras encoladas de citas/cobranza-admin.
