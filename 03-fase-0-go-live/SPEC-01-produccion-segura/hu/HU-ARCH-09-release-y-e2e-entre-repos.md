---
id: HU-ARCH-09
titulo: Release y pruebas E2E entre repos antes de promover a producción
spec: SPEC-01
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-ARCH-19, REQ-UX-06]
dependencias: [HU-ARCH-01]
skills: ["built-in-browser", "backend-design:testing-with-discernment", "desplegar-test-agent-core"]
estado: borrador
---

# HU-ARCH-09 · Release y pruebas E2E entre repos antes de promover a producción

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-01](../spec.md).

**ID:** HU-ARCH-09

**Título:** Release y pruebas E2E entre repos antes de promover a producción

**Workstream:** Arquitectura/Prod

**Historia:** Como operador quiero que cada release pase un smoke E2E con el backend y el panel reales en test antes de promover la misma imagen a producción para no romper a los clientes con un cambio entre repos.

**Por qué importa (valor empresarial):** El panel y el backend viven en repos distintos y se rompen entre sí (tipos desalineados, rutas cambiadas). Un smoke E2E evita que un cliente descubra el error en producción.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-19, REQ-UX-06

**Dependencias:** [HU-ARCH-01](HU-ARCH-01-produccion-fuera-de-dev.md)

**Criterios de aceptación (Gherkin):**
- **Imagen inmutable.** Dado un commit en `main`, cuando se construye, entonces la misma imagen etiquetada se despliega en test y luego en producción.
- **Smoke E2E.** Dado el despliegue en test, cuando corre Playwright, entonces valida login, cambio de negocio, probar asistente con sandbox, lista de conexiones y un pedido de prueba.
- **Contrato de API.** Dado un cambio en `openapi.json`, cuando los tipos del panel no se regeneraron, entonces el CI falla.
- **Promoción manual.** Dado el smoke en verde, cuando el operador aprueba, entonces se promueve; si falla, se bloquea.

**Evidencia / Definición de Terminado:**
- Workflow de release documentado en `solvershub-infra`.
- Reporte de Playwright de una corrida verde.

**Riesgos/Notas:**
- Las pruebas internas del panel (Testing Library, axe) son de [HU-UI-04](../../SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md); esta HU cubre la integración entre repos.
