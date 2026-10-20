---
id: HU-COM-05
titulo: Máquina de estados del pedido con avisos y eventos
spec: SPEC-09
fase: 0
hito: 0B
workstream: Comercio y suscripciones
prioridad: P0
critico: false
estimacion: M
impacto: [operacion, confianza]
req: [REQ-COM-03]
dependencias: [HU-ARCH-13, HU-SUB-03, HU-COM-04]
skills: ["backend-design:data-modeling-discipline", "backend-design:idempotency-and-side-effects", "db-migration"]
estado: borrador
---

# HU-COM-05 · Máquina de estados del pedido con avisos y eventos

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-09](../spec.md).

**ID:** HU-COM-05

**Título:** Máquina de estados del pedido con avisos y eventos

**Workstream:** Comercio y suscripciones

**Historia:** Como cliente de un restaurante quiero saber cuándo mi pedido está en preparación, listo o en camino, y como cocina quiero enterarme de cada pedido nuevo o pagado para operar sin preguntar por WhatsApp a cada rato.

**Por qué importa (valor empresarial):** "¿Dónde está mi pedido?" es la consulta más repetida de un restaurante. Avisar cada cambio de estado la elimina y alertar al equipo acelera la cocina. Hoy cualquier estado pasa a cualquier otro sin aviso (D9).

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-COM-03

**Dependencias:** [HU-ARCH-13](../../SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md), HU-SUB-03, [HU-COM-04](HU-COM-04-barrido-de-defectos.md)

**Criterios de aceptación (Gherkin):**
- **Transiciones válidas.** Dado un pedido `entregado`, cuando el panel intenta pasarlo a `nuevo`, entonces se rechaza; las transiciones permitidas son configurables por negocio.
- **Aviso al cliente.** Dado un pedido que pasa a `en_camino`, cuando cambia, entonces el cliente recibe el aviso con el texto del negocio (plantilla si la ventana está cerrada).
- **Alerta al equipo.** Dado un pedido nuevo o pagado, cuando ocurre, entonces los colaboradores con permiso de pedidos reciben la alerta.
- **Eventos.** Dado cada cambio, cuando se guarda, entonces se emite `order.*` por el outbox.
- **Cancelar libera stock.** Dado un pedido cancelado, cuando se cancela, entonces el stock vuelve.

**Evidencia / Definición de Terminado:**
- Tabla de transiciones por negocio; eventos `order.*` documentados; tests.

**Riesgos/Notas:**
- Las notificaciones al equipo por la campana del panel llegan con [HU-UI-13](../../../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-13-cuenta-y-notificaciones.md); aquí basta WhatsApp o correo.
