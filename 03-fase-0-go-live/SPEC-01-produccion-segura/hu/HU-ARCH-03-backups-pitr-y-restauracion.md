---
id: HU-ARCH-03
titulo: Backups WAL/PITR fuera del sitio y restauración probada
spec: SPEC-01
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, legal]
req: [REQ-ARCH-03]
dependencias: [HU-ARCH-01]
skills: ["deep-research", "backend-design:incident-thinker", "backend-design:boring-by-default"]
ola: 3
estado: borrador
---

# HU-ARCH-03 · Backups WAL/PITR fuera del sitio y restauración probada

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-01](../spec.md) (P-02).

**ID:** HU-ARCH-03

**Título:** Backups WAL/PITR fuera del sitio y restauración probada

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de SolversHub quiero backups continuos de la base y de `TENANTS_ROOT` fuera del servidor, con una restauración probada, para no perder pedidos, pagos ni conversaciones si el servidor falla.

**Por qué importa (valor empresarial):** Perder un día de pagos y pedidos de un cliente es perder al cliente y, por la Ley 1581, un incidente reportable. El SLO publicado en `security.md` (15 min) solo es honesto con PITR.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-03

**Dependencias:** [HU-ARCH-01](HU-ARCH-01-produccion-fuera-de-dev.md)

**Criterios de aceptación (Gherkin):**
- **PITR.** Dado WAL continuo hacia el almacenamiento externo, cuando se pide restaurar a un instante de hace una hora, entonces la base restaurada contiene las transacciones hasta ese instante.
- **Archivos.** Dado `TENANTS_ROOT` y las evidencias de cobranza, cuando se restaura, entonces los archivos coinciden con la base (sin evidencias huérfanas).
- **Simulacro con tiempo.** Dado un servidor limpio, cuando el operador sigue el runbook, entonces la plataforma queda operativa dentro del RTO acordado y el tiempo queda registrado.
- **Alerta.** Dado que el envío de WAL falla más de 15 minutos, cuando se detecta, entonces llega una alerta.

**Evidencia / Definición de Terminado:**
- `solvershub-comercial/runbooks/backup-restore.md` reescrito con el procedimiento real.
- Registro del simulacro en `runbooks/evidencia/` (fecha, duración, punto restaurado).
- Retención configurada (30 días PITR, 12 mensuales).

**Riesgos/Notas:**
- `pack_cobranza/evidencias.py:5` cita "el backup del runbook": queda cubierto con esta HU.
- Decisión P-02 (RPO 15 min recomendado).
