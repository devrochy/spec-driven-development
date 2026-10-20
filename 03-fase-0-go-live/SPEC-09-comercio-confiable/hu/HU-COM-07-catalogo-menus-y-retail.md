---
id: HU-COM-07
titulo: Catálogo para menús y retail
spec: SPEC-09
fase: 0
hito: 0B
workstream: Comercio y suscripciones
prioridad: P0
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-COM-04]
dependencias: [HU-COM-04]
skills: ["db-migration", "frontend-design", "xlsx", "panel-ui"]
estado: borrador
---

# HU-COM-07 · Catálogo para menús y retail

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-09](../spec.md).

**ID:** HU-COM-07

**Título:** Catálogo para menús y retail

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de un restaurante quiero marcar platos como disponibles o agotados sin manejar stock, subir fotos y permitir notas por plato, y como tienda quiero productos con variantes e importación por CSV, para tener mi catálogo real en el asistente.

**Por qué importa (valor empresarial):** Hoy un menú tiene que fingir stock (`generar_cotizacion` bloquea sin stock), el editor solo maneja una variante y el CSV duplica productos. Sin catálogo real, el restaurante no puede vender por el asistente: es el bloqueo del primer cliente de comercio.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-COM-04

**Dependencias:** [HU-COM-04](HU-COM-04-barrido-de-defectos.md)

**Criterios de aceptación (Gherkin):**
- **Disponibilidad sin stock.** Dado un producto con `track_inventory = false`, cuando está "disponible", entonces se puede cotizar sin stock; si está "agotado", el asistente ofrece alternativas.
- **Archivo.** Dado un producto que ya no se vende, cuando se archiva, entonces deja de ofrecerse sin borrar su historial.
- **Fotos.** Dado un producto con imagen, cuando un cliente lo consulta por SKU y hay una sola coincidencia, entonces el asistente envía la foto.
- **Variantes e importación.** Dado un CSV con variantes (talla, color), cuando lo importo con vista previa, entonces se agrupan por producto y se actualizan por SKU sin duplicar.
- **Notas por línea.** Dado un plato, cuando el cliente pide "sin cebolla", entonces la nota queda en la línea del pedido y la cocina la ve.

**Evidencia / Definición de Terminado:**
- Migraciones (`active`, `track_inventory`, imágenes, notas); editor multi-variante en el panel; importación con vista previa; tests.

**Riesgos/Notas:**
- Los modificadores y combos llegan en [HU-COM-15](../../../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-15-modificadores-y-combos.md) (Fase 1).
