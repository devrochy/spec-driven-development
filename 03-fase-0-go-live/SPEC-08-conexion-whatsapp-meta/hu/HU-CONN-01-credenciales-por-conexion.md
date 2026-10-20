---
id: HU-CONN-01
titulo: Resolver de credenciales por conexión con origen guardado
spec: SPEC-08
fase: 0
hito: 0A
workstream: Canales y conexiones
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, operacion]
req: [REQ-CONN-01, REQ-PLUS-02]
dependencias: []
skills: ["deep-research", "backend-design:security-discipline", "arquitecto", "backend-design:testing-with-discernment", "meta-whatsapp"]
ola: 2
estado: en-curso
---

# HU-CONN-01 · Resolver de credenciales por conexión con origen guardado

> Estado SDD: En curso — BYOK verificado contra Meta real en test (2026-10-08); falta Embedded Signup (sin app de plataforma en test), `/codex:adversarial-review` y golden sets.

**ID:** HU-CONN-01

**Título:** Resolver de credenciales por conexión con origen guardado

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio que conectó WhatsApp con su propia app de Meta (BYOK) quiero que Números, Plantillas, salud, webhook, precios y créditos funcionen con mis credenciales para gestionar mi conexión desde el panel.

**Por qué importa (valor empresarial):** BYOK es hoy el único alta que funciona y casi todas las herramientas de Meta fallan con él. Es la causa raíz de la mayoría de los defectos de Conexiones; sin arreglarla, nada de lo demás de esta spec funciona.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-CONN-01, REQ-PLUS-02

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **BYOK completo.** Dado una conexión BYOK, cuando abro Números, Plantillas o Diagnosticar, entonces cada llamada a la Graph API usa el token y el secreto de esa conexión y responde con datos reales.
- **Embedded Signup.** Dado una conexión ES, cuando uso las mismas herramientas, entonces usan su token y el secreto de la plataforma.
- **Origen guardado.** Dado cualquier conexión, cuando se consulta, entonces tiene `origin` guardado (`byok`, `embedded_signup`, `manual`); las existentes se migran con un script revisado.
- **Crons.** Dado el cron de plantillas y el de precios, cuando corren, entonces procesan cada conexión con sus propias credenciales y registran el error por conexión si falla.
- **Aislamiento.** Dado dos negocios, cuando uno usa sus credenciales, entonces nunca se resuelven las del otro (test).

**Evidencia / Definición de Terminado:**
- `MetaCredentials` + `credentials_for`; los 9 puntos de uso migrados (`meta_numbers_service.py`, `meta_templates_service.py`, `meta_ops.py`, `meta_health_service.py`, `meta_health.py`, `meta_pricing_sync.py`, `message_template_sync.py`, `meta_costs_service.py`, descarga de media); tests por origen.

