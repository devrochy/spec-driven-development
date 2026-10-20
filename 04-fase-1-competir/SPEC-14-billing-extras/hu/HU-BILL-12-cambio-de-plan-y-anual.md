---
id: HU-BILL-12
titulo: Cambio de plan de plataforma con prorrateo y ciclo anual
spec: SPEC-14
fase: 1
hito: "1"
workstream: Billing
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso]
req: [REQ-BILL-11, REQ-ARCH-13]
dependencias: [HU-SH-04, HU-BILL-05]
skills: ["backend-design:think-before-coding", "backend-design:testing-with-discernment", "pagos-wompi"]
estado: borrador
---

# HU-BILL-12 · Cambio de plan de plataforma con prorrateo y ciclo anual

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-14](../spec.md). [SPEC-14](../spec.md) está parqueada (D-35, 2026-10-17) salvo esta HU, que se ejecuta con HU-BILL-05 sobre el catálogo de planes por agentes.

**ID:** HU-BILL-12

**Título:** Cambio de plan de plataforma con prorrateo y ciclo anual

**Workstream:** Billing

**Historia:** Como cliente de SolversHub quiero subir de plan a mitad de mes pagando solo la diferencia, o pasarme al plan anual con descuento, para crecer sin perder lo que ya pagué.

**Por qué importa (valor empresarial):** El upgrade es la principal fuente de expansión de ingreso y el plan anual adelanta 10 meses de caja. Hoy no existe ni prorrateo ni ciclo anual en el billing de plataforma.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-BILL-11, REQ-ARCH-13

**Dependencias:** [HU-SH-04](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md), HU-BILL-05

**Criterios de aceptación (Gherkin):**
- **Upgrade prorrateado.** Dado Basic a mitad de período, cuando subo a Premium, entonces pago la diferencia por los días restantes y el cupo de créditos se ajusta de inmediato.
- **Downgrade.** Dado Premium, cuando bajo a Basic, entonces el cambio ocurre en el próximo período y se me avisa de los límites que superaría.
- **Anual.** Dado un plan mensual, cuando paso a anual, entonces pago 10 meses por 12 y el período dura un año.
- **Dos canales.** Dado el cambio, cuando lo hago por el asistente o por el panel, entonces se refleja en la misma `tenant_subscriptions`.

**Evidencia / Definición de Terminado:**
- Lógica de prorrateo con tests; opción anual en el panel y en la oferta del asistente.

**Riesgos/Notas:**
- Reutiliza el cambio de plan de suscripciones (HU-SUB-07) en el tenant `solvershub`.
