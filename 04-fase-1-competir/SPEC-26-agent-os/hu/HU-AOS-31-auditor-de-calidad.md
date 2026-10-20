---
id: HU-AOS-31
titulo: "Auditor de calidad y LLM-juez calibrado"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia]
req: [REQ-AOS-12]
dependencias: [HU-AOS-21, HU-AOS-28]
skills: ["eval-author", "data:statistical-analysis", "eval-runner"]
estado: borrador
---

# HU-AOS-31 · Auditor de calidad y LLM-juez calibrado

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-31

**Título:** Auditor de calidad y LLM-juez calibrado

**Workstream:** Agent OS

**Historia:** Como responsable de calidad quiero que cada noche se revise una muestra de conversaciones reales con una rúbrica calibrada contra personas, para detectar en producción lo que las pruebas no cubren.

**Por qué importa (valor empresarial):** Cierra la brecha entre simulación y realidad (Nubank, 2026): la producción alimenta las pruebas.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-12

**Dependencias:** [HU-AOS-21](HU-AOS-21-gate-de-release-pass-k.md), [HU-AOS-28](HU-AOS-28-depurador-y-en-curso.md)

**Criterios de aceptación (Gherkin):**
- **Calibración.** Dado 100 conversaciones etiquetadas por personas, cuando el juez las califica, entonces el acuerdo es mayor o igual al umbral de P-23 antes de usarlo.
- **Muestra.** Dado el tráfico del día, cuando corre el auditor, entonces evalúa una muestra estratificada por superpoder y guarda `turn_feedback`.
- **A pruebas.** Dado una conversación mal calificada, cuando se revisa, entonces puede convertirse en escenario de usuario simulado.

**Evidencia / Definición de Terminado:**
- Rúbrica versionada; agente auditor en back-office; reporte nocturno.

**Riesgos/Notas:**
- Etiquetar consume tiempo del dueño (P-24): muestra pequeña y bien elegida.
