---
id: HU-AOS-20
titulo: "Colaboración con pila de tareas"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, diferenciacion]
req: [REQ-AOS-07]
dependencias: [HU-AOS-19]
skills: ["eval-author", "agentcore-conventions"]
estado: borrador
---

# HU-AOS-20 · Colaboración con pila de tareas

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-20

**Título:** Colaboración con pila de tareas

**Workstream:** Agent OS

**Historia:** Como cliente quiero pedir dos cosas en el mismo mensaje y recibir una sola respuesta que cubra ambas, para no tener que repetir.

**Por qué importa (valor empresarial):** Resuelve la multi-intención con coherencia: un mensaje y una sola pregunta.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-07

**Dependencias:** [HU-AOS-19](HU-AOS-19-handoff-delegacion-y-consulta.md)

**Criterios de aceptación (Gherkin):**
- **Dos tareas.** Dado "quiero el Premium y una demo el jueves", cuando el Coordinador detecta dos disparadores fuertes de agentes habilitados en la conexión, entonces abre una tarea en foco y otra en pausa (la colaboración no es un permiso de `agent_links`, ADR-0116).
- **Un mensaje.** Dado las dos tareas, cuando responde, entonces envía un solo mensaje con como máximo una pregunta y el verificador valida montos y horarios.
- **Retomar.** Dado la tarea en foco completada, cuando sigue la conversación, entonces se retoma la que estaba en pausa.

**Evidencia / Definición de Terminado:**
- Pila con `stack_position` y límite `maxStack`; escenarios simulados.

**Riesgos/Notas:**
- Más de dos intenciones a la vez se atienden en orden, no en paralelo.
