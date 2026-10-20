# SPEC-31 · Mejoras del ciclo de pruebas 2026-10-13

> Estado SDD: Diseño aprobado · Fase 1 · Hito 1 · Dueño: el dueño del producto · Nace de [D-38](../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas) (2026-10-19)

## Problema

En el ciclo de pruebas «2026-10-13 · catálogo v5», el dueño (`master@demo.test`) dejó en el centro de pruebas de test:
- 97 notas: 78 de paso y 19 de prueba;
- 2 capturas;
- 1 nota más en el ciclo «Release 2026-10-17».

El [informe del ciclo](../../11-pruebas/informes/ciclo-2026-10-13.md) separó esas notas en tres grupos:
- **12 defectos** (§4): al 2026-10-19 están corregidos y desplegados en test (core #467/#468, panel #79, landing #13).
- **Pedidos de producto** (§5): los repartió en HU del Agent OS.
- **Mejoras de diseño y UX**: las mandó a un «backlog de [SPEC-29](../SPEC-29-sistema-de-diseno-unificado/spec.md)» que el spec no tiene.

Por eso unas 30 mejoras que el dueño pidió con nombre y apellido no tienen dueño en el backlog:
- tres de ellas, «como hoy tenemos en agent-sale»: la bandeja de conversaciones, los clientes y los motivos de escalación;
- el resto, del shell y de las secciones;
- más tres piezas grandes: el centro de notificaciones, el pack de conocimiento (RAG) y el onboarding con guion.

Las notas que más pesan, textuales:

- **Conversaciones:** «nos gustaría que la vista de conversaciones cambie sea al estilo de WhatsApp Web. Además queremos que los mensajes en la conversación se actualicen sin necesidad de refrescar la pantalla». También: «no se está visualizando correctamente las conversaciones de las diferentes conexiones».
- **Leads:** «Esto ya se hace en agent-sale … se puede pausar por cliente el bot, se puede ver la clasificación del cliente, se puede editar … sería bueno tener los leads filtrados de acuerdo a la conexión».
- **Escalaciones:** «El motivo no es muy claro cuando se menciona una tool … Podemos trabajar en los motivos como se hizo en agent-sale».
- **Shell:** el ícono de plegar «al lado del logo»; «avatar y nombre de usuario … con menú flotante para cerrar sesión, cambiar dark o light, abrir perfil»; las pestañas «arriba del título»; «un sistema de notificaciones en el panel y en la apk».
- **Agentes:** «con 10 preguntas se pueda configurar un agente»; «un pack de rag con la posibilidad de adjuntar conocimiento».

## Usuarios y contexto

- **Dueño del negocio:** atiende desde el panel y la app. Quiere ver sus conversaciones en vivo, saber quién es cada cliente y entender por qué el agente escaló.
- **Colaborador:** responde conversaciones y tickets dentro de las secciones que le da su rol (ADR-0047).
- **Master y testers:** prueban en test con el [centro de pruebas](../SPEC-30-centro-de-pruebas/spec.md). Cada nota de este inventario se cierra con una prueba del catálogo en OK.

## Por qué importa (valor empresarial)

[D-35](../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes) vende agentes. Un dueño confía en un agente cuando puede:
- verlo trabajar en vivo;
- intervenir en una conversación;
- entender por qué escaló.

Hoy la bandeja es una tabla que se refresca a mano, los motivos salen como nombres técnicos y los clientes no se pueden editar ni pausar. Eso es lo que más se nota en una demo frente a la competencia, y frente a agent-sale, que el dueño ya usa en producción.

Las mejoras del shell, de los avisos y de los formularios bajan las notas «no es claro», que aparecen 18 veces en la ejecución del dueño. El onboarding con guion y el conocimiento adjunto son lo que pide un negocio nuevo para dejar su agente listo sin ayuda.

## Alcance

| HU | Qué entrega | Talla |
|---|---|---|
| [HU-UX-12](hu/HU-UX-12-arreglos-rapidos-del-ciclo.md) | Arreglos rápidos: tooltip con portal, período de Agentes, «Pagar» en la fila pendiente, una sola paginación, canal legible | S |
| [HU-UX-13](hu/HU-UX-13-avisos-y-formularios-en-espanol.md) | Avisos de 4 tipos con ícono, errores y validaciones en español, ayuda de los campos con teclado y al tocar, mensajes claros al vincular un dispositivo | M |
| [HU-UX-17](hu/HU-UX-17-motivos-de-escalacion-legibles.md) | Motivos de escalación con lista cerrada, etiqueta, color y filtro, y el texto completo a un clic | M |
| [HU-UX-16](hu/HU-UX-16-clientes-estilo-agent-sale.md) | Clientes: pausar el bot por cliente, ficha editable con lo que el agente aprendió, clasificación, filtros por canal y conexión, CSV | L |
| [HU-UX-15](hu/HU-UX-15-bandeja-de-conversaciones.md) | Bandeja de conversaciones estilo WhatsApp Web, en vivo, con la conexión de cada chat y tickets (tomar, resolver, devolver al bot) | L |
| [HU-UX-14](hu/HU-UX-14-shell-v2-y-perfil.md) | Shell v2: plegar junto al logo, bloque de usuario con menú, página de perfil, pestañas sobre el título, Resumen con los indicadores primero, acciones con íconos | M |
| [HU-UX-18](hu/HU-UX-18-listas-y-formularios-de-seccion.md) | Promesas con filtros y detalle, formularios de habilidad por grupos, Cobro de la plataforma, guardrails a la vista, paso «configurar la habilidad» | M |
| [HU-UX-19](hu/HU-UX-19-centro-de-notificaciones.md) | Centro de notificaciones en el panel y la APK | L |
| [HU-AOS-48](hu/HU-AOS-48-onboarding-con-guion-por-agente.md) | Onboarding con guion de ~10 preguntas por tipo de agente, en una ventana al primer ingreso | L |
| [HU-AOS-49](hu/HU-AOS-49-pack-de-conocimiento.md) | Pack de conocimiento (RAG): ADR, ingesta de documentos y búsqueda por agente | L |
| [HU-UX-20](hu/HU-UX-20-apk-lo-que-falto-del-ciclo.md) | APK: búsqueda en Negocios, esqueletos y aviso sin conexión en Inicio, notas de cartera para el admin | M |

**Cambios en specs existentes (sin HU nueva):**
- [HU-AOS-28](../SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md) queda con el depurador y el panel «En curso». La bandeja en vivo pasa a [HU-UX-15](hu/HU-UX-15-bandeja-de-conversaciones.md).
- [HU-AOS-16](../SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md) aclara que las habilidades viven dentro de su pack y no en una lista global del core.
- [HU-AOS-24](../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) anota el costo estimado por mensaje en el selector de modelo.
- [HU-COM-09](../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-09-modificar-pedido.md) recoge la nota «mejorar la interacción del agente» al cancelar o modificar un pedido.

El inventario completo, nota por nota, está en [design.md](design.md#inventario).

## Escenarios clave (Gherkin)

- **Bandeja en vivo.** Dado que tengo abierta la bandeja de conversaciones, cuando un cliente escribe por WhatsApp o por el chat web, entonces el mensaje aparece en el hilo y la conversación sube en la lista sin refrescar la página.
- **Conversación por conexión.** Dado un negocio con dos conexiones de WhatsApp, cuando abro la bandeja, entonces cada conversación muestra el nombre de su conexión y puedo filtrar por una de ellas.
- **Motivo legible.** Dado que el agente escaló porque una herramienta falló o porque el cliente se quejó, cuando abro Escalaciones, entonces veo el motivo en palabras («Queja del cliente», «Acción de Ventas falló») con su color y puedo filtrar por motivo.
- **Pausa por cliente.** Dado un cliente en Clientes, cuando apago su interruptor «Agente», entonces el agente deja de responderle en cualquier conversación hasta que lo vuelva a encender.
- **Ficha que no vuelve a preguntar.** Dado que el agente guardó la dirección de un cliente, cuando abro su ficha, entonces la veo con su origen (agente o persona) y puedo corregirla.
- **Avisos en español.** Dado cualquier formulario del panel, cuando dejo un correo incompleto o guardo con un error del servidor, entonces el mensaje sale en español junto al campo o en un aviso que se cierra solo.
- **Usuario abajo.** Dado el panel abierto, cuando hago clic en mi avatar al pie de la barra lateral, entonces puedo abrir mi perfil, cambiar el tema o cerrar sesión.
- **Notificaciones.** Dado que se generó un reporte o se resolvió un pago, cuando miro la campana del panel o de la app, entonces veo la notificación sin leer y me lleva a lo que pasó.
- **Agente en 10 preguntas.** Dado que entro por primera vez a un negocio nuevo, cuando elijo «agente de cobranza» en la bienvenida, entonces respondo unas 10 preguntas y el agente queda configurado con sus primeros pasos.
- **Conocimiento.** Dado que subí un PDF de preguntas frecuentes al agente, cuando un cliente pregunta algo que está en el documento, entonces el agente responde con esa información.

## Decisiones

### D-SPEC-31-1 · ¿Tiempo real con polling o con SSE?

| Opción | Pros | Contras |
|---|---|---|
| **A. Polling con `?after=` cada 3–5 s solo con la pestaña visible (elegida)** | Reusa el patrón del chat web (`web_chat.py:278`); sin infraestructura nueva; funciona detrás del túnel de Cloudflare y del BFF de Next | Más peticiones; 3–5 s de demora |
| B. SSE con Redis pub/sub | Instantáneo y menos peticiones | Conexiones largas a través del BFF y del túnel; más superficie para el aislamiento entre tenants |

**Recomendación:** A. B queda como mejora si la carga lo pide. **Estado:** ✅ tomada (D-38)

### D-SPEC-31-2 · ¿Dónde vive la clasificación del cliente?

| Opción | Pros | Contras |
|---|---|---|
| **A. La aporta pack_commerce con `lead_registry`, calculada al vuelo como `clasificarCliente` de agent-sale (elegida)** | El core no conoce pedidos; sin migración; cada pack puede sumar su propia columna | Solo hay clasificación con pack_commerce |
| B. Columna `clasificacion` en `customers` | Simple de filtrar | El core tendría que saber de pedidos |

**Recomendación:** A. **Estado:** ✅ tomada (D-38)

### D-SPEC-31-3 · ¿Proveedor de LLM por agente?

| Opción | Pros | Contras |
|---|---|---|
| A. Un proveedor por agente | Lo que pidió el dueño | Rompe el BYOK por negocio (ADR del proveedor) y el registro de costos |
| **B. Proveedor por negocio, modelo por agente con costo por mensaje a la vista (recomendada)** | Ya existe `GET /admin/agent-models` con precios | No cumple al pie de la letra la nota |

**Recomendación:** B, anotada en [HU-AOS-24](../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md). **Estado:** ⏳ pendiente del dueño (D-38)

### D-SPEC-31-4 · ¿Dónde guarda los vectores el pack de conocimiento?

| Opción | Pros | Contras |
|---|---|---|
| **A. pgvector en el mismo Postgres, con RLS por `tenant_id` (recomendada)** | Ya está en la imagen de test y producción; el aislamiento entre negocios usa la misma RLS que el resto; un backup | Comparte recursos con la base operativa; índices vectoriales grandes |
| B. Un servicio de vectores aparte (Qdrant, Pinecone) | Escala por separado | Infraestructura nueva; el aislamiento por tenant se reimplementa; otro proveedor con datos del cliente |

**Recomendación:** sí. pgvector ya está en la imagen de Postgres de test y producción, con búsqueda semántica o híbrida configurable por agente. El ADR de [HU-AOS-49](hu/HU-AOS-49-pack-de-conocimiento.md) lo cierra. **Estado:** ⏳ se decide en el ADR

## Fuera de alcance

- **Alerta de consumo de crédito** por WhatsApp o push ([HU-BILL-09](../SPEC-14-billing-extras/hu/HU-BILL-09-avisos-de-consumo.md)): sigue parqueada por D-35. Queda anotado que `GET /admin/plan` devuelve el crédito con `used: null`.
- **Panel clásico:** se descontinúa o se arregla según la decisión pendiente del dueño ([pendientes § B](../../10-pendientes-del-dueno.md#b--decisiones-cortas)).
- **Etiquetas, respuestas rápidas, adjuntos desde el panel y búsqueda dentro del chat:** ni SolversHub ni agent-sale los tienen. No se pidieron.
- **Reescritura de las pruebas confusas del catálogo:** va en el catálogo de pruebas, no en el producto.

## Métricas de éxito

- Las notas del inventario cierran con su prueba en OK en el ciclo siguiente.
- «No es claro» y «no encuentro» bajan a la mitad en las notas del dueño.
- Un mensaje entrante aparece en la bandeja en ≤ 5 s con la pestaña abierta.
- Ningún texto en inglés en avisos ni validaciones del panel. Se comprueba con un test que recorre los formularios.

## Requerimientos cubiertos

REQ-UX-16, REQ-UX-17, REQ-UX-18, REQ-UX-19, REQ-UX-20, REQ-UX-21, REQ-UX-22, REQ-UX-23, REQ-AOS-18, REQ-AOS-19.
