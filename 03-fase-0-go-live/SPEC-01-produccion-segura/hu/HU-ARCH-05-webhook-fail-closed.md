---
id: HU-ARCH-05
titulo: Webhook fail-closed sin firma no se procesa
spec: SPEC-01
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: S
impacto: [confianza]
req: [REQ-ARCH-04]
dependencias: []
skills: ["backend-design:security-discipline", "backend-design:security-reviewer", "backend-design:testing-with-discernment"]
ola: 1
estado: terminada
---

# HU-ARCH-05 · Webhook fail-closed: sin firma no se procesa

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-01](../spec.md).

**ID:** HU-ARCH-05

**Título:** Webhook fail-closed sin firma no se procesa

**Workstream:** Arquitectura/Prod

**Historia:** Como responsable de seguridad quiero que un mensaje de WhatsApp sin firma válida nunca llegue al asistente en producción para que nadie pueda inyectar conversaciones falsas en un negocio.

**Por qué importa (valor empresarial):** Hoy, si a una conexión le falta el `app_secret`, el webhook acepta mensajes sin verificar (`core/gateway/webhooks.py:223`). Un atacante podría disparar pedidos, cobros o consumo de créditos a nombre de cualquier cliente.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-ARCH-04

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Sin secreto en producción.** Dado una conexión de producción sin `app_secret` resoluble, cuando llega un webhook, entonces responde 401, no se encola y se registra una alerta.
- **Firma inválida.** Dado una firma `X-Hub-Signature-256` que no coincide, cuando llega el webhook, entonces responde 401.
- **Alta manual exige secreto.** Dado el formulario de conexión manual de WhatsApp, cuando falta el `app_secret`, entonces no se puede guardar.
- **Test explícito.** Dado el entorno de test, cuando la variable `WEBHOOK_ALLOW_UNSIGNED=true` está puesta, entonces se permite y queda un aviso en el log.

**Evidencia / Definición de Terminado:**
- Tests de integración con firma válida, inválida y ausente.
- `connection_types.py` con `app_secret` obligatorio para WhatsApp manual.

**Implementada (2026-10-02, PR #184 en `devrochy/agent-core`):**
- `WEBHOOK_ALLOW_UNSIGNED` (escape solo de test; en producción se ignora y se registra error).
- Sin `app_secret` resoluble → **401**, no se encola y se alerta (endpoints genérico y por slug).
- `app_secret` obligatorio en el schema de la conexión WhatsApp Meta.
- CI con `WHATSAPP_APP_SECRET` de prueba.
- 4 tests de integración (Gherkin) + 1 del schema; gate de CI verde.

**Riesgos/Notas:**
- El secreto **por conexión** para que BYOK y Embedded Signup convivan llega en [HU-CONN-05](../../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md); esta HU cierra el caso "sin secreto".
