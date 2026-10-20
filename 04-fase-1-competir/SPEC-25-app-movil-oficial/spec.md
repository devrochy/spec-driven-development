# SPEC-25 · App móvil oficial (el APK de cobranza se convierte en la app de todo SolversHub)

> Estado SDD: En ejecución · Fase 1 · Workstream App móvil

## Problema

El repo `solvershub-apk` es una app de campo de cobranza excelente (Expo SDK 57, TypeScript strict,
~23k LOC, 490 tests verdes, cola offline idempotente con ack por evento, contrato v2 camelCase con
`api_gestor` del backend) pero sirve a un solo rol: el gestor. El panel web (`solvershub-panel`)
tiene 4 grupos core (Operación, Configuración, Negocio, Herramientas) + Plataforma y 3 packs
(Cobranza con 16 secciones, Comercio, Calendario) que el dueño y sus colaboradores solo pueden
operar desde el escritorio. No existe una app móvil oficial de SolversHub: el dueño no puede ver
conversaciones, pedidos, citas o el estado del negocio desde el teléfono, y el gestor no puede salir
de su vertical.

## Por qué importa (valor empresarial)

La cobranza con APK es el diferencial casi único del mercado (decisión D-02) y la app de campo ya
está probada en calle. Convertirla en la app oficial (a) protege ese diferencial al darle un hogar
arquitectónico estable, (b) le vende movilidad al panel completo como argumento de venta frente a
la matriz, y (c) unifica auth, marca, offline y notificaciones en una sola base de código y un solo
release — un APK para todo el panel, con módulos visibles según permisos y sin regresiones en
cobranza.

## Alcance

| HU | Qué |
|---|---|
| [HU-APP-01](hu/HU-APP-01-nucleo-modular-de-la-app.md) | Núcleo modular: reestructura por módulos con fronteras, core/shared/data, ADR-APP-01..06 |
| [HU-APP-02](hu/HU-APP-02-sesion-unica-y-recuperacion.md) | Sesión única (login admin + `gestor-token`), recuperación de contraseña y biometría |
| [HU-APP-03](hu/HU-APP-03-navegacion-por-permisos.md) | Navegación compuesta por permisos y roles (field shell vs panel shell) |
| [HU-APP-04](hu/HU-APP-04-dashboard-con-kpis.md) | Dashboard móvil con KPIs del negocio |
| [HU-APP-05](hu/HU-APP-05-notificaciones-push.md) | Notificaciones push (Expo) para eventos del negocio y de campo |
| [HU-APP-06](hu/HU-APP-06-almacenamiento-local-cifrado.md) | Almacenamiento local cifrado (expo-sqlite + SQLCipher) y migración desde AsyncStorage |
| [HU-APP-07](hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md) | Cobranza migrada al nuevo núcleo sin regresión (campo completo + autovinculación de dispositivo) |
| [HU-APP-08](hu/HU-APP-08-operacion-movil.md) | Operación móvil: conversaciones (con acciones), escalaciones y leads |
| [HU-APP-09](hu/HU-APP-09-negocio-movil.md) | Negocio móvil: plan y consumo, costos LLM y suscripción |
| [HU-APP-10](hu/HU-APP-10-comercio-movil.md) | Comercio móvil: productos, categorías, promociones y pedidos |
| [HU-APP-11](hu/HU-APP-11-calendario-movil.md) | Calendario móvil: citas, tipos, bloqueos y horario |
| [HU-APP-12](hu/HU-APP-12-configuracion-movil.md) | Configuración móvil: colaboradores, habilidades, conexiones y ajustes |
| [HU-APP-13](hu/HU-APP-13-herramientas-y-plataforma-movil.md) | Herramientas y plataforma móvil: asistente, plantillas, DLQ y negocios (solo master) |
| [HU-APP-14](hu/HU-APP-14-busqueda-global.md) | Búsqueda global unificada con resultados por sección |
| [HU-APP-15](hu/HU-APP-15-sync-offline-por-modulos.md) | Sincronización offline-first por módulos (cursor incremental + escrituras encoladas) |
| [HU-APP-16](hu/HU-APP-16-seguridad-de-la-app.md) | Seguridad: certificate pinning y hardening OWASP MASVS L1 |
| [HU-APP-17](hu/HU-APP-17-release-firmado-y-guias.md) | Release firmado y reproducible (dev/staging/prod) con guías de build |
| [HU-APP-18](hu/HU-APP-18-cobranza-admin-movil.md) | Cobranza admin móvil: réplica total del pack (resumen, clientes, promesas, dispositivos, auditoría) |
| [HU-APP-19](hu/HU-APP-19-cobranza-admin-profunda.md) | Cobranza admin profunda: cartera (caja, liquidación, ruta optimizada), reportes, monitoreo, reglas y alertas |
| [HU-APP-20](hu/HU-APP-20-escrituras-moviles.md) | Escrituras móviles: crear productos/categorías/promociones, tipos y bloqueos de agenda, invitar colaboradores |
| [HU-APP-21](hu/HU-APP-21-herramientas-profunda.md) | Herramientas profundas: playground, plan/purga, plantillas Meta, opt-out de push y deep links de búsqueda |

