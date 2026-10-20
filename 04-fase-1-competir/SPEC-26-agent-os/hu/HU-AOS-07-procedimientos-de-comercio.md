---
id: HU-AOS-07
titulo: "Procedimientos de comercio (planes, contratar plan, pedido con entrega)"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, calidad_ia]
req: [REQ-AOS-03]
dependencias: [HU-AOS-06]
skills: ["new-pack", "new-tool", "eval-author"]
estado: terminada
---

# HU-AOS-07 · Procedimientos de comercio (planes, contratar plan, pedido con entrega)

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-07

**Título:** Procedimientos de comercio (planes, contratar plan, pedido con entrega)

**Workstream:** Agent OS

**Historia:** Como negocio de comercio o de planes quiero que consultar planes, contratar un plan y tomar un pedido con entrega sean procedimientos tipados, para que el total, el link y la confirmación salgan siempre del servidor.

**Por qué importa (valor empresarial):** Es el camino del dinero (ADR-0087) por el que el 0A vende planes. Con procedimientos, un monto o un link equivocado deja de ser posible por construcción.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-03

**Dependencias:** [HU-AOS-06](HU-AOS-06-comandos-y-verificador-sobre-estado.md)

**Criterios de aceptación (Gherkin):**
- **Contratar un plan.** Dado el procedimiento `contratar_plan`, cuando un cliente simulado compra Premium mensual, entonces el pedido tiene la variante y el total del servidor, el link es el de la acción y el escenario tiene pass^4 ≥ 0,85.
- **Pedido con entrega.** Dado un pedido a domicilio, cuando falta la dirección, entonces la tarea no pasa a confirmar hasta tenerla confirmada.
- **Cambio de opinión.** Dado un cliente que cambia de plan antes de confirmar, cuando actualiza el dato, entonces la cotización se recalcula y la anterior no se usa.

**Evidencia / Definición de Terminado:**
- Procedimientos en `pack-commerce` con *resolvers*; escenarios de usuario simulado; journeys de comercio en verde.

**Terminada (2026-10-11):** PRs agent-core [#454](https://github.com/devrochy/agent-core/pull/454), [#457](https://github.com/devrochy/agent-core/pull/457), [#458](https://github.com/devrochy/agent-core/pull/458), [#459](https://github.com/devrochy/agent-core/pull/459), [#462](https://github.com/devrochy/agent-core/pull/462).

**Riesgos/Notas:**
- El catálogo de planes de HU-SUB-07 (ADR-0111) se reutiliza; no se duplica.
