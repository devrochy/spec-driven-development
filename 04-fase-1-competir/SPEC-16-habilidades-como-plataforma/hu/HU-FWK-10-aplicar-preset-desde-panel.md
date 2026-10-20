---
id: HU-FWK-10
titulo: Aplicar un preset desde el panel con diff
spec: SPEC-16
fase: 1
hito: "1"
workstream: Framework/Plugins
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-FWK-02]
dependencias: [HU-FWK-03, HU-FWK-04]
skills: ["onboard-tenant", "frontend-design"]
estado: borrador
---

# HU-FWK-10 · Aplicar un preset desde el panel con diff

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-16](../spec.md).

**ID:** HU-FWK-10

**Título:** Aplicar un preset desde el panel con diff

**Workstream:** Framework/Plugins

**Historia:** Como dueño de un negocio existente quiero aplicar un preset (por ejemplo "Planes y suscripciones") y ver antes qué cambiará para agregarle un superpoder a mi asistente con seguridad.

**Por qué importa (valor empresarial):** Es la venta de expansión: llevar a clientes actuales a nuevos casos de uso con un clic. El diff evita el miedo a romper lo que ya funciona.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FWK-02

**Dependencias:** [HU-FWK-03](../../../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md), [HU-FWK-04](HU-FWK-04-catalogo-de-habilidades.md)

**Criterios de aceptación (Gherkin):**
- **Previsualizar.** Dado un preset, cuando lo previsualizo, entonces veo habilidades, configuración, datos de ejemplo y flujo que cambiarán.
- **Aplicar.** Dado confirmar, cuando se aplica, entonces se crea una versión nueva del AgentSpec reversible y queda auditado.
- **Plan.** Dado un preset que requiere un plan superior, cuando lo intento, entonces se me ofrece cambiar de plan.

**Evidencia / Definición de Terminado:**
- Endpoint de previsualización y aplicación; UI; tests.

**Riesgos/Notas:**
- El diff del flujo lo aporta [HU-FLOW-06](../../SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-06-flujo-semilla-por-preset.md).
