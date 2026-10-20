---
id: HU-APP-01
titulo: Núcleo modular de la app
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-APP-01]
dependencias: []
skills: [adr, frontend-design]
estado: terminada
---

# HU-APP-01 · Núcleo modular de la app

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-01

**Título:** Núcleo modular de la app

**Workstream:** App móvil

**Historia:** Como desarrollador de la app oficial quiero una estructura modular (`src/modules/*` con fronteras duras, `core`, `shared`, `data` y `navigation`) verificada por un script en CI, para que la app crezca de 1 a 10 módulos sin mezclar dominios y sin romper lo existente.

**Por qué importa (valor empresarial):** La app pasa de ser el APK de cobranza a la app oficial de todo SolversHub. Sin fronteras entre módulos, el costo de cada feature nueva crece con el acoplamiento; con ellas, cada módulo del panel se agrega con riesgo acotado y el diferencial de cobranza queda protegido.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Estructura.** Dado el repo con la estructura `src/{app,core,shared,data,modules,navigation}`, cuando ejecuto `scripts/check-module-boundaries.mjs`, entonces no hay importaciones entre módulos y el check pasa en CI.
- **Movimiento sin cambio.** Dado el código actual migrado a la nueva estructura, cuando corro `npm run check`, entonces los 490 tests siguen verdes y el typecheck no reporta errores nuevos.
- **Contrato de módulo.** Dado un módulo nuevo creado con la plantilla, cuando se integra al navegador, entonces expone `navigation.tsx`, `screens/`, `features/`, `api.ts`, `repository.ts` y sus tests, y el script de fronteras lo valida.

**Evidencia / Definición de Terminado:**
- `scripts/check-module-boundaries.mjs` corriendo dentro de `scripts/check.sh` y en CI; plantilla de módulo (`docs/modulo-template.md`); ADR-APP-01..06 en `docs/adr/`; reestructura física sin cambio de comportamiento; `npm run check` en verde; tipos de API generados desde OpenAPI (`npm run api:types` con diff-check) en CI.

**Implementada (2026-10-06):** [solvershub-apk #107](https://github.com/devrochy/solvershub-apk/pull/107) — núcleo modular (router, providers, tema y arranque).

**Riesgos/Notas:**
- El movimiento es mecánico (mover archivos y ajustar imports); cualquier cambio de comportamiento en esta HU es un error. Las 3 pantallas gigantes de cobranza no se descomponen aquí (eso es [HU-APP-07](HU-APP-07-cobranza-al-nucleo-sin-regresion.md)).

**App implementada (2026-10-05):** [solvershub-apk #107](https://github.com/devrochy/solvershub-apk/pull/107) — reestructura a `src/{app,core,shared,data,modules,navigation}` con aliases `@core/@shared/@data`, `scripts/check-module-boundaries.mjs` en CI, tipos de API generados (`npm run api:types`, `schema.d.ts` commiteado con diff-check), `docs/modulo-template.md` y `AGENTS.md` §8. 498/498 tests verdes (baseline F0: 498). 114 archivos legacy exentos hasta [HU-APP-07](HU-APP-07-cobranza-al-nucleo-sin-regresion.md).