**Implementada (2026-10-05, [PR #238](https://github.com/devrochy/agent-core/pull/238) en `devrochy/agent-core`, mergeado a `develop` en [`4844720`](https://github.com/devrochy/agent-core/commit/48447205ec262f68b4a7a7e7c78d7e33c0a13894); issue [#237](https://github.com/devrochy/agent-core/issues/237), ADR-0094):**
- `meta_connections.origin` (`byok` | `embedded_signup` | `manual`, `NOT NULL` sin valor por defecto, CHECK; migración `0051`): el **modo de credenciales vigente**. Lo fija cada alta y cambia si el wizard de ES toma una conexión BYOK. Backfill por tenant (fija `app.tenant_id`) con la evidencia de cada alta; con tokens de los dos orígenes queda `byok` (el que usaba el sender) y se listan en el log; sin evidencia → `manual`.
- `core/gateway/meta_credentials.py`: **una sola regla** de qué token usa cada origen (`access_token_refs`, `access_token_for`, `access_token_expires_at`) y `credentials_for` (`MetaCredentials`). BYOK usa el token y el App Secret de la conexión; ES y manual, el token de la conexión y la app de la plataforma. Aislamiento: chequeo de tenant (falla cerrado sin `tenant_scope`) + RLS + AAD del token store.
- Migrados: Números, Plantillas (servicios, panel SSR y API), salud, costos y créditos, endpoints de token BYOK y los crons de plantillas y precios (error por conexión, sin cortar a las demás): 8 de los 9 puntos de la lista. Además el **sender** y los **avisos de vencimiento**, que seguían eligiendo "BYOK primero", y las etiquetas "Origen" del panel. `POST /manual` valida con la app de la plataforma, la misma con la que se resuelve.
- **Descarga de media: no hay nada que migrar.** El core no la hace hoy (`inbound.py` deja `url: ""`); [HU-MEDIA-02](../../SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md) deberá construirla sobre `credentials_for`.
- Antes de esta HU los crons de plantillas y precios exigían el token de system user **y** `app_access`, que ninguna alta guarda juntos: no procesaban ninguna conexión real.
- Tests: 24 unitarios y 14 de integración nuevos (incluidos el sender y el cron de vencimiento con una conexión tomada por ES, y el SQL del backfill corrido como `app_runtime`, sin bypass), con pruebas de mutación sobre el resolver, la regla de token, los crons y el backfill. `ruff`, `basedpyright` e `import-linter` limpios. La suite completa solo falla en tests que **ya fallaban igual en `develop`** (sin red a Graph en el sandbox y 3 de otros temas). En el CI de agent-core el `gate` del PR pasó completo en los dos commits: lint, tipos, capas, unitarios, integración y el gate de evals (subconjunto crítico, con el LLM real).

**Revisión con los agentes del repo (2026-10-05):** `arquitecto` y `auditor-multitenant` sobre el primer commit. El arquitecto dio "no procede tal cual"; cada hallazgo se verificó contra el código y se corrigió en [`3d787c3`](https://github.com/devrochy/agent-core/pull/238/commits/3d787c3472952c65649ea3015721275969067c0c):
- dos fuentes de verdad (sender y avisos de vencimiento deducían el token) → una sola regla por `origin`;
- `origin` con default `manual` → sin default, y los 25 fixtures de tests fijan su origen;
- el resolver sin `tenant_scope` saltaba el chequeo de tenant → falla cerrado (`no_tenant_scope`);
- etiquetas "Origen" deducidas de `meta_app_id` → desde la columna;
- ADR-0094 ampliado: supersede parcial de ADR-0040 §3 y ADR-0041 §5, enmienda de ADR-0034, cita de ADR-0027;
- menores del auditor: lock de plantillas con el tenant en la llave, filtros explícitos de tenant, correlación por tenant en la migración y mensaje fijo en `create_template`.
- **Hallazgo alto preexistente, fuera de esta HU**: un negocio puede registrar la WABA o el número de otro y recibir sus mensajes (el resolver de número no mira `phone_numbers`, el de WABA hace `LIMIT 1` sin orden y las altas no verifican la WABA). Arreglo en [agent-core#241](https://github.com/devrochy/agent-core/pull/241) (ADR-0095), mergeado a `develop` en [`dd5ae43`](https://github.com/devrochy/agent-core/commit/dd5ae43c92852861b2b8f2c74681b77ae41ff17c) y desplegado en test el 2026-10-06 (`develop` [`45386bf`](https://github.com/devrochy/agent-core/commit/45386bf5effb4cda533729c9015eada1416f05e9)); falta verificarlo contra Meta real. Ver la bitácora.

**Verificación contra Meta real en test (2026-10-08, `develop` [`e2641a0`](https://github.com/devrochy/agent-core/commit/e2641a074283bc9601e60d16113b3c6767609066)):** conexión BYOK de `solvershub` (`d8782ebd…`, WABA `849940918140578`, número de prueba de Meta `+1 555-191-6775`). Se corrieron las funciones reales del core en el worker de test.

| Criterio | Resultado |
|---|---|
| BYOK completo | ✅ `credentials_for` resuelve la app propia de la conexión (token + App Secret). Con ellas responden con datos reales Números, Plantillas (sync y alta: `cancelacion_plan_prueba`, UTILITY en español, llegó a Meta) y Diagnosticar (8 checks, `token_valid` verificado contra Graph) |
| Embedded Signup | ⛔ **No verificable en test**: `META_APP_ID` de la plataforma está vacío. Queda para cuando se configure la app de la plataforma ([HU-SH-05](../../SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md)) |
| Origen guardado | ✅ Backfill: `select origin, count(*) from meta_connections group by 1` → `byok 1`, ninguna en `NULL` |
| Crons | ✅ Plantillas: sincroniza cada hora por conexión con sus credenciales. Precios: después de los arreglos de abajo, `sync_all_waba_pricing` guardó 2 filas reales en `pricing_daily` (2026-10-08, CO: 2 SERVICE y 3 UTILITY) y una segunda corrida no las duplica |
| Aislamiento | ✅ Por tests de integración (`test_meta_credentials_origin.py`, resolver que falla cerrado sin `tenant_scope`). En test hay una sola conexión de Meta: no hay caso real entre dos negocios |

Lo que encontró la verificación (todo mergeado y desplegado en test):
- [core #298](https://github.com/devrochy/agent-core/pull/298): la salud marcaba `degraded` un número sano con `code_verification_status = NOT_VERIFIED` (número de prueba o registrado sin SMS). Ahora decide el `status` del número (`CONNECTED`). La conexión volvió sola a `connected` (ADR-0102).
- [core #302](https://github.com/devrochy/agent-core/pull/302): el cron de precios **nunca guardó nada**. Meta agrupa los puntos en `data[].data_points[]` y el parser descartaba cada grupo como inválido (los mocks usaban la forma plana). Antes de #298 tampoco corría para esta conexión, porque solo procesa las `connected`.
- [core #300](https://github.com/devrochy/agent-core/pull/300), **seguridad**: el worker de Celery no pasaba por `configure_logging` y `httpx` registraba en INFO la URL de `/oauth/access_token?…&client_secret=…`. El App Secret de la app BYOK quedó en claro en el log del worker de test (1 línea; ninguna en los otros contenedores en 72 h). Ahora `httpx`/`httpcore` van en WARNING en la API, el worker y el beat; verificado sin líneas tras el deploy. **Rotar el App Secret de esa app** (lo hace el dueño en Meta).
- [core #296](https://github.com/devrochy/agent-core/pull/296): la respuesta salía por WhatsApp Web cuando el cliente había escrito al número de Meta (la conversación guardaba las dos rutas).

**Falta para `terminada`:**
- [ ] Verificar el criterio de Embedded Signup con una conexión ES real (requiere `META_APP_ID`/secreto de la plataforma en test).
- [x] Verificar en test los criterios con una conexión BYOK real (2026-10-08, tabla de arriba).
- [x] Revisar el resultado del backfill en test: `byok 1`, ninguna en `NULL`.
- [x] Revisión de los agentes `arquitecto` y `auditor-multitenant`; hallazgos corregidos en `3d787c3`.
- [ ] `/codex:adversarial-review` (no existe en la sesión en la nube; correrlo desde Claude Code local).
- [ ] Golden sets completos sin regresión (`eval-runner`). El subconjunto crítico ya pasó en el CI del PR; el cambio no toca prompts.
- [x] Mergear el PR con los checks en verde (agent-core no tiene protección de rama): mergeado a `develop` el 2026-10-05 ([`4844720`](https://github.com/devrochy/agent-core/commit/48447205ec262f68b4a7a7e7c78d7e33c0a13894)), con `gate` y `secret-scan` en verde.
**Fixes posteriores (2026-10-06):** [agent-core #250](https://github.com/devrochy/agent-core/pull/250) (ADR-0101: una conexión BYOK degradada o con error sigue prestando su secreto) + [#253](https://github.com/devrochy/agent-core/pull/253) (ADR-0102: una conexión en `error`/`degraded` se recupera sola y solo mejora con el diagnóstico verificado) — mergeados a `develop` y desplegados en test. La recuperación sola se verificó contra Meta el 2026-10-08 (`degraded` → `connected` tras #298). **Pendiente:** confirmar el secreto de la plataforma antes de producción.

**Riesgos/Notas:**
- Defecto 1 y 9 de la auditoría.
- Al desplegar: los crons ahora **sí llaman a Graph** para las conexiones ES y BYOK (más tráfico que antes), y la salud de las BYOK corre completa, así que una con el token vencido pasará a `degraded`/`error`. `POST /manual` deja de aceptar tokens de la app propia del negocio (para eso está el wizard BYOK).
- Fuera de alcance, anotado en `docs/BACKLOG.md` de agent-core: suscripciones y webhook siguen eligiendo "la" conexión del tenant, y `meta_app_id` queda desalineado tras una toma por ES ([HU-CONN-05](HU-CONN-05-webhook-por-conexion.md)); `meta_private.meta_tokens` tiene RLS habilitada pero no forzada.
