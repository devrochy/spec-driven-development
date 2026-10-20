---
id: HU-FWK-13
titulo: Plugin del tenant formalizado con scaffold completo
spec: SPEC-22
fase: 2
hito: "2"
workstream: Framework/Plugins
prioridad: P2
critico: false
estimacion: L
impacto: [diferenciacion]
req: [REQ-FWK-06]
dependencias: [HU-FWK-04]
skills: ["plugin-dev", "new-pack", "adr"]
estado: terminada
---

# HU-FWK-13 · Plugin del tenant formalizado con scaffold completo

> Estado SDD: Terminada — implementada 2026-10-03.

**ID:** HU-FWK-13

**Título:** Plugin del tenant formalizado con scaffold completo

**Workstream:** Framework/Plugins

**Historia:** Como implementador quiero crear un plugin acotado a un solo negocio, con sus tablas y tareas, para resolver una necesidad particular sin tocar el core ni hacer un fork.

**Por qué importa (valor empresarial):** Es el tercer nivel del orden de personalización (invariante 2): sin él, los casos especiales terminan en forks o en tools declarativas que no alcanzan.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-FWK-06

**Dependencias:** [HU-FWK-04](../../../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md)

**Criterios de aceptación (Gherkin):**
- **Scaffold.** Dado `solvershub plugin new`, cuando lo ejecuto, entonces genera módulo, `models.py`, `jobs.py`, migraciones y tests.
- **Acotado.** Dado un plugin de negocio, cuando se instala, entonces solo se activa para ese negocio y sus tablas cumplen RLS.
- **Revisión.** Dado un plugin nuevo, cuando se despliega, entonces pasa revisión del master y los checks de invariantes.

**Evidencia / Definición de Terminado:**
- ADR del nivel "plugin del tenant"; scaffold; plugin de ejemplo.

**Implementada (2026-10-03, PR [agent-core #204](https://github.com/devrochy/agent-core/pull/204)):** ADR-0089 formaliza el nivel 3 (plugin del tenant). Scaffold `agent-core plugin scaffold <nombre> --tenant` genera `models.py` (TenantMixin + `tenant_id` + RLS + `deleted_at`), `jobs.py` (`@register_cron`), árbol Alembic propio (`version_table` separada) y tests; la migración de ejemplo nace con RLS forzada + policy + grant y pasa la guarda de invariantes. `PLUGIN-CONTRACT` distingue pack vs. plugin del tenant. Revisión del master = guarda de migraciones + `ruff` + `pytest` (el scaffold genera el test que verifica RLS).

**Riesgos/Notas:**
- —
