---
id: HU-ARCH-17
titulo: Golden set de cobranza
spec: SPEC-02
fase: 0
hito: 0B
workstream: Comercio y suscripciones
prioridad: P0
critico: true
estimacion: L
impacto: [calidad_ia, ingreso]
req: [REQ-ARCH-10]
dependencias: [HU-ARCH-13, HU-FWK-01, HU-SUB-12]
skills: ["eval-author", "eval-runner"]
estado: borrador
---

# HU-ARCH-17 · Golden set de cobranza

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-02](../spec.md).

**ID:** HU-ARCH-17

**Título:** Golden set de cobranza

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de una cartera de cobranza quiero que el asistente esté probado en conversaciones de saldo, negociación, promesas y pago para delegarle el cobro sin miedo a que prometa lo que no debe.

**Por qué importa (valor empresarial):** Cobranza es el vertical diferencial (casi nadie en la matriz lo tiene con APK). Un asistente que concede descuentos indebidos o registra promesas falsas cuesta dinero directo al cliente.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** L

**REQ mapeados:** REQ-ARCH-10

**Dependencias:** [HU-ARCH-13](HU-ARCH-13-plantillas-fuera-de-24h.md), [HU-FWK-01](../../SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md), HU-SUB-12

**Criterios de aceptación (Gherkin):**
- **Cobertura.** Dado el golden set de cobranza, cuando se revisa, entonces tiene al menos 15 journeys: saldo, estado de cuenta, negociación dentro y fuera de reglas, promesa de pago, abono, link de pago, mora con plantilla, cliente agresivo, solicitud de humano y suscripción.
- **Umbral.** Dado el nightly, cuando corre 3 noches seguidas, entonces el pase es ≥95 %.
- **Guardrail de promesas.** Dado un intento de registrar una promesa sin fecha o fuera de política, cuando el asistente lo afirma, entonces el guardrail lo bloquea y el journey lo verifica.

**Evidencia / Definición de Terminado:**
- Escenarios en `evals/` con gate en CI y reporte de 3 noches.

**Riesgos/Notas:**
- `playbooks/seguimiento-cobranza.md:6-8` dice que "el sistema envía recordatorios por cron" y no existe: se corrige o se implementa con HU-SUB-05.
