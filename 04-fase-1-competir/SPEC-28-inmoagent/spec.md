# SPEC-28 · Vertical inmobiliaria (InmoAgent)

> Estado SDD: En revisión (2026-10-09) · Fase 1 · Workstream Verticales · Decisión de arranque D-31 · Todo el código exige un piloto firmado (P-26)
>
> **2026-10-17 ([D-35](../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes)):** encaja con la visión (D-31: especialistas en un hilo sobre el Agent OS); queda en diseño, sin calendario hasta tener piloto (P-26/P-31). No se parquea.

## Problema

Una inmobiliaria atiende por WhatsApp a cinco públicos distintos:

- quien busca comprar;
- quien busca arrendar;
- el propietario que quiere publicar su inmueble;
- el arrendatario que paga un canon cada mes;
- el asesor que muestra los inmuebles.

Hoy agent-core no puede atender a ninguno de ellos bien. Lo que falta está verificado contra `solvershub-backend` en `develop` @ `cf73dc4`:

| # | Hueco | Evidencia |
|---|---|---|
| 1 | No existe la entidad inmueble. El catálogo de pack-commerce es de productos con stock y su búsqueda es `ILIKE` por palabras, sin rangos, sin área y sin ubicación. | `packages/pack-commerce/pack_commerce/models.py`; `pack_commerce/skills.py:721-723` (`consultar_inventario`) |
| 2 | No hay búsqueda geoespacial. PostGIS está instalado (ADR-0058), pero solo `pack_cobranza_clientes.geom` lo usa y ninguna consulta llama a `ST_DWithin` ni a `ST_Distance`. Tampoco hay geocodificación. | `docker/postgres/Dockerfile`; `packages/pack-cobranza/alembic/versions/0002_postgis.py` |
| 3 | La ubicación que comparte el cliente por WhatsApp se pierde. La respuesta a una lista o botón llega solo con su `title`, sin el payload. | `core/gateway/channels/whatsapp/inbound.py:76-81` |
| 4 | Solo se puede responder con texto, una imagen por turno o una plantilla. No hay botones, listas ni ubicación de salida. | `core/gateway/channels/whatsapp/outbound.py`; `core/orchestrator/safe_renderer.py` (`_image_url`) |
| 5 | La agenda es una sola por negocio: la restricción de solape es por tenant, así que dos asesores no pueden mostrar inmuebles a la misma hora. Además, el correo es obligatorio para agendar y la cita no sabe de qué inmueble es. | `packages/pack-calendar/alembic/versions/0004_demo_de_punta_a_punta.py:35-40`; `pack_calendar/skills.py:380-383` |
| 6 | Las suscripciones no sirven tal cual para un arriendo. Con `variante_id` nulo y sin coincidencia de referencia, `activate` modifica la suscripción vigente del cliente y da el período en curso por pagado. Las tools `sub_*` actúan sobre la primera suscripción activa: un cliente con gimnasio y arriendo podría pausar el arriendo. | `packages/pack-subscriptions/pack_subscriptions/capability.py:134-240`; `core/subscriptions/tools.py:48-52` |
| 7 | Los avisos al cliente por evento son una lista fija del core. Un pack no puede declarar "visita realizada" ni "contrato por vencer". | `core/gateway/event_notices.py` (`EVENTOS`); `core/events/core_handlers.py` (`_HANDLERS`) |
| 8 | Los recordatorios de cobro salen todos los días a las 09:00 de Bogotá, domingos y festivos incluidos. Afecta hoy a todos los negocios: se corrige aparte en HU-SUB-18. | `packages/pack-subscriptions/pack_subscriptions/jobs.py:359-362` |

**El Agent OS ya planificado.** [SPEC-26](../SPEC-26-agent-os/spec.md) (D-27) descarta agentes LLM independientes frente al cliente. Por eso el "orquestador con 7 subagentes" del encargo original no se puede construir como está pedido. Hay que traducirlo a Coordinador, especialistas en un hilo, procedimientos tipados y back-office que solo propone.

## Usuarios y contexto

