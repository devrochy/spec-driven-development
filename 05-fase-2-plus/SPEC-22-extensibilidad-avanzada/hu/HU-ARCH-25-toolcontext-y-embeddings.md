---
id: HU-ARCH-25
titulo: ToolContext según el contrato y embeddings por negocio
spec: SPEC-22
fase: 2
hito: "2"
workstream: Arquitectura/Prod
prioridad: P2
critico: false
estimacion: L
impacto: [operacion, calidad_ia]
req: [REQ-ARCH-11]
dependencias: [HU-REP-03]
skills: ["adr", "arquitecto", "/codex:adversarial-review"]
estado: borrador
---

# HU-ARCH-25 · `ToolContext` según el contrato y embeddings por negocio

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-22](../spec.md).

**ID:** HU-ARCH-25

**Título:** ToolContext según el contrato y embeddings por negocio

**Workstream:** Arquitectura/Prod

**Historia:** Como desarrollador de packs quiero un `ToolContext` que coincida con el contrato (tenant, agente, traza, logger, emisión de eventos) y memoria semántica configurable por negocio para escribir packs sin abrir sesiones de base directamente.

**Por qué importa (valor empresarial):** Hoy los packs abren sesiones de base en 182 lugares (invariante 6) y la memoria semántica está apagada por defecto. Alinear el contrato reduce errores y habilita mejores respuestas.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-ARCH-11

**Dependencias:** [HU-REP-03](../../../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-03-transicion-de-identificadores.md)

**Criterios de aceptación (Gherkin):**
- **Contrato.** Dado el ADR y el bump major, cuando se publica, entonces `ToolContext` incluye lo del contrato con shim para los packs actuales.
- **Embeddings.** Dado un negocio, cuando configura su proveedor de embeddings, entonces su memoria semántica funciona con su dimensión.

**Evidencia / Definición de Terminado:**
- ADR; contrato versionado; migración de packs.

**Riesgos/Notas:**
- Cambia un contrato inmutable: ADR obligatorio (invariante 4).
