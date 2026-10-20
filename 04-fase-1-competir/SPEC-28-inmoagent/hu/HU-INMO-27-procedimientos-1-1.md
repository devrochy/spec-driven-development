---
id: HU-INMO-27
titulo: "Afirmaciones de atributo, distancia y prohibidas"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, diferenciacion]
req: [REQ-INMO-11]
dependencias: [HU-AOS-06, HU-INMO-17]
skills: ["adr", "arquitecto", "eval-author"]
estado: borrador
---

# HU-INMO-27 · Afirmaciones de atributo, distancia y prohibidas

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-27

**Título:** Afirmaciones de atributo, distancia y prohibidas

**Workstream:** Agent OS

**Historia:** Como negocio quiero que el verificador compruebe áreas, habitaciones y distancias, y que bloquee la dirección antes de agendar, para que el asistente nunca afirme un dato del inmueble que el servidor no dio.

**Por qué importa (valor empresarial):** El verificador del Agent OS solo conoce afirmaciones de monto, link y estado. La vertical necesita atributos, distancias y una afirmación prohibida.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-11

**Dependencias:** [HU-AOS-06](../../SPEC-26-agent-os/hu/HU-AOS-06-comandos-y-verificador-sobre-estado.md), [HU-INMO-17](HU-INMO-17-fichas-y-verificacion-de-hechos.md)

**Criterios de aceptación (Gherkin):**
- **Atributo.** Dado una respuesta que dice "3 habitaciones" cuando la ficha devolvió 2, cuando corre el verificador, entonces falla.
- **Distancia.** Dado una distancia redondeada por el servidor, cuando la respuesta la cita con otra cifra, entonces el verificador falla.
- **Prohibida.** Dado `kind: forbidden` sobre la dirección exacta, cuando el modelo la menciona sin una visita del cliente, entonces el verificador falla.

**Evidencia / Definición de Terminado:**
- ADR nuevo: cambio de forma del contrato de procedimientos, con su incremento de versión según ADR-0011; verificador y linter actualizados; tests.

**Riesgos/Notas:**
- Fase INMO 5 · Agent OS nativo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- Lo genérico (dato desde payload, condición por tipo de contenido, dato con candidatos) quedó en [HU-AOS-03](../../SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md).