- **Buscador** (comprador o arrendatario potencial): describe lo que quiere en lenguaje natural ("un apartamento cerca del colegio de mis hijos, hasta 3 millones") y espera opciones reales, con razones, y poder agendar la visita.
- **Propietario**: quiere publicar su inmueble en venta o en arriendo sin llenar formularios largos. Comparte ubicación y fotos por WhatsApp.
- **Arrendatario**: recibe el recordatorio del canon, paga por link y consulta su estado de cuenta.
- **Asesor comercial** (colaborador del negocio): recibe leads y visitas asignadas, valida captaciones y toma la conversación cuando hay oferta, negociación o queja.
- **Dueño o gerente de la inmobiliaria**: configura zonas, asesores, pesos de recomendación y plantillas, y mira los KPIs.

País de referencia: Colombia (`[PAÍS]`), moneda COP (`[MONEDA]`) y pagos con Wompi. El nombre de la inmobiliaria (`[NOMBRE DE LA INMOBILIARIA]`) es una variable del preset (`assistant_name` y `business_description`).

## Por qué importa (valor empresarial)

Las inmobiliarias concentran el negocio en WhatsApp, y su costo está en el asesor que filtra consultas, agenda visitas y persigue pagos. Una vertical con búsqueda geoespacial explicada, captación conversacional y cobro del canon les ofrece algo que un bot genérico no da. Para SolversHub abre un segmento nuevo sin fork ([HU-FWK-11](../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-11-presets-adicionales.md) ya lo nombraba).

La revisión del 2026-10-09 separó lo que tiene consumidores reales hoy y lo sacó de esta spec, para que no espere al piloto:

- el botón interactivo ([HU-AOS-09](../SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md));
- las extensiones genéricas de procedimientos ([HU-AOS-03](../SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md));
- los presets v2 ([HU-AOS-46](../SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md));
- el cobro en horario legal (HU-SUB-18).

Todo lo que queda aquí tiene como único consumidor la vertical, así que espera al piloto (ADR-0023: no se sube un contrato al core con un solo caso de uso real).

## Alcance

La vertical se ejecuta en seis fases internas. El frontmatter de todas las HU dice `fase: 1`.

| Fase INMO | Qué entrega | HU |
|---|---|---|
| 0 · DoR | ADRs propuestos de la vertical y decisiones abiertas; es la única HU sin piloto | [HU-INMO-01](hu/HU-INMO-01-adrs-y-dor-del-piloto.md) |
| 1 · Fundaciones | Listas y ubicación del canal, avisos declarados por habilidades, agenda por asesor, agenda como capacidad, suscripciones de plazo fijo, relevo al asesor, supresión de datos, pack base geoespacial y panel de inventario | [HU-INMO-02](hu/HU-INMO-02-entrada-estructurada-whatsapp.md) a [HU-INMO-11](hu/HU-INMO-11-inventario-y-captaciones-en-el-panel.md) |
| 2 · Búsqueda, geo y recomendación | Geocodificación, zonas y POI, búsqueda por filtros y radio, scoring explicado, relajación, perfil persistente y fichas | [HU-INMO-12](hu/HU-INMO-12-geocodificacion-y-zonas.md) a [HU-INMO-17](hu/HU-INMO-17-fichas-y-verificacion-de-hechos.md) |
| 3 · Captación, visitas y proactividad | Captación de propietarios, visitas con el asesor del inmueble, oportunidades, seguimiento post-visita, encuesta, alertas y reenganche | [HU-INMO-18](hu/HU-INMO-18-captacion-de-propietarios.md) a [HU-INMO-22](hu/HU-INMO-22-alertas-y-reenganche.md) |
| 4 · Arriendos, preset y medición | Contrato como registro, cobro del canon, mora, incremento anual, preset `inmobiliaria`, golden y journeys, KPIs | [HU-INMO-23](hu/HU-INMO-23-contrato-de-arriendo-y-canon.md) a [HU-INMO-26](hu/HU-INMO-26-kpis-de-la-vertical.md) |
| 5 · Agent OS nativo | Afirmaciones de la vertical para el verificador, procedimientos y especialistas (tras AOS R1 y R3), back-office y memoria por scope (tras AOS R5) | [HU-INMO-27](hu/HU-INMO-27-procedimientos-1-1.md), [HU-INMO-29](hu/HU-INMO-29-procedimientos-inmobiliarios.md) a [HU-INMO-31](hu/HU-INMO-31-back-office-y-memoria.md) |

