---
id: HU-CONN-03
titulo: Ciclo de vida seguro de las conexiones
spec: SPEC-08
fase: 0
hito: 0A
workstream: Canales y conexiones
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, legal]
req: [REQ-CONN-02]
dependencias: [HU-CONN-01]
skills: ["db-migration", "backend-design:migration-safety", "auditor-multitenant", "meta-whatsapp"]
ola: 3
estado: en-curso
---

# HU-CONN-03 · Ciclo de vida seguro de las conexiones

> Estado SDD: En curso desde el 2026-10-08 en otra sesión (worktree `solvershub-backend-conn03`, issue [core #336](https://github.com/devrochy/agent-core/issues/336)).

**ID:** HU-CONN-03

**Título:** Ciclo de vida seguro de las conexiones

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero que "Desactivar" detenga de verdad al asistente en esa conexión y que "Eliminar" conserve el historial y revoque los accesos para controlar mi canal sin perder datos.

**Por qué importa (valor empresarial):** Hoy "Desactivar" no detiene al bot y "Eliminar" borra en duro números, WABA, costos y plantillas (invariante 8). Un negocio que pausa su asistente y lo ve seguir respondiendo pierde la confianza en toda la plataforma.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-CONN-02

**Dependencias:** [HU-CONN-01](HU-CONN-01-credenciales-por-conexion.md)

**Criterios de aceptación (Gherkin):**
- **Pausa real.** Dado una conexión pausada, cuando entra un mensaje, entonces no se procesa con IA (se guarda y se avisa al negocio) y el sender no envía por ella.
- **Eliminar sin perder historia.** Dado eliminar una conexión, cuando se confirma, entonces la conexión, sus números y su WABA quedan con `deleted_at`, los tokens se revocan en Meta y los costos y plantillas se conservan.
- **Activar con criterio.** Dado una conexión en borrador o con error, cuando pulso "Activar", entonces no pasa a `conectada`; solo una pausada que pasa el diagnóstico vuelve.
- **Sin acciones sobre borradas.** Dado una conexión eliminada, cuando se intenta cualquier acción o aparece en Salud, entonces se rechaza o no se lista (filtro de `deleted_at` en `get_owned`).
- **Sin respaldo silencioso.** Dado una conexión eliminada, cuando el asistente quiere responder, entonces no cae a las credenciales del `.env` (`sender.py:148-175`).

**Evidencia / Definición de Terminado:**
- Migración que cambia las cascadas físicas por borrado lógico; tests de los cinco escenarios.

**Riesgos/Notas:**
- Defectos 5 y 6 de la auditoría y "acciones sobre borradas".
