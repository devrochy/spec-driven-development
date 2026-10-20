---
id: HU-ARCH-13
titulo: Plantillas de WhatsApp fuera de la ventana de 24 horas
spec: SPEC-02
fase: 0
hito: 0A
workstream: Canales y conexiones
prioridad: P0
critico: true
estimacion: M
impacto: [ingreso, operacion]
req: [REQ-ARCH-15, REQ-COMP-03]
dependencias: []
skills: ["adr", "backend-design:idempotency-and-side-effects", "backend-design:error-handling-as-design", "deep-research", "meta-whatsapp"]
ola: 2
estado: terminada
---

# HU-ARCH-13 · Plantillas de WhatsApp fuera de la ventana de 24 horas

> Estado SDD: Terminada — implementada 2026-10-08; verificada en test contra Meta real el mismo día (los 4 casos).

**ID:** HU-ARCH-13

**Título:** Plantillas de WhatsApp fuera de la ventana de 24 horas

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero que los avisos de cobro, recordatorios de cita y seguimientos se envíen con una plantilla aprobada cuando el cliente no ha escrito en 24 horas para que lleguen siempre.

**Por qué importa (valor empresarial):** Cobrar una suscripción, recordar una demo o recuperar un carrito ocurre casi siempre fuera de la ventana. Sin plantillas, el producto no puede cobrar por sí mismo: es la pieza que habilita el ingreso recurrente de todo el Hito 0A.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-15, REQ-COMP-03

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Envío fuera de ventana.** Dado un cliente que escribió hace 30 horas y un evento `subscription.charge_created` con plantilla mapeada, cuando se envía el aviso, entonces sale como plantilla con las variables resueltas del evento y queda `sent`.
- **Dentro de ventana.** Dado un cliente que escribió hace 2 horas, cuando ocurre el mismo evento, entonces se envía el texto de respaldo (más barato) en vez de la plantilla.
- **Sin plantilla.** Dado un evento sin plantilla mapeada y la ventana cerrada, cuando se intenta enviar, entonces se registra `sin_plantilla` y el negocio ve una alerta en el panel.
- **Respuesta humana.** Dado un operador que responde fuera de ventana y recibe 409 `window_expired`, cuando abre el selector, entonces puede elegir una plantilla aprobada y enviarla.
- **Variables seguras.** Dado una plantilla con variables, cuando se resuelven, entonces salen del evento o de la base, nunca del texto del LLM.

**Evidencia / Definición de Terminado:**
- `send_template` en el adapter, con test contra un mock de la Graph API.
- Config `message_templates_map` editable en el panel y documentada.
- ADR "Plantillas por evento".

**Implementada (2026-10-08):** [agent-core #277](https://github.com/devrochy/agent-core/pull/277) (ADR-0108, migración `0057`) + [panel #38](https://github.com/devrochy/solvershub-panel/pull/38). `send_template` en el adapter; `app_settings.message_templates_map` (evento → plantilla aprobada, variables con rutas permitidas, texto de respaldo); `send_event_notice` (ventana abierta → texto, cerrada → plantilla `APPROVED` de la WABA de la conexión, sin plantilla → `failed`/`sin_plantilla`); `subscription.charge_created` por el outbox desde `generar_cargos`; el 409 `window_expired` del operador vuelve a salir (el sender se lo tragaba) con selector de plantillas en la conversación; editor en `/plantillas/eventos` y alerta `sin_plantilla` en el Resumen. Revisión de seguridad aplicada (sin envío por el número de la plataforma, parámetros limpios, ventana desconocida = cerrada, reintento si no se encola). 24 tests nuevos · suite 1071.

**Riesgos/Notas:**
- Las plantillas se crean y sincronizan por WABA (ya existe, ADR-0031); el envío por conexión depende del resolver de credenciales ([HU-CONN-01](../../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md)) para BYOK.

**Verificada en test contra Meta real (2026-10-08):** negocio `solvershub`, número de prueba de Meta
`+1 555-191-6775`, conversación con el celular del dueño (destinatario permitido). Se usaron las mismas
funciones del core que llaman el outbox y la API. El mapa `subscription.charge_created` →
`jaspers_market_order_confirmation_v1` (UTILITY, aprobada; variables `cliente.nombre`,
`cargo.referencia`, `cargo.fecha_vencimiento`) se puso solo para la prueba; al terminar, el mapa y la
ventana de la conversación volvieron a su estado anterior.

| Caso | Resultado | Evidencia |
|---|---|---|
| Dentro de ventana | `texto`: sale el texto de respaldo con las variables del evento | `wamid.…`, estado `read` |
| Fuera de ventana con plantilla mapeada | `plantilla`: sale la plantilla con las variables resueltas | `wamid.…`, estado `read` |
| Sin plantilla y ventana cerrada | `sin_plantilla`: mensaje `failed` con `error_reason = sin_plantilla` | lo cuenta `GET /admin/settings/message-templates/missing` (alerta del Resumen) |
| Operador fuera de ventana | `send_to_conversation(raise_on_window_expired=True)` lanza `window_expired` (409 en la API); el selector lista las 5 aprobadas de la WABA; la plantilla enviada como `human` sale | `wamid.…`, estado `read` |

Las variables seguras ya estaban cubiertas por los tests unitarios (rutas permitidas por evento).

**Hallazgos al verificar:**
- [agent-core #296](https://github.com/devrochy/agent-core/pull/296): una conversación que pasó de WhatsApp
  Web (QR) al número de Meta respondía por WhatsApp Web (sesión caída, `client is nil`). Ahora responde
  por donde escribió el cliente. Se mergeó y desplegó en test.
- Tras agotar los reintentos de envío, la conversación se escaló (`send_failed`) y el bot quedó pausado.
  Es el comportamiento esperado: hubo que resolver la escalación para que el bot volviera a responder.
- La salud de la conexión marca `degraded` por `code_verification_status = NOT_VERIFIED`. En un número de
  prueba de Meta eso **no impide enviar** (se verificó que entrega), así que la comprobación
  `number_registered` da un falso negativo con números de prueba. Queda como seguimiento.
- La plantilla en español `pedido_cancelado` sigue `PENDING` y es de MARKETING. Para avisos de cobro en
  producción hace falta una de UTILITY en español aprobada en la WABA real del negocio.
