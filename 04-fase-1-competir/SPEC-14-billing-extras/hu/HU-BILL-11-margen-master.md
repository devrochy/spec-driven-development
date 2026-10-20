---
id: HU-BILL-11
titulo: Vista de margen para la plataforma
spec: SPEC-14
fase: 1
hito: "1"
workstream: Billing
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, operacion]
req: [REQ-BILL-10]
dependencias: [HU-BILL-04]
skills: ["kpi-dashboard-design", "data:sql-queries", "data:validate-data", "panel-ui"]
estado: parqueada
---

# HU-BILL-11 · Vista de margen para la plataforma

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-14](../spec.md).

**ID:** HU-BILL-11

**Título:** Vista de margen para la plataforma

**Workstream:** Billing

**Historia:** Como master de SolversHub quiero ver por negocio, plan y modelo cuánto ingresa, cuánto cuesta y qué margen deja para ajustar precios y detectar clientes o modelos que pierden dinero.

**Por qué importa (valor empresarial):** El modelo de precios tiene 10 supuestos. Sin medición, un cambio de precio de un proveedor o un cliente atípico pueden volver negativo el margen sin que nadie lo vea.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-BILL-10

**Dependencias:** HU-BILL-04

**Criterios de aceptación (Gherkin):**
- **Tabla de margen.** Dado un período, cuando abro la vista, entonces veo por negocio ingreso, costo de proveedores, créditos vendidos y margen.
- **Por modelo.** Dado el mismo período, cuando agrupo por modelo, entonces veo cuál deja menos margen.
- **Alertas.** Dado un negocio con margen negativo dos semanas seguidas, cuando corre el reporte, entonces se alerta al master.

**Evidencia / Definición de Terminado:**
- Endpoint de plataforma y página en "Plataforma → Planes y tarifario"; tests de permisos (solo master).

**Riesgos/Notas:**
- Los costos de Meta no entran (D-06).
