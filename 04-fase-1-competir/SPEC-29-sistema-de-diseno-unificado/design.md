# SPEC-29 · Diseño

> Sigue el orden del encargo del 2026-10-10: fundamentos visuales → sistema de diseño → navegación
> → Resumen → app → stack → motion. El orden de ejecución está en [tasks.md](tasks.md). Se parte de
> lo que ya existe: `brand/manual-de-marca.md`, `brand/tokens/tokens.json` y
> `apps/panel-web/DESIGN.md`. Nada de esto se reemplaza: se extiende.

## Componentes y flujo

```
brand/tokens/tokens.json (DTCG, fuente única)
        │  build.mjs  (HU-DS-01 agrega tipografía, elevación, motion, estados por tema y datos)
        ├──► brand/tokens/dist/tokens.css ──► panel-web/app/tokens.css ──► @theme de Tailwind v4
        └──► brand/tokens/dist/theme.ts   ──► apk/src/core/theme/tokens.ts (npm run tokens:sync)
                                                     │
   panel-web                                         │  apk
   components/ui (átomos, moléculas)                 │  src/shared/ui (kit RN, HU-DS-09)
   components/dataviz (HU-DS-06)  ◄── misma geometría (d3-scale/d3-shape) ──►  src/shared/dataviz
   components/shell (sidebar, migas, Ctrl+K)         │  src/navigation (PanelShell v2, HU-DS-11)
   components/templates (ListPage, DashboardPage…)   │  modules/cobranza (mismas vistas, HU-DS-10)
   app/(app)/dashboard (Resumen por rol, HU-DS-07)   │  modules/dashboard (Resumen móvil por rol)
```

Los perfiles del Resumen (`lib/dashboard/perfiles.ts`) y el catálogo de widgets se definen igual en
los dos repos: mismas claves, mismos permisos requeridos y mismos endpoints. Como no hay paquete
compartido entre repos, la paridad la verifica un test en cada repo contra la tabla de esta spec.

---

## 1. 🎨 Fundamentos visuales

### Moodboard textual: "torre de control de un negocio pequeño"

- **Qué se siente:** un instrumento de cabina de noche: fondo navy profundo, lecturas en cyan que
  se encienden solo donde hay un dato y todo lo demás en silencio. Nada de luces de tragamonedas.
- **Materia:** superficies sólidas y opacas, como paneles de aluminio anodizado. Bordes finos en
  lugar de sombras pesadas. Sin vidrio ni desenfoque (D-SPEC-29-9).
- **Dónde se gasta la audacia:** solo en el **lenguaje de datos**. Las cifras grandes van en
  Montserrat con números tabulares, las tendencias en trazo cyan de 2 px y el delta en texto con
  flecha. El degradado aparece en un solo lugar: la CTA principal de cada pantalla (`gradient-cta`).
- **Referencias de tono, no de copia:** la sobriedad de Linear en el shell, la densidad de las
  tablas de Stripe y la lectura de un velocímetro en los KPIs.
- **Lo que se evita a propósito:** el kit de tarjetas SaaS (todo en tarjetas iguales con la misma
  sombra gris), los eyebrows en mayúsculas sobre cada título, los degradados de relleno y las
  animaciones de entrada escalonadas.

### Paleta (ya existe; esta spec agrega los roles que faltan)

| Rol | Claro | Oscuro (por defecto en producto, manual §5.5) | Uso |
|---|---|---|---|
| Fondo | `paper #F7F9FC` | `navy-900 #0B1733` | Lienzo |
| Superficie | `white #FFFFFF` | `navy-800 #11224D` | Tarjetas, tablas |
| Superficie elevada | `frost #F1F5FA` | `navy-750 #16294F` / `navy-700 #172F6C` | Popovers, ítem activo |
| Texto | `navy-900` (17,4:1) | `ice #E8EDF7` (14,9:1) | Cuerpo |
| Texto secundario | `slate-600 #5A6B85` (5,4:1) | `fog #A9B6CC` (7,5:1) | Ayudas |
| Enlace y foco | `blue-600 #2560E6` (5,4:1) | `cyan-400 #22C7E0` (7,6:1) | Enlaces, outline de foco |
| Marca | `navy-700 #172F6C` | `navy-700` | Header de la app |
| **CTA principal (nuevo)** | `gradient-cta`: `#172F6C → #2560E6`, texto blanco (≥ 5,4:1) | ídem | Una por pantalla. El gradiente de marca `#2F6BFF → #22C7E0` queda solo para acentos sin texto |
| **Estados (nuevo, texto)** | éxito `#17784F` (5,5:1) · aviso `#8A6100` (5,5:1) · peligro `#B42E2E` (6,2:1) | éxito `#2FBF7F` (6,5:1) · aviso `#E0A106` (6,8:1) · peligro `#F28B82` (6,5:1) | Texto e íconos de estado |
| Estados (relleno) | `success/warning/danger` actuales al 12 % | ídem | Fondo de badges y banners |

Los contrastes se calcularon el 2026-10-10 sobre `white` (claro) y `navy-800` (oscuro). Los
colores de estado actuales siguen sirviendo como **relleno** y como marca no textual, pero ya no
como texto: hoy `text-warning` sobre blanco da 2,3:1.

**Paleta de datos (nueva, validada con `dataviz/scripts/validate_palette.js`):**

| Slot | Claro (superficie `#FFFFFF`) | Oscuro (superficie `#11224D`) |
|---|---|---|
| 1 | `#2560E6` azul | `#4F7FF5` azul |
| 2 | `#B8860B` oro | `#A8851A` oro |
| 3 | `#0E9DB5` cyan | `#139AAF` cyan |
| 4 | `#7B4FD6` violeta | `#8E6CE8` violeta |

Resultado: las 5 verificaciones pasan en los dos modos (banda de luminosidad, croma, separación CVD
≥ 10,7, piso de visión normal ≥ 19,4 y contraste ≥ 3:1). El orden es fijo y no se cicla: con más de
4 series, el resto va a "Otros". Una sola serie usa cyan (`#0E9DB5` claro, `#22C7E0` oscuro). Los
colores de estado quedan reservados para estados y nunca se usan como "serie 3".

