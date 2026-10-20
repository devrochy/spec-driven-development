---
id: HU-INMO-25
titulo: "Preset inmobiliaria, golden y journeys de la vertical"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, calidad_ia]
req: [REQ-INMO-12]
dependencias: [HU-INMO-17, HU-INMO-18, HU-INMO-19, HU-INMO-24, HU-ARCH-28]
skills: ["eval-author", "onboard-tenant", "customizer", "eval-runner"]
estado: borrador
---

# HU-INMO-25 · Preset inmobiliaria, golden y journeys de la vertical

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-25

**Título:** Preset inmobiliaria, golden y journeys de la vertical

**Workstream:** Verticales

**Historia:** Como inmobiliaria nueva quiero activar un asistente inmobiliario completo con un preset, y como equipo de SolversHub quiero medir su consistencia cada noche, para vender la vertical sin desarrollo a medida.

**Por qué importa (valor empresarial):** El preset convierte la vertical en producto replicable (constitución §1.2.2); el golden y los journeys evitan regresiones.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-12

**Dependencias:** [HU-INMO-17](HU-INMO-17-fichas-y-verificacion-de-hechos.md), [HU-INMO-18](HU-INMO-18-captacion-de-propietarios.md), [HU-INMO-19](HU-INMO-19-visitas-con-el-asesor.md), [HU-INMO-24](HU-INMO-24-mora-e-incremento-del-canon.md), [HU-ARCH-28](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md)

**Criterios de aceptación (Gherkin):**
- **Preset.** Dado un negocio nuevo, cuando se crea con `--preset inmobiliaria --plan <plan>`, entonces quedan activos los cuatro packs con su configuración y sus pasos de activación.
- **Golden.** Dado el set `inmobiliaria-base`, cuando corre el nightly con k = 4, entonces pass^4 ≥ 0,85 y pass@1 ≥ 95 %.
- **Journeys.** Dado el set de journeys `inmobiliaria`, cuando corre, entonces cubre búsqueda → visita, captación, canon con pago y mora, y verifica el estado en las tablas.

**Evidencia / Definición de Terminado:**
- `core/presets/inmobiliaria.json` y fragmentos por pack; golden y journeys en `evals/`; nightly en verde tres noches.

**Riesgos/Notas:**
- Fase INMO 4 · Arriendos y medición.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- [HU-FWK-11](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-11-presets-adicionales.md) remite aquí para la inmobiliaria.
