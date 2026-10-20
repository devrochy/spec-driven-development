# Registro de decisiones

Cada decisión tiene fecha, fuente, opciones consideradas con pros y contras y la opción elegida.
Las decisiones son del cliente salvo que se diga "metodológica". Las que faltan están en
[preguntas-abiertas.md](preguntas-abiertas.md).

## Decisiones previas al encargo

### D-01 · Modelo de negocio: plataforma directa ahora, agencia después
- **Fecha / fuente**: anterior al 2026-09-28; `PLAN-COMPETENCIA-Y-PRODUCCION.md`.

| Opción | Pros | Contras |
|---|---|---|
| **A. Directa ahora, agencia después (elegida)** | Menos superficie; se aprende del cliente final; el modelo de datos queda listo para sub-cuentas | Se cede el canal de agencias a Lety mientras tanto |
| B. Agencia/white-label desde v1 | Escala por revendedores | Multiplica billing, permisos y soporte antes de tener producto probado |

### D-02 · Dos verticales en paralelo (comercio/restaurantes y cobranza con APK)
- **Fecha / fuente**: anterior al 2026-09-28; plan vigente.

| Opción | Pros | Contras |
|---|---|---|
| **A. Ambas en paralelo (elegida)** | Cobranza con APK es diferencial casi único; comercio es el mercado grande | Dos golden sets y dos runbooks |
| B. Solo comercio primero | Foco | Se pierde el diferencial de cobranza |

### D-03 · Voz en llamadas fuera de v1; notas de voz (STT) y OCR dentro
- **Fecha / fuente**: anterior al 2026-09-28; plan vigente.

| Opción | Pros | Contras |
|---|---|---|
| **A. STT + OCR en v1, llamadas en Fase 2 (elegida)** | Lo que los clientes mandan por WhatsApp son audios y fotos de comprobantes | Darwin AI ofrece voz |
| B. Todo en v1 | Paridad con Darwin | Telefonía, latencia y costos nuevos antes de vender |

## Decisiones del 2026-09-28

### D-04 · Un archivo por HU
| Opción | Pros | Contras |
|---|---|---|
| **A. Un archivo por HU (elegida)** | Enlazable desde PR; estado por HU; genera el backlog | Muchos archivos |
| B. Una tabla por fase | Compacto | No escala ni se enlaza |

### D-05 · Llave de LLM híbrida
| Opción | Pros | Contras |
|---|---|---|
| **A. Híbrida (elegida)**: la llave de plataforma es el defecto y cobra créditos a costo × margen; con llave propia (BYOK) solo se descuenta el fee de plataforma | Arranque sin fricción; margen controlado; el cliente grande trae su llave | Dos modos de costeo |
| B. Solo BYOK | Sin riesgo de costo | Fricción de alta: el pyme no tiene llave |
| C. Solo plataforma | Simple | Clientes grandes pagan sobreprecio |

### D-06 · Meta fuera de créditos
| Opción | Pros | Contras |
|---|---|---|
| **A. Meta factura directo al negocio; el panel lo muestra como información; los créditos solo cubren el fee de plantillas (elegida)** | Sin riesgo cambiario ni de crédito con Meta; coherente con ADR-0033 | El negocio ve dos facturas |
| B. Revender Meta en créditos | Una sola factura | SolversHub financia a Meta y asume cambios de tarifa como el del 2026-10-01 |

### D-07 · Precios re-derivados desde costos
| Opción | Pros | Contras |
|---|---|---|
| **A. Re-derivar desde costos con escenarios pequeño/mediano/grande (elegida)** | Margen demostrable | Puede mover precios publicados |
| B. Mantener precios y solo cambiar límites | Sin fricción comercial | Margen negativo al tope (N-13) |

Resultado en documento de precios (privado): se mantienen los precios
0/200k/600k/1,8M con créditos, porque el costo real con DeepSeek deja margen sano a escala.

### D-08 · SDD: Fases → Specs → HU (metodológica, aprobada por el cliente)
| Opción | Pros | Contras |
|---|---|---|
| **A. Fases que contienen specs; cada spec con `spec`, `design`, `tasks` y `hu/` (elegida)** | La spec es la unidad de decisión; las fases dan el orden | Temas grandes se parten en varias fases |
| B. Specs planas y la fase como atributo | Menos carpetas | Se pierde la lectura por fase |

### D-09 · Formato Spec Kit + Gherkin con constitución
| Opción | Pros | Contras |
|---|---|---|
| **A. Spec Kit + Gherkin (elegida)** | Estándar conocido; criterios verificables | Más texto |
| B. Formato libre | Rápido | Inconsistente |

### D-10 · HU con decisiones abiertas como borradores sobre la opción recomendada
| Opción | Pros | Contras |
|---|---|---|
| **A. Borrador sobre la recomendada, "sujeta a aprobación de la spec" (elegida)** | El backlog está completo hoy | Hay que revisarlas si la decisión cambia |
| B. Esperar las decisiones | Nada se reescribe | Backlog incompleto |

## Decisiones del 2026-09-30

### D-11 · Plan + suscripción como capacidad del core (actualizada por D-15)
| Opción | Pros | Contras |
|---|---|---|
| A. Evento del core (`order.paid`) que escucha cobranza | Acoplamiento mínimo | El bus es fire-and-forget; sin respuesta en el mismo turno |
| **B. Registro `SubscriptionCapability` en el core, como `payment_registry` (elegida)** | Respuesta síncrona; sirve para Free y pruebas; proveedor intercambiable; reutiliza `payment.confirmed` | Comercio conoce la bandera "recurrente" |
| C. Planes nativos en un pack de suscripciones | Modelo limpio | Duplica la mora y las promesas de cobranza |

Hoy el registro existe (`core/subscriptions/__init__.py`). La parte "cobranza es el primer
proveedor" quedó reemplazada por D-15.

### D-12 · Alta del cliente automática completa
| Opción | Pros | Contras |
|---|---|---|
| **A. El pago crea el tenant con su plan, aplica la plantilla del vertical e invita al owner; el cliente conecta WhatsApp solo (elegida)** | Escala sin el fundador; es la demo viva del producto | Exige identidad de servicio, antiabuso y Embedded Signup |
| B. Alta asistida por el master | Control | No escala; contradice "vende solo" |