### Tipografía

| Rol | Familia | Panel | App | Notas |
|---|---|---|---|---|
| Cifra héroe (KPI principal) | Montserrat 700 | 30/36 | 28/34 | `tabular-nums` para que las cifras no bailen al actualizar |
| Título de página (`h1`) | Montserrat 600 | 24/32 | 22/28 | Uno por página (`PageHeader`) |
| Título de bloque | Montserrat 600 | 17/24 | 17/24 | Tarjetas y widgets |
| Cuerpo | Inter 400 | 15/24 | 16/24 | En la app sube a 16 por legibilidad bajo el sol |
| Cuerpo denso (tablas compactas) | Inter 400 | 14/20 | 14/20 | Solo en `DataTable density="compact"` |
| Etiqueta y ayuda | Inter 500 / 400 | 13/18 · 12/16 | 14/20 · 12/16 | |
| Código e IDs | JetBrains Mono | 13/18 | 13/18 | Solo IDs técnicos. Nunca en etiquetas de datos |

Se mantienen Montserrat (display) e Inter (cuerpo) porque los fija el manual de marca: son dos
familias claramente distintas y ya están cargadas en los dos repos. La app tiene instalados
`@expo-google-fonts/montserrat` e `inter`, pero el comentario de `theme.ts` dice que todavía usa
Roboto en buena parte: [HU-DS-09](hu/HU-DS-09-kit-de-componentes-app.md) lo cierra. Las mayúsculas siguen reservadas a los encabezados de
tabla (regla vigente de `DESIGN.md`).

---

## 2. 🧩 Sistema de diseño

### Tokens

| Categoría | Tokens | Valor | Estado |
|---|---|---|---|
| Color base | `navy-*`, `blue-*`, `cyan-400`, `gold-500`, `slate-*`, neutros | ver `tokens.json` | ✅ existe |
| Color semántico | `bg`, `surface`, `surface-2`, `surface-raised`, `border*`, `text*`, `link`, `focus`, `hover`, `overlay` | por tema | ✅ existe |
| **Estado por tema** | `status-{success,warning,danger,info}-{fg,bg,border}` | tabla de arriba | ➕ [HU-DS-01](hu/HU-DS-01-tokens-v2.md) |
| **Datos** | `data-cat-{1..4}`, `data-seq-{100..700}` (cyan), `data-single`, `data-grid`, `data-axis` | tabla de arriba | ➕ [HU-DS-01](hu/HU-DS-01-tokens-v2.md) |
| Espacio | `space-{1,2,3,4,6,8,12,16}` = 4…64 px | base 4 | ✅ existe |
| Radio | `radius-sm 6` (inputs, badges) · `md 12` (tarjetas) · `lg 20` (diálogos, sheets) · `pill` | el radio interno siempre es menor que el del contenedor | ✅ existe; se documenta la jerarquía |
| **Tipografía** | `type-{hero,h1,block,body,body-dense,label,caption,mono}` (familia, tamaño, alto de línea, peso, tracking) | tabla de arriba | ➕ [HU-DS-01](hu/HU-DS-01-tokens-v2.md) |
| **Elevación** | `elev-0` (plano, borde suave) · `elev-1` (tarjeta: borde + `0 1px 2px rgb(8 15 34 / .06)`) · `elev-2` (popover: `0 8px 24px rgb(8 15 34 / .12)`) · `elev-3` (diálogo: `0 16px 48px rgb(8 15 34 / .18)`) | En oscuro la elevación se marca con el paso de superficie (`surface` → `surface-2` → `surface-raised`) y el borde, no con sombra | ➕ [HU-DS-01](hu/HU-DS-01-tokens-v2.md) |
| **Motion** | `dur-instant 100` · `dur-fast 150` · `dur-base 200` · `dur-slow 250` ms; `ease-out cubic-bezier(.2,0,0,1)` · `ease-in cubic-bezier(.3,0,1,1)` · `ease-emphasized cubic-bezier(.05,.7,.1,1)` | La salida dura el 75 % de la entrada | ➕ [HU-DS-01](hu/HU-DS-01-tokens-v2.md) |
| **Densidad** | `row-comfortable 48` · `row-compact 40` · `control-md 40` · `control-lg 48` (táctil) | La app usa siempre `control-lg` (48 dp) | ➕ [HU-DS-01](hu/HU-DS-01-tokens-v2.md) |
| **Breakpoints** | `sm 640` · `md 768` · `lg 1024` · `xl 1280` · `2xl 1536` | Los de Tailwind; se documentan como contrato del shell | ➕ se documentan |

Convención de nombres: `--sh-<categoría>-<rol>[-<variante>]` en CSS (por ejemplo
`--sh-status-warning-fg`) y `shToken.<categoría>.<rol>` en la app. Los tokens viejos quedan como
alias durante una versión y la regla de lint de [HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md) avisa cuando se usan.

### Librería de componentes (Atomic Design)

`✅` existe y se mantiene · `🔁` existe y pasa a v2 · `➕` nuevo. **P** = panel, **A** = app.

**Átomos**

