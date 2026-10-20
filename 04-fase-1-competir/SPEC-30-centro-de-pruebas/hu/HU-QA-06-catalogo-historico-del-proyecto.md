---
id: HU-QA-06
titulo: Catálogo histórico del proyecto
spec: SPEC-30
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: L
impacto: ["confianza", "operacion"]
req: [REQ-ARCH-22]
dependencias: []
skills: ["ejecutar-hu", "doc-coauthoring"]
estado: borrador
---

# HU-QA-06 · Catálogo histórico del proyecto

> Estado SDD: Lista para ejecutar — [SPEC-30](../spec.md) en Diseño aprobado (D-33).

**ID:** HU-QA-06

**Título:** Catálogo histórico del proyecto

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño quiero que el catálogo de pruebas documente todo lo construido desde el inicio del proyecto, con pasos y resultado esperado, para que un tester sin contexto pueda verificar el producto completo.

**Por qué importa (valor empresarial):** Hoy el catálogo cubre 3 de las 72 HU terminadas; sin las pruebas del resto, un ciclo no dice si el producto entero funciona.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-ARCH-22

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Cobertura de HU.** Dado que una HU está en estado `terminada` o `en-curso` y tiene comportamiento visible, cuando se busca en el catálogo, entonces tiene al menos una prueba con su `id` en `hu`.
- **Antes de SDD.** Dado un caso de `solvershub-comercial/PLAN-DE-PRUEBAS.md`, cuando se busca en el catálogo, entonces está cubierto (con su ID en `origen`) o anotado como absorbido por otra prueba.
- **Paso a paso.** Dado que un tester elige cualquier prueba del catálogo, cuando la abre, entonces cada paso trae una acción y su resultado esperado, más precondiciones y datos de prueba sin secretos.
- **Validado.** Dado un PR de docs que cambia el catálogo, cuando corre el CI, entonces `regenerar.py --check` rechaza ids duplicados, HU inexistentes o campos faltantes.

**Evidencia / Definición de Terminado:**
- Catálogo v2 en 2 o 3 PRs (panel y plataforma; app, agenda y cobros; anterior a SDD y guía 0A), con conteo de cobertura por HU en el README de `11-pruebas`.

**Riesgos/Notas:**
- Las fuentes son los criterios Gherkin de las HU, el plan de pruebas del panel anterior a SDD, la guía del 0A y las pruebas actuales; lo que solo se verifica en CI (migraciones, evals) no entra.
