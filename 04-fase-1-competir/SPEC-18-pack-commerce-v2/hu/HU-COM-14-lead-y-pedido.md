---
id: HU-COM-14
titulo: Vínculo entre lead y pedido
spec: SPEC-18
fase: 1
hito: "1"
workstream: Comercio y suscripciones
prioridad: P1
critico: false
estimacion: S
impacto: [ingreso, operacion]
req: [REQ-COM-07]
dependencias: [HU-COM-05]
skills: ["backend-design:data-modeling-discipline"]
estado: parqueada
---

# HU-COM-14 · Vínculo entre lead y pedido

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-18](../spec.md).

**ID:** HU-COM-14

**Título:** Vínculo entre lead y pedido

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de un negocio quiero que un lead quede como convertido cuando hace su primer pedido para medir mi embudo de punta a punta.

**Por qué importa (valor empresarial):** Sin el vínculo no se puede calcular la conversión por campaña ([HU-SH-09](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-09-landing-con-atribucion.md)) ni el costo de adquisición.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-COM-07

**Dependencias:** [HU-COM-05](../../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md)

**Criterios de aceptación (Gherkin):**
- **Conversión.** Dado un lead que hace su primer pedido pagado, cuando ocurre, entonces el lead pasa a convertido con fecha y pedido.
- **Vista unificada.** Dado la vista de Clientes, cuando abro un lead convertido, entonces veo sus pedidos.

**Evidencia / Definición de Terminado:**
- Proveedor de commerce en el registro de leads del core; tests.

**Riesgos/Notas:**
- —