| Componente | P | A | Props y variantes | Notas |
|---|---|---|---|---|
| `Button` | 🔁 | ➕ | `variant: primary·secondary·ghost·danger·link` · `size: sm·md·lg` · `loading` · `iconLeft/Right` · `asChild` | `primary` es el único que lleva el gradiente. `loading` conserva el ancho y pone `aria-busy` |
| `IconButton` (hoy `IconAction`) | 🔁 | ➕ | `label` obligatorio (nombre accesible) · `tone` · `size` | Blanco mínimo de 40 px en panel y 48 dp en app |
| `Input`, `Textarea`, `Select`, `Switch` | ✅ | ➕ | `invalid` · `disabled` · `size` | `invalid` pone `aria-invalid` y el borde `status-danger-border` |
| `Checkbox`, `Radio` | ➕ | ➕ | `checked` · `indeterminate` · `disabled` | Radix en el panel |
| `Badge` | 🔁 | ➕ | `tone: neutral·info·success·warning·danger·accent` · `icon` · `size` | Con tono de estado el ícono es **obligatorio** (el color nunca va solo) |
| `Avatar` | ➕ | 🔁 | `src` · `name` (iniciales) · `size: xs·sm·md·lg` · `status` | La app ya tiene `Avatar` en `modules/cobranza/components`: sube a `shared/ui` |
| `Skeleton` | ✅ | ➕ | `shape: text·rect·circle` · `lines` | Estático, sin pulso (regla de `DESIGN.md`) |
| `Tooltip` | ✅ | — | `content` · `side` · `delay 400 ms` | Nunca lleva información que no esté en otro lado. En la app no hay tooltips: se usa una etiqueta visible |
| `Kbd` | ➕ | — | `keys: string[]` | Atajos en la paleta y en la ayuda |
| `Separator` | ✅ | ➕ | `orientation` | |

**Moléculas**

| Componente | P | A | Props y variantes | Notas |
|---|---|---|---|---|
| `Field` | ✅ | 🔁 | `label` · `hint` · `error` · `required` | Une label, control y error con `aria-describedby`. En la app reemplaza `CampoModal` y `CampoTelefono` |
| `SearchInput` | ➕ | ➕ | `value` · `onChange` · `shortcut="/"` · `loading` | |
| `Breadcrumbs` | ➕ | — | `items: {label, href?}[]` | Se arman solas desde `nav.ts` (ver §3). En la app, el `Breadcrumb` de cobranza se conserva |
| `Tabs` | 🔁 | ➕ | `items` · `value` · `asLinks` | Si cada pestaña cambia de ruta se renderiza como `nav` con `aria-current`, no como `tablist` |
| `DropdownMenu`, `Popover` | ➕ | — | Radix | Menús de fila, del usuario y de la sidebar plegada |
| `Toast` | ✅ | ➕ | `success` (`role=status`, 5 s) · `error` (`role=alert`, hasta cerrarlo) | En la app reemplaza `BannerMensaje` para la confirmación de acciones |
| `KpiTile` (hoy `StatCard`) | 🔁 | ➕ | `label` · `value` · `delta` · `polarity: up-good·up-bad` · `period` · `sparkline` · `href` · `loading` · `error` | El delta se escribe ("+12 % frente a los 7 días anteriores") con flecha. El color es secundario |
| `EmptyState` | 🔁 | ➕ | `icon` · `title` · `description` · `action` · `secondaryAction` | Siempre ofrece una acción (regla de [HU-UX-04](../SPEC-12-arquitectura-de-informacion/hu/HU-UX-04-estados-vacios-y-permisos.md)) |
| `SyncStatus` | — | ➕ | `state: online·offline·syncing·error` · `pending: number` · `onRetry` | Chip permanente en el header de campo |
| `Pagination` | ✅ | — | | |

**Organismos**

| Componente | P | A | Notas |
|---|---|---|---|
| `DataTable` v2 | 🔁 | — | `density` · orden · selección · encabezado fijo · visibilidad de columnas · estados de carga, vacío y error. La usa [HU-UI-08](../SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md) para su `FilterBar` |
| `ListItem` / `RecordRow` | — | ➕ | La fila táctil de la app (cliente, cartera, pago), con `leading`, `trailing`, `meta` y `badge` |
| `Dialog`, `Confirm` | ✅ | ➕ | `Confirm` explica la **consecuencia** (regla vigente) |
| `Sheet` (panel lateral o inferior) | ➕ | 🔁 | Panel: detalle sin salir de la tabla. App: `ModalConFooter` pasa a `Sheet` con asa y cierre por gesto |
| `PageHeader` v2 | 🔁 | 🔁 | Migas + título + descripción + acciones + pestañas de sección. En la app equivale a `HeaderPantalla` |
| `Sidebar` v2, `Topbar` v2 | 🔁 | — | §3 |
| `CommandPalette` | ➕ | — | [HU-DS-05](hu/HU-DS-05-paleta-de-comandos-y-atajos.md) |
| `ChartCard` | ➕ | ➕ | Título, período, gráfico, leyenda (desde 2 series) y botón "Ver tabla" |
| `ActivityFeed`, `AlertList`, `QuickActions` | ➕ | ➕ | Widgets del Resumen |
| `WidgetGrid` | ➕ | ➕ | Grilla bento del Resumen ([HU-DS-07](hu/HU-DS-07-resumen-modular-por-rol.md)) |

**Plantillas** (`components/templates/` en el panel): `ListPage` (header + filtros + tabla),
`DetailPage` (header con migas + resumen + pestañas), `DashboardPage` (período + grilla de widgets),
`SettingsPage` (pestañas con estado, [HU-UI-09](../SPEC-13-vistas-profesionales/hu/HU-UI-09-configuracion-por-pestanas.md)) y `AuthCard` (ya existe como `tarjeta-de-acceso`).

**Páginas:** `app/(app)/**/page.tsx` solo hace fetch y composición, como manda `DESIGN.md`.

### Estados de interacción (iguales en todo el kit)

| Estado | Regla visual | Regla técnica |
|---|---|---|
| default | Tokens del tema | |
| hover | Fondo `hover`, transición `dur-fast` | Solo con puntero (`@media (hover: hover)`) |
| active / pressed | Un paso más oscuro de superficie | En la app, `Pressable` con `android_ripple` del tema |
| focus-visible | Outline de 2 px `focus` con 2 px de separación | Nunca `outline: none` sin reemplazo. WCAG 2.4.11 |
| disabled | Texto `text-soft` y borde `control-border`. Sin opacidad sobre el texto | `disabled` nativo o `aria-disabled` si debe seguir enfocable |
| loading | Skeleton con la forma del contenido. En botones, spinner dentro sin cambiar el ancho | `aria-busy="true"` |
| error | Borde y texto `status-danger-*` con ícono y mensaje que dice qué pasó y cómo seguir | `aria-invalid` + `aria-describedby` |
| selected / current | Fondo `surface-raised` e indicador de 3 px a la izquierda | `aria-current="page"` o `aria-selected` |

