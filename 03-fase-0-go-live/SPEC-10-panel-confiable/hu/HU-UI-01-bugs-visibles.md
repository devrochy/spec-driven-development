---
id: HU-UI-01
titulo: Lote de bugs visibles del panel
spec: SPEC-10
fase: 0
hito: 0A
workstream: UX/Onboarding
prioridad: P0
critico: true
estimacion: S
impacto: [confianza]
req: [REQ-UX-05]
dependencias: []
skills: ["frontend-design", "built-in-browser", "backend-design:auth-and-authorization", "panel-ui"]
ola: 1
estado: terminada
---

# HU-UI-01 · Lote de bugs visibles del panel

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-10](../spec.md).

**ID:** HU-UI-01

**Título:** Lote de bugs visibles del panel

**Workstream:** UX/Onboarding

**Historia:** Como dueño de varios negocios quiero que la configuración se guarde en el negocio que tengo seleccionado, que los precios se vean en pesos y que los errores digan qué pasó para confiar en lo que hago en el panel.

**Por qué importa (valor empresarial):** Guardar la configuración en otro negocio es un error de aislamiento visible para el cliente (master y agencias lo sufren primero). Precios en "US$" y errores genéricos hacen que el producto parezca sin terminar. Son arreglos pequeños con efecto inmediato en la confianza.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-UX-05

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Negocio correcto.** Dado un usuario con dos negocios y el negocio B seleccionado, cuando guarda la config de una habilidad, entonces se guarda en B (el BFF envía `X-Tenant-Id`).
- **Moneda.** Dado productos y pedidos de comercio en COP, cuando se muestran, entonces usan `formatMoney(moneda del negocio)` y no `formatUsd`.
- **Errores del backend.** Dado un error de validación del backend en un formulario de schema, cuando se guarda, entonces se muestra el mensaje real y los números se envían como números.
- **Rollback.** Dado un switch optimista que el servidor rechaza, cuando falla, entonces vuelve a su estado anterior y se informa.
- **Detalles.** Dado el botón vacío del encabezado de Calendario, los botones destructivos en verde de cobranza y el menú sin Clientes ni Gestores de cobranza ni Horarios de calendario, cuando se corrige, entonces coinciden con el backend y con `DESIGN.md`.
- **Cancelar cita.** Dado cancelar una cita que falla en el servidor, cuando ocurre, entonces el panel lo informa (hoy no revisa `res.ok`).

**Evidencia / Definición de Terminado:**
- Un test por bug donde aplique; capturas antes y después.

**Implementada (2026-10-03):**
- Panel (PR [#13](https://github.com/devrochy/solvershub-panel/pull/13)): N-11 (`X-Tenant-Id` en el PUT de config), `formatMoney(moneda)`, números como número, botón vacío → "Configurar horario", destructivos en rojo, cancelar cita revisa `res.ok`, menú con Gestores/Clientes/Horario, página `/cobranza/gestores` y `/calendario/horario` (editor visual de `business_hours`), moneda editable.
- Backend (PR [#197](https://github.com/devrochy/agent-core/pull/197)): `AppSettings.currency` (default COP) expuesta en `/admin/settings`.
- 20 tests del panel verdes; `typecheck`/`lint`/`build` OK.
- **Decisión**: los costos de proveedor siguen en USD; la conversión por TRM es del billing del core (HU-BILL-03), no de la UI. Capturas antes/después: pendientes de navegador.

**Riesgos/Notas:**
- Las confirmaciones de acciones irreversibles van en [HU-UI-02](HU-UI-02-kit-de-feedback.md) con el diálogo compartido.
