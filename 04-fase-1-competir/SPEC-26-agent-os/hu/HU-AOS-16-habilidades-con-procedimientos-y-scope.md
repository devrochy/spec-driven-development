---
id: HU-AOS-16
titulo: "Habilidades versionadas con procedimientos, consultas y plantillas (instalación por scope)"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-AOS-02, REQ-AOS-05]
dependencias: [HU-AOS-12, HU-FWK-04]
skills: ["plugin-dev", "db-migration", "auditor-multitenant", "backend-design:security-discipline"]
estado: en-curso
---

# HU-AOS-16 · Habilidades versionadas con procedimientos, consultas y plantillas (instalación por scope)

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-16

**Título:** Habilidades versionadas con procedimientos, consultas y plantillas (instalación por scope)

**Workstream:** Agent OS

**Historia:** Como dueño quiero instalar una habilidad para todo el negocio o solo para una conexión, con sus superpoderes, consultas y plantillas de agente versionados, para armar cada canal con lo que necesita.

**Por qué importa (valor empresarial):** Extensibilidad por habilidades con scope explícito; las plantillas aceleran el primer agente de cada negocio.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-02, REQ-AOS-05

**Dependencias:** [HU-AOS-12](HU-AOS-12-agentes-versionados.md), [HU-FWK-04](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md)

**Criterios de aceptación (Gherkin):**
- **Scope.** Dado una habilidad instalada solo en la conexión de Ventas, cuando se atiende otra conexión, entonces sus procedimientos no se ofrecen; y si la conexión tiene su propia instalación, reemplaza entera a la del negocio, sin merge.
- **Contenido congelado.** Dado una versión nueva de la habilidad, cuando la release activa fija la anterior, entonces los textos y procedimientos anteriores siguen vigentes hasta que se promueva la candidata de plataforma ([HU-AOS-14](HU-AOS-14-releases-por-conexion.md)); la instalación no lleva versión.
- **Una sola lectura.** Dado la habilitación de packs, cuando cualquier parte del core, del CLI o de un pack la consulta, entonces pasa por `enabled_packs()`, `enabled_business_packs()` o `count_tenant_packs()` (ya `async`, desde `pack_installations`) y el CI falla si queda una lectura de `spec.packs` fuera del lector tolerante.
- **Plugin del negocio.** Dado un plugin del negocio (ADR-0089), cuando se habilita, entonces queda en `pack_installations` sin fila en `pack_versions` y la release lo fija por nombre de instalación.
- **Fail-closed.** Dado un agente v3 (o el General del lector tolerante) sin un procedimiento, cuando intenta una acción de ese procedimiento, entonces se deniega; con `AOS_RUNTIME = legacy`, `_tool_denial` sigue fail-open (ADR-0019).

**Evidencia / Definición de Terminado:**
- `pack_installations` con scope y sin versión; `plugin_manager.load_config` por la conexión del turno (contextvar del Coordinador) y, si no hay, por la del negocio; crons y eventos de un pack corren si hay alguna instalación activa en el negocio.
- Backfill desde `enabled_business_packs(spec activo)` y `plugin_configs` (cifrado tal cual; packs no habilitados como instalación inactiva): desde ahí es la única fuente, sin importar la bandera, y un rollback del AgentSpec ya no cambia los packs. Los presets (ADR-0110 §3) habilitan y escriben su config en `pack_installations` con scope de negocio.
- Secretos por instalación con scope; las escrituras nuevas con AAD `(tenant_id, installation_id)`; la instalación `core` de secretos de `declarativeTools` no cuenta para el tope del plan.
- `docs/MULTITENANT.md` lista `pack_versions` como tabla de sistema (su sync llega en [HU-AOS-14](HU-AOS-14-releases-por-conexion.md)); tests de aislamiento.

**Riesgos/Notas:**
- El código de una habilidad es uno solo en el binario: las acciones con cambios rompedores (incluido subir su riesgo) se publican como `nombre_v2` (ADR-0118).
- Los plugins del negocio no publican procedimientos en v1.
- Nota del ciclo de pruebas 2026-10-13 ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)): «que cada pack tenga sus habilidades internamente y no tener una lista de habilidades en toda la configuración del core». Al cerrar esta HU, la configuración del negocio deja de listar las herramientas de todos los packs: cada agente ve solo los superpoderes de los packs instalados en sus conexiones, y la configuración del core solo muestra las del core.
- `pack_installations.config_encrypted`: las escrituras nuevas atan el cifrado con AAD a `(tenant_id, installation_id)` (ADR-0118 §5, revisión de seguridad de [HU-AOS-02](HU-AOS-02-esquema-aditivo.md)), así una fila copiada a otra instalación o a otro negocio no se descifra. El esquema ya exige texto cifrado (`ck_pack_installations_config_cifrada`) y rechaza instalar el plugin privado de otro negocio (`plugins.owner_tenant_id`).
