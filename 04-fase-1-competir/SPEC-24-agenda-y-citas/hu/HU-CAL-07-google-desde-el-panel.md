---
id: HU-CAL-07
titulo: Conectar Google Calendar desde el panel nuevo
spec: SPEC-24
fase: 1
hito: "1"
workstream: Agenda
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, confianza]
req: [REQ-CAL-03]
dependencias: [HU-CAL-02]
skills: ["backend-design:auth-and-authorization", "backend-design:security-discipline", "adr", "panel-ui", "desplegar-test-agent-core", "desplegar-test"]
estado: terminada
---

# HU-CAL-07 · Conectar Google Calendar desde el panel nuevo

> Estado SDD: Terminada — implementada y verificada en test 2026-10-05 · issue [core #229](https://github.com/devrochy/agent-core/issues/229) · diseño en [design.md](../design.md#conexión-con-google-desde-el-panel-hu-cal-07) (D-SPEC-24-11 y 12).

**ID:** HU-CAL-07

**Título:** Conectar Google Calendar desde el panel nuevo

**Workstream:** Agenda

**Historia:** Como dueño de un negocio quiero conectar mi cuenta de Google Calendar con un clic desde Calendario en el panel, de forma segura y sin errores, para que el asistente agende directamente en mi calendario de Google cuando prefiero ese modo.

**Por qué importa (valor empresarial):** El modo Google es el que piden los negocios que ya viven en Google Calendar; hoy no se puede conectar desde el panel nuevo. En test (2026-10-05) el botón "Conectar con Google" terminó en `redirect_uri_mismatch` y, al registrar la URI que manda la app, en un 404: la app arma una ruta que no existe (`packages/pack-calendar/pack_calendar/oauth.py:50-52` vs. el prefijo `/api/v1/pack/calendar` de `admin_api.py`), el túnel manda todo `/api/v1/*` al panel (`docs/despliegue-coolify.md:52-55`), el callback de la API no sabe a qué negocio guardar los tokens (no tiene sesión) y el flujo no usa `state` (CSRF de OAuth). Cambiar el calendario a modo Google sin conexión además oculta todas las tools del calendario y el asistente escala (ADR-0072).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-CAL-03

**Dependencias:** [HU-CAL-02](HU-CAL-02-agendar-reagendar-cancelar.md)

**Criterios de aceptación (Gherkin):**
- **Conectar.** Dado un negocio con las credenciales OAuth de Google configuradas y la URI del entorno registrada en Google Cloud Console, cuando el dueño pulsa "Conectar con Google" en Calendario y autoriza, entonces vuelve a `/calendario?google=ok` y queda una conexión `google_calendar` activa con el email de la cuenta.
- **URI de retorno.** Dado el entorno de test, cuando se inicia la conexión, entonces Google recibe `redirect_uri=https://test.solvershub.site/api/calendar/oauth/callback` (`PANEL_BASE_URL`, o `PUBLIC_BASE_URL` si no está) y el intercambio del código usa exactamente la misma URI.
- **Protección CSRF.** Dado un retorno de Google con un `state` distinto al de la cookie `oauth_state`, o sin esa cookie, cuando llega al callback, entonces no se intercambia el código ni se guarda nada y el panel muestra `google=error`.
- **Sin sesión.** Dado un retorno de Google en un navegador sin sesión del panel, cuando llega al callback, entonces redirige al login y no procesa el código.
- **Cancelar.** Dado que el dueño cancela en la pantalla de Google, cuando vuelve al panel, entonces ve `google=cancelado` y no cambia ninguna conexión.
- **Aislamiento.** Dado un colaborador con acceso a dos negocios, cuando conecta Google con el negocio A seleccionado, entonces la conexión y los tokens quedan solo en A.

**Evidencia / Definición de Terminado:**
- ADR-0093 (la URL del callback pasa al panel; supersede la parte de ADR-0070 que la fijaba en `/admin/plugins/…`).
- Backend: `redirect_uri` del panel; `state` en `/oauth/start` (cookie `oauth_state` httponly) y validado en `/oauth/callback`, que exige principal (`pack_calendar:conexion`, escritura) y borra las cookies OAuth al terminar; OpenAPI regenerado.
- Panel: ruta BFF `GET /api/calendar/oauth/callback` que reenvía la petición con la sesión y el negocio y propaga el 302 y las cookies.
- Tests: unitarios del armado de la URI y del `state`; integración del callback (sin `state` → error, `state` correcto → intercambio con el `code` simulado y conexión guardada en el negocio del principal, cross-tenant).
- URI registrada en Google Cloud Console por el usuario; conexión real hecha en test con su cuenta; `CALENDAR.md` y CHANGELOG al día.

**Implementada (2026-10-05):** backend [core #230](https://github.com/devrochy/agent-core/pull/230) — `panel_redirect_uri()` (`<PANEL>/api/calendar/oauth/callback`), `state` anti-CSRF en `/oauth/start` (cookie httponly `oauth_state`), `/oauth/callback` con principal (`pack_calendar:conexion`) que valida el `state` con `compare_digest`, guarda los tokens en la conexión del negocio del principal y borra las cookies; ADR-0093 (supersede la URL del callback de ADR-0070); `CALENDAR.md`, OpenAPI y CHANGELOG. Panel [#25](https://github.com/devrochy/solvershub-panel/pull/25) — ruta BFF `GET /api/calendar/oauth/callback`. Documentación [docs #25](https://github.com/devrochy/solvershub-docs/pull/25).

**Fixes encontrados al verificar en test:** (1) las redirecciones de respaldo del OAuth en el panel iban a la dirección interna del contenedor (`https://0.0.0.0:3000/login`), porque Next arma `request.url` con su host interno → `publicUrl()` con los encabezados del proxy; (2) `next` del inicio aceptaba `//otro-dominio` (redirección abierta) → solo rutas relativas; (3) el primer intento real falló con `calendar_oauth_state_invalido`: el `<Link>` de "Conectar con Google" hacía **prefetch** del inicio del OAuth (4 llamadas a `/oauth/start` por carga de Calendario), cada una renovaba el `state` y pisaba la cookie → el botón pasó a `<a>`. Los tres en panel [#26](https://github.com/devrochy/solvershub-panel/pull/26).

**Verificado en test (2026-10-05):** con el panel `11101d9` y la URI `https://test.solvershub.site/api/calendar/oauth/callback` registrada en Google Cloud Console, el dueño conectó su cuenta: una sola llamada a `/oauth/start`, intercambio del código (200) y `userinfo` (200), callback sin errores; quedó la conexión `google_calendar` activa con `devrochy@gmail.com` (`active_connection_type_ids` = `email_smtp`, `google_calendar`, `whatsapp_waweb`) y el calendario sigue en `source = interno`. Tests: 807 unit + 9 integración de OAuth (start con `state`, callback sin auth → 401, `state` inválido o sin cookie → error sin intercambio, cancelado, conexión solo en su negocio) en verde; suite de integración 310 passed (2 fallas ajenas, las mismas de `develop`).

**Riesgos/Notas:**
- Cada negocio que use sus propias credenciales de Google debe registrar la URI de su entorno en su consola (se documenta en `CALENDAR.md` y en la pantalla de Conexión).
- Las conexiones hechas antes con el flujo clásico siguen sirviendo: no cambia dónde se guardan los tokens (ADR-0070).
- Mientras no haya conexión, el calendario debe quedar en modo `interno`: en modo `google` sin conexión el asistente no tiene tools de agenda.
