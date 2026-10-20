---
id: HU-SH-01
titulo: Tenant solvershub reproducible y coherente
spec: SPEC-07
fase: 0
hito: 0A
workstream: Asistente SolversHub
prioridad: P0
critico: true
estimacion: M
impacto: [ingreso, confianza]
req: [REQ-SH-01, REQ-PLUS-06]
dependencias: [HU-FWK-03, HU-SUB-06]
skills: ["onboard-tenant", "customizer", "eval-runner"]
ola: 3
estado: terminada
---

# HU-SH-01 · Tenant `solvershub` reproducible y coherente

> Estado SDD: Terminada — implementada y aplicada en test el 2026-10-08 (issue [core #299](https://github.com/devrochy/agent-core/issues/299)).

**ID:** HU-SH-01

**Título:** Tenant solvershub reproducible y coherente

**Workstream:** Asistente SolversHub

**Historia:** Como dueño de SolversHub quiero que el asistente de SolversHub se construya con un preset, una sola fuente de precios y textos coherentes con D-16 para que diga siempre la verdad sobre los planes y se pueda reconstruir en cualquier entorno.

**Por qué importa (valor empresarial):** Es el vendedor de la empresa. Hoy promete 30 días de prueba en todos los planes, tiene precios en tres lugares y un re-seed le borra el flujo: un vendedor que promete lo que el producto no da genera reclamos desde la primera venta.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-SH-01, REQ-PLUS-06

**Dependencias:** [HU-FWK-03](../../SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md), HU-SUB-06

**Criterios de aceptación (Gherkin):**
- **Una fuente de precios.** Dado `core/billing/plans.py`, cuando cambia el precio de Basic, entonces el producto del tenant `solvershub` muestra el precio nuevo sin editar `catalog.json` ni la voz de marca.
- **Prueba coherente.** Dado un prospecto que pregunta "¿tienen prueba?", cuando el asistente responde, entonces dice que Free tiene 30 días y que los planes pagos se cobran desde el primer día (`voz-de-marca.md:28`, `ventas.md:22` y `seguimiento.md:8` corregidos).
- **Reproducible.** Dado un entorno vacío, cuando se ejecuta el runbook, entonces el tenant queda igual: preset aplicado, secciones `tenant`, packs (commerce, calendar, payments, subscriptions) y proveedor `pack_subscriptions`.
- **Persistencia.** Dado un redespliegue, cuando arranca el contenedor, entonces el tenant conserva sus archivos en `TENANTS_ROOT`.
- **Docs al día.** Dado `tenants/solvershub/docs/README.md`, cuando se lee, entonces describe los packs reales y que la agenda es interna.

**Evidencia / Definición de Terminado:**
- Runbook "reconstruir el asistente de SolversHub" en `solvershub-comercial/runbooks/`.
- Evals existentes del tenant en verde tras los cambios.

**Terminada (2026-10-08):** [agent-core #301](https://github.com/devrochy/agent-core/pull/301) + [#303](https://github.com/devrochy/agent-core/pull/303) y [comercial #10](https://github.com/devrochy/solvershub-comercial/pull/10) + [#11](https://github.com/devrochy/solvershub-comercial/pull/11). Desplegada en test (`4e0fc38`).

Lo que quedó:
- **Preset y CLI:**
  - preset genérico `suscripciones`: commerce, agenda interna, payments y subscriptions, con proveedor `pack_subscriptions`;
  - `tenant aplicar-preset`, que no siembra ejemplos en un negocio existente (#303);
  - `tenant seed --voz-de-marca`.
- **Precio:** sale de `core/billing/plans.py` (`precio_de_plan`), al sembrar y con un cron horario.
- **Archivos del negocio:** versionados en `solvershub-comercial/tenants/solvershub/`.
  - Voz de marca sin precios y con D-16.
  - `ventas.md` y `seguimiento.md` corregidos.
  - `docs/README.md` al día.
- **Runbook:** `runbooks/reconstruir-asistente-solvershub.md`.

**Verificado en test (runbook completo):**
- volumen con nombre en `/app/tenants`; `flow.json` igual antes y después;
- preset `suscripciones`, con commerce, calendar, payments y subscriptions habilitados y proveedor `pack_subscriptions`;
- los 4 planes con el precio de `plans.py` y prueba solo en Free;
- voz de marca sin precios y sin prueba en los planes pagos;
- golden set 12/12, más el escenario nuevo «¿tienen prueba?».

Con el ciclo completo de «Probar asistente», 3 de 3 respuestas dicen que la prueba de 30 días es solo de Free y que Basic se cobra desde el primer día, con el precio sacado del catálogo.

**Incidente al aplicar:** la primera versión de `aplicar-preset` sembró los ejemplos del preset en `solvershub`: creó «Plan mensual» (`PLAN-MENSUAL`) y pisó los atributos de `PLAN-FREE`. La variante quedó desactivada a mano y `PLAN-FREE` se restauró con el seed. #303 lo evita.

**Pendiente:**
- desplegar #303 en test;
- el runner de evals solo mira la primera respuesta del modelo, sin herramientas;
- el modelo de test (`deepseek-chat`) está discontinuado (P-05).

**Riesgos/Notas:**
- Si P-03 elige cobranza, el proveedor cambia cuando llegue HU-SUB-15 (0B); el resto no cambia.
