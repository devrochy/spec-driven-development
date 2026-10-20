---
id: HU-AOS-45
titulo: "Editor de estructura de superpoderes para el negocio"
spec: SPEC-27
fase: 2
hito: "2"
workstream: Agent OS
prioridad: P2
critico: false
estimacion: L
impacto: [diferenciacion]
req: [REQ-AOS-03, REQ-AOS-13]
dependencias: [HU-AOS-25]
skills: ["panel-ui", "frontend-design"]
estado: borrador
---

# HU-AOS-45 · Editor de estructura de superpoderes para el negocio

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-27](../spec.md).

**ID:** HU-AOS-45

**Título:** Editor de estructura de superpoderes para el negocio

**Workstream:** Agent OS

**Historia:** Como dueño avanzado o implementador quiero crear y modificar la estructura de un superpoder (pasos, datos y confirmaciones) para casos propios, con validación y pruebas.

**Por qué importa (valor empresarial):** Lleva el Agent OS a casos a medida sin código ni fork (invariante 2).

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-AOS-03, REQ-AOS-13

**Dependencias:** [HU-AOS-25](../../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md)

**Criterios de aceptación (Gherkin):**
- **Linter en vivo.** Dado un cambio de estructura, cuando agrega una acción irreversible sin confirmación, entonces el editor lo marca y no deja guardar.
- **Prueba obligatoria.** Dado un superpoder editado, cuando intenta publicarlo, entonces exige sus escenarios y pass^k.
- **Propiedad del negocio.** Dado un superpoder propio, cuando se guarda, entonces queda con scope del negocio y no afecta a otros.

**Evidencia / Definición de Terminado:**
- Editor de estructura; procedimientos propios del negocio versionados; tests.

**Riesgos/Notas:**
- Complejidad para no técnicos: solo para implementadores o el master al principio (P-09).