---

## 3. 🗺️ Mapa de navegación

### Árbol (máximo 3 niveles: grupo › sección › pestaña)

Los grupos y nombres son los de [HU-UX-02](../SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) ([SPEC-12](../SPEC-12-arquitectura-de-informacion/spec.md)). Esta spec no los decide: los usa.

```
Inicio ─────────────── Resumen (por rol)
Atención ───────────── Conversaciones · Por atender · Contactos
Ventas y cobros
  ├─ Comercio ──────── Pedidos · Productos · Categorías · Promociones          (si el pack está activo)
  ├─ Cobranza
  │   ├─ Operación ─── Resumen · Carteras › [cartera] · Clientes › [cliente] · Pagos · Promesas · Cobros al propietario
  │   ├─ Equipo de campo ─ Gestores · Dispositivos · Monitoreo IA
  │   └─ Control ───── Reportes · Reglas · Alertas de acceso · Auditoría · Propietario
  └─ Agenda ────────── Citas · Tipos · Bloqueos · Horario
Asistente ──────────── Habilidades › [habilidad] · Probar asistente · Plantillas
Canales ────────────── Conexiones › WhatsApp | Meta › [conexión] | WhatsApp Web
Consumo y plan ─────── Plan · Consumo
Equipo ─────────────── Colaboradores
Configuración
Plataforma (master) ── Negocios · Alta automática · Meta de plataforma · Mensajes fallidos
```

Las subsecciones de Cobranza ya existen en `nav.ts` como `sub` (General, Monitoreo, Seguridad). Esta
spec propone renombrarlas a Operación, Equipo de campo y Control, y darle a cada ítem su propio
ícono: hoy 12 de los 14 usan `HandCoins`, y con la barra plegada no se distinguirían.

### Comportamiento responsive del shell

| Ancho | Sidebar | Topbar | Contenido |
|---|---|---|---|
| < 768 px | Cajón (`MobileNav` actual) que abre desde el botón de menú. Atrapa el foco, cierra con Escape, con el fondo o al navegar | Logo, negocio, búsqueda (abre la paleta) y avatar | Ancho completo, `px-4`. Las migas se reducen a "‹ Sección anterior" |
| 768–1279 px | **Plegada (72 px)** por defecto: íconos con tooltip a la derecha. Los grupos con hijos abren un menú flotante (`DropdownMenu side="right"`) | Migas completas | `max-w-[1200px]` |
| ≥ 1280 px | **Expandida (256 px)** por defecto, con grupos plegables (lo que ya guarda `panel_nav_collapsed`) | Migas, búsqueda y estado del asistente | `max-w-[1200px]`. Bandeja y tablas densas, a todo el ancho (D-SPEC-13-1) |

- **Persistencia:** la elección del usuario (expandida o plegada) se guarda en la cookie
  `panel_sidebar` y la lee el layout en el servidor, así que no hay salto al cargar (D-SPEC-29-4).
  Vale para ≥ 768 px. Los grupos plegados siguen en `localStorage` como hoy.
- **Control:** botón al pie de la sidebar ("Plegar menú", con `aria-expanded`) y atajo `[`.
- **Activo:** indicador cyan de 3 px a la izquierda, fondo `surface-raised` y `aria-current="page"`.
  Con la barra plegada, el grupo que contiene la página activa también queda marcado.
- **Migas:** se derivan de `nav.ts` (grupo › sección) y las páginas de detalle agregan su etiqueta
  (`PageHeader breadcrumbs={[…, {label: cartera.nombre}]}`). Van en `nav aria-label="Migas de pan"`
  con `aria-current="page"` en la última.
- **Pestañas de sección:** las secciones de un pack con `sub` muestran sus hermanas como pestañas en
  el `PageHeader` (por ejemplo, Agenda: Citas · Tipos · Bloqueos · Horario). Con desborde hacen scroll
  horizontal con máscara de fundido. No hay pestañas dentro de pestañas.

### Atajos de teclado

| Atajo | Acción |
|---|---|
| `Ctrl K` / `⌘ K` | Paleta de comandos: secciones permitidas, acciones rápidas y búsqueda global (`GET /search`, ADR-0096, el mismo endpoint de la búsqueda de la app) |
| `/` | Enfoca el buscador o el filtro de la página |
| `[` | Plegar o expandir la sidebar |
| `g` y luego `i` · `a` · `c` · `v` | Ir a Inicio · Atención · Conversaciones · Ventas y cobros |
| `?` | Ayuda de atajos |
| `Esc` | Cierra la capa superior (paleta, diálogo, sheet, cajón) |

Los atajos de una sola tecla no se disparan dentro de campos editables y se pueden apagar en
Configuración → Accesibilidad, como exige WCAG 2.1.4 ("Atajos de teclado por caracteres").

---

## 4. 📊 Wireframe textual del Resumen

### Estructura común

```
┌ PageHeader ─────────────────────────────────────────────────────────────────────────────┐
│ Inicio › Resumen                                                                        │
│ Resumen                                   [Hoy | 7 días | 30 días | Mes]  [Personalizar] │
│ Actualizado hace 2 min · Reintentar                                                     │
└─────────────────────────────────────────────────────────────────────────────────────────┘
┌ Primeros pasos (fijo arriba mientras queden pasos, HU-SH-06) ───────────────────────────┐
└─────────────────────────────────────────────────────────────────────────────────────────┘
┌ Alertas (solo si hay) ─ "Tu asistente está pausado" · "Consumo al 80 %" · "3 alertas de acceso" ┐
```

Grilla de 12 columnas en ≥ 1280 px (widget S = 3, M = 6, L = 8 o 12), de 6 en 768–1279 y de 1 en
celular. El orden de lectura en el DOM es el mismo que el visual, así que el lector de pantalla y el
tabulador recorren la grilla en el orden en que se ve.

