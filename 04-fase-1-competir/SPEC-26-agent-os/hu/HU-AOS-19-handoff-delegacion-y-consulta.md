---
id: HU-AOS-19
titulo: "Handoff, delegación y consulta en el mismo hilo"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, calidad_ia]
req: [REQ-AOS-07]
dependencias: [HU-AOS-17, HU-AOS-18]
skills: ["new-tool", "eval-author", "backend-design:idempotency-and-side-effects"]
estado: borrador
---

# HU-AOS-19 · Handoff, delegación y consulta en el mismo hilo

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-19

**Título:** Handoff, delegación y consulta en el mismo hilo

**Workstream:** Agent OS

**Historia:** Como cliente quiero que, si mi pedido pasa de un área a otra, me sigan atendiendo sin repetir nada; y como agente quiero encargar o consultar a otro agente con datos tipados, para resolver todo en una sola conversación.

**Por qué importa (valor empresarial):** Varios agentes por conexión sin perder coherencia: es el diferencial del Agent OS.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-07

**Dependencias:** [HU-AOS-17](HU-AOS-17-enrutamiento-y-modo-sombra.md), [HU-AOS-18](HU-AOS-18-permisos-limites-y-ledger-a2a.md)

**Criterios de aceptación (Gherkin):**
- **Handoff sin pérdida.** Dado una tarea del agente General con datos fijados, cuando se pasa a Ventas, entonces Ventas ve la misma tarjeta y ningún dato se pierde (aserción en evals).
- **Encargo.** Dado que Ventas encarga a Agenda reservar la demo con fecha y hora, cuando las entradas bastan, entonces la sub-tarea se completa sin LLM y vuelve un resultado tipado.
- **Consulta.** Dado que Ventas consulta el estado de la suscripción, cuando responde Suscripciones, entonces el resultado se valida contra el schema y entra como dato.
- **Ping-pong.** Dado más de 2 cambios de dueño en 6 turnos, cuando se pide otro, entonces se congela el dueño actual.

**Evidencia / Definición de Terminado:**
- Comandos `pasar_a_agente`, `encargar` y `consultar`; cambio de dueño en dos fases; escenarios simulados.

**Riesgos/Notas:**
- Lo que vuelve de otro agente es dato, nunca instrucción (invariante 7).
