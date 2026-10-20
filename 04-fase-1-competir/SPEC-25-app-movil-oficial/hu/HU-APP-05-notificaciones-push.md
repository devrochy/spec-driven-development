---
id: HU-APP-05
titulo: Notificaciones push
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, diferenciacion]
req: [REQ-APP-05]
dependencias: [HU-APP-02]
skills: [agentcore-conventions, backend-design:observability-by-default]
estado: terminada
---

# HU-APP-05 · Notificaciones push

> Estado SDD: Terminada — push verificado de punta a punta en dispositivo 2026-10-08 (token registrado, push recibido y deep link).

**ID:** HU-APP-05

**Título:** Notificaciones push

**Workstream:** App móvil

**Historia:** Como dueño o gestor quiero recibir notificaciones push en el teléfono cuando pasa algo relevante (escalación de un cliente, cita próxima, pago o gasto de un gestor, promesa incumplida) y que al tocarlas me lleven a la pantalla exacta, para reaccionar a tiempo sin abrir la app constantemente.

**Por qué importa (valor empresarial):** Hoy las notificaciones de la app son pull (`/gestor/notificaciones`) y el panel no empuja nada al móvil. El push convierte la app en canal de alerta real, eleva la respuesta del dueño ante escalaciones y es un argumento de venta frente a la matriz.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-05

**Dependencias:** [HU-APP-02](HU-APP-02-sesion-unica-y-recuperacion.md)

**Criterios de aceptación (Gherkin):**
- **Registro.** Dado un usuario logueado que acepta notificaciones, cuando la app obtiene el token Expo, entonces lo registra en `POST /api/v1/me/push-token` con su dispositivo y negocio.
- **Envío.** Dado un evento relevante (p. ej. una escalación nueva), cuando el backend lo procesa, entonces envía push vía Expo Push Service a los destinatarios con permiso sobre esa sección y al gestor correspondiente.
- **Deep link.** Dado un push recibido y tocado, cuando la app abre, entonces navega a la pantalla de destino (conversación, cita, diario) usando el deep link.
- **Permisos.** Dado un usuario sin permiso sobre la sección del evento, cuando se envía el push, entonces no lo recibe.
- **Opt-out.** Dado un usuario que desactiva notificaciones en Ajustes, cuando ocurre un evento, entonces no recibe push y su token se da de baja en el backend.

**Evidencia / Definición de Terminado:**
- Backend: tabla `push_tokens` (tenant_id + RLS forzada), endpoints de registro/baja, cliente de Expo Push Service y tareas Celery para los eventos acordados (escalación, cita, pago/abono/gasto del campo, promesa, mora); tests de envío con mock del proveedor y RBAC.
- App: `expo-notifications` con permisos, canales Android, manejo en foreground/background/killed y navegación por deep link; bandeja in-app sincronizada con `/gestor/notificaciones`.
- Evidencia en test: push de escalación recibido y deep link funcionando; CI verde en ambos repos.

