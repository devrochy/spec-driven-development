---
id: HU-UX-10
titulo: Cobranza y Ventas como una entrada con pestañas
spec: SPEC-12
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-UX-12]
dependencias: [HU-UX-02]
skills: ["frontend-design", "panel-ui", "built-in-browser", "dataviz"]
estado: borrador
---

# HU-UX-10 · Cobranza y Ventas como una entrada con pestañas

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-12](../spec.md). Nace de [D-37](../../../02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto) (2026-10-19).

**ID:** HU-UX-10

**Título:** Cobranza y Ventas como una entrada con pestañas

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio de cobranza o de comercio quiero entrar a Cobranza o a Ventas desde una sola entrada y moverme por pestañas, con un resumen que me lleva a lo que más uso, para no recorrer 14 entradas del menú.

**Por qué importa (valor empresarial):** Cobranza es el vertical con app de campo y el que más entradas tiene (14). Agruparla y darle accesos rápidos baja el tiempo hasta la acción diaria (promesas, pagos, gestores) y deja espacio en el menú para los agentes.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-12

**Dependencias:** [HU-UX-02](HU-UX-02-menu-v2.md)

**Criterios de aceptación (Gherkin):**
- **Cobranza en una entrada.** Dado un negocio con cobranza, cuando abro Cobranza, entonces veo su Resumen con accesos rápidos y pestañas agrupadas en Operación, Monitoreo y Seguridad.
- **Cobros en una página.** Dado un colaborador con `pack_cobranza:cobros`, cuando abre Cobros, entonces ve «Cobros al propietario» y «Pagos de clientes» como dos pestañas de una sola página.
- **Ventas con Suscripciones.** Dado un negocio con comercio y suscripciones, cuando abro Ventas, entonces veo Comercio con Resumen, Productos, Categorías, Promociones y Pedidos, y la pestaña Suscripciones.
- **Permisos por pestaña.** Dado un gestor sin permiso de Auditoría, cuando abre Cobranza, entonces no ve esa pestaña ni recibe un 403.
- **Enlaces viejos.** Dado un enlace a `/cobranza/promesas` o `/comercio/pedidos`, cuando lo abro, entonces llego a la pestaña equivalente.

**Evidencia / Definición de Terminado:**
- Páginas de `/cobranza/*` y `/comercio/*` agrupadas como pestañas con la plantilla de `components/templates/`; Resumen de Cobranza con accesos rápidos (kit de [SPEC-29](../../SPEC-29-sistema-de-diseno-unificado/spec.md)).
- Página nueva de Suscripciones (el panel no la tiene) como pestaña de Ventas, sobre `/subscriptions/lista` (etiqueta ya en `lib/labels.ts`); el menú v2 de [HU-UX-02](HU-UX-02-menu-v2.md) no la incluye.
- Redirecciones de `/cobranza/*` y `/comercio/*`, con test; páginas en `lib/a11y/paginas.test.tsx`; capturas.

**Riesgos/Notas:**
- La app de campo de cobranza no cambia (D-SPEC-29-6); solo el panel y su cajón ([HU-UX-11](HU-UX-11-cajon-de-la-app-con-menu-v2.md)).
- Los subgrupos de hoy en `nav.ts` (`sub`: General, Monitoreo, Seguridad) son la base de las pestañas; «General» pasa a llamarse Operación.
