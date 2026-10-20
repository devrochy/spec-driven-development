---
id: HU-FWK-03
titulo: Registro de presets, seeds por pack y alta sin fallas
spec: SPEC-05
fase: 0
hito: 0A
workstream: Framework/Plugins
prioridad: P0
critico: true
estimacion: M
impacto: [diferenciacion, operacion]
req: [REQ-FWK-02, REQ-FWK-03]
dependencias: [HU-FWK-02]
skills: ["onboard-tenant", "new-pack", "backend-design:idempotency-and-side-effects", "auditor-multitenant"]
ola: 3
estado: terminada
---

# HU-FWK-03 · Registro de presets, seeds por pack y alta sin fallas

> Estado SDD: Terminada — implementada y verificada en test el 2026-10-08 (issue [core #285](https://github.com/devrochy/agent-core/issues/285)).

**ID:** HU-FWK-03

**Título:** Registro de presets, seeds por pack y alta sin fallas

**Workstream:** Framework/Plugins

**Historia:** Como master de SolversHub (y como el aprovisionamiento automático) quiero crear un negocio con un preset que habilite sus packs, cargue datos de ejemplo y deje el flujo listo, sin fallar por packs que piden claves, para dar de alta un cliente en minutos.

**Por qué importa (valor empresarial):** Es el habilitador directo del alta automática (D-12, [HU-SH-03](../../SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md)): sin un `onboard_tenant` que no falle y presets aplicables por código, SolversHub no puede crear el negocio de un cliente que acaba de pagar.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-FWK-02, REQ-FWK-03

**Dependencias:** [HU-FWK-02](HU-FWK-02-adr-presets.md)

**Criterios de aceptación (Gherkin):**
- **Alta con preset.** Dado `agent-core tenant create --preset restaurante`, cuando termina, entonces el negocio tiene commerce y payments habilitados, catálogo de ejemplo, flujo compuesto y una versión nueva del AgentSpec.
- **Packs con claves.** Dado un preset con `pack_payments` sin claves, cuando se aplica, entonces el pack queda "pendiente de configurar" con un paso en primeros pasos, y el alta no falla.
- **Fragmentos por pack.** Dado commerce, cuando se aplica el preset, entonces sus datos de ejemplo salen de `seed_data` y su config de `default_config` del pack, y el manifiesto no copia nada de eso (el CLI deja de importar `pack_commerce.models`).
- **Idempotencia.** Dado el mismo preset aplicado dos veces, cuando termina, entonces no hay datos duplicados.
- **Catálogo inicial.** Dado el registro, cuando se lista, entonces existen los presets Comercio, Restaurante y Cobranza.

**Evidencia / Definición de Terminado:**
- `core/presets/` con 3 manifiestos; `apply_preset` con tests; `seed_data` y `default_config` implementados en commerce.
- `cli/commands/tenant.py` sin imports de packs.

**Terminada (2026-10-08):** [agent-core #286](https://github.com/devrochy/agent-core/pull/286) (ADR-0110), desplegada en test (`e96d0c5`). `core/presets/` (`PresetManifest` con `extra="forbid"`, `load_fragment` que rechaza secretos y claves desconocidas, `apply_preset` idempotente), manifiestos `comercio`, `restaurante` y `cobranza`, fragmentos de commerce, `pack_commerce.seed_data` (el catálogo salió del CLI; `cli/commands/tenant.py` sin imports de packs, con test por AST), `onboard_tenant(preset=, plan=)` y CLI `--preset/--plan` + `tenant presets`. 10 tests unitarios + 4 de integración.

**Verificada en test:** `agent-core tenant create -y --name "Prueba Preset Restaurante" --preset restaurante --plan basic` → `pack_commerce` habilitado, `pack_payments` pendiente (faltan `public_key`, `private_key`, `events_secret`) sin romper el alta, menú sembrado (`MENU-PLATO-DIA`, `MENU-LIMONADA`), prefijo `PED`, versión nueva del AgentSpec, flujo compuesto (saludo → descubrimiento → cotización → pedido → escalamiento) y `tenants.settings["preset"]` + `audit_log`. Aplicarlo otra vez no crea spec, productos ni versiones nuevas.

**Nota:** los negocios nuevos arrancan en `free`; el preset necesita `--plan` (master o aprovisionamiento con el plan comprado, [HU-SH-03](../../SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md)).

**Riesgos/Notas:**
- Calendar y subscriptions implementan su `seed_data` en HU-SUB-11.
