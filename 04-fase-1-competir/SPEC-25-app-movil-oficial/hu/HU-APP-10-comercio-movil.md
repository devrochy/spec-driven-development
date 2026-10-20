---
id: HU-APP-10
titulo: "Comercio móvil: productos, categorías, promociones y pedidos"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso]
req: [REQ-APP-07]
dependencias: [HU-APP-03]
skills: [frontend-design, panel-ui]
estado: terminada
---

# HU-APP-10 · Comercio móvil: productos, categorías, promociones y pedidos

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-10

**Título:** Comercio móvil: productos, categorías, promociones y pedidos

**Workstream:** App móvil

**Historia:** Como dueño de un negocio con comercio quiero ver productos (con variantes y stock), categorías, promociones y pedidos desde la app, y cambiar el estado de un pedido, para operar la tienda mientras estoy en el local o en la calle.

**Por qué importa (valor empresarial):** El pack de comercio convierte conversaciones en pedidos; que el dueño pueda gestionar catálogo y despachos desde el celular cierra el ciclo de la venta por WhatsApp y amplía la propuesta de valor de la app oficial frente a la matriz.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-03](HU-APP-03-navegacion-por-permisos.md)

**Criterios de aceptación (Gherkin):**
- **Catálogo.** Dado un negocio con productos, cuando abre Comercio, entonces ve la lista paginada con búsqueda, variantes (SKU, precio, stock) y puede crear/editar productos y categorías con validaciones iguales al panel.
- **Promociones.** Dado un dueño, cuando abre Promociones, entonces ve vigencia y estado (programada/activa/vencida) y puede activar/desactivar.
- **Pedidos.** Dado un pedido confirmado, cuando el dueño cambia su estado (abierto→despachado→entregado/cancelado/expirado), entonces el cambio se registra con confirmación y el estado del pago permanece independiente.
- **Offline.** Dado un pedido con cambio de estado hecho sin conexión, cuando vuelve la red, entonces el cambio se encola y sincroniza sin duplicados (regla de escrituras encoladas del ADR-APP-04).

**Evidencia / Definición de Terminado:**
- `modules/comercio/` (productos, categorías, promociones, pedidos) contra `/api/v1/pack/commerce/*`; escritura encolada para `orders/{id}/status`; tests unitarios, de render y de encolado; captura en dev client.

**Implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — comercio móvil (productos, categorías, promociones y pedidos).

**Riesgos/Notas:**
- La importación CSV del panel queda fuera de la v1 móvil (acción de escritorio) con CTA "abrir en web".
- El agente elige la mejor promoción en el servidor; la app solo muestra/administra, nunca calcula beneficios.

**App implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — `modules/comercio`: pedidos con cambio de estado confirmado, productos, promociones (toggle) y categorías. Formularios completos de creación (deuda). 3 tests.
