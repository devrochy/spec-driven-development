# SPEC-29 · Sistema de diseño unificado y experiencia v2 (panel web + app)

> Estado SDD: Diseño aprobado (2026-10-10, D-32) · Fase 1 · Workstreams UX/Onboarding y App móvil · Dueño: Robinson Aguilar
> · Creada el 2026-10-10

## Problema

El panel (`solvershub-panel/apps/panel-web`) y la app (`solvershub-apk`) ya comparten la paleta de
marca por tokens DTCG (`brand/tokens/tokens.json` → `tokens.css` y `src/core/theme/tokens.ts`), pero
el sistema de diseño se quedó en la paleta. La revisión del código del 2026-10-10 encontró:

| Hallazgo | Evidencia | Consecuencia |
|---|---|---|
| **El contraste de los estados no cumple AA en modo claro**, aunque `DESIGN.md` dice que está verificado | `success #22A06B` da 3,3:1 sobre blanco, `warning #E0A106` 2,3:1 y `danger #D64545` 4,4:1. Hay 135 usos de `text-success/warning/danger` en el panel (los badges incluidos) | Textos de estado ilegibles para baja visión. Incumple la DoD común ("contraste AA") |
| **La CTA con degradado tampoco cumple** | `Button variant="accent"` pone texto blanco sobre `#2F6BFF → #22C7E0`. En el extremo cyan da 2,0:1 | El botón más importante de la pantalla es el menos legible |
| Los tokens no cubren tipografía, elevación, motion ni color de datos | `tokens.json` solo tiene color, gradiente, familias, radios y espacios | Cada pantalla decide tamaños, sombras y duraciones a mano |
| La app no usa los tokens de forma uniforme | 48 archivos `.tsx` con `shColor.*` o hex directos, 58 `StyleSheet.create` sin un kit común | La app y el panel divergen con cada pantalla nueva |
| El shell del panel no se adapta | Sidebar fija de 240 px (`w-60`). No se puede plegar a íconos, no hay migas, no hay paleta de comandos ni atajos de teclado | Con 3 packs y más de 40 secciones, llegar a una sección cuesta 2 a 4 clics |
| El Resumen es igual para todos | 4 `StatCard` sin tendencia, sin período y sin vista por rol (`app/(app)/dashboard/page.tsx`) | El supervisor de cobranza y el operador de la bandeja ven métricas que no son suyas |
| No hay gráficos | El panel no tiene librería de gráficos y la app tampoco | No se pueden mostrar tendencias ([HU-UI-07](../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) pide "gráfico SVG accesible") |
| El panel en la app tiene 8 pestañas abajo | `GRUPOS_PANEL` + "Más" en `src/navigation/PanelShell.tsx` | Las etiquetas se truncan y los blancos táctiles quedan por debajo de 48 dp. Material recomienda de 3 a 5 destinos |

Lo que **funciona y no se toca**: el flujo de campo de cobranza de la app (selección de cartera,
Inicio, Clientes con filtros, Diario, ficha del cliente como overlay con cierre por gesto, préstamo,
menú lateral), probado en calle con más de 490 tests. El dueño pidió explícitamente conservar esas
vistas (D-SPEC-29-6).

## Usuarios y contexto

| Persona | Superficie | Qué necesita del rediseño |
|---|---|---|
| **Dueño / administrador** del negocio | Panel web en escritorio, app en el celular | Saber en 10 segundos si el negocio va bien y llegar a cualquier sección sin conocer el menú |
| **Supervisor** de cobranza | Panel web (oficina) y app (calle) | Carteras, gestores, promesas y alertas del día, con tendencia frente a la semana anterior |
| **Operador** de atención | Panel web, muchas horas al día | Bandeja y escalaciones primero, con atajos de teclado y tablas densas |
| **Gestor** de campo | App Android de gama media (smoke en OPPO), sol directo, una mano, conexión intermitente | El mismo flujo de siempre, más legible y con el estado de sincronización siempre visible |
| **Master** de plataforma | Panel web | Negocios, DLQ y plataforma, sin que eso ensucie la vista de los demás |

## Por qué importa (valor empresarial)

