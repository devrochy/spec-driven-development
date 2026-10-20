---
id: HU-DS-01
titulo: Tokens v2
spec: SPEC-29
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, diferenciacion]
req: [REQ-UX-09]
dependencias: []
skills: ["frontend-design", "dataviz", "panel-ui"]
estado: terminada
---

# HU-DS-01 · Tokens v2

> Estado SDD: Terminada — implementada 2026-10-11.

**ID:** HU-DS-01

**Título:** Tokens v2

**Workstream:** UX/Onboarding

**Historia:** Como responsable del producto quiero que los tokens de marca cubran estados con contraste AA por tema, tipografía, elevación, motion, densidad y colores de datos para que el panel y la app se construyan con las mismas decisiones y nadie las invente pantalla por pantalla.

**Por qué importa (valor empresarial):** Es la base de toda la spec. Arregla el incumplimiento de contraste que hoy afecta a cada badge y a la CTA principal, y baja el costo de cada pantalla nueva de [SPEC-13](../../SPEC-13-vistas-profesionales/spec.md), 15, 16 y 18.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-09

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Estados legibles.** Dado el tema claro, cuando se genera `tokens.css`, entonces `--sh-status-{success,warning,danger}-fg` dan ≥ 4,5:1 sobre `surface` y `bg`, y lo mismo pasa en el tema oscuro.
- **CTA legible.** Dado el token `gradient-cta`, cuando se calcula el contraste del texto blanco en el inicio y en el final del degradado, entonces los dos son ≥ 4,5:1.
- **Paleta de datos validada.** Dado `data-cat-1..4` de cada tema, cuando corre `validate_palette.js` con la superficie del tema, entonces pasan las 5 verificaciones.
- **Una fuente, dos salidas.** Dado un cambio en `tokens.json`, cuando corro el build y `npm run tokens:sync` en la app, entonces `tokens.css` y `tokens.ts` traen los mismos valores para tipografía, elevación, motion y densidad.
- **Sin romper lo existente.** Dado un componente que usa un token viejo, cuando se publica v2, entonces sigue funcionando por alias y el lint avisa que está deprecado.

**Evidencia / Definición de Terminado:**
- Panel [#60](https://github.com/devrochy/solvershub-panel/pull/60) (issue #59), mergeado el 2026-10-11: `tokens.json` v1.4, `build.mjs` (CSS, Tailwind, RN y Android), ADR-0002.
- App [#148](https://github.com/devrochy/solvershub-apk/pull/148), mergeado: `tokens.ts` v1.4, `tokens:sync` a `src/core/theme` y `tokens-v2.test.ts`.
- `brand/tokens/contrast.mjs` en el job `tokens` del CI: 88 pares, 0 fallas (91 desde [HU-DS-02](HU-DS-02-contraste-aa-y-gates.md)). Prueba de mutación con los valores viejos: 7 fallas (warning 2,27:1, CTA 2,04:1).
- Paleta de datos validada con `validate_palette.js` en claro y oscuro (categórica y rampas ordinales).
- Escenario "Sin romper lo existente": ningún token cambió de valor. El lint de clases sin AA lo agregó [HU-DS-02](HU-DS-02-contraste-aa-y-gates.md).

**Riesgos/Notas:**
- Los valores exactos de estado y datos están en el design.md de [SPEC-29](../spec.md) §1; si la marca cambia, se recalculan con el mismo script.
- DTCG no tiene un tipo estándar para densidad: se modela como `dimension`.
