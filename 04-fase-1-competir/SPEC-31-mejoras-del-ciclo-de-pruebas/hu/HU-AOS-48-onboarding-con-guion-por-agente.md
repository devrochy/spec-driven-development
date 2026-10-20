---
id: HU-AOS-48
titulo: Onboarding con guion de preguntas por tipo de agente
spec: SPEC-31
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, diferenciacion, operacion]
req: [REQ-AOS-18]
dependencias: [HU-AOS-24, HU-AOS-46]
skills: ["panel-ui", "frontend-design", "agentcore-conventions", "eval-author"]
estado: borrador
---

# HU-AOS-48 · Onboarding con guion de preguntas por tipo de agente

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-AOS-48

**Título:** Onboarding con guion de preguntas por tipo de agente

**Workstream:** Agent OS

**Historia:** Como dueño de un negocio nuevo quiero que, al entrar por primera vez, una ventana me pregunte para qué quiero mi agente y me haga unas 10 preguntas, para dejarlo configurado sin recorrer formularios largos.

**Por qué importa (valor empresarial):** El dueño lo pidió textual: «con 10 preguntas se pueda configurar un agente». Es lo que convierte una prueba gratuita en un agente publicado: menos campos, más negocios activos.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-18

**Dependencias:** [HU-AOS-24](../../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md), [HU-AOS-46](../../SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md)

**Criterios de aceptación (Gherkin):**
- **Ventana al primer ingreso.** Dado un negocio nuevo sin agentes, cuando el dueño entra por primera vez, entonces ve una ventana que le pregunta para qué quiere su agente (ventas, cobranza, agenda o suscripciones).
- **Guion por fin.** Dado que elegí «agente de cobranza», cuando avanzo, entonces respondo unas 10 preguntas con opciones o respuesta abierta, en lenguaje de negocio.
- **Agente listo.** Dado que terminé el guion, cuando confirmo, entonces el agente queda creado con su identidad, horario, superpoderes y conexión, y la Bienvenida muestra solo los pasos que faltan para ese agente.
- **Retomar.** Dado que cerré la ventana a mitad del guion, cuando vuelvo desde la Bienvenida, entonces retomo donde quedé.

**Evidencia / Definición de Terminado:**
- Las plantillas de [HU-AOS-24](../../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) suman `preguntas[]` (opción o texto, a qué campo del agente va cada respuesta).
- Core: aplicar las respuestas al borrador del agente reutilizando el editor y los presets v2; progreso guardado por negocio.
- Panel: `ui/dialog.tsx` paso a paso reutilizando `agentes/[id]/editar/_components/pasos.tsx`; enlace desde `components/domain/bienvenida.tsx`.
- Prueba del catálogo para cada fin y eval corto del agente resultante.

**Riesgos/Notas:**
- Nota que lo motiva: ítem 22 del [inventario de SPEC-31](../design.md#inventario).
- No reemplaza el editor completo: el guion es el camino corto, el editor sigue para ajustar.
