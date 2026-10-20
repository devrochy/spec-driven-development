---
id: HU-APP-18
titulo: "Cobranza admin móvil: réplica total del pack"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, diferenciacion]
req: [REQ-APP-07]
dependencias: [HU-APP-03]
skills: [frontend-design, panel-ui]
estado: terminada
---

# HU-APP-18 · Cobranza admin móvil: réplica total del pack

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-18

**Título:** Cobranza admin móvil: réplica total del pack

**Workstream:** App móvil

**Historia:** Como dueño de un negocio con cobranza quiero administrar el pack desde la app (resumen, clientes con su ficha y cambios pendientes, pagos, promesas, dispositivos y auditoría), para que la app oficial sea una réplica total del panel también en la vertical que la hizo nacer.

**Por qué importa (valor empresarial):** La cobranza con APK es el diferencial del producto (D-02). El tab Cobranza del PanelShell era el último placeholder de la réplica: sin él, el dueño tenía que volver al escritorio justo en la vertical más importante. Cerrarlo completa la réplica total pedida para la app oficial.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-03](HU-APP-03-navegacion-por-permisos.md)

**Criterios de aceptación (Gherkin):**
- **Resumen.** Dado un dueño con permiso de cobranza, cuando abre el tab Cobranza, entonces ve los KPIs del pack desde `/pack/cobranza/summary`.
- **Clientes y ficha.** Dado un dueño, cuando busca y abre un cliente, entonces ve su ficha con préstamos, saldos y los cambios propuestos con aprobar/rechazar con confirmación.
- **Promesas y dispositivos.** Dado un dueño, cuando cambia el estado de una promesa o aprueba/bloquea un dispositivo, entonces la acción se aplica con confirmación y la lista se refresca.
- **Auditoría.** Dado un dueño, cuando abre Auditoría, entonces ve el log del pack (entidad, operación, actor y fecha).

**Evidencia / Definición de Terminado:**
- Módulo `src/modules/cobranza-admin` (resumen, clientes con ficha, pagos, promesas, dispositivos, auditoría) contra `/api/v1/pack/cobranza/*` verificado en el OpenAPI; tab Cobranza del PanelShell conectado; 8 tests nuevos.

**Implementada (2026-10-06):** [solvershub-apk #123](https://github.com/devrochy/solvershub-apk/pull/123) — módulo `cobranza-admin` con 6 secciones (resumen KPIs, clientes+búsqueda+ficha con préstamos/cambios, pagos, promesas, dispositivos, auditoría), acciones con confirmación; reemplaza el placeholder del tab Cobranza. 611/611 tests.

**Riesgos/Notas:**
- Quedan fuera de esta HU (web/iteración posterior): caja/liquidaciones/inyecciones, ruta optimizada y reportes consolidados del pack en móvil.
