---
id: HU-SUB-17
titulo: Débito recurrente automático en el contrato de suscripción
spec: SPEC-21
fase: 2
hito: "2"
workstream: Comercio y suscripciones
prioridad: P2
critico: false
estimacion: L
impacto: [ingreso]
req: [REQ-SUB-07]
dependencias: [HU-SUB-15]
skills: ["deep-research", "backend-design:security-discipline", "backend-design:idempotency-and-side-effects", "pagos-wompi"]
estado: parqueada
---

# HU-SUB-17 · Débito recurrente automático en el contrato de suscripción

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-21](../spec.md).

**ID:** HU-SUB-17

**Título:** Débito recurrente automático en el contrato de suscripción

**Workstream:** Comercio y suscripciones

**Historia:** Como cliente de un negocio con mensualidad quiero inscribir mi tarjeta una vez y que me cobren solo cada período para no tener que pagar un link cada mes.

**Por qué importa (valor empresarial):** El cobro automático es lo que más reduce la mora en suscripciones. Hoy todo cobro es por link y depende de que el cliente pague a tiempo.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-SUB-07

**Dependencias:** HU-SUB-15

**Criterios de aceptación (Gherkin):**
- **Inscripción.** Dado un cliente, cuando inscribe su tarjeta con el proveedor, entonces la suscripción queda con cobro automático (sin guardar datos de tarjeta en SolversHub).
- **Cobro.** Dado el inicio de un período, cuando se cobra, entonces el resultado actualiza el cargo por el mismo contrato.
- **Falla.** Dado un cobro rechazado, cuando ocurre, entonces entra al flujo de mora con link de respaldo.

**Evidencia / Definición de Terminado:**
- Operación `auto_charge` en el contrato; integración con el proveedor; tests.

**Riesgos/Notas:**
- Requiere un proveedor con tokenización y cumplimiento PCI del lado del proveedor.
