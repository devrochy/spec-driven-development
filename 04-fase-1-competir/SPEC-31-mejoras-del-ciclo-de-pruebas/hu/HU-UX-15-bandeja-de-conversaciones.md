---
id: HU-UX-15
titulo: Bandeja de conversaciones en vivo estilo WhatsApp Web
spec: SPEC-31
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion, confianza]
req: [REQ-UX-18]
dependencias: [HU-UX-16, HU-UX-17]
skills: ["panel-ui", "frontend-design", "backend-design:query-discipline", "backend-design:performance-and-scaling", "auditor-multitenant"]
estado: borrador
---

# HU-UX-15 · Bandeja de conversaciones en vivo estilo WhatsApp Web

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-UX-15

**Título:** Bandeja de conversaciones en vivo estilo WhatsApp Web

**Workstream:** UX/Onboarding

**Historia:** Como dueño o colaborador quiero ver mis conversaciones como en WhatsApp Web, con los mensajes llegando solos, la conexión de cada chat y la posibilidad de tomar, resolver o devolver una conversación al agente, para atender sin refrescar ni saltar de página.

**Por qué importa (valor empresarial):** Es la vista que más se usa y la que el dueño comparó con agent-sale y con WhatsApp Web. Ver al agente trabajar en vivo y poder intervenir es lo que da confianza para publicar un agente (D-35).

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-18

**Dependencias:** [HU-UX-16](HU-UX-16-clientes-estilo-agent-sale.md), [HU-UX-17](HU-UX-17-motivos-de-escalacion-legibles.md)

**Criterios de aceptación (Gherkin):**
- **Dos columnas.** Dado la sección Conversaciones en escritorio, cuando la abro, entonces veo la lista de chats a la izquierda (nombre, último mensaje, hora, conexión y estado) y el hilo del chat elegido a la derecha.
- **Mensaje en vivo.** Dado un chat abierto, cuando el cliente escribe por WhatsApp o por el chat web, entonces el mensaje aparece en el hilo en 5 segundos o menos sin refrescar y el chat sube en la lista.
- **Conexión de cada chat.** Dado un negocio con dos conexiones de WhatsApp, cuando miro la lista, entonces cada chat dice por qué conexión llegó y puedo filtrar por una conexión.
- **Tomar y devolver.** Dado un chat escalado, cuando lo tomo, entonces el agente queda pausado en esa conversación, aparece la caja para responder, y cuando lo devuelvo al agente la caja desaparece y el agente vuelve a responder.
- **Lo que hizo el agente.** Dado un hilo, cuando el agente usó una herramienta, entonces veo la llamada plegada en el hilo, y en la cabecera veo el costo y los tokens de la conversación.
- **Notas internas.** Dado un chat, cuando escribo una nota interna, entonces queda visible para el equipo junto a las notas del agente y nunca le llega al cliente.
- **Celular.** Dado el panel en el celular, cuando elijo un chat, entonces veo solo el hilo con un botón para volver a la lista.

**Evidencia / Definición de Terminado:**
- Panel `app/(app)/conversaciones`: lista e hilo en dos columnas con `?c=<id>`, reusando `MessageThread`, `ConversationActions`, `components/domain/channel-icon.tsx` y la ficha del cliente de [HU-UX-16](HU-UX-16-clientes-estilo-agent-sale.md).
- Polling con `document.visibilityState`: hilo cada 3–5 s con `?after=`, lista cada 10–15 s (D-SPEC-31-1); test con timers falsos.
- Core `core/api/routers/conversations.py`: `last_message`, `last_message_at`, conexión (`label` y proveedor), orden por actividad, `?connection_id=`; `GET /admin/conversations/{id}/messages?after=`; `ConversationDetail` con la escalación activa y `state.notes`; tomar y devolver al bot con `Escalation.assigned_admin_id`; notas de personas con `source="human"`. Tests de API y de aislamiento.
- Índice `(conversation_id, created_at)` en `messages` verificado o creado.
- Captura de la bandeja con dos conexiones y medición de la demora de un mensaje entrante en test.

**Riesgos/Notas:**
- Notas que lo motivan: ítems 1 y 2 del [inventario de SPEC-31](../design.md#inventario); diseño tomado de agent-sale (`src/admin/adminPanel.ts:3714-3951`), que no tiene tiempo real.
- [HU-AOS-28](../../SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md) queda con el depurador; su nota de conversación en vivo pasa aquí.
- SSE queda como mejora si el polling pesa (D-SPEC-31-1).
