---
id: HU-CHAN-03
titulo: Pack de marketing con campañas, segmentos y consentimiento
spec: SPEC-17
fase: 1
hito: "1"
workstream: Canales y conexiones
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, diferenciacion, legal]
req: [REQ-COMP-03]
dependencias: [HU-ARCH-13, HU-BILL-06]
skills: ["new-pack", "plugin-dev", "marketing:campaign-plan", "meta-whatsapp"]
estado: borrador
---

# HU-CHAN-03 · Pack de marketing con campañas, segmentos y consentimiento

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-17](../spec.md) (D-SPEC-17-1).

**ID:** HU-CHAN-03

**Título:** Pack de marketing con campañas, segmentos y consentimiento

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero enviar campañas por WhatsApp a segmentos de clientes que aceptaron recibirlas, ver el costo estimado antes de enviar y medir resultados para reactivar ventas sin spam.

**Por qué importa (valor empresarial):** Las campañas son la fuente de ingreso que más rápido muestra retorno al cliente y lo que venden Interakt, Wati y ClonAI. Con consentimiento registrado se cumple la ley y las políticas de Meta.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-COMP-03

**Dependencias:** [HU-ARCH-13](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md), HU-BILL-06

**Criterios de aceptación (Gherkin):**
- **Segmento.** Dado clientes con opt-in, cuando armo un segmento (compraron hace más de 30 días, suscripción vencida), entonces veo cuántos son.
- **Costo previo.** Dado una campaña, cuando la preparo, entonces veo el costo estimado de Meta y los créditos de fee antes de enviar.
- **Envío controlado.** Dado el envío, cuando corre, entonces respeta el límite por minuto y excluye a quien hizo opt-out.
- **Resultados.** Dado una campaña enviada, cuando la abro, entonces veo entregados, leídos, respuestas y ventas atribuidas.

**Evidencia / Definición de Terminado:**
- Pack nuevo con tablas (RLS), registro de consentimiento, UI; tests.

**Riesgos/Notas:**
- Plantillas de marketing tienen otra tarifa de Meta: el costo se informa por categoría.