## Métricas de éxito

| Métrica | Meta | Cómo se mide |
|---|---|---|
| Un solo APK sirve para todo el panel | 100 % de las secciones del panel accesibles desde la app según permisos | Inventario de secciones de `nav.ts` del panel vs módulos de la app en [HU-APP-13](hu/HU-APP-13-herramientas-y-plataforma-movil.md) |
| Cobranza sin regresiones | 490+ tests verdes + smoke E2E Maestro (login→diario→pago offline→sync) | CI del repo APK en [HU-APP-07](hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md) |
| Módulos según permisos | 0 pantallas accesibles sin permiso | Test por rol (master/owner/colaborador/gestor) en [HU-APP-03](hu/HU-APP-03-navegacion-por-permisos.md) |
| Conexión intermitente | Escrituras encoladas se sincronizan con ack y sin duplicados | E2E offline de [HU-APP-07](hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md) y [HU-APP-15](hu/HU-APP-15-sync-offline-por-modulos.md) |
| Build reproducible | Mismo commit → mismo AAB firmado por EAS | Guía y runbook de [HU-APP-17](hu/HU-APP-17-release-firmado-y-guias.md) |

## Requerimientos cubiertos

REQ-APP-01..10 (nuevos, ver `02-vision-y-decisiones/requerimientos.md`), más REQ-PLUS-04
(cobranza con APK, en [HU-APP-07](hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md)) y REQ-ARCH-16 (APK lista para producción, en [HU-APP-17](hu/HU-APP-17-release-firmado-y-guias.md)).

## Decisiones

### D-SPEC-25-1 · Cómo se estructura la app para crecer de 1 a 10 módulos

| Opción | Pros | Contras |
|---|---|---|
| **A. Monolito modular en un solo proyecto Expo (`src/modules/*`) con fronteras duras verificadas en CI (ADR-APP-01)** | Un solo release y una sola auth; reuso total de core/shared; la regla "ningún módulo importa de otro" detecta acoplamientos; migrar de aquí a multi-paquete después es barato | Los módulos comparten versión de librerías; exige disciplina de fronteras |
| B. Monorepo multi-paquete (un paquete npm por módulo) | Versionado y builds independientes por módulo | Fricción de Metro y versionado para un solo desarrollador; sin beneficio en managed workflow |
| C. Dos apps (campo + panel móvil) | Cada app más chica | Viola el requisito "un solo APK para todo el panel"; duplica auth, tema y release |

**Recomendación: A.** Se registra en ADR-APP-01.

### D-SPEC-25-2 · Qué navegador se usa para componer 10 módulos y deep links

| Opción | Pros | Contras |
|---|---|---|
| **A. Mantener React Navigation 7, un navigator por módulo compuesto en `AppNavigator`, shell armado por permisos y deep links vía `linking` (ADR-APP-02)** | Cero regresión en cobranza; patrón "navigator por módulo" refuerza el contrato; permisos aplicados en un solo lugar | Tipos de rutas por módulo que mantener |
| B. Migrar a expo-router | Routing por archivos estilo Next, paridad mental con el panel | Reescribir navegación y 13 pantallas con riesgo en cobranza; deep links no justifican el costo |

**Recomendación: A.** Se registra en ADR-APP-02.

### D-SPEC-25-3 · Cómo se resuelve "panel + campo" con una sola sesión

