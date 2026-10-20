---
id: HU-COM-15
titulo: Modificadores y combos para menús
spec: SPEC-18
fase: 1
hito: "1"
workstream: Comercio y suscripciones
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, diferenciacion]
req: [REQ-COM-04]
dependencias: [HU-COM-07]
skills: ["db-migration", "backend-design:data-modeling-discipline", "eval-author"]
estado: parqueada
---

# HU-COM-15 · Modificadores y combos para menús

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-18](../spec.md).

**ID:** HU-COM-15

**Título:** Modificadores y combos para menús

**Workstream:** Comercio y suscripciones

**Historia:** Como restaurante quiero ofrecer tamaños, adicionales con precio y combos para que el asistente tome pedidos como los toma un cajero.

**Por qué importa (valor empresarial):** "Hamburguesa doble con tocineta extra y papas grandes" es el pedido típico; sin modificadores, el restaurante no puede usar el asistente para todo su menú. ClonAI se especializa justamente en restaurantes.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-COM-04

**Dependencias:** [HU-COM-07](../../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-07-catalogo-menus-y-retail.md)

**Criterios de aceptación (Gherkin):**
- **Grupos de opciones.** Dado un plato con tamaño (obligatorio) y adicionales (0 a 3), cuando el cliente pide, entonces el asistente pregunta lo obligatorio y suma los adicionales al precio.
- **Combos.** Dado un combo con productos elegibles, cuando se pide, entonces se arma con su precio de combo.
- **Cocina.** Dado el pedido, cuando la cocina lo ve, entonces cada línea muestra sus modificadores.

**Evidencia / Definición de Terminado:**
- Modelo de modificadores; tools actualizadas; golden set de restaurante ampliado.

**Riesgos/Notas:**
- Aumenta el tamaño del esquema de tools: medir el costo en créditos.
