---
id: HU-SH-08
titulo: Golden set E2E del asistente SolversHub y canary
spec: SPEC-07
fase: 0
hito: 0A
workstream: Asistente SolversHub
prioridad: P0
critico: true
estimacion: M
impacto: [calidad_ia, ingreso]
req: [REQ-SH-01, REQ-ARCH-10]
dependencias: [HU-SH-01, HU-SH-02, HU-SUB-12, HU-ARCH-28]
skills: ["eval-author", "eval-runner"]
ola: 4
estado: borrador
---

# HU-SH-08 · Golden set E2E del asistente SolversHub y canary

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-07](../spec.md).

**ID:** HU-SH-08

**Título:** Golden set E2E del asistente SolversHub y canary

**Workstream:** Asistente SolversHub

**Historia:** Como dueño de SolversHub quiero journeys automáticos de la demo al alta y un canary con cada cambio para saber que el vendedor de la empresa sigue funcionando antes de que lo pruebe un prospecto real.

**Por qué importa (valor empresarial):** Si el asistente de SolversHub falla, la empresa deja de vender y además da la peor demo posible de su propio producto. Es el criterio de salida del Hito 0A: ≥95 % durante 3 noches.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-SH-01, REQ-ARCH-10

**Dependencias:** [HU-SH-01](HU-SH-01-tenant-reproducible.md), [HU-SH-02](HU-SH-02-demo-de-punta-a-punta.md), HU-SUB-12, [HU-ARCH-28](../../SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md)

**Criterios de aceptación (Gherkin):**
- **Cobertura.** Dado el golden set del tenant, cuando se revisa, entonces cubre al menos: preguntar planes, prueba gratis, agendar y reagendar demo, comprar Free, comprar un plan pago con pago simulado, alta del negocio, objeciones de precio, pedir humano, intento de descuento y spam.
- **Multi-turno.** Dado cada journey, cuando corre, entonces usa el runner de HU-SUB-12 y verifica tools, estados y el negocio creado.
- **Umbral.** Dado el nightly, cuando corre 3 noches seguidas, entonces pasa ≥95 %.
- **Canary.** Dado un cambio de spec, de playbook o de modelo, cuando se publica, entonces corre un subconjunto del golden set antes de activarse y se revierte si baja del umbral.

**Evidencia / Definición de Terminado:**
- Escenarios versionados en `tenants/solvershub/evals/`; reporte de 3 noches; canary documentado.

**Riesgos/Notas:**
- Reemplaza los 8 escenarios actuales de un solo turno.
