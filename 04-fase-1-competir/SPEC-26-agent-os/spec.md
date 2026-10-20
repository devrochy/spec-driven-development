# SPEC-26 · Agent OS de procedimientos

> Estado SDD: Diseño aprobado (2026-10-08) · Fase 1 · Workstream Agent OS · Responde P-10 (D-27)
> Alineada el 2026-10-09 con los ADR-0112 a 0118 corregidos tras la revisión del arquitecto ([agent-core #402](https://github.com/devrochy/agent-core/pull/402)).
> 2026-10-17: alineada con D-35 («SolversHub vende agentes»): [HU-AOS-47](hu/HU-AOS-47-mi-agente-y-su-data.md) nueva (R4), [HU-AOS-37](hu/HU-AOS-37-cuotas-y-planes.md) achicada, 14 HU terminadas y [HU-AOS-11](hu/HU-AOS-11-conexion-canonica.md) y [HU-AOS-15](hu/HU-AOS-15-migracion-sin-regresion.md) en curso.

## Problema

- agent-core es un SO sólido **de un agente por negocio**. Hay un solo `AgentSpec` activo por negocio (`core/agents/spec.py:224`) y "vender o agendar" se decide con un playbook (`core/playbooks/enrutamiento.md`). No hay agentes por conexión ni comunicación entre agentes.
- La conexión es un inventario de credenciales, no una unidad de ejecución. El webhook identifica la conexión dueña del número para verificar la firma (ADR-0126) pero no la propaga; la conversación es del cliente y se re-asigna a la última conexión por la que escribió (`core/orchestrator/consumer.py::_resolve_conversation`). El chat web es configuración y no una conexión.
- **La consistencia no se mide ni se garantiza**:
  - la línea base de evals quedó en 34/35 y 7/8 (`09-linea-base.md`);
  - tres reglas de seguridad heurísticas escalaban compras válidas (ADR-0119 retiró dos; `calendar_completion_check` sigue en medición);
  - las secciones del flujo no restringen en runtime qué acción se llama (`docs/ASSISTANT-OS.md:200-201`).
- Agregar agentes que conversen entre sí sobre esta base multiplica estos errores. La evidencia externa (Cognition, Anthropic, τ-bench, Nubank) está en [design.md](design.md#27-lo-que-dice-la-evidencia-externa).

## Usuarios y contexto

- **Dueño del negocio** (no técnico): arma agentes desde plantillas, ajusta superpoderes y publica o vuelve atrás.
- **Persona que atiende**: toma conversaciones con el panel "En curso".
- **Cliente final**: conversa por WhatsApp, chat web y, más adelante, API, correo o Slack.
- **Master/implementador**: autor de procedimientos y de plantillas.

## Por qué importa (valor empresarial)

Permite vender SolversHub como un sistema operativo de agentes: un negocio con N conexiones y varios agentes especialistas por conexión. Además lo diferencia por lo que el mercado más castiga, la falta de consistencia: dinero siempre del servidor, nada irreversible sin confirmación, datos que no se piden dos veces, rollback en un clic y calidad medida con pass^k.

## Alcance

| Fase AOS | HU | Qué |
|---|---|---|
| R1 | [HU-AOS-01](hu/HU-AOS-01-adrs-del-agent-os.md) | ADRs del Agent OS (0112–0119) |
| R1 | [HU-AOS-02](hu/HU-AOS-02-esquema-aditivo.md) | Esquema aditivo del Agent OS (expand) |
| R1 | [HU-AOS-03](hu/HU-AOS-03-contrato-de-procedimientos.md) | Contrato procedure/1, linter y conversión de flujos |
| R1 | [HU-AOS-04](hu/HU-AOS-04-estado-de-la-conversacion.md) | Estado de la conversación: tareas event-sourced y tarjeta de estado |
| R1 | [HU-AOS-05](hu/HU-AOS-05-motor-de-procedimientos.md) | Motor de procedimientos: etapas, datos validados, precondiciones, confirmación y cierre |
| R1 | [HU-AOS-06](hu/HU-AOS-06-comandos-y-verificador-sobre-estado.md) | Comandos del hilo y verificador sobre el estado |
| R1 | [HU-AOS-07](hu/HU-AOS-07-procedimientos-de-comercio.md) | Procedimientos de comercio (planes, contratar plan, pedido con entrega) |
| R1 | [HU-AOS-08](hu/HU-AOS-08-procedimientos-de-agenda-suscripciones-y-cobranza.md) | Procedimientos de agenda, suscripciones (incluye cambio de plan) y cobranza |
| R1 | [HU-AOS-09](hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md) | Política de modelo por riesgo y confirmación con botón interactivo |
| R1 | [HU-AOS-10](hu/HU-AOS-10-kernel-del-coordinador.md) | Kernel del Coordinador: políticas, core_decisions, turn_outcomes y trazas |
| R2 | [HU-AOS-11](hu/HU-AOS-11-conexion-canonica.md) | Conexión canónica y conversación por conexión (chat web como conexión) |
| R2 | [HU-AOS-12](hu/HU-AOS-12-agentes-versionados.md) | Agentes con versiones inmutables: AgentSpec v3 y KernelSpec |
| R2 | [HU-AOS-13](hu/HU-AOS-13-instancias-por-conexion.md) | Instancias por conexión: Coordinador + General |
| R2 | [HU-AOS-14](hu/HU-AOS-14-releases-por-conexion.md) | Releases por conexión con rollback en un clic |
| R2 | [HU-AOS-15](hu/HU-AOS-15-migracion-sin-regresion.md) | Migración de todos los negocios sin regresión de pass^k |
| R3 | [HU-AOS-16](hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md) | Habilidades versionadas con procedimientos, consultas y plantillas (instalación por scope) |
| R3 | [HU-AOS-17](hu/HU-AOS-17-enrutamiento-y-modo-sombra.md) | Enrutamiento: tarea en foco, reglas, disparadores y modo sombra |
| R3 | [HU-AOS-18](hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md) | Permisos de colaboración, límites y ledger A2A |
| R3 | [HU-AOS-19](hu/HU-AOS-19-handoff-delegacion-y-consulta.md) | Handoff, delegación y consulta en el mismo hilo |
| R3 | [HU-AOS-20](hu/HU-AOS-20-colaboracion-con-pila-de-tareas.md) | Colaboración con pila de tareas |
| R3 | [HU-AOS-21](hu/HU-AOS-21-gate-de-release-pass-k.md) | Gate de release por pass^k (procedimiento, agente y ruta) |
| R3 | [HU-AOS-22](hu/HU-AOS-22-dogfooding-solvershub.md) | Dogfooding: SolversHub con Ventas, Agenda y Suscripciones |
| R3 | [HU-AOS-46](hu/HU-AOS-46-presets-v2.md) | Presets v2: plantillas de agente, reglas del Coordinador y permisos |
| R4 | [HU-AOS-23](hu/HU-AOS-23-consola-de-conexiones.md) | Consola de conexiones y hub |
| R4 | [HU-AOS-24](hu/HU-AOS-24-editor-de-agentes.md) | Editor de agentes desde plantillas |
| R4 | [HU-AOS-25](hu/HU-AOS-25-superpoderes-en-el-panel.md) | Superpoderes en el panel: recorrido, frases, textos y confirmaciones |
| R4 | [HU-AOS-26](hu/HU-AOS-26-colaboracion-en-el-panel.md) | Colaboración y enrutamiento en el panel |
| R4 | [HU-AOS-27](hu/HU-AOS-27-versiones-en-el-panel.md) | Versiones: diferencias, probar, publicar y revertir |
| R4 | [HU-AOS-28](hu/HU-AOS-28-depurador-y-en-curso.md) | Depurador conversacional y panel En curso |
| R4 | [HU-AOS-29](hu/HU-AOS-29-tablero-de-fiabilidad.md) | Tablero de fiabilidad |
| R4 | [HU-AOS-47](hu/HU-AOS-47-mi-agente-y-su-data.md) | Mi agente y su data: conversaciones, tareas, clientes y registros, consumo y consistencia por agente (D-35) |
| R5 | [HU-AOS-30](hu/HU-AOS-30-agentes-de-back-office.md) | Agentes de back-office asíncronos |
| R5 | [HU-AOS-31](hu/HU-AOS-31-auditor-de-calidad.md) | Auditor de calidad y LLM-juez calibrado |
| R5 | [HU-AOS-32](hu/HU-AOS-32-canary-y-auto-rollback.md) | Canary sticky con no-inferioridad y auto-rollback |
| R5 | [HU-AOS-33](hu/HU-AOS-33-feedback-y-propuestas.md) | Feedback y propuestas de mejora con aprobación humana |
| R5 | [HU-AOS-34](hu/HU-AOS-34-acciones-v2.md) | Acciones v2: timeouts, reintentos, circuit breaker y respaldo |
| R5 | [HU-AOS-35](hu/HU-AOS-35-cache-por-version.md) | Caché por versión de lo compilado |
| R5 | [HU-AOS-36](hu/HU-AOS-36-memoria-por-scope.md) | Memoria por scope con procedencia y olvido |
| R6 | [HU-AOS-37](hu/HU-AOS-37-cuotas-y-planes.md) | Cuotas Agent OS: operaciones entre agentes y back-office (los planes por agentes son de HU-BILL-05) |
| R6 | [HU-AOS-38](hu/HU-AOS-38-lanzamiento-comercial.md) | Lanzamiento comercial (incluye validar el nombre) |

Las evals de consistencia y el verificador ([HU-ARCH-28](../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) y [HU-ARCH-29](../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md)) se adelantan al Hito 0A en [SPEC-02](../../03-fase-0-go-live/SPEC-02-agente-confiable/spec.md). Las capacidades avanzadas (federación, sandbox, auto-mejora asistida, canales nuevos, topología, editor de estructura) están en [SPEC-27](../../05-fase-2-plus/SPEC-27-agent-os-plus/spec.md).

## Escenarios clave (Gherkin)

- **Coherencia entre agentes.** Dado una conversación que pasa del agente General a Ventas, cuando continúa, entonces el cliente no repite ningún dato que ya dio.
- **Dinero del servidor.** Dado cualquier respuesta con un monto o un link de pago, cuando se envía, entonces coincide con una acción o con el estado de la tarea.
- **Irreversible confirmado.** Dado una acción irreversible, cuando se ejecuta, entonces hay una confirmación explícita registrada antes.
- **Aislamiento.** Dado dos negocios, cuando se configura la colaboración entre agentes, entonces el esquema impide referenciar un agente del otro negocio.
- **Rollback.** Dado una versión que empeora, cuando el dueño vuelve a la anterior, entonces las conversaciones nuevas la usan en ≤ 5 s.
- **Consistencia.** Dado un superpoder publicado, cuando corre el nightly, entonces su pass^4 es ≥ 0,85.

## Decisiones

### D-SPEC-26-0 · Centro de gravedad del Agent OS

| Opción | Pros | Contras |
|---|---|---|
| **A. Procedimientos tipados sobre un estado único, en un hilo por conversación** | Consistencia: mismo estado, mismas acciones posibles; lógica de negocio en código; evoluciona el loop actual | Hay que escribir procedimientos por habilidad |
| B. Especialistas LLM independientes conversando entre sí frente al cliente | Literal a la idea de agentes que hablan | Error compuesto por salto y contexto partido; el multiagente usa ≈ 15× los tokens de un chat |
| C. Seguir con prompts y playbooks | Sin trabajo nuevo | No mejora la consistencia (34/35, 7/8, escalamientos falsos) |

**Recomendación: A.** Estado: ✅ tomada (D-28, 2026-10-08).

### D-SPEC-26-1 · Forma de la plataforma

| Opción | Pros | Contras |
|---|---|---|
| **A. Evolucionar el monolito modular (módulos nuevos en `core/`, mismo binario)** | Reutiliza loop, RLS, outbox, panel y evals; operable por 1–3 personas | Módulos nuevos dentro del core |
| B. Microservicios (gateway, kernel, runtime, broker) | Escalado independiente | Salto de red por operación; operación que el equipo no sostiene |
| C. Reescribir sobre un framework de agentes | Componentes listos | Pierde invariantes, golden sets y RLS |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-2 · Conexión canónica

| Opción | Pros | Contras |
|---|---|---|
| **A. `channel_connections` es la Conexión; `meta_connections` queda como cuenta del proveedor** | Backfill acotado; respeta ADR-0069 y ADR-0095 | Migración de datos detrás de una bandera |
| B. Tabla nueva `connections` | Modelo limpio | Toca todo el ruteo y el *sender* |
| C. Mantener el puente doble | Sin trabajo | No hay "la" conexión de un mensaje |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-3 · Unidad de conversación

| Opción | Pros | Contras |
|---|---|---|
| **A. Una conversación abierta por (conexión, cliente); la memoria del cliente es del negocio** | Un Coordinador por conexión; responde por donde escribió el cliente | Un cliente en dos números tiene dos conversaciones |
| B. Una conversación por cliente (hoy) | Una sola historia | Rompe el modelo y ya causó respuestas por el canal equivocado |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-4 · Contratos

| Opción | Pros | Contras |
|---|---|---|
| **A. `procedure/1` + AgentSpec v3 + KernelSpec v1 (major con ADR y lector tolerante de v2)** | El contrato no miente; validación en CI | Major y migración de habilidades |
| B. Todo en `extensions` | Sin ADR | Viola ADR-0050 |
| C. JSON libre | Flexible | Sin validación |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-5 · Estado de la conversación

| Opción | Pros | Contras |
|---|---|---|
| **A. Tareas *event-sourced* (`task_events`) + proyección (`conversation_tasks`)** | Reproducible, auditable y verificable en evals | Más tablas y una excepción controlada de purga |
| B. JSONB libre en `conversations.state` (hoy) | Simple | Sin validación ni historia |
| C. Solo el historial de mensajes | Nada nuevo | El modelo reconstruye el estado en cada turno |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-6 · Cómo habla el LLM con el kernel

| Opción | Pros | Contras |
|---|---|---|
| **A. Comandos como acciones del core con JSON Schema, dentro del loop actual** | Una llamada típica; reutiliza el loop | Schemas estrictos para no confundir al modelo |
| B. Siempre dos llamadas (entender → kernel → redactar) | Separación limpia | Más latencia y costo en todos los turnos |
| C. NLU clásica entrenada | Determinista | Requiere datos de entrenamiento que no hay |

**Recomendación: A (B solo en etapas de riesgo alto).** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-7 · Ejecución de los especialistas

| Opción | Pros | Contras |
|---|---|---|
| **A. Agentes del mismo hilo; delegar = agente como acción; contexto propio solo en back-office** | Coherencia y una sola voz | Menos autonomía aparente frente al cliente |
| B. Agentes con contexto propio frente al cliente | Prompts aislados | Inconsistencia documentada |
| C. Agentes remotos | Interoperabilidad | Latencia y operación |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-8 · Enrutamiento

| Opción | Pros | Contras |
|---|---|---|
| **A. Tarea en foco → reglas → disparadores → elección restringida del propio hilo → coprocesador solo con muchos candidatos** | Sin llamadas extra en la mayoría de turnos; explicable | Umbrales que calibrar |
| B. Clasificador LLM en cada turno | Simple | Costo y latencia en cada turno; no determinista |
| C. Solo reglas | Determinista | No escala al lenguaje natural |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-9 · Verificación de lo que se dice

| Opción | Pros | Contras |
|---|---|---|
| **A. Verificador determinista contra la evidencia del turno y el estado** | Barato, reproducible y medible | Parsers por tipo de afirmación |
| B. LLM-juez en línea en cada turno | Cubre matices | Costo, latencia y no determinismo |
| C. Guardrails heurísticos actuales | Ya existen | Escalan compras válidas |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-10 · Métrica de calidad

| Opción | Pros | Contras |
|---|---|---|
| **A. pass^k con usuario simulado y aserciones de estado + LLM-juez calibrado en producción** | Mide consistencia y resultado | Más cómputo en las evals |
| B. pass@1 del golden actual | Barato | Oculta la inconsistencia |
| C. Solo métricas de producción | Reales | Llegan tarde, cuando ya afectaron a clientes |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-11 · Versión y promoción

| Opción | Pros | Contras |
|---|---|---|
| **A. Versiones inmutables (agente, procedimiento, permisos; las políticas van en el KernelSpec del Coordinador, sin tablas aparte) + release por conexión con puntero** | Rollback atómico; caché por hash | Más objetos que gestionar |
| B. `is_active` por agente (hoy) | Simple | Rollback parcial |
| C. GitOps | Auditable | No apto para dueños no técnicos |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-12 · Canary

| Opción | Pros | Contras |
|---|---|---|
| **A. Porcentaje sticky por episodio de conversación decidido por el Coordinador + gate de pass^k + playground con la candidata** | Regresiones desconocidas acotadas | Necesita tráfico para decidir: sin muestra mínima la promoción es manual |
| B. Mantener ADR-0016 | Sin trabajo | Una regresión desconocida llega al 100 % |

**Recomendación: A (reemplaza en parte ADR-0016).** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-13 · Ledger A2A y aislamiento entre negocios

| Opción | Pros | Contras |
|---|---|---|
| **A. `a2a_events` append-only + FKs compuestas `(tenant_id, id)`; federación aparte con doble consentimiento** | Imposible referenciar otro negocio; auditable | Más índices |
| B. Solo RLS y trazas | Menos trabajo | Un id ajeno dentro de un JSONB pasaría |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-14 · Voz ante el cliente

| Opción | Pros | Contras |
|---|---|---|
| **A. Una voz por conexión; presentación opcional al cambiar de agente** | Coherencia de marca | Menos personalidad por área |
| B. Nombre y voz por agente | Sensación de equipo | Incoherencia de tono |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08); la presentación queda en P-12.

### D-SPEC-26-15 · Topología

| Opción | Pros | Contras |
|---|---|---|
| **A. Mantener ADR-0021 tal cual: panel y gateway+consumer se separan por rol solo cuando se cumpla su disparador** | Sin complejidad prematura | Hay que medir |
| B. Separar ya | Aislamiento | Operación sin evidencia |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

### D-SPEC-26-16 · Versionado de habilidades

| Opción | Pros | Contras |
|---|---|---|
| **A. Procedimientos y contenido congelados por versión; código = binario único; acciones rompedoras como `nombre_v2`** | Invariante 2 intacta | Acciones duplicadas por un tiempo |
| B. Varias versiones de código en un proceso | Aislamiento total | Imposible sin aislar imports |

**Recomendación: A.** Estado: ✅ tomada (2026-10-08).

Las preguntas abiertas que afectan a esta spec (P-11 a P-25) están en
[preguntas-abiertas.md](../../02-vision-y-decisiones/preguntas-abiertas.md); ninguna bloquea R1.

## Fuera de alcance

Federación entre negocios, sandbox de código no confiable, auto-mejora asistida, canal API, Slack y correo entrante, separación de topología y editor de estructura de superpoderes ([SPEC-27](../../05-fase-2-plus/SPEC-27-agent-os-plus/spec.md)). Voz en llamadas sigue en [SPEC-23](../../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/spec.md) (D-03).

## Métricas de éxito

- pass^4 ≥ 0,85 por procedimiento publicado; pass@1 ≥ 95 %.
- **0** montos o links sin evidencia; **0** acciones irreversibles sin confirmación; **0** datos perdidos al cambiar de agente.
- Precisión y recall de ruta ≥ 0,90 y ≥ 0,85; 0 bucles A2A ejecutados.
- Rollback ≤ 5 s; sobrecarga p95 del kernel ≤ 50 ms; costo por conversación ≤ +10 % frente a un agente por conexión.
- 3 de 3 dueños crean y publican un agente en < 15 min sin ayuda.

## Requerimientos cubiertos

REQ-AOS-01, REQ-AOS-02, REQ-AOS-03, REQ-AOS-04, REQ-AOS-05, REQ-AOS-06, REQ-AOS-07, REQ-AOS-08, REQ-AOS-09, REQ-AOS-10, REQ-AOS-11, REQ-AOS-12, REQ-AOS-13, REQ-AOS-14, REQ-AOS-15, REQ-AOS-17, REQ-ARCH-20, REQ-ARCH-21.
