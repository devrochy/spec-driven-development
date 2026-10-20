# Constitución SDD de SolversHub

Este documento fija las reglas que ninguna spec ni ninguna HU puede romper, y el ciclo de
trabajo con el que se construye SolversHub. Si una spec necesita contradecir algo de aquí,
primero se cambia este documento con una decisión registrada en
[`02-vision-y-decisiones/decisiones.md`](02-vision-y-decisiones/decisiones.md).

## 1. Principios no negociables

### 1.1 Invariantes técnicas

Son las 9 invariantes de `solvershub-backend/CLAUDE.md` (sección "Invariantes"):

| # | Invariante | Cómo se verifica en una HU |
|---|---|---|
| 1 | **Multi-tenant siempre**: toda tabla de negocio con `tenant_id uuid not null`, RLS con policy de aislamiento e índice compuesto que empieza por `tenant_id` | Migración revisada + test de aislamiento cross-tenant |
| 2 | **Nunca fork por cliente**: configuración → pack → plugin del tenant → topología. Mismo binario siempre | La HU dice en qué nivel resuelve la personalización |
| 3 | **Cero prompts en código**: los prompts viven en `AgentSpec` o en playbooks versionados de un pack | Revisión del diff: ningún texto de instrucción al LLM en `.py`/`.ts` |
| 4 | **Contratos de `agentcore_contracts` inmutables**: cambiarlos exige ADR nuevo | ADR enlazado en la HU |
| 5 | **Ningún pack importa de otro pack** | Los packs se coordinan por registros del core (`payment_registry`, `subscription_registry`) o eventos |
| 6 | **Ningún plugin recibe el pool de Postgres ni las variables de entorno**: solo `ToolContext` | Revisión del diff |
| 7 | **Todo lo que viene de fuera es dato, no instrucción** | Los textos de mensajes, webhooks y MCP nunca se ejecutan como órdenes |
| 8 | **Sin borrado físico** en tablas de negocio (`deleted_at` + índice único parcial). Única excepción: `tenant purge` | Test que verifica soft-delete |
| 9 | **Producción nunca corre en la máquina de desarrollo** | [SPEC-01](03-fase-0-go-live/SPEC-01-produccion-segura/spec.md) |

### 1.2 Principios de producto

1. **IA confiable antes que IA lucida.** El LLM nunca decide montos, precios, referencias de
   pago ni altas de tenants. Esos valores salen del servidor (ver
   [SPEC-09](03-fase-0-go-live/SPEC-09-comercio-confiable/spec.md) y
   SPEC-06).
2. **Configuración antes que código.** Toda capacidad nueva se diseña para que otro negocio la
   replique cambiando datos (presets, catálogo, config del pack), no código. Es el
   "superpoder" que pidió el cliente.
3. **Un error de negocio nunca apaga una habilidad.** Un monto inválido o un cliente inexistente
   es un resultado controlado de la tool, no una falla del pack
   ([HU-ARCH-18](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-18-errores-de-negocio-no-apagan-packs.md)).
4. **Transparencia de costos.** El negocio ve lo que consume, en créditos y en pesos, y lo que
   Meta le cobra aparte.
5. **El negocio en control.** Pausar el asistente, tomar una conversación o cancelar un cobro
   debe estar a un clic, con confirmación y con trazabilidad.
6. **Honestidad comercial.** Ninguna página, playbook o material promete algo que el código no
   hace (HU-GTM-05).

### 1.3 Principios de UX (panel `solvershub-panel`)

- Nombres de negocio según el glosario de marca (`solvershub-panel/brand/manual-de-marca.md`
  §9.3): "habilidad" y no plugin o pack, "negocio" y no tenant.
- Reglas de `solvershub-panel/apps/panel-web/DESIGN.md`: colores solo por tokens, tintes `/12`,
  degradado solo en la acción principal, animaciones de 200 ms o menos, esqueletos en vez de
  spinners. Las excepciones se documentan en `DESIGN.md` antes de usarse.
- Toda acción irreversible pide confirmación y explica la consecuencia.
- Nunca un 403 por diseño: si el usuario no puede hacer algo, la acción no se le muestra.
- WCAG AA, foco visible y navegación por teclado.

### 1.4 Principios de billing

