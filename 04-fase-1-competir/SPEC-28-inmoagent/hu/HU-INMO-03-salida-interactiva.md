---
id: HU-INMO-03
titulo: "Listas, ubicación e imágenes salientes"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Canales y conexiones
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, calidad_ia]
req: [REQ-INMO-10]
dependencias: [HU-INMO-01]
skills: ["meta-whatsapp", "agentcore-conventions", "new-tool"]
estado: borrador
---

# HU-INMO-03 · Listas, ubicación e imágenes salientes

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-03

**Título:** Listas, ubicación e imágenes salientes

**Workstream:** Canales y conexiones

**Historia:** Como negocio quiero que el asistente responda con listas, ubicación e imágenes que arma el servidor, para que elegir sea un toque y no un texto ambiguo.

**Por qué importa (valor empresarial):** Hoy solo salen texto, una imagen por turno (`core/orchestrator/safe_renderer.py`) y plantillas. La lista muestra 5 inmuebles en un solo mensaje, más barato que 5 tarjetas.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-10

**Dependencias:** [HU-INMO-01](HU-INMO-01-adrs-y-dor-del-piloto.md)

**Criterios de aceptación (Gherkin):**
- **Lista desde una acción.** Dado una acción que devuelve `_interactive` con 5 filas, cuando cierra el turno, entonces se envía una lista de WhatsApp con esas filas, y el LLM nunca escribe los ids.
- **Ids opacos.** Dado una lista de inmuebles, cuando se arma, entonces cada fila lleva un índice de la lista guardada para esa conversación (`inm:3`), no el uuid.
- **Ubicación.** Dado una visita confirmada del cliente, cuando la acción devuelve `_location`, entonces el cliente recibe la ubicación nativa del inmueble.
- **Fuera de 24 h o sin listas.** Dado la ventana cerrada o el chat web, cuando hay un extra interactivo, entonces no se envía fuera de la ventana y en el chat web se degrada a texto numerado con el mismo índice.

**Evidencia / Definición de Terminado:**
- Adaptador de salida con listas, ubicación y varias imágenes; `TurnResult` (interno) ampliado; tests.
- El contrato no cambia: `InteractiveContent` y `LocationContent` ya existen y `OutboundMessage` los admite.

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- El botón de confirmación es de [HU-AOS-09](../../SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md); esta HU reutiliza su adaptador.
