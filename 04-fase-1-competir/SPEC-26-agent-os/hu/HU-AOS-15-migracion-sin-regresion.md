---
id: HU-AOS-15
titulo: "Migración de todos los negocios sin regresión de pass^k"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-AOS-01, REQ-AOS-12]
dependencias: [HU-AOS-07, HU-AOS-08, HU-AOS-10, HU-AOS-14, HU-ARCH-28]
skills: ["release", "eval-runner", "desplegar-test-agent-core"]
estado: en-curso
---

# HU-AOS-15 · Migración de todos los negocios sin regresión de pass^k

> Estado SDD: En curso — depende de la medición pass^4 (compuerta de [HU-ARCH-28](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md)) antes de encender `AOS_PROCEDURES`; hoy el loop ejecuta el AgentSpec v2 también en los negocios con `AOS_RUNTIME = v3`.

**ID:** HU-AOS-15

**Título:** Migración de todos los negocios sin regresión de pass^k

**Workstream:** Agent OS

**Historia:** Como responsable de la plataforma quiero migrar todos los negocios al runtime por releases con procedimientos, comprobando que su consistencia no empeora, para cerrar la base del Agent OS sin afectar a ningún cliente.

**Por qué importa (valor empresarial):** Cierra R1 y R2 con evidencia por negocio y una reversa probada.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-01, REQ-AOS-12

**Dependencias:** [HU-AOS-07](HU-AOS-07-procedimientos-de-comercio.md), [HU-AOS-08](HU-AOS-08-procedimientos-de-agenda-suscripciones-y-cobranza.md), [HU-AOS-10](HU-AOS-10-kernel-del-coordinador.md), [HU-AOS-14](HU-AOS-14-releases-por-conexion.md), [HU-ARCH-28](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md)

**Criterios de aceptación (Gherkin):**
- **Por negocio.** Dado un negocio con `AOS_RUNTIME = v3`, cuando corre su pass^4, entonces es igual o mejor que antes de migrar; y si no lo es, entonces la bandera vuelve a `legacy`.
- **Orden de banderas.** Dado el panel del master, cuando intenta encender `AOS_PROCEDURES` sin `AOS_RUNTIME = v3`, `AOS_RUNTIME = v3` sin `AOS_CONNECTION_ROUTING`, o apagar `AOS_CONNECTION_ROUTING` con algún negocio en `v3`, entonces la combinación se rechaza.
- **Contract.** Dado 2 releases estables sin rollback, cuando se aplica el *contract*, entonces `connection_id` y `release_id` quedan obligatorios.
- **Observación.** Dado una semana con la bandera de reversa disponible, cuando termina, entonces no hubo incidentes P1 atribuibles a la migración.

**Evidencia / Definición de Terminado:**
- Runbook de migración con el orden de encendido (`AOS_CONNECTION_ROUTING` global → `AOS_RUNTIME` por negocio → `AOS_PROCEDURES` por negocio) y de apagado (inverso); el pass^4 de [HU-ARCH-28](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) antes de encender `AOS_PROCEDURES`, con valor y fecha en la bitácora (ADR-0112); reporte por negocio; *contract* aplicado.

**Riesgos/Notas:**
- Las banderas `tenants.aos_runtime` y `tenants.aos_procedures` las escribe solo el master. Hoy `app_runtime` tiene `UPDATE` sobre toda `tenants` (el runtime actualiza `settings`), y acotarlo por columna haría que cada columna nueva de `tenants` naciera sin permiso. El setter va en una función `SECURITY DEFINER` (con `search_path` fijo, `REVOKE ALL FROM PUBLIC`) que exige el rol master y valida el orden con `AOS_CONNECTION_ROUTING`; en ese PR se evalúa quitar `UPDATE (aos_runtime, aos_procedures)` a `app_runtime` (requisito de la revisión de [HU-AOS-02](HU-AOS-02-esquema-aditivo.md)).
- Producción todavía en la máquina de desarrollo: la migración en producción espera a [HU-ARCH-01](../../../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md).
