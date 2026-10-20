---
id: HU-FLOW-04
titulo: Editor visual del flujo con arrastrar y soltar accesible
spec: SPEC-15
fase: 1
hito: "1"
workstream: Flujo visual
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion]
req: [REQ-FLOW-02]
dependencias: [HU-FLOW-03, HU-UI-03]
skills: ["frontend-design", "figma-design-to-code", "built-in-browser", "panel-ui"]
estado: parqueada
---

# HU-FLOW-04 · Editor visual del flujo con arrastrar y soltar accesible

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-15](../spec.md) (D-SPEC-15-2).

**ID:** HU-FLOW-04

**Título:** Editor visual del flujo con arrastrar y soltar accesible

**Workstream:** Flujo visual

**Historia:** Como dueño de un negocio quiero ver las etapas de mi asistente en columnas y mover, agregar o quitar las acciones de cada habilidad con el mouse o el teclado para adaptar el comportamiento sin escribir archivos.

**Por qué importa (valor empresarial):** Es el diferencial visible del encargo 3.3 y la paridad con los flow builders de Hubtype y SleekFlow, pero sobre el modelo de habilidades de SolversHub.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-FLOW-02

**Dependencias:** [HU-FLOW-03](HU-FLOW-03-validador-y-api.md), [HU-UI-03](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md)

**Criterios de aceptación (Gherkin):**
- **Columnas.** Dado mi flujo, cuando abro el editor, entonces veo una columna por etapa con tarjetas de acción y una bandeja "Sin asignar".
- **Arrastrar.** Dado una tarjeta, cuando la arrastro a otra etapa, entonces se mueve y el borrador se marca con cambios.
- **Teclado.** Dado el teclado, cuando selecciono una tarjeta y uso las flechas, entonces puedo moverla igual que con el mouse.
- **Errores.** Dado un error del validador, cuando guardo, entonces se marca la etapa con el problema.
- **Vista previa.** Dado el borrador, cuando abro la vista previa, entonces veo el bloque de instrucciones que recibirá el asistente.

**Evidencia / Definición de Terminado:**
- Página del editor; tests de componentes; prueba con un dueño de negocio.

**Riesgos/Notas:**
- Respeta `DESIGN.md` (animaciones ≤200 ms, tokens).
