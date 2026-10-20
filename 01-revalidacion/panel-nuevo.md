# Panel nuevo (`solvershub-panel/apps/panel-web`)

Fuente: inventario del 2026-09-30 y revisión UX/UI contra el panel de `agent-sale`
(`agent-sale/src/admin/adminPanel.ts`) del 2026-10-01. Rutas relativas a `apps/panel-web/` salvo
que se indique otra cosa.

## Lo que está bien

- **48 páginas, 36 handlers BFF** sobre `/api/v1` (149 rutas en `openapi.json`: 86 admin, 2 auth,
  61 pack). El panel SSR se retiró: 147 de 148 rutas migradas (`solvershub-comercial/PARIDAD-PANEL.md`).
- **Sesión segura**: el BFF guarda un token opaco y revocable en la cookie `httpOnly` `panel_session`
  (`app/api/session/route.ts:16,36-43`) y agrega `Authorization` y `X-Tenant-Id` en cada llamada
  (`lib/api/server.ts:30-46`).
- `DESIGN.md`, tema oscuro sin parpadeo, foco visible global (`app/globals.css:72-76`), respeto de
  `prefers-reduced-motion`, 80 `aria-label`.
- Iconos por canal, Costos de Meta y salud con tres estados.
- Campaña de pruebas manual: 116/122 casos OK y 0 defectos altos
  (`solvershub-comercial/REPORTE-DE-PRUEBAS-2026-09-28.md`).

## Lo que está mal

| Problema | Evidencia |
|---|---|
| **No hay panel en producción** | Coolify de producción solo tiene recursos del backend (`solvershub-backend/docs/despliegue-coolify.md:16-24`) |
| 2 archivos de test (12 casos) para ~16 mil líneas, y **el CI no los corre** | `vitest.config.mts:9-10`; `solvershub-panel/.github/workflows/ci.yml:52-72` |
| Las páginas de cada pack están escritas a mano: un pack nuevo exige desplegar el panel | `components/shell/nav.ts:54-175`; el backend ya tiene `admin_menu` y `ViewDescriptor` (`solvershub-backend/core/admin/view_registry.py:20-75`) sin exponer |
| Las tools declarativas solo viven en `/legacy` | `configuracion/_components/advanced-panel.tsx:122-127` |
| Sin onboarding ni tour | Solo el checklist de Meta (`components/domain/checklist-meta.tsx`) |
| Escalaciones de solo lectura | La API solo tiene `GET /admin/escalations` (`solvershub-backend/core/api/routers/escalations.py:31`) |
| **Embedded Signup no está implementado** | El botón solo crea la sesión y pide cargar el SDK a mano (`conexiones/whatsapp/_components/whatsapp-wizard.tsx:74-88`) |

## Bugs visibles (van al Hito 0A en [HU-UI-01](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-01-bugs-visibles.md))

| Bug | Evidencia | Efecto |
|---|---|---|
| **Guardar la config de una habilidad escribe en el negocio equivocado** | `app/api/plugins/[pluginId]/route.ts:37-41` hace un fetch sin `X-Tenant-Id`; el backend cae al primer negocio del admin (`solvershub-backend/core/api/deps.py:84-88`) | Un usuario con varios negocios (master, agencia) guarda la config en otro |
| Precios de comercio en USD | `comercio/page.tsx:46`, `productos/page.tsx:64,75`, `pedidos/page.tsx:61,67` usan `formatUsd`; el pack usa COP | "US$ 150.000" |
| El formulario de schema pierde el error del backend y envía números como texto | `components/domain/json-schema-form.tsx:84-87,178` | Solo se ve un error genérico |
| Acciones irreversibles sin confirmación | Eliminar conexión (`conexiones/_components/connection-actions.tsx:111-118`), desactivar colaborador, resolver conversación, cancelar cita (`calendario/_components/cancel-appointment.tsx:19-24`, que además no revisa `res.ok`) | Pérdida de datos o fallas silenciosas |
| Switches optimistas sin rollback | `conversation-actions.tsx:49-52`, `habilidades/_components/plugin-actions.tsx:46,55` | La UI muestra un estado que el servidor rechazó |
| Botón destructivo en verde | `cobranza/carteras/_components/portfolio-dialog.tsx:184`, `cobranza/clientes/_components/client-dialog.tsx:205` | El color comunica lo contrario |
| Menú desalineado con el backend | Faltan Clientes y Gestores de cobranza y "Horarios y calendario" (`components/shell/nav.ts:84-126`) | `/cobranza/clientes` solo se alcanza desde el detalle de una cartera |
| Datos de la API que el panel nunca muestra | `alert_metric`, `warning_metric`, `remaining`, `brand_voice_warning`, `MessageItem.status` | Avisos de cuota y estado de entrega invisibles |

## Problemas transversales

| Área | Hoy | Brecha |
|---|---|---|
| Shell | Sidebar fijo `w-60` sin breakpoints (`components/shell/sidebar.tsx:132`) | Inutilizable en el celular |
| Carga y errores | Sin `loading.tsx`, `error.tsx` ni `not-found.tsx`; el 404 sale en inglés | `DESIGN.md:68` pide esqueletos |
| Feedback | 53 estados locales de carga/error/éxito, 9 confirmaciones caseras y un `window.confirm` | Sin toasts ni diálogo de confirmación compartido |
| Tablas | `DataTable` suma búsqueda y paginación del lado del cliente sobre la paginación del servidor (`components/ui/data-table.tsx:48`) | Dos buscadores y dos paginadores en Conversaciones, Leads y Escalaciones |
| Colores y degradado | `IconAction` y `ChannelIcon` con pasteles fijos y `hover:scale-105`; 47 botones con degradado | Rompe `DESIGN.md:49,52,53,59` |
| Jerga | "Fernet", ".env", WABA, BYOK y rutas de API a la vista | Lenguaje claro y glosario |

