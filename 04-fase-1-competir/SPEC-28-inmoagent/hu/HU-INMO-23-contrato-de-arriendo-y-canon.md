---
id: HU-INMO-23
titulo: "Contrato de arriendo como registro y cobro del canon"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, confianza]
req: [REQ-INMO-08]
dependencias: [HU-INMO-08, HU-INMO-11]
skills: ["pagos-wompi", "db-migration", "auditor-multitenant", "new-tool"]
estado: borrador
---

# HU-INMO-23 · Contrato de arriendo como registro y cobro del canon

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-23

**Título:** Contrato de arriendo como registro y cobro del canon

**Workstream:** Verticales

**Historia:** Como inmobiliaria que administra arriendos quiero registrar cada contrato y que el canon se cobre solo cada mes con link de pago, para dejar de perseguir pagos a mano.

**Por qué importa (valor empresarial):** El canon es el ingreso recurrente de la inmobiliaria; cobrarlo con recordatorio y link reduce la mora (D-SPEC-28-2).

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-INMO-08

**Dependencias:** [HU-INMO-08](HU-INMO-08-suscripciones-de-plazo-fijo.md), [HU-INMO-11](HU-INMO-11-inventario-y-captaciones-en-el-panel.md)

**Criterios de aceptación (Gherkin):**
- **Registro.** Dado un contrato creado en el panel con canon, día de pago e inicio, cuando se marca vigente, entonces se crea su suscripción de plazo fijo con `reference = contrato:<id>` y `autogestion=false`.
- **Link solo para el arrendatario.** Dado un cliente que pide el link del canon, cuando se llama `inmo_link_canon`, entonces solo se consideran contratos con `arrendatario_customer_id` de ese cliente, y el monto y el link salen del cargo pendiente.
- **Un contrato vigente por inmueble.** Dado un inmueble con contrato vigente, cuando se intenta registrar otro vigente, entonces se rechaza.
- **Pago.** Dado un pago confirmado, cuando llega `subscription.charge_paid`, entonces el contrato queda al día y su espejo de cargos se actualiza.

**Evidencia / Definición de Terminado:**
- Tabla `contratos` con espejo del estado de cargos alimentado por eventos (sin leer tablas de pack-subscriptions); integración con `subscription_registry`; panel de contratos.

**Riesgos/Notas:**
- Fase INMO 4 · Arriendos y medición.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- Fuera de alcance: PDF, firma y liquidación al propietario.
