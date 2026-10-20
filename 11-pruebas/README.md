# 11 · Pruebas

Control de pruebas de SolversHub: qué se prueba en cada requerimiento, qué falta configurar en test y qué hay que
validar para pasar a producción.

| Qué | Dónde | Cómo se versiona |
|---|---|---|
| **Catálogo** (pruebas paso a paso, configuraciones y variables) | [catalogo.yaml](catalogo.yaml) | Con git: cada cambio entra en un PR de docs |
| **Resultados** (pasos, notas, capturas, informes por tester) | Plataforma › Pruebas del panel de test ([SPEC-30](../04-fase-1-competir/SPEC-30-centro-de-pruebas/spec.md)). **Única fuente de verdad desde el ciclo «2026-10-13 · catálogo v5»**; el artifact «Camino a producción» (`https://claude.ai/artifact/P2spcrvuTNGZXf2xEEqgLn`) queda de solo lectura ([HU-QA-05](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-05-migrar-desde-el-artifact.md)) | Por **ciclo**: al cerrarlo queda una foto fija con la versión del catálogo; la lectura de cada ciclo va en [informes/](informes/) |

## El catálogo

Cada fila tiene un `id` estable (minúsculas, números y guiones; no se reutiliza ni se cambia: es lo que une la
historia de una prueba entre versiones), una `seccion` y su contenido:

| `seccion` | Para qué | Campos obligatorios |
|---|---|---|
| `pruebas` | Algo que un tester ejecuta paso a paso y da OK, Falla o Bloqueada | `grupo`, `titulo`, `pasos` y, si algún paso no trae su resultado, `esperado` |
| `test` | Una configuración que falta en el entorno de test | `grupo`, `titulo`, `porque`, `como` |
| `prod` | Un punto a validar antes de pasar a producción | `grupo`, `titulo`, `porque`, `como` |
| `datos` | La guía de datos: qué es un dato externo, para qué sirve y cómo conseguirlo (tarjeta de Wompi, correo con alias, celular autorizado…) | `grupo`, `titulo`, `porque`, `como` |

Desde la **v6** cada prueba lleva además `entorno` y `area` (obligatorios):

| Campo | Qué lleva |
|---|---|
| `entorno` | Dónde se ejecuta: `panel`, `apk`, `whatsapp`, `web` o `api` |
| `area` | La sección donde se ejecuta: en el panel, la de su menú (Conversaciones, Colaboradores, Cobranza, Calendario…); en la APK, su pantalla (Campo (gestor), Cobranza del dueño, Agenda…). La lista cerrada por entorno está en `QA_AREAS` de `herramientas/regenerar.py` y su orden es el de la lista lateral |
| `requiere` | Los `id` de la sección `datos` que la prueba necesita; el panel los enlaza desde el encabezado de la prueba |

Campos opcionales de una prueba (esquema v2, compatible con v1):

| Campo | Qué lleva |
|---|---|
| `modulo` | Panel, App móvil (dueño), App de campo (gestor), Cobranza, Asistente y WhatsApp, Cobros y suscripciones, Comercio, Agenda, Plataforma o Landing |
| `prioridad` | `P0` (humo: se corre en cada release), `P1` o `P2` |
| `plataforma` | Uno o varios de `panel`, `app`, `whatsapp`, `web`, `api`, `correo` |
| `contexto` | Qué se construyó y por qué, en una o dos frases, para un tester sin historia del proyecto |
| `precondiciones` | Lista de lo que tiene que estar listo antes (negocio, sesión, datos) |
| `datos` | Cuentas, teléfonos o montos de test a usar. **Nunca contraseñas ni tokens.** Las cuentas se nombran desde el tester: «Tu dueño de prueba», «Tu gestor de prueba», «Tu colaborador de prueba», «Tu negocio de prueba» (los crea Pruebas › Datos de prueba) o «Tu cuenta de tester». Las cuentas demo (`master@demo.test`, `dueno-a@demo.test`, `gestor@demo.test`) son del equipo interno y no se citan |
| `pasos` | Lista de pasos. En v2 cada paso es `{accion, esperado}`; un paso en texto (v1) sigue valiendo y usa el `esperado` general |
| `esperado` | Resultado final de la prueba |
| `hu` | Las HU que cubre |
| `origen` | De dónde sale si no es de una HU: `PLAN-DE-PRUEBAS:AUTH-03`, `guia-0A:§7` |
| `quien` | Quién la corre normalmente (Tester, Dueño, Claude) |

