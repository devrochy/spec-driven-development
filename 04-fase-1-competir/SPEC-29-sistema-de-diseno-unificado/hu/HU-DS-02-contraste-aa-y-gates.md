---
id: HU-DS-02
titulo: Contraste AA y gates del sistema de diseño
spec: SPEC-29
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, legal]
req: [REQ-UX-09, REQ-UX-06]
dependencias: [HU-DS-01, HU-UI-04]
skills: ["panel-ui", "web-perf", "/code-review"]
estado: terminada
---

# HU-DS-02 · Contraste AA y gates del sistema de diseño

> Estado SDD: Terminada — implementada 2026-10-11.

**ID:** HU-DS-02

**Título:** Contraste AA y gates del sistema de diseño

**Workstream:** UX/Onboarding

**Historia:** Como responsable del producto quiero que el CI rechace un cambio que rompa el contraste, use un color suelto o meta una violación grave de accesibilidad para que la calidad visual no dependa de la memoria de quien revisa.

**Por qué importa (valor empresarial):** WCAG 2.2 AA es requisito en licitaciones y en el documento de seguridad enterprise. Hoy hay 135 textos de estado bajo AA en el panel y 48 archivos de la app con colores sueltos; sin un gate la deriva vuelve.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-09, REQ-UX-06

**Dependencias:** [HU-DS-01](HU-DS-01-tokens-v2.md), [HU-UI-04](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md)

**Criterios de aceptación (Gherkin):**
- **Estados migrados.** Dado el panel, cuando busco `text-success`, `text-warning` o `text-danger` en `components` y `app`, entonces no hay ninguno y todos usan `text-status-*-fg`.
- **Contraste en CI.** Dado un PR que cambia `tokens.json`, cuando un par texto/fondo del catálogo de pares baja de 4,5:1 (o de 3:1 en no-texto), entonces el CI falla y dice qué par.
- **Sin hex sueltos en la app.** Dado un PR de la app, cuando un `.tsx` fuera de `src/core/theme` usa un hex o `shColor.*` directo, entonces el lint falla.
- **Axe sin graves.** Dado `/catalogo` y las 10 páginas principales del panel en claro y oscuro, cuando corre axe en el CI, entonces no hay violaciones `serious` ni `critical`.
- **DESIGN.md v2.** Dado el repo del panel y el de la app, cuando abro su `DESIGN.md`, entonces describe los tokens v2, los estados de interacción y las reglas de esta spec.

**Evidencia / Definición de Terminado:**
- Panel [#64](https://github.com/devrochy/solvershub-panel/pull/64) (issue #63): 136 textos de estado, 13 tintes, 11 bordes y 22 enlaces migrados; botones `default`, `accent` y `danger` corregidos (de 4,497, 2,04 y 4,38:1 a ≥ 5,39:1); indicadores no textuales con `*-focus`; regla `no-restricted-syntax` contra clases sin AA (probada con un archivo de prueba).
- `contrast.mjs`: 91 pares, 0 fallas, incluido el blanco sobre los rellenos de botón.
- App [#152](https://github.com/devrochy/solvershub-apk/pull/152): `colores-sueltos.test.ts` con `colores-pendientes.json`, que solo puede bajar (44/280 al crearla; 19/67 después de [HU-DS-10](HU-DS-10-cobranza-de-campo-con-el-kit.md)). Prueba de mutación hecha.
- Axe sin violaciones graves en las 10 páginas principales ([HU-UI-04](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md)) y en `/catalogo` ([HU-DS-03](HU-DS-03-kit-de-componentes-panel.md), panel #66). En jsdom axe no mide contraste: lo cubre `contrast.mjs`.
- `DESIGN.md` v2 en el panel y `DESIGN.md` nuevo en la app.

**Riesgos/Notas:**
- La migración de los 48 archivos de la app se puede hacer junto con [HU-DS-10](HU-DS-10-cobranza-de-campo-con-el-kit.md) y [HU-DS-11](HU-DS-11-shell-del-panel-en-la-app.md); mientras tanto, el lint arranca en `warn` con una lista de excepciones que solo puede bajar.
