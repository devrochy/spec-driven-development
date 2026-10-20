---
id: HU-REP-05
titulo: Repo solvershub-docs con CI y regla un tema, un dueño
spec: SPEC-00
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: false
estimacion: S
impacto: [operacion]
req: [REQ-REP-01]
dependencias: []
skills: ["doc-coauthoring", "/code-review"]
estado: terminada
---

# HU-REP-05 · Repo `solvershub-docs` con CI y regla "un tema, un dueño"

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-00](../spec.md).

**ID:** HU-REP-05

**Título:** Repo solvershub-docs con CI y regla un tema, un dueño

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño del producto quiero que la planificación viva en un repo propio con validaciones automáticas para que el backlog y las decisiones no se desalineen de los repos de código.

**Por qué importa (valor empresarial):** La planificación es el activo que permite delegar trabajo a personas o agentes nuevos sin perder contexto. Sin validación automática, el backlog se pudre igual que hoy el ROADMAP.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** S

**REQ mapeados:** REQ-REP-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Repo creado.** Dado la carpeta local `solvershub/solvershub-docs`, cuando el cliente crea el remoto `devrochy/solvershub-docs`, entonces el contenido sube con historia y un README que explica cómo usar SDD.
- **CI de consistencia.** Dado un PR que rompe un enlace, cambia un ID de HU o deja un campo de la plantilla vacío, cuando corre el CI, entonces falla con el archivo y la línea.
- **Backlog regenerado.** Dado un cambio de estado en el frontmatter de una HU, cuando se mergea, entonces `06-backlog-resumen.md` se regenera.
- **Banners.** Dado `solvershub-comercial/PLAN-COMPETENCIA-Y-PRODUCCION.md`, cuando se abre, entonces un banner dice que la planificación vigente está en `solvershub-docs`.

**Evidencia / Definición de Terminado:**
- Repo con workflow de CI (enlaces, frontmatter, generación del backlog).
- Tabla "un tema, un dueño" en el README de cada repo.

**Implementada (2026-10-03):**
- Repo remoto `devrochy/solvershub-docs` con CI `regenerar.py --check` (PR #3 del repo).
- Banner en `solvershub-comercial/PLAN-COMPETENCIA-Y-PRODUCCION.md` apuntando a este repo.
- Tabla "un tema, un dueño" en el README de backend (PR #198), panel (#14), apk (#104), landing (#2) y comercial (#4).

**Riesgos/Notas:**
- La carpeta local ya existe (entrega del 2026-10-01); falta el remoto, que crea el cliente.
