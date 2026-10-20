---
id: HU-AOS-27
titulo: "Versiones: diferencias, probar, publicar y revertir"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-AOS-10, REQ-AOS-13]
dependencias: [HU-AOS-14, HU-AOS-21, HU-AOS-23]
skills: ["panel-ui", "frontend-design"]
estado: borrador
---

# HU-AOS-27 · Versiones: diferencias, probar, publicar y revertir

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-27

**Título:** Versiones: diferencias, probar, publicar y revertir

**Workstream:** Agent OS

**Historia:** Como dueño quiero ver qué cambia entre versiones, probar la candidata y publicarla a una parte o a todos, o volver atrás con un clic, para cambiar con control.

**Por qué importa (valor empresarial):** "Rollback siempre" llega a manos del dueño, no solo del CLI.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-10, REQ-AOS-13

**Dependencias:** [HU-AOS-14](HU-AOS-14-releases-por-conexion.md), [HU-AOS-21](HU-AOS-21-gate-de-release-pass-k.md), [HU-AOS-23](HU-AOS-23-consola-de-conexiones.md)

**Criterios de aceptación (Gherkin):**
- **Diferencias.** Dado una candidata, cuando abre "Ver diferencias", entonces ve los cambios en lenguaje claro agrupados por agente, superpoder y permisos.
- **Publicar con gate.** Dado una candidata sin pruebas aprobadas, cuando intenta publicar, entonces la acción no está disponible y se explica por qué.
- **Revertir.** Dado la versión activa, cuando vuelve a la anterior y confirma, entonces se aplica en ≤ 5 s y se explica qué pasa con las conversaciones abiertas.
- **Candidata de la plataforma.** Dado una candidata `origin = platform` (versión nueva de una habilidad), cuando el dueño abre Versiones, entonces ve el aviso con sus diferencias y puede detenerla.

**Evidencia / Definición de Terminado:**
- Diff semántico y badge de versión; confirmación con consecuencia; tests.

**Riesgos/Notas:**
- Publicar a una parte requiere [HU-AOS-32](HU-AOS-32-canary-y-auto-rollback.md); antes, solo "a todos", tras probar la candidata en el playground (ADR-0075).
