---
id: HU-BILL-13
titulo: Cobro internacional en USD
spec: SPEC-21
fase: 2
hito: "2"
workstream: Billing
prioridad: P2
critico: false
estimacion: L
impacto: [ingreso]
req: [REQ-BILL-12]
dependencias: [HU-BILL-12]
skills: ["deep-research", "adr", "backend-design:idempotency-and-side-effects"]
estado: parqueada
---

# HU-BILL-13 · Cobro internacional en USD

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-21](../spec.md).

**ID:** HU-BILL-13

**Título:** Cobro internacional en USD

**Workstream:** Billing

**Historia:** Como negocio fuera de Colombia quiero pagar mi plan en dólares con tarjeta internacional para usar SolversHub desde mi país.

**Por qué importa (valor empresarial):** Abre mercados (LATAM, hispanos en EE. UU.) donde compiten Lety y Darwin AI, con precios en USD que no dependen de la TRM.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-BILL-12

**Dependencias:** [HU-BILL-12](../../../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-12-cambio-de-plan-y-anual.md)

**Criterios de aceptación (Gherkin):**
- **Precios en USD.** Dado un negocio con país fuera de Colombia, cuando ve los planes, entonces ve precios en USD.
- **Proveedor.** Dado el pago, cuando lo hace, entonces se procesa con un proveedor internacional a través de la misma capacidad de billing.
- **Créditos.** Dado un negocio en USD, cuando consume, entonces sus créditos se calculan con la misma fórmula sin TRM.

**Evidencia / Definición de Terminado:**
- Segundo proveedor de billing; catálogo multimoneda; tests.

**Riesgos/Notas:**
- Implicaciones tributarias por país: revisión legal.
