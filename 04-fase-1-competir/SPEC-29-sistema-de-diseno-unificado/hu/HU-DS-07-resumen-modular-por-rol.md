---
id: HU-DS-07
titulo: Resumen modular por rol
spec: SPEC-29
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, diferenciacion]
req: [REQ-UX-11]
dependencias: [HU-DS-03, HU-DS-06, HU-UI-07]
skills: ["kpi-dashboard-design", "dataviz", "frontend-design", "panel-ui"]
estado: borrador
---

# HU-DS-07 · Resumen modular por rol

> Estado SDD: Lista para ejecutar — [SPEC-29](../spec.md) en Diseño aprobado (D-32).

**ID:** HU-DS-07

**Título:** Resumen modular por rol

**Workstream:** UX/Onboarding

**Historia:** Como dueño, supervisor u operador quiero un Resumen que muestre mis métricas, comparadas con el período anterior, con alertas y acciones a mano, para saber en segundos si mi parte del negocio va bien y qué hacer.

**Por qué importa (valor empresarial):** El dueño renueva cuando ve el valor cada semana. Un Resumen por rol también vende el plan a supervisores y operadores, que hoy ven métricas que no son suyas.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-11

**Dependencias:** [HU-DS-03](HU-DS-03-kit-de-componentes-panel.md), [HU-DS-06](HU-DS-06-primitivas-de-visualizacion.md), [HU-UI-07](../../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md)

**Criterios de aceptación (Gherkin):**
- **Perfil por permisos.** Dado un colaborador que solo tiene `conversations` y `escalations`, cuando entra al Resumen, entonces ve el perfil Operador y ningún widget de costos, plan ni packs.
- **Comparativa.** Dado el período "7 días", cuando veo un KPI, entonces muestra el valor, el delta escrito contra los 7 días anteriores con flecha y una sparkline.
- **Polaridad.** Dado el KPI "Clientes en mora" subiendo, cuando lo veo, entonces el delta se marca como desfavorable aunque el número suba.
- **Falla aislada.** Dado que falla el endpoint de cobranza, cuando cargo el Resumen, entonces solo ese widget muestra el error con "Reintentar" y el resto carga.
- **Vacío con acción.** Dado un negocio sin WhatsApp conectado, cuando veo el widget de conversaciones, entonces me invita a conectarlo con un enlace a Conexiones.
- **KPI que lleva a la lista.** Dado el KPI "Por atender", cuando lo pulso, entonces llego a la lista filtrada correspondiente.

**Evidencia / Definición de Terminado:**
- Capturas de los tres perfiles en claro y oscuro, en escritorio y celular.
- Test de la derivación de perfil desde permisos (owner, master, supervisor, operador).
- `web-perf`: LCP ≤ 2,5 s en test.

**Riesgos/Notas:**
- Depende de que [HU-UI-07](../../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) entregue `GET /admin/dashboard?period=` con series y comparación.
- La lista de widgets y permisos es la tabla de design.md §4: la app ([HU-DS-11](HU-DS-11-shell-del-panel-en-la-app.md)) la replica con un test de paridad.
