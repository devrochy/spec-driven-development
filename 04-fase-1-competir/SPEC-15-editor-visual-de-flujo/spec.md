# SPEC-15 · Editor visual del flujo por pack

> Estado SDD: Parqueada (2026-10-17, D-35) · Fase 1 · Workstream Flujo visual

**Parqueada (2026-10-17, [D-35](../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes)):** el flujo por pack (`flow.json`) deja de ser lo que el dueño edita: los agentes se configuran con superpoderes (procedimientos tipados, [HU-AOS-05](../SPEC-26-agent-os/hu/HU-AOS-05-motor-de-procedimientos.md)) y el editor vive en [HU-AOS-25](../SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md) y [HU-AOS-45](../../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md). Cierra P-21 para esta spec; [HU-FLOW-07](../../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FLOW-07-purpose-y-reglas-por-etapa.md) y [HU-ARCH-26](../../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md) ([SPEC-22](../../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/spec.md), fase 2) quedan pendientes del dueño.

## Problema

El flujo de atención (`flow.json`, ADR-0054) define qué tools usa el asistente en cada etapa, pero se
edita solo por archivo y el panel lo muestra en lectura (ADR-0017/0026/0054 §5). El encargo pide un
**editor visual y dinámico por tenant** que permita agregar, quitar y reordenar las tools que aporta
cada pack, aprovechando `flow.json`, el AgentSpec (ADR-0050) y los descriptores del panel.

## Por qué importa (valor empresarial)

Hubtype y SleekFlow venden su flow builder como diferencial. Un editor que el dueño entiende reduce
la dependencia de un implementador para cada ajuste y hace visible el "superpoder" de combinar
habilidades. Debe ser seguro: un cambio se prueba antes de publicarse y se puede revertir.

## Alcance

| HU | Qué |
|---|---|
| [HU-FLOW-01](hu/HU-FLOW-01-adr-editor-de-flujo.md) | ADR del editor de flujo |
| [HU-FLOW-02](hu/HU-FLOW-02-flujo-en-agentspec.md) | Flujo versionado dentro del AgentSpec |
| [HU-FLOW-03](hu/HU-FLOW-03-validador-y-api.md) | Esquema, validador único, API y catálogo de acciones |
| [HU-FLOW-04](hu/HU-FLOW-04-editor-visual.md) | Editor visual |
| [HU-FLOW-05](hu/HU-FLOW-05-borrador-y-publicacion.md) | Borrador, prueba, publicación y reversa |
| [HU-FLOW-06](hu/HU-FLOW-06-flujo-semilla-por-preset.md) | Flujo semilla por preset |

## Decisiones

- Quién edita el texto de las etapas: [P-09](../../02-vision-y-decisiones/preguntas-abiertas.md#p-09--quién-edita-el-purpose-de-las-etapas-del-flujo).

### D-SPEC-15-1 · Dónde vive el flujo

| Opción | Pros | Contras |
|---|---|---|
| **A. `AgentSpec.extensions["flow"]` con borrador separado** | Versionado y reversa del spec; sin tocar el contrato | Migrar los flujos actuales |
| B. Tabla `tenant_flows` | Independiente | Otra versión que sincronizar con el spec |
| C. Archivo (hoy) | Sin cambios | No editable en el panel |

**Recomendación: A.** Estado: ⏳ pendiente.

> Afectada por [SPEC-26](../SPEC-26-agent-os/spec.md) (D-27): el flujo pasa a los procedimientos de las habilidades y al AgentSpec v3. La propuesta de reencuadrar esta spec como editor de superpoderes está en [P-21](../../02-vision-y-decisiones/preguntas-abiertas.md#p-21--spec-15-como-editor-de-superpoderes).

### D-SPEC-15-2 · Arrastrar y soltar

| Opción | Pros | Contras |
|---|---|---|
| **A. `dnd-kit` (React, sensores de teclado)** | Accesible por teclado; encaja con Next.js | Una dependencia |
| B. SortableJS | Probado | No es nativo de React; accesibilidad limitada |
| C. Botones subir/bajar sin arrastre | Sin dependencias | Menos usable |

**Recomendación: A**, con C como alternativa accesible siempre disponible. Estado: ⏳ pendiente.

## Métricas de éxito

- Al menos un negocio cambia su flujo sin soporte y sin regresión en sus evals.

## Requerimientos cubiertos

REQ-FLOW-01 a REQ-FLOW-04, REQ-FIX-03.
