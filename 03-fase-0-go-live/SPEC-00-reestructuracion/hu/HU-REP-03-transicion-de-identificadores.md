---
id: HU-REP-03
titulo: Transición de identificadores rompedores con alias y ADR
spec: SPEC-00
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-REP-01]
dependencias: [HU-REP-02]
skills: ["adr", "arquitecto", "/codex:adversarial-review", "release"]
estado: borrador
---

# HU-REP-03 · Transición de identificadores rompedores con alias y ADR

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-00](../spec.md) (D-SPEC-00-2 y D-SPEC-00-3).

**ID:** HU-REP-03

**Título:** Transición de identificadores rompedores con alias y ADR

**Workstream:** Arquitectura/Prod

**Historia:** Como responsable de la plataforma quiero renombrar el CLI, la distribución, los grupos de entry points y las variables `AGENT_CORE_*` con alias temporales para completar la marca sin cortar ningún despliegue.

**Por qué importa (valor empresarial):** Termina la transición de marca sin downtime. Un cambio de nombre mal hecho puede impedir que arranquen los contenedores de producción o que corran los tests: los alias eliminan ese riesgo.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-REP-01

**Dependencias:** [HU-REP-02](HU-REP-02-renombre-cosmetico.md)

**Criterios de aceptación (Gherkin):**
- **CLI con alias.** Dado un contenedor que ejecuta `agent-core db migrate`, cuando arranca con el release nuevo, entonces funciona y registra un aviso de deprecación; `solvershub db migrate` hace lo mismo sin aviso.
- **Entry points dobles.** Dado un pack que solo declara `agent_core.plugins`, cuando arranca el core, entonces se descubre; si declara ambos grupos, se carga una sola vez.
- **Variables con respaldo.** Dado `AGENT_CORE_ROLE=worker` sin la variable nueva, cuando arranca el contenedor, entonces toma el rol `worker`.
- **Tests no saltados.** Dado el CI, cuando se renombra `AGENT_CORE_INTEGRATION`, entonces un test falla si los tests de integración no corrieron.
- **Lo intocable.** Dado los IDs `pack_*`, la base `agent_core` y los streams `agent_core:inbound[:dlq]`, cuando termina la HU, entonces siguen iguales.

**Evidencia / Definición de Terminado:**
- ADR "Transición de nombres solvershub-*" aceptado en `solvershub-core/docs/adr/`.
- Variables migradas en todas las apps de Coolify con fecha de retiro de los alias (dos releases).
- Paquete `solvershub_contracts` con re-exportación y test de importación (si se aprueba D-SPEC-00-3).

**Riesgos/Notas:**
- `@agentcore/contracts` (TypeScript) está obsoleto desde ADR-0011: se elimina.
- `COMPOSE_PROJECT_NAME` no se cambia para no dejar huérfanos los volúmenes locales.
