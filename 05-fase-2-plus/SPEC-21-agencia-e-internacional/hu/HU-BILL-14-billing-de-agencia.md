---
id: HU-BILL-14
titulo: Billing de agencia con reventa y factura consolidada
spec: SPEC-21
fase: 2
hito: "2"
workstream: Billing
prioridad: P2
critico: false
estimacion: L
impacto: [ingreso]
req: [REQ-BILL-12]
dependencias: [HU-FWK-12, HU-BILL-10]
skills: ["backend-design:data-modeling-discipline", "adr"]
estado: parqueada
---

# HU-BILL-14 · Billing de agencia con reventa y factura consolidada

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-21](../spec.md).

**ID:** HU-BILL-14

**Título:** Billing de agencia con reventa y factura consolidada

**Workstream:** Billing

**Historia:** Como agencia quiero pagar un plan mayorista, asignar créditos a mis clientes y cobrarles con mi margen para hacer de SolversHub una línea de negocio propia.

**Por qué importa (valor empresarial):** Es lo que hace atractivo el canal de agencias: margen propio y una sola factura. Wati, Respond.io y SleekFlow no son white-label (debilidad registrada en la matriz).

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-BILL-12

**Dependencias:** [HU-FWK-12](HU-FWK-12-organizaciones-y-subcuentas.md), [HU-BILL-10](../../../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-10-recargas.md)

**Criterios de aceptación (Gherkin):**
- **Mayorista.** Dado una organización con plan de agencia, cuando asigna créditos a un negocio hijo, entonces se descuentan de su bolsa.
- **Reventa.** Dado un markup configurado, cuando la agencia cobra a su cliente, entonces el precio incluye su margen.
- **Factura.** Dado el fin de período, cuando se cierra, entonces la agencia recibe una factura consolidada.

**Evidencia / Definición de Terminado:**
- Modelo de bolsa de créditos de organización; reportes; tests.

**Riesgos/Notas:**
- —
