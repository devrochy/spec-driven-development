---
id: HU-SH-03
titulo: Identidad de servicio y aprovisionamiento automático de negocios
spec: SPEC-07
fase: 0
hito: 0A
workstream: Asistente SolversHub
prioridad: P0
critico: true
estimacion: L
impacto: [ingreso, operacion]
req: [REQ-SH-03, REQ-COMP-08]
dependencias: [HU-SUB-03, HU-FWK-03]
skills: ["adr", "backend-design:auth-and-authorization", "backend-design:security-reviewer", "backend-design:idempotency-and-side-effects", "/codex:adversarial-review"]
ola: 4
estado: en-curso
---

# HU-SH-03 · Identidad de servicio y aprovisionamiento automático de negocios

> Estado SDD: En curso. Implementada y mergeada el 2026-10-09 ([core #345](https://github.com/devrochy/agent-core/pull/345), ajuste final en [core #347](https://github.com/devrochy/agent-core/pull/347)); falta desplegarla en test y verificar los criterios (issue [core #332](https://github.com/devrochy/agent-core/issues/332)).

**ID:** HU-SH-03

**Título:** Identidad de servicio y aprovisionamiento automático de negocios

**Workstream:** Asistente SolversHub

**Historia:** Como dueño de SolversHub quiero que, cuando un cliente activa un plan en el asistente, se cree solo su negocio con el plan, el preset de su vertical y una invitación al owner para no intervenir en ninguna alta.

**Por qué importa (valor empresarial):** Es la pieza que hace que el negocio escale sin el fundador (D-12). Hoy cada alta exige al master con sesión humana. Hacerlo seguro (allowlist, idempotencia, auditoría, sin tokens en manos del LLM) es lo que permite abrir el canal sin miedo a altas fraudulentas o duplicadas.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** L

**REQ mapeados:** REQ-SH-03, REQ-COMP-08

**Dependencias:** HU-SUB-03, [HU-FWK-03](../../SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md)

**Criterios de aceptación (Gherkin):**
- **Alta automática.** Dado `subscription.activated` en el tenant `solvershub` con `plan_code = premium`, cuando el consumidor lo procesa, entonces se crea el negocio con el plan Premium, el preset del vertical declarado y una invitación al owner en menos de 2 minutos.
- **Solo vendedores.** Dado el mismo evento en un negocio que no está en la allowlist, cuando llega, entonces no se crea nada.
- **Idempotencia.** Dado el mismo evento entregado dos veces, cuando se procesa, entonces existe un solo negocio para esa referencia.
- **Sin el LLM.** Dado cualquier conversación, cuando el asistente intenta crear un negocio, entonces no tiene ninguna tool ni token para hacerlo.
- **Auditoría.** Dado un alta, cuando se consulta el `audit_log`, entonces aparece con actor "provisioning", referencia del pedido, plan y preset.
- **Free.** Dado el plan Free confirmado, cuando se procesa, entonces se crea el negocio en prueba de 30 días (D-16).

**Evidencia / Definición de Terminado:**
- ADR "Identidad de servicio y aprovisionamiento"; consumidor con tests de los seis escenarios; variable `PROVISIONING_SELLER_TENANTS` documentada.

**Riesgos/Notas:**
- El vertical se pregunta en la conversación de venta y viaja en el pedido como dato, no como texto libre.

**Avance (2026-10-09):**
- ADR-0121 «Identidad de servicio y aprovisionamiento»: enmienda ADR-0081 §4. Por seguridad, el enlace de acceso va solo por correo (enmienda de D-SPEC-07-2).
- Revisada por los agentes `auditor-multitenant`, `backend-design:security-reviewer` y `arquitecto`. Sus hallazgos se corrigieron en [core #345](https://github.com/devrochy/agent-core/pull/345) y [core #347](https://github.com/devrochy/agent-core/pull/347), con tests que fallan si vuelve el problema.
- **No se enciende en producción antes de [HU-SH-04](HU-SH-04-cobro-de-plataforma-dos-canales.md):** el plan pago que crea el alta todavía no se renueva.
- **Para verificar en test:**
  - `PROVISIONING_SELLER_TENANTS` con el UUID de `solvershub` en el worker;
  - `checkout_fields.plan` con `business_name` y `vertical`;
  - el playbook de ventas pidiendo el nombre y el tipo de negocio;
  - `SYSTEM_SMTP_*` configurado;
  - una compra Free y una Premium de prueba.

- **Guía de prueba en test:** [guia-de-prueba-alta-automatica.md](../guia-de-prueba-alta-automatica.md).
