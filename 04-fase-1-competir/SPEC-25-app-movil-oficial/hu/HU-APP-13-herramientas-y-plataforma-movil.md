---
id: HU-APP-13
titulo: "Herramientas y plataforma móvil: asistente, plantillas, DLQ y negocios"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-APP-07]
dependencias: [HU-APP-03]
skills: [frontend-design]
estado: terminada
---

# HU-APP-13 · Herramientas y plataforma móvil: asistente, plantillas, DLQ y negocios

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-13

**Título:** Herramientas y plataforma móvil: asistente, plantillas, DLQ y negocios

**Workstream:** App móvil

**Historia:** Como dueño quiero probar mi asistente desde la app, ver el estado de mis plantillas de WhatsApp y la bandeja de fallos (DLQ) con reintento; y como master de plataforma quiero administrar negocios (suspender, cambiar plan, eliminar con confirmación) desde el teléfono, para cerrar la réplica del panel sin huecos.

**Por qué importa (valor empresarial):** Herramientas y Plataforma son las secciones que completan la réplica total del panel pedida para la app oficial. El master de plataforma gana movilidad operativa y el dueño gana diagnóstico rápido (probar el asistente, revisar fallos) desde el celular.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-03](HU-APP-03-navegacion-por-permisos.md)

**Criterios de aceptación (Gherkin):**
- **Asistente.** Dado un dueño, cuando abre Probar asistente, entonces puede conversar con el playground (mismos límites del panel: sin efectos reales).
- **Plantillas y DLQ.** Dado un dueño, cuando abre Plantillas o Fallos, entonces ve el estado de las plantillas de su conexión y la bandeja DLQ con acción de reintento.
- **Negocios.** Dado un admin master, cuando abre Negocios, entonces ve la lista paginada con búsqueda y puede suspender/activar, cambiar plan y eliminar con la frase de confirmación exacta.
- **Gate master.** Dado un usuario que no es master, cuando intenta abrir Negocios, entonces la sección no existe en su navegación y la ruta profunda devuelve acceso denegado.

**Evidencia / Definición de Terminado:**
- `modules/herramientas/` (asistente, plantillas, DLQ) y `modules/plataforma/` (negocios) contra `/api/v1/admin/playground`, `/admin/dlq`, `/api/v1/pack/*` y `/admin/platform/tenants`; tests unitarios, de render y de RBAC master; captura en dev client.

**Implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — herramientas y plataforma móvil (asistente, plantillas, DLQ y negocios).

**Riesgos/Notas:**
- El playground móvil hereda la protección [HU-ARCH-14](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-14-playground-sandbox.md) (sin efectos reales) del backend; no hay lógica nueva de sandbox en la app.
- Eliminar negocio (purge) es la única excepción de borrado físico del sistema (ADR): confirmación por frase y doble paso.

**App implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — `modules/herramientas`: bandeja de fallos (DLQ) con reintento y negocios de plataforma (solo master) con suspender/activar confirmado. Asistente/plantillas quedan en web (deuda). 3 tests.
