---
id: HU-FWK-02
titulo: ADR de presets de agente
spec: SPEC-05
fase: 0
hito: 0A
workstream: Framework/Plugins
prioridad: P0
critico: true
estimacion: S
impacto: [diferenciacion, operacion]
req: [REQ-FWK-02]
dependencias: [HU-FWK-01]
skills: ["adr", "doc-coauthoring", "arquitecto"]
ola: 2
estado: terminada
---

# HU-FWK-02 · ADR de presets de agente

> Estado SDD: Terminada — ADR-0110 aceptado el 2026-10-08 (issue [core #283](https://github.com/devrochy/agent-core/issues/283)).

**ID:** HU-FWK-02

**Título:** ADR de presets de agente

**Workstream:** Framework/Plugins

**Historia:** Como responsable técnico quiero un ADR que defina qué es un preset, qué contiene, cómo se versiona y cómo se aplica para que el alta automática y los presets futuros sigan una sola regla.

**Por qué importa (valor empresarial):** El preset instala agentes; la unidad que se vende es el agente ([D-35](../../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes); antes esta línea decía «el preset es la unidad que se vende»). Un preset («asistente para restaurantes», «planes y suscripciones») deja al negocio con sus agentes «para un fin» listos ([HU-AOS-46](../../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md)). Definirlo bien desde el principio evita forks por cliente (invariante 2) y permite crecer el catálogo sin deuda.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-FWK-02

**Dependencias:** [HU-FWK-01](HU-FWK-01-composicion-de-flujos.md)

**Criterios de aceptación (Gherkin):**
- **Contenido.** Dado el ADR, cuando se revisa, entonces define el manifiesto del preset (packs, playbooks, persona, conexiones, pasos de activación, plan mínimo, golden set), los fragmentos que declara cada pack (`flow.json`, `seed_data`, `default_config`), la versión y la regla "sin prompts, solo referencias a playbooks" (D-SPEC-05-1 = B).
- **Aplicación.** Dado el ADR, cuando se lee, entonces describe los 6 pasos de `apply_preset`, qué pasa con packs que exigen claves y cómo se audita.
- **Orden de personalización.** Dado el ADR, cuando se lee, entonces explica dónde encaja el preset en el orden configuración → pack → plugin del tenant → topología.

**Evidencia / Definición de Terminado:**
- ADR aceptado en `agent-core/docs/adr/` (`solvershub-core` tras [HU-REP-02](../../SPEC-00-reestructuracion/hu/HU-REP-02-renombre-cosmetico.md)) y `docs/ASSISTANT-OS.md` actualizado.

**Terminada (2026-10-08):** [agent-core #284](https://github.com/devrochy/agent-core/pull/284): ADR-0110 «Presets de agente» (manifiesto corto en `core/presets/` + fragmentos por pack y vertical con config sin secretos y `seed` para el hook `seed_data` de ADR-0083; `apply_preset` idempotente en 6 pasos; packs con claves pendientes sin romper el alta; `tenants.settings["preset"]` + `audit_log`; el preset es configuración, no código). `docs/ASSISTANT-OS.md` con sección de presets y la de flujo al día con ADR-0109.

**Riesgos/Notas:**
- Las opciones B y C de D-SPEC-05-1 quedan documentadas como descartadas.
