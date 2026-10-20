# Propuestas de herramientas para ejecutar el plan

> 2026-10-01 · Estado: **decididas el 2026-10-02** (ver columna "Decisión"). Complementa el bloque D
> de la Semana 0 de la [guía de ejecución](../07-guia-de-ejecucion.md). Cuando se decide una, se marca
> aquí y, si es una skill, se registra en [`catalogo-skills.yml`](catalogo-skills.yml).

## Criterios

Una herramienta entra solo si cumple al menos uno de estos criterios, sin chocar con lo que ya hay
(skills del backend, `backend-design`, `code-review`, `codex` y el hook `guards.py`):

1. **Protege una invariante sola**, sin depender de que alguien se acuerde. Ejemplos: RLS, aislamiento
   entre packs, secretos.
2. **Ahorra trabajo que se repite en muchas HU.** Ejemplos: Meta y pagos.
3. **Cuesta poco mantenerla.**

## Resumen

| # | Propuesta | Tipo | Decisión (2026-10-02) | Esfuerzo | Por qué |
|---|---|---|---|---|---|
| R1 | Chequeo "RLS forzada" en el CI + migración `pack_subscriptions_0003` | CI | ✅ B · test de integración | S | Habría detectado N-36 sola |
| R2 | `ruff` también sobre `packages/` en el CI | CI | ✅ Sí | S | Hoy el CI no lintea los packs |
| R3 | `import-linter`: ningún pack importa de otro | CI | ✅ A · import-linter | S | Invariante 5 verificada en cada PR |
| S1 | Skill `ejecutar-hu` | Skill | ✅ Hecha | S | Aplica el ciclo por HU en las 165 HU |
| H2 | Hook de cierre en `solvershub-docs` (`regenerar.py --check`) | Hook | ✅ Hecho | S | El plan nunca queda con enlaces o frontmatter rotos |
| P1 | Plugin **Security Guidance** (Anthropic) | Plugin | ✅ Probar 2 semanas | S | Revisión de seguridad automática al editar y al cerrar |
| P2 | Plugin **context7** | Plugin | ✅ Sí | S | Documentación vigente de Next.js 16, FastAPI, SQLAlchemy, Expo |
| L1 | Desactivar los MCP que fallan y los plugins sin uso | Limpieza | ✅ Sí | S | Menos ruido y menos contexto gastado por sesión |
| H1 | Hook `ruff check` sobre el archivo `.py` recién editado | Hook | ✅ Sí | S | Corrige antes del CI |
| H3 | `guards.py` también bloquea leer `.env*` por Bash | Hook | ✅ Sí | S | Hoy solo está cubierta la tool Read |
| R4 | `pre-commit`: ruff + gitleaks + chequeo de migraciones | Repo | ✅ Sí | S | Cubre commits hechos fuera de Claude Code |
| R5 | Dependabot solo con alertas de seguridad | Repo | ✅ A · Dependabot | S | Backend, panel y APK |
| S2 | Skill `panel-ui` en `solvershub-panel` | Skill | ✅ Sí | S | `DESIGN.md` y BFF respetados por los agentes |
| S3 | Skill de conocimiento `meta-whatsapp` | Skill | ✅ Sí | M | Unas 15 HU de CONN, SH-05 y ARCH-13 |
| S4 | Skill de conocimiento `pagos-wompi` | Skill | ✅ Sí | S | COM-01, SUB-*, SH-04 |
| R6 | `schemathesis` contra el OpenAPI en el CI | Repo | 🕒 Hito 0B | M | Encuentra 500 como los de N-18 |
| R7 | `squawk` (lint de locks en migraciones) | Repo | 🕒 Después | M | Hoy lo cubre la skill `backend-design:migration-safety` |
| H4 | Review gate de Codex al cerrar | Hook | 🕒 Solo HU críticas | S | Segunda opinión en los caminos del dinero |
| P3 | Plugin **sentry** | Plugin | 🕒 Según [HU-ARCH-07](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md) | S | Solo si la observabilidad elige Sentry |
| P4 | Plugin **Superpowers** | Plugin | ⛔ No por ahora | S | Se superpone con las skills propias |
| — | Plugin **github** oficial, **securitymaxxing**, **Aevral**, **Sent**, **Playwright** (MCP) | Plugin | ⛔ No | — | Ver motivos abajo |

## 1. CI y repositorio

### R1 · Chequeo "RLS forzada" en el CI

Después de "Migrar y sembrar", un paso consulta las tablas con RLS habilitada y sin FORCE. Si hay
alguna, el CI falla. Es la misma consulta que el check `rls_forced` del checklist de producción.