### D-13 · Dos canales de cobro de plataforma con fuente única
| Opción | Pros | Contras |
|---|---|---|
| **A. Asistente (suscripción en el tenant `solvershub`) y panel (`/plan`) actualizan la misma suscripción de plataforma (`tenant_subscriptions`) (elegida)** | El cliente paga por donde quiera; dogfooding real | Sincronización y conciliación |
| B. Solo panel | Simple | El asistente no puede cobrar |
| C. Solo asistente | Dogfooding total | Sin respaldo si falla el canal |

### D-14 · Documentación en un repo nuevo `solvershub-docs`
| Opción | Pros | Contras |
|---|---|---|
| **A. Repo nuevo (elegida)** | Un dueño por tema; cruza todos los repos | Un repo más |
| B. Dentro de `solvershub-comercial` | Sin repo nuevo | Mezcla planificación técnica con material comercial |

## Decisiones del 2026-10-01

### D-15 · Dos proveedores de suscripción con un contrato único
Contexto: la implementación se apartó de D-11 y quedaron dos motores
([suscripciones-alineacion.md](../01-revalidacion/suscripciones-alineacion.md)).

| Opción | Pros | Contras |
|---|---|---|
| **A. `pack_subscriptions` (pago en línea) y la `Suscripcion` de cobranza (cobro en campo con APK) implementan la misma `SubscriptionCapability`, con los mismos estados y eventos; comercio no sabe cuál hay detrás; cada negocio elige (elegida)** | Aprovecha lo construido; cubre negocios en línea y en campo | Contrato y tests compartidos más exigentes |
| B. Solo cobranza (como decía D-11) | Un motor | Tira `pack_subscriptions`, que ya funciona con comercio |
| C. Solo `pack_subscriptions` | Simple | Pierde la mora, las promesas y la APK de cobranza |

**Consecuencia para el Hito 0A**: el tenant `solvershub` cobra con `pack_subscriptions`; cobranza
entra como segundo proveedor en el 0B (HU-SUB-15).

### D-16 · Solo Free tiene prueba
| Opción | Pros | Contras |
|---|---|---|
| **A. Free con 30 días (coherente con `core/billing`); los planes pagos se cobran desde el primer día; Free se activa al confirmar el pedido, sin cobro (elegida)** | Un solo mensaje; sin tarjetas para probar; coherente con el código | La landing y los playbooks dicen otra cosa (se corrigen) |
| B. Todos los planes con 30 días | Atractivo | Exige cobro diferido y tarjeta tokenizada, que no existen |
| C. Sin prueba | Simple | Peor que el mercado (14 días es la norma) |

### D-17 · Capacidad: 1 persona apoyada por agentes de IA
| Opción | Pros | Contras |
|---|---|---|
| **A. 1 persona + agentes, con un factor de aceleración explícito y fechas en rango (elegida)** | Realista; se recalibra con la velocidad real | Incertidumbre alta |
| B. Equipo de 3 | Fechas más cortas | No es la realidad hoy |

Detalle en [calendario-estimado.md](calendario-estimado.md).

### D-18 · Corte de la Fase 0 en dos hitos
| Opción | Pros | Contras |
|---|---|---|
| **A. Primero el Hito 0A "SolversHub vende y cobra solo", después el 0B "go-live amplio" (elegida)** | Valor visible en semanas; el propio negocio prueba el producto | Billing por créditos y media llegan después |
| B. Toda la Fase 0 de una vez | Un solo lanzamiento | Meses sin nada en producción |

## Decisiones del 2026-10-02

