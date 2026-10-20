---
id: HU-FWK-11
titulo: Presets adicionales de agendamiento, marketing y atención
spec: SPEC-16
fase: 1
hito: "1"
workstream: Framework/Plugins
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-FWK-02]
dependencias: [HU-FWK-10]
skills: ["new-pack", "eval-author", "customizer"]
estado: borrador
---

# HU-FWK-11 · Presets adicionales de agendamiento, marketing y atención

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-16](../spec.md).

**ID:** HU-FWK-11

**Título:** Presets adicionales de agendamiento, marketing y atención

**Workstream:** Framework/Plugins

**Historia:** Como clínica, inmobiliaria o negocio de servicios quiero un preset listo para mi caso (agendar, captar leads, responder preguntas) para tener un asistente útil desde el primer día.

**Por qué importa (valor empresarial):** Cada preset nuevo abre un segmento de mercado sin desarrollo a medida. Lety compite con 12 verticales preconfiguradas; los presets son nuestra respuesta.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FWK-02

**Dependencias:** [HU-FWK-10](HU-FWK-10-aplicar-preset-desde-panel.md)

**Criterios de aceptación (Gherkin):**
- **Agendamiento.** Dado el preset de agendamiento, cuando se aplica, entonces el asistente agenda, reagenda y recuerda citas con su flujo y golden set base.
- **Marketing y leads.** Dado el preset de marketing, cuando se aplica, entonces captura y califica leads con formulario alojado y seguimiento.
- **Atención y preguntas frecuentes.** Dado el preset de atención, cuando se aplica, entonces responde con la base de conocimiento del negocio y escala.

**Evidencia / Definición de Terminado:**
- Tres presets registrados con golden set base cada uno.

**Riesgos/Notas:**
- El de marketing con campañas depende de [HU-CHAN-03](../../SPEC-17-canales-y-campanas/hu/HU-CHAN-03-pack-marketing.md).
- La inmobiliaria tiene su propia vertical en [SPEC-28](../../SPEC-28-inmoagent/spec.md): su preset es [HU-INMO-25](../../SPEC-28-inmoagent/hu/HU-INMO-25-preset-golden-y-journeys.md). Esta HU cubre agendamiento, marketing y atención genéricos.
