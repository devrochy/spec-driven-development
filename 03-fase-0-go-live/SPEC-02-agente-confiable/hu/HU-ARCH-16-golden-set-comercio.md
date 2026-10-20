---
id: HU-ARCH-16
titulo: Golden set y journeys multi-turno de comercio
spec: SPEC-02
fase: 0
hito: 0B
workstream: Comercio y suscripciones
prioridad: P0
critico: true
estimacion: L
impacto: [calidad_ia, ingreso]
req: [REQ-ARCH-10]
dependencias: [HU-COM-01, HU-COM-02, HU-FWK-01, HU-SUB-12]
skills: ["eval-author", "eval-runner"]
estado: borrador
---

# HU-ARCH-16 · Golden set y journeys multi-turno de comercio

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-02](../spec.md).

**ID:** HU-ARCH-16

**Título:** Golden set y journeys multi-turno de comercio

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de una tienda o restaurante quiero que el asistente esté probado en conversaciones completas de compra para confiar en que no inventa precios ni confirma pedidos que no existen.

**Por qué importa (valor empresarial):** Comercio es el vertical grande del mercado. Un solo pedido mal confirmado destruye la confianza del primer cliente; la meta de ≥95 % medida en conversaciones completas es la promesa de calidad del go-live.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** L

**REQ mapeados:** REQ-ARCH-10

**Dependencias:** [HU-COM-01](../../SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md), [HU-COM-02](../../SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md), [HU-FWK-01](../../SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md), HU-SUB-12

**Criterios de aceptación (Gherkin):**
- **Cobertura.** Dado el golden set de comercio, cuando se revisa, entonces tiene al menos 15 journeys: consulta, recomendación, cotización, promoción, pedido con domicilio y con retiro, pago en línea simulado, transferencia, estado del pedido, cancelación, monto alto, fuera de stock, foto de producto y escalamiento.
- **Umbral.** Dado el nightly, cuando corre 3 noches seguidas, entonces el pase es ≥95 % y se guarda por versión del spec.
- **Sin invenciones.** Dado cualquier journey, cuando el asistente menciona un monto, entonces coincide con el calculado por el servidor.

**Evidencia / Definición de Terminado:**
- Escenarios en `evals/golden_scenarios/` y gate en CI.
- Reporte de 3 noches.

**Riesgos/Notas:**
- Usa el runner de journeys de HU-SUB-12 (eventos y reloj simulados).
