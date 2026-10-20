---
id: HU-DS-06
titulo: Primitivas de visualización de datos
spec: SPEC-29
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion]
req: [REQ-UX-09]
dependencias: [HU-DS-01]
skills: ["dataviz", "frontend-design", "panel-ui"]
estado: en-curso
---

# HU-DS-06 · Primitivas de visualización de datos

> Estado SDD: Lista para ejecutar — [SPEC-29](../spec.md) en Diseño aprobado (D-32).

**ID:** HU-DS-06

**Título:** Primitivas de visualización de datos

**Workstream:** UX/Onboarding

**Historia:** Como desarrollador quiero sparkline, línea/área, barras y anillo de progreso accesibles, con la misma geometría en el panel y en la app, para mostrar tendencias sin traer una librería pesada.

**Por qué importa (valor empresarial):** Las tendencias son lo que convierte el Resumen en una razón para renovar. Hacerlas una vez con las reglas de dataviz evita dos estilos y unos 100 KB de JS.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-09

**Dependencias:** [HU-DS-01](HU-DS-01-tokens-v2.md)

**Criterios de aceptación (Gherkin):**
- **Formas.** Dado el kit, cuando lo reviso, entonces existen `Sparkline`, `LineChart` (con área opcional), `BarChart` y `ProgressRing` en el panel (`components/dataviz`) y en la app (`src/shared/dataviz`).
- **Tabla alternativa.** Dado un `LineChart`, cuando pulso "Ver tabla", entonces veo los mismos datos en una tabla con encabezados.
- **Hover y teclado.** Dado un `LineChart` en el panel, cuando paso el puntero o muevo las flechas con el foco en el gráfico, entonces aparece un crosshair con el valor y la fecha, y se anuncia.
- **Colores por entidad.** Dado un gráfico de 3 series, cuando filtro una, entonces las otras dos conservan su color.
- **Un solo eje.** Dado dos medidas de escala distinta, cuando se piden juntas, entonces la API del componente no permite un segundo eje Y.

**Evidencia / Definición de Terminado:**
- Página de `/catalogo` con cada forma en claro y oscuro.
- Tests de las funciones de escala compartidas (mismos casos en los dos repos).
- Revisión contra `references/anti-patterns.md` de la skill dataviz.

**Riesgos/Notas:**
- `react-native-svg` es una dependencia nueva de la app (soportada por Expo).
- ADR-0002 del panel registra D-SPEC-29-2.
