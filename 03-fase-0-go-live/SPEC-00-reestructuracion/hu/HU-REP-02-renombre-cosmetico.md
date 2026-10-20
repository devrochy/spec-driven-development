---
id: HU-REP-02
titulo: Renombre cosmético a solvershub-core y documentación correcta
spec: SPEC-00
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-REP-01]
dependencias: [HU-REP-01]
skills: ["cloudflare", "desplegar-test-agent-core", "doc-coauthoring"]
estado: borrador
---

# HU-REP-02 · Renombre cosmético a `solvershub-core` y documentación correcta

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-00](../spec.md) (D-SPEC-00-1).

**ID:** HU-REP-02

**Título:** Renombre cosmético a solvershub-core y documentación correcta

**Workstream:** Arquitectura/Prod

**Historia:** Como integrante del equipo quiero que cada repo, app de Coolify y carpeta siga la convención `solvershub-<section>` y tenga un README que diga qué es, para encontrar cualquier cosa sin preguntar.

**Por qué importa (valor empresarial):** La convención de nombres es la base de la marca técnica y de la operación: alertas, runbooks y despliegues hablan el mismo idioma. Reduce errores al operar producción.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-REP-01

**Dependencias:** [HU-REP-01](HU-REP-01-limpiar-residuos.md)

**Criterios de aceptación (Gherkin):**
- **GitHub y runner.** Dado el repo `devrochy/agent-core`, cuando se renombra a `solvershub-core`, entonces el runner `solvershub-ci` toma un PR de prueba y las URL viejas redirigen.
- **Coolify.** Dado las apps `agent-core*`, `clone-of-agent-core-test-*` y `panel-web-test`, cuando se renombran, entonces los UUID y dominios no cambian y la landing aparece en el runbook de despliegue.
- **Producción con nombre de producción (N-37).** Dado la app, el worker y el beat del entorno `production`, que en Coolify todavía se llaman `agent-core-test*`, cuando se renombran, entonces ningún recurso de producción lleva "test" en el nombre y ninguno de test lleva "clone-of".
- **Carpeta local.** Dado `solvershub/solvershub-backend`, cuando pasa a `solvershub-core`, entonces `make` y `npm run api:types` del panel siguen funcionando.
- **Enlaces.** Dado los 13 enlaces rotos a `../agent-core` en comercial, cuando se corrigen, entonces el chequeo de enlaces no reporta ninguno.
- **README por repo.** Dado cada repo `solvershub-*`, cuando se abre su README, entonces dice qué es, cómo se corre y quién es el dueño de qué tema; el del panel deja de ser el "Centro de lanzamiento" y `solvershub-apk/AGENTS.md` describe `pack_cobranza` y no NestJS.

**Evidencia / Definición de Terminado:**
- Capturas de Coolify con los nombres nuevos y del runner tomando un job.
- PR en cada repo con README actualizado; `solvershub-landing/package.json` con `name: solvershub-landing`.
- `brand/manual-de-marca.md:102,104` corregido (dominio `solvershub.site`, regla de nombres).

**Riesgos/Notas:**
- El GitHub de la APK ya pasó por un renombre (`app-cobranza-apk` → `solvershub-apk`): repetir ese procedimiento.
- Nunca cambiar `com.solvershub.apk` ni el projectId de EAS.