- **Ventas.** La primera impresión en una demo es el Resumen y el menú. Un panel que se ve armado
  por partes pierde frente a Respond.io, SleekFlow o Zendesk aunque el motor sea mejor.
- **Retención.** Un dashboard por rol con tendencias muestra el valor del plan cada semana. Si el
  dueño no ve el valor, no renueva.
- **Costo de construir.** Un kit con variantes y estados documentados recorta el tiempo de cada
  pantalla nueva de [SPEC-13](../SPEC-13-vistas-profesionales/spec.md), 15, 16 y 18, y evita rehacer la consistencia en cada PR.
- **Riesgo legal y comercial.** WCAG 2.2 AA es requisito en las licitaciones grandes y en el
  documento de seguridad para enterprise (`solvershub-comercial/security.md`). Hoy no se cumple en
  los estados.
- **Diferencial.** La app de campo de cobranza es el diferencial casi único (D-02). Llevarla al
  mismo lenguaje visual del panel, sin tocar su flujo, la vende como parte de una sola plataforma.

## Alcance

| HU | Qué | Repo |
|---|---|---|
| [HU-DS-01](hu/HU-DS-01-tokens-v2.md) | Tokens v2: estados por tema con AA, escala tipográfica, elevación, motion y paleta de datos validada | panel (`brand/`) + apk (sync) |
| [HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md) | Contraste AA real y gates del sistema de diseño en CI | panel + apk |
| [HU-DS-03](hu/HU-DS-03-kit-de-componentes-panel.md) | Kit de componentes v2 del panel y catálogo vivo | panel |
| [HU-DS-04](hu/HU-DS-04-shell-adaptativo-del-panel.md) | Shell adaptativo: sidebar expandida, plegada o cajón, migas y pestañas de sección | panel |
| [HU-DS-05](hu/HU-DS-05-paleta-de-comandos-y-atajos.md) | Paleta de comandos (Ctrl/⌘ K) y atajos de teclado | panel |
| [HU-DS-06](hu/HU-DS-06-primitivas-de-visualizacion.md) | Primitivas de visualización (sparkline, tendencia, barras, tabla alternativa) | panel + apk |
| [HU-DS-07](hu/HU-DS-07-resumen-modular-por-rol.md) | Resumen modular por rol (bento) con KPIs, tendencias, actividad, alertas y acciones | panel |
| [HU-DS-08](hu/HU-DS-08-widgets-reorganizables.md) | Widgets reorganizables y preferencias del Resumen | panel |
| [HU-DS-09](hu/HU-DS-09-kit-de-componentes-app.md) | Kit de componentes de la app sobre tokens v2 | apk |
| [HU-DS-10](hu/HU-DS-10-cobranza-de-campo-con-el-kit.md) | Cobranza de campo con el kit nuevo y las mismas vistas | apk |
| [HU-DS-11](hu/HU-DS-11-shell-del-panel-en-la-app.md) | Shell del panel en la app: header con hamburguesa y cajón lateral como el panel web, tema oscuro por defecto (D-34) | apk |
| [HU-DS-12](hu/HU-DS-12-motion-y-microinteracciones.md) | Motion y microinteracciones en panel y app | panel + apk |
| [HU-DS-13](hu/HU-DS-13-resumen-movil-por-rol.md) | Resumen móvil por rol con los widgets del panel | apk |

El cómo está en [design.md](design.md) y el orden en [tasks.md](tasks.md).

## Escenarios clave (Gherkin)

- **Estados legibles.** Dado el modo claro, cuando veo un badge "En mora", entonces su texto tiene
  contraste ≥ 4,5:1 y lleva ícono además del color.
- **Sidebar plegable.** Dado un escritorio de 1280 px, cuando pliego la barra lateral, entonces queda
  en 72 px con íconos y tooltips, y al recargar la página sigue plegada sin parpadeo.
- **Ir a cualquier parte.** Dado que estoy en cualquier sección, cuando pulso Ctrl+K y escribo
  "prom", entonces veo "Cobranza › Promesas" (si tengo permiso) y llego con Enter.
