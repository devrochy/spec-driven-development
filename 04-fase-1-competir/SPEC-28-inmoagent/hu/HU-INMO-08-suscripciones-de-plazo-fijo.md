---
id: HU-INMO-08
titulo: "Suscripciones para contratos de plazo fijo"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Comercio y suscripciones
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, confianza]
req: [REQ-INMO-08]
dependencias: [HU-INMO-01]
skills: ["pagos-wompi", "db-migration", "backend-design:idempotency-and-side-effects", "auditor-multitenant"]
estado: borrador
---

# HU-INMO-08 · Suscripciones para contratos de plazo fijo

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-08

**Título:** Suscripciones para contratos de plazo fijo

**Workstream:** Comercio y suscripciones

**Historia:** Como habilidad que cobra cuotas de un contrato quiero crear cobros periódicos con inicio, día de pago, fin y valor programado, sin que el cliente pueda pausarlos ni cancelarlos por chat.

**Por qué importa (valor empresarial):** `activate` con `variante_id` nulo y sin coincidencia de referencia modifica la suscripción vigente del cliente y da el período en curso por pagado (`packages/pack-subscriptions/pack_subscriptions/capability.py:134-240`). Las tools `sub_*` actúan sobre `activas[0]` (`core/subscriptions/tools.py:48-52`): un cliente con gimnasio y arriendo podría pausar el arriendo.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-08

**Dependencias:** [HU-INMO-01](HU-INMO-01-adrs-y-dor-del-piloto.md)

**Criterios de aceptación (Gherkin):**
- **Identidad por referencia.** Dado un cliente con dos contratos, cuando se crea la segunda suscripción con otra `reference`, entonces conviven y la primera no cambia (único `(tenant_id, referencia_origen, variante_id)` parcial).
- **Inicio y día de pago.** Dado inicio el 1 de noviembre y día de pago 5, cuando se activa, entonces el primer cargo vence el 5 de noviembre y el período no se da por pagado salvo que se pida.
- **Sin autogestión.** Dado una suscripción con `autogestion=false`, cuando el asistente intenta pausarla, cancelarla o cambiarle el plan, entonces el proveedor lo rechaza (fail-closed) y el asistente escala.
- **Valor programado.** Dado un nuevo valor con fecha, cuando llega la fecha, entonces los cargos siguientes lo usan sin prorrateo, reutilizando `cambio_programado`.

**Evidencia / Definición de Terminado:**
- Operaciones opcionales con el molde de `permite_varias` y `registrar_pago_externo` (`core/subscriptions/__init__.py:325-358`); pack-cobranza no se toca.
- Solo kwargs con valores por defecto que conservan la conducta actual en `activate`; journeys de suscripciones, [HU-SH-03](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md) y [HU-SH-04](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md) en verde. ADR nuevo que enmienda ADR-0106.

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