Ejemplo v2:

```yaml
- id: pruebas-ir-a-una-seccion-con-ctrl-k
  seccion: pruebas
  modulo: Panel
  grupo: Navegación y paleta
  titulo: Ir a una sección con Ctrl+K
  prioridad: P0
  plataforma: panel
  contexto: La paleta de comandos (SPEC-29) lleva a cualquier sección sin usar el menú.
  precondiciones: [Sesión iniciada en el panel de test con un negocio de cobranza]
  pasos:
  - accion: Pulsar Ctrl+K desde cualquier página.
    esperado: Se abre la paleta con el foco en la búsqueda.
  - accion: Escribir «prom».
    esperado: Aparece Cobranza › Promesas como primer resultado.
  - accion: Pulsar Enter.
    esperado: Llega a Promesas y el foco vuelve a la página.
  hu: [HU-DS-05]
```

`version` sube en 1 con cada cambio del catálogo, y `fecha` dice cuándo. `herramientas/regenerar.py --check` (CI)
valida el archivo: ids únicos y bien formados, campos por sección, pasos, valores de `modulo`, `prioridad`,
`plataforma`, `entorno` y `area`, que cada `requiere` apunte a la sección `datos` y que las HU citadas existan.

## Regla de trabajo

Cada HU que agrega o cambia comportamiento actualiza, **en el mismo PR de docs**:

1. Sus pruebas en `catalogo.yaml` (nuevas o con pasos corregidos), con el `id` de la HU en `hu`.
2. Las configuraciones de test que pide y las variables o cuentas que va a necesitar producción.
3. La `version` del catálogo.

Después de mergear se importa en el panel (`agent-core qa importar 11-pruebas/catalogo.yaml`) y el ciclo abierto
muestra las pruebas nuevas sin correr.

## Cómo se ejecuta (panel de test)

1. El dueño invita al tester desde Plataforma › Pruebas › Testers; le llega un correo con un enlace de un solo uso.
2. El tester entra con permisos de master; en Colaboradores actúa como **dueño del negocio activo** (no crea
   masters ni toca cuentas de plataforma). El rol solo existe en test.
3. En **Datos de prueba** pulsa «Preparar mis datos»: se crea su negocio «QA · …» con Comercio, Agenda y Cobranza,
   productos, citas y una cartera con clientes al día, en mora y sin préstamo, más sus cuentas de dueño, gestor y
   colaborador (contraseñas visibles una sola vez). La misma pestaña tiene la guía de los datos externos.
4. En Ejecutar elige una prueba de la lista lateral, agrupada por entorno (Panel, APK, WhatsApp, Web, API) y por
   sección, con filtros por estado, entorno, sección y prioridad P0. La
   corre paso a paso: Aprobar, Falla, Bloqueado u Omitir, con nota y capturas (pegar con Ctrl+V o arrastrar). Todo se
   guarda al instante y la cabecera muestra su avance y el del ciclo.
5. Al terminar pulsa **Enviar informe**: revisa la vista previa, confirma, y su ejecución queda en solo lectura. Al
   dueño le llega un correo con el enlace; el informe se imprime a PDF o se descarga en Markdown.

## Ciclos

Un ciclo agrupa una ronda de pruebas, normalmente una release. Cada tester tiene su propia ejecución dentro del ciclo;
la lista consolida a todos (Falla si alguien la falló, luego Bloqueada, luego OK, luego Sin correr). Al cerrar el ciclo
se guarda la foto de resultados y en el ciclo nuevo las pruebas vuelven a «Sin correr». La configuración de test y
los puntos de producción no se reinician: describen el entorno, no una corrida.

## Informes por ciclo

Cada ciclo deja dos cosas: la foto oficial que guarda el panel al cerrarlo (resumen por tester, informes en Markdown
y PDF) y una **lectura** en este repo, en lenguaje claro, con los defectos reales y su evidencia, lo que es dirección de
producto y a qué HU va, lo que no se corrige y por qué, y qué cambia en el catálogo siguiente. El panel de pruebas es
la única fuente de verdad de los resultados desde el ciclo «2026-10-13 · catálogo v5»; el artifact «Camino a
producción» queda de solo lectura ([HU-QA-05](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-05-migrar-desde-el-artifact.md)).

