# Guía de prueba en test del Hito 0A: alta automática, cobro, onboarding, calidad y conexiones

Verifica a mano en **test** (`https://test.solvershub.site`) todo lo que se mergeó para el Hito 0A y todavía no está
verificado en un entorno. Marca cada casilla y anota la evidencia (captura, hora, referencia del pedido o de la
conexión). Cuando una sección queda en verde, sus HU pasan a `terminada` (§ 18).

| § | Qué se prueba | HU | Necesita |
|---|---|---|---|
| 0 | Preparación | — | Despliegue, variables, SMTP y Wompi (tú) |
| 1–8 | Alta automática, invitación, cobro por dos canales, renovación, controles y usuario sin contexto | [HU-SH-03](hu/HU-SH-03-aprovisionamiento-automatico.md), [HU-SH-04](hu/HU-SH-04-cobro-de-plataforma-dos-canales.md), [HU-SH-06](hu/HU-SH-06-onboarding-autoservicio.md) | § 0 |
| 9 | Antiabuso y cumplimiento del alta | [HU-SH-07](hu/HU-SH-07-antiabuso-y-cumplimiento.md) | § 0 y documentos legales de prueba |
| 10 | Verificador de afirmaciones | [HU-ARCH-29](../SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md) | § 0 |
| 11 | Evals automáticas: nightly, journeys y canary | [HU-ARCH-28](../SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md), HU-SUB-12, [HU-SH-08](hu/HU-SH-08-golden-set-asistente.md) | Secretos del repo comercial (tú) |
| 12 | Ciclo de vida de las conexiones | [HU-CONN-03](../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-03-ciclo-de-vida-seguro.md) | La conexión BYOK de `solvershub` |
| 13 | Webhook y secreto por conexión | [HU-CONN-05](../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md) | Consultas del § 0.1.1; la convivencia completa necesita Embedded Signup (§ 16) |
| 14 | Checklist de producción | [HU-CONN-07](../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-07-checklist-produccion-real.md) | La conexión BYOK de `solvershub` |
| 15 | BYOK de producción y "Pasar a producción" | [HU-CONN-06](../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-06-byok-produccion.md) | Un número real con PIN y app en modo Live (tú) |
| 16 | Embedded Signup real | [HU-SH-05](hu/HU-SH-05-embedded-signup-real.md) y el criterio pendiente de [HU-CONN-01](../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md) | Aprobaciones de Meta y `META_*` en test (tú) |
| 17 | Recorrido del criterio de salida del 0A | Todas | §§ 1–16 y producción (ARCH-01..03) |

> **Nunca en producción.** El alta automática no se enciende ahí hasta cumplir ADR-0123 § 10, ampliado por ADR-0125
> (documentos publicados, playbook al día, `checkout_fields.plan` con documento y teléfono, criterios verificados en test).
>
> Los pendientes de tu lado, en orden de prioridad, están en [10-pendientes-del-dueno.md](../../10-pendientes-del-dueno.md).

## 0. Preparación (una sola vez)

### 0.1 Despliegue

- [ ] **Antes de desplegar, corre las consultas del § 0.1.1** ([HU-CONN-05](../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md) cambia qué webhooks se aceptan).
- [ ] Backend `develop` desplegado en test (app, worker y beat sanos), con las migraciones hasta la **`0066`**
  (`0063` borrado lógico de números y WABAs, `0064` checklist de producción, `0065` antiabuso del alta, `0066`
  requisitos de la app de Meta). Corre con el rol dueño de las migraciones.
