# 07 · Guía de ejecución: cómo avanzar, checklists y skills

Esta guía convierte el plan en trabajo diario: qué hacer primero, cómo ejecutar cada spec y cada HU,
cuándo dar por cerrado un hito y qué skill, comando o agente de Claude Code conviene usar en cada caso.

> **Cómo se marcan las casillas.** Las de las HU se marcan solas: cuando una HU termina, se cambia
> `estado: terminada` en su frontmatter y se corre `python3 herramientas/regenerar.py`. Las demás
> (arranque, criterios de salida, cierre) se marcan a mano en este archivo.

## 1. Cómo te recomiendo avanzar

1. **Semana 0: prepara el terreno antes de escribir código de producto.** Cierra las decisiones que
   bloquean el Hito 0A, arranca los trámites externos y pon al día tus herramientas. Es la semana con
   más retorno: los agentes de IA siguen las skills al pie de la letra, y hoy cinco skills del backend
   describen un proyecto TypeScript con Supabase que ya no existe. Además, el hook que exige RLS en las
   migraciones solo revisa archivos `.sql`, y las migraciones reales son Alembic (`.py`): **hoy ninguna
   migración nueva pasa por ese control**.
2. **Ejecuta el Hito 0A por olas, en orden.** La Ola 1 (12 HU) quita riesgos que pueden romper la
   operación o el cobro hoy mismo: modelo discontinuado, Meta cobrando cada burbuja, el LLM eligiendo
   montos, errores de negocio que apagan packs. No abras HU del 0B mientras el 0A esté abierto, salvo
   los trámites externos.
3. **Una HU = un issue = una rama = un PR.** Crea un issue por HU en el repo dueño y trabájalo con
   `/work-on-issue #N`, siguiendo el ciclo de la sección 5. Si una HU L no cabe en un PR revisable,
   divídela en commits, no en HU nuevas.
4. **Revisión doble donde hay dinero, seguridad o datos de varios negocios.** `/code-review` en todo
   PR; además `/codex:adversarial-review` y el agente `auditor-multitenant` en pagos, suscripciones,
   alta automática, credenciales y migraciones. Para los PR más grandes (outbox, resolver de
   credenciales, aprovisionamiento) considera `/code-review ultra`: una revisión multiagente en la nube
   que lanzas tú y que tiene costo.
5. **Cierre semanal de 30 minutos** (sección 8): estados, `regenerar.py`, trámites, riesgos y días
   reales.
6. **Recalibra al cerrar cada spec** el factor de aceleración y el rango de fechas del
   [calendario](02-vision-y-decisiones/calendario-estimado.md).
7. **No cambies de hito sin su criterio de salida.** El 0A se cierra solo con la evidencia del recorrido
   completo de un prospecto real.
