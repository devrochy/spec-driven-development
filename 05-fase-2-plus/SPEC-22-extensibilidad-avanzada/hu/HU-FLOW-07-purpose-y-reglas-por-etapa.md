---
id: HU-FLOW-07
titulo: Edición avanzada del purpose y reglas por etapa
spec: SPEC-22
fase: 2
hito: "2"
workstream: Flujo visual
prioridad: P2
critico: false
estimacion: M
impacto: [diferenciacion, calidad_ia]
req: [REQ-FLOW-05]
dependencias: [HU-FLOW-05]
skills: ["eval-runner", "frontend-design", "panel-ui"]
estado: borrador
---

# HU-FLOW-07 · Edición avanzada del `purpose` y reglas por etapa

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-22](../spec.md) (P-09).

**ID:** HU-FLOW-07

**Título:** Edición avanzada del purpose y reglas por etapa

**Workstream:** Flujo visual

**Historia:** Como implementador quiero editar el texto de cada etapa y definir reglas de entrada y salida para ajustar finamente el comportamiento de asistentes complejos.

**Por qué importa (valor empresarial):** Los clientes grandes necesitan control fino; hacerlo con permiso y evals evita que un cambio de texto degrade la calidad.

**Prioridad:** P2 plus

**Estimación:** M

**REQ mapeados:** REQ-FLOW-05

**Dependencias:** [HU-FLOW-05](../../../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-05-borrador-y-publicacion.md)

**Criterios de aceptación (Gherkin):**
- **Permiso.** Dado un usuario sin permiso de implementador, cuando abre el editor, entonces el texto de las etapas es de solo lectura.
- **Evals.** Dado un cambio de texto, cuando se publica, entonces corre el golden set y bloquea si baja del umbral.
- **Reglas.** Dado una regla de salida ("solo pasar a Pago con pedido confirmado"), cuando se cumple, entonces el flujo avanza.

**Evidencia / Definición de Terminado:**
- Extensión del editor; tests.

**Riesgos/Notas:**
- El texto sigue en el AgentSpec (invariante 3).
