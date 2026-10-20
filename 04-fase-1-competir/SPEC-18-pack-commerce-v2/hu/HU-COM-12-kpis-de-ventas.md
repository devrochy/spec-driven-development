---
id: HU-COM-12
titulo: KPIs de ventas y reporte periódico al equipo
spec: SPEC-18
fase: 1
hito: "1"
workstream: Comercio y suscripciones
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-COM-07]
dependencias: [HU-COM-05]
skills: ["kpi-dashboard-design", "data:sql-queries"]
estado: parqueada
---

# HU-COM-12 · KPIs de ventas y reporte periódico al equipo

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-18](../spec.md).

**ID:** HU-COM-12

**Título:** KPIs de ventas y reporte periódico al equipo

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de una tienda quiero ver ventas, ticket promedio, conversión y productos top frente al período anterior, y recibir un resumen diario, para medir lo que el asistente vende.

**Por qué importa (valor empresarial):** El dueño renueva cuando ve ventas atribuidas al asistente. Hoy el KPI de pedidos ni siquiera pasa de 5.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-COM-07

**Dependencias:** [HU-COM-05](../../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md)

**Criterios de aceptación (Gherkin):**
- **KPIs.** Dado un período, cuando abro Ventas, entonces veo ventas, ticket promedio, conversión cotización → pedido, top productos y clientes con la variación.
- **Reporte.** Dado el reporte diario activado, cuando cierra el día, entonces el equipo recibe el resumen por su canal.

**Evidencia / Definición de Terminado:**
- Endpoint de KPIs; vista; job de reporte; tests.

**Riesgos/Notas:**
- Base para el reporte mensual ([HU-UX-07](../../../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-UX-07-reporte-mensual.md)).
