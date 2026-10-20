# SPEC-07 · Asistente SolversHub (dogfooding)

> Estado SDD: Diseño aprobado (2026-10-09: D-SPEC-07-1 y D-SPEC-07-2 tomadas; SH-01 y SH-02 ya ejecutadas) · Fase 0 · Hito 0A (SH-01 a SH-08) y 0B (SH-09) · Workstream Asistente SolversHub

## Problema

El objetivo final del cliente es que el tenant `solvershub` sea el asistente de SolversHub: agenda
una demo, vende un plan, cobra la suscripción y da de alta al cliente, todo solo. Hoy
([brechas-objetivo-solvershub.md](../../01-revalidacion/brechas-objetivo-solvershub.md)):

- El tenant tiene **tres fuentes de precios**, promete 30 días de prueba en todos los planes
  (`docs/voz-de-marca.md:28`, `playbooks/ventas.md:22`, `seguimiento.md:8`) y sus secciones de flujo
  se pisan con un re-seed.
- La demo funciona con el asistente, pero **agendar desde el panel en modo interno falla**
  (`pack_calendar/admin_api.py:281-297`), se ofrecen horas pasadas y no hay recordatorios, aviso al
  equipo ni no-show.
- **Crear un tenant solo lo puede hacer el master con sesión humana**
  (`core/api/routers/platform.py:28-30,114-197`): no hay identidad de servicio ni consumidor de
  aprovisionamiento.
- El cobro de la plataforma tiene **dos registros sin sincronizar** (la suscripción en el tenant
  `solvershub` y la `TenantSubscription` del negocio nuevo).
- **Embedded Signup no funciona**: el cliente nuevo no puede conectar su WhatsApp solo.
- No hay onboarding guiado, ni antiabuso, ni evals de la conversación completa.

## Usuarios y contexto

- **Prospecto** que llega por WhatsApp o la landing.
- **Cliente nuevo** que recibe su negocio listo y conecta su WhatsApp.
- **SolversHub** como operador que no quiere intervenir en cada alta.

## Por qué importa (valor empresarial)

Es la **demo viva del producto y su canal de ventas**: si el asistente de SolversHub vende y da de
alta solo, cada conversación prueba lo que se vende. Convierte el costo de adquisición en algo casi
marginal y escala sin el fundador. Ningún competidor de la matriz muestra su propio agente cerrando
ventas y aprovisionando clientes de punta a punta (REQ-PLUS-06).

## Alcance

| HU | Qué | Hito |
|---|---|---|
| [HU-SH-01](hu/HU-SH-01-tenant-reproducible.md) ★ | Tenant `solvershub` reproducible y coherente | 0A |
| [HU-SH-02](hu/HU-SH-02-demo-de-punta-a-punta.md) ★ | Demo de punta a punta | 0A |
| [HU-SH-03](hu/HU-SH-03-aprovisionamiento-automatico.md) ★ | Identidad de servicio y consumidor de aprovisionamiento | 0A |
| [HU-SH-04](hu/HU-SH-04-cobro-de-plataforma-dos-canales.md) ★ | Dos canales de cobro de plataforma con fuente única | 0A |
| [HU-SH-05](hu/HU-SH-05-embedded-signup-real.md) ★ | Embedded Signup real y requisitos de Tech Provider | 0A |
| [HU-SH-06](hu/HU-SH-06-onboarding-autoservicio.md) ★ | Onboarding autoservicio | 0A |
| [HU-SH-07](hu/HU-SH-07-antiabuso-y-cumplimiento.md) ★ | Antiabuso y cumplimiento del alta | 0A |
| [HU-SH-08](hu/HU-SH-08-golden-set-asistente.md) ★ | Golden set E2E del asistente y canary | 0A |
| [HU-SH-09](hu/HU-SH-09-landing-con-atribucion.md) | Landing → asistente con atribución | 0B |

## Escenario del Hito 0A (criterio de salida)

> Dado un prospecto real que escribe al WhatsApp de SolversHub, cuando agenda una demo, compra un
> plan y paga (o confirma Free), entonces, sin intervención humana: su negocio se crea con el plan y el
> preset de su vertical, recibe una invitación, la acepta, conecta su WhatsApp por Embedded Signup y,
> al final del período, recibe el cobro del período siguiente con aviso por plantilla. Todo queda
> auditado.

## Decisiones

- ✅ D-12 (alta automática completa), ✅ D-13 (dos canales con fuente única), ✅ D-15/D-16.
- Proveedor del tenant `solvershub` (✅ tomada: D-21, `pack_subscriptions`): [P-03](../../02-vision-y-decisiones/preguntas-abiertas.md#p-03--proveedor-de-suscripción-del-tenant-solvershub).

### D-SPEC-07-1 · Cómo se autoriza el aprovisionamiento

| Opción | Pros | Contras |
|---|---|---|
| **A. Consumidor interno del core que escucha `subscription.activated` de negocios en una allowlist de vendedores; idempotente por referencia; auditado** | Nadie guarda un token de master; el LLM nunca lo dispara | Lógica especial en el core |
| B. Token de servicio con scope `platform:provision` que usa una acción configurable | Reutiliza HU-SUB-14 | Un token poderoso guardado en la config de un negocio |
| C. Tool declarativa HTTP con el token del master | Rápido | Inaceptable: el LLM podría crear negocios y el token queda en el AgentSpec |

**Recomendación: A** (con identidad de servicio solo para auditoría). Estado: ✅ tomada (2026-10-02): consumidor interno del core sobre `subscription.activated` con allowlist.

### D-SPEC-07-2 · Invitación del owner

| Opción | Pros | Contras |
|---|---|---|
| **A. Invitación sin contraseña (ADR-0081): enlace de un solo uso por correo y WhatsApp, el owner define su contraseña** | Seguro; reutiliza lo existente | Depende de que el correo llegue |
| B. Contraseña temporal por WhatsApp | Simple | Secreto en un canal de mensajería |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): enlace de un solo uso por correo y WhatsApp (ADR-0081).

**Enmienda (2026-10-09, ADR-0121, por seguridad):** el enlace que define la contraseña va **solo por correo** y solo para una cuenta creada por esa alta. Por WhatsApp sale un aviso sin enlace, con el correo enmascarado. Así, canjearlo prueba que se controla el correo: la revisión de [core #345](https://github.com/devrochy/agent-core/pull/345) mostró que el enlace por WhatsApp permitía quedarse con la cuenta de un correo ajeno.

## Fuera de alcance

Registro desde la landing sin conversación ([HU-UX-06](../../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-06-registro-desde-landing.md)), oferta de agencia (Fase 2).

## Métricas de éxito

- Tiempo desde el pago hasta el negocio creado < 2 minutos; hasta el WhatsApp conectado < 1 día.
- 0 altas que requieran al master en el último mes.
- Golden E2E del asistente ≥95 % durante 3 noches; canary sin regresiones.

## Requerimientos cubiertos

REQ-SH-01 a REQ-SH-07, REQ-PLUS-06, REQ-COMP-07, REQ-COMP-08, REQ-UX-02, REQ-CONN-03, REQ-BILL-11.
