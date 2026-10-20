---
id: HU-INMO-01
titulo: "ADRs de la vertical y DoR del piloto"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, legal]
req: [REQ-INMO-12]
dependencias: []
skills: ["adr", "arquitecto", "agentcore-conventions", "deep-research"]
estado: borrador
---

# HU-INMO-01 · ADRs de la vertical y DoR del piloto

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-01

**Título:** ADRs de la vertical y DoR del piloto

**Workstream:** Verticales

**Historia:** Como equipo de SolversHub quiero dejar escritas las decisiones de arquitectura de la vertical y el acuerdo con un piloto antes de escribir código, para no construir un pack especulativo ni contradecir ADRs aceptados.

**Por qué importa (valor empresarial):** La vertical toca el gateway, la agenda, las suscripciones y el contrato de procedimientos. Decidir primero evita retrabajo en cuatro packs y cumple la regla de la skill `new-pack` (no hay packs sin cliente real).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-12

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **ADRs escritos.** Dado el diseño de [SPEC-28](../spec.md), cuando se cierra la HU, entonces existen en agent-core, propuestos, el ADR de la vertical (inventario geoespacial, listas y ubicación del canal, agenda por asesor, avisos declarados por habilidades, suscripciones de plazo fijo, supresión por titular) y se aceptan al firmarse el piloto.
- **Piloto.** Dado que no hay cliente, cuando se quiere iniciar [HU-INMO-02](HU-INMO-02-entrada-estructurada-whatsapp.md) o cualquier HU marcada con piloto, entonces sigue bloqueada hasta que P-26 tenga un piloto firmado con nombre, ciudad, tamaño del inventario y si administra arriendos.
- **Decisiones.** Dado D-SPEC-28-4 a D-SPEC-28-9, cuando termina la HU, entonces cada una queda ✅ o remite a su pregunta abierta.

**Evidencia / Definición de Terminado:**
- ADRs propuestos en `solvershub-backend/docs/adr/` con índice actualizado y revisión del agente `arquitecto`. Las enmiendas a ADR aceptados se escriben como ADR nuevos.
- [SPEC-28](../spec.md) en "Diseño aprobado".

**Riesgos/Notas:**
- Fase INMO 0 · DoR.
- Es la única HU de la spec que no exige piloto: escribe y cierra decisiones, no código.
- Las piezas genéricas que sí tienen consumidor real salieron a otras specs: el botón a [HU-AOS-09](../../SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md), las extensiones de procedimientos a [HU-AOS-03](../../SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md), presets v2 a [HU-AOS-46](../../SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) y el cobro en horario legal a HU-SUB-18.
