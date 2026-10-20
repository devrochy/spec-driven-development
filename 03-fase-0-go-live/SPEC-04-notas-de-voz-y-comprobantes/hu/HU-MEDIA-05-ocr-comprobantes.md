---
id: HU-MEDIA-05
titulo: OCR de comprobantes en la ruta financiera
spec: SPEC-04
fase: 0
hito: 0B
workstream: Multimodalidad
prioridad: P0
critico: true
estimacion: L
impacto: [ingreso, operacion]
req: [REQ-MEDIA-04]
dependencias: [HU-MEDIA-04, HU-COM-06]
skills: ["backend-design:idempotency-and-side-effects", "backend-design:security-discipline", "eval-author", "/codex:adversarial-review"]
estado: borrador
---

# HU-MEDIA-05 · OCR de comprobantes en la ruta financiera

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-04](../spec.md).

**ID:** HU-MEDIA-05

**Título:** OCR de comprobantes en la ruta financiera

**Workstream:** Multimodalidad

**Historia:** Como dueño de un negocio quiero que, cuando un cliente manda la foto de su transferencia, el sistema lea el monto y la cuenta destino, apruebe solo los que coinciden y me deje revisar el resto para cobrar por transferencia sin revisar cada foto.

**Por qué importa (valor empresarial):** La transferencia es el medio de pago dominante de los pymes y la única forma de cobrar montos bajo el mínimo de Wompi. Automatizar la conciliación quita horas de trabajo diario y es el argumento de venta más concreto para cobranza.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** L

**REQ mapeados:** REQ-MEDIA-04

**Dependencias:** [HU-MEDIA-04](HU-MEDIA-04-dispatcher-de-vision.md), [HU-COM-06](../../SPEC-09-comercio-confiable/hu/HU-COM-06-operacion-de-pagos.md)

**Criterios de aceptación (Gherkin):**
- **Aprobación automática.** Dado un pedido o cuota pendiente por transferencia y un comprobante cuyo monto coincide (± tolerancia configurable) y cuya cuenta destino es una del negocio, cuando se procesa, entonces se marca pagado, se avisa al cliente y queda en `payment_receipts` como `aprobado_auto`.
- **Revisión.** Dado un comprobante ilegible, con otro monto o con otra cuenta, cuando se procesa por segunda vez sin coincidir, entonces queda `pendiente_revision` y el negocio lo ve con la imagen y los datos leídos.
- **Nunca inventa.** Dado un campo ilegible, cuando el OCR responde, entonces el campo es nulo y nunca se aprueba.
- **Fuera del LLM.** Dado un comprobante, cuando se procesa, entonces la decisión la toma el código con los datos del OCR; el LLM conversacional solo comunica el resultado.
- **Cuotas.** Dado una cuota de cobranza o un cargo de suscripción, cuando el comprobante se aprueba, entonces se registra el pago por el mismo camino que un pago en línea.

**Evidencia / Definición de Terminado:**
- Tests con comprobantes de ejemplo; vista de revisión en el panel con aprobar y rechazar.
- Los prompts del OCR en un playbook versionado.

**Riesgos/Notas:**
- Habilita HU-SUB-13 (cobros bajo el mínimo de Wompi).
