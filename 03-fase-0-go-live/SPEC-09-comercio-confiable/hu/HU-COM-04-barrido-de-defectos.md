---
id: HU-COM-04
titulo: Barrido de defectos de comercio D5 a D16 y D18
spec: SPEC-09
fase: 0
hito: 0B
workstream: Comercio y suscripciones
prioridad: P0
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-COM-03]
dependencias: [HU-COM-01]
skills: ["backend-design:query-discipline", "/backend-design:hunt-n-plus-one", "backend-design:testing-with-discernment"]
estado: borrador
---

# HU-COM-04 · Barrido de defectos de comercio D5 a D16 y D18

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-09](../spec.md).

**ID:** HU-COM-04

**Título:** Barrido de defectos de comercio D5 a D16 y D18

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de una tienda quiero que los seguimientos automáticos se envíen de verdad, que el stock no se sobrevenda, que las promociones y los segmentos calculen bien y que los montos se vean en formato colombiano para confiar en lo que el sistema hace por mí.

**Por qué importa (valor empresarial):** Son 13 defectos pequeños que juntos hacen que el comercio "parezca" funcionar: crons que nunca envían, stock que se sobrevende con pedidos simultáneos, un KPI que nunca pasa de 5. Cada uno es una promesa rota para el primer cliente.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-COM-03

**Dependencias:** [HU-COM-01](HU-COM-01-dinero-en-el-servidor.md)

**Criterios de aceptación (Gherkin):**
- **Crons vivos (D5, D6, D7).** Dado una cotización de hace 4 h o un lead sin respuesta, cuando corre el cron con la config por defecto, entonces envía el seguimiento, lo marca enviado solo si se envió y un error de un negocio no detiene a los demás.
- **Plantillas seguras (D8).** Dado una plantilla de mensaje con una variable mal escrita, cuando se usa, entonces se envía el texto por defecto y el pack sigue habilitado.
- **Stock atómico (D10, D11).** Dado dos pedidos simultáneos por la última unidad, cuando se crean, entonces solo uno la obtiene; el LLM recibe "disponible" y no el número exacto.
- **Promociones y segmentos (D12, D13).** Dado una promoción por categoría con subcategorías, cuando aplica, entonces incluye las subcategorías; el ítem gratis es una línea de $0; un cliente con 1 pedido es "nuevo".
- **Panel (D14, D15).** Dado más de 5 pedidos, cuando veo el KPI, entonces muestra el total real; dado una categoría con hijos, cuando la borro, entonces se impide.
- **Formato (D18).** Dado un monto, cuando se muestra al cliente, entonces usa el símbolo y el formato del negocio (`$60.000`).

**Evidencia / Definición de Terminado:**
- Un test de regresión por defecto; golden set de comercio actualizado.

**Riesgos/Notas:**
- D9 va en [HU-COM-05](HU-COM-05-estados-del-pedido.md) y D16 en HU-SUB-04.
