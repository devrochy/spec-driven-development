---
id: HU-INMO-02
titulo: "Ubicación y respuestas de lista entrantes"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Canales y conexiones
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, diferenciacion]
req: [REQ-INMO-10]
dependencias: [HU-INMO-01]
skills: ["meta-whatsapp", "agentcore-conventions", "backend-design:security-discipline"]
estado: borrador
---

# HU-INMO-02 · Ubicación y respuestas de lista entrantes

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-02

**Título:** Ubicación y respuestas de lista entrantes

**Workstream:** Canales y conexiones

**Historia:** Como negocio quiero que el asistente reciba la ubicación que comparte el cliente y la fila de lista que elige, para no perder datos ni reinterpretar texto.

**Por qué importa (valor empresarial):** Hoy la ubicación se descarta y de una lista solo llega el título (`core/gateway/channels/whatsapp/inbound.py:76-81`). Sin esto no hay búsqueda por cercanía ni captación con pin.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-10

**Dependencias:** [HU-INMO-01](HU-INMO-01-adrs-y-dor-del-piloto.md)

**Criterios de aceptación (Gherkin):**
- **Ubicación.** Dado un cliente que comparte un pin, cuando llega el webhook, entonces el mensaje se guarda con latitud, longitud y nombre, y la acción que lo necesite lo lee con `ultima_ubicacion()` sin que el LLM copie coordenadas.
- **Alcance de la ubicación.** Dado un pin compartido en una captación hace dos días, cuando el cliente busca "cerca de mí" hoy, entonces no se usa: `ultima_ubicacion()` toma la conversación del `ToolContext`, solo mensajes entrantes y solo del episodio (≤ 24 h).
- **Fila de lista.** Dado una lista enviada por el asistente, cuando el cliente elige una fila, entonces el turno recibe el `id` de la fila además del título, como dato no confiable.
- **Bandera apagada.** Dado un negocio sin la bandera de mensajes estructurados, cuando llega una ubicación, entonces la conducta es la de hoy y solo se guarda la estructura.

**Evidencia / Definición de Terminado:**
- `inbound.py` sin descartar ubicación ni `list_reply.id`; tests con fixtures reales de Meta.
- El contrato no cambia: `LocationContent` ya existe (`packages/contracts/agentcore_contracts/contracts.py`). El pin guardado en `messages` lo cubre la supresión de [HU-INMO-09](HU-INMO-09-supresion-de-datos-del-titular.md).

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- El botón (salida, `button_reply.id` y botones de plantilla) es de [HU-AOS-09](../../SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md).
