---
id: HU-QA-02
titulo: Catálogo versionado desde docs
spec: SPEC-30
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: S
impacto: ["operacion"]
req: [REQ-ARCH-22]
dependencias: [HU-QA-01]
skills: ["agentcore-conventions", "backend-design:idempotency-and-side-effects"]
estado: terminada
---

# HU-QA-02 · Catálogo versionado desde docs

> Estado SDD: Lista para ejecutar — [SPEC-30](../spec.md) en Diseño aprobado (D-33).

**ID:** HU-QA-02

**Título:** Catálogo versionado desde docs

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño quiero importar `11-pruebas/catalogo.yaml` de solvershub-docs al panel para que las pruebas se versionen con git junto a cada HU.

**Por qué importa (valor empresarial):** El catálogo se revisa en el mismo PR que la HU; el panel solo guarda resultados.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-ARCH-22

**Dependencias:** [HU-QA-01](HU-QA-01-modelo-y-api-de-pruebas.md)

**Criterios de aceptación (Gherkin):**
- **Importar.** Dado el `catalogo.yaml` versión 2, cuando el dueño corre `agent-core qa importar` (o `POST /admin/qa/catalog/import`), entonces queda una versión nueva con todas sus pruebas y el ciclo abierto la usa.
- **Idempotente.** Dado un catálogo ya importado, cuando se vuelve a importar el mismo archivo, entonces no se duplica.
- **Esquema v1 y v2.** Dado un ítem con pasos en texto (v1) y otro con pasos `{accion, esperado}` (v2), cuando se importan, entonces ambos se muestran paso a paso.
- **Historia por slug.** Dado un ciclo cerrado con la versión 1, cuando se importa la versión 2, entonces el ciclo cerrado conserva la versión 1 y las pruebas con el mismo `id` mantienen su historial.

**Evidencia / Definición de Terminado:**
- Tests del importador (v1, v2, idempotencia, errores de esquema); importación real del catálogo en test.

**Riesgos/Notas:**
- El YAML valida su esquema también en el CI de docs (`regenerar.py --check`).