**Implementada (2026-10-06):** [agent-core #243](https://github.com/devrochy/agent-core/pull/243) + **Implementada (2026-10-06):** [solvershub-apk #110](https://github.com/devrochy/solvershub-apk/pull/110) — push Expo con deep links (ADR-0095/0099).

**Riesgos/Notas:**
- Requiere credenciales del proyecto Expo (projectId EAS, ya existente y no renombrable) y, en producción, revisar cuotas del servicio Expo Push.
- El envío es determinista desde el servidor (Celery), nunca desde el modelo; los textos de push viven en playbooks/config, no en código.

**Backend implementado (2026-10-05):** [agent-core #243](https://github.com/devrochy/agent-core/pull/243) (base: rama de #240) — tabla `push_tokens` (0052, RLS forzada), `POST/DELETE /api/v1/me/push-token`, cliente Expo + tareas Celery (`EXPO_PUSH_*`), disparadores de escalación y de sync de campo por gestor (destinatarios: dueños). ADR-0095. 9 tests de integración en verde. Los disparadores de cita/próxima y promesa/mora quedan para una HU de seguimiento.

**App implementada (2026-10-06):** [solvershub-apk #110](https://github.com/devrochy/solvershub-apk/pull/110) — módulo `src/modules/notificaciones/` (permisos, canal Android, token Expo con projectId EAS, alta/baja en `/me/push-token`, `PushProvider` con re-registro por negocio y baja en logout), deep link v1 (`cobranza.sync` → Diario) y 11 tests (547/547). Deuda: Expo Go ya no recibe push remoto (E2E real con dev client/APK preview); switch de opt-out en [HU-APP-12](HU-APP-12-configuracion-movil.md); deep links del panel con [HU-APP-04](HU-APP-04-dashboard-con-kpis.md)/08/11. **Fix 2026-10-06** ([apk #118](https://github.com/devrochy/solvershub-apk/pull/118)): guard `isRunningInExpoGo()` — todas las utilidades de push son no-op en Expo Go (el SDK lanza al pedir token allí) y dependencias alineadas al SDK 57 con `expo install --fix`. **Fix 2026-10-06 (2)** ([apk #120](https://github.com/devrochy/solvershub-apk/pull/120)): causa raíz capturada con `adb logcat` — importar el paquete evalúa su auto-registro (`DevicePushTokenAutoRegistration.fx`), que lanza `[runtime not ready]` en Expo Go/Android; ahora se carga con require diferido y nunca se evalúa en Expo Go. Verificado en dispositivo (arranque limpio, 0 errores JS).

**Reabierta (2026-10-08): push no funciona en APK.** Diagnóstico en el OPPO y en el entorno de test:
- La app no trae `google-services.json`. En Android, `getExpoPushTokenAsync` necesita Firebase, así
  que ningún APK obtiene token, y el provider se tragaba el error. En test hay un solo token en
  `push_tokens`, del 2026-10-06; desde entonces no se registró ninguno, aunque hubo muchos logins
  con v4, v5 y v6.
- El worker de test no tiene `EXPO_PUSH_ENABLED`: el envío queda en log (`push_disabled`).
- Sin estas piezas no se puede cumplir la evidencia "push de escalación recibido" de la DoD.

[solvershub-apk #139](https://github.com/devrochy/solvershub-apk/pull/139) deja la app lista:
`googleServicesFile` desde la variable de archivo de EAS `GOOGLE_SERVICES_JSON`, el error de
token visible en logcat y la guía `docs/push-android.md`. **Pendiente (manual):**
1. Crear el proyecto de Firebase y subir `google-services.json` a EAS.
2. Subir la clave FCM V1 a las credenciales de EAS.
3. Poner `EXPO_PUSH_ENABLED=true` en el worker de test.
4. Build `preview` y E2E en dispositivo: token registrado, push recibido y deep link.

**Verificada en dispositivo (2026-10-08, OPPO CPH2603, APK preview `a14abc11`):**
- Firebase: `google-services.json` va como variable de archivo de EAS (`GOOGLE_SERVICES_JSON`) y la
  clave FCM V1 está en las credenciales de EAS. Se confirmó que el APK trae `google_app_id`; el v6 no lo traía.
- Permiso: la app nunca mostraba el diálogo. Android 13+ no lo muestra sin un canal creado, y un
  permiso nunca pedido llega como `denied`. Se corrigió en [solvershub-apk #141](https://github.com/devrochy/solvershub-apk/pull/141):
  se crea el canal antes y se pide mientras `canAskAgain` lo permita.
- Registro: el dueño (`dueno-a@demo.test`, Cobranza Demo) aceptó el permiso y apareció un token
  `android`/`expo` nuevo en `push_tokens`.
- Envío: con `EXPO_PUSH_ENABLED=true` en el worker de test, la tarea `core.push.notify_owners`
  terminó en Expo `200 OK` y `push_sent destinatarios=1`.
- Recepción y deep link: con la app en segundo plano, la notificación llegó al teléfono. Al tocarla,
  la app abrió **Conversaciones** (`core.escalation`). La actividad de campo (`cobranza.sync`) lleva
  a Cobranza en el panel y a Cartera en la sesión de campo (#141).

**Pendientes menores (actualizado 2026-10-08):**
- ~~Arranque en frío~~: **resuelto** en [solvershub-apk #142](https://github.com/devrochy/solvershub-apk/pull/142).
  Probado en el OPPO matando el proceso con `am kill`: el push llegó y, al tocarlo, la app abrió
  Conversaciones. Con `am force-stop` Android no entrega FCM hasta que el usuario vuelva a abrir
  la app; eso es del sistema.
- #142 también incluye el arreglo del permiso, que había quedado fuera del merge de #141.
- ~~`channelId`~~: **resuelto** en [agent-core #289](https://github.com/devrochy/agent-core/pull/289)
  (`solvershub-general`). Falta desplegarlo en el worker de test.
- En test sigue arriba un worker viejo (`wv6kycjeae…`, imagen del 2026-09-28) sin `EXPO_PUSH_ENABLED`.
