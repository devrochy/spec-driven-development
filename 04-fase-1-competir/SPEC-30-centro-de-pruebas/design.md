# SPEC-30 · Diseño

> Aprobado el 2026-10-13 con las decisiones D-SPEC-30-1 a 5 de [spec.md](spec.md) (D-33).

## Componentes y flujo

```
solvershub-docs/11-pruebas/catalogo.yaml ──(importar, HU-QA-02)──▶ agent-core: qa_catalog_versions + qa_items
                                                                        │
panel: Plataforma › Pruebas (HU-QA-03) ──BFF /api/qa/*──▶ API /api/v1/admin/qa/* (HU-QA-01)
   │  lista lateral · ejecución paso a paso · progreso · informe            │
   │  ciclos · configurar test · paso a producción · testers               ▼
   └── rol tester (HU-QA-04): master + dueño en Colaboradores, solo test   qa_cycles · qa_runs · qa_step_results
                                                                    qa_item_results · qa_attachments · qa_events
                                                    capturas: TENANTS_ROOT/.plataforma/pruebas/<run_id>/
```

## Datos (tablas, migraciones, RLS)

Tablas de sistema de la plataforma (sin `tenant_id`, como `admins`): no pertenecen a ningún negocio y solo las usan
master y el rol tester. La migración lo documenta con «Tabla de SISTEMA (sin RLS)» y el ADR del centro de pruebas.

| Tabla | Columnas principales | Notas |
|---|---|---|
| `qa_catalog_versions` | `id`, `version`, `commit_docs`, `importado_en`, `importado_por` | Una fila por importación del YAML |
| `qa_items` | `catalog_version_id`, `slug`, `seccion` (`pruebas`, `test`, `prod`), `modulo`, `grupo`, `titulo`, `resumen`, `contexto`, `prioridad`, `plataforma`, `precondiciones`, `datos`, `pasos` (jsonb `[{accion, esperado}]`), `esperado`, `porque`, `como`, `vars` (text[]), `quien`, `hu` (text[]), `origen` (text[]), `orden` | El `slug` es estable entre versiones para seguir la historia de una prueba |
| `qa_cycles` | `id`, `nombre`, `catalog_version_id`, `abierto_en`, `cerrado_en`, `cerrado_por`, `resumen` (jsonb) | Índice parcial único: un solo ciclo abierto |
| `qa_runs` | `id`, `cycle_id`, `admin_id`, `estado` (`en_curso`, `enviada`), `iniciada_en`, `enviada_en`, `informe` (jsonb), `comentario` | Única por (`cycle_id`, `admin_id`): una ejecución por tester y ciclo |
| `qa_step_results` | `run_id`, `item_slug`, `paso`, `estado` (`ok`, `falla`, `bloqueado`, `omitido`), `nota`, `actualizado_en` | PK (`run_id`, `item_slug`, `paso`) |
| `qa_item_results` | `run_id`, `item_slug`, `estado` (`sin_correr`, `en_curso`, `ok`, `falla`, `bloqueada`), `nota`, `actualizado_en` | Derivado de los pasos (falla > bloqueado > en curso > ok) más una nota general |
| `qa_attachments` | `id`, `run_id`, `item_slug`, `paso`, `ruta`, `nombre_original`, `mimetype`, `tamano`, `subido_por`, `subido_en` | El archivo físico se llama `uuid4` |
| `qa_config_status` | `item_slug`, `estado` (`pendiente`, `en_curso`, `listo`, `no_aplica`), `nota`, `actualizado_en`, `actualizado_por` | Config de test y puntos de prod: no se reinician por ciclo |
| `qa_events` | `id`, `cycle_id`, `run_id`, `item_slug`, `paso`, `campo`, `antes`, `despues`, `admin_id`, `en` | Historial; nunca se borra |
| `qa_tester_invitations` | `id`, `email`, `admin_id`, `token_nonce`, `estado` (`pendiente`, `aceptada`, `revocada`, `vencida`), `expires_at`, `invitado_por`, `creada_en` | Enlace de un solo uso para testers ([HU-QA-04](hu/HU-QA-04-rol-tester-e-invitaciones.md)) |

**Consolidación por ciclo** (lo que ve el dueño en la lista): `falla` si algún tester la falló, si no `bloqueada`, si
no `ok`, si no `sin_correr`.

## API (`/api/v1/admin/qa`, sección RBAC `qa`, global)

