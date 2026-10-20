---
id: HU-ARCH-26
titulo: Tool siguiente forzada y turnos silenciosos en el core
spec: SPEC-22
fase: 2
hito: "2"
workstream: Arquitectura/Prod
prioridad: P2
critico: false
estimacion: L
impacto: [calidad_ia, confianza]
req: [REQ-ARCH-07]
dependencias: [HU-ARCH-20]
skills: ["claude-api", "adr", "eval-runner"]
estado: borrador
---

# HU-ARCH-26 · Tool siguiente forzada y turnos silenciosos en el core

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-22](../spec.md).

**ID:** HU-ARCH-26

**Título:** Tool siguiente forzada y turnos silenciosos en el core

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de SolversHub quiero que el core pueda obligar la siguiente tool en pasos críticos y cortar turnos que no deben responder para que los flujos de dinero sean deterministas.

**Por qué importa (valor empresarial):** Es el siguiente nivel de "IA confiable" que `agent-sale` ya usaba: más fuerte que los guardrails por regex.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-ARCH-07

**Dependencias:** [HU-ARCH-20](../../../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-20-guardrails-runtime.md)

**Criterios de aceptación (Gherkin):**
- **Forzar.** Dado un paso que exige `confirmar_pago_pedido`, cuando el LLM responde sin llamarla, entonces el core la fuerza o reintenta con `tool_choice`.
- **Silencio.** Dado un turno marcado como silencioso, cuando ocurre, entonces no se envía mensaje al cliente.

**Evidencia / Definición de Terminado:**
- Cambios en el loop; tests; compatibilidad por proveedor (algunos modelos rechazan `tool_choice` forzado).

**Riesgos/Notas:**
- Claude Fable 5.1 devuelve 400 con `tool_choice` forzado: la estrategia debe depender del proveedor.