### Perfil Dueño (owner o master)

```
┌ KPI S ──────────┐┌ KPI S ──────────┐┌ KPI S ──────────┐┌ KPI S ──────────┐
│ Conversaciones  ││ Resueltas sin   ││ Recaudo de hoy  ││ Consumo del plan│
│ 1.284           ││ humano  82 %    ││ $ 4.320.000     ││ 64 %            │
│ ▲ 12 % vs 7 d   ││ ▲ 3 pts         ││ ▼ 5 % vs ayer   ││ 11 días restan. │
│ ╱╲╱‾‾╲╱ (spark) ││ ╱‾‾╲╱‾ (spark)  ││ ╲╱╲__╱ (spark)  ││ ▓▓▓▓▓▓░░░ (barra)│
└─────────────────┘└─────────────────┘└─────────────────┘└─────────────────┘
┌ Tendencia L (8) ─────────────────────────────────┐┌ Acciones rápidas S (4) ─┐
│ Conversaciones y resueltas sin humano (30 días)  ││ Pausar asistente        │
│ línea + área, crosshair, "Ver tabla"             ││ Invitar colaborador     │
│                                                  ││ Nuevo producto          │
└──────────────────────────────────────────────────┘└─────────────────────────┘
┌ Actividad reciente M (6) ────────────────────────┐┌ Estado del sistema M (6) ┐
│ Conversación de Ana resuelta · hace 3 min        ││ Asistente  ● Activo     │
│ Pago registrado por Luis (campo) · hace 10 min   ││ Habilidades activas  3  │
│ Pedido OC-0142 pagado · hace 22 min              ││ WhatsApp  ● Conectado   │
└──────────────────────────────────────────────────┘└─────────────────────────┘
```

### Perfil Supervisor (escritura en secciones de un pack)

Recaudo de hoy · Clientes en mora · Promesas que vencen hoy · Gestores en ruta (KPI S) → Recaudo
frente a meta, 30 días (barras, L) + Alertas de cobranza (S) → Promesas del día (lista, M) + Gestores
con su avance del día (lista con barra de progreso, M). Para Comercio o Agenda, el mismo patrón con
pedidos o citas.

### Perfil Operador (solo atención)

Por atender ahora · Tiempo medio de primera respuesta · Resueltas sin humano (KPI S) → Cola de
escalaciones (lista con antigüedad, L) + Acciones rápidas (S). Sin costos, plan ni packs.

### Catálogo de widgets

| Clave | Forma | Datos | Permiso requerido |
|---|---|---|---|
| `kpi.conversaciones` | KpiTile + sparkline | `GET /admin/dashboard?period=` ([HU-UI-07](../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md)) | `conversations` |
| `kpi.resueltas_sin_humano` | KpiTile | ídem | `conversations` |
| `kpi.por_atender` | KpiTile (`polarity=up-bad`) | ídem | `escalations` |
| `kpi.consumo` | KpiTile + barra de uso | ídem (`billing`) | `plan` |
| `kpi.recaudo_hoy`, `kpi.mora`, `kpi.promesas_hoy` | KpiTile | resumen de `pack_cobranza` (el que ya consume la app admin) | `pack_cobranza:resumen` |
| `kpi.pedidos`, `kpi.citas_hoy` | KpiTile | endpoints de `pack_commerce` y `pack_calendar` | sección del pack |
| `chart.tendencia_atencion` | Línea y área | [HU-UI-07](../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) | `conversations` |
| `chart.recaudo_vs_meta` | Barras | resumen de cobranza | `pack_cobranza:reportes` |
| `lista.actividad` | ActivityFeed | conversaciones y auditoría | `conversations` o `pack_cobranza:auditoria` |
| `lista.alertas` | AlertList | asistente pausado, consumo, plantillas faltantes, alertas de acceso | cualquiera (cada alerta filtra la suya) |
| `lista.escalaciones` | Lista con antigüedad | escalaciones | `escalations` |
| `acciones.rapidas` | QuickActions | — (cada acción revisa su permiso de escritura) | según la acción |
| `estado.sistema` | Lista clave/valor | `/admin/dashboard` | `dashboard` |

Reglas del Resumen (skills `kpi-dashboard-design` y `dataviz`):

- De 4 a 6 KPIs por perfil. Ninguna métrica de vanidad: cada KPI tiene un `href` a la lista filtrada
  que lo explica.
- El delta siempre dice contra qué compara. `polarity` decide si subir es bueno (conversaciones) o
  malo (mora, escalaciones).
- Cada widget es un límite de `Suspense` con su propio skeleton y su propio error con "Reintentar":
  si falla uno, el resto se muestra igual (streaming de RSC).
- Vacío con acción, por ejemplo "Conecta WhatsApp para empezar a ver conversaciones" →
  `/conexiones`.
- Sin polling, salvo `lista.escalaciones`, que sigue la regla de D-SPEC-13-2 (5–10 s con la pestaña
  visible).
- Cada gráfico tiene un botón "Ver tabla" con los mismos datos, un crosshair con tooltip al pasar el
  puntero o con flechas, y un solo eje Y.

---

## 5. 📱 Adaptación a la app (diferencias clave frente a la web)

### Dos shells, dos heurísticas

| | Campo (gestor) | Panel en la app (dueño, supervisor, colaborador) |
|---|---|---|
| Navegación | **Cajón lateral (se conserva)** con Inicio, Carteras (si hay más de una), Clientes (con filtros) y Diario | **Header con hamburguesa y cajón lateral** (D-34, reemplaza a D-SPEC-29-5) con la misma lista agrupada que el sidebar del panel web: secciones dentro de grupos plegables, packs plegados al arrancar |
| Por qué | Una cartera a la vez, secciones anidadas (filtros de clientes), memoria muscular de calle | Paridad exacta con el panel web en móvil; ~40 secciones que no caben en 4 destinos; cero dependencias nativas (sale por OTA) |
| Detalle | Overlays a pantalla completa con cierre por gesto (`VentanaCerrarConSwipe`), como hoy | Stack nativo con back del sistema; cada sección del cajón abre su módulo en la pestaña interna pedida |
| Qué cambia en [HU-DS-10](hu/HU-DS-10-cobranza-de-campo-con-el-kit.md) / [HU-DS-11](hu/HU-DS-11-shell-del-panel-en-la-app.md) | Solo los componentes visuales (y arranca en oscuro) | El shell (header, cajón, tema); el Resumen por rol pasa a [HU-DS-13](hu/HU-DS-13-resumen-movil-por-rol.md) |

