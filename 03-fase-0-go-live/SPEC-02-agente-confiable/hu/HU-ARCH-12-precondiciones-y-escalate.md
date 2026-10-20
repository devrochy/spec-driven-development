---
id: HU-ARCH-12
titulo: Precondiciones terminales, señal escalate y scopes en tools de pago
spec: SPEC-02
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: M
impacto: [calidad_ia, confianza]
req: [REQ-ARCH-07, REQ-PLUS-01]
dependencias: []
skills: ["new-tool", "backend-design:error-handling-as-design", "adr", "eval-author"]
estado: borrador
---

# HU-ARCH-12 · Precondiciones terminales, señal `escalate` y scopes en tools de pago

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-02](../spec.md).

**ID:** HU-ARCH-12

**Título:** Precondiciones terminales, señal escalate y scopes en tools de pago

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de un negocio quiero que las acciones que cierran una venta o cobran solo corran si se cumplen sus condiciones, y que un monto alto escale a un humano de forma automática, para no depender de lo que el modelo decida escribir.

**Por qué importa (valor empresarial):** Es el núcleo de "IA confiable", el diferencial que nadie en la liga LATAM comunica. Hoy la señal `escalate` que devuelve `crear_pedido` nunca se lee (`pack_commerce/skills.py:1158-1163`) y las tools de pago no declaran permisos.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-07, REQ-PLUS-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Precondición.** Dado una tool terminal que requiere un pedido confirmado, cuando el LLM la llama sin pedido confirmado, entonces el host la rechaza con `precondicion_no_cumplida` sin ejecutarla.
- **Escalamiento determinista.** Dado una tool que devuelve `_escalate` con motivo `monto_alto`, cuando termina el turno, entonces el core crea la escalación y pausa el bot aunque el texto del LLM no lo diga.
- **Scopes.** Dado un negocio sin el scope `payments:create_link` en su binding, cuando el LLM pide un link, entonces se rechaza y queda auditado.
- **Idempotencia estable.** Dado un turno reintentado, cuando una tool usa `ToolContext.message_id` como llave, entonces no duplica el efecto.

**Evidencia / Definición de Terminado:**
- Tests de las tres reglas y del reintento.
- `PLUGIN-CONTRACT.md` documenta `requires`, `_escalate` y `scopes`.

**Riesgos/Notas:**
- Cambia `ToolContext` en runtime, no el contrato congelado: si toca `agentcore_contracts`, se escribe ADR.
