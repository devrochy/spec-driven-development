---
id: HU-QA-05
titulo: Migrar resultados desde el artifact
spec: SPEC-30
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: S
impacto: ["operacion"]
req: [REQ-ARCH-22]
dependencias: [HU-QA-02, HU-QA-03]
skills: ["migrator", "backend-design:idempotency-and-side-effects"]
estado: borrador
---

# HU-QA-05 · Migrar resultados desde el artifact

> Estado SDD: Lista para ejecutar — [SPEC-30](../spec.md) en Diseño aprobado (D-33).

**ID:** HU-QA-05

**Título:** Migrar resultados desde el artifact

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño quiero pasar al panel los resultados y el historial del artifact «Camino a producción» para no perder lo que ya se probó.

**Por qué importa (valor empresarial):** Cierra la etapa provisoria sin rehacer pruebas.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-ARCH-22

**Dependencias:** [HU-QA-02](HU-QA-02-catalogo-versionado-desde-docs.md), [HU-QA-03](HU-QA-03-seccion-pruebas-en-el-panel.md)

**Criterios de aceptación (Gherkin):**
- **Migración.** Dado el artifact con resultados del ciclo abierto, cuando se corre la migración, entonces el panel muestra los mismos estados, notas e historial.
- **Ciclos cerrados.** Dado un ciclo cerrado en el artifact, cuando se migra, entonces aparece en Ciclos con su resumen y su foto de resultados.
- **Prueba con usuarios.** Dados los 5 participantes del artifact, cuando se migran, entonces sus tiempos y resultados quedan en el panel.

**Evidencia / Definición de Terminado:**
- Conteos iguales entre el artifact y el panel; capturas del antes y después.

**Riesgos/Notas:**
- Después el artifact queda en solo lectura con un enlace a Plataforma › Pruebas.
