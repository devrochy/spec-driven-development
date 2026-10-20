---
id: HU-AOS-35
titulo: "Caché por versión de lo compilado"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: S
impacto: [operacion]
req: [REQ-AOS-11]
dependencias: [HU-AOS-14]
skills: ["optimizer", "backend-design:performance-and-scaling"]
estado: borrador
---

# HU-AOS-35 · Caché por versión de lo compilado

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-35

**Título:** Caché por versión de lo compilado

**Workstream:** Agent OS

**Historia:** Como plataforma quiero cachear en proceso lo compilado de cada release (prompt fijo, procedimientos y disparadores) con una clave que incluya la versión, y mantener estables los bloques fijos del prompt, para bajar costo y latencia sin servir nunca contenido viejo.

**Por qué importa (valor empresarial):** Menos costo por turno sin arriesgar respuestas desactualizadas.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-AOS-11

**Dependencias:** [HU-AOS-14](HU-AOS-14-releases-por-conexion.md)

**Criterios de aceptación (Gherkin):**
- **Por versión.** Dado una release nueva, cuando entra un turno, entonces lo compilado se busca con la clave `(tenant_id, release_hash, agent_version_hash)` nueva y no se lee nada de la anterior; nada se invalida, porque las versiones son inmutables.
- **Bloques fijos estables.** Dado un cambio de cliente, conversación o turno, cuando se arma el prompt, entonces los bloques fijos son idénticos byte a byte: solo llevan valores congelados en la release y lo variable va al bloque dinámico (ADR-0091).
- **Prefijo.** Dado una semana de tráfico, cuando se mide, entonces los tokens cacheados son al menos el 50 % de los de entrada.

**Evidencia / Definición de Terminado:**
- Caché en proceso de lo compilado por versión (ADR-0117 §7) en `core/agents/compiler.py` y `core/llm/prompt_builder.py`; test que compara los bloques fijos entre dos clientes; métrica de tokens cacheados por agente.
- Sin *epochs*, sin warm-up y sin caché de resultados de acciones: llegan cuando se mida una acción que lo justifique, con su propia HU.

**Riesgos/Notas:**
- Una variable en los bloques fijos rompe la caché del proveedor (PROMPT-CACHING-GUIDE).
- Se achicó de M a S el 2026-10-09, al recortarse la caché en ADR-0117 (revisión del arquitecto, agent-core #402).
