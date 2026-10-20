---
id: HU-UX-04
titulo: Estados vacíos con acción y permisos coherentes
spec: SPEC-12
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-UX-03]
dependencias: [HU-UX-02]
skills: ["frontend-design", "backend-design:auth-and-authorization", "panel-ui"]
estado: borrador
---

# HU-UX-04 · Estados vacíos con acción y permisos coherentes

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-12](../spec.md).

**ID:** HU-UX-04

**Título:** Estados vacíos con acción y permisos coherentes

**Workstream:** UX/Onboarding

**Historia:** Como colaborador con permisos limitados quiero ver solo lo que puedo hacer y, en una lista vacía, saber qué hacer a continuación para no chocar con errores ni pantallas en blanco.

**Por qué importa (valor empresarial):** Un 403 por diseño o una tabla vacía sin explicación hacen que el panel parezca roto. Las acciones ocultas según el permiso son también un control de seguridad.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-03

**Dependencias:** [HU-UX-02](HU-UX-02-menu-v2.md)

**Criterios de aceptación (Gherkin):**
- **Vacío con acción.** Dado una lista sin datos (productos, conexiones, citas), cuando la abro, entonces veo qué es y un botón para crear el primero.
- **Sin 403.** Dado un colaborador sin permiso de escritura, cuando abre una vista, entonces no ve botones que lo llevarían a un 403.
- **Permisos desde el backend.** Dado cada vista, cuando carga, entonces recibe del backend las acciones permitidas para ese usuario.

**Evidencia / Definición de Terminado:**
- `EmptyState` con acción obligatoria; endpoint de acciones permitidas; tests con roles distintos.

**Riesgos/Notas:**
- Grants por sub-sección quedan para cuando lo pida un cliente.
