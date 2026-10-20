---
id: HU-MEDIA-04
titulo: Dispatcher de visión con prueba de conexión y benchmark
spec: SPEC-04
fase: 0
hito: 0B
workstream: Multimodalidad
prioridad: P0
critico: true
estimacion: M
impacto: [calidad_ia]
req: [REQ-MEDIA-03, REQ-MEDIA-07, REQ-BILL-03]
dependencias: [HU-MEDIA-02, HU-BILL-04]
skills: ["claude-api", "data:statistical-analysis", "optimizer"]
estado: borrador
---

# HU-MEDIA-04 · Dispatcher de visión con prueba de conexión y benchmark

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-04](../spec.md) (D-SPEC-04-3).

**ID:** HU-MEDIA-04

**Título:** Dispatcher de visión con prueba de conexión y benchmark

**Workstream:** Multimodalidad

**Historia:** Como dueño de SolversHub quiero un dispatcher de visión que use el proveedor configurado por negocio, con prueba de conexión y un benchmark de comprobantes reales, para elegir el proveedor por datos y no por costumbre.

**Por qué importa (valor empresarial):** El OCR de comprobantes mueve dinero: un error de lectura aprueba un pago falso o rechaza uno real. Elegir el proveedor con un benchmark medido es la diferencia entre automatizar el cobro o seguir revisando a mano.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-MEDIA-03, REQ-MEDIA-07, REQ-BILL-03

**Dependencias:** [HU-MEDIA-02](HU-MEDIA-02-almacenamiento-media.md), HU-BILL-04

**Criterios de aceptación (Gherkin):**
- **Proveedores.** Dado la config del negocio, cuando se procesa una imagen, entonces se usa el proveedor elegido (Anthropic, DeepSeek u OpenAI) con llave de plataforma o propia.
- **Prueba de conexión.** Dado el panel, cuando el dueño pulsa "Probar", entonces se envía una imagen mínima y se muestra éxito o el error del proveedor.
- **Benchmark.** Dado al menos 30 comprobantes reales anonimizados de Nequi, Bancolombia y Daviplata, cuando corre el benchmark, entonces reporta exactitud de monto y cuenta, latencia y costo por proveedor.
- **Costo.** Dado cada llamada, cuando termina, entonces hay una fila `vision` en el ledger con los tokens reales.
- **Retiro de modelos.** Dado un modelo con fecha de retiro (Gemini 2.5 Flash-Lite, 2026-10-20), cuando se configura, entonces el panel avisa.

**Evidencia / Definición de Terminado:**
- Informe del benchmark en `solvershub-docs` y proveedor por defecto decidido.
- Tests con mocks de cada proveedor.

**Riesgos/Notas:**
- `agent-sale` descartaba el uso de tokens que devuelve la API (`callVisionModel.ts:53-54`): aquí se registra.
