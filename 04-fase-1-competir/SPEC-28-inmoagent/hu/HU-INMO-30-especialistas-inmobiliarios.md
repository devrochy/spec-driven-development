---
id: HU-INMO-30
titulo: "Especialistas inmobiliarios en el Coordinador"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, diferenciacion]
req: [REQ-INMO-11]
dependencias: [HU-INMO-29, HU-AOS-46, HU-AOS-19, HU-AOS-21]
skills: ["eval-author", "arquitecto", "customizer"]
estado: borrador
---

# HU-INMO-30 · Especialistas inmobiliarios en el Coordinador

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-30

**Título:** Especialistas inmobiliarios en el Coordinador

**Workstream:** Verticales

**Historia:** Como cliente quiero hablar con un solo asistente que sepa de búsqueda, captación y arriendos, sin repetir datos cuando cambio de tema.

**Por qué importa (valor empresarial):** Los 3 especialistas (D-SPEC-28-6) dan profundidad por área con una sola voz y sin perder contexto.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-11

**Dependencias:** [HU-INMO-29](HU-INMO-29-procedimientos-inmobiliarios.md), [HU-AOS-46](../../SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md), [HU-AOS-19](../../SPEC-26-agent-os/hu/HU-AOS-19-handoff-delegacion-y-consulta.md), [HU-AOS-21](../../SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md)

**Criterios de aceptación (Gherkin):**
- **Ruta.** Dado mensajes de búsqueda, captación y arriendo, cuando los enruta el Coordinador, entonces la precisión de ruta es ≥ 0,90 en el set de la vertical.
- **Pila.** Dado una búsqueda en curso y la pregunta "¿y cuánto debo del arriendo?", cuando se responde, entonces la búsqueda queda en pausa y se retoma sin perder datos.
- **Consulta.** Dado que `asesor_comercial` necesita saber si el cliente es arrendatario, cuando consulta a `arriendos`, entonces recibe una lectura tipada y no escribe en su namespace.

**Evidencia / Definición de Terminado:**
- Plantillas de agente `asesor_comercial`, `captacion` y `arriendos`; reglas del KernelSpec; set de ruta.

**Riesgos/Notas:**
- Fase INMO 5 · Agent OS nativo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