| Opción | Pros | Contras |
|---|---|---|
| **A. Paso SQL en `ci.yml`** + migración `pack_subscriptions_0003` en el mismo PR | Barata. Cubre core y packs. Habría detectado N-36 | Depende de `psql` o de un one-liner de Python en el runner |
| B. Test de integración que llame a `check_rls_forced()` | Reutiliza el código del checklist; corre local igual que en el CI | Queda mezclado con los tests de negocio |
| C. Paso al final de `upgrade_all` que fuerce toda tabla con RLS | Imposible olvidarlo | Esconde el error en vez de mostrarlo; cambia producto, no solo control |

**Recomendación: B.** Un test es más fácil de correr en local que un paso del CI, y la migración `0003`
va en el mismo PR, porque sin ella el test falla desde el primer día. La opción C queda descartada:
forzar en silencio contradice "el error se ve".

**✅ Decidida (2026-10-02): B.** Test de integración que reutiliza `check_rls_forced()` + migración `pack_subscriptions_0003`.

### R2 · `ruff` sobre `packages/`

Hoy el CI corre `ruff check core cli scripts alembic evals tests`, sin `packages/`. Los packs ya pasan
limpios, así que agregarlo no rompe nada y evita la deriva.

**Recomendación: sí.** Es una línea.

**✅ Decidida (2026-10-02): sí**, incluir `packages/` en el paso de `ruff`.

### R3 · `import-linter`

Contratos:

1. `pack_*` independientes entre sí (invariante 5);
2. los packs no importan `cli`;
3. `agentcore_contracts` no importa nada del repo.

Hoy no hay violaciones: lo verifiqué el 2026-10-01.

| Opción | Pros | Contras |
|---|---|---|
| **A. import-linter** en el CI | Declarativo, mensajes claros, estándar en Python | Una dependencia de desarrollo más |
| B. Test propio que recorra los imports | Sin dependencias | Hay que mantener el parser |
| C. Confiar en `auditor-multitenant` | Cero costo | Solo corre cuando alguien lo pide |

**Recomendación: A.**

**✅ Decidida (2026-10-02): A**, `import-linter` en el CI.

### R4 · `pre-commit`

Corre ruff, gitleaks y un chequeo de migraciones que reutiliza `missing_isolation()` de `guards.py`
sobre los archivos en stage. Cubre los commits hechos desde la terminal, OpenCode o la web de GitHub.

- **Contra:** cada colaborador tiene que instalarlo. Por eso el CI (R1–R3) sigue siendo la red final.

**Recomendación: sí, después de R1–R3.**

**✅ Decidida (2026-10-02): sí**, configuración de `pre-commit` (ruff + gitleaks + chequeo de migraciones).

### R5 · Dependabot

Solo actualizaciones de seguridad, sin PR por cada versión nueva, en el backend (`pip`/`uv`), el panel
(`npm`) y la APK (`npm`/Expo).

| Opción | Pros | Contras |
|---|---|---|
| **A. Dependabot (seguridad)** | Nativo de GitHub, sin instalar nada | Menos configurable |
| B. Renovate | Agrupa y programa mejor | Requiere una app externa y más configuración |

**Recomendación: A.**

**✅ Decidida (2026-10-02): A**, Dependabot solo con alertas de seguridad (backend, panel, APK).

### R6 · `schemathesis` (Hito 0B)

Genera llamadas a partir de `docs/openapi.json` y reporta las rutas que devuelven 500 o que
incumplen el esquema. Corre en el CI contra la BD efímera, nunca contra test ni producción, porque crea
datos. Va con [HU-ARCH-09](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-09-release-y-e2e-entre-repos.md).

**Contra:** necesita un usuario semilla y excluir los webhooks.

### R7 · `squawk`

Lintea el SQL de las migraciones en busca de operaciones que bloquean tablas. Con Alembic hay que
generar el SQL en modo offline, y las migraciones dinámicas (como `0029`) no lo soportan.

**Recomendación: después.** Mientras tanto lo cubre la skill `backend-design:migration-safety`.

## 2. Hooks de Claude Code

### H1 · `ruff check` al editar

Hook `PostToolUse` sobre Write/Edit de archivos `.py` del backend. Corre `ruff check <archivo>` sin
`--fix` y, si hay errores, se los devuelve al agente. No usa `ruff format`, porque el repo no está
formateado de forma uniforme y generaría diffs ruidosos en archivos viejos.

**Recomendación: sí.**

**✅ Decidida (2026-10-02): sí.** Hook `PostToolUse` de `ruff check` al editar `.py`.

### H2 · `regenerar.py --check` al cerrar (solvershub-docs)

