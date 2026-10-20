---
id: HU-AOS-46
titulo: "Presets v2: plantillas de agente, reglas del Coordinador y permisos"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, operacion]
req: [REQ-AOS-05, REQ-FWK-02]
dependencias: [HU-AOS-16, HU-FWK-10]
skills: ["adr", "arquitecto", "agentcore-conventions"]
estado: en-curso
---

# HU-AOS-46 · Presets v2: plantillas de agente, reglas del Coordinador y permisos

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-46

**Título:** Presets v2: plantillas de agente, reglas del Coordinador y permisos

**Workstream:** Agent OS

**Historia:** Como dueño quiero que un preset instale los agentes especialistas, las reglas del Coordinador y los permisos de colaboración de mi tipo de negocio, para tener un asistente listo con el Agent OS sin armarlo a mano.

**Por qué importa (valor empresarial):** Los presets (ADR-0110) habilitan packs en el AgentSpec v2, pero ADR-0113 saca `packs` del contrato v3 y ningún documento dice cómo un preset crea agentes desde plantillas ni el KernelSpec. Sin esto, los presets que ya existen (comercio, restaurante, cobranza, suscripciones) dejan de servir para vender el Agent OS.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-05, REQ-FWK-02

**Dependencias:** [HU-AOS-16](HU-AOS-16-habilidades-con-procedimientos-y-scope.md), [HU-FWK-10](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-10-aplicar-preset-desde-panel.md)

**Criterios de aceptación (Gherkin):**
- **Instalar.** Dado un preset v2, cuando se aplica a una conexión, entonces crea los agentes desde sus plantillas, las reglas del Coordinador y los permisos de colaboración en una release nueva, sin activarla.
- **Presets v1.** Dado un preset v1 (comercio, cobranza), cuando se aplica con el Agent OS activo, entonces sigue funcionando con el agente General.
- **Idempotencia.** Dado un preset ya aplicado, cuando se vuelve a aplicar, entonces no duplica agentes ni pisa lo que el dueño cambió.

**Evidencia / Definición de Terminado:**
- ADR nuevo que enmienda ADR-0110 sobre AgentSpec v3; `PresetManifest` v2; tests con los presets existentes.

**Riesgos/Notas:**
- Nació en la revisión de [SPEC-28](../../SPEC-28-inmoagent/spec.md) (2026-10-09): el hueco afecta a todos los presets, no solo a la vertical inmobiliaria.
