---
id: HU-SH-04
titulo: Cobro de plataforma por dos canales con fuente única
spec: SPEC-07
fase: 0
hito: 0A
workstream: Billing
prioridad: P0
critico: true
estimacion: L
impacto: [ingreso, confianza]
req: [REQ-SH-04, REQ-BILL-11, REQ-ARCH-13]
dependencias: [HU-SH-03, HU-SUB-05]
skills: ["adr", "backend-design:idempotency-and-side-effects", "backend-design:incident-thinker", "data:validate-data", "pagos-wompi"]
ola: 4
estado: en-curso
---

# HU-SH-04 · Cobro de plataforma por dos canales con fuente única

> Estado SDD: En curso. Implementada y mergeada el 2026-10-09 ([core #348](https://github.com/devrochy/agent-core/pull/348) + [panel #47](https://github.com/devrochy/solvershub-panel/pull/47)); falta desplegarla en test y verificar los criterios.

**ID:** HU-SH-04

**Título:** Cobro de plataforma por dos canales con fuente única

**Workstream:** Billing

**Historia:** Como cliente de SolversHub quiero pagar mi mensualidad por el link que me manda el asistente o desde "Plan" en el panel, sin que me cobren dos veces, para pagar por donde me resulte cómodo.

**Por qué importa (valor empresarial):** Es el ingreso recurrente de SolversHub. Dos canales suben la tasa de cobro; una fuente única (`tenant_subscriptions`) evita el doble cobro y que el negocio pase a `past_due` aunque haya pagado por el otro canal. Hoy además no existe un job de renovación.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** L

**REQ mapeados:** REQ-SH-04, REQ-BILL-11, REQ-ARCH-13

**Dependencias:** [HU-SH-03](HU-SH-03-aprovisionamiento-automatico.md), HU-SUB-05

**Criterios de aceptación (Gherkin):**
- **Pago por el asistente.** Dado un cargo del período `plat-acme-202611` en el tenant `solvershub`, cuando el cliente paga el link, entonces `tenant_subscriptions` del negocio Acme extiende su período.
- **Pago por el panel.** Dado el mismo período, cuando el cliente paga desde `/plan`, entonces el cargo del canal asistente queda pagado y el asistente no lo vuelve a cobrar.
- **Sin doble cobro.** Dado un período ya pagado por un canal, cuando el otro intenta generar un link, entonces responde "ya pagado".
- **Renovación.** Dado un período que vence en 5 días, cuando corre el job, entonces se genera el cobro del siguiente con la referencia del período y se avisa por el canal preferido.
- **Conciliación.** Dado una diferencia entre ambos lados, cuando corre el job diario, entonces se alerta con el detalle.
- **Plan creado por el alta.** Dado un negocio creado por el alta automática ([HU-SH-03](HU-SH-03-aprovisionamiento-automatico.md)) con un plan pago, cuando vence su período, entonces entra en la renovación como cualquier otro y no queda bloqueado si paga.
- **Cambio de plan desde el asistente.** Dado un negocio Free creado por el alta que compra un plan pago en el asistente, cuando se confirma el pago, entonces su plan cambia sin crear otro negocio y se aplica el preset que quedó pendiente (ADR-0110 §3.1).

**Evidencia / Definición de Terminado:**
- ADR "Dos canales de cobro de plataforma"; jobs de renovación y conciliación; tests de los cinco escenarios.
- Verificación documentada del riesgo R-05 (URL de eventos de Wompi).

**Riesgos/Notas:**
- `billing_lifecycle` hoy solo marca `past_due`/`expired` (`core/tasks/billing_lifecycle.py:27-68`).
- `PROVISIONING_SELLER_TENANTS` se enciende en producción solo con esta HU terminada (ADR-0121).

**Avance (2026-10-09):**
- ADR-0123 «Dos canales de cobro de plataforma con fuente única». Enmienda ADR-0121 § 2: `PROVISIONING_SELLER_TENANTS` es obligatoria en la app y en el worker.
- Revisada por los agentes de aislamiento, seguridad y arquitectura; sus hallazgos se corrigieron en [core #348](https://github.com/devrochy/agent-core/pull/348) con tests.
- Riesgo R-05 confirmado: Wompi admite una URL de eventos por cuenta y ambiente. Lo resuelve un enrutador con `BILLING_WOMPI_EVENTOS_TENANT`.
- **Requisitos para encender el alta automática en producción** (ADR-0123 § 10): canal preferido respetado y `dias_anticipacion` del vendedor igual a `BILLING_DIAS_RENOVACION`; la variable en app y worker; R-05 verificado en el sandbox de Wompi; los criterios verificados en test.
- **Decisión del 2026-10-09 (enmienda de ADR-0123, [core #351](https://github.com/devrochy/agent-core/pull/351)):** el aviso de renovación por el panel de un negocio del alta sale por la integración SMTP del vendedor y, si no la tiene, por el SMTP de la plataforma. El acceso del alta y la recuperación de contraseña siguen por el SMTP de la plataforma. Elegir el SMTP por propósito queda en el BACKLOG del core.
- **Para verificar en test:** pago por el asistente y por `/plan`, «ya pagado», renovación, conciliación y paso de Free a Premium con el preset pendiente (runbook `docs/runbooks/cobro-de-plataforma.md`).
- **Guía de prueba en test:** [guia-de-prueba-alta-automatica.md](../guia-de-prueba-alta-automatica.md).