Hook `Stop` en `solvershub-docs/.claude/settings.json`. Si cambió algún `.md` de una HU, corre la
validación (un segundo) y avisa si dejó errores.

**Recomendación: sí**, sobre todo cuando varios agentes editan HU.

**✅ Decidida (2026-10-02): ya implementado** (`.claude/hooks/validar_backlog.sh` + `settings.json`).

### H3 · `.env` por Bash

El deny de lectura de `.env` cubre la tool Read, pero no `cat .env` ni `grep … .env`. Se agrega a
`guards.py`: se deniegan los comandos que lean `.env*`, salvo `.env.example`.

**Recomendación: sí.** Se hace en minutos y ya tiene dónde probarse (`tests/test_guards_hook.py`).

**✅ Decidida (2026-10-02): sí.** Añadir a `guards.py` el deny de lectura de `.env*` por Bash (salvo `.env.example`).

### H4 · Review gate de Codex

El plugin `codex` puede revisar con Codex cada vez que el agente intenta cerrar, y bloquear el cierre
si encuentra problemas.

- **Pros:** segunda opinión de otro modelo.
- **Contras:** consume rápido los límites de uso y alarga cada cierre.

**Recomendación:** no dejarlo siempre encendido. Usar `/codex:adversarial-review` a mano en las HU que
mueven dinero (COM-01, SUB-*, SH-04).

## 3. Plugins

### Recomendados

**P1 · Security Guidance** (publicado por Anthropic).

- **Qué hace:** advertencias por patrón al editar, revisión del diff al cerrar y revisor de commits
  (inyección, SSRF, secretos y más).
- **Pros:** es automático, a diferencia de `backend-design:security-reviewer`, que hay que pedir.
- **Contras:**
  - la revisión al cerrar suma latencia y tokens;
  - puede repetir hallazgos de `code-review`.
- **Recomendación:** probarlo 2 semanas en el backend y medir cuántos hallazgos reales aporta.

**P2 · context7.**

- **Qué hace:** trae la documentación vigente de cada librería, por versión.
- **Pros:** el panel usa Next.js 16 y la APK usa Expo/EAS, versiones posteriores a lo que los modelos
  conocen bien.
- **Contras:**
  - pide autenticarse en Context7;
  - las consultas (nombres de librerías) salen a un servicio externo. El código no.
- **Recomendación:** sí.

### Después

**P3 · sentry.** Solo si [HU-ARCH-07](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md)
elige Sentry, alojado o self-hosted. Si elige otra cosa, no aporta.

### No recomendados

- **Superpowers.** Buena biblioteca general (TDD, depuración, verificación), pero agrega un hook de
  inicio y reglas que se superponen con las skills del repo y con `ejecutar-hu`. Revisarlo si después
  de un mes faltara disciplina de TDD.
