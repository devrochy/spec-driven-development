---
id: HU-MEDIA-06
titulo: Clasificación de imágenes y descripción de producto
spec: SPEC-04
fase: 0
hito: 0B
workstream: Multimodalidad
prioridad: P0
critico: false
estimacion: M
impacto: [calidad_ia, ingreso]
req: [REQ-MEDIA-05]
dependencias: [HU-MEDIA-04]
skills: ["eval-author", "optimizer"]
estado: borrador
---

# HU-MEDIA-06 · Clasificación de imágenes y descripción de producto

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-04](../spec.md).

**ID:** HU-MEDIA-06

**Título:** Clasificación de imágenes y descripción de producto

**Workstream:** Multimodalidad

**Historia:** Como cliente de una tienda quiero mandar la foto de un producto y que el asistente lo busque en el catálogo para no tener que saber cómo se llama.

**Por qué importa (valor empresarial):** "¿Tienen esto?" con una foto es una consulta de compra muy común. Separar fotos de producto de comprobantes evita aprobar pagos por error y convierte imágenes en ventas.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-MEDIA-05

**Dependencias:** [HU-MEDIA-04](HU-MEDIA-04-dispatcher-de-vision.md)

**Criterios de aceptación (Gherkin):**
- **Clasificación.** Dado un cliente con un pago pendiente que manda una imagen, cuando se procesa, entonces se clasifica como comprobante o producto; ante la duda se trata como comprobante (falla segura).
- **Descripción.** Dado una foto de producto, cuando se procesa, entonces el turno recibe `[Foto de producto] <descripción>` y el asistente busca en el catálogo.
- **Prompts como datos.** Dado los prompts de clasificación y descripción, cuando se revisan, entonces viven en playbooks del pack de comercio, genéricos para cualquier rubro (no los de motos de `agent-sale`).

**Evidencia / Definición de Terminado:**
- Tests con imágenes de ejemplo y escenarios en el golden set de comercio.

**Riesgos/Notas:**
- Sin pago pendiente, toda imagen se trata como foto de producto.
