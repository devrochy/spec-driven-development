---
id: HU-BILL-10
titulo: Recargas de créditos y cierres de período
spec: SPEC-14
fase: 1
hito: "1"
workstream: Billing
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso]
req: [REQ-BILL-09, REQ-FIX-06]
dependencias: [HU-BILL-06]
skills: ["db-migration", "backend-design:idempotency-and-side-effects", "/codex:adversarial-review", "pagos-wompi"]
estado: parqueada
---

# HU-BILL-10 · Recargas de créditos y cierres de período

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-14](../spec.md) (P-07, D-SPEC-14-1).

**ID:** HU-BILL-10

**Título:** Recargas de créditos y cierres de período

**Workstream:** Billing

**Historia:** Como dueño de un negocio que se quedó sin créditos quiero comprar una recarga con un clic y seguir atendiendo para no tener que cambiar de plan por un mes de mucho movimiento.

**Por qué importa (valor empresarial):** La recarga es ingreso incremental de alto margen y evita el downgrade por miedo al bloqueo. Es el modelo de créditos que valida la matriz (Wati).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-BILL-09, REQ-FIX-06

**Dependencias:** HU-BILL-06

**Criterios de aceptación (Gherkin):**
- **Comprar.** Dado un paquete de recarga, cuando pago con Wompi, entonces los créditos se suman al saldo en cuanto se confirma el pago.
- **Orden de consumo.** Dado cupo del plan y recarga, cuando consumo, entonces primero se usa el cupo y luego la recarga.
- **Vigencia.** Dado una recarga, cuando vence según P-07, entonces su saldo deja de contar y queda registrado.
- **Cierre.** Dado el fin de un período, cuando corre el cierre, entonces queda el snapshot con cupo, recargas, consumo y saldo.

**Evidencia / Definición de Terminado:**
- Tabla `credit_topups`, cobro por `core/billing`, snapshot de cierre; tests.

**Riesgos/Notas:**
- Los paquetes respetan el mínimo de Wompi.
