---
id: HU-DS-03
titulo: Kit de componentes v2 del panel y catálogo
spec: SPEC-29
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-UX-09]
dependencias: [HU-DS-01]
skills: ["frontend-design", "panel-ui", "/code-review"]
estado: terminada
---

# HU-DS-03 · Kit de componentes v2 del panel y catálogo

> Estado SDD: Terminada — implementada 2026-10-11.

**ID:** HU-DS-03

**Título:** Kit de componentes v2 del panel y catálogo

**Workstream:** UX/Onboarding

**Historia:** Como desarrollador del panel quiero un kit de átomos, moléculas, organismos y plantillas con variantes y estados documentados en un catálogo vivo para construir cada vista nueva sin decidir estilos de nuevo.

**Por qué importa (valor empresarial):** [SPEC-13](../../SPEC-13-vistas-profesionales/spec.md) tiene 10 vistas por construir. Con el kit cada una sale más rápido y todas se ven del mismo producto, que es lo que se percibe como "profesional" en una demo.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-09

**Dependencias:** [HU-DS-01](HU-DS-01-tokens-v2.md)

**Criterios de aceptación (Gherkin):**
- **Catálogo vivo.** Dado `PANEL_CATALOGO=1`, cuando abro `/catalogo`, entonces veo cada componente del kit con sus variantes y estados (default, hover, foco, deshabilitado, cargando, error) en claro y oscuro.
- **Catálogo oculto en producción.** Dado producción, cuando alguien abre `/catalogo`, entonces recibe 404.
- **Componentes nuevos.** Dado el kit, cuando lo reviso, entonces existen `Checkbox`, `Radio`, `Avatar`, `Kbd`, `Breadcrumbs`, `DropdownMenu`, `Popover`, `SearchInput`, `Sheet`, `KpiTile` y las plantillas `ListPage`, `DetailPage`, `DashboardPage` y `SettingsPage`.
- **Badge con ícono.** Dado un `Badge` con tono de estado, cuando se renderiza sin ícono, entonces el tipo de TypeScript lo rechaza.
- **DataTable v2.** Dado una `DataTable` con `density="compact"`, cuando la veo, entonces las filas miden 40 px, el encabezado queda fijo al hacer scroll y la tabla tiene estados de carga, vacío y error.

**Evidencia / Definición de Terminado:**
- Panel [#66](https://github.com/devrochy/solvershub-panel/pull/66) (issue #65), mergeado el 2026-10-11.
- `/catalogo` solo con `PANEL_CATALOGO=1` (404 si no), con cada componente en claro y oscuro lado a lado; revisado en el navegador con el build.
- Nuevos: Checkbox, RadioGroup, Avatar, Kbd, Breadcrumbs, TabLinks, DropdownMenu, Popover, SearchInput, Sheet y KpiTile; plantillas ListPage, DetailPage, DashboardPage y SettingsPage. Leads y Escalaciones migradas a ListPage.
- Badge: con tono de estado trae su ícono y `icon={null}` no compila (verificado quitando la directiva `@ts-expect-error`).
- DataTable v2: filas de 40 px en compacta, encabezado fijo con `maxHeight`, carga, error y vacío.
- `kit.test.tsx` (21 pruebas, con axe del catálogo); 234 tests en total. Arregla `cn()`, que descartaba `text-sh-*`.

**Riesgos/Notas:**
- No se migran todas las páginas en esta HU: cada vista de [SPEC-13](../../SPEC-13-vistas-profesionales/spec.md) migra la suya.
- `StatCard` queda como alias de `KpiTile` una versión.
