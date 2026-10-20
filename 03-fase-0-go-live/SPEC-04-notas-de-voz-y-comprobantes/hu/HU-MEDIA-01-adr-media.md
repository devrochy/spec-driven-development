---
id: HU-MEDIA-01
titulo: ADR de procesamiento de media en el core
spec: SPEC-04
fase: 0
hito: 0B
workstream: Multimodalidad
prioridad: P0
critico: true
estimacion: S
impacto: [calidad_ia, legal]
req: [REQ-ARCH-05, REQ-MEDIA-06]
dependencias: []
skills: ["adr", "arquitecto", "deep-research"]
estado: borrador
---

# HU-MEDIA-01 · ADR de procesamiento de media en el core

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-04](../spec.md) (D-SPEC-04-1, D-SPEC-04-2).

**ID:** HU-MEDIA-01

**Título:** ADR de procesamiento de media en el core

**Workstream:** Multimodalidad

**Historia:** Como responsable técnico quiero decidir por escrito dónde se procesa y se guarda la media, cuánto se retiene y cómo se cobra para portar lo de `agent-sale` sin romper las invariantes.

**Por qué importa (valor empresarial):** La media trae datos personales (voces, documentos, cuentas bancarias). Una decisión explícita sobre retención y privacidad es requisito legal (Ley 1581) y de cualquier cliente enterprise.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** S

**REQ mapeados:** REQ-ARCH-05, REQ-MEDIA-06

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Decisiones escritas.** Dado el ADR, cuando se revisa, entonces fija ubicación del procesamiento, almacenamiento, retención por defecto, límites (16 MB, timeouts), idempotencia, costeo y dónde viven los prompts.
- **Qué no se porta.** Dado el ADR, cuando se lee, entonces explica por qué no se porta el base64 en Postgres ni los prompts en código de `agent-sale`.

**Evidencia / Definición de Terminado:**
- ADR aceptado en `solvershub-core/docs/adr/`.

**Riesgos/Notas:**
- El DPA (HU-GTM-02) debe mencionar el procesamiento de media y sus subprocesadores.
