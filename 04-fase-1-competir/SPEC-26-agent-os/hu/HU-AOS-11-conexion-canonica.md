---
id: HU-AOS-11
titulo: "Conexión canónica y conversación por conexión (chat web como conexión)"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [confianza, operacion]
req: [REQ-AOS-01]
dependencias: [HU-AOS-02, HU-CONN-01, HU-CONN-05]
skills: ["meta-whatsapp", "db-migration", "backend-design:migration-safety", "auditor-multitenant"]
estado: en-curso
---

# HU-AOS-11 · Conexión canónica y conversación por conexión (chat web como conexión)

> Estado SDD: En curso — [agent-core #427](https://github.com/devrochy/agent-core/pull/427) y [#452](https://github.com/devrochy/agent-core/pull/452) (parte 1: guardas de pausa, backfill y ruteo por conexión); falta el *contract*, el chat web como conexión y la verificación con Meta real.

**ID:** HU-AOS-11

**Título:** Conexión canónica y conversación por conexión (chat web como conexión)

**Workstream:** Agent OS

**Historia:** Como negocio con varios canales quiero que cada número, widget o buzón sea una conexión con su propia conversación, para que cada conexión tenga su Coordinador y responda siempre por donde escribió el cliente.

**Por qué importa (valor empresarial):** Es la base de "N conexiones por negocio": elimina el puente doble entre modelos de conexión y la conversación compartida entre canales.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-01

**Dependencias:** [HU-AOS-02](HU-AOS-02-esquema-aditivo.md), [HU-CONN-01](../../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md), [HU-CONN-05](../../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md)

**Criterios de aceptación (Gherkin):**
- **Pausa antes del backfill.** Dado una cuenta de Meta pausada (ADR-0122) y conversaciones con y sin `connection_id`, cuando entra o sale un mensaje, entonces las guardas (`motivo_pausa_de_conversacion`, `_registrar_si_pausada`, `outbound_send`, `event_notices`, `_rechazar_si_conexion_pausada`) y `sender.resolve_credentials` resuelven la cuenta por `channel_connections.meta_connection_id` y nada se envía; este cambio se despliega antes del backfill.
- **Backfill.** Dado números vivos de WhatsApp (BYOK, Embedded Signup o manuales) sin fila en `channel_connections`, cuando corre el backfill, entonces cada número tiene **una** conexión ligada a su cuenta, sin credenciales propias (CHECK) y con `is_primary = false`, y las conversaciones tienen su `connection_id`; el *dry-run* reporta los choques con una conexión manual del mismo `external_id` y no crea una segunda fila.
- **Altas posteriores.** Dado un alta o una reconexión de un número por cualquiera de los cinco caminos de ADR-0122 §6, cuando se reclama el número, entonces su conexión se crea o revive en la misma transacción de `claim_assets` (`meta_asset_claims.numero_para_conexion`); y dado la promoción de ADR-0127 §3, entonces se crea la conexión del número real con sus instancias y su release clonadas de la de prueba.
- **Ruteo.** Dado un mensaje a un número, cuando entra, entonces el consumer resuelve la conexión por `connection_external_id` (el webhook no cambia), se abre o continúa la conversación de (conexión, cliente) y la respuesta sale por el número de esa conexión, no por el primer número vivo de la cuenta.
- **Chat web.** Dado la configuración del widget en `AppSettings`, cuando se migra, entonces queda como conexión `webchat`, el endpoint público la resuelve por su clave con un resolvedor `SECURITY DEFINER` y un índice único global de la clave, el secreto de Turnstile pasa a `credentials_encrypted` y, con dos widgets, un visitante no ve la conversación del otro.
- **Reversa.** Dado la bandera `AOS_CONNECTION_ROUTING` apagada antes del *contract*, cuando entra un mensaje, entonces se usa el ruteo anterior sin errores: todavía no hay índice único, la vuelta atrás va en orden inverso (primero `AOS_RUNTIME = legacy` en todos los negocios) y, si la conversación tenía `release_id`, el camino anterior (modificado para eso) lo limpia al cambiar de conexión.
- **Contract sin cerrar conversaciones.** Dado dos conversaciones abiertas del mismo (conexión, cliente), cuando corre el *contract*, entonces queda la más reciente, la otra le pasa sus mensajes y se marca con `deleted_at` (sus tareas y `task_events` no se mueven), y recién después se crea el índice único.
- **Cuota.** Dado un cliente que escribe a dos números del negocio, cuando se mide la cuota `conversaciones`, entonces cuenta dos (enmienda de ADR-0045 en ADR-0115).

**Evidencia / Definición de Terminado:**
- Guardas de pausa y `resolve_credentials` por la conexión, desplegadas antes del backfill; backfill idempotente por lotes (Messenger e Instagram quedan fuera hasta que haya un cliente); altas y promoción que crean la conexión; ruteo por conexión sin reescribir `connection_id`; FK compuesta a `meta_connections`.
- En el *contract* (tras 2 releases estables): deduplicación sin cerrar y luego índice único de conversación abierta por (conexión, cliente). `meta_asset_claims.mover_conversaciones` se elimina en el mismo cambio en que el sender y las guardas dejan de leer `conversations.meta_connection_id`, no antes.
- El backfill pone `type_id` (y `category`) en las conexiones viejas que no lo tienen **antes** del backfill de agentes de [HU-AOS-13](HU-AOS-13-instancias-por-conexion.md): `agent_instance_checks()` rechaza una instancia en una conexión sin tipo conversacional.
- La clave pública del widget de `webchat` (`external_id`) se genera aleatoria (≥ 128 bits, nunca derivada del negocio ni elegida por él): el índice `uq_cc_webchat_key` es global, así que un choque de clave delataría que otro negocio la usa.
- Requisitos de la revisión de seguridad de [HU-AOS-02](HU-AOS-02-esquema-aditivo.md): la clave del widget la genera el servidor (el panel no la recibe del usuario); el resolvedor `SECURITY DEFINER` que reemplaza `web_chat_resolve` resuelve por igualdad sobre `uq_cc_webchat_key`, sin `LIMIT 1`, con `search_path` fijo y solo con conexiones vivas; los errores de `save_connection` no exponen el nombre del constraint (un choque de clave no debe delatar a otro negocio). El índice incluye las conexiones borradas: una clave no se reutiliza nunca.
- El camino anterior, al reescribir `connection_id`, limpia `release_id` y `active_agent_instance_id` (las FKs compuestas apuntan a la conexión anterior).
- Verificación con Meta real en test.

**Riesgos/Notas:**
- El ruteo de webhooks es crítico (ADR-0095): se valida con la conexión BYOK real de test antes de encender la bandera.
- La pausa sigue siendo la de ADR-0122 (por cuenta): `channel_connections` no agrega estado propio para Meta.
- Integraciones: siguen siendo del negocio; ligarlas a una conexión se decide cuando un negocio con varios números lo pida (ADR-0115 §3).
