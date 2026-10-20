# Preguntas abiertas

Decisiones que todavía son del cliente. Cada una trae opciones con pros y contras, una
recomendación y la HU que bloquea. Las HU afectadas están escritas como borrador sobre la opción
recomendada (D-10).

| # | Pregunta | Recomendación | Bloquea |
|---|---|---|---|
| P-01 | ¿Dónde corre producción y con qué presupuesto? | ✅ A · VPS dedicado con Coolify + almacenamiento S3 compatible (D-19) | [HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) |
| P-02 | ¿Qué RPO y RTO se prometen? | ✅ A · PITR con WAL: RPO 15 min, RTO 4 h (D-20) | [HU-ARCH-03](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md) |
| P-03 | ¿Con qué proveedor cobra sus suscripciones el tenant `solvershub`? | ✅ A · `pack_subscriptions` (en línea) (D-21) | [HU-SH-01](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-01-tenant-reproducible.md) |
| P-04 | ¿Se mantienen los precios 0/200k/600k/1,8M? | Sí, con créditos y plan anual | HU-BILL-05 |
| P-05 | ¿Qué modelo usa la llave de plataforma por defecto? | ✅ A · `deepseek-flash` (D-22), con `gpt-4o-mini` de respaldo | [HU-ARCH-10](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md) |
| P-06 | ¿Qué pasa al agotar los créditos con una conversación abierta? | Colchón de 5 % solo para conversaciones abiertas | HU-BILL-06 |
| P-07 | ¿Cuánto duran las recargas? | Hasta el fin del período siguiente | [HU-BILL-10](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-10-recargas.md) |
| P-08 | ¿Se vende WhatsApp Web (no oficial) a clientes? | No en v1; solo pruebas internas | [HU-CONN-08](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md) |
| P-09 | ¿Quién edita el texto (`purpose`) de las etapas del flujo? | Solo master en v1; el negocio edita la estructura | [HU-FLOW-01](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-01-adr-editor-de-flujo.md) |
| P-10 | ¿Un asistente por negocio en v1? | ✅ Agent OS de procedimientos: varios agentes por conexión, por fases, tras el 0A (D-27); la unidad que se vende es el agente del negocio y el Coordinador es su agente core instanciado en cada conexión (D-35) | HU-BILL-05 |
| P-11 | ¿Cómo se llama el Agente Core en el panel? | "Coordinador" | [HU-AOS-23](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md) |
| P-12 | ¿Una voz por conexión o un nombre por agente? | Una voz; presentación opcional al cambiar de agente | [HU-AOS-19](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-19-handoff-delegacion-y-consulta.md) |
| P-13 | ¿Cómo se empaqueta el Agent OS en los planes? | ✅ D-35: agentes publicados (con al menos una instancia en una conexión), crédito mensual y colaboradores; 1 conexión incluida por agente; operaciones entre agentes dentro de los créditos; cifras por plan como propuesta en documento de precios (privado) §5 | HU-BILL-05 |
| P-14 | ¿Cuál es el primer piloto externo? | Un negocio de cobranza (D-02) | [HU-AOS-38](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-38-lanzamiento-comercial.md) |
| P-15 | ¿Hay demanda de federación entre negocios? | Diferir hasta 2 interesados reales | [HU-AOS-39](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-39-federacion-entre-negocios.md) |
| P-16 | ¿Qué modelo usa el coprocesador? | `deepseek-flash` sin *thinking*, salida restringida, respaldo `gpt-4o-mini` (D-22) | [HU-AOS-17](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-17-enrutamiento-y-modo-sombra.md) |
| P-17 | ¿Quién ve entradas y salidas de acciones en el depurador? | Solo `observabilidad:ver`, siempre redactadas | [HU-AOS-28](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md) |
| P-18 | ¿Qué canal sigue como conexión después de WhatsApp y el chat web? | Canal API, luego correo entrante; Slack según demanda | [HU-AOS-42](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-42-canal-api-y-webhooks.md) |
| P-19 | ¿Qué embeddings se usan en producción? | Local multilingüe de 384 dimensiones, evaluado contra `text-embedding-3-small` | [HU-AOS-17](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-17-enrutamiento-y-modo-sombra.md) |
| P-20 | ¿Un agente puede escribir hechos en el namespace de otro? | No; se pide por consulta o encargo | [HU-AOS-36](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-36-memoria-por-scope.md) |
| P-21 | ¿Se reencuadra [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md) como editor de superpoderes? | ✅ D-35: [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md) queda parqueada ([HU-FLOW-01](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-01-adr-editor-de-flujo.md) a 06 fuera del calendario); el motor y el editor de superpoderes viven en [HU-AOS-05](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-05-motor-de-procedimientos.md), [HU-AOS-25](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md) y [HU-AOS-45](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md). [HU-ARCH-26](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md) y [HU-FLOW-07](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FLOW-07-purpose-y-reglas-por-etapa.md) ([SPEC-22](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/spec.md), fase 2) siguen pendientes del dueño | [HU-AOS-25](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md) |
| P-22 | ¿Es obligatorio un botón interactivo para confirmar lo irreversible? | Sí en etapas de riesgo alto; clasificador sí/no en canales sin botones | [HU-AOS-09](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md) |
| P-23 | ¿Qué umbrales de calidad se exigen? | pass^4 ≥ 0,85 por procedimiento; LLM-juez con kappa ≥ 0,7 frente a 100 conversaciones etiquetadas | [HU-ARCH-28](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md), [HU-AOS-21](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md), [HU-AOS-31](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-31-auditor-de-calidad.md) |
| P-24 | ¿Quién etiqueta conversaciones para calibrar el LLM-juez? | El master: 50 conversaciones por semana durante 2 semanas | [HU-AOS-31](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-31-auditor-de-calidad.md) |
| P-25 | ¿Se usa "Agent OS" como nombre comercial? | Validar con el abogado (HU-GTM-02) y tener lista una alternativa propia | [HU-AOS-38](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-38-lanzamiento-comercial.md) |
| P-26 | ¿Qué inmobiliaria es el piloto de la vertical y qué alcance tiene? | Firmar un piloto con arriendos administrados antes de escribir el pack | [HU-INMO-02](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-02-entrada-estructurada-whatsapp.md) |
| P-27 | ¿Qué geocodificador usa la vertical inmobiliaria? | Pin primero; Mapbox permanente u OSM propio para guardar; Google solo para consultas sin guardar | [HU-INMO-12](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-12-geocodificacion-y-zonas.md) |
| P-28 | ¿Quién carga el IPC y quién aprueba el incremento del canon? | El negocio carga el IPC anual; el asesor aprueba cada ajuste | [HU-INMO-24](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-24-mora-e-incremento-del-canon.md) |
| P-29 | ¿Dónde se registra la autorización de tratamiento de datos? | En el core, por cliente y versión del aviso, reutilizable por todas las habilidades | [HU-INMO-18](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-18-captacion-de-propietarios.md) |
| P-30 | ¿Cuándo da el asistente la dirección exacta de un inmueble? | Al confirmar la visita; antes, barrio y ubicación aproximada | [HU-INMO-17](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-17-fichas-y-verificacion-de-hechos.md) |
| P-31 | ¿Cuándo se ejecuta la vertical frente al Agent OS? | Al firmarse el piloto, intercalada con el Agent OS sin tocar su camino crítico; la fase 5 tras AOS R3 y R5 | [HU-INMO-01](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md) |

