---
id: HU-CHAN-01
titulo: Instagram y Messenger con salida
spec: SPEC-17
fase: 1
hito: "1"
workstream: Canales y conexiones
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, diferenciacion]
req: [REQ-FIX-01, REQ-COMP-01]
dependencias: [HU-CONN-08]
skills: ["deep-research", "new-tool", "backend-design:security-discipline", "meta-whatsapp"]
estado: borrador
---

# HU-CHAN-01 · Instagram y Messenger con salida

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-17](../spec.md).

**ID:** HU-CHAN-01

**Título:** Instagram y Messenger con salida

**Workstream:** Canales y conexiones

**Historia:** Como tienda de moda que vende por Instagram quiero que el asistente responda los mensajes directos de Instagram y Messenger para atender a mis clientes donde ya me escriben.

**Por qué importa (valor empresarial):** Para muchos pymes el canal de venta es Instagram, no WhatsApp. El plan Premium ya promete Instagram (`plans.py`) y la matriz lo marca como brecha frente a Respond.io y SleekFlow.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-FIX-01, REQ-COMP-01

**Dependencias:** [HU-CONN-08](../../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md)

**Criterios de aceptación (Gherkin):**
- **Conectar.** Dado una página de Facebook y una cuenta de Instagram del negocio, cuando las conecto, entonces aparecen como conexiones con su icono y su hub.
- **Responder.** Dado un mensaje directo en Instagram, cuando llega, entonces el asistente responde por Instagram respetando la ventana de 24 h.
- **Plan.** Dado un negocio Basic, cuando intenta conectar Instagram, entonces se le explica que su plan no lo incluye.

**Evidencia / Definición de Terminado:**
- Ramas `feat/instagram-connection` y `feat/messenger-connection` integradas y probadas; conexiones con `available = true`.

**Riesgos/Notas:**
- Requiere permisos de Meta adicionales en App Review.
