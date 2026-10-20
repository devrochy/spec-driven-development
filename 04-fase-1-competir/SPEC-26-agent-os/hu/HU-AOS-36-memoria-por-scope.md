---
id: HU-AOS-36
titulo: "Memoria por scope con procedencia y olvido"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [calidad_ia, legal]
req: [REQ-AOS-11]
dependencias: [HU-AOS-12]
skills: ["backend-design:data-modeling-discipline", "auditor-multitenant", "backend-design:security-discipline"]
estado: terminada
---

# HU-AOS-36 · Memoria por scope con procedencia y olvido

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-36

**Título:** Memoria por scope con procedencia y olvido

**Workstream:** Agent OS

**Historia:** Como cliente quiero que el negocio recuerde lo que ya le dije en cualquier canal y lo olvide si lo pido; y como dueño quiero que cada agente lea y escriba solo lo que le corresponde.

**Por qué importa (valor empresarial):** Coherencia entre canales sin perder privacidad (ADR-0053).

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-11

**Dependencias:** [HU-AOS-12](HU-AOS-12-agentes-versionados.md)

**Criterios de aceptación (Gherkin):**
- **Procedencia.** Dado una dirección confirmada en una tarea, cuando la tarea cierra, entonces queda como hecho con su fuente y su turno.
- **Tareas de un episodio anterior.** Dado una tarea cerrada como `episode_expired` ([HU-AOS-04](HU-AOS-04-estado-de-la-conversacion.md)), cuando corre la consolidación, entonces sus datos válidos pasan a `memory_facts` con procedencia, cubiertos por la purga de cliente y la retención.
- **Permisos.** Dado Ventas sin el namespace `cobranza`, cuando intenta escribir ahí, entonces se deniega.
- **Proyección.** Dado un hecho nuevo en `memory_facts`, cuando se escribe, entonces `customers.attributes` se actualiza en la misma transacción y ningún otro camino escribe `attributes` directamente.
- **Olvido.** Dado una purga de cliente, cuando se ejecuta, entonces sus hechos, sus claves en `customers.attributes` y sus vectores quedan borrados (lógico) y se limpia la memoria de trabajo de Redis de todas sus conversaciones; sus tareas y mensajes quedan como registro del negocio (ADR-0053).
- **Sin PII en vectores.** Dado un hecho con `data_class` `pii` o `sensitive`, cuando se consolida, entonces no se embebe en `memory_vectors`.

**Evidencia / Definición de Terminado:**
- `memory_facts` como fuente y `customers.attributes` como su proyección (incluido `core/memory/entity.py`); scopes en `memory_vectors`; consolidación nocturna; el cron de retención (`MEMORY_RETENTION_DAYS`) cubre `memory_facts`; tests.
- Migración propia de `memory_vectors` (columnas `scope`, `connection_id`, `agent_id`, `kind`, `importance`, `expires_at`, `embedding_model`, `source_turn_id`, los CHECK `ck_mv_scope`, `ck_mv_kind`, `ck_mv_keys` y el índice concurrente `ix_memory_vectors_scope`; diseño §4.3 bloque 11). No entró en el expand de [HU-AOS-02](HU-AOS-02-esquema-aditivo.md).

**Terminada (2026-10-11):** PRs agent-core [#444](https://github.com/devrochy/agent-core/pull/444).

**Riesgos/Notas:**
- Recuerdos que contradicen el estado: la tarjeta de estado gana, para las tareas del episodio en curso (ADR-0114).
- Hoy el loop guarda cada intercambio en L3 **sin `customer_id`** (`core/orchestrator/loop.py` → `vector_memory.store_memory`, que atrapa el error y solo lo registra). Con `scope = 'customer'` por defecto, `ck_mv_keys` rechazaría en silencio esos INSERT aunque fuera `NOT VALID`, y las filas viejas sin cliente harían fallar su `VALIDATE`. Antes de agregar los CHECK hay que decidir el scope de esas filas (resolver el cliente desde la conversación al guardar, o un scope propio) y cubrirlo con un test.
- `memory_facts.data_class` (revisión de seguridad de [HU-AOS-02](HU-AOS-02-esquema-aditivo.md)): el código asigna `pii` o `sensitive` según el *namespace* y la clave (documento, teléfono, salud…), nunca por defecto `internal` para esos datos; los hechos `pii`/`sensitive` no se embeben ni entran al prompt de agentes sin el `readScope` que los permita, y la purga por cliente los cubre.
