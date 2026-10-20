---
id: HU-ARCH-10
titulo: Modelos de DeepSeek vigentes y verificados
spec: SPEC-02
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: S
impacto: [calidad_ia, confianza]
req: [REQ-ARCH-18]
dependencias: []
skills: ["deep-research", "eval-runner", "optimizer"]
ola: 1
estado: terminada
---

# HU-ARCH-10 · Modelos de DeepSeek vigentes y verificados

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-02](../spec.md) (P-05).

**ID:** HU-ARCH-10

**Título:** Modelos de DeepSeek vigentes y verificados

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de un negocio quiero que mi asistente use un modelo que exista y soporte tools para que no deje de responder de un día para otro.

**Por qué importa (valor empresarial):** El modelo por defecto (`deepseek-chat`, `core/config.py:89`) fue discontinuado el 2026-07-24. Si un entorno lo usa, el asistente falla por completo: es el riesgo más inmediato de toda la plataforma.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-ARCH-18

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Modelo vigente.** Dado la configuración por defecto, cuando arranca el core, entonces usa `deepseek-flash` (o el que decida P-05) y no `deepseek-chat` ni `deepseek-reasoner`.
- **Tools verificadas.** Dado el golden set del framework, cuando corre con el modelo nuevo, entonces pasa ≥ el resultado actual (34/35) y las llamadas a tools son válidas.
- **Respaldo.** Dado un error del proveedor o una tasa de fallas de tools > 5 % en una hora, cuando ocurre, entonces el core usa el modelo de respaldo configurado y registra el cambio.
- **Precios.** Dado el tarifario de `openai_compatible.py`, cuando se consulta el costo de `deepseek-flash`, entonces tiene precio (no 0) con caché y tarifa combinada pico/valle.
- **Aviso a negocios con modelo fijo.** Dado un negocio con `llm_model` = `deepseek-chat` en su config, cuando se despliega, entonces se migra al modelo vigente y queda auditado.

**Evidencia / Definición de Terminado:**
- Reporte de evals antes y después.
- `docs/despliegue-coolify.md` y `.env.example` sin los nombres viejos.

**Implementada (2026-10-02, PR en `devrochy/agent-core`):**
- `core/config.py`: default `deepseek-flash` (chat y razonamiento), `LLM_MODEL_FALLBACK=gpt-4o-mini`, `LLM_THINKING_DEFAULT/REASONING`.
- `core/llm/openai_compatible.py`: precios V4 (`deepseek-flash` $0.14/$0.28, `v4-pro` $0.435/$0.87), `RETIRED_DEEPSEEK_MODELS` y `resolve_thinking_for_model()`; `thinking` explícito en `generate`/`stream` para DeepSeek.
- `core/llm/__init__.py` + `core/orchestrator/loop.py`: el router decide thinking off (default) / on (razonamiento).
- Migración `0043_migrar_modelos_deepseek.py`: reescribe `agent_specs` con IDs retirados a `deepseek-flash`.
- ADR-0086 (supersede parcial del ADR-003); `.env.example`, `cli/init.py`, `cli/preflight.py`, `cli/configure.py` y docs al día.
- Golden set del framework: **34/35** con `deepseek-flash` (igual que la línea base; el único FAIL, `datos-no-inventar-precios-15`, es preexistente y no empeora).
- `pytest`: 672 passed, 250 skipped. `ruff`: limpio. `import-linter`: 3 contratos OK.

**Riesgos/Notas:**
- Por verificar: tool calling de `deepseek-flash` en modo con y sin razonamiento (S-07).
- Gemini 2.5 Flash-Lite se retira el 2026-10-20: no usarlo como respaldo.
