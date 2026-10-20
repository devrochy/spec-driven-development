---
id: HU-ARCH-23
titulo: Higiene de repos, migraciones y documentación
spec: SPEC-19
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-ARCH-17]
dependencias: [HU-REP-01]
skills: ["/code-review", "agentcore-conventions"]
estado: borrador
---

# HU-ARCH-23 · Higiene de repos, migraciones y documentación

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-19](../spec.md).

**ID:** HU-ARCH-23

**Título:** Higiene de repos, migraciones y documentación

**Workstream:** Arquitectura/Prod

**Historia:** Como integrante del equipo quiero un repo sin miles de carpetas de prueba, sin código muerto y con documentación al día para trabajar rápido y sin confusiones.

**Por qué importa (valor empresarial):** La deuda acumulada multiplica el costo de cada cambio para una persona sola y confunde a los agentes de IA que leen el repo.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-17

**Dependencias:** [HU-REP-01](../../../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-01-limpiar-residuos.md)

**Criterios de aceptación (Gherkin):**
- **Tests limpios.** Dado los tests de integración, cuando terminan, entonces borran sus carpetas en `tenants/`; las ~3.088 actuales se eliminan.
- **Migraciones.** Dado la tabla de pack en la migración 0040 del core, cuando se corrige, entonces vive en la cadena del pack sin romper bases existentes.
- **Mayúsculas.** Dado `docs/adr` y `docs/ADR`, cuando se unifican, entonces queda una sola carpeta.
- **Docs.** Dado `BACKLOG`, `INSTALLATION`, `despliegue-coolify`, `CHANGELOG` y `ROADMAP`, cuando se revisan, entonces reflejan el estado real.

**Evidencia / Definición de Terminado:**
- PRs de limpieza con CI verde.

**Riesgos/Notas:**
- Código muerto: `core/tasks/queue.py`, `register_resource`, evento `conversation.closed` nunca emitido.