## P-01 · Infraestructura de producción

Hoy producción y test corren en la máquina de desarrollo (invariante 9).

| Opción | Pros | Contras |
|---|---|---|
| **A. VPS dedicado (2 nodos) con Coolify, backups en almacenamiento S3 compatible** | Reutiliza lo que ya funciona en test; costo bajo ((costo interno)) | La operación de Postgres es propia |
| B. Nube administrada (Postgres gestionado, contenedores gestionados) | Backups y alta disponibilidad incluidos | 3–5× más caro; migrar Coolify y túneles |
| C. Seguir en la máquina propia con UPS | Gratis | Viola la invariante 9; un corte de luz tumba a todos los clientes |

**Recomendación: A.** Bloquea [HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md).

**Decidida (2026-10-02): A**, registrada como [D-19](decisiones.md#d-19--infraestructura-de-producción-vps-dedicado-con-coolify).

## P-02 · RPO y RTO

`security.md` publica un SLO de 15 min, pero un dump diario da un RPO de 24 h.

| Opción | Pros | Contras |
|---|---|---|
| **A. WAL continuo + PITR (RPO 15 min, RTO 4 h)** | Cumple lo publicado | Más configuración (pgBackRest o wal-g) |
| B. Dump diario y bajar el SLO publicado a 24 h | Simple | Pierde hasta un día de pedidos y pagos |

**Recomendación: A.** Bloquea [HU-ARCH-03](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md).

**Decidida (2026-10-02): A**, registrada como [D-20](decisiones.md#d-20--rpo-y-rto-de-producción).

## P-03 · Proveedor de suscripción del tenant `solvershub`

El pedido original era "usar pack-cobranza para el cobro"; D-15 permite elegir.

| Opción | Pros | Contras |
|---|---|---|
| **A. `pack_subscriptions` (pago en línea)** | Ya integrado con comercio; los clientes de SolversHub pagan en línea; disponible en el Hito 0A | No ejercita cobranza en el dogfooding |
| B. Cobranza (`Suscripcion`) | Dogfooding de cobranza; mora y promesas maduras | Llega en el 0B (HU-SUB-15); pensado para cobro en campo |

**Recomendación: A** para SolversHub, y cobranza para negocios con cobradores en calle. Bloquea
[HU-SH-01](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-01-tenant-reproducible.md).

**Decidida (2026-10-02): A**, registrada como [D-21](decisiones.md#d-21--proveedor-de-suscripción-del-tenant-solvershub).

## P-04 · Precios de lanzamiento

| Opción | Pros | Contras |
|---|---|---|
| **A. Mantener 0/200k/600k/1,8M con créditos + plan anual con 2 meses gratis** | Sin fricción comercial; margen ≥50 % a 100 clientes en el peor caso | Margen bajo con menos de ~50 clientes (por el costo fijo) |
| B. Basic a 150k (el mínimo de Wompi) | Entrada más barata frente a ClonAI | Con los mismos 20.000 créditos el margen del peor caso es negativo por debajo de ~31 clientes y nunca llega al 50 %; habría que bajar a ~12.000 créditos |
| C. Basic a 250k | Peor caso ≥50 % desde ~50 clientes | Más caro que la referencia local |

**Recomendación: A.** Detalle en documento de precios (privado). Bloquea
HU-BILL-05.

## P-05 · Modelo por defecto con la llave de plataforma

| Opción | Pros | Contras |
|---|---|---|
| **A. `deepseek-flash`** | (costo por conversación); multimodal nativo | Hay que verificar tool calling y estabilidad; tarifa pico/valle |
| B. `gpt-4o-mini` | Tool calling probado | ~2× el costo |
| C. `claude-haiku-4-5` | Mejor calidad en español y en tools | ~8× el costo |

**Recomendación: A**, con B como respaldo automático si fallan las evals, y C como opción "premium"
para el negocio. Bloquea [HU-ARCH-10](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md).

**Decidida (2026-10-02): A**, registrada como [D-22](decisiones.md#d-22--modelo-por-defecto-de-la-llave-de-plataforma).

## P-06 · Créditos agotados con una conversación abierta

| Opción | Pros | Contras |
|---|---|---|
| **A. Colchón de 5 % del cupo solo para conversaciones ya abiertas; después escala a humano** | Nunca se corta a un cliente a mitad de camino | 5 % de consumo no cobrado |
| B. Corte duro | Simple | Rompe la regla "no se corta a mitad de conversación" |
| C. Gracia por tiempo (24 h) | Predecible | Consumo sin techo durante la gracia |

**Recomendación: A.** Bloquea HU-BILL-06.

## P-07 · Vigencia de las recargas

| Opción | Pros | Contras |
|---|---|---|
| **A. Hasta el fin del período siguiente; se consumen después del cupo del plan** | Justo para el cliente; pasivo acotado | Lógica de dos bolsas |
| B. 60 días | Simple | Desalineado con el ciclo |
| C. Sin arrastre | Sin pasivo | Percepción de pérdida |

**Recomendación: A.** Bloquea [HU-BILL-10](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-10-recargas.md).

## P-08 · WhatsApp Web (no oficial, ADR-0074)

| Opción | Pros | Contras |
|---|---|---|
| **A. No se vende en v1; solo pruebas y demos internas** | Sin riesgo de bloqueo de números de clientes | Algunos pymes lo piden |
| B. Se vende con aviso de riesgo | Más clientes rápido | Bloqueos de Meta y responsabilidad legal |

**Recomendación: A.** Afecta [HU-CONN-08](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md).

## P-09 · Quién edita el `purpose` de las etapas del flujo

El `purpose` es texto que va al prompt (invariante 3: vive en el AgentSpec).

| Opción | Pros | Contras |
|---|---|---|
| **A. Solo master/implementador en v1; el negocio edita la estructura (orden, tools, etapas)** | Protege la calidad de las evals | Menos autonomía |
| B. El negocio edita todo | Autonomía total | Regresiones de calidad difíciles de soportar |

**Recomendación: A.** Bloquea [HU-FLOW-01](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-01-adr-editor-de-flujo.md).

## P-10 · Asistentes por negocio

| Opción | Pros | Contras |
|---|---|---|
| **A. Uno por negocio en v1; varios en Fase 2 con ADR** | Coincide con el modelo actual (un AgentSpec por tenant) | Un negocio con dos marcas necesita dos tenants |
| B. Varios desde v1 | Flexibilidad | Cambia contratos, billing y panel |

**Recomendación: A.** Afecta los límites de HU-BILL-05.

**Decidida (2026-10-08): ni A ni B tal cual.** Varios agentes por conexión con el Agent OS de procedimientos, por fases y tras el 0A, registrada como [D-27](decisiones.md#d-27--agent-os-varios-agentes-por-conexión-responde-p-10).

**Actualizada (2026-10-17): [D-35](decisiones.md#d-35--solvershub-vende-agentes).** La unidad que se vende y se configura es el agente del negocio; el Coordinador por conexión es el agente core del negocio instanciado en cada conexión; los planes cobran por agentes publicados, crédito mensual y colaboradores (HU-BILL-05).

## P-11 · Nombre del Agente Core en el panel

¿Cómo se llama el Agente Core en el panel?

| Opción | Pros | Contras |
|---|---|---|
| **A. "Coordinador"** | Describe lo que hace sin sugerir que conversa | Palabra nueva para el dueño |
| B. "Recepción" | Familiar | Sugiere que atiende y responde |
| C. "Agente principal" | Simple | Se confunde con un especialista |

**Recomendación: A.** Bloquea [HU-AOS-23](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md).

## P-12 · Voz por conexión o por agente

¿Una voz por conexión o un nombre por agente?

| Opción | Pros | Contras |
|---|---|---|
| **A. Una voz por conexión; presentación opcional al cambiar de agente** | Coherencia de marca | Menos sensación de equipo |
| B. Nombre y voz por agente | Parece un equipo humano | Incoherencia de tono |

**Recomendación: A.** Bloquea [HU-AOS-19](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-19-handoff-delegacion-y-consulta.md).

## P-13 · Empaquetado del Agent OS en los planes

¿Cómo se empaqueta el Agent OS en los planes?

| Opción | Pros | Contras |
|---|---|---|
| **A. Límites por plan siguiendo la escalera de habilidades (agentes 1+General/3/8/∞, conexiones 1/2/5/∞)** | Sigue la escalera actual; simple | Cifras por validar con el modelo de precios |
| B. Agentes como add-on pagado | Ingreso extra | Fricción y otra factura |
| C. Sin límites | Adopción | Sin palanca de expansión |

**Recomendación: A.** Bloquea [HU-AOS-37](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-37-cuotas-y-planes.md).

**Decidida (2026-10-17): [D-35](decisiones.md#d-35--solvershub-vende-agentes).** Ni la escalera de habilidades (A) ni un add-on (B): los planes cobran por **agentes publicados** (con al menos una instancia en una conexión; el General cuenta, el Coordinador no), **crédito mensual** y **colaboradores**; 1 conexión incluida por agente y las adicionales como dimensión propuesta; las operaciones entre agentes se cobran dentro de los créditos. Las cifras por plan son una propuesta para validar con el dueño en documento de precios (privado) §5. Los límites viven en HU-BILL-05; [HU-AOS-37](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-37-cuotas-y-planes.md) se achica a operaciones entre agentes y agentes de back-office.

## P-14 · Primer piloto externo de Agent OS

¿Cuál es el primer piloto externo?

| Opción | Pros | Contras |
|---|---|---|
| **A. Un negocio de cobranza** | Diferencial casi único (D-02); procedimientos claros | Requiere APK y cobradores |
| B. Un restaurante | Mercado grande | Diferencial menor |

**Recomendación: A.** Bloquea [HU-AOS-38](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-38-lanzamiento-comercial.md).

## P-15 · Federación entre negocios

¿Hay demanda de federación entre negocios?

| Opción | Pros | Contras |
|---|---|---|
| **A. Diferir hasta tener 2 interesados reales** | Sin trabajo especulativo | Sin vitrina de marketplace por ahora |
| B. Construirla en la Fase 1 | Diferencial | Riesgo de aislamiento sin demanda |

**Recomendación: A.** Bloquea [HU-AOS-39](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-39-federacion-entre-negocios.md).

## P-16 · Modelo del coprocesador del Coordinador

¿Qué modelo usa el coprocesador?

| Opción | Pros | Contras |
|---|---|---|
| **A. `deepseek-flash` sin *thinking* con salida restringida y respaldo `gpt-4o-mini`** | Barato y coherente con D-22 | Verificar latencia y JSON |
| B. `gpt-4o-mini` siempre | Tool calling probado | Cerca del doble de costo |

**Recomendación: A.** Bloquea [HU-AOS-17](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-17-enrutamiento-y-modo-sombra.md).

## P-17 · Visibilidad de datos en el depurador

¿Quién ve entradas y salidas de acciones en el depurador?

| Opción | Pros | Contras |
|---|---|---|
| **A. Solo el permiso `observabilidad:ver`, siempre redactado** | Privacidad | Menos detalle para depurar |
| B. Todo visible para el dueño | Depuración completa | Datos personales expuestos |

**Recomendación: A.** Bloquea [HU-AOS-28](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md).

## P-18 · Próximo canal como conexión

¿Qué canal sigue como conexión después de WhatsApp y el chat web?

| Opción | Pros | Contras |
|---|---|---|
| **A. Canal API, luego correo entrante; Slack según demanda** | Integraciones y pruebas primero | Slack llega más tarde |
| B. Slack primero | Algunos clientes B2B | Poca demanda en pymes |

**Recomendación: A.** Bloquea [HU-AOS-42](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-42-canal-api-y-webhooks.md).

## P-19 · Embeddings en producción

¿Qué embeddings se usan en producción?

| Opción | Pros | Contras |
|---|---|---|
| **A. Modelo local multilingüe de 384 dimensiones, evaluado contra `text-embedding-3-small`** | Sin costo por uso ni texto a terceros | CPU del servidor |
| B. `text-embedding-3-small` | Calidad conocida | Costo y datos a un tercero |
| C. Sin embeddings | Nada que operar | Más llamadas al coprocesador |

**Recomendación: A.** Bloquea [HU-AOS-17](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-17-enrutamiento-y-modo-sombra.md).

## P-20 · Escritura en namespaces de otro agente

¿Un agente puede escribir hechos en el namespace de otro?

| Opción | Pros | Contras |
|---|---|---|
| **A. No: cada agente escribe solo en sus namespaces** | Responsabilidad clara | Más consultas entre agentes |
| B. Sí, con auditoría | Flexible | Datos inconsistentes entre áreas |

**Recomendación: A.** Bloquea [HU-AOS-36](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-36-memoria-por-scope.md).

## P-21 · SPEC-15 como editor de superpoderes

¿Se reencuadra [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md) como editor de superpoderes?

| Opción | Pros | Contras |
|---|---|---|
| **A. Sí: retirar [HU-FLOW-01](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-01-adr-editor-de-flujo.md)..06, [HU-ARCH-26](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md) y [HU-FLOW-07](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FLOW-07-purpose-y-reglas-por-etapa.md) y absorberlas en el motor y el editor de superpoderes** | Un solo mecanismo; unos 35 días-persona menos | Reescribir [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md) |
| B. Mantener [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md) aparte | Sin cambios | Dos mecanismos de borrador y publicación |

**Recomendación: A.** Bloquea [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md), [HU-AOS-25](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md).

**Decidida (2026-10-17): A, por [D-35](decisiones.md#d-35--solvershub-vende-agentes).** [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md) se parquea en lugar de reencuadrarse: [HU-FLOW-01](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-01-adr-editor-de-flujo.md) a 06 quedan `parqueada`, fuera del calendario; el motor de procedimientos ([HU-AOS-05](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-05-motor-de-procedimientos.md)) y el editor de superpoderes ([HU-AOS-25](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md), [HU-AOS-45](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md)) absorben lo útil. [HU-ARCH-26](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md) y [HU-FLOW-07](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FLOW-07-purpose-y-reglas-por-etapa.md) ([SPEC-22](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/spec.md), fase 2) no se tocan en esta decisión: [HU-FLOW-07](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FLOW-07-purpose-y-reglas-por-etapa.md) depende de [HU-FLOW-05](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-05-borrador-y-publicacion.md) (parqueada), así que el dueño decide su retiro al revisar [SPEC-22](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/spec.md).

## P-22 · Botón para confirmar lo irreversible

¿Es obligatorio un botón interactivo para confirmar lo irreversible?

| Opción | Pros | Contras |
|---|---|---|
| **A. Obligatorio en etapas de riesgo alto; clasificador sí/no en canales sin botones** | Elimina malentendidos del "sí" | Fuera de la ventana de 24 h hace falta plantilla con botones |
| B. Texto libre | Natural | El "sí" se malinterpreta |

**Recomendación: A.** Bloquea [HU-AOS-09](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md).

## P-23 · Umbrales de calidad

¿Qué umbrales de calidad se exigen?

| Opción | Pros | Contras |
|---|---|---|
| **A. pass^4 ≥ 0,85 por procedimiento para publicar; LLM-juez con acuerdo kappa ≥ 0,7 frente a 100 conversaciones etiquetadas; ajustar con la primera medición** | Concreto y medible | Puede ser exigente al principio |
| B. Solo pass@1 ≥ 95 % | Ya existe | Oculta la inconsistencia |

**Recomendación: A.** Bloquea [HU-ARCH-28](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md), [HU-AOS-21](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md), [HU-AOS-31](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-31-auditor-de-calidad.md).

## P-24 · Quién etiqueta para calibrar el LLM-juez

¿Quién etiqueta conversaciones para calibrar el LLM-juez?

| Opción | Pros | Contras |
|---|---|---|
| **A. El master: 50 conversaciones por semana durante 2 semanas** | Conoce el negocio | Tiempo del dueño |
| B. Un tercero | Libera tiempo | Costo y menos contexto |

**Recomendación: A.** Bloquea [HU-AOS-31](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-31-auditor-de-calidad.md).

## P-25 · Nombre comercial "Agent OS"

¿Se usa "Agent OS" como nombre comercial?

| Opción | Pros | Contras |
|---|---|---|
| **A. Validar con el abogado y tener una alternativa propia** | Evita conflicto con un competidor que ya usa el nombre | Trámite |
| B. Usarlo sin revisar | Rápido | Riesgo legal y de confusión |

**Recomendación: A.** Bloquea [HU-AOS-38](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-38-lanzamiento-comercial.md).

## P-26 · Piloto de la vertical inmobiliaria

¿Qué inmobiliaria es el piloto de la vertical y qué alcance tiene? La skill `new-pack` no permite construir un pack sin un cliente real (D-31).

| Opción | Pros | Contras |
|---|---|---|
| **A. Firmar un piloto que administre arriendos, con 100 a 1.000 inmuebles en una ciudad, antes de escribir el pack** | Valida búsqueda, captación y cobro con datos reales | Hay que conseguirlo |
| B. Piloto solo comercial (venta o arriendo sin administración) | Más fácil de conseguir | No prueba el cobro del canon |
| C. Construir sin piloto | No espera a nadie | Pack especulativo |

**Recomendación: A.** Bloquea todas las HU de [SPEC-28](../04-fase-1-competir/SPEC-28-inmoagent/spec.md) menos [HU-INMO-01](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md).

## P-27 · Geocodificador de la vertical inmobiliaria

¿Qué proveedor convierte direcciones y lugares en coordenadas?

| Opción | Pros | Contras |
|---|---|---|
| **A. Pin primero; Mapbox permanente u OSM propio para direcciones que se guardan; Google solo para consultas que no se guardan** | Licencias compatibles con guardar el inventario; costo bajo | Dos proveedores; la cobertura de la nomenclatura colombiana está por verificar |
| B. Solo Google | Mejor cobertura | Solo permite guardar coordenadas ≤ 30 días |
| C. Solo pin y zonas, sin geocodificador | Cero costo y cero licencias | No entiende "cerca de Unicentro" si no está en los POI |

**Recomendación: A.** Bloquea [HU-INMO-12](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-12-geocodificacion-y-zonas.md).

## P-28 · IPC y aprobación del incremento del canon

¿Quién carga el IPC del año anterior y quién aprueba el incremento de cada contrato?

| Opción | Pros | Contras |
|---|---|---|
| **A. El negocio carga el IPC en la configuración; el asesor aprueba cada ajuste antes del aviso** | Control humano; sin depender de una API externa | Un paso manual al año |
| B. Se toma del DANE automáticamente y se aplica solo | Sin trabajo manual | Dependencia externa; un error se aplica a todos los contratos |

**Recomendación: A.** Bloquea [HU-INMO-24](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-24-mora-e-incremento-del-canon.md).

## P-29 · Registro de la autorización de datos

¿Dónde se guarda la autorización de tratamiento de datos (Ley 1581 de 2012) que da un propietario o un buscador?

| Opción | Pros | Contras |
|---|---|---|
| **A. En el core, por cliente y versión del aviso, para todas las habilidades** | Una sola fuente; sirve a toda vertical | Cambio en el core |
| B. En cada pack | Sin tocar el core | Duplicado y difícil de auditar |

**Recomendación: A.** Bloquea [HU-INMO-18](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-18-captacion-de-propietarios.md).

## P-30 · Cuándo se revela la dirección exacta

¿Cuándo da el asistente la dirección exacta de un inmueble?

| Opción | Pros | Contras |
|---|---|---|
| **A. Al confirmar la visita; antes, barrio y ubicación aproximada (configurable por negocio)** | Protege al propietario y a los inmuebles ocupados | Algún cliente la pide antes |
| B. Siempre | Simple | Riesgo de seguridad y de saltarse a la inmobiliaria |
| C. Nunca por el asistente | Máxima reserva | Fricción en cada visita |

**Recomendación: A.** Bloquea [HU-INMO-17](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-17-fichas-y-verificacion-de-hechos.md) y [HU-INMO-19](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-19-visitas-con-el-asesor.md).

## P-31 · Prioridad de la vertical frente al Agent OS

¿Cuándo se ejecuta la vertical inmobiliaria, si una sola persona desarrolla y el Agent OS arranca al terminar el código del 0A (D-30)?

| Opción | Pros | Contras |
|---|---|---|
| **A. Al firmarse el piloto, intercalada con el Agent OS: las fases INMO 0 a 4 entre fases del AOS sin tocar su camino crítico, y la fase 5 tras AOS R3 y R5** | Respeta la secuencia híbrida (D-SPEC-28-3); el piloto llega antes de que termine el Agent OS | Alarga el calendario del Agent OS en lo que dure el intercalado |
| B. En paralelo con el Agent OS desde ya, sin piloto | Llega antes | Divide a la única persona y construye sin cliente |
| C. Esperar a que termine el Agent OS | Una sola cosa a la vez | La vertical llega a finales de 2027 |

**Recomendación: A.** Bloquea [HU-INMO-01](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md).
