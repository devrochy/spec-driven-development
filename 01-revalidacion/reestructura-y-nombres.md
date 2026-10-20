# Reestructura `solvershub-<section>` y nombres

Fuente: inventario de repos del 2026-09-30 y verificación directa del 2026-10-01.

## Repos actuales

| Repo | Remoto / rama | Para qué | Estado |
|---|---|---|---|
| `solvershub-backend` | `devrochy/agent-core`; local en `fix/ref-cargo-link` (= `origin/develop` `b0f54d3`) | Motor multi-tenant: FastAPI `/api/v1`, panel SSR clásico en retiro, webhooks, Celery, packs | 495 commits; CI en runner propio con ruff, migraciones, tests, gate de evals y gitleaks |
| `solvershub-panel` | `devrochy/solvershub-panel` | Panel nuevo (`apps/panel-web`, Next.js 16) + sistema de marca (`brand/`) | CI sin paso de tests; **sin despliegue de producción** |
| `solvershub-apk` | `devrochy/solvershub-apk` | App de campo de cobranza (Expo 57) | `AGENTS.md:7,9,19` todavía describe el backend NestJS |
| `solvershub-landing` | `devrochy/solvershub-landing` | Sitio público, formularios de lead, formulario alojado `/f/<slug>` | Sin CI; corre en Coolify pero **no figura en el runbook**; `package.json` se llama `landing` |
| `solvershub-comercial` | `devrochy/solvershub-comercial` | Legal, runbooks, kit comercial, pruebas, paridad | **Sin README** |

## La carpeta `solvershub/apps/`

| Verificación | Resultado |
|---|---|
| Contenido | Solo `apps/panel-web/.next/` (caché de build) y un log de error de 41 líneas |
| ¿Algo único? | No: `diff -rq` contra `solvershub-panel/apps/panel-web` solo muestra archivos que existen en el repo |
| Origen | Creada el 2026-09-28 a las 22:54 por un servidor de desarrollo que quedó con la ruta anterior a la reestructura (`next.config.ts:6-8` fija `turbopack.root: process.cwd()`) |
| Referencias | Ninguna en CI, compose, Makefile ni Dockerfiles; solo texto en ADR-0078:15, ADR-0079:8 y `PLAN-DE-PRUEBAS.md:4,23` |

**Veredicto: se elimina** ([HU-REP-01](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-01-limpiar-residuos.md)).

**Otros `apps/`**

- `solvershub-backend/apps/{gateway,agentos,worker}` y `packages/{core-crm,core-runtime,channel-whatsapp}`:
  stubs vacíos que el propio `CLAUDE.md` llama residuos. Se eliminan.
- `solvershub-panel/apps/` **se mantiene**: lo usan el CI (`ci.yml:34,62-72`), la base de Coolify, el
  `Makefile:11`, la profundidad relativa de `package.json:17` y `parity-report.py:105`.

## Clones viejos fuera de `solvershub/`

| Ruta | Estado | Acción |
|---|---|---|
| `Proyectos/agent-core`, `Proyectos/landing` | Ya no existen: se movieron | Recrear el venv del backend (`.venv/pyvenv.cfg` apunta a la ruta vieja) |
| `Proyectos/cobranza/app-cobranza`, `app-cobranza-admin` | Legados NestJS/Next, en sincronía con su remoto | Archivar en GitHub, borrar local |
| `agent-core (copy)`, `agent-core-end`, tarballs v1/v2/v3 | Copias viejas; todo está en la historia del backend | Borrar (revisar antes el `.env` de la copia) |

## Mapa de nombres

| Actual | Propuesto | Por qué |
|---|---|---|
| Carpeta `solvershub-backend`, GitHub `devrochy/agent-core` | **`solvershub-core`** | Es el único que rompe la convención; GitHub redirige las URL viejas |
| `solvershub-panel/brand/` (15 MB) | **`solvershub-brand`** (repo nuevo) | Los tokens alimentan panel, APK y landing; los binarios pesados no pertenecen a una app |
| Infra fuera de git (túneles de Cloudflare, crontab `@reboot`, registry local, runners, inventario de Coolify, imagen de Postgres) | **`solvershub-infra`** (repo nuevo) | Hoy casi nada de esto está versionado: es la base de la recuperación ante desastres |
| — | **`solvershub-docs`** (esta carpeta) | Hogar único de la planificación |
| `solvershub-panel`, `-apk`, `-landing`, `-comercial` | Se mantienen | Ya cumplen la convención; nunca cambiar `com.solvershub.apk` ni el projectId de EAS |

