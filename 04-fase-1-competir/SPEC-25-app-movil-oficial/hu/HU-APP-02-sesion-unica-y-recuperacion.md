---
id: HU-APP-02
titulo: Sesión única, recuperación de contraseña y biometría
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [confianza, operacion]
req: [REQ-APP-02]
dependencias: [HU-APP-01]
skills: [backend-design:auth-and-authorization, backend-design:security-discipline, frontend-design]
estado: terminada
---

# HU-APP-02 · Sesión única, recuperación de contraseña y biometría

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-02

**Título:** Sesión única, recuperación de contraseña y biometría

**Workstream:** App móvil

**Historia:** Como dueño, colaborador o gestor quiero entrar a la app con un solo login (que me lleve al panel o al campo según mi rol), recuperar mi contraseña sin soporte humano y desbloquear con biometría, para que la app oficial tenga una puerta de entrada única, segura y sin fricción.

**Por qué importa (valor empresarial):** La app oficial atiende dos identidades (admin del panel y gestor de campo) y hoy ninguna tiene recuperación de contraseña móvil ni biometría. Una puerta única con recuperación self-service y desbloqueo biométrico reduce soporte y eleva la seguridad percibida, requisito para presentar la app como producto.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-02

**Dependencias:** [HU-APP-01](HU-APP-01-nucleo-modular-de-la-app.md)

**Criterios de aceptación (Gherkin):**
- **Login único.** Dado un usuario con rol admin o gestor, cuando inicia sesión con usuario y contraseña, entonces entra al shell que corresponde a su rol (panel o campo) con los permisos del backend.
- **Modo campo.** Dado un admin con rol de pack gestor y dispositivo vinculado, cuando entra al modo campo, entonces la app obtiene el JWT de gestor vía `POST /api/v1/pack/cobranza/gestor-token` y opera la API de campo.
- **Recuperación.** Dado un usuario que olvidó su contraseña, cuando pide recuperarla con su correo y escribe el token recibido y una contraseña nueva, entonces puede iniciar sesión y sus sesiones anteriores quedan invalidadas.
- **Biometría.** Dado un usuario con biometría activada, cuando abre la app estando logueado, entonces puede desbloquear con huella/rostro y sin biometría no accede a los datos.
- **Logout.** Dado un usuario logueado, cuando cierra sesión, entonces se revoca la sesión admin, se descartan ambos tokens y la app vuelve al login sin datos sensibles en pantalla.

**Evidencia / Definición de Terminado:**
- Backend: `POST /api/v1/auth/forgot-password` y `POST /api/v1/auth/reset-password` (token por correo, bcrypt, invalidación de sesiones) y `POST /api/v1/pack/cobranza/gestor-token` con RBAC, RLS y validación de dispositivo; tests cross-tenant e idempotencia; `docs/openapi.json` regenerado.
- App: pantallas de login, recuperación y biometría (`expo-local-authentication`, opt-in), doble credencial en `expo-secure-store`, logout que limpia todo; tests de flujo con MSW.
- Evidencia en test: recuperación completa de punta a punta y login admin→gestor con `npm run check` en verde.

**Implementada (2026-10-06):** [agent-core #240](https://github.com/devrochy/agent-core/pull/240) + **Implementada (2026-10-06):** [solvershub-apk #108](https://github.com/devrochy/solvershub-apk/pull/108) — login unificado, recuperación por SMTP y biometría (ADR-0094/0098).

**Riesgos/Notas:**
- El correo de recuperación reutiliza el canal SMTP existente (ADR-0071); la respuesta de `forgot-password` no debe filtrar si la cuenta existe.
- La vinculación de dispositivo del gestor (ADR-0068) sigue siendo prerrequisito del modo campo; su autovinculación pendiente es de [HU-APP-07](HU-APP-07-cobranza-al-nucleo-sin-regresion.md).

**Backend implementado (2026-10-05):** [agent-core #240](https://github.com/devrochy/agent-core/pull/240) — `POST /api/v1/auth/forgot-password` y `/reset-password` (código de un solo uso por correo de sistema `SYSTEM_SMTP_*`, tabla de SISTEMA `password_reset_tokens` 0051, revocación total de sesiones) y `POST /api/v1/pack/cobranza/gestor-token` (sesión admin → par de tokens de campo reusando ADR-0081/0068). ADR-0094. 9 tests de integración nuevos en verde; falta la parte de la app (pantallas + biometría + doble credencial).

**App implementada (2026-10-05):** [solvershub-apk #108](https://github.com/devrochy/solvershub-apk/pull/108) — módulo `src/modules/auth/` (cliente admin `/api/v1`, `AdminSessionProvider` en SecureStore, login unificado con exchange, pantallas de recuperación, biometría opt-in con `expo-local-authentication`, puerta biométrica) y convergencia en `App.tsx` sin regresión (el exchange aplica los tokens de campo con `aplicarSesionExterna`; 0/varios negocios delegan al flujo legado ADR-0081). 517/517 tests (19 nuevos). Deuda: selector admin multi-negocio y PanelShell llegan con [HU-APP-03](HU-APP-03-navegacion-por-permisos.md).
