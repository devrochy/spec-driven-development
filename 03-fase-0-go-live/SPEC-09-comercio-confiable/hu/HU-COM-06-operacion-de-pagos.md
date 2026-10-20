---
id: HU-COM-06
titulo: Operación de pagos manuales y comprobantes
spec: SPEC-09
fase: 0
hito: 0B
workstream: Comercio y suscripciones
prioridad: P0
critico: false
estimacion: M
impacto: [ingreso, operacion]
req: [REQ-COM-03]
dependencias: [HU-COM-05]
skills: ["backend-design:auth-and-authorization", "frontend-design", "pagos-wompi", "panel-ui"]
estado: borrador
---

# HU-COM-06 · Operación de pagos manuales y comprobantes

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-09](../spec.md).

**ID:** HU-COM-06

**Título:** Operación de pagos manuales y comprobantes

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de un negocio que cobra por transferencia quiero marcar un pedido como pagado o rechazado desde el panel, con el comprobante adjunto, y que el cliente reciba el aviso, para cerrar las ventas que no pasan por Wompi.

**Por qué importa (valor empresarial):** La transferencia domina en los pymes colombianos y hoy un pedido por transferencia nunca puede marcarse pagado: queda `pendiente` para siempre. Sin esto, el negocio lleva sus ventas en otra parte.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-COM-03

**Dependencias:** [HU-COM-05](HU-COM-05-estados-del-pedido.md)

**Criterios de aceptación (Gherkin):**
- **Marcar pagado.** Dado un pedido por transferencia pendiente, cuando el operador lo marca pagado con confirmación, entonces el pago queda registrado con el usuario y el cliente recibe la confirmación.
- **Rechazar.** Dado un comprobante inválido, cuando el operador rechaza, entonces el cliente recibe el aviso con el motivo y el pedido sigue pendiente.
- **Comprobante adjunto.** Dado una imagen enviada por el cliente con un pago pendiente, cuando llega, entonces se adjunta al pedido para revisarla en el panel.
- **Permisos.** Dado un colaborador sin permiso de pagos, cuando abre el pedido, entonces no ve las acciones de pago.

**Evidencia / Definición de Terminado:**
- Endpoints con permisos y auditoría; vista en el detalle del pedido; tests.

**Riesgos/Notas:**
- La conciliación automática con OCR es [HU-MEDIA-05](../../SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-05-ocr-comprobantes.md), que depende de esta.