| Opción | Pros | Contras |
|---|---|---|
| **A. Un solo login admin y un endpoint `POST /api/v1/pack/cobranza/gestor-token` que intercambia a JWT de gestor validando rol, carteras y dispositivo (ADR-APP-03)** | Una puerta de entrada; permisos calculados en el servidor; el modo campo sigue cumpliendo ADR-0068; recuperación/biometría se implementan una vez | Dos tokens en el cliente; un endpoint más en el backend |
| B. Dos logins separados en la app | Sin endpoint nuevo | Dos entradas de sesión, UX confusa, duplicación de recuperación y biometría |
| C. Emitir el JWT de gestor dentro del login admin | Menos pasos | Acopla el core al pack de cobranza (invariante 5 del backend) |

**Recomendación: A.** Se registra en ADR-APP-03.

### D-SPEC-25-4 · Cómo se maneja el estado del servidor y el offline

| Opción | Pros | Contras |
|---|---|---|
| **A. TanStack Query para lecturas admin + el motor offline propio (cola idempotente + sync por cursor) para campo y escrituras críticas (ADR-APP-04)** | Cada módulo usa la herramienta justa; el motor de campo probado queda intacto; pantallas nuevas heredan caché/skeletons | Una dependencia nueva; regla de no mezclar motores en una pantalla |
| B. Solo TanStack Query con persistencia genérica | Menos código | Pierde idempotencia y ack por evento del campo |
| C. Solo el motor propio para todo | Sin dependencias | Reimplementar paginación/invalidación a mano en 10 módulos |

**Recomendación: A.** Se registra en ADR-APP-04.

### D-SPEC-25-5 · Dónde viven los datos locales y cómo se cifran

| Opción | Pros | Contras |
|---|---|---|
| **A. expo-sqlite con SQLCipher (`useSQLCipher: true`), clave en SecureStore con `requireAuthentication`, migración AsyncStorage vía `sqlcipher_export` (ADR-APP-05)** | Cumple REQ-APK-021; consultas reales para sync y búsqueda local; clave en Keystore/Keychain | Sin Expo Go para datos (dev client, que ya es el flujo); `PRAGMA key` por conexión |
| B. AsyncStorage + cifrado manual | Sin migración | Frágil, sin consultas, sin garantías criptográficas |
| C. WatermelonDB o Realm | APIs relacionales cómodas | Motores pesados, mantenimiento incierto, fricción con New Architecture |

**Recomendación: A.** Se registra en ADR-APP-05.

### D-SPEC-25-6 · De dónde salen los tipos de la API en la app

| Opción | Pros | Contras |
|---|---|---|
| **A. Extender `scripts/export_openapi.py` del backend para incluir `/api/pack/pack_cobranza` y generar un único `schema.d.ts` con `openapi-typescript` (ADR-APP-06)** | Una fuente de verdad; el typecheck de la app detecta cambios de contrato; mismo mecanismo que el panel | Mantener el exportador; el OpenAPI crece |
| B. Mantener `src/types/gestor.ts` a mano | Sin cambios | Es la causa del desfase actual y no escala a 10 módulos |

**Recomendación: A.** Se registra en ADR-APP-06.

## Riesgos y notas

- **Regresión en cobranza** es el riesgo #1: [HU-APP-07](hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md) mueve archivos sin cambiar comportamiento,
  con la suite de 490 tests como red y un smoke E2E (Maestro) antes y después.
- **Réplica total del panel** es alcance grande: el orden de ejecución empieza por los módulos de
  lectura (operación, negocio) y deja configuración compleja (conexiones Meta, plataforma) al final,
  con adaptaciones móviles (OAuth por browser/webview, checkout por webview).
- **Push** depende de credenciales del proyecto Expo (el projectId de EAS ya existe y no se renombra).
- **Pinning** vs rotación de certificados: doble pin y override por perfil de build ([HU-APP-16](hu/HU-APP-16-seguridad-de-la-app.md)).
- El propietario usa la app para el panel y, si además es gestor, el modo campo; el login sigue el
  contrato ADR-0081 (membresías múltiples → selección de negocio).

## Fuera de alcance

- Sucursales como entidad nueva: la segmentación sigue siendo negocio (tenant) + cartera + permisos.
- iOS en esta fase: el proyecto queda iOS-ready (Expo compila ambos) pero el release es Android primero.
- Procesamiento de pagos nativo (tarjetas): se reutiliza link de pago/Wompi existente vía webview.
- App pública de clientes finales (solo chat web/widget), que es otra superficie.