- **Resumen por rol.** Dado un colaborador que solo tiene permisos de conversaciones y
  escalaciones, cuando entra al Resumen, entonces ve los widgets de atención y no ve costos ni
  cobranza.
- **Campo intacto.** Dado un gestor con dos carteras, cuando entra a la app después del rediseño,
  entonces el menú lateral sigue mostrando Inicio, Carteras, Clientes (con sus filtros) y Diario, y
  registrar un pago sin conexión sigue tomando los mismos pasos.
- **Menos movimiento.** Dado un usuario con "reducir movimiento" activado, cuando abre un diálogo,
  entonces aparece sin animación en el panel y en la app.

## Decisiones

### D-SPEC-29-1 · Relación con SPEC-12, SPEC-13 y SPEC-25

| Opción | Pros | Contras |
|---|---|---|
| **A. SPEC-29 es la base visual y las demás la consumen** ([SPEC-12](../SPEC-12-arquitectura-de-informacion/spec.md) define el contenido del menú, [SPEC-13](../SPEC-13-vistas-profesionales/spec.md) las vistas y SPEC-29 tokens, kit, shell y Resumen) | Cada spec conserva un solo tema. [HU-UI-07](../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) queda como contrato de datos (endpoint con período) y la UI del Resumen la hace [HU-DS-07](hu/HU-DS-07-resumen-modular-por-rol.md) | Hay que coordinar el orden: [HU-DS-03](hu/HU-DS-03-kit-de-componentes-panel.md) antes de [HU-UI-08](../SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md) |
| B. Meter todo en [SPEC-13](../SPEC-13-vistas-profesionales/spec.md) | Un solo lugar | [SPEC-13](../SPEC-13-vistas-profesionales/spec.md) pasa de 10 a 22 HU y mezcla vistas con fundamentos |
| C. Hacer [SPEC-13](../SPEC-13-vistas-profesionales/spec.md) primero y el sistema de diseño después | Valor visible antes | Se construyen 10 vistas con el kit viejo y después se rehacen |

**Recomendación: A.** [HU-UI-07](../SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) se reduce a datos (endpoint `GET /admin/dashboard?period=` y series)
y [HU-UI-08](../SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md) usa la `DataTable` v2 de [HU-DS-03](hu/HU-DS-03-kit-de-componentes-panel.md). Estado: ✅ tomada (D-32).

### D-SPEC-29-2 · Librería de gráficos

| Opción | Pros | Contras |
|---|---|---|
| **A. Primitivas SVG propias sobre `d3-scale` y `d3-shape`**, con `react-native-svg` en la app | La misma geometría y las mismas reglas en panel y app. Unos 15 KB gz. Control total de accesibilidad (tabla alternativa, foco por punto) y de los tokens | Hay que construir 4 primitivas (sparkline, línea/área, barras, dona de progreso) |
| B. Recharts en el panel y Victory Native en la app | Rápido de empezar | Dos APIs y dos estilos que mantener. Recharts suma unos 100 KB gz y su accesibilidad es limitada |
| C. ECharts en el panel y en un webview en la app | Muy completo | Pesado. Un webview en Android de gama media es lento y no sigue el tema |

**Recomendación: A.** El panel solo necesita 4 formas (la regla de dataviz: si es un número solo,
va como tile y no como gráfico). Estado: ✅ tomada (D-32).

### D-SPEC-29-3 · Documentación viva de componentes

| Opción | Pros | Contras |
|---|---|---|
| **A. Ruta interna `/catalogo` del panel**, visible solo en desarrollo y en test (`PANEL_CATALOGO=1`) | Sin dependencias. Usa el mismo Next, los mismos tokens y el mismo tema. Sirve para capturas y para axe | No tiene addons como Storybook |
| B. Storybook | Estándar de la industria, addons de accesibilidad | Otro build con Next 16 y Tailwind v4 que mantener, para un equipo de una persona |
| C. Solo `DESIGN.md` | Cero costo | No se ven los estados. La deriva vuelve |

**Recomendación: A.** En la app, el equivalente es una pantalla "Catálogo" solo en builds de
desarrollo. Estado: ✅ tomada (D-32).

### D-SPEC-29-4 · Dónde se guardan las preferencias del shell y del Resumen

