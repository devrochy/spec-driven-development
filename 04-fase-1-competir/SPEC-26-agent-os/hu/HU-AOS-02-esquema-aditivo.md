---
id: HU-AOS-02
titulo: "Esquema aditivo del Agent OS (expand)"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [confianza, operacion]
req: [REQ-AOS-02, REQ-AOS-09]
dependencias: [HU-AOS-01]
skills: ["db-migration", "backend-design:migration-safety", "auditor-multitenant"]
estado: terminada
---

# HU-AOS-02 · Esquema aditivo del Agent OS (expand)

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-02

**Título:** Esquema aditivo del Agent OS (expand)

**Workstream:** Agent OS

**Historia:** Como desarrollador quiero crear las tablas y columnas nuevas del Agent OS sin cambiar la conducta, para que las HU siguientes trabajen sobre un esquema estable y aislado por negocio.

**Por qué importa (valor empresarial):** Separar el *expand* reduce el riesgo de cada HU posterior y permite revertir sin pérdida de datos.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-02, REQ-AOS-09

**Dependencias:** [HU-AOS-01](HU-AOS-01-adrs-del-agent-os.md)

**Criterios de aceptación (Gherkin):**
- **Sin cambio de conducta.** Dado la migración aplicada en test, cuando corren el golden y los journeys, entonces los resultados son iguales a los de antes.
- **Aislamiento.** Dado cada tabla nueva, cuando se consulta con otro negocio en el `tenant_scope`, entonces devuelve 0 filas (RLS forzada) y el test de RLS de CI la incluye.
- **Referencias entre negocios imposibles.** Dado un intento de insertar un permiso o una instancia que apunte a un agente de otro negocio, cuando se ejecuta, entonces la FK compuesta `(tenant_id, id)` lo rechaza.
- **Reversa.** Dado el `downgrade` en el stack efímero, cuando se ejecuta, entonces el esquema vuelve al estado anterior sin errores.

**Evidencia / Definición de Terminado:**
- Migraciones Alembic `0067`–`0071` de agent-core según el DDL del diseño (§4.3, con la tabla de lo que no es del expand): índices concurrentes, constraints `NOT VALID`, la función genérica nueva `prevent_mutation()` (rechaza DELETE y todo UPDATE salvo las columnas que recibe por `TG_ARGV`; `pack_versions` exime `yanked`), triggers de instancias y del Coordinador (los dos sentidos). Cada tabla grande se altera en su propia transacción y Alembic confirma cada revisión por separado (`transaction_per_migration`).
- Sin modelos SQLAlchemy: cada modelo llega con la HU que primero lee o escribe su tabla. `memory_vectors` ([HU-AOS-36](HU-AOS-36-memoria-por-scope.md)) y las columnas del gate en `eval_*` ([HU-AOS-21](HU-AOS-21-gate-de-release-pass-k.md)) quedan fuera.
- `channel_connections` sin estado ni scope propios (la pausa de Meta sigue siendo la de ADR-0122; las integraciones son del negocio), con el CHECK de que una fila con `meta_connection_id` no guarda credenciales y el índice único global de la clave de `webchat`.
- Sin tablas de políticas (presupuestos en el KernelSpec); `pack_installations` sin versión; `conversations.release_id` y `episode_started_at`; FKs compuestas en toda referencia del A2A; `UNIQUE (tenant_id, id)` en `conversations` y `customers` con `CREATE UNIQUE INDEX CONCURRENTLY` + `ADD CONSTRAINT … USING INDEX`.
- Banderas por negocio en `tenants` (`aos_runtime`, `aos_procedures`) con el CHECK de orden.
- Tablas de sistema (`pack_versions`) en la allowlist del hook de migraciones y en `docs/MULTITENANT.md`.
- `auditor-multitenant` sin hallazgos.

**Terminada (2026-10-11):** PRs agent-core [#407](https://github.com/devrochy/agent-core/pull/407).

**Riesgos/Notas:**
- Locks en tablas grandes (`conversations`, `usage_ledger`): solo columnas nullables o con default constante e índices concurrentes.
