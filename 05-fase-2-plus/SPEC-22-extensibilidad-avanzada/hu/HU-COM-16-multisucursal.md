---
id: HU-COM-16
titulo: Varias sucursales en comercio
spec: SPEC-22
fase: 2
hito: "2"
workstream: Comercio y suscripciones
prioridad: P2
critico: false
estimacion: L
impacto: [ingreso, diferenciacion]
req: [REQ-COM-08]
dependencias: [HU-COM-08, HU-COM-15]
skills: ["backend-design:data-modeling-discipline", "db-migration", "auditor-multitenant"]
estado: borrador
---

# HU-COM-16 · Varias sucursales en comercio

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-22](../spec.md).

**ID:** HU-COM-16

**Título:** Varias sucursales en comercio

**Workstream:** Comercio y suscripciones

**Historia:** Como cadena de restaurantes quiero que cada sucursal tenga su menú, stock, horario y zonas, y que los pedidos lleguen a la sucursal correcta, para operar todas con un solo asistente.

**Por qué importa (valor empresarial):** Las cadenas son los clientes de mayor ticket del vertical restaurante; hoy tendrían que abrir un negocio por sucursal.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-COM-08

**Dependencias:** [HU-COM-08](../../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-08-domicilios.md), [HU-COM-15](../../../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-15-modificadores-y-combos.md)

**Criterios de aceptación (Gherkin):**
- **Ruteo.** Dado la dirección del cliente, cuando pide, entonces el pedido va a la sucursal que cubre su zona.
- **Menú y stock.** Dado una sucursal, cuando el cliente consulta, entonces ve su menú y disponibilidad.
- **Alertas.** Dado un pedido, cuando entra, entonces avisa al equipo de esa sucursal.

**Evidencia / Definición de Terminado:**
- Modelo `branches`; ruteo; tests.

**Riesgos/Notas:**
- Límite de sucursales por plan.