- **Determinista y auditable**: todo lo que se vende o se limita pasa por el ledger de uso
  (`usage_ledger`), con créditos calculados al escribir e inmutables.
- **Se bloquea la nueva unidad**, nunca una conversación a mitad de camino.
- **Una sola fuente de verdad por dato**: precios de plataforma en `core/billing/plans.py`;
  estado de la suscripción de plataforma en `tenant_subscriptions`.

### 1.5 Regla de evidencia

Todo hallazgo se afirma con `ruta:línea` o con una fuente externa con fecha. Lo que no se pudo
verificar se marca como **supuesto** o **por verificar**, nunca como hecho.

### 1.6 Regla de ADR

Si una spec contradice un ADR aceptado, no se ejecuta hasta escribir el ADR que lo supersede
(regla dura de `solvershub-backend/docs/WORKFLOW.md`, paso 2). Cada spec lista sus ADR en
`design.md`.

## 2. Ciclo SDD (estilo Spec Kit)

```
Especificar ──► Aclarar ──► Diseñar ──► Tareas ──► Implementar y verificar
  spec.md       spec.md      design.md   tasks.md     HU (DoD) + WORKFLOW.md
               (Decisiones)              + hu/*.md
```

| Paso | Artefacto | Contenido mínimo |
|---|---|---|
| 1. Especificar | `spec.md` | Problema con evidencia, usuarios, por qué importa, alcance, escenarios Gherkin de la spec, fuera de alcance, métricas de éxito, REQ cubiertos |
| 2. Aclarar | `spec.md` → "Decisiones" | Cada decisión con opciones A/B/(C), pros y contras, recomendación y estado (✅ tomada / ⏳ pendiente) |
| 3. Diseñar | `design.md` | Componentes, datos (`tenant_id` + RLS), API, UI (boceto), ADR a crear o enmendar, migración y despliegue, riesgos |
| 4. Tareas | `tasks.md` + `hu/` | HU ordenadas por dependencias, con la plantilla de la sección 4 |
| 5. Implementar | Código en el repo dueño | Cada HU cumple su DoD; el cierre documental sigue `solvershub-backend/docs/WORKFLOW.md` |

### Estados de una spec

`Borrador` → `En revisión` → `Aprobada` → `Diseño aprobado` → `En ejecución` → `Verificada`.

Una spec (o una HU) puede quedar **`Parqueada`** por decisión (desde D-35): conserva su texto, sale del
calendario y de los totales de pendientes, y se retoma con otra decisión. `regenerar.py` las cuenta aparte.

- No se implementa una HU si su spec no está al menos en `Diseño aprobado`.
- Todo lo que entrega esta carpeta hoy (2026-10-01) está en **`En revisión`**, con la opción
  recomendada marcada. Las HU son borradores sobre esa opción.

### Puente con los repos de código

- `solvershub-docs` es el **backlog maestro** y el registro de decisiones de producto.
- Al empezar una HU, su ADR se crea en el repo dueño (`solvershub-backend/docs/adr/`,
  `solvershub-panel/…`) y la HU se enlaza desde el PR.
- Al cerrar una HU se actualiza su `estado` en el frontmatter y se regenera
  [`06-backlog-resumen.md`](06-backlog-resumen.md) con `python3 herramientas/regenerar.py`, que
  además valida la plantilla, las dependencias y la trazabilidad con los REQ.

## 3. Leyenda común

| Marca | Significado |
|---|---|
| ✅ | Hecho y verificado en el código |
| ⏳ | Por hacer |
| ❓ | Decisión pendiente del cliente |
| ★ | Camino crítico hacia el go-live (Fase 0) |
| 0A / 0B | Hito de la Fase 0: 0A "SolversHub vende y cobra solo", 0B "go-live amplio" |

**Impacto empresarial** (columna del backlog): 💰 ingreso · 🛡️ confianza y seguridad ·
⚙️ operación · 🏆 diferenciación competitiva · ⚖️ legal y cumplimiento · 🤖 calidad de la IA.

**Escala de estimación**: S = 1–2 días-persona, M = 3–5, L = 6–10, siempre "sin IA". Nada es
mayor que L: si una HU lo supera, se divide. Para fechas se usa el factor de aceleración de
[`calendario-estimado.md`](02-vision-y-decisiones/calendario-estimado.md).