### Vistas de campo de cobranza que se conservan (D-SPEC-29-6)

| Vista | Archivo | Se conserva | Cambia (solo visual, [HU-DS-10](hu/HU-DS-10-cobranza-de-campo-con-el-kit.md)) |
|---|---|---|---|
| Selección de cartera | `SeleccionCarteraScreen` | Lista de carteras con KPIs y flujo hacia la cartera activa | `ListItem` + `KpiTile`, skeleton, `EmptyState` con acción |
| Inicio de la cartera | `CarteraDetalleScreen` | Información, estadísticas, del día, en mora y notas | KPIs con `KpiTile` (sparkline del recaudo de 7 días si el dato existe localmente), `Sheet` para editar la nota |
| Clientes | `ClientesScreen` | Filtros Todos, Al día, En mora y Sin préstamos desde el menú, alta de cliente | `SearchInput`, `RecordRow` con `Badge` de estado con ícono, `Field` en el alta |
| Diario | `TrayectoDiarioScreen` | Pagos y abonos del día, cliente cercano, GPS, liquidación, PDF, trayectos | Botones del kit (la CTA "Generar liquidación" es la `primary`), `SyncStatus` |
| Ficha del cliente | `ClienteScreen` (overlay) | Préstamos, cuotas, registrar pago o no pago, QR, mapa, evidencias | Encabezado con `Avatar`, `Sheet` para registrar pago, toast + háptico al confirmar |
| Préstamo | `PrestamoScreen` | Canvas de cuotas y envío por WhatsApp | Tipografía y tokens |
| Menú lateral | `navigation/MenuLateral.tsx` | Estructura e ítems dinámicos de `CarteraFlujo` | Tokens, indicador de activo y blancos de 48 dp |
| Perfil, Configuración, Notificaciones | `PerfilScreen`, `ConfiguracionScreen`, `NotificacionesScreen` | Contenido | Kit |

La cobranza admin de la app (`modules/cobranza-admin`, pestañas Resumen, Carteras, Clientes, Pagos,
Promesas, Dispositivos, Reportes, Monitoreo, Reglas, Alertas, Auditoría, Gestores y Propietario
según permisos) también conserva su estructura. Solo cambia al kit en [HU-DS-11](hu/HU-DS-11-shell-del-panel-en-la-app.md).

### Reglas propias de la app

- **Blancos táctiles** de al menos 48 × 48 dp. La CTA principal va en la zona del pulgar (abajo).
- **Escala de fuente del sistema** respetada hasta 200 %. Las cifras densas usan
  `maxFontSizeMultiplier=1.6` para no romper filas.
- **Sol directo:** las cifras y estados del campo apuntan a 7:1 (AAA). El tema arranca en **oscuro**
  en toda la app, como el panel web (D-34; no sigue al sistema), con el selector en el header del
  panel, en el cajón y en el menú lateral del campo; la preferencia guardada manda.
- **Edge-to-edge** (obligatorio con `targetSdk 35`): todo con `SafeAreaView` o `useSafeAreaInsets`.
  Nada bajo la barra de estado (lo que ya se ve en el smoke del OPPO).
- **Gestos:** back del sistema y back predictivo (los `BackHandler` de `CarteraFlujo` cierran overlay
  → trayectos → pantalla), pull-to-refresh en listas y cierre por gesto en overlays y sheets.
  Ninguna acción vive solo en una pulsación larga.
- **Hápticos** (`expo-haptics`, dependencia nueva de Expo): éxito al confirmar un pago, aviso en un
  error de validación. Nada más.
- **Offline-first:** el motor offline no cambia (ADR-APP-04). Lo que cambia es que el estado es
  visible: `SyncStatus` en el header de campo ("Sin conexión · 3 cambios por enviar") y un `Badge`
  "Pendiente" en cada pago registrado sin conexión hasta que llegue el ack.
- **Push:** el canal y el deep link ya existen ([HU-APP-05](../SPEC-25-app-movil-oficial/hu/HU-APP-05-notificaciones-push.md)). Cada categoría de notificación tiene su
  ícono y lleva a la pantalla exacta. La bandeja interna (`NotificacionesScreen`) usa `RecordRow`.
- **Gráficos:** `react-native-svg` + `d3-scale`/`d3-shape`, con las mismas primitivas que el panel.
  No se ponen sparklines dentro de listas de más de 50 filas (rendimiento en gama media).

---

## 6. ⚙️ Stack técnico y estructura

### Stack (se conserva lo que hay; se agrega lo mínimo)

| Capa | Panel | App | Qué se agrega |
|---|---|---|---|
| Framework | Next.js 16 (App Router, RSC) + React 19 | Expo 57 + React Native 0.86 | — |
| Estilos | Tailwind v4 con `@theme` sobre variables CSS de los tokens | `StyleSheet` + `useTheme()` sobre `tokens.ts` | Nada |
| Primitivos | Radix (dialog, slot), cva, tailwind-merge, lucide | `@expo/vector-icons` | Panel: `@radix-ui/react-dropdown-menu`, `popover`, `checkbox`, `radio-group` y `cmdk` |
| Gráficos | — | — | `d3-scale`, `d3-shape` (los dos) y `react-native-svg` (app) |
| Estado del servidor | RSC + `apiFetch` + `useAction` (`router.refresh`) | Motor offline propio + (ADR-APP-04) TanStack Query | — |
| Estado de UI | `useState` + `useSyncExternalStore` sobre cookie o `localStorage` (patrón de `sidebar.tsx` y `toast-store.ts`) | Context (`theme-context`, `menu-lateral-context`, …) | — |
| Tests | Vitest + Testing Library + axe ([HU-UI-04](../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md)) | Jest + RNTL | Test de contraste de tokens y regla de lint anti-hex ([HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md)) |