| Opción | Pros | Contras |
|---|---|---|
| **A. Cookie para el estado de la sidebar** (el servidor la lee y no hay salto al cargar, como `panel_pasos_plegados`) **y `localStorage` por usuario y negocio para el orden de widgets**. Endpoint de preferencias más adelante | Sin backend nuevo. Sin parpadeo de layout. Mismo patrón que ya usa el panel | Las preferencias no viajan entre dispositivos |
| B. Endpoint `PUT /admin/me/preferences` desde el día uno | Viajan entre web y app | Migración, RLS y API para algo cosmético |
| C. Todo en `localStorage` | Lo más simple | En SSR la sidebar aparece expandida y salta a plegada (CLS) |

**Recomendación: A.** El encargo pide `localStorage`. Para la sidebar se cambia a cookie porque el
panel renderiza en el servidor y `localStorage` produce un salto visible. Estado: ✅ tomada (D-32).

### D-SPEC-29-5 · Navegación del panel dentro de la app

> **Reemplazada por D-34 (2026-10-14):** el panel dentro de la app lleva header con hamburguesa y cajón
> lateral con la misma lista agrupada que el sidebar del panel web, y la app arranca en tema oscuro.
> La tabla de abajo se conserva como historial.

| Opción | Pros | Contras |
|---|---|---|
| **A. 4 destinos + "Más"**: Inicio, Atención, el pack principal del negocio (Cobranza, Comercio o Agenda, el primero habilitado) y Buscar. El resto va en Más | Cumple la guía de 3 a 5 destinos. Etiquetas completas. Blancos de 48 dp | Lo que hoy es pestaña pasa a estar a dos toques |
| B. Cajón lateral como en el campo | Una sola convención en toda la app | Esconde las secciones más usadas detrás de un gesto |
| C. Mantener 8 pestañas | Sin cambio | Etiquetas truncadas y blancos pequeños |

**Recomendación: A.** El campo mantiene su cajón (D-SPEC-29-6) porque allí el gestor trabaja una
cartera a la vez y las secciones van anidadas. Estado: ✅ tomada (D-32).

### D-SPEC-29-6 · Qué pasa con las vistas de campo de cobranza

| Opción | Pros | Contras |
|---|---|---|
| **A. Conservar vistas, flujo, rutas y lógica. Solo se cambian los componentes visuales por los del kit** | Cero riesgo para el diferencial. Los gestores no tienen que volver a aprender la app. Los 490+ tests siguen siendo la red | Cambios estructurales de UX que pudieran ayudar quedan fuera |
| B. Rediseñar el campo con pestañas abajo | Coherente con el panel móvil | Rompe la memoria muscular de los gestores en calle y arriesga regresiones |

**Recomendación: A**, elegida por el dueño el 2026-10-10 ("mantengamos la idea de las vistas que existían para la
cobranza"). Aplica también a la cobranza admin de la app (`CobranzaAdminScreen` con sus pestañas
por sección). Estado: ✅ tomada.

### D-SPEC-29-7 · Cómo se decide el Resumen de cada rol

| Opción | Pros | Contras |
|---|---|---|
| **A. Perfil derivado de los permisos** (ADR-0047): dueño si es owner o master, supervisor si tiene escritura en secciones de un pack, operador si solo tiene atención. Cada perfil trae un layout por defecto que el usuario puede ajustar | Sin roles nuevos en el backend. Nunca muestra un widget sin permiso | La regla de derivación hay que documentarla y probarla |
| B. Roles fijos nuevos (admin, supervisor, operador) | Fácil de explicar | Duplica el RBAC por sección que ya existe |
| C. Cada usuario arma su Resumen desde cero | Flexible | Un usuario nuevo encuentra el Resumen vacío |

**Recomendación: A.** Estado: ✅ tomada (D-32).

### D-SPEC-29-8 · Plataforma de la app

