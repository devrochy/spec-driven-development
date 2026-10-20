---
name: ejecutar-hu
description: >
  Ejecuta una historia de usuario (HU) de solvershub-docs de punta a punta siguiendo el
  ciclo SDD. Úsala cuando se diga "trabaja la HU-XXX-NN", "implementa esta historia",
  "avancemos con la ola N" o cuando haya que retomar el plan. Lee la HU y su spec, revisa
  el DoR, carga las skills recomendadas, implementa con el DoD, cambia el estado y regenera.
---

Ejecuta una HU del backlog maestro (este repo) aplicando la [guía de ejecución](../../../07-guia-de-ejecucion.md),
sección 5. El código vive en el repo dueño; aquí solo se documenta estado y evidencia.

## Entrada

El ID de la HU (por ejemplo `HU-COM-01`) o un issue que la cite. Si no lo dan, elige la
siguiente HU de la ola actual en [03-fase-0-go-live/README.md](../../../03-fase-0-go-live/README.md).

## Pasos

1. **Leer.** Abre `03-fase-0-go-live/SPEC-*/hu/<HU>.md` y el `spec.md` de su spec.
   Anota: historia, valor empresarial, Gherkin, dependencias, REQ, repo dueño y el campo `skills`.
2. **DoR.** Verifica:
   - su spec está en `Diseño aprobado` (o superior) y no tiene decisiones ❓ que la afecten;
   - sus dependencias están `terminada` (revisa su frontmatter);
   - existe el issue en el repo dueño (si no, créalo).
   Si algo falla, **detente y dilo**; no inventes el contrato que falta.
3. **Abrir el issue** con `/work-on-issue #N` en el repo dueño. Una HU = un issue = una rama = un PR.
4. **Diseñar corto** (backend) con `backend-design:think-before-coding`; si toca capas o
   contratos, pasa el diseño por el agente `arquitecto` antes de codificar.
5. **Implementar** cargando las skills del frontmatter de la HU. Reglas duras de la
   [constitución](../../../00-constitucion.md): multi-tenant + RLS forzada, cero prompts en
   código, dinero en el servidor, sin borrado físico, contratos inmutables.
6. **Datos.** Si hay migración: `db-migration` + `backend-design:migration-safety`, revisión
   con `/backend-design:review-migration` o el agente `backend-design:schema-reviewer`.
7. **Probar.** Unitarios + integración + **aislamiento cross-tenant**; evals con `eval-author`
   si cambia la conducta del asistente.
8. **Revisar.** `/code-review`; donde hay dinero, seguridad o datos de varios negocios,
   además `/codex:adversarial-review` y el agente `auditor-multitenant`.
9. **Desplegar a test** con `desplegar-test-agent-core` (backend) o `desplegar-test` (otros
   repos) y verificar a mano cada escenario Gherkin.

## DoD (al cerrar)

- [ ] Criterios Gherkin verificados, con evidencia (PR, salida de tests o captura) escrita
  en la sección **Evidencia / Definición de Terminado** de la HU.
- [ ] ADR en el repo dueño si el cambio fue estructural.
- [ ] `ROADMAP.md`, `CHANGELOG.md` y `BACKLOG.md` del repo dueño al día.
- [ ] `estado: terminada` en el frontmatter de la HU.
- [ ] `python3 herramientas/regenerar.py` sin errores (regenera backlog, guía y enlaces).
- [ ] Fila de la HU en [08-bitacora-de-ejecucion.md](../../../08-bitacora-de-ejecucion.md)
  actualizada con PR y observaciones.

## Reglas

- Nunca marques `terminada` sin evidencia: el estado es una afirmación verificable.
- Si la HU revela una decisión nueva, regístrala en
  [decisiones.md](../../../02-vision-y-decisiones/decisiones.md) y actualiza las HU afectadas.
- Si la HU no cabe en un PR revisable, divídela en commits, **no** en HU nuevas.
- Al cerrar una spec completa, corre el ciclo de la sección 4 de la guía (verificar, recalibrar
  calendario, `regenerar.py`).

## En OpenCode

La skill funciona igual en OpenCode, siempre que se abra dentro del repo dueño de la HU
(`cd solvershub-backend && opencode`). Así carga los plugins y las skills del repo, y el plan
queda disponible como referencia `docs`. Las skills de proyecto, `desplegar-test`,
`desplegar-test-agent-core` y los agentes `arquitecto`, `auditor-multitenant` y `eval-runner`
existen con el mismo nombre. Lo que en Claude Code viene de un plugin o de un comando se usa así:

| En Claude Code | En OpenCode |
|---|---|
| Skills `backend-design:<x>`, `data:<x>` o `marketing:<x>` | La misma skill sin el prefijo: `think-before-coding`, `migration-safety`… |
| `/work-on-issue #N` | Skill `work-on-issue` |
| `/backend-design:review-migration` o agente `backend-design:schema-reviewer` | Skills `migration-safety` y `data-modeling-discipline`, más el agente `auditor-multitenant` |
| Agente `backend-design:security-reviewer` | Skill `security-discipline` |
| `/code-review` | Agente `reviewer` (global de OpenCode) |
| `/codex:adversarial-review` | No existe en OpenCode: pídelo desde Claude Code |
| Hooks: guardas, ruff y validación del plan | Plugins en `.opencode/plugins/` del backend y de este repo, que corren los mismos scripts |
