---
id: HU-COM-10
titulo: Proactividad de ventas v2
spec: SPEC-18
fase: 1
hito: "1"
workstream: Comercio y suscripciones
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso]
req: [REQ-COM-06]
dependencias: [HU-COM-05, HU-ARCH-13]
skills: ["backend-design:idempotency-and-side-effects", "marketing:email-sequence", "eval-author"]
estado: parqueada
---

# HU-COM-10 · Proactividad de ventas v2

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-18](../spec.md).

**ID:** HU-COM-10

**Título:** Proactividad de ventas v2

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de una tienda quiero que el asistente expire pedidos impagos liberando stock, recuerde transferencias pendientes, retome cotizaciones frías y pregunte cómo le fue al cliente para recuperar ventas y mejorar el servicio sin hacerlo a mano.

**Por qué importa (valor empresarial):** Cada recordatorio bien hecho recupera ventas que hoy se pierden en silencio, y la encuesta da el CSAT que pide el dashboard de calidad. `agent-sale` ya lo hacía.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-COM-06

**Dependencias:** [HU-COM-05](../../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md), [HU-ARCH-13](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md)

**Criterios de aceptación (Gherkin):**
- **Expiración.** Dado un pedido online impago por N días (configurable), cuando corre el job, entonces se expira, se libera el stock y se avisa al cliente.
- **Transferencia.** Dado un pedido por transferencia sin comprobante en 24 h, cuando corre el job, entonces se recuerda una vez.
- **Reenganche.** Dado una cotización de hace 3 días sin pedido, cuando corre el job, entonces se envía una plantilla de reenganche configurable.
- **Encuesta.** Dado un pedido entregado, cuando pasan X horas, entonces se pide una calificación de 1 a 5 y, si es ≥4, se ofrece el enlace de reseña.

**Evidencia / Definición de Terminado:**
- Jobs con tests de reloj; textos en la config; resultados en el dashboard.

**Riesgos/Notas:**
- Cada plantilla consume fee y costo de Meta: los textos de la config lo advierten.
