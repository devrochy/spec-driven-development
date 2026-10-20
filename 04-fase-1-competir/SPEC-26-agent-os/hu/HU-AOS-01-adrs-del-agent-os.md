---
id: HU-AOS-01
titulo: "ADRs del Agent OS (0112–0119)"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, calidad_ia]
req: [REQ-AOS-01, REQ-AOS-03]
dependencias: []
skills: ["adr", "arquitecto"]
estado: terminada
---

# HU-AOS-01 · ADRs del Agent OS (0112–0119)

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-01

**Título:** ADRs del Agent OS (0112–0119)

**Workstream:** Agent OS

**Historia:** Como responsable de la arquitectura quiero aceptar los ADR del Agent OS (procedimientos, contratos, estado, conexión canónica, colaboración, releases, habilidades y fiabilidad) para que el desarrollo arranque con decisiones explícitas y revisadas.

**Por qué importa (valor empresarial):** P-10 queda resuelta con un ADR y ninguna HU de código empieza sin su decisión (constitución §1.6). Evita retrabajo en el corazón del turno.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-01, REQ-AOS-03

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Revisión.** Dado los 8 ADR en estado propuesto, cuando el agente `arquitecto` los revisa contra los ADR vigentes y las 9 invariantes, entonces no quedan hallazgos bloqueantes sin resolver.
- **Aceptación.** Dado un ADR revisado, cuando el dueño lo aprueba, entonces pasa a `aceptado` en el índice y los ADR que enmienda quedan enlazados.
- **Numeración.** Dado otros PR de ADR en paralelo, cuando se mergea, entonces ningún número choca con `origin/develop`.

**Evidencia / Definición de Terminado:**
- ADR-0112 a ADR-0119 aceptados (ADR-0119 puede aceptarse antes, porque lo usan [HU-ARCH-28](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) y [HU-ARCH-29](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md)).
- Índice `docs/adr/README.md` actualizado y enlazado desde [SPEC-26](../spec.md).

**Terminada (2026-10-11):** PRs agent-core [#402](https://github.com/devrochy/agent-core/pull/402).

**Riesgos/Notas:**
- Los ADR se escribieron el 2026-10-08 con estado propuesto; si una decisión cambia, se corrige el ADR antes de aceptarlo.
- 2026-10-09: el agente `arquitecto` revisó ADR-0112 a 0118 y se corrigieron en [agent-core #402](https://github.com/devrochy/agent-core/pull/402) (siguen propuestos hasta la aprobación del dueño); el diseño, la spec y las HU de [SPEC-26](../spec.md) se alinearon con esa versión.
