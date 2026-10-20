# SPEC-00 · Diseño

## Orden de operaciones

1. **Fugas de marca** ([HU-REP-04](hu/HU-REP-04-sin-fugas-de-marca-tecnica.md)): independiente de todo lo demás; va primero.
2. **Limpieza** ([HU-REP-01](hu/HU-REP-01-limpiar-residuos.md)): borrar `solvershub/apps/`, los stubs del backend y las copias viejas
   (revisando antes el `.env` de `agent-core (copy)`); archivar `app-cobranza*` en GitHub; recrear el
   venv.
3. **Renombre cosmético** ([HU-REP-02](hu/HU-REP-02-renombre-cosmetico.md)): GitHub → Coolify (nombres visibles; los UUID no cambian) →
   runner → carpeta local → Makefile y `package.json` del panel → enlaces y README.
4. **Transición de identificadores** ([HU-REP-03](hu/HU-REP-03-transicion-de-identificadores.md)): ADR, alias, migración de variables en Coolify y
   retiro de los alias después de dos releases.
5. **Infra** ([HU-REP-06](hu/HU-REP-06-solvershub-infra.md)) y **docs** ([HU-REP-05](hu/HU-REP-05-repo-solvershub-docs.md)) en paralelo.

## Mecanismo de alias

| Identificador | Cómo convive el nombre viejo |
|---|---|
| CLI | `[project.scripts]` declara `solvershub` y `agent-core` apuntando a la misma función; el viejo imprime un aviso |
| Entry points | `plugin_manager` y el registro de canales descubren `solvershub.plugins` y `agent_core.plugins`; si un pack declara ambos, gana el nuevo |
| Variables | Helper `env_compat("SOLVERSHUB_ROLE", "AGENT_CORE_ROLE")` en `core/config.py` y en `scripts/entrypoint.sh` |
| `AGENT_CORE_INTEGRATION` | Se renombra en un solo PR junto con `ci.yml` y el Makefile, con un test que falla si la variable vieja sigue en uso |
| Contratos | Paquete `solvershub_contracts` que hace `from agentcore_contracts import *` |

## `solvershub-infra`

```
solvershub-infra/
├── README.md                 qué hay, cómo restaurar desde cero
├── cloudflare/               configs de túnel (sin tokens) y reglas de Access
├── coolify/                  inventario de apps, variables (sin secretos), dominios
├── crontab/                  scripts @reboot y su instalación
├── registry/                 registro local de imágenes
├── runners/                  instalación de los runners de GitHub
├── postgres/                 Dockerfile de la imagen (pg17 + PostGIS + pgvector)
└── runbooks/                 restauración, rotación de secretos
```

Los secretos nunca entran al repo: se documenta **dónde** viven (Coolify, gestor de contraseñas) y
cómo se rotan.

## `solvershub-docs`

Esta carpeta se convierte en repo con un CI mínimo: chequeo de enlaces relativos, validación del
frontmatter de las HU y regeneración de `06-backlog-resumen.md`. La regla "un tema, un dueño":

| Tema | Repo dueño |
|---|---|
| Planificación, specs, HU, decisiones de producto | `solvershub-docs` |
| ADR de implementación, ROADMAP, CHANGELOG del motor | `solvershub-core` |
| Sistema de diseño del panel | `solvershub-panel/apps/panel-web/DESIGN.md` |
| Legal, runbooks operativos, material comercial | `solvershub-comercial` |
| Infraestructura | `solvershub-infra` |

## ADR a crear

- **ADR "Transición de nombres solvershub-*"** en `solvershub-core/docs/adr/`: qué se renombra, qué
  nunca, alias y fecha de retiro.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| El runner deja de tomar jobs tras renombrar el repo | Probar con un PR vacío antes de seguir |
| Un contenedor de producción arranca con el nombre viejo del CLI | Alias en el mismo release |
| Tests de integración saltados en silencio por la variable renombrada | Test que verifica que la variable nueva está activa en CI |
