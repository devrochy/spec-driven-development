---
id: HU-REP-01
titulo: Limpiar residuos de la reestructura
spec: SPEC-00
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: false
estimacion: S
impacto: [operacion]
req: [REQ-REP-01, REQ-ARCH-17]
dependencias: []
skills: ["/code-review", "desplegar-test-agent-core"]
estado: borrador
---

# HU-REP-01 · Limpiar residuos de la reestructura

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-00](../spec.md).

**ID:** HU-REP-01

**Título:** Limpiar residuos de la reestructura

**Workstream:** Arquitectura/Prod

**Historia:** Como responsable de la plataforma quiero eliminar las carpetas, stubs y copias que dejó la reestructura para que nadie trabaje sobre código muerto ni restaure una copia vieja por error.

**Por qué importa (valor empresarial):** Cada copia vieja es un riesgo: tiene `.env` con secretos y código que parece vigente. Un repo limpio reduce el tiempo de entrada de cualquier persona o agente nuevo y es lo primero que mira una auditoría técnica.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** S

**REQ mapeados:** REQ-REP-01, REQ-ARCH-17

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Carpeta suelta eliminada.** Dado `solvershub/apps/` con solo una caché `.next` y un log, cuando se ejecuta la limpieza, entonces la carpeta no existe y las 4 menciones en documentos (ADR-0078:15, ADR-0079:8, `PLAN-DE-PRUEBAS.md:4,23`) apuntan a `solvershub-panel/apps/panel-web`.
- **Stubs eliminados.** Dado `solvershub-backend/apps/{gateway,agentos,worker}` y `packages/{core-crm,core-runtime,channel-whatsapp}`, cuando se borran, entonces el CI completo pasa y `CLAUDE.md` deja de mencionarlos.
- **Copias revisadas antes de borrar.** Dado `agent-core (copy)` con un `.env`, cuando se va a borrar, entonces primero se confirma que sus secretos no siguen en uso o se rotan.
- **Venv sano.** Dado el venv del backend creado en la ruta vieja, cuando se recrea, entonces `.venv/bin/pytest` y `.venv/bin/uvicorn` funcionan sin `python -m`.

**Evidencia / Definición de Terminado:**
- PR en `solvershub-backend` que borra los stubs, con CI verde.
- Lista de lo borrado y lo archivado (`app-cobranza`, `app-cobranza-admin` archivados en GitHub) en el CHANGELOG.
- Nota de rotación si algún secreto de las copias seguía vigente.

**Riesgos/Notas:**
- `solvershub-panel/apps/` **no** se toca: lo usan CI, Coolify, Makefile y `parity-report.py`.
- Los tarballs de 52–95 MB pueden ir a almacenamiento frío en vez de borrarse.
