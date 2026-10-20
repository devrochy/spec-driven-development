---
id: HU-COM-02
titulo: Guardrails de montos y de cierre correctos
spec: SPEC-09
fase: 0
hito: 0A
workstream: Comercio y suscripciones
prioridad: P0
critico: true
estimacion: S
impacto: [calidad_ia, ingreso]
req: [REQ-COM-02, REQ-PLUS-01]
dependencias: []
skills: ["backend-design:testing-with-discernment", "eval-author"]
ola: 1
estado: terminada
---

# HU-COM-02 · Guardrails de montos y de cierre correctos

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-09](../spec.md).

**ID:** HU-COM-02

**Título:** Guardrails de montos y de cierre correctos

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de un negocio quiero que el control de montos entienda cualquier cifra en pesos y que el control de cierre solo acepte acciones que de verdad ocurrieron en este turno para que el asistente no bloquee ventas grandes ni afirme pedidos que no existen.

**Por qué importa (valor empresarial):** Hoy todo monto ≥ 1.000.000 se bloquea (`1.5e+06` en `pack_commerce/module.py:1254-1277`): SolversHub no puede vender su plan Empresarial. Y el chequeo de cierre acepta intentos viejos o fallidos: el asistente puede decir "pedido confirmado" sin pedido.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-COM-02, REQ-PLUS-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Montos grandes.** Dado un total de COP 1.800.000 calculado por el servidor, cuando el asistente lo menciona como "$1.800.000", entonces el guardrail lo acepta.
- **Montos inventados.** Dado un total de COP 150.000, cuando el asistente dice "$15", entonces el guardrail lo bloquea (hoy pasa por coincidencia de texto).
- **Formatos.** Dado montos con punto de miles, coma decimal, "COP" o sin símbolo, cuando se comparan, entonces se interpretan como números según el locale del negocio.
- **Solo el turno actual.** Dado un `crear_pedido` fallido en un turno anterior, cuando el asistente afirma "tu pedido quedó confirmado", entonces el guardrail lo bloquea porque en este turno no hubo un `crear_pedido` exitoso.
- **Umbral por tipo de producto.** Dado el umbral `monto_alto` configurado, cuando el pedido es de un plan recurrente, entonces aplica el umbral de planes (configurable) y no escala la venta de Empresarial por defecto.

**Evidencia / Definición de Terminado:**
- Parser numérico con tests de formatos; el loop expone los resultados del turno actual al guardrail (`core/orchestrator/loop.py:466-487`); tests de D2 y D3 reproducidos.

**Implementada (2026-10-02, PR #188 en `devrochy/agent-core`):**
- `parse_money()` interpreta montos es-CO con `Decimal` (`$1.800.000`, `1.800.000,50`, `COP …`, sin símbolo).
- `_amount_guardrail` compara por **valor** con 2 decimales (no substring): montos ≥ 1e6 dejan de bloquearse y `$15` con total 150.000 ya no pasa.
- Loop estampa `_current_turn`/`_ok`; `_completion_guardrail` solo cuenta tools del turno actual que no fallaron.
- Umbral por planes `monto_alto_planes_threshold` (`None` = nunca escala): plan de 1.8M no escala, one-shot de 1.8M sí.
- 16 tests nuevos; suite 691 passed; ruff e import-linter verdes.

**Riesgos/Notas:**
- El escalamiento determinista por `_escalate` lo implementa [HU-ARCH-12](../../SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md).
