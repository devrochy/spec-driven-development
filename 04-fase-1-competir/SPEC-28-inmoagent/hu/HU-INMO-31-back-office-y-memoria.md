---
id: HU-INMO-31
titulo: "Back-office y memoria de la vertical"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, ingreso]
req: [REQ-INMO-11]
dependencias: [HU-INMO-21, HU-INMO-22, HU-INMO-30, HU-AOS-30, HU-AOS-36]
skills: ["eval-author", "arquitecto"]
estado: borrador
---

# HU-INMO-31 · Back-office y memoria de la vertical

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-31

**Título:** Back-office y memoria de la vertical

**Workstream:** Verticales

**Historia:** Como inmobiliaria quiero que el sistema detecte coincidencias, prepare el resumen para el asesor y recuerde al cliente con procedencia, sin que nada le escriba al cliente por fuera del Coordinador.

**Por qué importa (valor empresarial):** Cierra el mapeo de MatchAgent y HandoffAgent sobre el Agent OS: el back-office propone y el Coordinador decide (ADR-0116).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-11

**Dependencias:** [HU-INMO-21](HU-INMO-21-seguimiento-post-visita-y-encuesta.md), [HU-INMO-22](HU-INMO-22-alertas-y-reenganche.md), [HU-INMO-30](HU-INMO-30-especialistas-inmobiliarios.md), [HU-AOS-30](../../SPEC-26-agent-os/hu/HU-AOS-30-agentes-de-back-office.md), [HU-AOS-36](../../SPEC-26-agent-os/hu/HU-AOS-36-memoria-por-scope.md)

**Criterios de aceptación (Gherkin):**
- **Coincidencias.** Dado un inmueble publicado, cuando corre el back-office "Coincidencias", entonces propone avisos que pasan por las políticas del Coordinador y nunca escribe directo al cliente.
- **Resumen.** Dado un relevo al asesor, cuando se dispara `escalation.triggered`, entonces queda una nota con el perfil, los inmuebles vistos y la visita.
- **Memoria.** Dado una tarea de búsqueda cerrada, cuando se consolida, entonces sus datos útiles pasan a `memory_facts` en `inmo_busqueda` con procedencia.

**Evidencia / Definición de Terminado:**
- Agentes back-office de la vertical; namespaces `inmo_*` con el escritor de servidor definido en [HU-AOS-36](../../SPEC-26-agent-os/hu/HU-AOS-36-memoria-por-scope.md); escenarios de consolidación.

**Riesgos/Notas:**
- Fase INMO 5 · Agent OS nativo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- Espera AOS R5 ([HU-AOS-30](../../SPEC-26-agent-os/hu/HU-AOS-30-agentes-de-back-office.md), [HU-AOS-34](../../SPEC-26-agent-os/hu/HU-AOS-34-acciones-v2.md), [HU-AOS-36](../../SPEC-26-agent-os/hu/HU-AOS-36-memoria-por-scope.md)).
