---
id: HU-INMO-17
titulo: "Fichas en el chat y verificación de hechos del inmueble"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, confianza]
req: [REQ-INMO-04]
dependencias: [HU-INMO-03, HU-INMO-15, HU-ARCH-29]
skills: ["new-tool", "eval-author", "meta-whatsapp"]
estado: borrador
---

# HU-INMO-17 · Fichas en el chat y verificación de hechos del inmueble

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-17

**Título:** Fichas en el chat y verificación de hechos del inmueble

**Workstream:** Verticales

**Historia:** Como cliente quiero ver la ficha del inmueble con foto, precio y cercanías, y confiar en que lo que dice el asistente es cierto.

**Por qué importa (valor empresarial):** Un precio o una distancia inventados destruyen la confianza en la inmobiliaria; el dinero y los datos salen del servidor (constitución §1.2) y los verifica el verificador del core (ADR-0119).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-04

**Dependencias:** [HU-INMO-03](HU-INMO-03-salida-interactiva.md), [HU-INMO-15](HU-INMO-15-recomendaciones-y-relajacion.md), [HU-ARCH-29](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md)

**Criterios de aceptación (Gherkin):**
- **Ficha.** Dado un inmueble elegido de la lista, cuando se pide la ficha, entonces llegan la portada, el precio, el área y las cercanías.
- **Precio inventado.** Dado una respuesta con un precio que ninguna acción del turno devolvió, cuando corre el verificador con las afirmaciones que declara el pack, entonces falla y se aplica `guardrail_fail_action`.
- **Dirección reservada.** Dado `revelar_direccion = tras_agendar` sin una visita de ese cliente, cuando se pide la ficha, entonces la acción no devuelve la dirección y las distancias van redondeadas a 100 m.

**Evidencia / Definición de Terminado:**
- Acción `inmo_ver_ficha`; afirmaciones de monto y link declaradas por el pack para [HU-ARCH-29](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md); escenarios golden de hechos.
- Sin guardrail heurístico propio (ADR-0119).

**Riesgos/Notas:**
- Fase INMO 2 · Búsqueda y geo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