**Sobre Redux Toolkit, Zustand o Pinia:** no se agregan. En el panel el estado del servidor vive en
RSC y el estado de UI global es poco (tema, sidebar, paleta abierta, toasts), y ya se resuelve con
stores de 20 líneas sobre `useSyncExternalStore`. Si un día hace falta un store compartido grande, se
usa Zustand (unos 2 KB) con un ADR. Pinia es de Vue y no aplica.

**Theming dinámico:** variables CSS por tema bajo `[data-theme="dark"|"light"]` (las escribe el
build de tokens), un `ThemeToggle` que guarda la cookie y la lee el servidor (sin parpadeo), y en la
app `ThemeContext`. Cambiar la marca toca `tokens.json` y nada más.

### Estructura de carpetas

Panel (`apps/panel-web`, organizado por feature en `app/(app)/<sección>`; se agregan las carpetas
marcadas con ➕):

```
app/
├── (app)/<sección>/page.tsx · loading.tsx · error.tsx · _components/   ← feature
├── (app)/dashboard/_widgets/                                           ➕ un archivo por widget
└── (dev)/catalogo/                                                     ➕ HU-DS-03 (solo dev y test)
components/
├── ui/          átomos y moléculas sin dominio
├── dataviz/     ➕ sparkline, line-chart, bar-chart, progress-ring, chart-table
├── domain/      organismos de dominio que reciben datos
├── shell/       sidebar, topbar, breadcrumbs ➕, command-palette ➕
└── templates/   ➕ list-page, detail-page, dashboard-page, settings-page
lib/
├── shell/       ➕ atajos, preferencias (cookie), migas desde nav.ts
├── dashboard/   ➕ perfiles por rol, registro de widgets
└── api/ · format.ts · labels.ts · use-action.ts                       (ya existen)
```

App (`solvershub-apk`, monolito modular con fronteras de ADR-APP-01):

```
src/
├── core/theme/      tokens.ts (generado) · theme.ts · motion.ts ➕
├── shared/ui/       ➕ kit RN (Button, Field, Badge, Avatar, KpiTile, RecordRow, Sheet, SyncStatus…)
├── shared/dataviz/  ➕ Sparkline, LineChart, BarChart sobre react-native-svg
├── navigation/      PanelShell v2 (4 + Más), MenuLateral (se conserva)
└── modules/<m>/     screens · components · api  (cobranza: mismas vistas)
```

### Convenciones de nombres

| Qué | Panel | App |
|---|---|---|
| Archivos de componentes | `kebab-case.tsx` (`kpi-tile.tsx`) | `PascalCase.tsx` (`KpiTile.tsx`) |
| Componentes | `PascalCase` | `PascalCase` |
| Hooks | `useAlgo` en `lib/` | `useAlgo` |
| Primitivos del kit | En inglés (`Button`, `Badge`), como hoy | En inglés, para que coincidan con el panel |
| Dominio | En español (`PrimerosPasos`, `TarjetaDeAcceso`) | En español (`CarteraFlujo`, `TrayectoDiario`) |
| Props | `variant`, `size`, `tone`, `polarity`, `loading`, `disabled`, `onAlgo` | Iguales |
| Tokens | `--sh-<categoría>-<rol>[-<variante>]` | `shToken.<categoría>.<rol>` |
| Tests | Al lado del componente: `*.test.tsx` | Al lado: `*.test.tsx` |

---

## 7. 🎞️ Motion y microinteracciones

| Interacción | Duración | Curva | Panel | App |
|---|---|---|---|---|
| Hover, foco, toggle | 150 ms | `ease-out` | Color y fondo | — |
| Presión de botón | 100 ms | `ease-out` | Fondo un paso más oscuro | Ripple del tema |
| Dropdown, tooltip, popover | 150 ms | `ease-out` | Opacidad + 4 px en Y | — |
| Diálogo | 200 ms entra / 150 ms sale | `ease-out` / `ease-in` | Opacidad + escala .98 → 1 | Opacidad |
| Sheet y cajón | 250 ms | `ease-emphasized` | Desliza desde el borde | Desliza, y sigue al dedo en el gesto |
| Toast | 200 ms | `ease-out` | Sube 8 px | Sube 8 px |
| Cambio de ruta | 150 ms | `ease-out` | Fundido cruzado solo del `main` (View Transitions, si el navegador lo soporta) | Animación nativa del stack |
| Sidebar plegar o expandir | 200 ms | `ease-out` | Ancho. Las etiquetas se ocultan sin animarse | — |
| Confirmación de pago | 200 ms | `ease-out` | — | Check que se dibuja + háptico de éxito |
| Actualización de un KPI | 150 ms | `ease-out` | Fundido del número | Fundido del número |

Reglas:

- Solo se anima lo que cambia por una acción del usuario. No hay entradas escalonadas, pulsos,
  `hover-scale` ni skeletons con brillo (regla vigente de `DESIGN.md`).
- **`prefers-reduced-motion`:** en el panel, la regla global de `globals.css` lleva las duraciones a
  ~0. En la app, `AccessibilityInfo.isReduceMotionEnabled()` alimenta `motion.ts`, que devuelve 0 en
  todas las duraciones. El háptico se mantiene, porque no es movimiento.
- Las duraciones salen de los tokens (`dur-*`, `ease-*`). Nada de `duration-300` sueltos.

---

## Datos (tablas, migraciones, RLS)

Ninguna. Las preferencias se guardan en una cookie y en `localStorage` (D-SPEC-29-4). Si se elige la
opción B, se crea `user_preferences` con `tenant_id`, RLS e índice `(tenant_id, user_id)` en una HU
aparte.

## API