| Ciclo | Catálogo | Lectura | Estado |
|---|---|---|---|
| 2026-10-13 | v5 (211 pruebas) | [informes/ciclo-2026-10-13.md](informes/ciclo-2026-10-13.md): 168 ejecuciones (106 OK, 27 fallas, 33 bloqueadas), 12 defectos reales, pedidos de producto mapeados a HU y reglas del catálogo v7 | Abierto: faltan enviar las 3 ejecuciones y cerrarlo en `/pruebas/ciclos` |

## Cobertura (catálogo v7, 2026-10-19)

El catálogo documenta todo lo construido desde el inicio del proyecto
([HU-QA-06](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-06-catalogo-historico-del-proyecto.md)). Son 235 pruebas, de las que 43 son de humo (P0) y conviene correrlas en cada release, más 11 fichas de la guía de datos.
La v7 agrega 21 pruebas del Agent OS para testers no técnicos (sección Agentes, consola de Conexiones y conversación
con los agentes en el chat web) y la ficha «Tu negocio de prueba con agentes».

| Entorno | Pruebas | Secciones con más pruebas |
|---|---|---|
| Panel | 131 | Navegación y sesión (22), Conexiones (21), Agentes (12), Calendario (12), Pruebas (10) |
| APK | 48 | Campo (gestor) (16), Sesión y permisos (6), Negocio y configuración (6), Cobranza del dueño (5) |
| WhatsApp | 37 | Asistente (9), Alta automática (9), Suscripciones (6) |
| Web | 14 | Chat web (10), Landing (4) |
| API | 5 | Seguridad (4), Operación (1) |

**De dónde salen** (campo `hu` u `origen` de cada prueba):

- **HU de SDD:** cubre 76 de las 106 HU terminadas o en curso (más [HU-AOS-16](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md), 17, 23, 24 y 47, todavía en borrador). Cada prueba lleva su HU en `hu`.
- **Plan de pruebas anterior a SDD** (`solvershub-comercial/PLAN-DE-PRUEBAS.md` v1.1, 2026-09-28): incluye 114 de sus casos, con el
  ID original en `origen` (`PLAN-DE-PRUEBAS:CONV-03`). Los casos que el plan corría en CI (`REG-*`) no entran. Tampoco entran
  `A11Y-01` (contraste), que lo mide `brand/tokens/contrast.mjs` en el CI del panel, y `TPL-04`, que se reemplaza por
  la creación de plantillas en el panel nuevo.
- **Guía de alta automática del 0A** (§ 1–16, en `origen` como `guia-0A:§n`): la § 11 (evals nocturnas) y la § 17
  (recorrido en producción) no son pruebas a mano y quedan en la guía.

**HU que solo se verifican en CI o en documentos** (sin prueba manual a propósito):

| HU | Por qué |
|---|---|
| [HU-APP-01](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-01-nucleo-modular-de-la-app.md), [HU-APP-06](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-06-almacenamiento-local-cifrado.md) | Estructura de módulos y cifrado de SQLite: tests y revisión de código |
| [HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) | Producción en el VPS: se valida con los puntos `prod-*` del checklist |
| [HU-ARCH-10](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md), [HU-ARCH-27](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-27-turnos-timeout-y-observabilidad.md), [HU-ARCH-28](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md), HU-SUB-12 | Modelo por defecto, timeouts de turno, evals y journeys: CI y evals nocturnas |
| [HU-FWK-02](../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-02-adr-presets.md), HU-SUB-01, [HU-UX-01](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-01-adr-arquitectura-de-informacion.md) | ADR |
| [HU-FWK-13](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FWK-13-plugin-del-tenant.md) | Scaffold de plugins: tests del CLI |
| [HU-GTM-11](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-11-matriz-corregida.md), [HU-REP-05](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-05-repo-solvershub-docs.md) | Matriz competitiva y repo de docs |
| [HU-UI-04](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md) | Tests y control de deriva en el CI del panel |