**No se separan**: contratos, evals y ADR del core (se importan en proceso o los referencia el código).

## Cambios cosméticos (seguros)

- Renombrar en GitHub y en Coolify (`agent-core*` → `solvershub-core-*`, `panel-web-test` →
  `solvershub-panel-test`), actualizar el runner (`/home/devrochy/actions-runner/.runner`) y
  `runbooks/backup-restore.md:13`.
- Renombrar la carpeta y actualizar `solvershub-panel/Makefile:9` y `apps/panel-web/package.json:17`.
- Arreglar **13 enlaces rotos a `../agent-core`** en comercial: `legal/contrato-servicio.md:18`,
  `runbooks/onboarding-cliente.md:7`, `runbooks/README.md:14,19`, `PLAN-DE-PRUEBAS.md:76`,
  `PRODUCCION-SOLVERSHUB.md:7,25,27,35,108,122`, `comercial/README.md:10,44`.
- README correcto por repo: el del panel todavía es el "Centro de lanzamiento" (`README.md:1`);
  comercial no tiene; el de la landing es el de create-next-app.
- Agregar la landing al runbook de despliegue.

## Cambios rompedores (con alias y ADR)

| Identificador | Dónde | Recomendación |
|---|---|---|
| dist `agent-core` | `pyproject.toml:6` | Renombrar a `solvershub-core` (los imports son `core`/`cli`) |
| CLI `agent-core` | `pyproject.toml:66`; lo usa el arranque del contenedor (`scripts/entrypoint.sh:43`), CI y Makefile | Agregar `solvershub` y mantener el alias un tiempo |
| Grupos de entry points `agent_core.plugins` / `.channels` | `core/plugin_manager.py:45`, `core/gateway/channels/registry.py:23`, `core/db/migrations.py:87`, `pyproject.toml` de cada pack | Descubrir ambos nombres durante la transición |
| `agentcore_contracts` (22 referencias) | `core/onboarding.py:18`, `core/llm/prompt_builder.py:19`, `evals/runner.py:25` | **Necesita ADR** (contratos inmutables): shim de re-exportación o mantener el nombre |
| `AGENT_CORE_ROLE`, `AGENT_CORE_API_URL`, `AGENT_CORE_INTEGRATION` | compose, entrypoint, panel, ~150 tests | Leer el nombre nuevo con respaldo del viejo; `AGENT_CORE_INTEGRATION` en un solo PR para no saltar tests en silencio |

**Nunca se renombran**: IDs de plugin `pack_*` (están en la base, en rutas de la APK y en tablas
`alembic_version_<id>`), la base `agent_core` y sus roles, los streams `agent_core:inbound[:dlq]`, el
nombre de la app Celery, las cookies del panel clásico y `COMPOSE_PROJECT_NAME`.

## Fugas de "agent-core" ante el cliente (rompen el manual de marca)

- `solvershub-backend/core/billing/providers/wompi.py:81`: descripción del link de pago de Wompi.
- `solvershub-backend/packages/pack-calendar/pack_calendar/skills.py:388`: texto del evento de
  Google Calendar que reciben los asistentes.

Se corrigen ya, con un test que impida que vuelvan ([HU-REP-04](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-04-sin-fugas-de-marca-tecnica.md)).

## Deriva documental

- `solvershub-backend/README.md:55` dice que los ADR llegan a 0021 y `:41` que el panel es SSR.
- `docs/adr` y `docs/ADR` chocan en sistemas que no distinguen mayúsculas (macOS, Windows).
- `docs/ROADMAP.md` no se actualiza desde el 2026-09-27; `docs/BACKLOG.md:198-215` todavía dice que
  `pack_subscriptions` no existe.
- `solvershub-panel/brand/manual-de-marca.md:104` permite "nombres técnicos" en los repos (contradice
  la convención nueva) y `:102` dice `solvershub.com` cuando el dominio vivo es `solvershub.site`.
