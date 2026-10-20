---
id: HU-ARCH-15
titulo: Caché de Anthropic con como máximo 4 breakpoints
spec: SPEC-02
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: false
estimacion: S
impacto: [calidad_ia]
req: [REQ-FIX-08]
dependencias: []
skills: ["claude-api", "optimizer"]
estado: borrador
---

# HU-ARCH-15 · Caché de Anthropic con como máximo 4 breakpoints

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-02](../spec.md).

**ID:** HU-ARCH-15

**Título:** Caché de Anthropic con como máximo 4 breakpoints

**Workstream:** Arquitectura/Prod

**Historia:** Como negocio que elige Claude quiero que las peticiones usen la caché de prompts dentro del límite de Anthropic para que no fallen y cuesten lo esperado.

**Por qué importa (valor empresarial):** Hoy cada bloque del system lleva `cache_control` (`core/llm/anthropic_provider.py:55-62`) y el spec por defecto ya pasa de 4: las peticiones probablemente se rechazan. Claude es la opción premium que se ofrece a clientes exigentes.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** S

**REQ mapeados:** REQ-FIX-08

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Límite.** Dado un spec con 6 bloques de system, cuando se serializa para Anthropic, entonces hay como máximo 4 `cache_control`, en los bloques estables (tools, playbooks, voz de marca, flujo).
- **Costeo.** Dado una respuesta con `cache_read_input_tokens` y `cache_creation_input_tokens`, cuando se registra el uso, entonces se cobran con sus multiplicadores (0,1× y 1,25×).
- **Prueba.** Dado el test de `_serialize_system`, cuando corre en CI, entonces verifica el conteo.

**Evidencia / Definición de Terminado:**
- Test unitario y una llamada real en test con Haiku 4.5.
- `PROMPT-CACHING-GUIDE.md` corregido (dice "usamos 3").

**Riesgos/Notas:**
- Multiplicadores según el skill `claude-api` (ver fuentes externas).