- **github oficial.** Ya hay un MCP de GitHub configurado que falla ("Authorization header is badly
  formatted") y el CLI `gh` funciona. Corresponde arreglar o desactivar el existente, no sumar otro.
- **securitymaxxing, Aevral.** Son de la comunidad y se superponen con P1, `code-review` y
  `backend-design`. Aevral además requiere instalar una GitHub App externa.
- **Sent.** Es el plugin de un proveedor de mensajería y empuja hacia su plataforma. SolversHub
  integra Meta directo.
- **Playwright (MCP).** Para mirar páginas ya está el navegador integrado. Los tests e2e del panel van
  con Playwright como test runner en el repo ([HU-ARCH-09](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-09-release-y-e2e-entre-repos.md) / [HU-UI-04](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md)), no como MCP.

### L1 · Limpieza

- **Desactivar o arreglar los MCP que fallan en cada sesión:** `github` (token mal formado) y
  `definite` (endpoint inexistente).
- **Desactivar en este proyecto los plugins `marketing` y `data`.** Sus MCP piden autenticación
  (HubSpot, Slack, BigQuery…) y sus skills ocupan contexto en cada sesión sin aportar a este plan.

> **Corrección (2026-10-02).** La premisa de arriba era falsa: las HU del plan recomiendan skills de
> esos plugins (`data` en 13 recomendaciones, como BILL-01, CONN-09, UI-07 y SUB-16; `marketing` en 23,
> sobre todo GTM, SH-06, BILL-08/09 y UX-03). Apagarlos dejaría esas HU sin sus skills, así que **se
> mantienen activos**. El ruido real son sus conectores sin autorizar (HubSpot, Slack, BigQuery…): se
> pueden ignorar o desactivar uno por uno en la configuración de conectores de claude.ai. Del MCP de
> GitHub: se arregla con un token (decisión del 2026-10-02).

## 4. Skills nuevas

| Skill | Dónde | Contenido | Cuándo |
|---|---|---|---|
| **S1 `ejecutar-hu`** | `solvershub-docs/.claude/skills` o usuario | Lee la HU y su spec, revisa el DoR, carga las skills del campo `skills`, implementa, cumple el DoD, cambia `estado` y corre `regenerar.py` | Ya (bloque D) |
| **S2 `panel-ui`** | `solvershub-panel/.claude/skills` | Tokens y reglas de `DESIGN.md`, BFF con `X-Tenant-Id`, `lib/labels.ts`, `useConfirm`, toasts | Antes de UI-01/UI-02 |
| **S3 `meta-whatsapp`** | backend | Embedded Signup (`config_id`, intercambio del código), plantillas y categorías, ventana de 24 h, precios por mensaje desde 2026, firma del webhook, códigos de error (130429, 131047…), BYOK y Tech Provider. Con fuentes y fecha de verificación | Antes de la Ola 2 (CONN-01) |
| **S4 `pagos-wompi`** | backend | Firma de integridad y checksum de eventos, sandbox y producción, montos mínimos, una URL de eventos por entorno (N-32), idempotencia y conciliación | Antes de COM-01 / SUB-03 |
| S5 `cerrar-spec`, `cierre-semanal` | `solvershub-docs` | Secciones 4 y 8 de la guía | Opcional |

Las skills de conocimiento (S3 y S4) llevan la fecha de cada dato y el enlace a la fuente. Se
re-verifican en el cierre de cada spec que las use.

## Orden sugerido

1. Mergear `chore/claude-skills-al-dia` (skills, hook y tests).
2. PR chico: R1 (test + migración `pack_subscriptions_0003`) + R2 + R3.
3. S1 `ejecutar-hu` + H2.
4. P1 y P2; limpieza L1.
5. H1, H3, R4, R5.
6. S2 antes de las HU del panel; S3 y S4 antes de la Ola 2.

## Estado de implementación (2026-10-02)

| # | Estado | Dónde | Pendiente |
|---|---|---|---|
| R1 | ✅ | backend #181: `tests/integration/test_rls_forced.py` + `pack_subscriptions_0003_force_rls` | — |
| R2 | ✅ | backend #181: `ruff check … packages` en el CI | — |
| R3 | ✅ | backend #181: `.importlinter` con 3 contratos | — |
| R4 | ✅ | backend #181 dejó el chequeo de migraciones sin efecto (corría `guards.py` sin payload). Corregido en backend #189: modo `--migraciones` contra HEAD, ruff v0.16.6. pre-commit 4.6.2 instalado en el backend. Verificado con un `git commit` real: la migración sin RLS no entra y la correcta pasa | — |
| R5 | ✅ | `dependabot.yml` en backend #181, panel #6 y apk #98. El backend pasa a `uv` en #189. Las alertas y los PR de seguridad están encendidos en los 3 repos (GET → 204 / `enabled: true`). La primera tanda de PR llegó el mismo día: backend #190, panel #8, apk #99 y #100. Los runs de Dependabot no tienen `LLM_API_KEY`. Desde backend #191 saltan los evals y dejan un aviso (verificado en #190) | — |
| H1 | ✅ | backend #181: `.claude/hooks/ruff_on_edit.sh` | — |
| H2 | ✅ | este repo: `.claude/hooks/validar_backlog.sh` | — |
| H3 | ✅ | backend #181: `guards.py` + tests | — |
| S1 | ✅ | este repo: `.claude/skills/ejecutar-hu` | — |
| S2 | ✅ | panel #6: `panel-ui`; conectada a 32 HU | — |
| S3 | ✅ | backend #181: `meta-whatsapp`; conectada a 16 HU | — |
| S4 | ✅ | backend #181: `pagos-wompi`; conectada a 14 HU | — |
| P1 | ✅ | Security Guidance 2.0.9, solo en el backend (scope local, en `.claude/settings.local.json`). El venv del Agent SDK está listo. En una prueba, la regla por patrón marcó `pickle.loads` y `os.system` | Revisión de la prueba el **2026-10-16**: hallazgos reales y consumo de tokens |
| P2 | ✅ | context7, para tu usuario. Responde consultas | — |
| L1 | ✅ | `data` y `marketing` se mantienen (ver la corrección en L1). El MCP de GitHub ya tiene token: `get_me` responde `devrochy` | `definite` (plugin `data`) sigue fallando al conectar |

**Además, al cerrar:** `uv.lock` no incluía `import-linter` desde #181, y cada `uv run` lo dejaba
modificado. Se regeneró en backend #189.

