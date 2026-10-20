---
id: HU-AOS-14
titulo: "Releases por conexión con rollback en un clic"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [confianza, operacion]
req: [REQ-AOS-10]
dependencias: [HU-AOS-13]
skills: ["release", "backend-design:data-modeling-discipline", "backend-design:testing-with-discernment"]
estado: terminada
---

# HU-AOS-14 · Releases por conexión con rollback en un clic

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-14

**Título:** Releases por conexión con rollback en un clic

**Workstream:** Agent OS

**Historia:** Como dueño quiero publicar los cambios de una conexión como una versión que incluye agentes (con las políticas del Coordinador), procedimientos, permisos y habilidades, y volver a la anterior con un clic, para cambiar sin miedo.

**Por qué importa (valor empresarial):** ADR-0009 pedía releases con rollback; ahora el rollback es atómico por conexión y la caché se invalida por hash.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-10

**Dependencias:** [HU-AOS-13](HU-AOS-13-instancias-por-conexion.md)

**Criterios de aceptación (Gherkin):**
- **Build.** Dado cambios en un agente, cuando se construye una candidata, entonces congela versiones (el KernelSpec trae las políticas), permisos, la versión exacta de cada habilidad, overrides de playbooks, secciones del negocio y los campos de `AppSettings` que entran al prompt (`brand_voice`, `assistant_name`, `business_description`, `language`) con un `manifest_hash`, y no se activa sola.
- **Versión nueva de una habilidad.** Dado que el sync del arranque registra una versión nueva de una habilidad, cuando termina, entonces cada conexión con una release activa que la usa recibe una candidata que solo cambia ese componente (`origin = platform`), que sigue el mismo gate y canary y que el dueño puede detener; y si la versión anterior se marca `yanked`, su reemplazo se promueve directo, sin canary, con un `release_event` que dice el motivo.
- **Sticky por episodio.** Dado una conversación en un episodio con la versión 12, cuando se publica la 13, entonces sigue con la 12 hasta el fin del episodio (`episode.idleMinutes` sin mensajes) y su siguiente mensaje usa la 13.
- **Rollback.** Dado la versión 13 activa, cuando se vuelve a la 12, entonces todas las conversaciones usan la 12 desde su siguiente turno (≤ 5 s tras el clic), las tareas abiertas conservan sus datos válidos (evento `revalidated`), las que ya tuvieron un efecto irreversible se escalan en vez de cancelarse y queda un `release_event`.

**Evidencia / Definición de Terminado:**
- Módulo de releases (`core/releases/`); API `/api/v1/connections/{id}/releases` y `/rollback` reflejada en `docs/openapi.json`; sin tablas de políticas (viven en el KernelSpec); tests.
- Sync de `pack_versions` en el arranque (inserción `SECURITY DEFINER` con `ON CONFLICT DO NOTHING`, alerta si cambia el `manifest_hash` de una versión ya registrada) y armado de candidatas `origin = platform`: se adelantan aquí desde [HU-AOS-16](HU-AOS-16-habilidades-con-procedimientos-y-scope.md) porque la release fija la versión exacta de cada habilidad.
- Release 1 por conexión conversacional, construida desde el AgentSpec v2 activo y los artefactos del disco, idempotente y detrás de `AOS_RUNTIME`; con `legacy` el runtime ignora `release_id` y sigue el rollback de ADR-0051 §1.

**Terminada (2026-10-11):** PRs agent-core [#446](https://github.com/devrochy/agent-core/pull/446).

**Riesgos/Notas:**
- El canary con porcentaje llega en [HU-AOS-32](HU-AOS-32-canary-y-auto-rollback.md) y el gate en [HU-AOS-21](HU-AOS-21-gate-de-release-pass-k.md); aquí la promoción es total y la candidata se prueba en el playground (que reemplaza al tenant de staging de ADR-0016, ADR-0075). Hasta entonces, una candidata de plataforma pasa el gate vigente de ADR-0016 (journeys) y se promueve total.
- Lo operativo de `AppSettings` (horarios, pausa, debounce, `guardrail_fail_action`) y la configuración de las instalaciones siguen en caliente y no entran a la release.
- Sync de `pack_versions` (requisitos de la revisión de seguridad de [HU-AOS-02](HU-AOS-02-esquema-aditivo.md)): función `SECURITY DEFINER` con `SET search_path = pg_catalog, public, pg_temp` y `REVOKE ALL … FROM PUBLIC` (solo la ejecuta quien sincroniza); solo registra packs de la plataforma (`plugins.owner_tenant_id IS NULL`); recalcula `manifest_hash` en la base y rechaza la fila si no coincide; mejor un rol de arranque propio que darle `EXECUTE` a `app_runtime`.
