---
id: HU-REP-06
titulo: solvershub-infra versionado como base de recuperación ante desastres
spec: SPEC-00
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, operacion]
req: [REQ-REP-02]
dependencias: []
skills: ["cloudflare-one", "cloudflare", "backend-design:boring-by-default", "doc-coauthoring"]
estado: borrador
---

# HU-REP-06 · `solvershub-infra` versionado como base de recuperación ante desastres

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-00](../spec.md).

**ID:** HU-REP-06

**Título:** solvershub-infra versionado como base de recuperación ante desastres

**Workstream:** Arquitectura/Prod

**Historia:** Como operador de la plataforma quiero que túneles, crontab, registry, runners, inventario de Coolify e imagen de Postgres estén versionados en un repo para reconstruir la plataforma desde cero siguiendo un runbook.

**Por qué importa (valor empresarial):** Hoy la infraestructura vive en una sola máquina y en la memoria de una persona. Es el mayor riesgo de continuidad del negocio y la primera pregunta de un cliente enterprise o de un inversionista.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-REP-02

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Inventario completo.** Dado el entorno actual, cuando se crea el repo, entonces contiene configs de Cloudflare Tunnel y Access, scripts de crontab, instalación de runners, inventario de Coolify y el Dockerfile de Postgres (pg17 + PostGIS + pgvector).
- **Sin secretos.** Dado el repo, cuando corre gitleaks, entonces no encuentra secretos; cada secreto tiene documentado dónde vive y cómo se rota.
- **Simulacro.** Dado una máquina vacía, cuando una persona sin contexto sigue el runbook, entonces levanta el entorno de test y deja el tiempo medido en la evidencia.

**Evidencia / Definición de Terminado:**
- Repo `solvershub-infra` con README y runbook de restauración.
- Registro del simulacro (fecha, duración, problemas encontrados).

**Riesgos/Notas:**
- La imagen de Postgres en compose se llama `agent-core-postgres:pg16-…` pero construye pg17: se corrige aquí.
- [HU-ARCH-01](../../SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) deja la producción nueva descrita en este repo si ya existe; si no, la mueve aquí al cerrarse esta HU.