El diseño completo está en [design.md](design.md): mapeo de los subagentes, integración con los packs, modelo de datos, geo, plantillas conversacionales y memoria. El orden de ejecución está en [tasks.md](tasks.md).

## Escenarios clave (Gherkin)

- **Búsqueda con radio.** Dado un inventario publicado con coordenadas, cuando el cliente escribe "apartamento en arriendo a menos de 1 km de la estación Calle 63, máximo 3 millones", entonces el asistente muestra hasta 5 inmuebles reales con su canon y su distancia, calculados por el servidor, y explica por qué recomienda cada uno.
- **Sin resultados.** Dado que ningún inmueble cumple los filtros, cuando el asistente responde, entonces ofrece como opciones las relajaciones que sí dan resultados ("subir a $3.300.000: 4 opciones", "ampliar a 1,5 km: 6 opciones") y nunca relaja lo que el cliente marcó como indispensable.
- **Captación.** Dado un propietario que escribe "quiero arrendar mi apartamento", cuando comparte la ubicación, los datos y las fotos y confirma, entonces queda una captación en validación, con la ubicación confirmada y la autorización de datos registrada, y el asesor de la zona recibe el aviso en menos de 1 minuto.
- **Visita.** Dado un inmueble que el cliente ya vio en esta conversación, cuando elige un horario de la agenda del asesor de ese inmueble y confirma, entonces queda una sola visita en la agenda de ese asesor, el cliente recibe la dirección exacta y los recordatorios, y nunca se agenda en un horario que no se ofreció.
- **Canon.** Dado un contrato de arriendo vigente registrado en el panel, cuando se acerca el día de pago, entonces el arrendatario recibe en horario legal (HU-SUB-18) un recordatorio con el monto y un link de pago generados por el servidor, y el contrato pasa a "en mora" si el cargo vence sin pagarse.
- **Relevo al asesor.** Dado un cliente que hace una oferta, cuando el asistente escala, entonces la conversación queda asignada al asesor del caso, y nadie le vuelve a pedir datos al cliente.

## Decisiones

### D-SPEC-28-1 · Cuándo se construye sin un cliente real

| Opción | Pros | Contras |
|---|---|---|
| **A. Especificar ahora; todo el código de la vertical exige un piloto firmado; lo genérico con consumidor real sale a su spec** | El backlog queda listo, no se escribe un pack especulativo y lo genérico no espera | La vertical depende de cerrar un piloto |
| B. No especificar hasta tener un cliente | Cero trabajo especulativo | Al llegar el cliente no hay plan, y las brechas genéricas siguen ocultas |
| C. Construir ya el pack completo | Llega antes al mercado | Contradice la regla de `new-pack` y compite con el Agent OS por la única persona |

**Recomendación: A.** Estado: ✅ tomada (D-31, 2026-10-09). La revisión del mismo día movió las piezas genéricas a [HU-AOS-03](../SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md), [HU-AOS-09](../SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md), [HU-AOS-46](../SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) y HU-SUB-18.

### D-SPEC-28-2 · Alcance de los arriendos en v1

| Opción | Pros | Contras |
|---|---|---|
| **A. Contrato como registro (partes, canon, fechas, regla de incremento) y cobro del canon con pack-subscriptions + Wompi, con recordatorios y mora** | Reutiliza el ciclo de cobro que ya existe; alcance acotado | Sin documento ni firma; la liquidación al propietario sigue fuera |
| B. Administración completa: PDF, firma electrónica, liquidación y giro al propietario, cartera con pack-cobranza | Producto completo | Casi duplica el alcance; requiere firma y pagos salientes |
| C. Solo comercial (búsqueda, captación y visitas) | Más rápido | Deja fuera el ingreso recurrente del arriendo |

**Recomendación: A.** Estado: ✅ tomada (D-31, 2026-10-09).

