---
id: HU-ARCH-24
titulo: Contenedor no-root, mypy gradual y embeddings configurables
spec: SPEC-19
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-ARCH-12]
dependencias: []
skills: ["backend-design:security-discipline", "release"]
estado: terminada
---

# HU-ARCH-24 · Contenedor no-root, mypy gradual y embeddings configurables

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-19](../spec.md).

**ID:** HU-ARCH-24

**Título:** Contenedor no-root, mypy gradual y embeddings configurables

**Workstream:** Arquitectura/Prod

**Historia:** Como responsable de la plataforma quiero contenedores sin root, chequeo de tipos que de verdad falle y la dimensión de embeddings configurable para reducir superficie de ataque y errores.

**Por qué importa (valor empresarial):** Correr como root agrava cualquier vulnerabilidad; un `mypy … || true` no detecta nada. Son puntos típicos de un pentest.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-12

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **No-root.** Dado la imagen del core, cuando arranca, entonces corre con un usuario sin privilegios.
- **mypy.** Dado los módulos del core marcados como estrictos, cuando hay un error de tipos, entonces el CI falla.
- **Embeddings.** Dado `EMBEDDING_DIMENSIONS`, cuando cambia, entonces la columna vectorial lo respeta con una migración.

**Evidencia / Definición de Terminado:**
- Dockerfile con `USER`; CI con mypy por módulos; migración.

**Implementada (2026-10-03, PR [agent-core #201](https://github.com/devrochy/agent-core/pull/201)):** Dockerfile con usuario `app` sin privilegios; gate de tipos en CI (basedpyright, falla el build); `memory_vectors.embedding` lee `EMBEDDING_DIMENSIONS` + migración 0046. Nota: mypy 2.x crashea en este entorno (metastore sqlite / plugin pydantic) y el Python del runner no trae `_sqlite3`; se usó basedpyright, que no depende de sqlite. `mypy` queda pineado a 1.x.

**Riesgos/Notas:**
- Hoy `Vector(384)` fijo en `core/db/models.py`.
