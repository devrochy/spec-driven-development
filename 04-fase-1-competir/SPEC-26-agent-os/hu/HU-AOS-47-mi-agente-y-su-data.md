---
id: HU-AOS-47
titulo: "Mi agente y su data"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-AOS-13, REQ-AOS-17]
dependencias: [HU-AOS-15, HU-AOS-23]
skills: ["panel-ui", "frontend-design", "backend-design:query-discipline", "auditor-multitenant"]
estado: terminada
---

# HU-AOS-47 · Mi agente y su data

> Estado SDD: Terminada (2026-10-18, tanda 7) — [SPEC-26](../spec.md). Nace de [D-35](../../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes) (2026-10-17): el cliente entra a SolversHub a ver cada agente y la data que construyó.

**ID:** HU-AOS-47

**Título:** Mi agente y su data

**Workstream:** Agent OS

**Historia:** Como dueño de un negocio quiero abrir cada uno de mis agentes (Ventas, Cobranza, Agenda…) y ver lo que hizo y construyó —sus conversaciones, sus tareas en curso y cerradas, los clientes y leads que atendió, los pedidos, citas y promesas de pago que creó, su consumo y su consistencia— para saber qué me está rindiendo cada agente que pago.

**Por qué importa (valor empresarial):** Es la promesa de D-35 hecha pantalla: lo que se vende es el agente y el cliente tiene que poder ver «su» agente y su data. Sin esta vista, los planes por agentes cobran algo que el dueño no puede mirar, y la decisión de subir de plan (otro agente, más crédito) no tiene en qué apoyarse.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-13, REQ-AOS-17

**Dependencias:** [HU-AOS-15](HU-AOS-15-migracion-sin-regresion.md), [HU-AOS-23](HU-AOS-23-consola-de-conexiones.md)

**Criterios de aceptación (Gherkin):**
- **Vista por agente.** Dado un negocio con los agentes Ventas y Agenda publicados, cuando el dueño abre Agentes → Ventas, entonces ve sus conversaciones (con la conexión y la versión que atendió cada una), sus tareas en curso y cerradas, los clientes y leads que atendió y los pedidos, citas y promesas de pago que creó, sin mezclar lo del otro agente.
- **Consumo y consistencia.** Dado el mismo agente, cuando abre su pestaña de consumo, entonces ve los créditos del período atribuidos a sus instancias (`usage_ledger.agent_instance_id`), el desglose por conexión y su pass^4 vigente con tendencia ([HU-AOS-21](HU-AOS-21-gate-de-release-pass-k.md) cuando exista; antes, la última medición de [HU-ARCH-28](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md)).
- **Plomería del turno.** Dado un turno atendido por una instancia, cuando se escriben el ledger, la conversación y la tarea, entonces quedan `usage_ledger.agent_instance_id`, `conversations.active_agent_instance_id` y `owner_instance_id` en la tarea; y dado un registro creado por una acción del agente (pedido, cita, promesa), entonces conserva qué instancia lo creó.
- **API por agente.** Dado `GET /admin/agents/{id}/conversations`, `/tasks`, `/records` y `/usage`, cuando se consultan con permiso de ver agentes, entonces responden paginados, filtrables por conexión y período, y solo con datos del negocio (RLS); y dado `GET /admin/plan`, cuando se consulta, entonces trae agentes publicados, colaboradores y crédito del período contra los topes de HU-BILL-05.
- **Aislamiento.** Dado dos negocios, cuando uno consulta un agente del otro por id, entonces recibe 404 y nada se filtra en el cuerpo ni en los logs.
- **Sin data todavía.** Dado un agente recién publicado, cuando el dueño lo abre, entonces ve un estado vacío que explica qué va a aparecer y cómo probarlo (el chat web de su conexión), no una tabla en blanco.

**Evidencia / Definición de Terminado:**
- Migración aditiva: `owner_instance_id` en las tareas y procedencia de instancia en los registros creados por acciones (pedidos, citas, promesas); el loop escribe `usage_ledger.agent_instance_id` y `conversations.active_agent_instance_id` en cada turno (hoy nunca se escriben).
- Endpoints `GET /admin/agents/{id}/{conversations,tasks,records,usage}` y `/admin/plan` con las métricas `agentes` y `colaboradores`; API y tipos generados; tests de aislamiento entre negocios.
- Sección **Agentes** del panel con la vista por agente (pestañas: Conversaciones, Tareas, Clientes y registros, Consumo y calidad) según `DESIGN.md`; capturas en claro, oscuro y móvil; prueba en el centro de pruebas (área Agentes).

**Implementada (2026-10-18, tanda 7):** sección Agentes con la ficha del agente («Atiende en …» con sus conexiones) y sus pestañas. PR [core #476](https://github.com/devrochy/agent-core/pull/476) + [panel #82](https://github.com/devrochy/solvershub-panel/pull/82).

**Riesgos/Notas:**
- Nació en la lectura del ciclo de pruebas 2026-10-13 y en D-35 (2026-10-17); va en la tanda 7 con [HU-AOS-24](HU-AOS-24-editor-de-agentes.md) y [HU-AOS-23](HU-AOS-23-consola-de-conexiones.md). El tamaño (L) y REQ-AOS-17 son propuesta para validar con el dueño.
- La atribución por instancia exige que [HU-AOS-15](HU-AOS-15-migracion-sin-regresion.md) ya ejecute la release v3 (hoy `route_source` siempre es `default` y los campos de instancia no se escriben); antes de eso la vista solo puede mostrar al agente General.
- Los registros de las habilidades (pedidos, citas, promesas) viven en tablas de packs: la procedencia se guarda en el core (tabla de procedencia por registro) para no tocar cada pack ni acoplarlos al Agent OS.