### D-SPEC-28-3 · Secuencia frente al Agent OS

| Opción | Pros | Contras |
|---|---|---|
| **A. Híbrida: datos, búsqueda geo y habilitadores sobre AgentSpec v2; procedimientos y especialistas cuando lleguen AOS R1 y R3; back-office y memoria con AOS R5** | Nada se tira: tablas, acciones y evals sirven a los dos motores | Hay que mantener dos superficies (`flow.json` y procedimientos) durante la transición |
| B. Esperar al Agent OS y construir todo nativo | Un solo diseño | La vertical llega a mediados de 2027 o después |
| C. Todo sobre el motor v2 ahora | Rápido | Compite con el AOS y después hay que migrar las conversaciones |

**Recomendación: A.** Estado: ✅ tomada (D-31, 2026-10-09).

### D-SPEC-28-4 · Cómo se agenda una visita

| Opción | Pros | Contras |
|---|---|---|
| **A. Capacidad de agenda del core (`SchedulingCapability`, molde de `payment_registry`), por `admin_id`, implementada por pack-calendar** | Una sola escritura determinista; funciona igual antes y después del AOS; la visita conserva su semántica (asesor, dirección, seguimiento) | Una interfaz nueva del core, que espera al piloto |
| B. `encargar(agenda, …)` A2A al procedimiento de agenda | Nativo del AOS | No existe antes de R3; agrega un salto y parte la visita en dos tareas |
| C. Antes del AOS, que el LLM llame las tools de calendar desde la sección `visitas` | Sin trabajo en el core | Dos escrituras hechas por el LLM, correo obligatorio y la cita sin vínculo con el inmueble |

**Recomendación: A**, con interfaz mínima (`disponibilidad`, `reservar`, `reagendar`, `cancelar`). Estado: ⏳ pendiente (se cierra en [HU-INMO-01](hu/HU-INMO-01-adrs-y-dor-del-piloto.md)).

### D-SPEC-28-5 · Geocodificación y puntos de interés

| Opción | Pros | Contras |
|---|---|---|
| **A. Pin primero; si no hay pin, geocodificador cuya licencia permita guardar la dirección del inmueble; zonas y POI importados de OSM por ciudad y por negocio, con cercanías precalculadas** | Costo casi cero por consulta; determinista; licencia compatible | La calidad de OSM y de la nomenclatura colombiana está por verificar; datos duplicados entre negocios de una misma ciudad |
| B. API de lugares en cada consulta (Google Places) | Datos frescos y completos | Costo por consulta; la licencia limita guardar (≤ 30 días) |
| C. Solo zonas dibujadas por el negocio | Control total | No resuelve "cerca de un colegio" |

**Recomendación: A**, con el proveedor concreto en P-27. Un catálogo compartido entre negocios solo con ADR y las condiciones de design.md. Estado: ⏳ pendiente.

### D-SPEC-28-6 · Cuántos especialistas

| Opción | Pros | Contras |
|---|---|---|
| **A. 3 especialistas (`asesor_comercial`, `captacion`, `arriendos`) más General; geo, match y relevo son acciones o back-office** | Menos errores de ruta; coherente con [SPEC-26](../SPEC-26-agent-os/spec.md) §2.7 | Cada especialista tiene más procedimientos |
| B. Los 7 "subagentes" del encargo como especialistas | Calca el encargo | Multiplica los errores de ruta y los cambios de dueño; varios no conversan (geo, match) |

**Recomendación: A.** Estado: ⏳ pendiente.

### D-SPEC-28-7 · Pipeline comercial

| Opción | Pros | Contras |
|---|---|---|
| **A. Tablas propias `oportunidades` y `oportunidad_eventos`; lead = `Customer` (ADR-0022) más columnas en la vista global de leads (ADR-0056)** | Etapas propias (visita, oferta, separación); no importa otro pack | Una tabla más |
| B. Reutilizar `pack_commerce_leads` | Ya existe | Exige activar commerce; sus estados no describen el ciclo inmobiliario; viola la invariante 5 si se escribe desde otro pack |

**Recomendación: A.** Estado: ⏳ pendiente.