8. **Desde el 2026-10-09, lo que queda del 0A avanza en frentes paralelos** (producción, alta
   automática, conexiones y calidad). Lo que falta de las Olas 2 y 3 depende sobre todo del dueño, así que
   el orden lo marcan las dependencias de cada HU, no la ola. El reparto, los issues y las reglas para
   que las sesiones no choquen están en la [bitácora](08-bitacora-de-ejecucion.md#plan-en-paralelo-del-hito-0a-2026-10-09).

### Ritmo sugerido

| Momento | Qué hacer | Apoyo |
|---|---|---|
| Lunes (30 min) | Elegir las HU de la semana dentro de la ola actual y revisar su DoR | Sección 6 |
| Cada HU | Ciclo de la sección 5 | Skills de la HU (sección 6) |
| Viernes (30 min) | Cierre semanal | Sección 8 |
| Al cerrar una spec | Paso "Cerrar" de la sección 4 | Agentes `eval-runner` y `auditor-multitenant` |

## 2. Herramientas disponibles

Inventario del 2026-10-01 en esta máquina y en tu cuenta de claude.ai. Cómo se usan en Claude Code:

- **Skill**: pídela por su nombre ("usa la skill `db-migration`") o escríbela como `/nombre`. Muchas se
  activan solas cuando la tarea coincide con su descripción.
- **Comando**: se escribe tal cual (`/code-review`, `/codex:adversarial-review`, `/work-on-issue #12`).
- **Agente**: pídelo por su nombre ("usa el agente `auditor-multitenant` sobre este diff"); trabaja
  aparte y devuelve un informe.

Las marcadas ⚠️ están desactualizadas y no se usan hasta corregirlas (las cinco del backend se
corrigieron el 2026-10-01, sección 3, bloque D). El catálogo vive en [`herramientas/catalogo-skills.yml`](herramientas/catalogo-skills.yml);
si agregas una skill, se registra ahí y cada HU puede recomendarla en su campo `skills`.

<!-- GENERADO:catalogo:inicio -->
**Proyecto**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `adr` | skill | Registrar una decisión de arquitectura como ADR numerado en docs/adr | ✅ | 38 |
| `agentcore-conventions` | skill | Dónde va cada cosa (core, pack, configuración, artefacto del tenant), límites de capa y nombres reales del repo Python | ✅ | 35 |
| `db-migration` | skill | Crear o revisar migraciones Alembic (core y packs) con tenant_id, RLS forzada, policy con nullif y tablas de sistema | ✅ | 34 |
| `desplegar-test-agent-core` | skill | Mergear a develop, desplegar en el Coolify de test (app tr0vpdei…) y verificar salud; nunca toca producción | ✅ | 10 |
| `eval-author` | skill | Crear o ampliar golden sets por tenant o del framework | ✅ | 44 |
| `incident` | skill | Runbook de triage cuando el agente no responde o responde mal | ✅ | 1 |
| `meta-whatsapp` | skill | Conocimiento vigente de WhatsApp/Meta: Embedded Signup, plantillas, ventana de 24 h, precios 2026, firma del webhook y BYOK | ✅ | 28 |
| `pagos-wompi` | skill | Conocimiento vigente de Wompi: firma de integridad, checksum de eventos, sandbox/producción, mínimos y conciliación | ✅ | 18 |
| `new-pack` | skill | Crear un pack vertical nuevo con su estructura Python, Alembic y flow | ✅ | 13 |
| `new-tool` | skill | Crear una MCPTool en un pack: schema, handler con errores como resultado, flow.json, tests cross-tenant y eval | ✅ | 29 |
| `onboard-tenant` | skill | Dar de alta un cliente con el CLI real (tenant create/seed), TENANTS_ROOT, BYOK, evals por tenant y publicación | ✅ | 9 |
| `release` | skill | Release develop → main: gates de CI, auditor, evals, migraciones, OpenAPI, CHANGELOG, deploy de producción, tag y rollback | ✅ | 8 |
| `arquitecto` | agente | Revisar un plan o diseño contra los ADR y las invariantes antes de codificar | ✅ | 21 |
| `auditor-multitenant` | agente | Auditar el aislamiento entre negocios tras cambios de queries, migraciones, tools o rutas | ✅ | 32 |
| `customizer` | agente | Ajustar prompt, tono y comportamiento del asistente de un negocio | ✅ | 8 |
| `eval-runner` | agente | Correr el golden set contra un candidato y reportar regresiones | ✅ | 20 |
| `migrator` | agente | Migrar datos externos (CSV, BD, API) a las entidades de los packs | ✅ | 2 |
| `optimizer` | agente | Optimizar costo de LLM y precisión de las tools | ✅ | 12 |
| `plugin-dev` | agente | Generar un plugin o pack desde cero | ✅ | 3 |

**Solvershub-docs**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `ejecutar-hu` | skill | Ejecutar una HU de punta a punta (DoR, skills del frontmatter, DoD, estado y regenerar) | ✅ | 1 |

**Solvershub-panel**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `panel-ui` | skill | UI del panel nuevo: DESIGN.md, tokens, BFF con X-Tenant-Id y formateo es-CO | ✅ | 83 |

**Plugin backend-design**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `backend-design:think-before-coding` | skill | Flujo senior de 6 pasos antes de escribir un componente backend | ✅ | 8 |
| `backend-design:error-handling-as-design` | skill | Diseñar el camino de error como parte del contrato | ✅ | 11 |
| `backend-design:idempotency-and-side-effects` | skill | Idempotencia y outbox en pagos, mensajes, eventos y terceros | ✅ | 34 |
| `backend-design:data-modeling-discipline` | skill | Invariantes en el esquema en vez de confiar en la aplicación | ✅ | 22 |
| `backend-design:migration-safety` | skill | Migraciones sin bloqueos, reversibles y por etapas | ✅ | 11 |
| `backend-design:query-discipline` | skill | Evitar N+1, índices faltantes, listas sin límite y mala paginación | ✅ | 11 |
| `backend-design:security-discipline` | skill | Reflejo de seguridad en cada cambio (IDOR, inyección, secretos, auth faltante) | ✅ | 36 |
| `backend-design:auth-and-authorization` | skill | Sesiones, tokens, permisos y alcance multi-tenant | ✅ | 19 |
| `backend-design:observability-by-default` | skill | Logs estructurados, métricas RED, trazas y healthchecks reales | ✅ | 12 |
| `backend-design:performance-and-scaling` | skill | Decidir rendimiento y escala con la carga real en mente | ✅ | 6 |
| `backend-design:testing-with-discernment` | skill | Decidir qué vale la pena probar y evitar tests que no prueban nada | ✅ | 28 |
| `backend-design:debugging-discipline` | skill | Método de investigación ante algo roto, lento o incorrecto | ✅ | 2 |
| `backend-design:boring-by-default` | skill | Defender la complejidad antes de adoptar tecnología nueva | ✅ | 4 |
| `/backend-design:design` | comando | Diseñar un componente backend con el flujo de 6 pasos antes de codificar | ✅ | 0 |
| `/backend-design:audit` | comando | Auditar un componente existente (invariantes, errores, idempotencia, permisos, observabilidad) | ✅ | 0 |
| `/backend-design:review-migration` | comando | Revisar una migración antes de commitearla | ✅ | 0 |
| `/backend-design:explain-this-query` | comando | Predecir el plan de ejecución de una query y sus riesgos | ✅ | 1 |
| `/backend-design:hunt-n-plus-one` | comando | Buscar patrones N+1 y proponer arreglos | ✅ | 1 |
| `backend-design:component-architect` | agente | Producir el blueprint de implementación de un componente backend | ✅ | 0 |
| `backend-design:schema-reviewer` | agente | Revisar un esquema o migración (restricciones, tipos, índices, riesgos) | ✅ | 3 |
| `backend-design:security-reviewer` | agente | Revisar un diff o componente en busca de fallas de seguridad | ✅ | 13 |
| `backend-design:incident-thinker` | agente | Listar incidentes probables de un diseño con detección y recuperación | ✅ | 5 |
| `backend-design:incident-investigator` | agente | Guiar una investigación de un problema activo en test o producción | ✅ | 1 |
| `backend-design:boring-tech-advisor` | agente | Cuestionar la adopción de tecnología nueva frente a la alternativa aburrida | ✅ | 2 |

**Plugin code-review**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `/code-review` | comando | Revisar un PR; `/code-review ultra` lanza una revisión multiagente en la nube (la inicia el usuario y tiene costo) | ✅ | 10 |

**Plugin codex**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `/codex:review` | comando | Segunda revisión del estado local de git con Codex | ✅ | 0 |
| `/codex:adversarial-review` | comando | Revisión que desafía el enfoque y las decisiones de diseño | ✅ | 9 |
| `/codex:rescue` | comando | Delegar una investigación o un arreglo difícil a Codex cuando hay bloqueo | ✅ | 0 |

**Plugin work-on-issue**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `work-on-issue` | skill | Trabajar un issue de GitHub de punta a punta (análisis, TDD, PR) con `/work-on-issue | ✅ | 0 |

**Plugin frontend-design**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `frontend-design` | skill | Dirección visual intencional al construir o rehacer UI | ✅ | 92 |

**Plugin figma**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `figma-design-to-code` | skill | Implementar una pantalla a partir de un diseño en Figma | ✅ | 3 |
| `figma-generate-design` | skill | Llevar una página del panel a Figma para iterar el diseño | ✅ | 0 |
| `figma-generate-library` | skill | Construir el sistema de diseño (tokens y componentes) en Figma desde el código | ✅ | 1 |
| `figma-generate-diagram` | skill | Diagramas (arquitectura, flujos) en FigJam | ✅ | 1 |

**Usuario**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `web-perf` | skill | Medir Core Web Vitals y accesibilidad de panel y landing | ✅ | 6 |
| `cloudflare` | skill | Plataforma Cloudflare (DNS, Workers, R2, WAF) | ✅ | 3 |
| `cloudflare-one` | skill | Tunnel y Access (borde de producción, rutas públicas de webhooks) | ✅ | 4 |
| `turnstile-spin` | skill | Configurar Turnstile de punta a punta en formularios y widgets | ✅ | 4 |
| `cloudflare-email-service` | skill | Correo transaccional (invitaciones, avisos) si se elige Cloudflare en vez de SMTP | ✅ | 1 |
| `desplegar-test` | skill | Desplegar a test en Coolify repos distintos del backend | ✅ | 1 |
| `kpi-dashboard-design` | skill | Diseñar dashboards de KPIs (MRR, churn, salud operativa) | ✅ | 14 |

**Claude.ai**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `built-in-browser` | skill | Probar el panel o la landing en el navegador integrado | ✅ | 24 |
| `chrome-browser` | skill | Guiar trámites en sitios donde tienes sesión (Business Manager); las credenciales las pones tú | ✅ | 1 |
| `theme-factory` | skill | Aplicar temas consistentes a material y reportes | ✅ | 1 |
| `deep-research` | skill | Investigar con varias fuentes y comparar opciones (proveedores, requisitos de Meta, ISO) | ✅ | 25 |
| `doc-coauthoring` | skill | Coescribir specs, ADR, contratos y documentos de decisión | ✅ | 12 |
| `docs` | skill | Documentos compartibles y comentables (fuera del repo) | ✅ | 1 |
| `docx` | skill | Documentos Word (por ejemplo, para el abogado) | ✅ | 1 |
| `pdf` | skill | PDF (one-pager, reportes) | ✅ | 2 |
| `pptx` | skill | Presentaciones (deck comercial) | ✅ | 3 |
| `xlsx` | skill | Hojas de cálculo (matriz competitiva, importaciones CSV) | ✅ | 3 |
| `canvas-design` | skill | Piezas gráficas estáticas para redes | ✅ | 1 |
| `skill-creator` | skill | Crear o mejorar skills propias (por ejemplo, el ciclo por HU) | ✅ | 0 |

**Plugin data**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `data:analyze` | skill | Responder preguntas de datos, desde un número hasta un análisis completo | ✅ | 3 |
| `data:sql-queries` | skill | SQL correcto y eficiente (calibración del ledger, KPIs, conciliación) | ✅ | 9 |
| `data:validate-data` | skill | Revisar un análisis antes de compartirlo | ✅ | 2 |
| `data:statistical-analysis` | skill | Tendencias, outliers y pruebas de significancia (benchmarks) | ✅ | 4 |
| `data:build-dashboard` | skill | Dashboard HTML con KPIs, gráficos y filtros | ✅ | 1 |

**Incluida en Claude Code**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `dataviz` | skill | Gráficos, KPIs y paletas de datos con validación de color y accesibilidad | ✅ | 5 |

**Integrada**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `claude-api` | skill | Precios, caché de prompts, visión y herramientas de la API de Claude | ✅ | 5 |

**Plugin marketing**

| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |
|---|---|---|---|---:|
| `marketing:campaign-plan` | skill | Brief de campaña con audiencia, mensajes, canales, calendario y métricas | ✅ | 4 |
| `marketing:content-creation` | skill | Contenido por canal (redes, blog, casos, landing) | ✅ | 4 |
| `marketing:draft-content` | skill | Borradores con formato por canal y recomendaciones SEO | ✅ | 1 |
| `marketing:seo-audit` | skill | Auditoría SEO, palabras clave y brechas de contenido | ✅ | 2 |
| `marketing:competitive-brief` | skill | Comparación de posicionamiento y mensajes frente a competidores | ✅ | 2 |
| `marketing:brand-review` | skill | Revisar textos contra la voz de marca y detectar promesas sin respaldo | ✅ | 4 |
| `marketing:email-sequence` | skill | Secuencias de mensajes (onboarding, reenganche, avisos) | ✅ | 3 |
| `marketing:performance-report` | skill | Reporte de resultados por canal con recomendaciones | ✅ | 3 |
<!-- GENERADO:catalogo:fin -->

## 3. Checklist de arranque (Semana 0)

### A. Decisiones que bloquean el Hito 0A

- [x] **P-01 · Infraestructura de producción** (bloquea [HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md)). Apoyo: `deep-research` para
  comparar proveedores y costos; agente `backend-design:boring-tech-advisor`. Decidida: D-19.
- [x] **P-02 · RPO y RTO** ([HU-ARCH-03](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md)). Apoyo: `deep-research` (pgBackRest frente a wal-g). Decidida: D-20.
- [x] **P-03 · Proveedor de suscripción del tenant `solvershub`** ([HU-SH-01](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-01-tenant-reproducible.md)). Recomendado:
  `pack_subscriptions`. Decidida: D-21.
- [x] **P-05 · Modelo por defecto** ([HU-ARCH-10](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md)). Apoyo: `deep-research`; agente `eval-runner` para
  comparar candidatos con el golden set. Decidida: D-22.
- [x] **Decisiones de spec que afectan al 0A** (cada una en el `spec.md` de su spec): D-SPEC-01-1 y
  D-SPEC-01-3, D-SPEC-02-1 y D-SPEC-02-2, D-SPEC-05-1 y D-SPEC-05-2, D-SPEC-06-1 y D-SPEC-06-3,
  D-SPEC-07-1 y D-SPEC-07-2, D-SPEC-09-1 y D-SPEC-09-2, D-SPEC-10-1, D-SPEC-11-1. Apoyo:
  `doc-coauthoring` para afinar cada spec; agente `arquitecto` para validarlas contra los ADR. Las 14 se tomaron el 2026-10-02.
- [x] Registrar cada decisión tomada en [decisiones.md](02-vision-y-decisiones/decisiones.md) y
  marcarla ✅ en su spec. Las demás preguntas (P-04, P-06 a P-10) pueden esperar hasta antes del 0B.

### B. Trámites externos (empiezan el día 1 y corren en paralelo)

- [ ] **Verificación del negocio de Roshi en Meta** (Business Manager). Apoyo: `chrome-browser` o
  `deep-research` para guiar los pasos; las credenciales y los envíos los haces tú.
- [ ] **App Review y `config_id` de Embedded Signup** para operar como Tech Provider ([HU-SH-05](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md)).
  Apoyo: `deep-research` sobre los requisitos vigentes de Meta.
- [ ] **Datos legales, dominio final y correos** (HU-GTM-01). Apoyo: `deep-research`.
- [ ] **Revisión del abogado** con los borradores de contrato, DPA, términos y privacidad (HU-GTM-02).
  Apoyo: `doc-coauthoring`, `docx`.
- [ ] **Infraestructura de producción** contratada según P-01 ([HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md)).
- [ ] **Plantillas de WhatsApp base** enviadas a aprobación: confirmación de demo, recordatorio de demo,
  cargo del período, recordatorio de pago y activación del plan.

### C. Repos, tablero y CI

- [x] Convertir `solvershub-docs` en repo y subirlo a GitHub: `devrochy/solvershub-docs`.
- [x] CI de `solvershub-docs` que corra `python3 herramientas/regenerar.py --check` ([HU-REP-05](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-05-repo-solvershub-docs.md)).
- [ ] Un issue por cada HU de la Ola 1 en su repo dueño (cuerpo = la HU; etiquetas `hito:0A`,
  `ola:1`, `SPEC-XX`) y un GitHub Project para verlos. Herramienta: `gh issue create`; después
  `/work-on-issue #N` para trabajarlos.
- [x] Configurar `GITHUB_PERSONAL_ACCESS_TOKEN` para el MCP de GitHub (decidido el 2026-10-02, ver
  [L1](herramientas/propuestas-de-tooling.md#l1--limpieza)). Verificado el mismo día: el MCP responde.

### D. Skills, hooks y convenciones al día

> Skills, hooks y agentes: backend #171 (2026-10-01). Propuestas decididas el 2026-10-02 e
> implementadas en backend #181, panel #6 y apk #98; el cierre (pre-commit efectivo, `uv.lock`,
> Dependabot con `uv` y skills nuevas conectadas a sus HU) quedó en backend #189 y docs #1.
> Lo que depende de HU futuras (presets, Embedded Signup, `BusinessError`) quedó escrito en cada skill
> como "cuando llegue la HU, actualizar".

- [x] Actualizar `db-migration`: migraciones Alembic (`.py`) del core y de cada pack, `tenant_id` + RLS
  **forzada** + policy con `nullif` + índice compuesto, borrado lógico, tablas de sistema y remisión a
  `backend-design:migration-safety`.
- [x] Actualizar `new-tool`: tools Python en `skills.py` del pack, errores de negocio como resultado y no
  como excepción ([HU-ARCH-18](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-18-errores-de-negocio-no-apagan-packs.md)), montos del servidor, `flow.json`, tests cross-tenant y su eval. El sandbox
  del playground ([HU-ARCH-14](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-14-playground-sandbox.md)) queda como advertencia hasta que exista.
- [x] Actualizar `release`: `ruff`, `pytest` (unitarios e integración), gate de evals, OpenAPI, CHANGELOG,
  PR `develop` → `main`, deploy de producción, tag y rollback. Incluye la alineación de versiones
  (N-38).
- [x] Actualizar `onboard-tenant`: CLI real (`tenant create`/`seed`/`webhook`), `TENANTS_ROOT`, evals en
  `tenants/<slug>/evals/`, BYOK hoy; presets ([HU-FWK-03](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md)) y Embedded Signup quedan anotados para cuando lleguen.
- [x] Actualizar `agentcore-conventions`: sin `apps/` ni TypeScript; los packs se coordinan por
  registros del core.
- [x] Extender `.claude/hooks/guards.py` del backend para exigir `tenant_id`, RLS **forzada** y policy
  también en `alembic/versions/*.py` (core y packs), con tests en `tests/test_guards_hook.py`. El plugin
  de OpenCode ahora le delega la decisión (una sola implementación).
- [x] Corregir `desplegar-test-agent-core`: apuntaba a la app y la BD de **producción**
  (N-37). El hook ahora pide confirmación ante cualquier
  comando que opere sobre los UUID de producción.
- [x] Poner al día los agentes `auditor-multitenant` y `eval-runner` (Python, FORCE, comandos reales), en
  `.claude/agents` y en su par de `.opencode/agents`.
- [x] Mergear la rama `chore/claude-skills-al-dia` (backend #171).
- [x] Decidir las [propuestas de herramientas](herramientas/propuestas-de-tooling.md) (2026-10-02) y
  marcar lo decidido en ese documento.
- [x] Crear la skill `ejecutar-hu` (`.claude/skills/ejecutar-hu` en este repo), que aplica la sección 5 a
  una HU. Siguen opcionales `cerrar-spec` (sección 4) y `cierre-semanal` (sección 8).
- [x] Skills de conocimiento `meta-whatsapp` y `pagos-wompi` (backend #181) y `panel-ui` (panel #6),
  conectadas al campo `skills` de sus HU para que `ejecutar-hu` las cargue.
- [x] Crear `.claude/skills` en `solvershub-panel` con las reglas de `DESIGN.md` y del BFF (skill
  `panel-ui`, panel #6).
- [x] Pasos tuyos (detalle en [propuestas de herramientas](herramientas/propuestas-de-tooling.md#estado-de-implementación-2026-10-02)):
  activar Dependabot en la configuración de los 3 repos, `pre-commit install` en el backend e instalar
  los plugins Security Guidance y context7. Hechos y verificados en uso el 2026-10-02.

### E. Línea base antes de tocar nada

- [ ] Dump manual de la "producción" actual (que vive en la máquina de desarrollo), guardado fuera de
  esa máquina. Es la red de seguridad hasta [HU-ARCH-03](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md).
- [ ] Rotar la credencial del master y revisar el historial de `solvershub-comercial` ([HU-ARCH-04](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-04-endurecer-acceso.md) lo
  formaliza).
- [ ] Correr el golden set del framework y el del tenant `solvershub` y guardar el resultado como línea
  base. Agente: `eval-runner`.
- [ ] Medir una semana de consumo real en `usage_ledger` (tokens por turno, llamadas, caché). Apoyo:
  `data:sql-queries`, `data:analyze`. Alimenta HU-BILL-01.

### F. Arranque formal

- [x] Pasar a "Aprobada" y "Diseño aprobado" las specs con HU de la Ola 1: [SPEC-00](03-fase-0-go-live/SPEC-00-reestructuracion/spec.md), [SPEC-01](03-fase-0-go-live/SPEC-01-produccion-segura/spec.md), [SPEC-02](03-fase-0-go-live/SPEC-02-agente-confiable/spec.md),
  SPEC-06, [SPEC-08](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/spec.md), [SPEC-09](03-fase-0-go-live/SPEC-09-comercio-confiable/spec.md), [SPEC-10](03-fase-0-go-live/SPEC-10-panel-confiable/spec.md) y SPEC-11.
- [ ] Anotar la fecha real de inicio en el calendario.

## 4. Ciclo por spec (SDD)

Para cada spec, en este orden. Si creas la skill `cerrar-spec`, hace este recorrido.

- [ ] **Especificar**: el problema y su evidencia siguen vigentes; vuelve a verificar las `ruta:línea`,
  que cambian rápido. Apoyo: `doc-coauthoring`.
- [ ] **Aclarar**: cada decisión de la spec está ✅. Las que adoptan tecnología nueva pasan por el
  agente `backend-design:boring-tech-advisor`.
- [ ] **Diseñar**: `design.md` al día; ADR escritos con `adr`; diseño revisado por el agente
  `arquitecto`; componentes backend nuevos con `/backend-design:design` o el agente
  `backend-design:component-architect`; escenarios de falla con el agente
  `backend-design:incident-thinker`; UI con `frontend-design` (y `figma-generate-design` si quieres
  iterar en Figma).
- [ ] **Tareas**: orden de `tasks.md` confirmado e issues creados para las HU de la ola actual.
- [ ] **Implementar**: cada HU con el ciclo de la sección 5.
- [ ] **Verificar**: golden sets sin regresión (agente `eval-runner`), aislamiento entre negocios
  (agente `auditor-multitenant`), seguridad (agente `backend-design:security-reviewer`) y métricas de
  éxito de la spec medidas.
- [ ] **Cerrar**: spec en "Verificada"; días reales y factor anotados en el calendario;
  `python3 herramientas/regenerar.py`.

## 5. Ciclo por HU

1. **Lista para empezar (DoR)**
   - [ ] Su spec está en "Diseño aprobado" y no tiene decisiones ❓ que la afecten.
   - [ ] Sus dependencias están terminadas (sección 6).
   - [ ] Existe su issue en el repo dueño.
2. **Arrancar** con `/work-on-issue #N`: crea la rama, analiza el issue y trabaja con TDD.
3. **Diseño corto** (backend) con `backend-design:think-before-coding`; si toca capas o contratos,
   agente `arquitecto`.
4. **Datos**: `db-migration` con `backend-design:migration-safety`; revisión con
   `/backend-design:review-migration` o el agente `backend-design:schema-reviewer`.
5. **Código**: las skills recomendadas de la HU (sección 6) y `agentcore-conventions`; tools nuevas con
   `new-tool`.
6. **Pruebas**: `backend-design:testing-with-discernment`; prueba de aislamiento entre negocios
   siempre; escenarios de conversación con `eval-author`; UI con `built-in-browser`.
7. **Revisión**: `/code-review`; donde hay dinero, seguridad o datos de varios negocios, además
   `/codex:adversarial-review` y el agente `auditor-multitenant`. Si te atascas: `/codex:rescue`.
8. **Desplegar a test** con `desplegar-test-agent-core` (backend) o `desplegar-test` (otros repos) y
   verificar a mano los criterios Gherkin.
9. **Terminada (DoD)**
   - [ ] Criterios Gherkin verificados y evidencia en la HU (PR, tests, captura).
   - [ ] ADR si fue estructural (`adr`); `CHANGELOG`, `ROADMAP` y `BACKLOG` del repo dueño al día.
   - [ ] `estado: terminada` en el frontmatter y `python3 herramientas/regenerar.py`.

## 6. Checklists por hito

Cada línea: casilla (se marca sola con `estado: terminada`), HU, ★ si es camino crítico, título,
tamaño, dependencias y las skills recomendadas para esa HU (campo `skills` de su frontmatter), además de
las comunes del ciclo de la sección 5.

### 6.1 Hito 0A · "SolversHub vende y cobra solo"

**Para empezar**

- [ ] Semana 0 completa (sección 3).

**HU por ola**

<!-- GENERADO:hu-0A:inicio -->
**Ola 1 · Urgente y barato** (12/12 terminadas, 20,5 días-persona sin IA)

- [x] [HU-REP-04](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-04-sin-fugas-de-marca-tecnica.md) ★ Sin marca técnica ante el cliente · S — `backend-design:testing-with-discernment`, `/code-review`, `pagos-wompi`
- [x] [HU-ARCH-05](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-05-webhook-fail-closed.md) ★ Webhook fail-closed sin firma no se procesa · S — `backend-design:security-discipline`, agente `backend-design:security-reviewer`, `backend-design:testing-with-discernment`
- [x] [HU-ARCH-10](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md) ★ Modelos de DeepSeek vigentes y verificados · S — `deep-research`, agente `eval-runner`, agente `optimizer`
- [x] [HU-ARCH-11](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-11-un-mensaje-por-defecto.md) ★ Una burbuja por respuesta por defecto y estilo editable · S — agente `optimizer`, agente `eval-runner`, `frontend-design`
- [x] [HU-ARCH-18](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-18-errores-de-negocio-no-apagan-packs.md) ★ Un error de negocio nunca apaga una habilidad · M — `adr`, `backend-design:error-handling-as-design`, agente `arquitecto`, `/codex:adversarial-review`
- [x] HU-SUB-02 ★ Corregir el pago en línea de cuotas de suscripción en cobranza · S — `db-migration`, `backend-design:migration-safety`, `backend-design:testing-with-discernment`
- [x] [HU-CONN-02](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-02-errores-500-y-bloqueos.md) ★ Errores 500 y bloqueos de Conexiones · S — `backend-design:debugging-discipline`, agente `backend-design:incident-investigator`, `backend-design:testing-with-discernment`
- [x] [HU-COM-01](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md) ★ El dinero del pedido se calcula en el servidor · S — `new-tool`, `backend-design:idempotency-and-side-effects`, `/codex:adversarial-review`, `eval-author`
- [x] [HU-COM-02](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md) ★ Guardrails de montos y de cierre correctos · S — `backend-design:testing-with-discernment`, `eval-author`
- [x] [HU-UI-01](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-01-bugs-visibles.md) ★ Lote de bugs visibles del panel · S — `frontend-design`, `built-in-browser`, `backend-design:auth-and-authorization`, `panel-ui`
- [x] HU-GTM-01 ★ Datos de negocio, dominio y fee de implementación · S — `deep-research`, `docs`
- [x] HU-GTM-05 ★ Claims honestos en landing, playbooks y material comercial · S — `marketing:brand-review`, `marketing:seo-audit`

**Ola 2 · Fundamentos** (8/12 terminadas, 53,5 días-persona sin IA)

- [ ] [HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) ★ Producción fuera de la máquina de desarrollo, con panel y landing · L · depende de HU-GTM-01 — `backend-design:boring-by-default`, agente `backend-design:boring-tech-advisor`, `cloudflare-one`, `deep-research`, `desplegar-test-agent-core`
- [ ] [HU-ARCH-04](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-04-endurecer-acceso.md) ★ Endurecer el acceso al panel, la API y la API de campo · M — `backend-design:auth-and-authorization`, `backend-design:security-discipline`, agente `backend-design:security-reviewer`, `/codex:adversarial-review`
- [x] [HU-ARCH-06](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-06-consumer-y-dlq.md) ★ Consumer con reclamo de pendientes y DLQ alcanzable · M — `backend-design:idempotency-and-side-effects`, `backend-design:error-handling-as-design`, agente `backend-design:incident-thinker`, `backend-design:observability-by-default`
- [x] [HU-ARCH-13](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md) ★ Plantillas de WhatsApp fuera de la ventana de 24 horas · M — `adr`, `backend-design:idempotency-and-side-effects`, `backend-design:error-handling-as-design`, `deep-research`, `meta-whatsapp`
- [x] [HU-FWK-01](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md) ★ Composición correcta de flujos multi-pack · M — `agentcore-conventions`, agente `arquitecto`, agente `eval-runner`, `adr`
- [x] [HU-FWK-02](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-02-adr-presets.md) ★ ADR de presets de agente · S · depende de [HU-FWK-01](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md) — `adr`, `doc-coauthoring`, agente `arquitecto`
- [x] HU-SUB-01 ★ ADR Suscripciones v1 con contrato único y tools del core · M — `adr`, agente `arquitecto`, `new-tool`, `/codex:adversarial-review`
- [x] HU-SUB-03 ★ Eventos de dominio durables con outbox · L — `backend-design:idempotency-and-side-effects`, `adr`, agente `backend-design:incident-thinker`, `backend-design:observability-by-default`, `pagos-wompi`
- [ ] [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md) ★ Resolver de credenciales por conexión con origen guardado · M — `deep-research`, `backend-design:security-discipline`, agente `arquitecto`, `backend-design:testing-with-discernment`, `meta-whatsapp`
- [x] [HU-COM-03](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-03-numeracion-y-datos-por-producto.md) ★ Numeración única y datos del cliente según el tipo de producto · M — `db-migration`, `backend-design:data-modeling-discipline`, `new-tool`
- [x] [HU-UI-02](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) ★ Kit de feedback, confirmaciones y etiquetas legibles · M — `frontend-design`, `built-in-browser`, `panel-ui`
- [ ] HU-GTM-02 ★ Legal v2 revisado por abogado y publicado · M · depende de HU-GTM-01 — `doc-coauthoring`, `docx`, `deep-research`

**Ola 3 · Capacidades** (8/16 terminadas, 64,5 días-persona sin IA)

- [ ] [HU-ARCH-02](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-02-borde-tls-y-webhook-prod.md) ★ Borde TLS y webhook de Meta de producción verificados · S · depende de [HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) — `cloudflare-one`, `cloudflare`, `built-in-browser`, `meta-whatsapp`
- [ ] [HU-ARCH-03](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md) ★ Backups WAL/PITR fuera del sitio y restauración probada · M · depende de [HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) — `deep-research`, agente `backend-design:incident-thinker`, `backend-design:boring-by-default`
- [x] [HU-FWK-03](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md) ★ Registro de presets, seeds por pack y alta sin fallas · M · depende de [HU-FWK-02](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-02-adr-presets.md) — `onboard-tenant`, `new-pack`, `backend-design:idempotency-and-side-effects`, agente `auditor-multitenant`
- [x] HU-SUB-04 ★ Ciclo de vida correcto de la suscripción · M · depende de HU-SUB-01 — `backend-design:think-before-coding`, `backend-design:testing-with-discernment`, `db-migration`, `pagos-wompi`
- [x] HU-SUB-05 ★ Cobro y mora con avisos por plantilla · M · depende de HU-SUB-04, [HU-ARCH-13](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md) — `backend-design:idempotency-and-side-effects`, `eval-author`, `backend-design:observability-by-default`, `meta-whatsapp`, `pagos-wompi`
- [x] HU-SUB-06 ★ Free con prueba y planes pagos desde el primer día · M · depende de HU-SUB-04 — `backend-design:think-before-coding`, `eval-author`, `onboard-tenant`, `pagos-wompi`
- [x] HU-SUB-09 ★ Comercio agnóstico al proveedor de suscripciones · S · depende de HU-SUB-01 — `agentcore-conventions`, `backend-design:testing-with-discernment`
- [x] [HU-SH-01](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-01-tenant-reproducible.md) ★ Tenant solvershub reproducible y coherente · M · depende de [HU-FWK-03](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md), HU-SUB-06 — `onboard-tenant`, agente `customizer`, agente `eval-runner`
- [x] [HU-SH-02](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-02-demo-de-punta-a-punta.md) ★ Demo agendada de punta a punta · L · depende de [HU-ARCH-13](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md) — `new-tool`, `backend-design:idempotency-and-side-effects`, `eval-author`, agente `customizer`
- [ ] [HU-SH-05](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md) ★ Embedded Signup real en el panel nuevo · L · depende de [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md), [HU-CONN-02](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-02-errores-500-y-bloqueos.md) — `deep-research`, `frontend-design`, `built-in-browser`, `backend-design:security-discipline`, `meta-whatsapp`, `panel-ui`
- [ ] [HU-CONN-03](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-03-ciclo-de-vida-seguro.md) ★ Ciclo de vida seguro de las conexiones · M · depende de [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md) — `db-migration`, `backend-design:migration-safety`, agente `auditor-multitenant`, `meta-whatsapp`
- [x] [HU-CONN-04](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-04-diagnostico-confiable.md) ★ Diagnóstico confiable de la conexión · S · depende de [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md) — `backend-design:observability-by-default`, `backend-design:testing-with-discernment`, `meta-whatsapp`
- [ ] [HU-CONN-05](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md) ★ Webhook y secreto por conexión · M · depende de [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md), [HU-ARCH-05](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-05-webhook-fail-closed.md) — `backend-design:security-discipline`, agente `backend-design:security-reviewer`, `cloudflare-one`, `meta-whatsapp`
- [ ] [HU-CONN-06](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-06-byok-produccion.md) ★ BYOK de producción con registro de número y promoción · M · depende de [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md), [HU-CONN-05](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md) — `deep-research`, `frontend-design`, `built-in-browser`, `meta-whatsapp`, `panel-ui`
- [ ] [HU-CONN-07](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-07-checklist-produccion-real.md) ★ Checklist de producción real · M · depende de [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md) — `backend-design:observability-by-default`, `backend-design:performance-and-scaling`, `meta-whatsapp`
- [ ] HU-GTM-03 ★ WhatsApp de Roshi verificado y asistente SolversHub en producción · M · depende de [HU-ARCH-02](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-02-borde-tls-y-webhook-prod.md), HU-GTM-02 — `deep-research`, `chrome-browser`, `meta-whatsapp`

**Ola 4 · Alta automática y cierre** (0/8 terminadas, 48,0 días-persona sin IA)

- [ ] [HU-ARCH-28](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) ★ Evals de consistencia: usuario simulado, aserciones de estado y pass^k · L · depende de HU-SUB-12 — `eval-author`, agente `eval-runner`, `backend-design:testing-with-discernment`, `db-migration`
- [ ] [HU-ARCH-29](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md) Verificador de afirmaciones con modelo de evidencia · M · depende de [HU-COM-02](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md) — `agentcore-conventions`, `backend-design:testing-with-discernment`, `eval-author`
- [ ] HU-SUB-12 ★ Golden set y journeys E2E multi-turno de suscripciones · M · depende de HU-SUB-05, HU-SUB-06, HU-SUB-09, [HU-COM-01](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md) — `eval-author`, agente `eval-runner`, `backend-design:testing-with-discernment`
- [ ] [HU-SH-03](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md) ★ Identidad de servicio y aprovisionamiento automático de negocios · L · depende de HU-SUB-03, [HU-FWK-03](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md) — `adr`, `backend-design:auth-and-authorization`, agente `backend-design:security-reviewer`, `backend-design:idempotency-and-side-effects`, `/codex:adversarial-review`
- [ ] [HU-SH-04](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md) ★ Cobro de plataforma por dos canales con fuente única · L · depende de [HU-SH-03](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md), HU-SUB-05 — `adr`, `backend-design:idempotency-and-side-effects`, agente `backend-design:incident-thinker`, `data:validate-data`, `pagos-wompi`
- [ ] [HU-SH-06](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md) ★ Onboarding autoservicio desde la invitación hasta el primer mensaje · L · depende de [HU-SH-03](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md), [HU-UI-02](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) — `frontend-design`, `built-in-browser`, `marketing:email-sequence`, `panel-ui`
- [ ] [HU-SH-07](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-07-antiabuso-y-cumplimiento.md) ★ Antiabuso y cumplimiento del alta automática · M · depende de [HU-SH-03](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md), HU-GTM-02 — `backend-design:security-discipline`, `turnstile-spin`, `doc-coauthoring`
- [ ] [HU-SH-08](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md) ★ Golden set E2E del asistente SolversHub y canary · M · depende de [HU-SH-01](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-01-tenant-reproducible.md), [HU-SH-02](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-02-demo-de-punta-a-punta.md), HU-SUB-12, [HU-ARCH-28](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) — `eval-author`, agente `eval-runner`
<!-- GENERADO:hu-0A:fin -->

**Para cerrar el 0A** (criterio de salida)

- [ ] Un prospecto real agenda una demo con el asistente de SolversHub.
- [ ] Compra un plan y paga el primer período (o confirma Free, sin cobro).
- [ ] Su negocio se crea solo, con plan, preset e invitación recibida.
- [ ] Conecta su WhatsApp por Embedded Signup (o por BYOK de producción si Meta aún no aprobó, anotado
  como desvío).
- [ ] Al final del período recibe el cobro siguiente con aviso por plantilla y con el proveedor elegido.
- [ ] Todo lo anterior sin intervención humana y con evidencia auditada (capturas, `audit_log`,
  eventos).
- [ ] Golden E2E del asistente ≥95 % durante 3 noches.
- [ ] Producción fuera de la máquina de desarrollo y restauración probada con evidencia.
- [ ] Ningún defecto 🔴 abierto en suscripciones, comercio o Conexiones.
- [ ] Retro del 0A: factor real, desvíos y ajustes al 0B anotados.

### 6.2 Hito 0B · "Go-live amplio"

**Para empezar**

- [ ] Hito 0A cerrado.
- [ ] Decididas P-04 (precios), P-06 (colchón de gracia), P-07 (recargas), P-08 (WhatsApp Web) y P-10
  (asistentes por negocio).
- [ ] Decisiones de spec del 0B tomadas: D-SPEC-00-1 a D-SPEC-00-3, D-SPEC-01-2, D-SPEC-02-3,
  D-SPEC-03-1 y D-SPEC-03-2, D-SPEC-04-1 a D-SPEC-04-3, D-SPEC-06-2, D-SPEC-08-1 y D-SPEC-08-2.
- [ ] SPEC-03 y [SPEC-04](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/spec.md) en "Diseño aprobado".

**HU por spec**

<!-- GENERADO:hu-0B:inicio -->
**[SPEC-00](03-fase-0-go-live/SPEC-00-reestructuracion/spec.md)** · reestructuracion (1/5)

- [ ] [HU-REP-01](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-01-limpiar-residuos.md) Limpiar residuos de la reestructura · S — `/code-review`, `desplegar-test-agent-core`
- [ ] [HU-REP-02](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-02-renombre-cosmetico.md) Renombre cosmético a solvershub-core y documentación correcta · M · depende de [HU-REP-01](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-01-limpiar-residuos.md) — `cloudflare`, `desplegar-test-agent-core`, `doc-coauthoring`
- [ ] [HU-REP-03](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-03-transicion-de-identificadores.md) Transición de identificadores rompedores con alias y ADR · M · depende de [HU-REP-02](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-02-renombre-cosmetico.md) — `adr`, agente `arquitecto`, `/codex:adversarial-review`, `release`
- [x] [HU-REP-05](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-05-repo-solvershub-docs.md) Repo solvershub-docs con CI y regla un tema, un dueño · S — `doc-coauthoring`, `/code-review`
- [ ] [HU-REP-06](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-06-solvershub-infra.md) ★ solvershub-infra versionado como base de recuperación ante desastres · M — `cloudflare-one`, `cloudflare`, `backend-design:boring-by-default`, `doc-coauthoring`

**[SPEC-01](03-fase-0-go-live/SPEC-01-produccion-segura/spec.md)** · produccion segura (0/3)

- [ ] [HU-ARCH-07](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md) ★ Observabilidad de producción con alertas · M · depende de [HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) — `backend-design:observability-by-default`, `kpi-dashboard-design`, `incident`
- [ ] [HU-ARCH-08](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-08-apk-a-produccion.md) ★ APK de cobranza lista para producción · M · depende de [HU-ARCH-02](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-02-borde-tls-y-webhook-prod.md) — `backend-design:security-discipline`, agente `backend-design:security-reviewer`, `/code-review`
- [ ] [HU-ARCH-09](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-09-release-y-e2e-entre-repos.md) Release y pruebas E2E entre repos antes de promover a producción · M · depende de [HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) — `built-in-browser`, `backend-design:testing-with-discernment`, `desplegar-test-agent-core`

**[SPEC-02](03-fase-0-go-live/SPEC-02-agente-confiable/spec.md)** · agente confiable (0/5)

- [ ] [HU-ARCH-12](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md) ★ Precondiciones terminales, señal escalate y scopes en tools de pago · M — `new-tool`, `backend-design:error-handling-as-design`, `adr`, `eval-author`
- [ ] [HU-ARCH-14](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-14-playground-sandbox.md) Probar asistente sin efectos reales · M — `new-tool`, `backend-design:testing-with-discernment`, agente `arquitecto`
- [ ] [HU-ARCH-15](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-15-cache-anthropic.md) Caché de Anthropic con como máximo 4 breakpoints · S — `claude-api`, agente `optimizer`
- [ ] [HU-ARCH-16](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-16-golden-set-comercio.md) ★ Golden set y journeys multi-turno de comercio · L · depende de [HU-COM-01](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md), [HU-COM-02](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md), [HU-FWK-01](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md), HU-SUB-12 — `eval-author`, agente `eval-runner`
- [ ] [HU-ARCH-17](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-17-golden-set-cobranza.md) ★ Golden set de cobranza · L · depende de [HU-ARCH-13](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md), [HU-FWK-01](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md), HU-SUB-12 — `eval-author`, agente `eval-runner`

**SPEC-03** · billing creditos (0/8)

- [ ] HU-BILL-01 ★ Calibración del consumo real y precios vigentes de proveedores · S · depende de [HU-ARCH-10](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md) — `data:sql-queries`, `data:analyze`, `deep-research`, `claude-api`, `meta-whatsapp`
- [ ] HU-BILL-02 ★ ADR Billing v2 por créditos · M · depende de HU-BILL-01 — `adr`, `doc-coauthoring`, agente `arquitecto`
- [ ] HU-BILL-03 ★ Tarifario versionado con ciclo de vida de modelos y costeo exacto · M · depende de HU-BILL-02 — `db-migration`, `backend-design:data-modeling-discipline`, agente `backend-design:schema-reviewer`, `claude-api`
- [ ] HU-BILL-04 ★ Ledger multi-concepto con créditos inmutables e idempotencia · M · depende de HU-BILL-03 — `db-migration`, `backend-design:idempotency-and-side-effects`, agente `backend-design:schema-reviewer`, agente `auditor-multitenant`
- [ ] HU-BILL-05 ★ Planes v2 con créditos y límites estructurales · M · depende de HU-BILL-02, HU-BILL-04 — `db-migration`, `backend-design:migration-safety`, agente `backend-design:schema-reviewer`
- [ ] HU-BILL-06 ★ Enforcement de créditos y límites con colchón de gracia · L · depende de HU-BILL-05 — `backend-design:error-handling-as-design`, `backend-design:query-discipline`, `backend-design:testing-with-discernment`, agente `auditor-multitenant`
- [ ] HU-BILL-07 ★ Panel Plan y créditos con saldo, proyección y desglose · M · depende de HU-BILL-06 — `frontend-design`, `kpi-dashboard-design`, `built-in-browser`, `panel-ui`
- [ ] HU-BILL-08 ★ Página de precios v2 alimentada por el core · M · depende de HU-BILL-05 — `frontend-design`, `web-perf`, `marketing:brand-review`

**[SPEC-04](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/spec.md)** · notas de voz y comprobantes (0/6)

- [ ] [HU-MEDIA-01](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-01-adr-media.md) ★ ADR de procesamiento de media en el core · S — `adr`, agente `arquitecto`, `deep-research`
- [ ] [HU-MEDIA-02](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md) ★ Descarga y almacenamiento de media entrante · M · depende de [HU-MEDIA-01](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-01-adr-media.md) — `db-migration`, `backend-design:idempotency-and-side-effects`, agente `auditor-multitenant`, `backend-design:security-discipline`
- [ ] [HU-MEDIA-03](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md) ★ Notas de voz a texto con llave híbrida · M · depende de [HU-MEDIA-02](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md), HU-BILL-04 — `backend-design:error-handling-as-design`, `deep-research`, agente `optimizer`, `eval-author`
- [ ] [HU-MEDIA-04](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md) ★ Dispatcher de visión con prueba de conexión y benchmark · M · depende de [HU-MEDIA-02](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md), HU-BILL-04 — `claude-api`, `data:statistical-analysis`, agente `optimizer`
- [ ] [HU-MEDIA-05](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-05-ocr-comprobantes.md) ★ OCR de comprobantes en la ruta financiera · L · depende de [HU-MEDIA-04](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md), [HU-COM-06](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-06-operacion-de-pagos.md) — `backend-design:idempotency-and-side-effects`, `backend-design:security-discipline`, `eval-author`, `/codex:adversarial-review`
- [ ] [HU-MEDIA-06](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-06-clasificacion-de-imagenes.md) Clasificación de imágenes y descripción de producto · M · depende de [HU-MEDIA-04](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md) — `eval-author`, agente `optimizer`

**SPEC-06** · planes y suscripciones (1/8)

- [x] HU-SUB-07 ★ Cambio de plan e idempotencia por pedido · M · depende de HU-SUB-04 — `backend-design:data-modeling-discipline`, `db-migration`, `new-tool`, `pagos-wompi`
- [ ] HU-SUB-08 ★ Administración de suscripciones en API y panel · M · depende de HU-SUB-01 — `frontend-design`, `backend-design:auth-and-authorization`, `backend-design:query-discipline`, `pagos-wompi`, `panel-ui`
- [ ] HU-SUB-10 Recurrencia de planes editable en API, panel y CSV · M · depende de HU-SUB-01 — `frontend-design`, `db-migration`, `backend-design:data-modeling-discipline`, `panel-ui`
- [ ] HU-SUB-11 Seeds por pack y preset Planes y suscripciones · M · depende de [HU-FWK-03](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md), HU-SUB-06 — `new-pack`, `onboard-tenant`, `eval-author`
- [ ] HU-SUB-13 Cobros por debajo del mínimo de Wompi · M · depende de HU-SUB-04, [HU-MEDIA-05](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-05-ocr-comprobantes.md) — `backend-design:error-handling-as-design`, `eval-author`, `pagos-wompi`
- [ ] HU-SUB-14 Acciones post-activación configurables · M · depende de HU-SUB-03 — `backend-design:idempotency-and-side-effects`, `backend-design:security-discipline`, agente `backend-design:security-reviewer`
- [ ] HU-SUB-15 Cobranza como segundo proveedor del contrato de suscripción · L · depende de HU-SUB-01, HU-SUB-02, HU-SUB-04 — `db-migration`, `backend-design:migration-safety`, `adr`, agente `auditor-multitenant`, `pagos-wompi`
- [ ] HU-SUB-18 Avisos de cobro en horario legal · S · depende de HU-SUB-05 — `pagos-wompi`, `agentcore-conventions`, `deep-research`

**[SPEC-07](03-fase-0-go-live/SPEC-07-asistente-solvershub/spec.md)** · asistente solvershub (0/1)

- [ ] [HU-SH-09](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-09-landing-con-atribucion.md) De la landing al asistente con atribución · S · depende de [HU-SH-01](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-01-tenant-reproducible.md) — `backend-design:data-modeling-discipline`, `marketing:performance-report`

**[SPEC-08](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/spec.md)** · conexion whatsapp meta (0/3)

- [ ] [HU-CONN-08](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md) Lista de conexiones v2 y hub de WhatsApp-Meta · L · depende de [HU-CONN-03](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-03-ciclo-de-vida-seguro.md), [HU-CONN-04](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-04-diagnostico-confiable.md), [HU-SH-05](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md), [HU-UI-02](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) — `frontend-design`, `built-in-browser`, `figma-design-to-code`, `meta-whatsapp`, `panel-ui`
- [ ] [HU-CONN-09](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-09-costos-meta-verificables.md) Costos de Meta verificables y opcionales por conexión · M · depende de [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md), [HU-CONN-08](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md) — `data:sql-queries`, `kpi-dashboard-design`, `frontend-design`, `meta-whatsapp`, `panel-ui`
- [ ] [HU-CONN-10](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-10-conexiones-no-meta.md) Arreglos de conexiones que no son de Meta · S — `backend-design:debugging-discipline`, `built-in-browser`

**[SPEC-09](03-fase-0-go-live/SPEC-09-comercio-confiable/spec.md)** · comercio confiable (0/6)

- [ ] [HU-COM-04](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) Barrido de defectos de comercio D5 a D16 y D18 · M · depende de [HU-COM-01](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md) — `backend-design:query-discipline`, `/backend-design:hunt-n-plus-one`, `backend-design:testing-with-discernment`
- [ ] [HU-COM-05](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md) Máquina de estados del pedido con avisos y eventos · M · depende de [HU-ARCH-13](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md), HU-SUB-03, [HU-COM-04](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) — `backend-design:data-modeling-discipline`, `backend-design:idempotency-and-side-effects`, `db-migration`
- [ ] [HU-COM-06](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-06-operacion-de-pagos.md) Operación de pagos manuales y comprobantes · M · depende de [HU-COM-05](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md) — `backend-design:auth-and-authorization`, `frontend-design`, `pagos-wompi`, `panel-ui`
- [ ] [HU-COM-07](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-07-catalogo-menus-y-retail.md) Catálogo para menús y retail · M · depende de [HU-COM-04](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) — `db-migration`, `frontend-design`, `xlsx`, `panel-ui`
- [ ] [HU-COM-08](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-08-domicilios.md) Domicilios con tarifa, zonas, mínimo y horario de pedidos · M · depende de [HU-COM-03](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-03-numeracion-y-datos-por-producto.md), [HU-COM-07](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-07-catalogo-menus-y-retail.md) — `backend-design:data-modeling-discipline`, `new-tool`
- [ ] [HU-COM-09](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-09-modificar-pedido.md) Tools para cancelar y modificar un pedido · M · depende de [HU-COM-05](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md) — `new-tool`, `eval-author`

**[SPEC-10](03-fase-0-go-live/SPEC-10-panel-confiable/spec.md)** · panel confiable (1/2)

- [x] [HU-UI-03](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md) Shell del panel responsive y accesible · M · depende de [HU-UI-02](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) — `frontend-design`, `web-perf`, `built-in-browser`, `panel-ui`
- [ ] [HU-UI-04](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md) Calidad del panel con tests en CI y control de deriva de la API · M — `backend-design:testing-with-discernment`, `built-in-browser`, `web-perf`, `panel-ui`

**SPEC-11** · lanzamiento comercial legal (0/2)

- [ ] HU-GTM-04 Kit comercial v2 coherente con créditos y D-16 · S · depende de HU-BILL-05, HU-GTM-05 — `pptx`, `xlsx`, `marketing:content-creation`
- [ ] HU-GTM-06 ★ Primer cliente de pago por vertical en producción · M · depende de [HU-ARCH-07](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md), [HU-ARCH-08](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-08-apk-a-produccion.md), [HU-ARCH-16](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-16-golden-set-comercio.md), [HU-ARCH-17](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-17-golden-set-cobranza.md), HU-BILL-06, [HU-MEDIA-05](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-05-ocr-comprobantes.md), [HU-COM-06](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-06-operacion-de-pagos.md), HU-SUB-15 — `marketing:campaign-plan`, `onboard-tenant`, `data:analyze`
<!-- GENERADO:hu-0B:fin -->

**Para cerrar el 0B** (y con él la Fase 0)

- [ ] 1 cliente de pago de comercio y 1 de cobranza en producción.
- [ ] Alta en menos de 1 día, medida.
- [ ] Créditos descontando y bloqueando de forma auditable.
- [ ] Notas de voz y comprobantes procesados en producción.
- [ ] Golden sets por vertical ≥95 % durante 3 noches.
- [ ] Retro de la Fase 0.

### 6.3 Fase 1 · "Competir"

**Para empezar**

- [ ] Fase 0 cerrada.
- [ ] P-09 decidida y decisiones de [SPEC-12](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md) a [SPEC-20](04-fase-1-competir/SPEC-20-crecimiento/spec.md) tomadas.
- [ ] Orden de las specs ajustado con lo que pidieron los primeros clientes.

<!-- GENERADO:hu-1:inicio -->
**[SPEC-12](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md)** · arquitectura de informacion (2/10)

- [x] [HU-UX-01](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-01-adr-arquitectura-de-informacion.md) ADR de arquitectura de información y glosario del panel · S — `adr`, `doc-coauthoring`, `figma-generate-diagram`, `panel-ui`
- [ ] [HU-UX-02](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) Menú v2 agrupado por tarea con renombres · M · depende de [HU-UX-01](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-01-adr-arquitectura-de-informacion.md) — `frontend-design`, `built-in-browser`, `panel-ui`
- [x] [HU-UX-03](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-03-ayuda-contextual.md) Ayuda contextual y lenguaje claro · M · depende de [HU-UX-01](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-01-adr-arquitectura-de-informacion.md) — `frontend-design`, `marketing:brand-review`, `panel-ui`
- [ ] [HU-UX-04](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-04-estados-vacios-y-permisos.md) Estados vacíos con acción y permisos coherentes · M · depende de [HU-UX-02](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) — `frontend-design`, `backend-design:auth-and-authorization`, `panel-ui`
- [ ] [HU-UX-05](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-05-guias-por-habilidad.md) Guías por habilidad y por preset · M · depende de [HU-SH-06](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md), [HU-FWK-04](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md) — `frontend-design`, `new-pack`, `panel-ui`
- [ ] [HU-UX-06](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-06-registro-desde-landing.md) Registro directo desde la landing · M · depende de [HU-SH-03](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md), [HU-SH-07](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-07-antiabuso-y-cumplimiento.md) — `turnstile-spin`, `frontend-design`, `backend-design:security-discipline`
- [ ] [HU-UX-08](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-08-agenda-unificada.md) Agenda unificada con calendario, tipos de cita y horario · M · depende de [HU-UX-02](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md), [HU-CAL-01](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-01-bloqueos-de-agenda.md), [HU-CAL-03](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-03-calendario-visual.md) — `frontend-design`, `panel-ui`, `built-in-browser`, `backend-design:migration-safety`
- [ ] [HU-UX-09](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-09-ficha-de-conexion-por-tipo.md) Ficha de conexión por tipo enlazada con los agentes · L · depende de [HU-UX-02](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md), [HU-AOS-23](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md), [HU-AOS-47](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md) — `frontend-design`, `panel-ui`, `built-in-browser`, `meta-whatsapp`
- [ ] [HU-UX-10](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-10-cobranza-y-ventas-en-pestanas.md) Cobranza y Ventas como una entrada con pestañas · M · depende de [HU-UX-02](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) — `frontend-design`, `panel-ui`, `built-in-browser`, `dataviz`
- [ ] [HU-UX-11](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md) Cajón del panel en la app alineado con el menú v2 · S · depende de [HU-UX-02](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md), [HU-DS-11](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-11-shell-del-panel-en-la-app.md) — `frontend-design`, `built-in-browser`

**[SPEC-13](04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md)** · vistas profesionales (0/0 · 10 parqueadas)


- [ ] [HU-MEDIA-07](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-MEDIA-07-visor-de-media.md) ⏸️ parqueada Visor de media y transcripciones en la bandeja · M · depende de [HU-UI-06](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-06-bandeja-dos-paneles.md), [HU-MEDIA-03](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md), [HU-MEDIA-04](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md) — `frontend-design`, `backend-design:security-discipline`
- [ ] [HU-UI-05](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-05-tickets-reales.md) ⏸️ parqueada Tickets reales en Por atender · M · depende de [HU-UI-02](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) — `frontend-design`, `backend-design:auth-and-authorization`, `db-migration`, `panel-ui`
- [ ] [HU-UI-06](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-06-bandeja-dos-paneles.md) ⏸️ parqueada Bandeja de conversaciones de dos paneles · L · depende de [HU-UI-05](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-05-tickets-reales.md), [HU-ARCH-13](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md) — `frontend-design`, `figma-design-to-code`, `built-in-browser`, `web-perf`, `panel-ui`
- [ ] [HU-UI-07](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) ⏸️ parqueada Dashboard con período, tendencias y calidad · M · depende de [HU-UI-03](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md) — `kpi-dashboard-design`, `frontend-design`, `data:sql-queries`, `panel-ui`
- [ ] [HU-UI-08](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md) ⏸️ parqueada FilterBar único y tablas densas · M · depende de [HU-UI-03](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md), [HU-DS-03](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-03-kit-de-componentes-panel.md) — `frontend-design`, `backend-design:query-discipline`, `panel-ui`
- [ ] [HU-UI-09](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-09-configuracion-por-pestanas.md) ⏸️ parqueada Configuración por pestañas con estado y controles claros · M · depende de [HU-UI-02](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) — `frontend-design`, `built-in-browser`, `panel-ui`
- [ ] [HU-UI-10](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-10-colaboradores-y-permisos.md) ⏸️ parqueada Colaboradores con grilla de permisos e invitaciones · M · depende de [HU-UI-02](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) — `frontend-design`, `backend-design:auth-and-authorization`, agente `backend-design:security-reviewer`, `panel-ui`
- [ ] [HU-UI-11](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-11-clientes-y-leads.md) ⏸️ parqueada Clientes con filtros, exportación y detalle · M · depende de [HU-UI-08](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md) — `frontend-design`, `backend-design:query-discipline`, `backend-design:security-discipline`, `panel-ui`
- [ ] [HU-UI-12](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-12-packs-costos-y-plan-compactos.md) ⏸️ parqueada Páginas de packs, Consumo y Plan compactas · M · depende de [HU-UI-08](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md), HU-BILL-07 — `frontend-design`, `kpi-dashboard-design`, `panel-ui`
- [ ] [HU-UI-13](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-13-cuenta-y-notificaciones.md) ⏸️ parqueada Cuenta, recuperación de contraseña y notificaciones a operadores · L · depende de [HU-UI-03](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md) — `backend-design:auth-and-authorization`, agente `backend-design:security-reviewer`, `frontend-design`, `panel-ui`

**[SPEC-14](04-fase-1-competir/SPEC-14-billing-extras/spec.md)** · billing extras (0/1 · 3 parqueadas)

- [ ] [HU-BILL-12](04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-12-cambio-de-plan-y-anual.md) Cambio de plan de plataforma con prorrateo y ciclo anual · M · depende de [HU-SH-04](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md), HU-BILL-05 — `backend-design:think-before-coding`, `backend-design:testing-with-discernment`, `pagos-wompi`

- [ ] [HU-BILL-09](04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-09-avisos-de-consumo.md) ⏸️ parqueada Avisos de consumo fuera del panel · S · depende de HU-BILL-06, [HU-ARCH-13](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md) — `marketing:email-sequence`, `backend-design:idempotency-and-side-effects`
- [ ] [HU-BILL-10](04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-10-recargas.md) ⏸️ parqueada Recargas de créditos y cierres de período · M · depende de HU-BILL-06 — `db-migration`, `backend-design:idempotency-and-side-effects`, `/codex:adversarial-review`, `pagos-wompi`
- [ ] [HU-BILL-11](04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-11-margen-master.md) ⏸️ parqueada Vista de margen para la plataforma · M · depende de HU-BILL-04 — `kpi-dashboard-design`, `data:sql-queries`, `data:validate-data`, `panel-ui`

**[SPEC-15](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md)** · editor visual de flujo (0/0 · 6 parqueadas)


- [ ] [HU-FLOW-01](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-01-adr-editor-de-flujo.md) ⏸️ parqueada ADR del editor visual de flujo · S · depende de [HU-FWK-01](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md) — `adr`, agente `arquitecto`, `doc-coauthoring`
- [ ] [HU-FLOW-02](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-02-flujo-en-agentspec.md) ⏸️ parqueada Flujo versionado dentro del AgentSpec · M · depende de [HU-FLOW-01](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-01-adr-editor-de-flujo.md) — `db-migration`, `backend-design:migration-safety`, agente `eval-runner`
- [ ] [HU-FLOW-03](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-03-validador-y-api.md) ⏸️ parqueada Esquema, validador único, API y catálogo de acciones del flujo · M · depende de [HU-FLOW-02](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-02-flujo-en-agentspec.md) — `backend-design:error-handling-as-design`, `backend-design:testing-with-discernment`
- [ ] [HU-FLOW-04](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-04-editor-visual.md) ⏸️ parqueada Editor visual del flujo con arrastrar y soltar accesible · L · depende de [HU-FLOW-03](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-03-validador-y-api.md), [HU-UI-03](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md) — `frontend-design`, `figma-design-to-code`, `built-in-browser`, `panel-ui`
- [ ] [HU-FLOW-05](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-05-borrador-y-publicacion.md) ⏸️ parqueada Probar el borrador, publicar y revertir · M · depende de [HU-FLOW-04](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-04-editor-visual.md), [HU-ARCH-14](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-14-playground-sandbox.md) — agente `eval-runner`, `backend-design:testing-with-discernment`
- [ ] [HU-FLOW-06](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-06-flujo-semilla-por-preset.md) ⏸️ parqueada Flujo semilla por preset con diff al aplicar · S · depende de [HU-FLOW-02](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-02-flujo-en-agentspec.md), [HU-FWK-10](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-10-aplicar-preset-desde-panel.md) — `new-pack`, agente `eval-runner`

**[SPEC-16](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/spec.md)** · habilidades como plataforma (2/8)

- [x] [HU-FWK-04](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md) Catálogo de habilidades con metadatos · M — `new-pack`, `agentcore-conventions`
- [ ] [HU-FWK-05](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-05-manifiesto-de-menu.md) Menú del panel desde un manifiesto del backend · S · depende de [HU-FWK-04](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md), [HU-UX-01](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-01-adr-arquitectura-de-informacion.md) — `frontend-design`, `backend-design:auth-and-authorization`
- [ ] [HU-FWK-06](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-06-descriptores-y-api-de-vistas.md) Descriptores enriquecidos y API de vistas de packs · M · depende de [HU-FWK-05](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-05-manifiesto-de-menu.md) — `adr`, agente `arquitecto`, `backend-design:testing-with-discernment`
- [ ] [HU-FWK-07](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-07-descriptor-view.md) Componente genérico DescriptorView y migración de pantallas · M · depende de [HU-FWK-06](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-06-descriptores-y-api-de-vistas.md), [HU-UI-08](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md) — `frontend-design`, `backend-design:testing-with-discernment`
- [x] [HU-FWK-08](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-08-formulario-de-schema-v2.md) Formulario de configuración por schema v2 · M · depende de [HU-UI-01](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-01-bugs-visibles.md) — `frontend-design`, `built-in-browser`
- [ ] [HU-FWK-09](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-09-tools-declarativas-panel.md) Acciones personalizadas (tools declarativas) en el panel nuevo · M · depende de [HU-FWK-08](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-08-formulario-de-schema-v2.md) — `new-tool`, `backend-design:security-discipline`, agente `backend-design:security-reviewer`
- [ ] [HU-FWK-10](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-10-aplicar-preset-desde-panel.md) Aplicar un preset desde el panel con diff · M · depende de [HU-FWK-03](03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md), [HU-FWK-04](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md) — `onboard-tenant`, `frontend-design`
- [ ] [HU-FWK-11](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-11-presets-adicionales.md) Presets adicionales de agendamiento, marketing y atención · M · depende de [HU-FWK-10](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-10-aplicar-preset-desde-panel.md) — `new-pack`, `eval-author`, agente `customizer`

**[SPEC-17](04-fase-1-competir/SPEC-17-canales-y-campanas/spec.md)** · canales y campanas (1/3)

- [ ] [HU-CHAN-01](04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-01-instagram-y-messenger.md) Instagram y Messenger con salida · L · depende de [HU-CONN-08](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md) — `deep-research`, `new-tool`, `backend-design:security-discipline`, `meta-whatsapp`
- [x] [HU-CHAN-02](04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-02-chat-web.md) Chat web embebible · L — `turnstile-spin`, `frontend-design`, agente `backend-design:security-reviewer`
- [ ] [HU-CHAN-03](04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-03-pack-marketing.md) Pack de marketing con campañas, segmentos y consentimiento · L · depende de [HU-ARCH-13](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md), HU-BILL-06 — `new-pack`, agente `plugin-dev`, `marketing:campaign-plan`, `meta-whatsapp`

**[SPEC-18](04-fase-1-competir/SPEC-18-pack-commerce-v2/spec.md)** · pack commerce v2 (0/0 · 6 parqueadas)


- [ ] [HU-COM-10](04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-10-proactividad-v2.md) ⏸️ parqueada Proactividad de ventas v2 · M · depende de [HU-COM-05](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md), [HU-ARCH-13](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md) — `backend-design:idempotency-and-side-effects`, `marketing:email-sequence`, `eval-author`
- [ ] [HU-COM-11](04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-11-promociones-v2.md) ⏸️ parqueada Promociones v2 con horarios, cupones y domicilio gratis · M · depende de [HU-COM-04](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md) — `backend-design:data-modeling-discipline`, `db-migration`
- [ ] [HU-COM-12](04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-12-kpis-de-ventas.md) ⏸️ parqueada KPIs de ventas y reporte periódico al equipo · M · depende de [HU-COM-05](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md) — `kpi-dashboard-design`, `data:sql-queries`
- [ ] [HU-COM-13](04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-13-busqueda-y-recomendaciones.md) ⏸️ parqueada Búsqueda tolerante y recomendaciones comprados juntos · M · depende de [HU-COM-07](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-07-catalogo-menus-y-retail.md) — `backend-design:query-discipline`, `/backend-design:explain-this-query`
- [ ] [HU-COM-14](04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-14-lead-y-pedido.md) ⏸️ parqueada Vínculo entre lead y pedido · S · depende de [HU-COM-05](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md) — `backend-design:data-modeling-discipline`
- [ ] [HU-COM-15](04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-15-modificadores-y-combos.md) ⏸️ parqueada Modificadores y combos para menús · L · depende de [HU-COM-07](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-07-catalogo-menus-y-retail.md) — `db-migration`, `backend-design:data-modeling-discipline`, `eval-author`

**[SPEC-19](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/spec.md)** · extensibilidad y operacion (2/8)

- [ ] [HU-ARCH-19](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md) MCP por tenant con allowlist y circuit breaker · L · depende de [HU-ARCH-12](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md) — `adr`, `backend-design:security-discipline`, agente `backend-design:security-reviewer`, agente `backend-design:boring-tech-advisor`
- [ ] [HU-ARCH-20](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-20-guardrails-runtime.md) Guardrails de runtime completos · M · depende de [HU-ARCH-12](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md) — `backend-design:security-discipline`, agente `backend-design:incident-thinker`
- [ ] [HU-ARCH-21](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-21-status-page-y-slos.md) Status page pública y SLO medidos · M · depende de [HU-ARCH-07](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md) — `backend-design:observability-by-default`, `kpi-dashboard-design`
- [ ] [HU-ARCH-22](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-22-pentest.md) Pentest externo y cuestionario de seguridad enterprise · M · depende de [HU-ARCH-04](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-04-endurecer-acceso.md), [HU-ARCH-05](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-05-webhook-fail-closed.md) — agente `backend-design:security-reviewer`, agente `auditor-multitenant`, `deep-research`
- [ ] [HU-ARCH-23](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-23-higiene.md) Higiene de repos, migraciones y documentación · M · depende de [HU-REP-01](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-01-limpiar-residuos.md) — `/code-review`, `agentcore-conventions`
- [x] [HU-ARCH-24](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-24-contenedor-y-tipos.md) Contenedor no-root, mypy gradual y embeddings configurables · M — `backend-design:security-discipline`, `release`
- [x] [HU-ARCH-27](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-27-turnos-timeout-y-observabilidad.md) Turnos con timeout, cupo justo y observabilidad · M · depende de [HU-ARCH-06](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-06-consumer-y-dlq.md) — `backend-design:error-handling-as-design`, `backend-design:performance-and-scaling`, `backend-design:observability-by-default`
- [ ] [HU-REP-07](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-REP-07-solvershub-brand.md) Repo solvershub-brand con tokens publicados · M · depende de [HU-REP-02](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-02-renombre-cosmetico.md) — `frontend-design`, `figma-generate-library`, `theme-factory`

**[SPEC-20](04-fase-1-competir/SPEC-20-crecimiento/spec.md)** · crecimiento (2/6)

- [ ] [HU-GTM-07](04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-07-redes-activas.md) Redes activas con calendario editorial · M · depende de HU-GTM-06 — `marketing:campaign-plan`, `marketing:content-creation`, `canvas-design`
- [ ] [HU-GTM-08](04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-08-activos-de-venta.md) Activos de venta con casos reales · M · depende de HU-GTM-06 — `pptx`, `pdf`, `marketing:content-creation`
- [ ] [HU-GTM-09](04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-09-leads-con-sla.md) Leads atendidos en menos de 5 minutos con pipeline · S · depende de [HU-SH-09](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-09-landing-con-atribucion.md) — `marketing:performance-report`, `data:analyze`
- [x] [HU-GTM-10](04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-10-paginas-de-integraciones-y-seo.md) Páginas de integraciones, casos de uso y SEO por vertical · M · depende de HU-GTM-05 — `marketing:seo-audit`, `marketing:draft-content`, `frontend-design`, `web-perf`
- [x] [HU-GTM-11](04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-11-matriz-corregida.md) Matriz competitiva corregida y mantenida · S — `xlsx`, `marketing:competitive-brief`, `deep-research`
- [ ] [HU-SUB-16](04-fase-1-competir/SPEC-20-crecimiento/hu/HU-SUB-16-mrr-y-embudo.md) MRR, churn y embudo para negocios con suscripciones · M · depende de HU-SUB-08, HU-SUB-15 — `kpi-dashboard-design`, `data:sql-queries`, `data:statistical-analysis`, `panel-ui`

**[SPEC-24](04-fase-1-competir/SPEC-24-agenda-y-citas/spec.md)** · agenda y citas (7/7)

- [x] [HU-CAL-01](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-01-bloqueos-de-agenda.md) Bloqueos de agenda y vista semanal · M — `agentcore-conventions`, `frontend-design`, `backend-design:security-discipline`
- [x] [HU-CAL-02](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-02-agendar-reagendar-cancelar.md) Agendar, reagendar y cancelar demos con correo · L · depende de [HU-CAL-01](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-01-bloqueos-de-agenda.md) — `agentcore-conventions`, `backend-design:security-discipline`, `backend-design:testing-with-discernment`
- [x] [HU-CAL-03](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-03-calendario-visual.md) Calendario visual tipo Google Calendar · L · depende de [HU-CAL-01](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-01-bloqueos-de-agenda.md), [HU-CAL-02](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-02-agendar-reagendar-cancelar.md) — `frontend-design`, `agentcore-conventions`
- [x] [HU-CAL-04](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md) Fecha actual en el prompt y política anti-escalamiento · M · depende de [HU-CAL-02](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-02-agendar-reagendar-cancelar.md) — `agentcore-conventions`, `db-migration`, `backend-design:migration-safety`, `adr`, `panel-ui`, `backend-design:testing-with-discernment`, `desplegar-test-agent-core`
- [x] [HU-CAL-05](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-05-pack-de-agendamiento-definitivo.md) Pack de agendamiento definitivo · L · depende de [HU-CAL-02](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-02-agendar-reagendar-cancelar.md), [HU-CAL-04](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md) — `new-tool`, `agentcore-conventions`, `backend-design:idempotency-and-side-effects`, `backend-design:testing-with-discernment`, `eval-author`, agente `auditor-multitenant`, `desplegar-test-agent-core`
- [x] [HU-CAL-06](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) Afinado del asistente de la agencia y E2E del agendamiento · M · depende de [HU-CAL-04](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md), [HU-CAL-05](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-05-pack-de-agendamiento-definitivo.md) — agente `customizer`, agente `eval-runner`, `desplegar-test-agent-core`, `built-in-browser`
- [x] [HU-CAL-07](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-07-google-desde-el-panel.md) Conectar Google Calendar desde el panel nuevo · M · depende de [HU-CAL-02](04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-02-agendar-reagendar-cancelar.md) — `backend-design:auth-and-authorization`, `backend-design:security-discipline`, `adr`, `panel-ui`, `desplegar-test-agent-core`, `desplegar-test`

**[SPEC-25](04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md)** · app movil oficial (20/21)

- [x] [HU-APP-01](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-01-nucleo-modular-de-la-app.md) Núcleo modular de la app · M — `adr`, `frontend-design`
- [x] [HU-APP-02](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-02-sesion-unica-y-recuperacion.md) Sesión única, recuperación de contraseña y biometría · L · depende de [HU-APP-01](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-01-nucleo-modular-de-la-app.md) — `backend-design:auth-and-authorization`, `backend-design:security-discipline`, `frontend-design`
- [x] [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md) Navegación por permisos y roles · M · depende de [HU-APP-01](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-01-nucleo-modular-de-la-app.md) — `frontend-design`, `backend-design:security-discipline`
- [x] [HU-APP-04](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-04-dashboard-con-kpis.md) Dashboard con KPIs · M · depende de [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md) — `panel-ui`, `frontend-design`
- [x] [HU-APP-05](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-05-notificaciones-push.md) Notificaciones push · M · depende de [HU-APP-02](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-02-sesion-unica-y-recuperacion.md) — `agentcore-conventions`, `backend-design:observability-by-default`
- [x] [HU-APP-06](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-06-almacenamiento-local-cifrado.md) Almacenamiento local cifrado · M · depende de [HU-APP-01](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-01-nucleo-modular-de-la-app.md) — `backend-design:data-modeling-discipline`, `backend-design:migration-safety`
- [x] [HU-APP-07](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md) Cobranza al núcleo sin regresión · L · depende de [HU-APP-01](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-01-nucleo-modular-de-la-app.md), [HU-APP-02](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-02-sesion-unica-y-recuperacion.md), [HU-APP-06](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-06-almacenamiento-local-cifrado.md) — `frontend-design`, `backend-design:testing-with-discernment`
- [x] [HU-APP-08](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-08-operacion-movil.md) Operación móvil: conversaciones, escalaciones y leads · L · depende de [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md), [HU-APP-04](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-04-dashboard-con-kpis.md) — `frontend-design`, `panel-ui`
- [x] [HU-APP-09](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-09-negocio-movil.md) Negocio móvil: plan, consumo y costos · M · depende de [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md), [HU-APP-04](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-04-dashboard-con-kpis.md) — `panel-ui`
- [x] [HU-APP-10](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-10-comercio-movil.md) Comercio móvil: productos, categorías, promociones y pedidos · L · depende de [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md) — `frontend-design`, `panel-ui`
- [x] [HU-APP-11](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-11-calendario-movil.md) Calendario móvil: citas, tipos, bloqueos y horario · L · depende de [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md) — `frontend-design`, `panel-ui`
- [x] [HU-APP-12](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-12-configuracion-movil.md) Configuración móvil: colaboradores, habilidades, conexiones y ajustes · L · depende de [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md) — `frontend-design`, `backend-design:security-discipline`
- [x] [HU-APP-13](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-13-herramientas-y-plataforma-movil.md) Herramientas y plataforma móvil: asistente, plantillas, DLQ y negocios · M · depende de [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md) — `frontend-design`
- [x] [HU-APP-14](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-14-busqueda-global.md) Búsqueda global · M · depende de [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md) — `agentcore-conventions`, `backend-design:query-discipline`
- [x] [HU-APP-15](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-15-sync-offline-por-modulos.md) Sincronización offline-first por módulos · L · depende de [HU-APP-06](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-06-almacenamiento-local-cifrado.md), [HU-APP-08](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-08-operacion-movil.md) — `backend-design:idempotency-and-side-effects`, `backend-design:data-modeling-discipline`
- [x] [HU-APP-16](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-16-seguridad-de-la-app.md) Seguridad de la app: certificate pinning y hardening · M · depende de [HU-APP-06](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-06-almacenamiento-local-cifrado.md) — `backend-design:security-discipline`, `backend-design:auth-and-authorization`
- [ ] [HU-APP-17](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-17-release-firmado-y-guias.md) Release firmado y guías de build · M · depende de [HU-APP-07](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md), [HU-APP-15](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-15-sync-offline-por-modulos.md), [HU-APP-16](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-16-seguridad-de-la-app.md) — `release`, `adr`
- [x] [HU-APP-18](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-18-cobranza-admin-movil.md) Cobranza admin móvil: réplica total del pack · L · depende de [HU-APP-03](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md) — `frontend-design`, `panel-ui`
- [x] [HU-APP-19](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-19-cobranza-admin-profunda.md) Cobranza admin profunda móvil · L · depende de [HU-APP-18](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-18-cobranza-admin-movil.md) — `frontend-design`, `panel-ui`
- [x] [HU-APP-20](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-20-escrituras-moviles.md) Escrituras móviles · M · depende de [HU-APP-10](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-10-comercio-movil.md), [HU-APP-11](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-11-calendario-movil.md), [HU-APP-12](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-12-configuracion-movil.md) — `frontend-design`, `panel-ui`
- [x] [HU-APP-21](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-21-herramientas-profunda.md) Herramientas profundas móvil · M · depende de [HU-APP-08](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-08-operacion-movil.md), [HU-APP-12](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-12-configuracion-movil.md), [HU-APP-14](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-14-busqueda-global.md) — `frontend-design`, `panel-ui`

**[SPEC-26](04-fase-1-competir/SPEC-26-agent-os/spec.md)** · agent os (17/40)

- [x] [HU-AOS-01](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-01-adrs-del-agent-os.md) ADRs del Agent OS (0112–0119) · M — `adr`, agente `arquitecto`
- [x] [HU-AOS-02](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-02-esquema-aditivo.md) Esquema aditivo del Agent OS (expand) · L · depende de [HU-AOS-01](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-01-adrs-del-agent-os.md) — `db-migration`, `backend-design:migration-safety`, agente `auditor-multitenant`
- [x] [HU-AOS-03](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md) Contrato procedure/1, linter y conversión de flujos · M · depende de [HU-AOS-01](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-01-adrs-del-agent-os.md) — `agentcore-conventions`, `new-pack`, `backend-design:data-modeling-discipline`
- [x] [HU-AOS-04](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-04-estado-de-la-conversacion.md) Estado de la conversación: tareas event-sourced y tarjeta de estado · L · depende de [HU-AOS-02](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-02-esquema-aditivo.md) — `backend-design:data-modeling-discipline`, `backend-design:idempotency-and-side-effects`, agente `auditor-multitenant`
- [x] [HU-AOS-05](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-05-motor-de-procedimientos.md) Motor de procedimientos: etapas, datos validados, precondiciones, confirmación y cierre · L · depende de [HU-AOS-03](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md), [HU-AOS-04](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-04-estado-de-la-conversacion.md) — `agentcore-conventions`, `backend-design:think-before-coding`, `backend-design:idempotency-and-side-effects`
- [x] [HU-AOS-06](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-06-comandos-y-verificador-sobre-estado.md) Comandos del hilo y verificador sobre el estado · M · depende de [HU-AOS-05](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-05-motor-de-procedimientos.md), [HU-ARCH-29](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md) — `new-tool`, `agentcore-conventions`, `backend-design:testing-with-discernment`
- [x] [HU-AOS-07](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-07-procedimientos-de-comercio.md) Procedimientos de comercio (planes, contratar plan, pedido con entrega) · L · depende de [HU-AOS-06](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-06-comandos-y-verificador-sobre-estado.md) — `new-pack`, `new-tool`, `eval-author`
- [x] [HU-AOS-08](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-08-procedimientos-de-agenda-suscripciones-y-cobranza.md) Procedimientos de agenda, suscripciones (incluye cambio de plan) y cobranza · L · depende de [HU-AOS-06](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-06-comandos-y-verificador-sobre-estado.md) — `new-pack`, `new-tool`, `eval-author`
- [x] [HU-AOS-09](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md) Política de modelo por riesgo y confirmación con botón interactivo · M · depende de [HU-AOS-05](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-05-motor-de-procedimientos.md) — `meta-whatsapp`, `agentcore-conventions`, agente `optimizer`
- [x] [HU-AOS-10](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-10-kernel-del-coordinador.md) Kernel del Coordinador: políticas, core_decisions, turn_outcomes y trazas · L · depende de [HU-AOS-02](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-02-esquema-aditivo.md) — `agentcore-conventions`, `backend-design:observability-by-default`, `backend-design:think-before-coding`
- [ ] [HU-AOS-11](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-11-conexion-canonica.md) Conexión canónica y conversación por conexión (chat web como conexión) · L · depende de [HU-AOS-02](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-02-esquema-aditivo.md), [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md), [HU-CONN-05](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md) — `meta-whatsapp`, `db-migration`, `backend-design:migration-safety`, agente `auditor-multitenant`
- [x] [HU-AOS-12](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-12-agentes-versionados.md) Agentes con versiones inmutables: AgentSpec v3 y KernelSpec · L · depende de [HU-AOS-03](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md) — `agentcore-conventions`, `backend-design:data-modeling-discipline`, `adr`
- [x] [HU-AOS-13](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-13-instancias-por-conexion.md) Instancias por conexión: Coordinador + General · M · depende de [HU-AOS-11](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-11-conexion-canonica.md), [HU-AOS-12](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-12-agentes-versionados.md) — `db-migration`, agente `auditor-multitenant`, `onboard-tenant`
- [x] [HU-AOS-14](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-14-releases-por-conexion.md) Releases por conexión con rollback en un clic · L · depende de [HU-AOS-13](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-13-instancias-por-conexion.md) — `release`, `backend-design:data-modeling-discipline`, `backend-design:testing-with-discernment`
- [ ] [HU-AOS-15](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md) Migración de todos los negocios sin regresión de pass^k · M · depende de [HU-AOS-07](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-07-procedimientos-de-comercio.md), [HU-AOS-08](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-08-procedimientos-de-agenda-suscripciones-y-cobranza.md), [HU-AOS-10](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-10-kernel-del-coordinador.md), [HU-AOS-14](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-14-releases-por-conexion.md), [HU-ARCH-28](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) — `release`, agente `eval-runner`, `desplegar-test-agent-core`
- [ ] [HU-AOS-16](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md) Habilidades versionadas con procedimientos, consultas y plantillas (instalación por scope) · L · depende de [HU-AOS-12](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-12-agentes-versionados.md), [HU-FWK-04](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md) — agente `plugin-dev`, `db-migration`, agente `auditor-multitenant`, `backend-design:security-discipline`
- [ ] [HU-AOS-17](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-17-enrutamiento-y-modo-sombra.md) Enrutamiento: tarea en foco, reglas, disparadores y modo sombra · M · depende de [HU-AOS-15](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md) — `eval-author`, agente `optimizer`, `agentcore-conventions`
- [ ] [HU-AOS-18](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md) Permisos de colaboración, límites y ledger A2A · L · depende de [HU-AOS-15](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md) — `backend-design:security-discipline`, agente `auditor-multitenant`, `backend-design:think-before-coding`
- [ ] [HU-AOS-19](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-19-handoff-delegacion-y-consulta.md) Handoff, delegación y consulta en el mismo hilo · L · depende de [HU-AOS-17](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-17-enrutamiento-y-modo-sombra.md), [HU-AOS-18](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md) — `new-tool`, `eval-author`, `backend-design:idempotency-and-side-effects`
- [ ] [HU-AOS-20](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-20-colaboracion-con-pila-de-tareas.md) Colaboración con pila de tareas · M · depende de [HU-AOS-19](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-19-handoff-delegacion-y-consulta.md) — `eval-author`, `agentcore-conventions`
- [ ] [HU-AOS-21](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md) Gate de release por pass^k (procedimiento, agente y ruta) · M · depende de [HU-AOS-15](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md), [HU-ARCH-28](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) — agente `eval-runner`, `eval-author`, `release`
- [ ] [HU-AOS-22](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-22-dogfooding-solvershub.md) Dogfooding: SolversHub con Ventas, Agenda y Suscripciones · M · depende de [HU-AOS-16](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md), [HU-AOS-19](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-19-handoff-delegacion-y-consulta.md), [HU-AOS-21](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md), [HU-SH-08](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md) — `onboard-tenant`, agente `customizer`, agente `eval-runner`, `desplegar-test-agent-core`
- [x] [HU-AOS-23](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md) Consola de conexiones y hub · M · depende de [HU-AOS-15](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md) — `panel-ui`, `frontend-design`
- [x] [HU-AOS-24](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) Editor de agentes desde plantillas · L · depende de [HU-AOS-16](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md), [HU-FWK-08](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-08-formulario-de-schema-v2.md) — `panel-ui`, `frontend-design`, agente `customizer`
- [ ] [HU-AOS-25](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md) Superpoderes en el panel: recorrido, frases, textos y confirmaciones · M · depende de [HU-AOS-24](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) — `panel-ui`, `frontend-design`
- [ ] [HU-AOS-26](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-26-colaboracion-en-el-panel.md) Colaboración y enrutamiento en el panel · M · depende de [HU-AOS-18](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-24](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) — `panel-ui`, `frontend-design`
- [ ] [HU-AOS-27](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-27-versiones-en-el-panel.md) Versiones: diferencias, probar, publicar y revertir · M · depende de [HU-AOS-14](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-14-releases-por-conexion.md), [HU-AOS-21](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md), [HU-AOS-23](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md) — `panel-ui`, `frontend-design`
- [ ] [HU-AOS-28](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md) Depurador conversacional y panel En curso · L · depende de [HU-AOS-04](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-04-estado-de-la-conversacion.md), [HU-AOS-18](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-ARCH-14](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-14-playground-sandbox.md) — `panel-ui`, `frontend-design`, `backend-design:observability-by-default`
- [ ] [HU-AOS-29](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md) Tablero de fiabilidad · M · depende de [HU-AOS-18](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-21](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md) — `panel-ui`, `kpi-dashboard-design`, `data:build-dashboard`
- [ ] [HU-AOS-30](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-30-agentes-de-back-office.md) Agentes de back-office asíncronos · L · depende de [HU-AOS-18](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md) — `backend-design:idempotency-and-side-effects`, `new-tool`, `meta-whatsapp`
- [ ] [HU-AOS-31](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-31-auditor-de-calidad.md) Auditor de calidad y LLM-juez calibrado · M · depende de [HU-AOS-21](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md), [HU-AOS-28](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md) — `eval-author`, `data:statistical-analysis`, agente `eval-runner`
- [ ] [HU-AOS-32](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-32-canary-y-auto-rollback.md) Canary sticky con no-inferioridad y auto-rollback · M · depende de [HU-AOS-27](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-27-versiones-en-el-panel.md), [HU-AOS-29](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md) — `release`, `data:statistical-analysis`, `backend-design:observability-by-default`
- [ ] [HU-AOS-33](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-33-feedback-y-propuestas.md) Feedback y propuestas de mejora con aprobación humana · M · depende de [HU-AOS-31](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-31-auditor-de-calidad.md) — `eval-author`, `panel-ui`
- [ ] [HU-AOS-34](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-34-acciones-v2.md) Acciones v2: timeouts, reintentos, circuit breaker y respaldo · M · depende de [HU-AOS-16](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md) — `new-tool`, `backend-design:error-handling-as-design`, `backend-design:idempotency-and-side-effects`
- [ ] [HU-AOS-35](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-35-cache-por-version.md) Caché por versión de lo compilado · S · depende de [HU-AOS-14](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-14-releases-por-conexion.md) — agente `optimizer`, `backend-design:performance-and-scaling`
- [x] [HU-AOS-36](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-36-memoria-por-scope.md) Memoria por scope con procedencia y olvido · L · depende de [HU-AOS-12](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-12-agentes-versionados.md) — `backend-design:data-modeling-discipline`, agente `auditor-multitenant`, `backend-design:security-discipline`
- [ ] [HU-AOS-37](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-37-cuotas-y-planes.md) Cuotas Agent OS: operaciones entre agentes y back-office · M · depende de [HU-AOS-18](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), HU-BILL-05, HU-BILL-06 — `backend-design:think-before-coding`, `panel-ui`
- [ ] [HU-AOS-38](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-38-lanzamiento-comercial.md) Lanzamiento comercial (incluye validar el nombre) · M · depende de [HU-AOS-22](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-22-dogfooding-solvershub.md), [HU-AOS-26](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-26-colaboracion-en-el-panel.md), [HU-AOS-27](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-27-versiones-en-el-panel.md), [HU-AOS-37](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-37-cuotas-y-planes.md), HU-GTM-05, [HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) — `doc-coauthoring`, `frontend-design`
- [ ] [HU-AOS-46](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) Presets v2: plantillas de agente, reglas del Coordinador y permisos · M · depende de [HU-AOS-16](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md), [HU-FWK-10](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-10-aplicar-preset-desde-panel.md) — `adr`, agente `arquitecto`, `agentcore-conventions`
- [x] [HU-AOS-47](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md) Mi agente y su data · L · depende de [HU-AOS-15](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md), [HU-AOS-23](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md) — `panel-ui`, `frontend-design`, `backend-design:query-discipline`, agente `auditor-multitenant`

**[SPEC-28](04-fase-1-competir/SPEC-28-inmoagent/spec.md)** · inmoagent (0/30)

- [ ] [HU-INMO-01](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md) ADRs de la vertical y DoR del piloto · M — `adr`, agente `arquitecto`, `agentcore-conventions`, `deep-research`
- [ ] [HU-INMO-02](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-02-entrada-estructurada-whatsapp.md) Ubicación y respuestas de lista entrantes · M · depende de [HU-INMO-01](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md) — `meta-whatsapp`, `agentcore-conventions`, `backend-design:security-discipline`
- [ ] [HU-INMO-03](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-03-salida-interactiva.md) Listas, ubicación e imágenes salientes · M · depende de [HU-INMO-01](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md) — `meta-whatsapp`, `agentcore-conventions`, `new-tool`
- [ ] [HU-INMO-04](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-04-avisos-abiertos-a-habilidades.md) Avisos por evento abiertos a las habilidades · M · depende de [HU-INMO-01](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md) — `meta-whatsapp`, `agentcore-conventions`, `adr`
- [ ] [HU-INMO-05](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-05-agenda-por-responsable.md) Agenda por asesor con referencia y correo opcional · M · depende de [HU-INMO-01](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md) — `db-migration`, agente `auditor-multitenant`, `backend-design:migration-safety`, `agentcore-conventions`
- [ ] [HU-INMO-06](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-06-agenda-como-capacidad-del-core.md) Agenda como capacidad del core · M · depende de [HU-INMO-05](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-05-agenda-por-responsable.md) — `agentcore-conventions`, `backend-design:idempotency-and-side-effects`, `adr`
- [ ] [HU-INMO-07](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-07-escalamiento-al-responsable.md) Relevo al asesor del caso · S · depende de [HU-INMO-10](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md) — `agentcore-conventions`, `new-tool`
- [ ] [HU-INMO-08](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-08-suscripciones-de-plazo-fijo.md) Suscripciones para contratos de plazo fijo · M · depende de [HU-INMO-01](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md) — `pagos-wompi`, `db-migration`, `backend-design:idempotency-and-side-effects`, agente `auditor-multitenant`
- [ ] [HU-INMO-09](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-09-supresion-de-datos-del-titular.md) Supresión de datos del titular en la vertical · S · depende de [HU-INMO-10](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md) — `backend-design:security-discipline`, `db-migration`, agente `auditor-multitenant`
- [ ] [HU-INMO-10](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md) Pack inmobiliario: inventario geoespacial con RLS · L · depende de [HU-INMO-01](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md) — `new-pack`, `db-migration`, agente `auditor-multitenant`, `backend-design:data-modeling-discipline`
- [ ] [HU-INMO-11](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-11-inventario-y-captaciones-en-el-panel.md) Inventario y captaciones en el panel, con importación · L · depende de [HU-INMO-10](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md), [HU-FWK-07](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-07-descriptor-view.md), [HU-MEDIA-02](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md) — `panel-ui`, agente `migrator`, `frontend-design`
- [ ] [HU-INMO-12](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-12-geocodificacion-y-zonas.md) Geocodificación con confirmación y zonas · M · depende de [HU-INMO-02](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-02-entrada-estructurada-whatsapp.md), [HU-INMO-03](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-03-salida-interactiva.md), [HU-INMO-10](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md) — `new-tool`, `backend-design:security-discipline`, `deep-research`
- [ ] [HU-INMO-13](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-13-puntos-de-interes-y-cercanias.md) Puntos de interés y cercanías precalculadas · M · depende de [HU-INMO-10](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md) — `data:sql-queries`, `backend-design:performance-and-scaling`
- [ ] [HU-INMO-14](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-14-busqueda-con-filtros-y-geo.md) Búsqueda con filtros y consultas geoespaciales · L · depende de [HU-INMO-12](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-12-geocodificacion-y-zonas.md), [HU-INMO-13](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-13-puntos-de-interes-y-cercanias.md) — `new-tool`, `data:sql-queries`, `backend-design:query-discipline`, `eval-author`
- [ ] [HU-INMO-15](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-15-recomendaciones-y-relajacion.md) Recomendaciones explicadas y relajación de filtros · M · depende de [HU-INMO-14](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-14-busqueda-con-filtros-y-geo.md) — `new-tool`, `eval-author`, agente `optimizer`
- [ ] [HU-INMO-16](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-16-perfil-de-busqueda-persistente.md) Perfil de búsqueda persistente y feedback · M · depende de [HU-INMO-15](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-15-recomendaciones-y-relajacion.md) — `new-tool`, `backend-design:data-modeling-discipline`
- [ ] [HU-INMO-17](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-17-fichas-y-verificacion-de-hechos.md) Fichas en el chat y verificación de hechos del inmueble · M · depende de [HU-INMO-03](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-03-salida-interactiva.md), [HU-INMO-15](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-15-recomendaciones-y-relajacion.md), [HU-ARCH-29](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md) — `new-tool`, `eval-author`, `meta-whatsapp`
- [ ] [HU-INMO-18](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-18-captacion-de-propietarios.md) Captación de inmuebles de propietarios · L · depende de [HU-INMO-04](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-04-avisos-abiertos-a-habilidades.md), [HU-INMO-11](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-11-inventario-y-captaciones-en-el-panel.md), [HU-INMO-12](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-12-geocodificacion-y-zonas.md) — `new-tool`, `turnstile-spin`, `meta-whatsapp`, `backend-design:security-discipline`
- [ ] [HU-INMO-19](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-19-visitas-con-el-asesor.md) Visitas con el asesor del inmueble · M · depende de [HU-INMO-06](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-06-agenda-como-capacidad-del-core.md), [HU-INMO-17](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-17-fichas-y-verificacion-de-hechos.md) — `new-tool`, `eval-author`, `backend-design:idempotency-and-side-effects`
- [ ] [HU-INMO-20](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-20-oportunidades-y-asesores.md) Oportunidades, asesores y leads · M · depende de [HU-INMO-07](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-07-escalamiento-al-responsable.md), [HU-INMO-10](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md) — `panel-ui`, `db-migration`, `agentcore-conventions`
- [ ] [HU-INMO-21](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-21-seguimiento-post-visita-y-encuesta.md) Seguimiento post-visita y encuesta · M · depende de [HU-INMO-04](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-04-avisos-abiertos-a-habilidades.md), [HU-INMO-19](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-19-visitas-con-el-asesor.md), [HU-INMO-20](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-20-oportunidades-y-asesores.md) — `meta-whatsapp`, `eval-author`
- [ ] [HU-INMO-22](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-22-alertas-y-reenganche.md) Alertas de coincidencias y reenganche de leads · M · depende de [HU-INMO-04](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-04-avisos-abiertos-a-habilidades.md), [HU-INMO-16](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-16-perfil-de-busqueda-persistente.md), [HU-CHAN-03](04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-03-pack-marketing.md) — `meta-whatsapp`, `eval-author`
- [ ] [HU-INMO-23](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-23-contrato-de-arriendo-y-canon.md) Contrato de arriendo como registro y cobro del canon · L · depende de [HU-INMO-08](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-08-suscripciones-de-plazo-fijo.md), [HU-INMO-11](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-11-inventario-y-captaciones-en-el-panel.md) — `pagos-wompi`, `db-migration`, agente `auditor-multitenant`, `new-tool`
- [ ] [HU-INMO-24](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-24-mora-e-incremento-del-canon.md) Mora e incremento anual del canon · M · depende de [HU-INMO-04](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-04-avisos-abiertos-a-habilidades.md), HU-SUB-18, [HU-INMO-23](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-23-contrato-de-arriendo-y-canon.md) — `pagos-wompi`, `deep-research`, `meta-whatsapp`
- [ ] [HU-INMO-25](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-25-preset-golden-y-journeys.md) Preset inmobiliaria, golden y journeys de la vertical · M · depende de [HU-INMO-17](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-17-fichas-y-verificacion-de-hechos.md), [HU-INMO-18](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-18-captacion-de-propietarios.md), [HU-INMO-19](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-19-visitas-con-el-asesor.md), [HU-INMO-24](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-24-mora-e-incremento-del-canon.md), [HU-ARCH-28](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) — `eval-author`, `onboard-tenant`, agente `customizer`, agente `eval-runner`
- [ ] [HU-INMO-26](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-26-kpis-de-la-vertical.md) KPIs de la vertical · M · depende de [HU-INMO-20](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-20-oportunidades-y-asesores.md), [HU-INMO-24](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-24-mora-e-incremento-del-canon.md), [HU-FWK-07](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-07-descriptor-view.md) — `kpi-dashboard-design`, `data:sql-queries`, `panel-ui`
- [ ] [HU-INMO-27](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-27-procedimientos-1-1.md) Afirmaciones de atributo, distancia y prohibidas · M · depende de [HU-AOS-06](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-06-comandos-y-verificador-sobre-estado.md), [HU-INMO-17](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-17-fichas-y-verificacion-de-hechos.md) — `adr`, agente `arquitecto`, `eval-author`
- [ ] [HU-INMO-29](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-29-procedimientos-inmobiliarios.md) Procedimientos tipados inmobiliarios · L · depende de [HU-INMO-25](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-25-preset-golden-y-journeys.md), [HU-INMO-27](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-27-procedimientos-1-1.md) — `eval-author`, `new-tool`, `agentcore-conventions`
- [ ] [HU-INMO-30](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-30-especialistas-inmobiliarios.md) Especialistas inmobiliarios en el Coordinador · M · depende de [HU-INMO-29](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-29-procedimientos-inmobiliarios.md), [HU-AOS-46](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md), [HU-AOS-19](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-19-handoff-delegacion-y-consulta.md), [HU-AOS-21](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md) — `eval-author`, agente `arquitecto`, agente `customizer`
- [ ] [HU-INMO-31](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-31-back-office-y-memoria.md) Back-office y memoria de la vertical · M · depende de [HU-INMO-21](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-21-seguimiento-post-visita-y-encuesta.md), [HU-INMO-22](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-22-alertas-y-reenganche.md), [HU-INMO-30](04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-30-especialistas-inmobiliarios.md), [HU-AOS-30](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-30-agentes-de-back-office.md), [HU-AOS-36](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-36-memoria-por-scope.md) — `eval-author`, agente `arquitecto`

**[SPEC-29](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md)** · sistema de diseno unificado (5/13)

- [x] [HU-DS-01](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-01-tokens-v2.md) Tokens v2 · M — `frontend-design`, `dataviz`, `panel-ui`
- [x] [HU-DS-02](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-02-contraste-aa-y-gates.md) Contraste AA y gates del sistema de diseño · M · depende de [HU-DS-01](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-01-tokens-v2.md), [HU-UI-04](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md) — `panel-ui`, `web-perf`, `/code-review`
- [x] [HU-DS-03](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-03-kit-de-componentes-panel.md) Kit de componentes v2 del panel y catálogo · L · depende de [HU-DS-01](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-01-tokens-v2.md) — `frontend-design`, `panel-ui`, `/code-review`
- [x] [HU-DS-04](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-04-shell-adaptativo-del-panel.md) Shell adaptativo del panel · L · depende de [HU-DS-03](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-03-kit-de-componentes-panel.md), [HU-UI-03](03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md) — `frontend-design`, `panel-ui`, `built-in-browser`
- [ ] [HU-DS-05](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-05-paleta-de-comandos-y-atajos.md) Paleta de comandos y atajos · M · depende de [HU-DS-04](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-04-shell-adaptativo-del-panel.md) — `frontend-design`, `panel-ui`
- [ ] [HU-DS-06](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-06-primitivas-de-visualizacion.md) Primitivas de visualización de datos · M · depende de [HU-DS-01](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-01-tokens-v2.md) — `dataviz`, `frontend-design`, `panel-ui`
- [ ] [HU-DS-07](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-07-resumen-modular-por-rol.md) Resumen modular por rol · L · depende de [HU-DS-03](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-03-kit-de-componentes-panel.md), [HU-DS-06](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-06-primitivas-de-visualizacion.md), [HU-UI-07](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) — `kpi-dashboard-design`, `dataviz`, `frontend-design`, `panel-ui`
- [ ] [HU-DS-08](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-08-widgets-reorganizables.md) Widgets reorganizables · M · depende de [HU-DS-07](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-07-resumen-modular-por-rol.md) — `frontend-design`, `panel-ui`
- [ ] [HU-DS-09](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-09-kit-de-componentes-app.md) Kit de componentes de la app · L · depende de [HU-DS-01](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-01-tokens-v2.md) — `frontend-design`, `/code-review`
- [ ] [HU-DS-10](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-10-cobranza-de-campo-con-el-kit.md) Cobranza de campo con el kit nuevo · L · depende de [HU-DS-09](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-09-kit-de-componentes-app.md) — `frontend-design`, `/code-review`
- [x] [HU-DS-11](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-11-shell-del-panel-en-la-app.md) Shell del panel en la app con cajón lateral y tema oscuro · L · depende de [HU-DS-09](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-09-kit-de-componentes-app.md) — `frontend-design`, `/code-review`
- [ ] [HU-DS-12](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-12-motion-y-microinteracciones.md) Motion y microinteracciones · M · depende de [HU-DS-04](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-04-shell-adaptativo-del-panel.md), [HU-DS-09](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-09-kit-de-componentes-app.md) — `frontend-design`, `panel-ui`
- [ ] [HU-DS-13](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-13-resumen-movil-por-rol.md) Resumen móvil por rol · L · depende de [HU-DS-07](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-07-resumen-modular-por-rol.md), [HU-DS-11](04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-11-shell-del-panel-en-la-app.md) — `kpi-dashboard-design`, `dataviz`, `frontend-design`

**[SPEC-30](04-fase-1-competir/SPEC-30-centro-de-pruebas/spec.md)** · centro de pruebas (5/9)

- [x] [HU-QA-01](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-01-modelo-y-api-de-pruebas.md) Modelo y API de pruebas · M — `db-migration`, `backend-design:data-modeling-discipline`, `backend-design:auth-and-authorization`, agente `auditor-multitenant`
- [x] [HU-QA-02](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-02-catalogo-versionado-desde-docs.md) Catálogo versionado desde docs · S · depende de [HU-QA-01](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-01-modelo-y-api-de-pruebas.md) — `agentcore-conventions`, `backend-design:idempotency-and-side-effects`
- [x] [HU-QA-03](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-03-seccion-pruebas-en-el-panel.md) Sección Pruebas en el panel · M · depende de [HU-QA-01](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-01-modelo-y-api-de-pruebas.md) — `panel-ui`, `frontend-design`, `built-in-browser`
- [x] [HU-QA-04](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-04-rol-tester-e-invitaciones.md) Rol tester e invitaciones · M · depende de [HU-QA-03](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-03-seccion-pruebas-en-el-panel.md) — `backend-design:auth-and-authorization`, agente `backend-design:security-reviewer`, `panel-ui`, agente `auditor-multitenant`
- [ ] [HU-QA-05](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-05-migrar-desde-el-artifact.md) Migrar resultados desde el artifact · S · depende de [HU-QA-02](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-02-catalogo-versionado-desde-docs.md), [HU-QA-03](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-03-seccion-pruebas-en-el-panel.md) — agente `migrator`, `backend-design:idempotency-and-side-effects`
- [ ] [HU-QA-06](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-06-catalogo-historico-del-proyecto.md) Catálogo histórico del proyecto · L — `ejecutar-hu`, `doc-coauthoring`
- [ ] [HU-QA-07](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-07-datos-de-prueba.md) Datos de prueba propios y guía de datos · M · depende de [HU-QA-04](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-04-rol-tester-e-invitaciones.md) — `backend-design:idempotency-and-side-effects`, `panel-ui`, agente `auditor-multitenant`
- [ ] [HU-QA-08](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-08-pruebas-por-entorno-y-seccion.md) Pruebas por entorno y sección · S · depende de [HU-QA-06](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-06-catalogo-historico-del-proyecto.md) — `panel-ui`
- [x] [HU-QA-09](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-09-datos-de-prueba-para-el-agent-os.md) Datos de prueba listos para el Agent OS · M · depende de [HU-QA-07](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-07-datos-de-prueba.md) — `backend-design:idempotency-and-side-effects`, `panel-ui`, agente `auditor-multitenant`

**[SPEC-31](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/spec.md)** · mejoras del ciclo de pruebas (0/11)

- [ ] [HU-AOS-48](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-AOS-48-onboarding-con-guion-por-agente.md) Onboarding con guion de preguntas por tipo de agente · L · depende de [HU-AOS-24](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md), [HU-AOS-46](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) — `panel-ui`, `frontend-design`, `agentcore-conventions`, `eval-author`
- [ ] [HU-AOS-49](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-AOS-49-pack-de-conocimiento.md) Pack de conocimiento con documentos por agente · L · depende de [HU-AOS-24](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) — `new-pack`, `db-migration`, `adr`, agente `arquitecto`, agente `auditor-multitenant`, `eval-author`, agente `optimizer`
- [ ] [HU-UX-12](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-12-arreglos-rapidos-del-ciclo.md) Arreglos rápidos del ciclo de pruebas · S · depende de [HU-UX-02](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) — `panel-ui`, `frontend-design`
- [ ] [HU-UX-13](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-13-avisos-y-formularios-en-espanol.md) Avisos y formularios en español · M · depende de [HU-UX-12](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-12-arreglos-rapidos-del-ciclo.md) — `panel-ui`, `frontend-design`, `backend-design:error-handling-as-design`
- [ ] [HU-UX-14](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-14-shell-v2-y-perfil.md) Shell v2 y perfil del usuario · M · depende de [HU-UX-12](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-12-arreglos-rapidos-del-ciclo.md) — `panel-ui`, `frontend-design`, `backend-design:auth-and-authorization`
- [ ] [HU-UX-15](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-15-bandeja-de-conversaciones.md) Bandeja de conversaciones en vivo estilo WhatsApp Web · L · depende de [HU-UX-16](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-16-clientes-estilo-agent-sale.md), [HU-UX-17](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-17-motivos-de-escalacion-legibles.md) — `panel-ui`, `frontend-design`, `backend-design:query-discipline`, `backend-design:performance-and-scaling`, agente `auditor-multitenant`
- [ ] [HU-UX-16](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-16-clientes-estilo-agent-sale.md) Clientes con ficha editable y pausa del agente por cliente · L · depende de [HU-UX-12](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-12-arreglos-rapidos-del-ciclo.md) — `panel-ui`, `frontend-design`, `agentcore-conventions`, `backend-design:query-discipline`, agente `auditor-multitenant`
- [ ] [HU-UX-17](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-17-motivos-de-escalacion-legibles.md) Motivos de escalación legibles con lista cerrada · M — `panel-ui`, `frontend-design`, `agentcore-conventions`, `adr`
- [ ] [HU-UX-18](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-18-listas-y-formularios-de-seccion.md) Listas y formularios de las secciones · M · depende de [HU-UX-12](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-12-arreglos-rapidos-del-ciclo.md) — `panel-ui`, `frontend-design`
- [ ] [HU-UX-19](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-19-centro-de-notificaciones.md) Centro de notificaciones en el panel y la app · L · depende de [HU-UX-14](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-14-shell-v2-y-perfil.md) — `panel-ui`, `frontend-design`, `db-migration`, agente `arquitecto`, agente `auditor-multitenant`, `adr`
- [ ] [HU-UX-20](04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-20-apk-lo-que-falto-del-ciclo.md) APK con búsqueda en Negocios, inicio sin conexión y notas de cartera · M · depende de [HU-UX-11](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md) — `frontend-design`
<!-- GENERADO:hu-1:fin -->

**Para cerrar la Fase 1**

- [ ] 3–5 clientes de pago.
- [ ] Menú v2 y primeros pasos en producción.
- [ ] Bandeja y tickets en uso diario.
- [ ] Un negocio con dos agentes publicados operando con su Coordinador (D-35).
- [ ] Instagram o chat web operativo.
- [ ] Recargas vendidas.
- [ ] Status page pública.

### 6.4 Fase 2 · "Plus"

**Para empezar**

- [ ] Fase 1 cerrada y decisiones de [SPEC-21](05-fase-2-plus/SPEC-21-agencia-e-internacional/spec.md) a [SPEC-23](05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/spec.md) tomadas.

<!-- GENERADO:hu-2:inicio -->
**[SPEC-21](05-fase-2-plus/SPEC-21-agencia-e-internacional/spec.md)** · agencia e internacional (0/0 · 5 parqueadas)


- [ ] [HU-BILL-13](05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-BILL-13-cobro-internacional.md) ⏸️ parqueada Cobro internacional en USD · L · depende de [HU-BILL-12](04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-12-cambio-de-plan-y-anual.md) — `deep-research`, `adr`, `backend-design:idempotency-and-side-effects`
- [ ] [HU-BILL-14](05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-BILL-14-billing-de-agencia.md) ⏸️ parqueada Billing de agencia con reventa y factura consolidada · L · depende de [HU-FWK-12](05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-FWK-12-organizaciones-y-subcuentas.md), [HU-BILL-10](04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-10-recargas.md) — `backend-design:data-modeling-discipline`, `adr`
- [ ] [HU-FWK-12](05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-FWK-12-organizaciones-y-subcuentas.md) ⏸️ parqueada Organizaciones y sub-cuentas para agencias · M — `adr`, agente `arquitecto`, `backend-design:auth-and-authorization`, agente `auditor-multitenant`
- [ ] [HU-GTM-12](05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-GTM-12-oferta-de-agencia.md) ⏸️ parqueada Oferta de agencia y white-label · M · depende de [HU-BILL-14](05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-BILL-14-billing-de-agencia.md) — `marketing:campaign-plan`, `marketing:competitive-brief`, `pptx`
- [ ] [HU-SUB-17](05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-SUB-17-debito-recurrente.md) ⏸️ parqueada Débito recurrente automático en el contrato de suscripción · L · depende de HU-SUB-15 — `deep-research`, `backend-design:security-discipline`, `backend-design:idempotency-and-side-effects`, `pagos-wompi`

**[SPEC-22](05-fase-2-plus/SPEC-22-extensibilidad-avanzada/spec.md)** · extensibilidad avanzada (1/6)

- [ ] [HU-ARCH-25](05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-25-toolcontext-y-embeddings.md) ToolContext según el contrato y embeddings por negocio · L · depende de [HU-REP-03](03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-03-transicion-de-identificadores.md) — `adr`, agente `arquitecto`, `/codex:adversarial-review`
- [ ] [HU-ARCH-26](05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md) Tool siguiente forzada y turnos silenciosos en el core · L · depende de [HU-ARCH-20](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-20-guardrails-runtime.md) — `claude-api`, `adr`, agente `eval-runner`
- [ ] [HU-COM-16](05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-COM-16-multisucursal.md) Varias sucursales en comercio · L · depende de [HU-COM-08](03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-08-domicilios.md), [HU-COM-15](04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-15-modificadores-y-combos.md) — `backend-design:data-modeling-discipline`, `db-migration`, agente `auditor-multitenant`
- [ ] [HU-FLOW-07](05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FLOW-07-purpose-y-reglas-por-etapa.md) Edición avanzada del purpose y reglas por etapa · M · depende de [HU-FLOW-05](04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-05-borrador-y-publicacion.md) — agente `eval-runner`, `frontend-design`, `panel-ui`
- [x] [HU-FWK-13](05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FWK-13-plugin-del-tenant.md) Plugin del tenant formalizado con scaffold completo · L · depende de [HU-FWK-04](04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md) — agente `plugin-dev`, `new-pack`, `adr`
- [ ] [HU-FWK-14](05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FWK-14-integraciones-mcp.md) Integraciones MCP de catálogo · L · depende de [HU-ARCH-19](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md) — `deep-research`, `backend-design:security-discipline`

**[SPEC-23](05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/spec.md)** · voz reportes y confianza (0/4)

- [ ] [HU-GTM-13](05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-GTM-13-prueba-social.md) Prueba social real en la landing · S · depende de [HU-GTM-08](04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-08-activos-de-venta.md) — `marketing:content-creation`, `marketing:brand-review`
- [ ] [HU-GTM-14](05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-GTM-14-camino-iso-27001.md) Camino a ISO 27001 · L · depende de [HU-ARCH-22](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-22-pentest.md) — `deep-research`, `doc-coauthoring`
- [ ] [HU-MEDIA-08](05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-MEDIA-08-voz-en-llamadas.md) Voz en llamadas con ADR y spike · M · depende de [HU-MEDIA-03](03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md) — `deep-research`, `adr`
- [ ] [HU-UX-07](05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-UX-07-reporte-mensual.md) Reporte mensual automático por negocio · M · depende de [HU-UI-07](04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md), HU-BILL-07 — `kpi-dashboard-design`, `pdf`, `marketing:performance-report`

**[SPEC-27](05-fase-2-plus/SPEC-27-agent-os-plus/spec.md)** · agent os plus (0/7)

- [ ] [HU-AOS-39](05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-39-federacion-entre-negocios.md) Federación entre negocios con consentimiento · L · depende de [HU-AOS-18](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-37](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-37-cuotas-y-planes.md) — `backend-design:security-discipline`, agente `auditor-multitenant`, `backend-design:auth-and-authorization`
- [ ] [HU-AOS-40](05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-40-sandbox-de-acciones.md) Sandbox aislado para acciones no confiables · L · depende de [HU-AOS-34](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-34-acciones-v2.md), [HU-ARCH-19](04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md) — `backend-design:security-discipline`, `backend-design:boring-by-default`
- [ ] [HU-AOS-41](05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-41-auto-mejora-asistida.md) Auto-mejora asistida: de fallas a versión candidata · L · depende de [HU-AOS-32](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-32-canary-y-auto-rollback.md), [HU-AOS-33](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-33-feedback-y-propuestas.md) — `eval-author`, agente `optimizer`
- [ ] [HU-AOS-42](05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-42-canal-api-y-webhooks.md) Canal API y webhooks salientes como conexión · M · depende de [HU-AOS-11](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-11-conexion-canonica.md) — `backend-design:auth-and-authorization`, `backend-design:idempotency-and-side-effects`
- [ ] [HU-AOS-43](05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-43-slack-y-correo-entrante.md) Slack y correo entrante como conexiones · L · depende de [HU-AOS-42](05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-42-canal-api-y-webhooks.md) — `cloudflare-email-service`, `backend-design:think-before-coding`
- [ ] [HU-AOS-44](05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-44-topologia-por-roles.md) Topología por roles y escalado del runtime · M · depende de [HU-AOS-29](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md) — `backend-design:performance-and-scaling`, `release`
- [ ] [HU-AOS-45](05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md) Editor de estructura de superpoderes para el negocio · L · depende de [HU-AOS-25](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md) — `panel-ui`, `frontend-design`
<!-- GENERADO:hu-2:fin -->

**Para cerrar la Fase 2**

- [ ] 2 casos de estudio publicados.
- [ ] Al menos 3 integraciones MCP verificadas.
- [ ] Agencia y cobro en USD solo si [SPEC-21](05-fase-2-plus/SPEC-21-agencia-e-internacional/spec.md) se retoma (parqueada, D-35).

## 7. Checklist de cierre del plan

- [ ] Los criterios de salida de 0A, 0B, Fase 1 y Fase 2 cumplidos con evidencia.
- [ ] Cada HU en `terminada` o con una decisión registrada que la difiere o la descarta.
- [ ] Todas las specs en "Verificada".
- [ ] ADR, `ROADMAP`, `CHANGELOG` y `BACKLOG` de cada repo alineados con lo construido.
- [ ] Matriz competitiva actualizada ([HU-GTM-11](04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-11-matriz-corregida.md)) y columna de SolversHub fiel al producto.
- [ ] Modelo de precios recalibrado con datos reales (`calc_precios.py`) y márgenes medidos por plan.
- [ ] Retro del plan: factor de aceleración real, qué funcionó del método SDD y qué se cambia.
- [ ] Siguiente plan: brechas nuevas frente a la matriz y decisiones abiertas, en una nueva versión de
  `solvershub-docs`.

## 8. Cierre semanal (viernes, 30 minutos)

- [ ] Cambiar el `estado` de las HU terminadas y correr `python3 herramientas/regenerar.py`.
- [ ] Revisar los trámites externos (Meta, abogado, infraestructura) y anotar avances.
- [ ] Revisar los riesgos R-01 a R-14 de [riesgos-supuestos.md](02-vision-y-decisiones/riesgos-supuestos.md) que cambiaron.
- [ ] Anotar días trabajados y HU cerradas, para el factor real.
- [ ] Elegir las HU de la semana siguiente dentro de la ola.
