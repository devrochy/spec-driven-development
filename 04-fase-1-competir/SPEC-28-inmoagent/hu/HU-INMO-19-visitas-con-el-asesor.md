---
id: HU-INMO-19
titulo: "Visitas con el asesor del inmueble"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, operacion]
req: [REQ-INMO-06]
dependencias: [HU-INMO-06, HU-INMO-17]
skills: ["new-tool", "eval-author", "backend-design:idempotency-and-side-effects"]
estado: borrador
---

# HU-INMO-19 · Visitas con el asesor del inmueble

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-19

**Título:** Visitas con el asesor del inmueble

**Workstream:** Verticales

**Historia:** Como cliente quiero agendar la visita a un inmueble en un horario real del asesor que lo lleva, y recibir la dirección y los recordatorios, para no perder el viaje.

**Por qué importa (valor empresarial):** La visita es el paso de mayor conversión del embudo inmobiliario; agendar mal (hora ocupada, asesor equivocado) cuesta el negocio.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-06

**Dependencias:** [HU-INMO-06](HU-INMO-06-agenda-como-capacidad-del-core.md), [HU-INMO-17](HU-INMO-17-fichas-y-verificacion-de-hechos.md)

**Criterios de aceptación (Gherkin):**
- **Horarios reales.** Dado un inmueble con asesor, cuando el cliente pide visitarlo, entonces se ofrecen solo horarios libres de la agenda de ese asesor.
- **Confirmación.** Dado un horario elegido, cuando el cliente confirma (`requiresConfirmation`, y botón cuando exista [HU-AOS-09](../../SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md)), entonces quedan una visita y una cita con `referencia`, y se revela la dirección.
- **Horario o inmueble no ofrecido.** Dado un payload o una llamada con un inmueble que no se mostró o un horario que no se ofreció en esta conversación, cuando se llama la acción, entonces la acción lo rechaza.
- **Solo sus visitas.** Dado un cliente que pide reprogramar o cancelar, cuando se resuelve la visita, entonces solo se consideran visitas con `customer_id` de ese cliente.

**Evidencia / Definición de Terminado:**
- Acciones de visita sobre `SchedulingCapability`; recordatorios con pack-calendar; escenarios golden.

**Riesgos/Notas:**
- Fase INMO 3 · Captación y visitas.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