| Opción | Pros | Contras |
|---|---|---|
| **A. Seguir con Expo (React Native)** | Motor offline con cola idempotente, SQLCipher, push y OTA ya en producción. Más de 490 tests. TypeScript compartido con el panel | Hay que cuidar el rendimiento de listas largas |
| B. Flutter | Buen rendimiento y control del render | Reescribir unas 23k líneas y perder los tests. Dart no comparte nada con el panel |
| C. PWA empaquetada | Un solo código con el panel | GPS en segundo plano, SQLCipher, Keystore y push confiables en Android quedan limitados |

**Recomendación: A**, elegida en [SPEC-25](../SPEC-25-app-movil-oficial/spec.md) (D-SPEC-25-1). Se registra aquí porque el encargo pide justificarla.
Estado: ✅ tomada.

### D-SPEC-29-9 · Estilo de superficies del Resumen

| Opción | Pros | Contras |
|---|---|---|
| **A. Bento con superficies sólidas, 3 niveles de elevación por token y un solo acento (cyan para datos)** | Contraste predecible en claro y oscuro. Barato de pintar en Android de gama media | Menos "llamativo" en una captura |
| B. Glassmorphism (blur y transparencia) | Moderno en una demo | El contraste depende de lo que hay detrás, así que AA no se puede garantizar. `backdrop-filter` es caro en móviles de gama media |

**Recomendación: A.** El encargo pide "glassmorphism sobrio"; se descarta porque choca con la
restricción de accesibilidad del mismo encargo y con el principio "instrumento calmado" de
`DESIGN.md`. Estado: ✅ tomada (D-32).

## Fuera de alcance

- El contenido y los nombres del menú: son de [HU-UX-02](../SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) ([SPEC-12](../SPEC-12-arquitectura-de-informacion/spec.md)). Esta spec cambia el contenedor,
  no las etiquetas.
- Las vistas nuevas de [SPEC-13](../SPEC-13-vistas-profesionales/spec.md) (bandeja, tickets, configuración por pestañas): las construye [SPEC-13](../SPEC-13-vistas-profesionales/spec.md)
  con el kit de esta spec.
- Cambios de flujo, rutas o lógica del campo de cobranza (D-SPEC-29-6).
- Internacionalización a otro idioma: todo sigue en español de Colombia. Las cadenas siguen
  centralizadas en `lib/labels.ts` y en los módulos de la app, para no cerrarle el paso.
- iOS (sigue en [SPEC-25](../SPEC-25-app-movil-oficial/spec.md)) y la landing (`solvershub-landing`).
- Preferencias sincronizadas entre dispositivos (D-SPEC-29-4, opción B, queda para después).

## Métricas de éxito

| Métrica | Meta | Cómo se mide |
|---|---|---|
| Contraste | 100 % de los pares texto/fondo de los tokens ≥ 4,5:1 (texto) y ≥ 3:1 (no texto) | Test de contraste sobre `tokens.json` en CI ([HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md)) |
| Accesibilidad del panel | 0 violaciones `serious` o `critical` de axe en `/catalogo` y en las 10 páginas principales | Job de CI de [HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md) |
| Deriva visual de la app | 0 hex sueltos fuera de `src/core/theme` | Regla de lint de [HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md) |
| Llegar a una sección | Mediana ≤ 3 s con Ctrl+K frente a la navegación con el menú | Prueba moderada con 5 usuarios (dueño, supervisor, operador) |
| Campo sin regresión | Tests verdes y mismos pasos para registrar un pago sin conexión | CI de la app + smoke en el OPPO ([HU-DS-10](hu/HU-DS-10-cobranza-de-campo-con-el-kit.md)) |
| Rendimiento del Resumen | LCP ≤ 2,5 s en test. Hasta 40 KB gz de JS extra frente a hoy | `web-perf` sobre el Resumen y `next build` |
| Uso del Resumen | ≥ 60 % de los dueños activos lo abren al menos 3 días por semana | Eventos del panel (si existen) o logs del BFF |

## Requerimientos cubiertos

REQ-UX-09, REQ-UX-10, REQ-UX-11 y REQ-APP-11 (nuevos), más REQ-UX-06 (panel responsive y accesible)
en [HU-DS-02](hu/HU-DS-02-contraste-aa-y-gates.md) y [HU-DS-04](hu/HU-DS-04-shell-adaptativo-del-panel.md).
