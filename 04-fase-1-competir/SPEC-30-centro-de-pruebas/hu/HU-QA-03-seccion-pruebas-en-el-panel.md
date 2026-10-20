---
id: HU-QA-03
titulo: Sección Pruebas en el panel
spec: SPEC-30
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: ["confianza", "operacion"]
req: [REQ-ARCH-22]
dependencias: [HU-QA-01]
skills: ["panel-ui", "frontend-design", "built-in-browser"]
estado: terminada
---

# HU-QA-03 · Sección Pruebas en el panel

> Estado SDD: Lista para ejecutar — [SPEC-30](../spec.md) en Diseño aprobado (D-33).

**ID:** HU-QA-03

**Título:** Sección Pruebas en el panel

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño o tester quiero una sección Pruebas con la lista de pruebas a un lado, la ejecución paso a paso al otro, mi progreso a la vista y un informe al final para ejecutar y seguir las pruebas en un solo lugar.

**Por qué importa (valor empresarial):** Reemplaza el artifact con una pantalla del producto, interactiva y con evidencia, con el kit y la navegación de [SPEC-29](../../SPEC-29-sistema-de-diseno-unificado/spec.md).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-22

**Dependencias:** [HU-QA-01](HU-QA-01-modelo-y-api-de-pruebas.md)

**Criterios de aceptación (Gherkin):**
- **Lista y ejecución.** Dado un tester en Plataforma › Pruebas, cuando elige una prueba en la lista lateral, entonces a la derecha ve su contexto, precondiciones, datos y el primer paso con su resultado esperado.
- **Paso a paso.** Dado el paso 1 de una prueba, cuando pulsa «Aprobar» (o la tecla A), entonces el paso queda guardado, el panel muestra «Guardado» y pasa al paso 2.
- **Captura pegada.** Dado un paso en falla, cuando el tester pega una captura con Ctrl+V, entonces aparece la miniatura y queda adjunta al paso.
- **Progreso.** Dado un tester que terminó 3 de 10 pruebas, cuando mira la cabecera, entonces ve 3/10 con el desglose OK, Falla y Bloqueada, y el avance del ciclo.
- **Informe.** Dado un tester con pruebas en falla, cuando pulsa «Enviar informe», entonces ve una vista previa con las fallas, sus notas y capturas, y al confirmar su ejecución queda en solo lectura con el informe para imprimir o descargar.
- **Ciclos.** Dado un ciclo cerrado, cuando el dueño abre la pestaña Ciclos, entonces ve el resumen y los resultados de ese ciclo sin poder editarlos.

**Evidencia / Definición de Terminado:**
- Capturas a 375 y 1280 px en claro y oscuro; axe sin violaciones graves; tests de los componentes y de la lógica de progreso; recorrido completo en el navegador contra el backend.

**Riesgos/Notas:**
- Reutiliza `Badge`, `Tabs`, `Sheet`, `ProgressRing`, `useConfirm` y la paleta Ctrl+K; agrega `Progress`, `Stepper` y `Dropzone` al kit.
