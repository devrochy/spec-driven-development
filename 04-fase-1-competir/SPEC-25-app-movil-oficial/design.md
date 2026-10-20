# SPEC-25 · Diseño

## Estructura objetivo de la app (ADR-APP-01)

```
solvershub-apk/
├── src/
│   ├── app/            # bootstrap, providers, DI de servicios
│   ├── core/           # config, ApiClient admin+gestor, sesión, query client, i18n, theme
│   ├── shared/         # ui-kit (del DS existente), hooks, utils, formatters
│   ├── data/           # db (expo-sqlite + SQLCipher), repos, sync-engine, auditoría local
│   ├── modules/
│   │   ├── auth/           # login, recuperación, invitaciones, dispositivo, biometría
│   │   ├── dashboard/
│   │   ├── operacion/      # conversaciones, escalaciones, leads
│   │   ├── cobranza/       # campo (migrado) + admin (resumen, carteras, clientes, promesas, …)
│   │   ├── comercio/       # productos, categorías, promociones, pedidos
│   │   ├── calendario/     # citas, tipos, bloqueos, horario
│   │   ├── negocio/        # plan y consumo, costos
│   │   ├── configuracion/  # colaboradores, habilidades, conexiones, ajustes
│   │   ├── herramientas/   # asistente, plantillas, DLQ
│   │   ├── plataforma/     # negocios (solo master)
│   │   ├── notificaciones/ # bandeja + registro push
│   │   ├── busqueda/
│   │   └── auditoria/
│   └── navigation/     # AppNavigator + linking + shell por rol
├── scripts/check-module-boundaries.mjs
└── docs/adr/ADR-APP-01..06
```

Cada módulo exporta: `navigation.tsx`, `screens/`, `features/`, `api.ts`, `repository.ts`,
`__tests__/`. Reglas de frontera (verificadas en CI): un módulo solo importa `core/`, `shared/`,
`data/` y sus propios archivos; el shell (`navigation/`) es el único que importa de varios módulos.

## Superficies de API que consume la app

| Superficie | Credencial | Módulos |
|---|---|---|
| `/api/v1` + `/api/v1/pack/*` (admin, OpenAPI) | Token opaco de sesión + `X-Tenant-Id` | dashboard, operacion, negocio, comercio, calendario, configuracion, herramientas, plataforma, cobranza-admin, busqueda, sync |
| `/api/pack/pack_cobranza` (campo, v2 camelCase) | JWT gestor (access+refresh) | cobranza-campo |

Endpoints nuevos de backend (historia [HU-APP-02](hu/HU-APP-02-sesion-unica-y-recuperacion.md), [HU-APP-05](hu/HU-APP-05-notificaciones-push.md), [HU-APP-14](hu/HU-APP-14-busqueda-global.md), [HU-APP-15](hu/HU-APP-15-sync-offline-por-modulos.md)):

- `POST /api/v1/auth/forgot-password` y `POST /api/v1/auth/reset-password` (token por correo,
  bcrypt, invalida sesiones).
- `POST /api/v1/pack/cobranza/gestor-token` (sesión admin → JWT de gestor; valida rol de pack, carteras y
  dispositivo vinculado).
- `POST/DELETE /api/v1/me/push-token` (token Expo por dispositivo) y envío vía Expo Push Service
  en Celery para eventos (pago/abono/gasto del campo, escalación, cita, promesa incumplida, mora).
- `GET /api/v1/search?q=` (resultados unificados por sección, filtrados por RBAC y tenant).
- `GET /api/v1/sync/{entidad}?cursor=&limit=` → `{items, nextCursor, deletedIds}` para clientes,
  productos, categorías, promociones, pedidos, citas, tipos de cita, bloqueos, conversaciones,
  promesas y carteras.
- `POST /api/v1/audit/mobile-events` (auditoría idempotente por `event_id` + dispositivo).

