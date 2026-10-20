# SPEC-00 · Reestructuración `solvershub-<section>`

> Estado SDD: Diseño aprobado · Fase 0 · Hitos 0A ([HU-REP-04](hu/HU-REP-04-sin-fugas-de-marca-tecnica.md)) y 0B · Workstream Arquitectura/Prod

## Problema

SolversHub se partió en repos `solvershub-*`, pero la reestructura quedó a medias
([reestructura-y-nombres.md](../../01-revalidacion/reestructura-y-nombres.md)):

- El repo del motor se llama `agent-core` en GitHub y `solvershub-backend` en disco.
- Quedan residuos: la carpeta suelta `solvershub/apps/` (caché de un servidor de desarrollo), stubs
  vacíos en el backend, copias y tarballs viejos, y un venv que apunta a la ruta anterior.
- La documentación se desalineó: 13 enlaces rotos en comercial, README equivocados, `AGENTS.md` de la
  APK que describe NestJS.
- **"agent-core" se filtra a clientes** en el link de Wompi (`core/billing/providers/wompi.py:81`) y en
  los eventos de Google Calendar (`pack_calendar/skills.py:388`).
- La infraestructura (túneles, crontab, runners, inventario de Coolify) no está versionada.

## Usuarios y contexto

- **Equipo** (1 persona + agentes de IA, D-17): necesita saber dónde vive cada cosa.
- **Clientes finales**: ven la marca en links de pago e invitaciones de calendario.
- **Auditores y clientes enterprise**: piden saber cómo se recupera la plataforma ante un desastre.

## Por qué importa (valor empresarial)

Un comprador enterprise hace *due diligence*: pregunta dónde está la infraestructura, cómo se
restaura y quién es dueño de cada componente. Hoy la respuesta es "en la cabeza del fundador". Esta
spec convierte eso en repos con nombre claro, una marca consistente frente al cliente y la base de la
recuperación ante desastres que exige [SPEC-01](../SPEC-01-produccion-segura/spec.md).

## Alcance

| HU | Qué | Hito |
|---|---|---|
| [HU-REP-01](hu/HU-REP-01-limpiar-residuos.md) | Limpiar residuos | 0B |
| [HU-REP-02](hu/HU-REP-02-renombre-cosmetico.md) | Renombre cosmético y documentación | 0B |
| [HU-REP-03](hu/HU-REP-03-transicion-de-identificadores.md) | ADR y transición de identificadores rompedores con alias | 0B |
| [HU-REP-04](hu/HU-REP-04-sin-fugas-de-marca-tecnica.md) ★ | Sin marca técnica ante el cliente | 0A |
| [HU-REP-05](hu/HU-REP-05-repo-solvershub-docs.md) | Repo `solvershub-docs` y regla "un tema, un dueño" | 0B |
| [HU-REP-06](hu/HU-REP-06-solvershub-infra.md) ★ | `solvershub-infra` versionado | 0B |

## Escenarios clave

- **Marca limpia.** Dado un cliente que recibe un link de pago o una invitación de calendario, cuando
  lo abre, entonces no ve "agent-core" en ningún texto.
- **Arranque tras el renombre.** Dado el backend con el CLI renombrado, cuando un contenedor viejo
  arranca con `agent-core`, entonces el alias funciona y registra un aviso de deprecación.
- **Restauración desde cero.** Dado un servidor vacío, cuando el operador sigue `solvershub-infra`,
  entonces levanta túneles, runners y servicios sin conocimiento previo.

## Decisiones

### D-SPEC-00-1 · Nombre del repo del motor

| Opción | Pros | Contras |
|---|---|---|
| **A. `solvershub-core`** | Describe lo que es (motor + API + packs); cumple la convención | Renombrar GitHub, Coolify y runner |
| B. `solvershub-backend` también en GitHub | Coincide con la carpeta actual | "Backend" sugiere un servicio más, no el motor |
| C. Mantener `agent-core` | Cero trabajo | Rompe la convención y la marca |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): `solvershub-core`.

### D-SPEC-00-2 · Identificadores rompedores (CLI, entry points, variables)

| Opción | Pros | Contras |
|---|---|---|
| **A. Nombre nuevo + alias del viejo durante una transición, con ADR** | Sin cortes en despliegues | Dos nombres conviviendo un tiempo |
| B. Renombre de una vez | Limpio | Riesgo de romper el arranque de contenedores y saltar tests en silencio |
| C. No renombrar nunca | Cero riesgo | Deuda de marca permanente en lo interno |

**Recomendación: A.** Los IDs `pack_*`, la base `agent_core`, los streams de Redis y las cookies del
panel clásico **nunca** se renombran. Estado: ✅ tomada (2026-10-02): nombre nuevo + alias con ADR.

### D-SPEC-00-3 · `agentcore_contracts` (contrato inmutable, invariante 4)

| Opción | Pros | Contras |
|---|---|---|
| **A. Paquete nuevo `solvershub_contracts` que re-exporta el viejo (shim) + ADR** | Nombre correcto sin romper imports | Dos nombres para lo mismo |
| B. Mantener `agentcore_contracts` para siempre | Cero riesgo | Nombre técnico eterno |

**Recomendación: A**, sin prisa (puede quedar para la Fase 1). Estado: ✅ tomada (2026-10-02): shim `solvershub_contracts`, diferible.

## Fuera de alcance

- Renombrar IDs de plugin, base de datos, roles, streams o cookies.
- Separar la marca en su propio repo ([HU-REP-07](../../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-REP-07-solvershub-brand.md), Fase 1).
- Reescribir la historia de git.

## Métricas de éxito

- 0 apariciones de "agent-core" en textos que ve un cliente (test automatizado).
- 0 enlaces rotos entre repos (chequeo de enlaces en CI de `solvershub-docs`).
- Un simulacro de restauración se hace solo con `solvershub-infra` y su runbook.

## Requerimientos cubiertos

REQ-REP-01, REQ-REP-02, REQ-REP-03, REQ-ARCH-17.
