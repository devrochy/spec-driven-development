---
id: HU-INMO-10
titulo: "Pack inmobiliario: inventario geoespacial con RLS"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, ingreso]
req: [REQ-INMO-01]
dependencias: [HU-INMO-01]
skills: ["new-pack", "db-migration", "auditor-multitenant", "backend-design:data-modeling-discipline"]
estado: borrador
---

# HU-INMO-10 · Pack inmobiliario: inventario geoespacial con RLS

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-10

**Título:** Pack inmobiliario: inventario geoespacial con RLS

**Workstream:** Verticales

**Historia:** Como inmobiliaria quiero tener mis inmuebles con precio, área, características y ubicación precisa en el sistema, para que el asistente pueda buscarlos y mostrarlos.

**Por qué importa (valor empresarial):** Es la entidad central de la vertical; el catálogo de commerce no la representa (sin operación, área ni ubicación).

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-INMO-01

**Dependencias:** [HU-INMO-01](HU-INMO-01-adrs-y-dor-del-piloto.md)

**Criterios de aceptación (Gherkin):**
- **Aislamiento.** Dado dos negocios con inmuebles, cuando uno consulta, entonces nunca ve los del otro (test genérico sobre todas las tablas `pack_inmobiliario_%`).
- **Únicos por negocio.** Dado la misma persona como asesor en dos inmobiliarias, cuando se registra en la segunda, entonces se acepta: todo UNIQUE, PK y EXCLUDE empieza por `tenant_id`.
- **Geometría.** Dado un inmueble con latitud y longitud, cuando se guarda, entonces `geom` se calcula por trigger y entra al índice GIST `(tenant_id, geom)`.
- **Coherencia.** Dado un inmueble en arriendo sin canon, cuando se intenta publicar, entonces el CHECK lo rechaza.

**Evidencia / Definición de Terminado:**
- `packages/pack-inmobiliario` con modelos, config, `flow.json` mínimo y `module.py`.
- Cada migración que crea una tabla incluye RLS, FORCE, policy con `nullif`, grants sin DELETE e índice `(tenant_id, …)`; crea sus extensiones (postgis, btree_gist, btree_gin, pg_trgm, unaccent). Del patrón de cobranza se copia el trigger, no su índice sin `tenant_id`.
- FK lógicas validadas bajo RLS (`get_owned`) y admins contra `tenant_user`; `EXPLAIN` como `app_runtime`; revisión del subagente `auditor-multitenant`.

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
