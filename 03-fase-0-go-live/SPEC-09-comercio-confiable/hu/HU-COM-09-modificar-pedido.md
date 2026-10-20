---
id: HU-COM-09
titulo: Tools para cancelar y modificar un pedido
spec: SPEC-09
fase: 0
hito: 0B
workstream: Comercio y suscripciones
prioridad: P0
critico: false
estimacion: M
impacto: [operacion, calidad_ia]
req: [REQ-COM-03]
dependencias: [HU-COM-05]
skills: ["new-tool", "eval-author"]
estado: borrador
---

# HU-COM-09 · Tools para cancelar y modificar un pedido

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-09](../spec.md).

**ID:** HU-COM-09

**Título:** Tools para cancelar y modificar un pedido

**Workstream:** Comercio y suscripciones

**Historia:** Como cliente quiero cancelar mi pedido, cambiar la dirección o el método de pago y consultar el estado con la guía de envío desde el chat para resolverlo sin esperar a un humano.

**Por qué importa (valor empresarial):** Cada cambio que el asistente no puede hacer se convierte en una escalación y un humano ocupado. Son las acciones más pedidas después de comprar; `agent-sale` ya las tenía y el pack no las portó.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-COM-03

**Dependencias:** [HU-COM-05](HU-COM-05-estados-del-pedido.md)

**Criterios de aceptación (Gherkin):**
- **Cancelar.** Dado un pedido no pagado, cuando el cliente confirma explícitamente que quiere cancelar, entonces se cancela y se libera el stock; si ya está pagado, queda "cancelación pendiente de aprobación" y se crea una escalación.
- **Cambiar dirección.** Dado un pedido no despachado, cuando el cliente da otra dirección, entonces se actualiza (y la tarifa si cambia la zona) y se guarda para el futuro solo con consentimiento.
- **Cambiar método de pago.** Dado un pedido online pendiente, cuando el cliente prefiere transferencia, entonces se expira el link y se envían los datos de transferencia.
- **Estado con guía.** Dado un pedido despachado con guía, cuando el cliente pregunta, entonces recibe estado, transportadora, número de guía y tiempo estimado.

**Evidencia / Definición de Terminado:**
- Tools con `status` de listas cerradas y `requiresConfirmation` donde aplica; escenarios en el golden set.

**Riesgos/Notas:**
- Registrar la guía desde el panel es parte de [HU-COM-05](HU-COM-05-estados-del-pedido.md) (transición a `en_camino`).
- Nota del ciclo de pruebas 2026-10-13 (Cancelar o modificar un pedido): «Hay que mejorar un poco la interacción del agente». Se toma aquí ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)): con las tools de cancelar y modificar, el agente confirma el cambio con el cliente antes de aplicarlo y le dice qué pasó.
