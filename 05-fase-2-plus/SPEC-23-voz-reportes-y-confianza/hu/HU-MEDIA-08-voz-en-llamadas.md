---
id: HU-MEDIA-08
titulo: Voz en llamadas con ADR y spike
spec: SPEC-23
fase: 2
hito: "2"
workstream: Multimodalidad
prioridad: P2
critico: false
estimacion: M
impacto: [diferenciacion]
req: [REQ-MEDIA-08]
dependencias: [HU-MEDIA-03]
skills: ["deep-research", "adr"]
estado: borrador
---

# HU-MEDIA-08 · Voz en llamadas con ADR y spike

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-23](../spec.md).

**ID:** HU-MEDIA-08

**Título:** Voz en llamadas con ADR y spike

**Workstream:** Multimodalidad

**Historia:** Como dueño de SolversHub quiero un experimento medido de atención por llamada de voz para decidir con datos si se agrega al producto.

**Por qué importa (valor empresarial):** Darwin AI y Wolkvox ofrecen voz. D-03 lo dejó fuera de v1; un spike acotado evita apostar sin datos.

**Prioridad:** P2 plus

**Estimación:** M

**REQ mapeados:** REQ-MEDIA-08

**Dependencias:** [HU-MEDIA-03](../../../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md)

**Criterios de aceptación (Gherkin):**
- **Spike.** Dado un proveedor de telefonía, cuando se prueba con 20 llamadas reales, entonces se mide latencia, costo por minuto y satisfacción.
- **Decisión.** Dado los resultados, cuando se escribe el ADR, entonces decide seguir o no con opciones y costos.

**Evidencia / Definición de Terminado:**
- Informe del spike y ADR.

**Riesgos/Notas:**
- —
