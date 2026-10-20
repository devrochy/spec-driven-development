---
id: HU-ARCH-20
titulo: Guardrails de runtime completos
spec: SPEC-19
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, calidad_ia]
req: [REQ-ARCH-07]
dependencias: [HU-ARCH-12]
skills: ["backend-design:security-discipline", "backend-design:incident-thinker"]
estado: borrador
---

# HU-ARCH-20 · Guardrails de runtime completos

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-19](../spec.md).

**ID:** HU-ARCH-20

**Título:** Guardrails de runtime completos

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de SolversHub quiero que ninguna tool corra sin un permiso explícito y que haya límites por tiempo para que un error o un abuso no dispare acciones en cadena.

**Por qué importa (valor empresarial):** Hoy una tool sin binding corre igual ("fail-open transitorio"). Cerrar ese hueco y limitar la frecuencia es la base de la promesa "IA confiable" para clientes enterprise.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-07

**Dependencias:** [HU-ARCH-12](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md)

**Criterios de aceptación (Gherkin):**
- **Fail-closed.** Dado una tool sin binding para el negocio, cuando el LLM la llama, entonces se rechaza y queda auditado.
- **Límite por ventana.** Dado `generar_link_pago` llamado 10 veces en un minuto en una conversación, cuando se supera el límite, entonces se bloquea y se escala.

**Evidencia / Definición de Terminado:**
- Cambios en el loop con tests; límites configurables por tool.

**Riesgos/Notas:**
- La tool siguiente forzada queda en [HU-ARCH-26](../../../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md).
