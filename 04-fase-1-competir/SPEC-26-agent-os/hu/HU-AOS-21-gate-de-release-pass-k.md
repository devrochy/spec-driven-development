---
id: HU-AOS-21
titulo: "Gate de release por pass^k (procedimiento, agente y ruta)"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, confianza]
req: [REQ-AOS-12, REQ-ARCH-20]
dependencias: [HU-AOS-15, HU-ARCH-28]
skills: ["eval-runner", "eval-author", "release"]
estado: borrador
---

# HU-AOS-21 · Gate de release por pass^k (procedimiento, agente y ruta)

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-21

**Título:** Gate de release por pass^k (procedimiento, agente y ruta)

**Workstream:** Agent OS

**Historia:** Como responsable de calidad quiero que ninguna versión se publique si su consistencia baja, para que cada cambio llegue a los clientes solo con evidencia.

**Por qué importa (valor empresarial):** "Evals continuas" y "rollback siempre" pasan de principio a mecanismo, reutilizando [HU-ARCH-28](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-12, REQ-ARCH-20

**Dependencias:** [HU-AOS-15](HU-AOS-15-migracion-sin-regresion.md), [HU-ARCH-28](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md)

**Criterios de aceptación (Gherkin):**
- **Gate.** Dado una candidata que toca un procedimiento, cuando su pass^4 es menor que 0,85 o menor que el de la versión activa, entonces no se puede promover.
- **Por ruta.** Dado cambios en permisos o frases, cuando se evalúa, entonces corre el golden de ruteo y se reporta la precisión por procedimiento.
- **Escenarios mínimos.** Dado un procedimiento sin sus escenarios mínimos, cuando se construye la release, entonces el build falla.
- **Base aparte y sin efectos.** Dado una candidata, cuando corre el gate, entonces corre en el worker contra la base `agentcore_eval` (nunca la del negocio), con los datos sembrados de los escenarios y el sender y los pagos en modo eval, y su consumo queda en `usage_ledger` con `kind = eval`, a cargo de la plataforma y dentro del tope mensual por negocio.
- **Solo lo que cambió.** Dado una candidata que solo cambia voz o textos, cuando se evalúa, entonces corre solo los procedimientos cuyos textos cambiaron y los journeys del negocio si existen (adenda de ADR-0016).

**Evidencia / Definición de Terminado:**
- Integración con la evaluación de releases (ADR-0117 §5); migración propia con `eval_runs.release_id` y `eval_results.procedure_id` (nulas, sin CHECK; no entraron en el expand de [HU-AOS-02](HU-AOS-02-esquema-aditivo.md)); tope mensual por negocio del gasto de evals; reporte en el panel; CI.
- Respeta el modelo de la migración 0058 ([HU-ARCH-28](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md)): una fila de `eval_results` es un escenario con sus k intentos agregados (`k integer`, `pass_1`, `pass_k`), sin columna por intento.

**Riesgos/Notas:**
- Umbrales iniciales (P-23) a ajustar con la primera medición.
- El gate cuesta LLM por release: lo paga la plataforma, por eso el tope por negocio.