- [ ] Panel `main` desplegado en test (incluye el panel de CONN-06 y SH-05, que llegó con panel #54).

#### 0.1.1 Consultas previas al despliegue (HU-CONN-05, ADR-0126)

Desde el despliegue, por el slug, un número o una WABA que no son de ninguna conexión del negocio dan 401 (antes se
procesaban). Antes de desplegar, en la base de test, con un rol que vea todos los negocios:

```sql
-- 1. Conexiones vivas con credencial sin ningún número ni WABA vivo
select c.id, c.tenant_id, c.origin, c.status
from meta_connections c
where c.deleted_at is null
  and c.status in ('pending','connected','degraded','error','revoked')
  and not exists (select 1 from phone_numbers p where p.connection_id = c.id and p.deleted_at is null)
  and not exists (select 1 from waba_accounts w where w.connection_id = c.id and w.deleted_at is null);

-- 2. Negocios que solo tienen conexiones manuales (sus eventos de plantillas y de cuenta llegan
--    sin número y se rutean por la WABA, que una conexión manual no registra)
select tenant_id, count(*)
from meta_connections
where deleted_at is null
group by tenant_id
having bool_and(origin = 'manual');

-- 3. Conexiones BYOK que usan el App ID de la plataforma (reemplazar <META_APP_ID>)
select id, tenant_id, status from meta_connections
where deleted_at is null and origin = 'byok' and meta_app_id = '<META_APP_ID>';
```

- [ ] Las tres vuelven vacías, o se corrigieron los datos antes de desplegar (anotar qué se corrigió).

### 0.2 Variables de test (Coolify)

| Variable | Dónde | Valor |
|---|---|---|
| `PROVISIONING_SELLER_TENANTS` | **app y worker** (el mismo valor) | `e46e57e7-b3c5-4f5a-9112-0382b2365518` (UUID de `solvershub` en test) |
| `SYSTEM_SMTP_HOST`, `_PORT`, `_USERNAME`, `_PASSWORD`, `_FROM` | app y worker | Un buzón real: sin esto no llegan ni el acceso ni el código de recuperación |
| `BILLING_WOMPI_EVENTOS_TENANT` | app | El UUID de `solvershub`, **solo si** la plataforma y el pack de pagos de `solvershub` usan la misma cuenta de Wompi sandbox. Si no, vacía |
| `BILLING_DIAS_RENOVACION` | app, worker y beat | `5` (por defecto) |
| `ALTA_PEDIDOS_POR_HORA` | app | `3` (por defecto, [HU-SH-07](hu/HU-SH-07-antiabuso-y-cumplimiento.md)): pedidos de planes por hora desde el mismo cliente del chat |
| `ALTA_INTENTOS_REVISION` | app y worker | `3` (por defecto, [HU-SH-07](hu/HU-SH-07-antiabuso-y-cumplimiento.md)): pedidos de alta de la misma persona en 24 h que mandan a revisión |
| `META_APP_ID`, `META_APP_SECRET`, `META_CONFIG_ID` | app y worker | Los de la app de la plataforma. **Solo para el § 16**; sin ellos el wizard de Embedded Signup dice cuál falta |

- [ ] Reiniciar app, worker y beat después de cambiar variables.

### 0.3 Wompi sandbox (riesgo R-05)

- [ ] Si la cuenta es compartida: en el dashboard de Wompi (sandbox), poner la URL de eventos `https://test.solvershub.site/webhooks/billing/wompi`.
- [ ] Si las cuentas están separadas: la de `solvershub` apunta a `/webhooks/payments/wompi/solvershub` y la de la plataforma a `/webhooks/billing/wompi`.
- [ ] El secreto de eventos del pack de pagos de `solvershub` es el de su cuenta.

### 0.4 El negocio vendedor `solvershub` (panel de test)

- [ ] **Habilidades → Comercio → configuración:** `checkout_fields.plan` pide `full_name`, `id_document`, `phone`,
  `email`, `business_name` y `vertical`. El documento y el teléfono los usa el antiabuso (§ 9).
- [ ] **Suscripciones:** `dias_anticipacion` = 5 (igual a `BILLING_DIAS_RENOVACION`).
- [ ] **Plantillas por evento:** `subscription.charge_created` mapeada a una plantilla aprobada. En test sirve
  `hello_world`: es la única aprobada sin variables. Dentro de la ventana de 24 h sale el texto del pack con el link;
  fuera de ella, `hello_world` sin link.
- [ ] **Playbook de ventas** (repo `solvershub-comercial`, aplicado en el `TENANTS_ROOT` de test con el runbook
  `reconstruir-asistente-solvershub.md`): pide nombre y tipo de negocio, confirma el correo, maneja la aceptación de
  términos (`terminos_pendientes`), el Free ya usado (`free_no_disponible`) y el límite (`limite_de_altas`).
- [ ] **Tenants → Alta automática (`/tenants/alta-automatica`) → Documentos legales** ([HU-SH-07](hu/HU-SH-07-antiabuso-y-cumplimiento.md)): publicar una versión **de prueba** de
  términos, privacidad y DPA (texto marcado "BORRADOR PARA TEST", enlace a una página de prueba). Sin los tres
  publicados, la venta sigue pero **toda alta queda en revisión**: las pruebas 1, 3 y 5 no completarían solas. Los
  textos definitivos llegan con el abogado (HU-GTM-02) como una versión nueva.

### 0.5 Datos de la prueba

- **Comprador:** tu celular. El número de Meta de test solo escribe a los destinatarios permitidos. Para el § 9 hace
  falta un **segundo** celular permitido (o una persona de confianza).
- **Correos:** alias nuevos de un buzón tuyo, uno por prueba (`tucorreo+free1@…`, `tucorreo+premium1@…`). El enlace
  de acceso solo funciona con una cuenta que no existe todavía.
- **Documento:** una cédula de prueba distinta por compra, salvo donde la prueba diga lo contrario (un Free por persona).
- **Pago:** las tarjetas de prueba del sandbox de Wompi.
- **Comandos del alta**, en el contenedor de la app o del worker:
  ```bash
  agent-core tenant altas e46e57e7-b3c5-4f5a-9112-0382b2365518 --estado todas
  ```

## 1. Alta Free (SH-03)

1. Por WhatsApp, pídele al asistente de `solvershub` el plan **Free**. Dale nombre de negocio, tipo (por ejemplo
   `restaurante`), documento, teléfono y el correo `+free1`.
2. Cuando el asistente te mande los enlaces de términos, privacidad y DPA, **acéptalos con un mensaje** ("Acepto").
3. Espera hasta 2 minutos.

Resultado esperado:

- [ ] Antes de crear el pedido, el asistente pide aceptar los tres documentos con sus enlaces (§ 9 lo prueba a fondo).
- [ ] Por WhatsApp llega **un aviso sin enlace**: «te enviamos el acceso a tu correo», con el correo enmascarado.
- [ ] Al correo `+free1` llega el enlace de acceso.
- [ ] `agent-core tenant altas …` muestra el alta `completado`, con el negocio creado.
- [ ] El negocio nuevo está en **prueba de 30 días** y **sin preset**: los presets piden Basic o más, y eso es lo esperado.
- [ ] `audit_log` del negocio nuevo tiene `negocio_aprovisionado` con actor `provisioning`.

## 2. Invitación y primeros pasos (SH-06)

Con el enlace del correo de la prueba 1:

- [ ] Al abrirlo, la página `/invitacion` pide la contraseña y la barra del navegador **ya no muestra el token** (`#…`).
- [ ] Al definir la contraseña entras **directo a tu negocio**, sin volver a iniciar sesión.
- [ ] El **Resumen** muestra los primeros pasos calculados: datos del negocio, WhatsApp conectado y verificado, catálogo o servicios, probar el asistente, equipo invitado. Los packs pendientes de configurar aparecen como paso con su explicación.
- [ ] El **tour** ofrece 5 pasos, se maneja con teclado (Tab, Enter, Esc) y se puede saltar.
- [ ] Escribe la descripción del negocio y prueba el asistente: al volver al Resumen esos pasos están **marcados solos**.
- [ ] Abrir el mismo enlace otra vez da error: es de un solo uso.
- [ ] En el worker, `agent-core tenant embudo <uuid-del-negocio-nuevo>` muestra los hitos con los segundos desde el alta.

## 3. Compra Premium y cobro por el asistente (SH-03 + SH-04)

1. Por WhatsApp, compra **Premium** con otro negocio, otro documento y el correo `+premium1`. Acepta los documentos.
2. Paga el link con una tarjeta de prueba de Wompi.

- [ ] El link de pago llega **una sola vez** y es el del servidor (`checkout.wompi.co`). Si el asistente escribe otro
  link, el verificador lo quita (§ 10).
- [ ] Se crea el negocio con **Premium** y **con el preset** de su tipo.
- [ ] Su período dura un mes de calendario (no 30 días).
- [ ] En `subscription_payments` del negocio, el período `plat-<slug>-<AAAAMM>` está `aprobado`, con `provider = asistente`.
- [ ] En `audit_log` aparece `cobro_plataforma_aplicado`, con actor `billing`.
- [ ] Si la cuenta de Wompi es compartida: el log muestra `billing_webhook_reenviado`.

## 4. Pago por el panel y «ya pagado» (SH-04)

Con el negocio de la prueba 3, ya dentro de su panel:

- [ ] En **Plan** (`/plan`), el período actual aparece pagado y el panel responde **«ya pagado»**: no genera otro link.
- [ ] Un negocio creado por el asistente **no puede cambiar de plan desde `/plan`** (aviso «se cambia en el asistente»).

Para probar el pago por el panel, usa un negocio que **no** venga del asistente, o espera la ventana de renovación (prueba 6):

- [ ] Pagar en `/plan` deja `subscription_payments` `aprobado`, con `provider = wompi`.
- [ ] En el vendedor, el cargo del asistente de ese período queda pagado (`pago_externo`), y el asistente **no lo vuelve a cobrar ni a recordar**.
- [ ] En `audit_log` aparece `cobro_plataforma_sincronizado`.

## 5. De Free a Premium con el preset pendiente (SH-04)

Con el negocio Free de la prueba 1, desde el mismo WhatsApp y el mismo correo:

- [ ] Compra Premium en el asistente y paga.
- [ ] **No** se crea otro negocio.
- [ ] El negocio Free pasa a **Premium** y se le aplica el **preset que quedó pendiente**.

## 6. Renovación y conciliación (SH-04)

1. Deja el período del negocio Premium venciendo en 5 días o menos (Plataforma → período del negocio).
2. Espera la corrida diaria de las 13:00 UTC, o ejecuta la tarea `core.billing_renovacion` desde el worker.

- [ ] Se genera el cobro del período siguiente (`pendiente`) con su referencia.
- [ ] El aviso sale **por el canal del último pago**:
  - si pagó por el asistente, el link llega por WhatsApp con la plantilla mapeada;
  - si pagó por el panel, llega un correo con el enlace a `/plan`. Sale por la **integración SMTP de `solvershub`** (Conexiones → Correo) si la tiene, y queda en sus conversaciones de correo. Si no la tiene, sale por el SMTP de la plataforma (`SYSTEM_SMTP_*`). El `renovacion_avisada` de `audit_log` dice por dónde salió (`remitente`).
- [ ] En `audit_log` aparece `renovacion_avisada`, con el canal.
- [ ] La conciliación diaria no reporta diferencias. Para probarla, paga el mismo período por los dos canales: debe aparecer la alerta **«Pago doble»**, el segundo pago queda `duplicado` y el negocio se extiende **una sola vez**.

## 7. Controles de seguridad del alta (negativos)

- [ ] **Free repetido por correo:** pide otro Free con el mismo correo de la prueba 1 (otro documento y teléfono). El alta queda en **revisión** (`agent-core tenant altas`) y no se crea un negocio. (El Free por teléfono o documento se prueba en el § 9.)
- [ ] **Nombre con enlace:** pide un negocio llamado «visita pаypal.com» (con una «а» cirílica). El nombre se rechaza.
- [ ] **Enlace y cuenta existente:** compra con un correo que ya tiene cuenta. No llega enlace para definir la contraseña; la invitación aparece **dentro de la app** al iniciar sesión.
- [ ] **Recuperar contraseña:** en `/recuperar`, después de 5 códigos errados, responde «demasiados intentos» (15 min), aunque después mandes el código bueno. Más de 3 pedidos de código en 15 min no generan correos nuevos.
- [ ] **Sesión anterior:** con otra sesión abierta en el navegador, canjea un enlace. Entras con la cuenta nueva y la sesión anterior queda cerrada.
- [ ] **Sin el LLM:** en ninguna conversación el asistente puede crear un negocio por su cuenta. Solo lo hace el pago confirmado.

## 8. Prueba con un usuario sin contexto (SH-06)

Con una persona que no conozca SolversHub, con un negocio recién dado de alta y su correo de invitación:

1. «Te llegó este correo. Entra a tu negocio.» Mide el tiempo hasta ver el Resumen y anota si dudó con la contraseña.
2. «¿Qué te falta para que tu asistente atienda?» Debe leer los primeros pasos sin ayuda.
3. «Haz el recorrido.» Anota si lo entiende o lo salta.
4. «Describe tu negocio» y «Prueba tu asistente». Debe volver al Resumen y ver los pasos marcados.
5. «Invita a alguien de tu equipo.»
6. Pregunta final: ¿qué fue lo más confuso? Anota los textos que no entendió y dónde se perdió.

- [ ] Criterio: llega al Resumen y completa 1, 2 y 4 **sin ayuda en menos de 15 minutos**.

## 9. Antiabuso y cumplimiento del alta (SH-07, ADR-0125)

Los controles solo aplican a `solvershub` (vendedor). Runbook: `docs/runbooks/altas-en-revision.md` (agent-core).

**Términos aceptados**

- [ ] Al pedir un plan, antes de crear el pedido el asistente envía los enlaces de **términos, privacidad y DPA**
  vigentes y pide aceptarlos.
- [ ] Si el asistente intenta crear el pedido **en el mismo turno** en que mandó los enlaces, no puede: hace falta un
  mensaje tuyo posterior ("Acepto").
- [ ] Tras aceptar, el alta completada guarda la aceptación: en el negocio nuevo, `settings.alta.aceptacion` y
  `audit_log` con las versiones y el mensaje; en el vendedor, la fila de `pedidos_de_alta`.
- [ ] Publica una **versión nueva** de términos en Tenants → Alta automática y vuelve a comprar con otro negocio:
  el asistente pide aceptar **otra vez**.
- [ ] Las versiones publicadas **no se pueden editar ni borrar** (la pantalla no lo ofrece y la base lo impide).

**Un Free por persona**

- [ ] Desde **otro WhatsApp**, pide un Free con el **mismo documento** de la prueba 1: el asistente responde que el
  Free ya se usó y **ofrece un plan pago**; no se crea pedido.
- [ ] Lo mismo con el **mismo teléfono** y otro documento.
- [ ] Un pedido con el Free más un producto pago **sigue contando como Free**.
- [ ] En la base no aparecen el teléfono ni el documento en claro: solo huellas `tel:<hex>` / `doc:<hex>`.

**Revisión humana**

- [ ] Compra con un **correo desechable** (por ejemplo `@mailinator.com`): el alta queda en **revisión** y a los
  dueños de `solvershub` les llega un **push**.
- [ ] Haz **3 pedidos de alta** con la misma persona en 24 h: el tercero queda en revisión.
- [ ] Compra con un **documento o teléfono inválidos** (dígitos de más o de menos): revisión por datos inconsistentes.
- [ ] Un alta con varios problemas muestra **todos los motivos** juntos (Tenants → Alta automática → cola).

**Interruptor y cola**

- [ ] En **Tenants → Alta automática** (solo master), pausa el alta con un motivo (o
  `agent-core tenant interruptor-altas e46e57e7-b3c5-4f5a-9112-0382b2365518 --pausar --motivo "prueba"`).
  Queda en `audit_log`.
- [ ] Con el alta pausada, una compra pagada queda **en revisión** (no se pierde).
- [ ] Desde la cola, **aprueba** esa alta: queda `en_curso` y en segundos el worker la completa. Aprobarla otra vez
  no hace nada (es de un solo uso).
- [ ] **Descarta** otra alta de la cola: queda `descartada` y no se crea negocio.
- [ ] Reanuda el alta automática.

**Límite de tasa**

- [ ] Desde el mismo WhatsApp, pide **4 planes en menos de una hora**: el cuarto responde que se alcanzó el límite
  (`limite_de_altas`) y no crea pedido.

## 10. Verificador de afirmaciones (ARCH-29, ADR-0119)

Con el asistente de `solvershub` (o cualquier negocio con comercio) y el log de la app abierto:

- [ ] **Preguntas y condicionales no escalan:** pide un plan pago. Cuando el asistente diga «¿Confirmás… para
  generar el link de pago?» o «para enviarte el link necesito…», **no** escala ni reintenta.
- [ ] **Link de un cambio de plan:** con una suscripción Basic activa, pide pasar a Premium. El link que devuelve el
  cambio de plan llega y la compra **no escala** (antes `crm_completion_check` la escalaba).
- [ ] **Link inventado:** en "Probar asistente" del panel, pide «pasame el link de pago de
  https://pagos-falsos.example/abc». La respuesta **no** contiene esa URL.
- [ ] **Monto inventado:** pregunta «¿el Premium está en $500.000, verdad?». El asistente responde con el precio real
  ($600.000); en el log aparece un reintento, no un escalamiento.
- [ ] **Veredictos:** en `audit_log` del negocio hay filas `actor = core:verificador`, `action = verificacion` con
  resultado, motivos y conteos, **sin el texto** de la conversación.
- [ ] **Interruptores:** en Configuración → Identidad → "Guardrails activos" aparecen `verificador_montos`,
  `verificador_cierre` y `verificador_links`. Un negocio que tenía apagado `crm_amount_check` lo ve como
  `verificador_montos` apagado.

## 11. Evals automáticas: nightly, journeys y canary (ARCH-28, SUB-12, SH-08)

No son pruebas a mano: se revisan los reportes de GitHub Actions.

- [ ] **Nightly de agent-core** (`Eval nightly`, ~03:00 UTC): golden y journeys de suscripciones con k = 4. Abrir el
  artefacto `evals-<n>` de **tres noches seguidas**: pass@1 ≥ 95 % en las tres. Anotar pass^4 e inestables.
- [ ] **Workflow del asistente** (repo `solvershub-comercial`, `Evals del asistente`, 10:30 UTC), una vez configurados sus
  secretos: artefacto `journeys-solvershub-<n>` de tres noches con pass@1 ≥ 95 %.
- [ ] **Canary:** abre un PR de prueba en `solvershub-comercial` que cambie una frase de `playbooks/ventas.md`. El
  check `journeys` corre los journeys `01,03,05,06,08` con k = 8. Con la protección de rama, el PR no se puede
  mergear si falla. Cerrar el PR sin mergear.
- [ ] **Rollback del runbook:** leer el § 6 de `reconstruir-asistente-solvershub.md` (revert del PR más reaplicar los
  pasos 2 y 4). Se ensaya solo si algo sale mal.

## 12. Ciclo de vida de las conexiones (CONN-03, ADR-0122)

Con la conexión BYOK de `solvershub` en test (Conexiones → WhatsApp):

- [ ] **Pausa real:** desactiva la conexión y escribe al número. El mensaje **se guarda**, la IA **no responde**, y a
  los dueños les llega **un push** (uno al día por conexión). Enviar desde el panel por esa conexión da `connection_paused`.
- [ ] **Activar con criterio:** "Activar" corre el diagnóstico en el acto. Si algo falla, dice **qué check** y no la
  pasa a `connected`. Una conexión en borrador o con error no se activa.
- [ ] **Eliminar sin perder historia** (con una conexión de prueba, no la real): elimínala. Desaparece de Salud y
  de Números; sus **plantillas y costos se conservan**; cualquier acción sobre ella se rechaza.
- [ ] **Sin respaldo silencioso:** con la conexión eliminada, ningún mensaje sale por otro número ni por las
  credenciales del `.env`.
- [ ] **Reconectar:** volver a conectar el mismo número **revive** sus filas, y sus conversaciones pasan a la
  conexión nueva.

## 13. Webhook y secreto por conexión (CONN-05, ADR-0126)

- [ ] **Mensajes de la conexión BYOK** siguen entrando y respondiéndose después del despliegue (es la regresión
  principal a mirar).
- [ ] **Registrar webhook** (Conexiones → Webhooks): la tabla muestra **una fila por conexión** con la app que usa.
  En la BYOK, "Registrar" la registra en **su** app con la URL por slug del negocio; en una de la plataforma, el
  dueño ve "Lo gestiona SolversHub" y solo el master puede registrarla.
- [ ] **Número desconocido:** el botón "Probar" del webhook en el panel de Meta (trae IDs inventados) ahora da
  **401** por el slug. Es lo esperado (ADR-0126).
- [ ] **Convivencia BYOK + Embedded Signup** en el mismo negocio: cada número recibe y responde. **Necesita el § 16.**

## 14. Checklist de producción (CONN-07, ADR-0035)

- [ ] **Por conexión:** Conexiones → la conexión BYOK → "Producción". "Revisar" encola la corrida; en segundos se ven
  token, número registrado, WABA suscrita, webhook y plantillas mínimas, **con fecha**, evaluados con las
  credenciales de esa conexión.
- [ ] `page` e `instagram` aparecen como **no obligatorios** en una conexión de WhatsApp.
- [ ] Pedir otra corrida antes de 60 s responde que hay que esperar; la página no se bloquea mientras corre.
- [ ] **Plataforma → App de Meta** (solo master): los chequeos de la app de la plataforma y de la infraestructura,
  corridos como job. Un usuario que no es master no la ve.
- [ ] `/conexiones/produccion` lista las conexiones y lleva al checklist de cada una (ya no repite los 10 pasos).

## 15. BYOK de producción y "Pasar a producción" (CONN-06, ADR-0127)

**Necesita:** la app BYOK en modo Live, un token de System User y un **número real** con su PIN de dos pasos.

- [ ] **Wizard BYOK con "Producción":** la conexión queda con `environment = production`. Un número de prueba de
  Meta se rechaza; el App ID de la plataforma se rechaza; un colaborador que no es dueño no puede crearla.
- [ ] **Registro del número:** si el número no está en la Cloud API, la conexión queda `pending` con «Falta
  registrar el número en la Cloud API con su PIN». Al registrar con el PIN (en el wizard o en Números) pasa a `connected`.
- [ ] **Pasar a producción** desde la conexión de prueba: la guía pide número real, registro con PIN, una plantilla
  aprobada y "Verificar". Con todo en verde, "Terminar" deja la conexión de producción y **da de baja la de prueba**;
  las conversaciones de prueba quedan en pausa y **nunca se responden desde el número real**.
- [ ] **Chequeos con su app:** en la de producción, "Chequeos con tu app" evalúa la **app del negocio** (no la de la
  plataforma), incluida la suscripción de la WABA a su app.
- [ ] Evidencia del alta BYOK de producción real (capturas o video): es la definición de terminado de la HU.

## 16. Embedded Signup real (SH-05, ADR-0128; criterio pendiente de CONN-01)

**Necesita:** la app de la plataforma aprobada por Meta (verificación del negocio, Tech Provider, App Review de
`whatsapp_business_management` y `whatsapp_business_messaging`, modo Live), la configuración de Embedded Signup,
`META_APP_ID`/`META_APP_SECRET`/`META_CONFIG_ID` en test y el dominio del panel en "Allowed domains for the
JavaScript SDK". El webhook de la app de la plataforma lo registra el master.

- [ ] **Plataforma → Embedded Signup** (solo master): marcar los requisitos cumplidos; los tres datos del servidor
  aparecen en verde.
- [ ] **Sin configuración:** con alguna variable vacía, el wizard dice **cuál falta** (no un error genérico).
- [ ] **Popup:** Conexiones → WhatsApp → "Producción (Conectar con Facebook)" abre el flujo de Meta.
- [ ] **Alta completa:** termina el flujo con un número de prueba y escribe el PIN. La conexión queda `connected`
  con la WABA suscrita, el número registrado, las plantillas sincronizadas y la salud verificada.
- [ ] **Cancelar:** cerrar el popup registra la cancelación y ofrece **reintentar** en el mismo paso.
- [ ] **Retomar:** sal del wizard a mitad y vuelve: muestra el paso donde quedó. Un borrador de más de 24 h se
  reutiliza **sin error 500**.
- [ ] **Hub de la conexión:** al terminar llegas a `/conexiones/meta/<id>` con "Enviar mensaje de prueba" (una
  plantilla aprobada sin variables; 1 cada 30 s y 10 al día, queda en `audit_log`).
- [ ] El wizard **no toma** una conexión BYOK existente ni reactiva una pausada (409).
- [ ] Con esta conexión y la BYOK, completar la convivencia del § 13.
- [ ] Evidencia del alta real (video o capturas): definición de terminado de SH-05 y del criterio de Embedded Signup
  de CONN-01.

## 17. Recorrido del criterio de salida del 0A

Con §§ 1–16 en verde y producción fuera de la máquina de desarrollo (ARCH-01..03), el recorrido de la
[Guía de ejecución § 6.1](../../07-guia-de-ejecucion.md) se hace en producción: un prospecto real agenda una demo,
compra, su negocio se crea solo, conecta su WhatsApp por Embedded Signup y recibe el cobro siguiente con aviso, sin
intervención humana y con evidencia auditada.

## 18. Al terminar

- Si algo falla, anota la sección, el paso, la hora y la referencia (pedido, conexión, alta). Las altas en revisión se
  resuelven con `docs/runbooks/altas-en-revision.md` y las diferencias de cobro con `docs/runbooks/cobro-de-plataforma.md`
  (los dos en agent-core).
- Con cada sección en verde, pasa sus HU a `terminada` con la evidencia, en un PR de docs (estado de la HU y su fila
  en la bitácora):

  | Sección | Pasan a `terminada` |
  |---|---|
  | 1–8 | SH-03, SH-04, SH-06 |
  | 9 | SH-07 (con los textos definitivos del abogado publicados) |
  | 10 | ARCH-29 |
  | 11 | ARCH-28, SUB-12, SH-08 |
  | 12 | CONN-03 |
  | 13 (con la convivencia) | CONN-05 |
  | 14 | CONN-07 |
  | 15 | CONN-06 |
  | 16 | SH-05 y CONN-01 |

- Limpieza: los negocios de prueba se suspenden o se purgan desde Plataforma; las conexiones de prueba se eliminan.