Migraciones nuevas del backend: `push_tokens`, `password_reset_tokens` (tablas con `tenant_id` +
RLS forzada + policy + `deleted_at`, invariantes de `CLAUDE.md`), y extensión aditiva de auditoría.

## Almacenamiento local (ADR-APP-05)

Tablas: `cache_entidad(modulo, entidad, id, json, updated_at, cursor)`,
`cola_evento(id, modulo, tipo, payload, estado, intentos, creado_at)`,
`auditoria_local(id, accion, entidad, entidad_id, payload, user, device, ts, synced)`,
`sync_cursor(modulo, entidad, cursor)`. Clave maestra generada en primer uso en SecureStore con
`requireAuthentication`; `PRAGMA key` al abrir cada conexión. Migración única desde AsyncStorage
(claves `cobranza_*`) con verificación de filas y borrado del origen tras confirmar.

## Navegación y permisos (ADR-APP-02, ADR-APP-03)

- `AuthStack`: login → (recuperar | invitaciones | vinculación | selección de negocio).
- `FieldShell` (gestor): tabs Diario · Carteras · Clientes · Notificaciones · Perfil, filtrado por
  los 14 permisos finos de gestor.
- `PanelShell` (dueño/colaborador): tabs Inicio · Operación · Cobranza · Comercio · Calendario +
  drawer "Más" (Negocio, Configuración, Herramientas, Plataforma, Búsqueda, Auditoría), filtrado por
  `MeResponse.permissions` (mismas claves de sección que el sidebar del panel) y gating por pack
  (ADR-0019). Plataforma solo si `is_platform_master`.
- Deep links `solvershub://…` (notificación → pantalla de destino; link de pago → cobro QR).

## Migración, despliegue y reversa

1. **F0 (docs)**: ADR-APP-01..06 + esta spec. Sin código.
2. **[HU-APP-01](hu/HU-APP-01-nucleo-modular-de-la-app.md)**: reestructura física con tests verdes (movimiento mecánico). Reversible por git.
3. **[HU-APP-02](hu/HU-APP-02-sesion-unica-y-recuperacion.md)/05/14/15**: endpoints nuevos del backend en agent-core, tras la API existente
   (ninguna ruta actual cambia). Despliegue a test con `desplegar-test-agent-core`.
4. **[HU-APP-02](hu/HU-APP-02-sesion-unica-y-recuperacion.md)..06 (app)**: cada HU cierra con `npm run check` en verde y dev client funcionando;
   el APK de campo no se publica a producción hasta [HU-APP-07](hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md) + [HU-APP-17](hu/HU-APP-17-release-firmado-y-guias.md).
5. **[HU-APP-06](hu/HU-APP-06-almacenamiento-local-cifrado.md) (migración de datos)**: se publica con estrategia "leer AsyncStorage si SQLite no
   tiene la entidad" durante una versión, y una bandera `kill-switch` remota para volver al origen.
6. **Reversa de app**: EAS Update a canal anterior (OTA) o re-publicación del AAB anterior; la
   reversa de esquema del backend sigue el patrón de migraciones aditivas (nunca destructivas).

## Riesgos de la ampliación

- Pantallas gigantes de cobranza (`ClienteScreen`, `TrayectoDiarioScreen`) concentran lógica:
  [HU-APP-07](hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md) las descompone en hooks del módulo antes de agregar módulos nuevos.
- Dos motores de datos en una misma pantalla: prohibido por convención; se revisa en CI (lint).
- OAuth de Meta/Google desde la app usa browser/webview con el callback del panel; el checkout de
  plan usa webview hacia Wompi. Si un proveedor bloquea webview, se cae a navegador externo.
- Cifrado SQLCipher no aplica en Expo Go: el desarrollo de `data/` exige dev client (EAS development).
- Pinning mal configurado deja sin red a producción: doble pin + override por perfil + test en staging.

## Esfuerzo

17 HU · 10 M + 7 L ≈ 96,0 días-persona sin IA (secuencia y dependencias en `tasks.md`).