## Vista por vista (resumen)

| Vista | Qué falta frente a `agent-sale` |
|---|---|
| Dashboard | Selector de período, tendencias, gráfico, % resuelto sin humano, KPIs con enlace, aviso de cuota, primeros pasos |
| Conversaciones | Bandeja de dos paneles con vista previa, pestañas con contadores, orden por última actividad, ventana de 24 h, composer abajo |
| Escalaciones | Tomar / resolver / devolver al asistente, asignado, "esperando hace X" |
| Colaboradores | Grilla de permisos legible (las etiquetas ya existen en `solvershub-backend/core/admin/permissions.py:30-69`), selector de negocio, invitaciones enviadas |
| Leads | Filtros, CSV, detalle, enlace a la conversación |
| Configuración | Pestañas con estado y en la URL, tarjetas de opción, horario en grilla, selector de modelo, aviso de cambios sin guardar |
| Costos y Plan | Gráfico y período, enlaces a conversaciones, pestañas IA/WhatsApp, límites legibles |
| Cobranza | 11 botones que repiten el menú (`cobranza/page.tsx:63-99`); el detalle de cartera apila 7 KPIs y 8 secciones |
| Calendario | Tabla de citas duplicada (`calendario/page.tsx:99-101` y `calendario/citas/page.tsx:56`) y dos componentes de cancelar |
| Conexiones | Ver [conexiones-y-costos-meta.md](conexiones-y-costos-meta.md) |

## Páginas de packs dirigidas por descriptores (camino propuesto)

| Paso | Backend | Panel |
|---|---|---|
| 1. Manifiesto de menú | `GET /api/v1/admin/ui/manifest` filtrado por permisos y packs | Sidebar desde el manifiesto |
| 2. Descriptores enriquecidos | Tipos de celda, filtros, acciones por fila, KPIs, estado vacío | — |
| 3. API de vistas | `GET /api/v1/pack/{id}/views/{vista}` + acciones | `<DescriptorView>` genérico |
| 4. Formulario de schema v2 | — | `anyOf` nulos, enums etiquetados, arreglos, `x-widget` |
| 5. Salida de emergencia | `kind: "custom"` | Las pantallas complejas siguen a mano |

Pantallas que ya encajan: alertas, auditoría, dispositivos, pagos, promesas, reportes y monitoreo de
cobranza; categorías, pedidos y resumen de comercio; tipos y citas de calendario. Va a
[SPEC-16](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/spec.md).

## Top 15 de mejoras (ordenadas por impacto)

| # | Vista | Cambio | Tamaño | HU |
|---|---|---|---|---|
| 1 | Transversal | Lote de bugs visibles | S | [HU-UI-01](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-01-bugs-visibles.md) |
| 2 | Escalaciones | Tickets reales | M | [HU-UI-05](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-05-tickets-reales.md) |
| 3 | Conversaciones | Bandeja de dos paneles | L | [HU-UI-06](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-06-bandeja-dos-paneles.md) |
| 4 | Shell | Menú móvil, carga, error, 404, skip link, estado del asistente | M | [HU-UI-03](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md) |
| 5 | Transversal | Kit de feedback: toasts, `useConfirm`, `useAction` | M | [HU-UI-02](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) |
| 6 | Transversal | `lib/labels.ts` y cumplimiento de `DESIGN.md` | S | [HU-UI-02](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) |
| 7 | Dashboard y Costos | Período, tendencias, gráfico, primeros pasos | M | [HU-UI-07](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) |
| 8 | Listas | `FilterBar` único y densidad documentada | M | [HU-UI-08](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md) |
| 9 | Configuración | Pestañas con estado, tarjetas, horario en grilla | M | [HU-UI-09](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-09-configuracion-por-pestanas.md) |
| 10 | Colaboradores | Grilla de permisos e invitaciones | M | [HU-UI-10](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-10-colaboradores-y-permisos.md) |
| 11 | Cuenta | Perfil, recuperación de contraseña, notificaciones | L | [HU-UI-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-13-cuenta-y-notificaciones.md) |
| 12 | Leads | Filtros, CSV, detalle | M | [HU-UI-11](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-11-clientes-y-leads.md) |
| 13 | Packs, Costos, Plan | Sub-navegación y pestañas | M | [HU-UI-12](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-12-packs-costos-y-plan-compactos.md) |
| 14 | Plataforma de packs | Manifiesto, descriptores, `<DescriptorView>` | L | [SPEC-16](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/spec.md) |
| 15 | Calidad | Tests en CI, deriva de tipos, Playwright y axe | M | [HU-UI-04](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md) |

Los puntos 3 y 8 necesitan antes dos excepciones escritas en `DESIGN.md`: tablas más densas
(`DESIGN.md:13`) y bandeja a todo el ancho (`DESIGN.md:34`).