- Se consume `GET /admin/dashboard?period=` con series y comparación, que entrega [HU-UI-07](../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md).
- Se consume `GET /search` (ADR-0096) desde la paleta de comandos, por el BFF con `X-Tenant-Id`.
- El resumen de `pack_cobranza` ya existe (lo usa `modules/cobranza-admin` en la app).
- No hay endpoints nuevos en esta spec.

## UI

Lo cubren las secciones 1 a 7. Toda vista sigue `DESIGN.md` v2, que reescribe [HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md) con lo de
esta spec.

## ADR a crear o enmendar

| ADR | Repo | Qué decide |
|---|---|---|
| ADR-0002 · Sistema de diseño v2 | `solvershub-panel/docs/adr` | Tokens extendidos, paleta de datos, primitivas SVG propias (D-SPEC-29-2) y catálogo (D-SPEC-29-3) |
| ADR-0003 · Shell adaptativo y atajos | `solvershub-panel/docs/adr` | Breakpoints del shell, cookie `panel_sidebar` (D-SPEC-29-4), paleta y atajos de una tecla |
| ADR-APP-07 · Kit de UI y navegación v2 | `solvershub-apk/docs/adr` | `shared/ui`, 4 destinos + Más (D-SPEC-29-5) y el campo que se conserva (D-SPEC-29-6) |
| ADR-APP-04 (enmienda) | `solvershub-apk/docs/adr` | Registrar que TanStack Query todavía no está instalado (ver "Recomendaciones") |

## Migración, despliegue y reversa

- **Tokens:** cambio aditivo. Los nombres viejos quedan como alias una versión. Reversa: revertir el
  PR de `brand/` y volver a sincronizar.
- **Panel:** cada HU es un PR a `develop` desplegado en test (la regla de siempre). El shell v2 entra
  detrás de la variable `PANEL_SHELL_V2` hasta que pase la prueba con 5 usuarios. Después se quita la
  variable.
- **App:** [HU-DS-10](hu/HU-DS-10-cobranza-de-campo-con-el-kit.md) (campo) sale por EAS Update con despliegue gradual (10 % → 50 % → 100 %) después
  del smoke en el OPPO. Reversa: volver a publicar la actualización anterior (el rollback de OTA ya
  probado). [HU-DS-11](hu/HU-DS-11-shell-del-panel-en-la-app.md) sigue el mismo camino y lleva el tema
  oscuro por defecto al campo: hay que avisarlo en la nota de la OTA.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Regresión en el campo de cobranza | D-SPEC-29-6: solo visual. Los tests de comportamiento no se tocan. Smoke en el OPPO antes y después y despliegue gradual por OTA |
| [HU-UX-02](../SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) cambia `nav.ts` al mismo tiempo que [HU-DS-04](hu/HU-DS-04-shell-adaptativo-del-panel.md) | [HU-DS-04](hu/HU-DS-04-shell-adaptativo-del-panel.md) solo consume `NAV_GROUPS`. Si llegan juntas, se mergea primero [HU-UX-02](../SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) |
| El JS del Resumen crece | Sin librería de gráficos (D-SPEC-29-2). `cmdk` se carga solo al abrir la paleta (`dynamic import`) |
| Un rediseño "a medias" convive con pantallas viejas | Los alias de tokens y el catálogo dejan ver la deriva. [HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md) la mide con la regla de lint y el conteo baja PR a PR |
| El contraste del gradiente de la CTA | Hoy `Button variant="accent"` pone texto blanco sobre `#2F6BFF → #22C7E0`, que en el extremo cyan da **2,0:1**. [HU-DS-01](hu/HU-DS-01-tokens-v2.md) crea `gradient-cta` (`navy-700 #172F6C → blue-600 #2560E6`, con blanco ≥ 5,4:1 en todo el recorrido) y deja el gradiente de marca para acentos sin texto (logo, subrayado de 2 px, íconos). Lo verifica el test de [HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md) |

---

## Recomendaciones fuera del encargo

1. **Arreglar ya el contraste de los estados y de la CTA** ([HU-DS-01](hu/HU-DS-01-tokens-v2.md) + [HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md), unos 2 días). Son
   los dos hallazgos que hoy incumplen una regla escrita (`DESIGN.md` y la DoD común): afectan a
   cada badge y al botón principal de varias pantallas (texto blanco sobre cyan, 2,0:1).
2. **Alinear ADR-APP-04 con el código.** El ADR dice "TanStack Query para lecturas admin", pero
   `package.json` no lo tiene: las pantallas admin hacen fetch a mano. O se instala (y las pantallas
   heredan caché, reintentos y skeletons) o se enmienda el ADR. Se recomienda instalarlo en
   [HU-DS-11](hu/HU-DS-11-shell-del-panel-en-la-app.md), que de todos modos toca esas pantallas.
3. **Íconos propios por sección de Cobranza** (12 de 14 usan `HandCoins`). Es requisito para la
   sidebar plegada y además mejora la búsqueda visual con la barra expandida.
4. **Medir antes de rediseñar.** Registrar dos tiempos hoy, para comparar después: cuánto tarda un
   gestor en registrar un pago (eventos locales de la app) y cuánto tarda un dueño en llegar a
   "Promesas" en el panel. Sin línea base, la métrica de "llegar a una sección" no se puede probar.
5. **Capturas como regresión visual.** Playwright toma capturas de `/catalogo` en claro y oscuro en
   el CI del panel. En la app, el smoke con `adb` en el OPPO ya existe: se guarda una captura por
   vista de campo como evidencia en cada HU.
6. **Formato de cifras por token.** `lib/format.ts` ya formatea en es-CO. Hay que exigir números
   tabulares en toda cifra comparable (KPIs, montos en tablas), que hoy no se aplican.
7. **Modo "alto contraste para campo"** como paso siguiente: una variante del tema claro con texto
   `navy-950` y bordes de 2 px para uso a pleno sol. No entra en esta spec; se evalúa con los gestores
   después de [HU-DS-10](hu/HU-DS-10-cobranza-de-campo-con-el-kit.md).