### D-19 · Infraestructura de producción: VPS dedicado con Coolify
- **Fecha / fuente**: 2026-10-02; [P-01](preguntas-abiertas.md#p-01--infraestructura-de-producción).

| Opción | Pros | Contras |
|---|---|---|
| **A. VPS dedicado (2 nodos) con Coolify y backups en S3 compatible (elegida)** | Reutiliza lo que ya corre en test; (costo interno); control total | La operación de Postgres es propia (se cubre con PITR) |
| B. Nube administrada (Postgres y contenedores gestionados) | HA y backups incluidos | 3–5× más caro; migrar Coolify y túneles |
| C. Seguir en la máquina de desarrollo con UPS | Gratis | Viola la invariante 9; un corte tumba a todos los clientes |

**Consecuencia**: contratar 2 nodos y un bucket S3 compatible; [HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md)
los pone en marcha y [HU-ARCH-03](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md)
cubre el PITR.

### D-20 · RPO y RTO de producción
- **Fecha / fuente**: 2026-10-02; [P-02](preguntas-abiertas.md#p-02--rpo-y-rto).

| Opción | Pros | Contras |
|---|---|---|
| **A. WAL continuo + PITR (RPO 15 min, RTO 4 h) (elegida)** | Cumple el SLO ya publicado en `security.md`; pérdida máxima acotada | Más configuración (pgBackRest o wal-g) y pruebas de restauración |
| B. Dump diario con SLO de 24 h | Simple | Se pierde hasta un día de pedidos y pagos |

**Consecuencia**: [HU-ARCH-03](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md)
implementa WAL archiving al bucket S3 y una restauración probada con evidencia.

### D-21 · Proveedor de suscripción del tenant `solvershub`
- **Fecha / fuente**: 2026-10-02; [P-03](preguntas-abiertas.md#p-03--proveedor-de-suscripción-del-tenant-solvershub).

| Opción | Pros | Contras |
|---|---|---|
| **A. `pack_subscriptions` (pago en línea) (elegida)** | Disponible en el Hito 0A; el cliente paga en línea; encaja con el comercio ya construido | No ejercita cobranza en el dogfooding |
| B. Cobranza (`Suscripcion`) | Dogfooding de cobranza; mora y promesas maduras | Llega en el 0B (HU-SUB-15); pensada para cobro en campo |

**Consecuencia**: el tenant `solvershub` cobra con `pack_subscriptions` en el 0A; cobranza entra como
segundo proveedor del mismo contrato en el 0B. Las verticales con cobradores en calle usan cobranza.

### D-22 · Modelo por defecto de la llave de plataforma
- **Fecha / fuente**: 2026-10-02; [P-05](preguntas-abiertas.md#p-05--modelo-por-defecto-con-la-llave-de-plataforma).

| Opción | Pros | Contras |
|---|---|---|
| **A. `deepseek-flash` (elegida)** | (costo por conversación); multimodal nativo; tarifa pico/valle | Hay que verificar tool calling y estabilidad |
| B. `gpt-4o-mini` | Tool calling probado | ~2× el costo de A |
| C. `claude-haiku-4-5` | Mejor calidad en español y en tools | ~8× el costo de A |

**Consecuencia**: [HU-ARCH-10](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md)
fija el ID vigente en `core/config.py`, corre el golden set y deja B como respaldo automático y C como
opción premium del negocio.

## Decisiones de spec tomadas (2026-10-02)

Las opciones y el análisis de cada una viven en el `spec.md` de su spec; aquí solo la trazabilidad.

| Decisión | Elección |
|---|---|
| [D-SPEC-01-1](../03-fase-0-go-live/SPEC-01-produccion-segura/spec.md) | A · Cloudflare Tunnel + Access sobre Coolify |
| [D-SPEC-01-3](../03-fase-0-go-live/SPEC-01-produccion-segura/spec.md) | A · Variables de Coolify + runbook de rotación en `solvershub-infra` |
| [D-SPEC-02-1](../03-fase-0-go-live/SPEC-02-agente-confiable/spec.md) | A · Jerarquía `BusinessError` en el core |
| [D-SPEC-02-2](../03-fase-0-go-live/SPEC-02-agente-confiable/spec.md) | A · Config por negocio: evento → plantilla + variables |
| [D-SPEC-05-1](../03-fase-0-go-live/SPEC-05-presets-y-flujos/spec.md) | B · Cada pack declara sus fragmentos; el preset los compone (decisión del cliente). Aplicación aprobada el 2026-10-08: el preset es un manifiesto corto en `core/presets/` que referencia los fragmentos de los packs |
| [D-SPEC-05-2](../03-fase-0-go-live/SPEC-05-presets-y-flujos/spec.md) | A · IDs de sección con namespace por pack; secciones `tenant` intocables |
| D-SPEC-06-1 | A · Un solo juego `sub_*` en el core que despacha al proveedor |
| D-SPEC-06-3 | A · Vence al inicio del período; `vencida` tras 5 días de gracia |
| [D-SPEC-07-1](../03-fase-0-go-live/SPEC-07-asistente-solvershub/spec.md) | A · Consumidor interno del core sobre `subscription.activated` con allowlist |
| [D-SPEC-07-2](../03-fase-0-go-live/SPEC-07-asistente-solvershub/spec.md) | A · Invitación sin contraseña, enlace de un solo uso por correo y WhatsApp |
| [D-SPEC-09-1](../03-fase-0-go-live/SPEC-09-comercio-confiable/spec.md) | A · `confirmar_pago_pedido(order_id)`; el link se arma en el servidor |
| [D-SPEC-09-2](../03-fase-0-go-live/SPEC-09-comercio-confiable/spec.md) | A · Campos configurables por negocio y tipo de entrega, con consentimiento |
| [D-SPEC-10-1](../03-fase-0-go-live/SPEC-10-panel-confiable/spec.md) | A · Toasts propios sobre Radix + `useConfirm` + `useAction` |
| D-SPEC-11-1 | B · Sin fee para el alta automática; fee opcional por implementación asistida |
| [D-SPEC-00-1](../03-fase-0-go-live/SPEC-00-reestructuracion/spec.md) | A · El repo del motor pasa a `solvershub-core` |
| [D-SPEC-00-2](../03-fase-0-go-live/SPEC-00-reestructuracion/spec.md) | A · Nombre nuevo + alias del viejo con ADR; IDs/base/streams/cookies no se renombran |
| [D-SPEC-00-3](../03-fase-0-go-live/SPEC-00-reestructuracion/spec.md) | A · Shim `solvershub_contracts` (diferible a Fase 1) |
| [D-SPEC-08-1](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/spec.md) | A · Lista genérica + hub por tipo de conexión |
| [D-SPEC-08-2](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/spec.md) | A · Costos de Meta opcionales por conexión con verificación |
| [D-SPEC-01-2](../03-fase-0-go-live/SPEC-01-produccion-segura/spec.md) | A · Sentry + OTLP gestionado (0B) |
| [D-SPEC-02-3](../03-fase-0-go-live/SPEC-02-agente-confiable/spec.md) | A · `side_effects=True` + canal `test` simulado (0B) |
| D-SPEC-06-2 | B · Préstamo rodante (0B) |

## Decisiones del 2026-10-03

### D-23 · Dominio final del producto
- **Fecha / fuente**: 2026-10-03; HU-GTM-01.

| Opción | Pros | Contras |
|---|---|---|
| **A. `solvershub.site` (elegida)** | Es el dominio vivo (Cloudflare/Coolify); cero migración; correos ya resuelven | No es el `.com` que mencionaba el manual de marca |
| B. `solvershub.com` | Marca "premium" | Hay que comprarlo, migrar DNS/correos y actualizar el manual |

**Consecuencia**: el manual de marca y todas las URLs usan `solvershub.site`.

### D-24 · Correos del negocio
- **Fecha / fuente**: 2026-10-03; HU-GTM-01.

| Opción | Pros | Contras |
|---|---|---|
| **A. Seis correos sobre `solvershub.site` (elegida)**: `support@`, `marketing@`, `legal@`, `facturacion@`, `privacidad@`, `seguridad@` | Cada trámite tiene su buzón; los legales publican el correcto | Seis buzones que operar |
| B. Menos correos | Menos operación | Mezcla trámites |

**Consecuencia**: el cliente crea los buzones en Cloudflare; los legales ya los referencian.

### D-25 · Fee de implementación
- **Fecha / fuente**: 2026-10-03; HU-GTM-01; confirma D-SPEC-11-1.

| Opción | Pros | Contras |
|---|---|---|
| **A. Alta automática sin fee; implementación asistida cotizada según alcance (elegida)** | Sin fricción para el autoservicio; monetiza el acompañamiento | Dos ofertas que explicar |
| B. Fee fijo para todos | Ingreso predecible | Contradice "vende solo" |

### D-26 · Entidad legal de Roshi
- **Fecha / fuente**: 2026-10-03; HU-GTM-01.

| Opción | Pros | Contras |
|---|---|---|
| **A. Arrancar como persona natural (elegida)**: Robinson Aguilar Ramirez, C.C. C.C. (oculta en version publica), Manizales (Caldas), régimen simple | Ya puede contratar y facturar; cierra el 0A sin esperar constitución | Revisar IVA/retención y re-firmar si se constituye sociedad |
| B. Constituir S.A.S. antes | Estructura más limpia | Agrega tiempo/costo antes de vender |

**Consecuencia**: los legales se redactan en clave persona natural; **⏳ pendiente revisión del abogado** antes de firmar con el primer cliente.

## Decisiones del 2026-10-08

### D-27 · Agent OS: varios agentes por conexión (responde P-10)
- **Fecha / fuente**: 2026-10-08; [P-10](preguntas-abiertas.md#p-10--asistentes-por-negocio); [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md).

| Opción | Pros | Contras |
|---|---|---|
| **A. Agent OS de procedimientos: cada conexión con un Coordinador y N agentes del mismo hilo; por fases, tras el 0A (elegida)** | Varios agentes sin perder coherencia; se vende como sistema operativo de agentes; reutiliza el motor | 47 HU nuevas; contratos v3 |
| B. Uno por negocio en v1 (recomendación anterior de P-10) | Cero trabajo | No se puede vender como Agent OS; un negocio con dos marcas necesita dos tenants |
| C. Especialistas LLM independientes conversando entre sí frente al cliente | Literal al encargo | Error compuesto por salto y contexto partido (evidencia en el diseño de [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md), §2.7) |

**Consecuencia**: [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md) (Fase 1) y [SPEC-27](../05-fase-2-plus/SPEC-27-agent-os-plus/spec.md) (Fase 2); ADR-0112 a ADR-0119 en agent-core. Los agentes especialistas son perfiles del mismo hilo y los 5 modos de colaboración se cumplen con mecanismos deterministas.

### D-28 · Fiabilidad primero: procedimientos y evals de consistencia en el 0A
- **Fecha / fuente**: 2026-10-08; revisión del diseño pedida por el cliente ("operabilidad confiable, precisa y coherente").

| Opción | Pros | Contras |
|---|---|---|
| **A. Plan B: procedimientos tipados sobre estado único; evals de consistencia (pass^k) y verificador ya en el 0A, Ola 4 (elegida)** | La calidad del 0A sube ya; el Agent OS nace confiable | +12 días-persona sin IA en el 0A |
| B. Todo el Agent OS tras el 0A | Nada nuevo en el 0A | La consistencia se sigue midiendo con un intento |
| C. Todo ya, en paralelo al 0A | Agent OS antes | El 0A se corre y hay choques en el corazón del turno |

**Consecuencia**: [HU-ARCH-28](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) y [HU-ARCH-29](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md) entran a [SPEC-02](../03-fase-0-go-live/SPEC-02-agente-confiable/spec.md) (Ola 4, después de HU-SUB-07); [HU-SH-08](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md) depende de [HU-ARCH-28](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md). El resto del Agent OS empieza al cerrar el 0A.

### D-29 · Capacidad y entregable del rediseño
- **Fecha / fuente**: 2026-10-08; encargo de rediseño (roadmap ejecutable por 3–8 personas) frente a D-17.

| Opción | Pros | Contras |
|---|---|---|
| **A. Dos calendarios (1 persona + IA, D-17; y equipo de 3) y entregable SDD + ADR por PR (elegida)** | Honesto con la capacidad real; trazable | Más texto |
| B. Solo D-17 | Simple | No muestra el efecto de sumar personas |
| C. Equipo de 3–8 asumido | Fechas cortas | Contradice D-17 |

**Consecuencia**: [calendario-estimado.md](calendario-estimado.md#agent-os-d-27-a-d-29) suma el escenario de 3 personas para el Agent OS.

## Decisiones del 2026-10-09

### D-30 · El Agent OS arranca al terminar el código del 0A
- **Fecha / fuente**: 2026-10-09; pedido del dueño. El VPS ([HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md)) y la revisión del abogado (HU-GTM-02) tardan, y el criterio de salida del 0A depende de ellos. Ajusta la consecuencia de D-28.

| Opción | Pros | Contras |
|---|---|---|
| **A. El código del Agent OS arranca cuando esté mergeado el código del 0A. Los trámites del dueño y las verificaciones que dependen de ellos siguen en paralelo (elegida)** | El Agent OS no espera a terceros; el corazón del turno ya está estable (ARCH-28/29) | El 0A se cierra formalmente después de que el Agent OS ya empezó |
| B. Esperar al cierre formal del 0A (D-28) | Una sola cosa a la vez | Semanas parados por trámites externos |
| C. Arrancar ya | Lo más rápido | Choca con ARCH-29 en el loop y los guardrails; contradice D-28 |

**Qué es "código del 0A terminado"** (todo mergeado en `develop`, con tests y revisión):
- Calidad: [HU-ARCH-29](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md) y [HU-SH-08](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md). Las 3 noches de golden ≥95 % (SH-08 y HU-SUB-12) se miden en paralelo.
- Conexiones: [HU-CONN-03](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-03-ciclo-de-vida-seguro.md), [HU-CONN-05](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md), [HU-CONN-06](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-06-byok-produccion.md), [HU-CONN-07](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-07-checklist-produccion-real.md) y el código de [HU-SH-05](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md) (cierra también [HU-CONN-01](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md)). El alta real con Meta (App Review, `config_id`, `META_APP_ID`) y el alta BYOK de producción quedan como verificación pendiente.
- Alta automática: el código de [HU-SH-07](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-07-antiabuso-y-cumplimiento.md) (un Free por persona, aceptación versionada, revisión, interruptor y límites). Los textos legales definitivos llegan con HU-GTM-02 como una versión nueva.

**Fuera de la condición** (siguen en paralelo, del lado del dueño): ARCH-01, ARCH-02, ARCH-03, GTM-02, GTM-03, los pendientes de ARCH-04 y las verificaciones a mano en test y producción.

**Consecuencia**: al cumplirse la condición, [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md) arranca por R1 ([HU-AOS-01](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-01-adrs-del-agent-os.md)) y sus issues se crean entonces. Una HU de AOS no se mergea a `main` (release) con un defecto 🔴 abierto del 0A. El cierre formal del 0A y su retro siguen pendientes hasta cumplir su criterio de salida.

### D-31 · Vertical inmobiliaria (InmoAgent) especificada, con piloto como condición del código
- **Fecha / fuente**: 2026-10-09; encargo "prompt maestro InmoAgent" del dueño, adaptado a la arquitectura de agent-core y al Agent OS planificado (D-27); [SPEC-28](../04-fase-1-competir/SPEC-28-inmoagent/spec.md).

| Opción | Pros | Contras |
|---|---|---|
| **A. Especificar [SPEC-28](../04-fase-1-competir/SPEC-28-inmoagent/spec.md) ahora; el código del pack inmobiliario espera un piloto firmado; las HU genéricas entran cuando otra HU las consume (elegida)** | Backlog listo sin escribir un pack especulativo (skill `new-pack`); deja a la vista brechas genéricas del core | La vertical depende de cerrar un piloto |
| B. No especificar hasta tener cliente | Cero trabajo especulativo | Al llegar el cliente no hay plan |
| C. Construir ya el pack completo | Llega antes al mercado | Compite con el Agent OS por la única persona y contradice `new-pack` |

**Alcance elegido por el dueño**:
- Arriendos v1: contrato como registro más cobro del canon con pack-subscriptions y Wompi, con recordatorios y mora. Sin PDF, firma ni liquidación al propietario.
- Secuencia híbrida: datos, búsqueda geo y habilitadores sobre el motor actual; procedimientos y especialistas cuando lleguen AOS R1 y R3; back-office y memoria con AOS R5.
- Los 7 "subagentes" del encargo se traducen a Coordinador, 3 especialistas en un hilo, procedimientos tipados, acciones del servidor y back-office que solo propone. No hay agentes LLM independientes frente al cliente (D-27).

**Consecuencia**: [SPEC-28](../04-fase-1-competir/SPEC-28-inmoagent/spec.md) con 30 HU (≈ 139 días-persona sin IA), REQ-INMO-01 a REQ-INMO-12 y las preguntas P-26 a P-31. La revisión del arquitecto y del auditor multitenant del mismo día sacó lo genérico con consumidor real a otras specs: el botón a [HU-AOS-09](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md), las extensiones de procedimientos a [HU-AOS-03](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md), los presets v2 a [HU-AOS-46](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) ([SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md), +4 días) y el cobro en horario legal a HU-SUB-18 (SPEC-06, +1,5 días). No cambia el calendario del Agent OS (D-30): la vertical se agenda cuando P-26 y P-31 tengan respuesta.

## Decisiones del 2026-10-10

### D-32 · Sistema de diseño unificado para panel y app (SPEC-29)
- **Fecha / fuente**: 2026-10-10; encargo de rediseño del dueño ("panel empresarial, interactivo y consistente entre web y APK", manteniendo las vistas de campo de cobranza) y revisión una por una de las decisiones de [SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md).

| Opción | Pros | Contras |
|---|---|---|
| **A. Aprobar [SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md) con las recomendaciones de cada decisión (elegida)** | Se puede ejecutar desde [HU-DS-01](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-01-tokens-v2.md); corrige el contraste AA que hoy no se cumple; una sola base visual para [SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md), [SPEC-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md) y la app | 72 días-persona más en la fase 1 |
| B. Hacer solo arreglos puntuales de contraste | Barato | El panel y la app siguen divergiendo; [SPEC-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md) se construye con el kit viejo |
| C. Posponer el rediseño hasta después del Agent OS | No compite con el 0A | La primera impresión en las demos sigue débil |

| Decisión | Elegida |
|---|---|
| D-SPEC-29-1 | A · [SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md) es la base visual; [SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md) define el menú, [SPEC-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md) las vistas. [HU-UI-07](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) queda como contrato de datos y [HU-UI-08](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-08-filtros-y-tablas.md) depende de [HU-DS-03](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-03-kit-de-componentes-panel.md) |
| D-SPEC-29-2 | A · Primitivas SVG propias sobre `d3-scale`/`d3-shape` (y `react-native-svg` en la app) |
| D-SPEC-29-3 | A · Catálogo vivo en `/catalogo` (solo desarrollo y test) y pantalla Catálogo en builds de desarrollo de la app |
| D-SPEC-29-4 | A · Cookie `panel_sidebar` para la barra lateral y `localStorage` por usuario y negocio para los widgets |
| D-SPEC-29-5 | A · Panel en la app con 4 destinos + Más (Inicio, Atención, pack principal, Buscar) |
| D-SPEC-29-6 | A · El campo de cobranza conserva vistas, flujo, rutas y lógica (pedido del dueño) |
| D-SPEC-29-7 | A · Perfil del Resumen derivado de los permisos, sin roles nuevos |
| D-SPEC-29-8 | A · Seguir con Expo (React Native), ya elegido en [SPEC-25](../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md) |
| D-SPEC-29-9 | A · Bento con superficies sólidas, sin glassmorphism |

**Consecuencia**: [SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md) pasa a `Diseño aprobado` y sus 12 HU cumplen el DoR de spec. La ejecución arranca por [HU-DS-01](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-01-tokens-v2.md) (tokens v2) en `solvershub-panel`.


### D-33 · Centro de pruebas con rol tester solo en test (SPEC-30)
- **Fecha / fuente**: 2026-10-13; pedido del dueño ("que los tester puedan entrar y puedan ejecutar las acciones de un master pero el único acceso al que no puede tener es al de colaboradores"; prueba "muy interactiva, un paso a paso", con lista lateral, progreso e informe final) y respuestas a las decisiones de [SPEC-30](../04-fase-1-competir/SPEC-30-centro-de-pruebas/spec.md).

| Opción | Pros | Contras |
|---|---|---|
| **A. Aprobar [SPEC-30](../04-fase-1-competir/SPEC-30-centro-de-pruebas/spec.md) con tester = master en la operación y dueño en Colaboradores, solo en test, ejecución por tester con capturas e informe (elegida)** | Los testers prueban el producto completo con cuenta propia; evidencia e informe por persona; producción no cambia | Hay que revisar cada chequeo de master y guardar capturas |
| B. Tester con acceso solo a la sección Pruebas | Riesgo mínimo | No puede ejecutar las pruebas del panel |
| C. Seguir solo con el artifact | Ya existe | Sin capturas, sin informe por tester y los externos solo leen |

| Decisión | Elegida |
|---|---|
| D-SPEC-30-1 | A · Catálogo en `11-pruebas/catalogo.yaml` de docs, importado al panel |
| D-SPEC-30-2 | A · Rol `tester` = master en la operación y dueño del negocio activo en Colaboradores (habilitada el mismo día "para hacer las pruebas de esta sección"), solo con `QA_TESTERS_ENABLED` (test); en producción el login falla |
| D-SPEC-30-3 | A · Pruebas de la plataforma, no de cada negocio |
| D-SPEC-30-4 | B · Nota y capturas adjuntas por paso, en `TENANTS_ROOT/.plataforma/pruebas/` |
| D-SPEC-30-5 | A · Una ejecución por tester y ciclo; informe guardado en el panel, correo al dueño y descarga |

**Consecuencia**: [SPEC-30](../04-fase-1-competir/SPEC-30-centro-de-pruebas/spec.md) pasa a `Diseño aprobado` con 6 HU (suma [HU-QA-06](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-06-catalogo-historico-del-proyecto.md), el catálogo histórico). La ejecución arranca por el esquema v2 del catálogo y [HU-QA-01](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-01-modelo-y-api-de-pruebas.md) en agent-core.


## Decisiones del 2026-10-14

### D-34 · Panel en la app con cajón lateral y tema oscuro por defecto (reemplaza a D-SPEC-29-5)
- **Fecha / fuente**: 2026-10-14; pedido del dueño ("queremos menú de hamburguesa, con la lista de opciones así como se hace en el panel y con tema dark y light como en el panel"; "obviemos D-SPEC-29-6 [para el tema] y mantengamos el diseño que hay en cobranza pero entonces mantener el azul del dark en el fondo y en los componentes") al validar las tareas de la app y querer avanzar en interfaz porque probar el panel en la app con 8 pestañas era una pérdida de tiempo.

| Opción | Pros | Contras |
|---|---|---|
| **A. Header con hamburguesa y cajón lateral con la misma lista agrupada que el sidebar del panel web (lo que el panel hace por debajo de 768 px); secciones dentro de grupos plegables, packs plegados al arrancar; tema oscuro por defecto en toda la app, campo incluido (elegida)** | Paridad exacta con el panel web; las ~40 secciones caben; cero dependencias nativas (el cajón de campo ya era `Animated` + `Pressable`), así que sale por OTA; una sola convención de navegación en la app | Las secciones más usadas quedan detrás de un toque; los gestores ven el campo en oscuro de golpe tras la OTA (conservan el toggle «Modo claro» y la preferencia guardada) |
| B. Mantener D-SPEC-29-5: 4 destinos + Más, y agregar solo el toggle de tema | Destinos de primer nivel a un toque | Diverge del panel web; lo que no cabe en 4 destinos sigue a dos toques; había que decidir qué es «el pack principal» |
| C. Híbrido: 4 destinos + hamburguesa en lugar de «Más» | Lo mejor de A y B | Dos convenciones a la vez; más superficie que mantener |

| Decisión | Elegida |
|---|---|
| Navegación del panel en la app | A · header + cajón lateral; **D-SPEC-29-5 queda reemplazada** |
| Profundidad del cajón | Secciones en grupos plegables, como `nav.ts` del panel; cada sección abre el módulo en su pestaña interna |
| Tema | Oscuro por defecto como el panel web (no sigue al sistema), en toda la app incluido el campo; el toggle vive en el header del panel, en el cajón y en el menú lateral del campo; quien ya eligió un tema lo conserva |
| Campo de cobranza | D-SPEC-29-6 se mantiene para vistas, flujo y rutas; solo arranca en oscuro con el navy de los tokens |
| Alcance de la primera iteración | Shell + tema + bus de navegación + e2e; las pantallas del panel en la app no se migran al kit; el Resumen móvil por rol pasa a [HU-DS-13](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-13-resumen-movil-por-rol.md) (depende de [HU-DS-07](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-07-resumen-modular-por-rol.md)) |

**Consecuencia**: [HU-DS-11](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-11-shell-del-panel-en-la-app.md) se reescribe (solo depende de [HU-DS-09](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-09-kit-de-componentes-app.md)) y nace [HU-DS-13](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-13-resumen-movil-por-rol.md); ADR-APP-07 de la app queda enmendado. Código: apk #156 (tema oscuro), #157 (`Drawer` al kit) y #158 (shell con cajón). [HU-ARCH-08](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-08-apk-a-produccion.md) se marca absorbida por [SPEC-25](../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md) ([HU-APP-06](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-06-almacenamiento-local-cifrado.md), [HU-APP-16](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-16-seguridad-de-la-app.md) y [HU-APP-17](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-17-release-firmado-y-guias.md) ya cubren sus criterios y sus notas contradecían a [SPEC-25](../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md)).

## Decisiones del 2026-10-17

### D-35 · SolversHub vende agentes
- **Fecha / fuente**: 2026-10-17; pedido del dueño al priorizar el corazón del proyecto («SolversHub vende agentes: cada negocio tiene sus agentes —ventas, cobranza, agendamiento…— con su configuración y un agente core que los orquesta; el cliente entra a SolversHub a consultar su agente y la data que construyó; los planes cobran por agentes, crédito de uso y colaboradores; no se afinan requerimientos que no estén sincronizados con ese objetivo»), tras leer el ciclo de pruebas «2026-10-13 · catálogo v5»; [P-10](preguntas-abiertas.md#p-10--asistentes-por-negocio), [P-13](preguntas-abiertas.md#p-13--empaquetado-del-agent-os-en-los-planes) y [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md).

| Opción | Pros | Contras |
|---|---|---|
| **A. La unidad que se vende y se configura es el agente del negocio; un Coordinador por conexión los orquesta; las habilidades son capacidades que se le dan a un agente; los planes cobran por agentes publicados, crédito mensual y colaboradores (elegida)** | Coincide con lo que el dueño vende y con lo que [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md) ya construye (agentes versionados, instancias por conexión, releases); el cliente entiende qué compra («mi agente de ventas») y qué ve (su data); una sola unidad para planes, panel y landing | Reescribir la oferta (modelo de precios §5, HU-BILL-05, landing) y parquear las specs que venden packs o pantallas por habilidad; plomería nueva (`agent_instance_id` en el ledger, las conversaciones y las tareas) |
| B. Seguir vendiendo presets y habilidades (packs) con un asistente por negocio | Nada que cambiar en docs ni en billing | Contradice la visión del dueño y lo que [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md) construye; «habilidades activas» es un tope que el cliente no entiende; «asistentes por negocio = 1» ya era falso desde D-27 |
| C. Agentes como add-on pagado sobre un asistente base (P-13, opción B) | Ingreso extra por agente | Fricción y otra factura; Free no tendría agentes y no habría nada que probar |

> **D-35 · SolversHub vende agentes.** La unidad que se vende y se configura es el **agente** del negocio (Ventas, Cobranza, Agenda, Suscripciones, personalizados), no el pack ni el preset. Cada negocio define sus agentes con su configuración (identidad, proveedor y modelo, superpoderes, memoria, reglas) y un **Coordinador** por conexión los orquesta en el mismo hilo (mantiene D-27 y D-SPEC-26-2/3: el Coordinador es por conexión; los agentes se definen por negocio y se despliegan como instancias en una o más conexiones). **Un agente publicado debe tener al menos una conexión.** El cliente entra a SolversHub a ver cada agente y la data que construyó. Las habilidades (packs) pasan a ser capacidades que se le dan a un agente. Los planes cobran por agentes publicados, crédito mensual de uso y colaboradores (ver modelo de precios §5). Supersede P-10, P-13 y la línea de valor de [HU-FWK-02](../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-02-adr-presets.md) («el preset es la unidad que se vende»).

| Matiz | Cómo queda |
|---|---|
| «Agente core del negocio» (frase del dueño) frente a «Coordinador por conexión» (ADR-0112/0115, D-SPEC-26-2 y D-SPEC-26-3) | **Coordinador por conexión = el agente core del negocio instanciado en cada conexión.** Se define una vez por negocio (reglas, presupuestos, KernelSpec) y corre una instancia por conexión, que es donde enruta, confirma y responde |
| Unidad facturable | Agente publicado del negocio con **al menos una instancia en una conexión** (`agents` activos con instancia; no se cuentan filas de `agent_instances`). El General cuenta; el Coordinador no |
| Conexiones | 1 incluida por agente; las adicionales son una dimensión del plan (propuesta en el modelo de precios §5) |
| Habilidades (packs) | Capacidades que se le dan a un agente (instalación por scope, [HU-AOS-16](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md)); dejan de ser tope de plan y unidad vendible |
| Presets | Instalan agentes «para un fin» ([HU-AOS-46](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md)); no son la unidad que se vende |
| Cifras por plan | Las dimensiones (agentes, crédito, colaboradores) las confirmó el dueño; las cifras por plan y las dimensiones extra son **propuesta para validar con el dueño** |

**Consecuencia**: P-10 y P-13 cerradas, y P-21 cerrada para [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md). documento de precios (privado) §5 reescrito; HU-BILL-05 trae agentes publicados, crédito, colaboradores y conexiones (se retiran «habilidades activas» y «asistentes por negocio»); [HU-AOS-37](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-37-cuotas-y-planes.md) se achica a operaciones entre agentes y back-office; HU-BILL-08 describe los planes por agentes con la barra de crédito; [HU-FWK-02](../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-02-adr-presets.md) y [arquitectura-objetivo.md](arquitectura-objetivo.md) cambian el lenguaje de packs a agentes. Specs **parqueadas** (fuera del calendario y de los totales; se retoman por decisión): [SPEC-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md), [SPEC-14](../04-fase-1-competir/SPEC-14-billing-extras/spec.md) salvo [HU-BILL-12](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-12-cambio-de-plan-y-anual.md), [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md), [SPEC-18](../04-fase-1-competir/SPEC-18-pack-commerce-v2/spec.md) y [SPEC-21](../05-fase-2-plus/SPEC-21-agencia-e-internacional/spec.md); [SPEC-16](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/spec.md) y [SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md) se reorientan (habilidad = capacidad de un agente; menú Asistente → Agentes · Superpoderes · Calidad); [SPEC-28](../04-fase-1-competir/SPEC-28-inmoagent/spec.md) encaja (D-31) y espera piloto. Nace [HU-AOS-47](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md) «Mi agente y su data» (R4) y [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md) se pone al día (14 HU terminadas, [HU-AOS-11](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-11-conexion-canonica.md) y [HU-AOS-15](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md) en curso). Código pendiente (PR chico de core): métricas `agentes` y `colaboradores` en `core/billing/metrics.py` con enforcement al publicar o instanciar un agente y al invitar un colaborador; `/admin/plan` las expone y el panel las muestra con la barra de crédito.

## Decisiones del 2026-10-19

> D-36 está reservada para las decisiones cortas de la sección B de [10-pendientes-del-dueno.md](../10-pendientes-del-dueno.md#b--decisiones-cortas); por eso el menú se cierra como D-37.

### D-37 · Menú v2 del panel por tarea con fichas por objeto
- **Fecha / fuente**: 2026-10-19; pedido del dueño de mejorar la navegación del panel (un dueño con todos los packs ve 40 entradas en 8 grupos en `nav.ts` de `origin/main`) y aprobación de ampliar [SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md) en lugar de abrir una spec nueva. Cierra las opciones A/B/C de [arquitectura-informacion-panel.md](arquitectura-informacion-panel.md#opciones), que seguían ⏳, y usa el lenguaje de [D-35](#d-35--solvershub-vende-agentes). Base: el informe del ciclo [2026-10-13](../11-pruebas/informes/ciclo-2026-10-13.md) (7 fallas de «diseño del shell» y notas de «no encuentro»).

| Opción | Pros | Contras |
|---|---|---|
| **A. Por tarea, ≤ 12 entradas, fichas por objeto (conexión y agente) con pestañas dentro (elegida)** | Lo entiende cualquier dueño; cada cosa de una conexión vive en su ficha y no en páginas globales; el agente queda a un toque (D-35); escala a packs nuevos como pestañas; un solo cambio en `nav.ts` se propaga a migas, pestañas y paleta | Mueve casi todo de lugar; exige redirecciones y reestructurar Agenda, Conexiones, Cobranza y Comercio en HU siguientes |
| B. Por habilidad (un grupo por pack, como hoy) | Fácil de generar desde el manifiesto | El dueño piensa en tareas, no en packs; sigue en ~40 entradas; contradice D-35 (la habilidad es capacidad de un agente, no sección) |
| C. Mantener los grupos y solo renombrar | Cambio mínimo | No resuelve lo de Meta, ni la Agenda en 5 entradas, ni la falta de enlace entre agentes y conexiones |

| Decisión | Elegida |
|---|---|
| Primer nivel | 4 grupos y 11 entradas: **Operación** (Resumen, Conversaciones, Clientes) · **Tu asistente** (Agentes, Conexiones) · **Negocio** (Agenda, Ventas, Cobranza) · **Cuenta** (Consumo y plan, Equipo, Configuración), más **Plataforma** solo para master. Agenda, Ventas y Cobranza solo si el negocio tiene la habilidad. Desaparece «Herramientas». El menú v2 solo reagrupa: ninguna URL cambia; las rutas se mueven después con sus redirecciones |
| Agentes ↔ Conexiones | Muchos a muchos: no se anidan, se enlazan en las dos direcciones. Ficha del agente con pestaña **Conexiones** (conexión, tipo, rol, prioridad, principal, estado; hoy solo dice «Atiende en …»); ficha de la conexión con pestaña **Agentes** |
| Conexiones | Ficha `/conexiones/[id]` con pestañas por tipo; **Salud solo en las conexiones Meta**; WhatsApp Web (QR) con Vinculación · Estado · Agentes; la configuración de Google, Wompi, chat web y SMTP pasa a la ficha de su conexión |
| Agenda | Una entrada con Calendario · Tipos de cita · Horario; los bloqueos se crean sobre el calendario; cada tipo de cita con color o identificador |
| Cobranza y Ventas | Una entrada cada una; las páginas de hoy pasan a pestañas. Ventas suma Suscripciones |
| Configuración | Absorbe Mensajes fallidos y Habilidades (packs); toma el objetivo de [HU-UI-09](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-09-configuracion-por-pestanas.md) |
| Nombres | Superpoderes = capacidades del agente; Habilidades = packs; Clientes (ex Leads); Mensajes fallidos (ex DLQ); Negocios (ex Tenants) |
| App móvil | El cajón de D-34 sigue la misma lista ([HU-UX-11](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md)) |

**Consecuencia**: [SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md) se amplía con el árbol v2 y sus escenarios, y su [diseño](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/design.md) trae el análisis por sección y la tabla de redirecciones (la de [arquitectura-informacion-panel.md](arquitectura-informacion-panel.md) queda como antecedente). [HU-UX-02](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) se reescribe (solo reagrupa, sin cambiar URLs) y sin depender de [HU-CONN-08](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md) (el hub de Meta pasa a [HU-UX-09](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-09-ficha-de-conexion-por-tipo.md)). Nacen [HU-UX-08](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-08-agenda-unificada.md) (Agenda unificada), [HU-UX-09](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-09-ficha-de-conexion-por-tipo.md) (ficha de conexión por tipo, con el arreglo del diálogo «Agregar conexión»), [HU-UX-10](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-10-cobranza-y-ventas-en-pestanas.md) (Cobranza y Ventas en pestañas) y [HU-UX-11](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md) (cajón de la app), con REQ-UX-12 a REQ-UX-15. [SPEC-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md) registra que este rediseño absorbe [HU-UI-09](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-09-configuracion-por-pestanas.md); las pestañas Conexiones y Superpoderes de la ficha del agente ([HU-AOS-47](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md), terminada) las agrega [HU-UX-09](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-09-ficha-de-conexion-por-tipo.md). Antes del código va un prototipo clicable del menú v2 para que el dueño lo revise.

### D-38 · SPEC-31 Mejoras del ciclo de pruebas
- **Fecha / fuente**: 2026-10-19; pedido del dueño de identificar y planificar las mejoras que dejó como tester (`master@demo.test`) en el ciclo [2026-10-13](../11-pruebas/informes/ciclo-2026-10-13.md): 97 notas y 2 capturas, más una nota del ciclo «Release 2026-10-17». El informe había mandado las de diseño y UX a un «backlog de [SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md)» que el spec no tiene, y el dueño pidió revisar en particular lo que hace hoy agent-sale en conversaciones, leads y escalaciones.

| Opción | Pros | Contras |
|---|---|---|
| **A. Una spec nueva que agrupa todo lo que quedó sin plan, con HU propias (elegida)** | Cada nota tiene dueño y prueba de cierre; se ejecuta por olas; el inventario nota → HU queda en un solo lugar | Una spec más; algunas HU tocan áreas de otras specs |
| B. Repartir cada mejora en su spec dueña ([SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md), [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md), [SPEC-14](../04-fase-1-competir/SPEC-14-billing-extras/spec.md), [SPEC-25](../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md)) | Sin spec nueva | Vuelve a dispersar lo que se perdió por estar disperso; [SPEC-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md) y [SPEC-14](../04-fase-1-competir/SPEC-14-billing-extras/spec.md) están parqueadas |

| Decisión | Elegida |
|---|---|
| Alcance | 11 HU: [HU-UX-12](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-12-arreglos-rapidos-del-ciclo.md) a [HU-UX-20](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-20-apk-lo-que-falto-del-ciclo.md), [HU-AOS-48](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-AOS-48-onboarding-con-guion-por-agente.md) y [HU-AOS-49](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-AOS-49-pack-de-conocimiento.md). Entran las tres piezas grandes que eligió el dueño: centro de notificaciones, pack de conocimiento (RAG) y onboarding con guion |
| De agent-sale | Se toman la bandeja de dos columnas, los tickets (tomar, resolver, devolver al bot), la lista cerrada de motivos y la ficha de cliente con pausa por cliente, clasificación, filtros y CSV. agent-sale no tiene tiempo real: la bandeja en vivo se construye nueva |
| Tiempo real | Polling con `?after=` y la pestaña visible (D-SPEC-31-1); SSE solo si la carga lo pide |
| Clasificación del cliente | La aporta pack_commerce por `lead_registry`, calculada al vuelo (D-SPEC-31-2) |
| Orden | Olas: UX-12 y UX-17 → UX-13 y UX-16 → UX-15 → UX-14 y UX-18 → UX-19, AOS-48, AOS-49 y UX-20; despliegue en test y ciclo de pruebas después de cada ola |
| Fuera de alcance | La alerta de crédito por WhatsApp o push ([HU-BILL-09](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-09-avisos-de-consumo.md)) sigue parqueada; queda anotado que `GET /admin/plan` devuelve el crédito con `used: null` |
| Preguntas abiertas para el dueño | Proveedor de LLM por agente o por negocio (D-SPEC-31-3, se recomienda por negocio con el costo por mensaje a la vista); el panel clásico se descontinúa o se arregla; tipo de búsqueda del RAG (lo cierra el ADR de [HU-AOS-49](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-AOS-49-pack-de-conocimiento.md)) |

**Consecuencia**: nace [SPEC-31](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/spec.md) con su [inventario](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/design.md#inventario) nota por nota y REQ-UX-16 a REQ-UX-23, REQ-AOS-18 y REQ-AOS-19. [HU-AOS-28](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md) queda con el depurador (la bandeja en vivo pasa a [HU-UX-15](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-15-bandeja-de-conversaciones.md)); [HU-AOS-16](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md) aclara que las habilidades viven en su pack; [HU-AOS-24](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) anota el costo por mensaje; [HU-COM-09](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-09-modificar-pedido.md) recoge la nota del agente al cancelar o modificar un pedido. El informe del ciclo apunta a [SPEC-31](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/spec.md) en lugar del «backlog de [SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md)».
