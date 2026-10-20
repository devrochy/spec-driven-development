---
id: HU-AOS-49
titulo: Pack de conocimiento con documentos por agente
spec: SPEC-31
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [calidad_ia, diferenciacion, ingreso]
req: [REQ-AOS-19]
dependencias: [HU-AOS-24]
skills: ["new-pack", "db-migration", "adr", "arquitecto", "auditor-multitenant", "eval-author", "optimizer"]
estado: borrador
---

# HU-AOS-49 · Pack de conocimiento con documentos por agente

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-AOS-49

**Título:** Pack de conocimiento con documentos por agente

**Workstream:** Agent OS

**Historia:** Como dueño quiero adjuntarle documentos a mi agente (catálogos, preguntas frecuentes, políticas) y elegir cómo busca en ellos, para que responda con la información de mi negocio.

**Por qué importa (valor empresarial):** Es la capacidad que más piden los negocios después de vender y agendar, y la que el dueño nombró como «un pack de rag». Sin ella cada respuesta depende del prompt y el agente inventa o escala de más.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-19

**Dependencias:** [HU-AOS-24](../../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md)

**Criterios de aceptación (Gherkin):**
- **Subir un documento.** Dado la ficha de un agente, cuando subo un PDF de preguntas frecuentes, entonces queda procesado y listado con su estado.
- **Responder con el documento.** Dado un documento procesado, cuando un cliente pregunta algo que está en él, entonces el agente responde con esa información.
- **Configurar la búsqueda.** Dado el conocimiento de un agente, cuando elijo búsqueda semántica o híbrida y ajusto cuántos fragmentos usa, entonces el agente busca así.
- **Aislado por negocio.** Dado dos negocios con documentos, cuando el agente de uno busca, entonces nunca recibe fragmentos del otro.

**Evidencia / Definición de Terminado:**
- ADR del pack (pgvector, ingesta PDF, DOCX y URL, chunking, búsqueda semántica o híbrida, costo de embeddings) aprobado antes del código.
- Pack con tablas `knowledge_documents` y `knowledge_chunks` (`tenant_id`, RLS, índice vectorial) y la tool `buscar_conocimiento` por agente.
- Subida y lista de documentos en la ficha del agente.
- Eval de recuperación con un golden set; embeddings en modo replay en develop.

**Riesgos/Notas:**
- Nota que lo motiva: ítem 23 del [inventario de SPEC-31](../design.md#inventario); hoy solo existe `rag_top_k` global.
- Costo: modelo de embeddings barato y tope por plan; nada de llamadas reales en develop.
