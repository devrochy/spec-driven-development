---
id: HU-DS-13
titulo: Resumen móvil por rol
spec: SPEC-29
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-UX-11]
dependencias: [HU-DS-07, HU-DS-11]
skills: ["kpi-dashboard-design", "dataviz", "frontend-design"]
estado: borrador
---

# HU-DS-13 · Resumen móvil por rol

> Estado SDD: Lista para ejecutar — [SPEC-29](../spec.md) en Diseño aprobado (D-32); nace de D-34 al partir [HU-DS-11](HU-DS-11-shell-del-panel-en-la-app.md).

**ID:** HU-DS-13

**Título:** Resumen móvil por rol

**Workstream:** App móvil

**Historia:** Como dueño o supervisor que usa la app quiero un Inicio con las mismas métricas por rol que el panel para revisar el negocio desde el celular con una mano.

**Por qué importa (valor empresarial):** El Inicio de la app muestra siete cifras planas. Con el mismo Resumen por rol del panel (perfil derivado de permisos, D-SPEC-29-7), el dueño ve tendencias, alertas y acciones sin abrir la computadora.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-11

**Dependencias:** [HU-DS-07](HU-DS-07-resumen-modular-por-rol.md), [HU-DS-11](HU-DS-11-shell-del-panel-en-la-app.md)

**Criterios de aceptación (Gherkin):**
- **Resumen por rol.** Dado un supervisor de cobranza, cuando abre Inicio en la app, entonces ve los mismos widgets por defecto que su perfil en el panel.
- **Paridad de widgets.** Dado el catálogo de widgets, cuando corre el test de paridad, entonces claves, permisos y endpoints coinciden con la tabla de [SPEC-29](../spec.md).
- **Sin datos.** Dado un negocio recién creado, cuando abre Inicio, entonces cada widget sin datos muestra un estado vacío con una acción, nunca un cero sin contexto.

**Evidencia / Definición de Terminado:**
- Capturas por perfil (dueño, supervisor, operador) desde el OPPO en claro y oscuro.
- Test de paridad de widgets en el repo de la app.
- Decisión sobre TanStack Query registrada (instalarlo o enmendar ADR-APP-04).

**Riesgos/Notas:**
- Depende de los perfiles y widgets de [HU-DS-07](HU-DS-07-resumen-modular-por-rol.md) (que a su vez espera [HU-UI-07](../../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md)).
- Los gráficos usan las primitivas de [HU-DS-06](HU-DS-06-primitivas-de-visualizacion.md) con `react-native-svg`, que cambia el fingerprint: necesita una build nativa nueva.