| Método y ruta | Qué hace | Permiso |
|---|---|---|
| `GET /catalog?seccion=` | Catálogo vigente con el estado consolidado del ciclo abierto | `qa` lectura |
| `GET /runs/me`, `POST /runs/me/start` | Mi ejecución del ciclo abierto (la crea si no existe) con mis pasos, notas, capturas y progreso | `qa` escritura |
| `PUT /runs/me/items/{slug}/steps/{n}` | Estado y nota de un paso; recalcula el estado de la prueba y registra el evento | `qa` escritura |
| `PUT /runs/me/items/{slug}` | Nota general de la prueba | `qa` escritura |
| `POST /runs/me/attachments`, `DELETE /attachments/{id}` | Sube (multipart) o quita una captura de un paso de mi ejecución en curso | `qa` escritura |
| `GET /attachments/{id}` | Sirve la captura con sesión | `qa` lectura |
| `POST /runs/me/submit` | Congela mi ejecución, guarda el informe y avisa por correo a los masters | `qa` escritura |
| `GET /runs`, `GET /runs/{id}`, `GET /runs/{id}/report.md` | Informes (el tester ve los suyos, master todos) y su descarga en Markdown | `qa` lectura |
| `GET /items/{slug}/history` | Historial de la prueba en el ciclo | `qa` lectura |
| `GET /cycles`, `POST /cycles/close` | Lista ciclos; cierra el abierto (foto en `resumen`) y abre uno nuevo | `qa` escritura |
| `PUT /config/{slug}` | Estado y nota de un ítem de configuración de test o de producción | `qa` escritura |
| `POST /catalog/import` | Importa el YAML del catálogo | master |
| `GET/POST /testers`, `POST /testers/{id}/revoke`, `POST /testers/{id}/resend` | Gestión de testers | master |
| `POST /api/v1/auth/accept-tester-invitation` | Canjea el enlace: define la contraseña, activa la cuenta y abre la sesión | público con token |

## Rol tester ([HU-QA-04](hu/HU-QA-04-rol-tester-e-invitaciones.md))

- `admins.role = 'tester'`. `actua_como_master(admin)` es verdadero para master y para tester **si**
  `QA_TESTERS_ENABLED=true`; reemplaza los chequeos de operación (`effective_access`, `require`, middleware,
  plataforma, Meta, búsqueda, sync, onboarding, app de campo).
- La sección `collaborators` se entrega al tester (habilitada el 2026-10-13 a pedido del dueño). Como los servicios
  de cuentas siguen preguntando `role == 'master'`, el tester va por el camino del owner: gestiona las cuentas
  exclusivas del negocio activo. Gestionar cuentas de plataforma (crear masters, tocar cuentas de master o tester,
  vincular entre negocios, gestionar testers) sigue siendo solo de master.
- Un owner trata a un tester como a un master: no lo puede invitar, vincular, cambiarle la contraseña ni desactivarlo.
- Sin la variable (producción), `login` y la validación de sesión rechazan al tester y no se pueden crear testers.
- Revocar desactiva la cuenta y borra sus sesiones: el siguiente pedido ya falla.

## Panel

- **Plataforma › Pruebas** (sección `qa`), con pestañas Ejecutar · Informes · Ciclos · Configurar test · Paso a
  producción · Testers (esta última solo master).
- **Ejecutar**, dos columnas a partir de 1024 px:

```
┌ Ciclo 2026-10 · SPEC-29 ─ Mi avance ▓▓▓▓░░░░ 42/310 · ✔38 ✖3 ⏸1 ─ Ciclo 61 % ─ [Enviar informe] ┐
├───────────────────────────┬──────────────────────────────────────────────────────────────────┤
│ 🔍 Buscar  [Estado▾][Módulo▾][P0]│  Ir a una sección con Ctrl+K            HU-DS-05 · Panel · P0     │
│ ▾ Panel · navegación   4/6 │  Contexto · Precondiciones · Datos de prueba                    │
│   ✔ Abrir la paleta        │  ① Pulsar Ctrl+K ………………………… ✔                                   │
│ ▸ ● Ir a una sección       │  ② Escribir «prom»   Esperado: aparece Promesas                 │
│   ○ Atajos g+letra         │     [Aprobar A] [Falla F] [Bloqueado B] [Omitir]                │
│ ▸ App de campo       3/10  │     Nota ……  📎 Pegar o arrastrar capturas                      │
│ ▸ Cobros             0/14  │  ③ Enter                                                       │
│                            │  [Pasos | Registro]                     ← Anterior  Siguiente → │
└───────────────────────────┴──────────────────────────────────────────────────────────────────┘
```

  - La lista es una navegación de botones con teclado (↑↓, J/K). En el celular se abre como `Sheet` y la ejecución ocupa la
    pantalla.
  - Cada acción guarda al instante (PUT) y muestra «Guardado»; si falla la red, reintenta y avisa.
  - Al aprobar un paso pasa solo al siguiente; al terminar la prueba ofrece la siguiente sin correr.
- **Enviar informe:** vista previa (resumen, fallas y bloqueos con notas y capturas, lo que quedó sin correr), luego
  confirmación. El informe tiene hoja de impresión (PDF desde el navegador) y descarga en Markdown.
- **Kit:** `Progress` (lineal y segmentada), `Stepper` (sale del `Paso` de «Pasar a producción») y `Dropzone` (pegar
  y arrastrar imágenes) se suman a `components/ui` y al catálogo `/catalogo`.
- El menú, la paleta y las migas se arman desde `nav.ts` filtrado por permisos: el panel no tiene lógica de rol;
  muestra a cada uno lo que el backend le entrega en `/me`.

## Migración desde el artifact ([HU-QA-05](hu/HU-QA-05-migrar-desde-el-artifact.md))

El artifact guarda `items`, `usuarios`, `historial`, `ciclos` y `meta/ciclo` en su base. Claude los lee con la
herramienta de datos del artifact, los convierte al formato de la API y los carga. Después el artifact queda en solo
lectura con un enlace al panel.
