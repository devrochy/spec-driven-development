---
id: HU-AOS-37
titulo: "Cuotas Agent OS: operaciones entre agentes y back-office"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso]
req: [REQ-AOS-14]
dependencias: [HU-AOS-18, HU-BILL-05, HU-BILL-06]
skills: ["backend-design:think-before-coding", "panel-ui"]
estado: borrador
---

# HU-AOS-37 · Cuotas Agent OS: operaciones entre agentes y back-office

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md). Achicada el 2026-10-17 por [D-35](../../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes): agentes publicados, colaboradores y conexiones son de HU-BILL-05.

**ID:** HU-AOS-37

**Título:** Cuotas Agent OS: operaciones entre agentes y back-office

**Workstream:** Agent OS

**Historia:** Como SolversHub quiero cobrar las operaciones entre agentes dentro de los créditos y poner tope por plan a los agentes de back-office, para que el Agent OS tenga un modelo de precios claro sobre los planes por agentes de HU-BILL-05.

**Por qué importa (valor empresarial):** Convierte la capacidad en ingreso y en expansión por negocio sin duplicar HU-BILL-05: lo que se vende es el agente (D-35) y aquí solo se cobra lo que los agentes hacen entre sí y lo que trabaja sin escribirle al cliente.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-14

**Dependencias:** [HU-AOS-18](HU-AOS-18-permisos-limites-y-ledger-a2a.md), HU-BILL-05, HU-BILL-06

**Criterios de aceptación (Gherkin):**
- **Créditos A2A.** Dado operaciones entre agentes con LLM (consulta, delegación), cuando se cobran, entonces salen del ledger por unidad, atribuidas a la instancia que las pidió (`usage_ledger.agent_instance_id`), sin doble conteo.
- **Back-office.** Dado el tope de agentes de back-office del plan (`documento de precios (privado) §5`, propuesta), cuando el negocio intenta activar uno más, entonces el panel explica el límite y ofrece subir de plan; un agente de back-office no cuenta como agente publicado.
- **Presupuesto.** Dado el presupuesto A2A del KernelSpec agotado en un episodio, cuando un agente pide otra consulta, entonces el Coordinador la niega y queda registrado en `a2a_events`.

**Evidencia / Definición de Terminado:**
- Métricas `operaciones_a2a` y `agentes_backoffice`; enforcement; tests. Las métricas `agentes`, `colaboradores` y `conexiones` son de HU-BILL-05.

**Riesgos/Notas:**
- Achicada el 2026-10-17 (D-35): agentes publicados, conexiones y colaboradores pasaron a HU-BILL-05; P-13 cerrada. El tope de back-office solo se aplica cuando exista [HU-AOS-30](HU-AOS-30-agentes-de-back-office.md).
