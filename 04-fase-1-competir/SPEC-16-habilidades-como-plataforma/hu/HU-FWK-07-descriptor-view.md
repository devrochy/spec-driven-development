---
id: HU-FWK-07
titulo: Componente genérico DescriptorView y migración de pantallas
spec: SPEC-16
fase: 1
hito: "1"
workstream: Framework/Plugins
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, operacion]
req: [REQ-FWK-05, REQ-PLUS-05]
dependencias: [HU-FWK-06, HU-UI-08]
skills: ["frontend-design", "backend-design:testing-with-discernment"]
estado: borrador
---

# HU-FWK-07 · Componente genérico `<DescriptorView>` y migración de pantallas

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-16](../spec.md).

**ID:** HU-FWK-07

**Título:** Componente genérico DescriptorView y migración de pantallas

**Workstream:** Framework/Plugins

**Historia:** Como responsable del panel quiero un componente que dibuje cualquier vista descrita por el backend y migrar a él las pantallas que encajan para mantener una sola forma de mostrar listas y acciones.

**Por qué importa (valor empresarial):** Menos código propio por pack significa menos bugs y menos costo de mantenimiento para una persona; las pantallas migradas heredan las mejoras de las tablas (filtros, densidad, accesibilidad).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FWK-05, REQ-PLUS-05

**Dependencias:** [HU-FWK-06](HU-FWK-06-descriptores-y-api-de-vistas.md), [HU-UI-08](../../SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md)

**Criterios de aceptación (Gherkin):**
- **Renderizado.** Dado un descriptor, cuando el panel abre `/p/{pack}/{vista}`, entonces muestra encabezado, KPIs, `FilterBar`, tabla con los tipos de celda y acciones con confirmación.
- **Migración.** Dado las pantallas candidatas, cuando se migran, entonces se ven y funcionan igual o mejor y se borra su código propio.
- **Pruebas.** Dado cada tipo de celda y acción, cuando corre el CI, entonces hay un test.

**Evidencia / Definición de Terminado:**
- Componente con tests; lista de pantallas migradas con capturas.

**Riesgos/Notas:**
- La cartera, la bandeja y el wizard de WhatsApp quedan a mano.
