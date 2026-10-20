---
id: HU-APP-19
titulo: "Cobranza admin profunda móvil"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, diferenciacion]
req: [REQ-APP-07]
dependencias: [HU-APP-18]
skills: [frontend-design, panel-ui]
estado: terminada
---

# HU-APP-19 · Cobranza admin profunda móvil

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-19

**Título:** Cobranza admin profunda móvil

**Workstream:** App móvil

**Historia:** Como dueño de un negocio con cobranza quiero administrar la profundidad del pack desde la app (detalle de cartera con caja, liquidaciones y ruta del día optimizable, reportes consolidados, monitoreo del asistente, reglas de negociación y alertas de acceso), para que la app sea una réplica total del pack sin volver al escritorio.

**Por qué importa (valor empresarial):** Cierra lo que [HU-APP-18](HU-APP-18-cobranza-admin-movil.md) dejó fuera de la réplica (notas de riesgo). La caja, la liquidación y la optimización de ruta son las operaciones diarias de mayor frecuencia del dueño de cobranza; reportes, monitoreo, reglas y alertas son los controles que hoy exigen escritorio.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-18](HU-APP-18-cobranza-admin-movil.md)

**Criterios de aceptación (Gherkin):**
- **Detalle de cartera.** Dado un dueño, cuando abre una cartera, entonces ve la caja (saldo) y la ruta del día con sus clientes, y puede abrir/cerrar/ajustar/inyectar caja con confirmación y optimizar la ruta.
- **Liquidación.** Dado un dueño, cuando liquida una cartera por período, entonces la acción se confirma y la caja se refresca.
- **Reportes.** Dado un dueño, cuando abre Reportes, entonces ve el consolidado por cartera (clientes, préstamos, saldo, vencidas, cobrado, caja, gastos).
- **Monitoreo y reglas.** Dado un dueño, cuando abre Monitoreo, entonces ve KPIs y últimas promesas del asistente; cuando edita y guarda las Reglas, entonces el pack persiste los cambios.
- **Alertas.** Dado un dueño, cuando abre Alertas, entonces ve intentos de acceso con los críticos resaltados.

**Evidencia / Definición de Terminado:**
- `CarteraDetalleScreen` (caja con modal valor+motivo, liquidar, ruta+optimizar) y segmentos Carteras/Reportes/Monitoreo/Reglas/Alertas gated por permisos; contratos verificados contra el OpenAPI (`cash/*`, `liquidations`, `route(/optimize)`, `reports`, `monitoring`, `rules`, `alerts`); 8 tests nuevos.

**Implementada (2026-10-06):** [solvershub-apk #125](https://github.com/devrochy/solvershub-apk/pull/125) — detalle de cartera con caja y ruta optimizable, liquidaciones, y 5 segmentos nuevos con gating por permisos. 618/618 tests.

**Riesgos/Notas:**
- La optimización de ruta depende del servicio de mapa del pack; si no hay direcciones cargadas el plan se devuelve sin cambios.