### D-SPEC-28-8 · Cuándo se revela la dirección exacta

| Opción | Pros | Contras |
|---|---|---|
| **A. Barrio y distancias redondeadas hasta que ese cliente tenga una visita confirmada; dirección exacta con la visita** | Protege al propietario y a los inmuebles ocupados | Un cliente puede pedirla antes |
| B. Siempre visible | Simple | Riesgo de seguridad y de saltarse a la inmobiliaria |
| C. Nunca por el asistente; la da el asesor | Máxima reserva | Fricción en cada visita |

**Recomendación: A**, configurable por negocio (P-30). Estado: ⏳ pendiente.

### D-SPEC-28-9 · Dueño de los mensajes interactivos

| Opción | Pros | Contras |
|---|---|---|
| A. SPEC-28 construye botones, listas y ubicación, y [HU-AOS-09](../SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md) depende de ella | Un solo adaptador | Ata la R1 del Agent OS a una vertical sin cliente |
| **B. [HU-AOS-09](../SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md) es dueña del botón de punta a punta (salida, `button_reply.id` y botones de plantilla); SPEC-28 agrega listas, ubicación y varias imágenes con piloto** | El Agent OS no espera a la vertical; cada pieza tiene un consumidor real | Dos HU tocan el mismo adaptador, en momentos distintos |

**Recomendación: B** (revisión del arquitecto, 2026-10-09). Estado: ⏳ pendiente; las HU ya están escritas sobre B.

Las preguntas abiertas de esta spec (P-26 a P-31) están en [preguntas-abiertas.md](../../02-vision-y-decisiones/preguntas-abiertas.md). P-26 (piloto) bloquea todas las HU menos [HU-INMO-01](hu/HU-INMO-01-adrs-y-dor-del-piloto.md).

## Fuera de alcance

- Documento del contrato en PDF, firma electrónica, liquidación y giro al propietario, y cartera morosa con pack-cobranza (fase posterior, D-SPEC-28-2).
- Avalúos, crédito hipotecario y estudio del arrendatario con centrales de riesgo.
- Publicación automática en portales (Finca Raíz, Metrocuadrado) e importación por scraping. Solo se importan exportaciones del propio negocio.
- Tours virtuales y video en la ficha.
- Campañas masivas fuera de la ventana de 24 h: las hace [HU-CHAN-03](../SPEC-17-canales-y-campanas/hu/HU-CHAN-03-pack-marketing.md). La vertical solo aporta sus segmentos y eventos.
- Procedimientos editables por el negocio ([HU-AOS-45](../../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md), Fase 2).
- Lo que se movió a otras specs: botón interactivo ([HU-AOS-09](../SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md)), extensiones genéricas de procedimientos ([HU-AOS-03](../SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md)), presets v2 ([HU-AOS-46](../SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md)) y cobro en horario legal (HU-SUB-18).

## Métricas de éxito

El detalle de cómo se mide cada una está en [design.md](design.md#kpis-y-cómo-se-miden).

- Consulta → visita agendada: ≥ 15 % de los perfiles activos en 30 días (línea base del piloto).
- Búsquedas que terminan sin resultados tras ofrecer relajación: ≤ 10 %.
- Interés por recomendación ("me interesa" o visita) ≥ 25 %; feedback de la visita ≥ 4/5.
- Primera respuesta del asistente p95 ≤ 8 s; búsqueda en base p95 ≤ 300 ms con 10⁴ inmuebles.
- Recordatorios de canon: ≥ 70 % de cargos pagados a tiempo; **0** contactos de cobro fuera del horario legal.
- Captaciones completas en una sola conversación ≥ 70 %; asesor avisado en ≤ 1 min.
- Calidad: pass^4 ≥ 0,85 por procedimiento; **0** precios, distancias o links sin evidencia del servidor.

## Requerimientos cubiertos

REQ-INMO-01, REQ-INMO-02, REQ-INMO-03, REQ-INMO-04, REQ-INMO-05, REQ-INMO-06, REQ-INMO-07, REQ-INMO-08, REQ-INMO-09, REQ-INMO-10, REQ-INMO-11, REQ-INMO-12.
