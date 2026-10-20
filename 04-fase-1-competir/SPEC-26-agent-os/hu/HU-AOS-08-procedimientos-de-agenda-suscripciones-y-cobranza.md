---
id: HU-AOS-08
titulo: "Procedimientos de agenda, suscripciones (incluye cambio de plan) y cobranza"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, calidad_ia]
req: [REQ-AOS-03]
dependencias: [HU-AOS-06]
skills: ["new-pack", "new-tool", "eval-author"]
estado: terminada
---

# HU-AOS-08 · Procedimientos de agenda, suscripciones (incluye cambio de plan) y cobranza

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-08

**Título:** Procedimientos de agenda, suscripciones (incluye cambio de plan) y cobranza

**Workstream:** Agent OS

**Historia:** Como negocio con agenda, suscripciones o cobranza quiero que agendar, cambiar de plan, pagar un cargo y registrar una promesa de pago sean procedimientos tipados, para que fechas, montos y estados no dependan de la interpretación del modelo.

**Por qué importa (valor empresarial):** Cubre las otras verticales del 0A y el 0B; el cambio de plan, corregido en HU-SUB-07, pasa a ser estructural.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-03

**Dependencias:** [HU-AOS-06](HU-AOS-06-comandos-y-verificador-sobre-estado.md)

**Criterios de aceptación (Gherkin):**
- **Agendar.** Dado `agendar_demo`, cuando el cliente elige un horario no ofrecido, entonces el *resolver* lo rechaza y se ofrecen los disponibles.
- **Cambio de plan.** Dado una suscripción Basic, cuando el cliente pide Premium, entonces el precio y el prorrateo salen del catálogo del servidor (ADR-0111) y se confirma antes de cobrar.
- **Promesa de pago.** Dado un cliente con mora, cuando promete pagar el viernes, entonces la promesa se registra con fecha validada y el monto del saldo real.

**Evidencia / Definición de Terminado:**
- Procedimientos en `pack-calendar`, `pack-subscriptions` y `pack-cobranza`; escenarios simulados; journeys en verde.

**Terminada (2026-10-11):** PRs agent-core [#453](https://github.com/devrochy/agent-core/pull/453), [#455](https://github.com/devrochy/agent-core/pull/455).

**Riesgos/Notas:**
- Cobranza tiene reglas por cartera: los *resolvers* leen la configuración del pack, no del prompt.