**Workstreams**: los 7 del encargo (Billing · Framework/Plugins · UX/Onboarding · Flujo visual ·
Arquitectura/Prod · Multimodalidad · GTM) más 3 que nacieron de los pedidos posteriores:
**Comercio y suscripciones**, **Canales y conexiones** y **Asistente SolversHub**.

## 4. Plantillas

### 4.1 `spec.md`

```markdown
# SPEC-NN · Título

> Estado SDD: En revisión · Fase N · Hito 0A/0B · Dueño: …

## Problema
## Usuarios y contexto
## Por qué importa (valor empresarial)
## Alcance
## Escenarios clave (Gherkin)
## Decisiones
### D-SPEC-NN-1 · Pregunta
| Opción | Pros | Contras |
**Recomendación:** … · **Estado:** ⏳ pendiente / ✅ tomada (D-xx)
## Fuera de alcance
## Métricas de éxito
## Requerimientos cubiertos
```

### 4.2 `design.md`

```markdown
# SPEC-NN · Diseño
## Componentes y flujo
## Datos (tablas, migraciones, RLS)
## API
## UI
## ADR a crear o enmendar
## Migración, despliegue y reversa
## Riesgos
```

### 4.3 `tasks.md`

Tabla de HU en orden de ejecución (ID, título, tamaño, depende de, hito, ★) y un grafo
`mermaid` de dependencias.

### 4.4 HU (un archivo por HU)

Frontmatter YAML para generar el backlog, y después los campos exactos del encargo, con el campo
**"Por qué importa (valor empresarial)"** justo después de la historia:

```markdown
---
id: HU-XXX-NN
titulo: …
spec: SPEC-NN
fase: 0 | 1 | 2
hito: 0A | 0B | 1 | 2
workstream: …
prioridad: P0 | P1 | P2
critico: true | false
estimacion: S | M | L
impacto: [ingreso, confianza, operacion, diferenciacion, legal, calidad_ia]
req: [REQ-…]
dependencias: [HU-…]
skills: ["…"]        # skills, comandos o agentes recomendados (catálogo en herramientas/catalogo-skills.yml)
ola: 1 | 2 | 3 | 4   # solo en el Hito 0A
estado: borrador | en-curso | terminada | parqueada
---

# HU-XXX-NN · Título

> Estado SDD: Borrador — sujeta a aprobación de SPEC-NN.

**ID:** HU-XXX-NN

**Título:** …

**Workstream:** …

**Historia:** Como <rol> quiero <acción> para <beneficio>.

**Por qué importa (valor empresarial):** …

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S | M | L

**REQ mapeados:** …

**Dependencias:** …

**Criterios de aceptación (Gherkin):**
- **Nombre del escenario.** Dado …, cuando …, entonces …
**Evidencia / Definición de Terminado:**
- …
**Riesgos/Notas:**
- …
```

## 5. Definition of Ready (DoR)

Una HU puede empezar cuando:

1. Su spec está en `Diseño aprobado` y no tiene decisiones ❓ que la afecten.
2. Sus dependencias están terminadas o tienen un contrato acordado (API, evento, tabla).
3. Los criterios Gherkin son verificables sin interpretación.
4. Se sabe en qué repo vive y qué gate de `WORKFLOW.md` aplica (N1/N2/N3).

## 6. Definition of Done (DoD) común

Además de lo propio de cada HU, toda HU de código cumple:

- **Datos**: migración con `tenant_id` + RLS + índice compuesto; reversible o con plan de
  reversa; sin borrado físico.
- **API**: endpoints en `/api/v1` con permisos de sección; `docs/openapi.json` regenerado y tipos
  del panel actualizados.
- **Panel**: la vista sigue `DESIGN.md`, maneja carga, vacío y error, y no expone enums crudos.
- **Tests**: unitarios + integración + **aislamiento cross-tenant**; evals si cambia la conducta del
  asistente (golden set sin regresión).
- **Docs**: ADR si es estructural; `ROADMAP.md`, `CHANGELOG.md` y `BACKLOG.md` del repo dueño
  actualizados; frontmatter de la HU en `terminada`.
- **Evidencia**: enlace al PR, salida de tests o captura del panel en la sección de evidencia de la
  HU.
