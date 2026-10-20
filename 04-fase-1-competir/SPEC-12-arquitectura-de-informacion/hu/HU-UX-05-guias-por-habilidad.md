---
id: HU-UX-05
titulo: Guías por habilidad y por preset
spec: SPEC-12
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-UX-02]
dependencias: [HU-SH-06, HU-FWK-04]
skills: ["frontend-design", "new-pack", "panel-ui"]
estado: borrador
---

# HU-UX-05 · Guías por habilidad y por preset

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-12](../spec.md).

**ID:** HU-UX-05

**Título:** Guías por habilidad y por preset

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio que activa una habilidad nueva (por ejemplo, cobranza o suscripciones) quiero una guía corta con los pasos y datos de ejemplo para dejarla funcionando sin ayuda.

**Por qué importa (valor empresarial):** Cada habilidad activada y bien configurada es más valor percibido y más razones para subir de plan. Lety vende 12 verticales preconfiguradas; las guías hacen lo mismo con nuestros presets.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-02

**Dependencias:** [HU-SH-06](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md), [HU-FWK-04](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md)

**Criterios de aceptación (Gherkin):**
- **Checklist por habilidad.** Dado una habilidad recién activada, cuando entro, entonces veo sus pasos (declarados en sus metadatos) y su avance.
- **Datos de ejemplo.** Dado la guía, cuando pulso "Cargar ejemplo", entonces se cargan datos de prueba marcados que puedo borrar.
- **Por preset.** Dado un negocio creado con un preset, cuando entra, entonces la guía sigue el orden del preset.

**Evidencia / Definición de Terminado:**
- Metadatos de guía en los packs; componente de guía; tests.

**Riesgos/Notas:**
- Los datos de ejemplo usan `seed_data` ([HU-FWK-03](../../../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md), HU-SUB-11).
