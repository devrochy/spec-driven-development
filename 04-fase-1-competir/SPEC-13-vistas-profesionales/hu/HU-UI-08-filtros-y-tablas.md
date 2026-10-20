---
id: HU-UI-08
titulo: FilterBar único y tablas densas
spec: SPEC-13
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-UX-04]
dependencias: [HU-UI-03, HU-DS-03]
skills: ["frontend-design", "backend-design:query-discipline", "panel-ui"]
estado: parqueada
---

# HU-UI-08 · `FilterBar` único y tablas densas

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md) (D-SPEC-13-1).

**ID:** HU-UI-08

**Título:** FilterBar único y tablas densas

**Workstream:** UX/Onboarding

**Historia:** Como operador quiero filtrar, buscar, ordenar y paginar cada lista de una sola forma, con filas compactas que se abren con un clic, para revisar mucha información rápido.

**Por qué importa (valor empresarial):** Hoy hay dos buscadores y dos paginadores por lista y la búsqueda del cliente solo mira la página actual. Es la causa principal de que el panel se sienta "pesado".

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-04

**Dependencias:** [HU-UI-03](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md), [HU-DS-03](../../SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-03-kit-de-componentes-panel.md)

**Criterios de aceptación (Gherkin):**
- **Un solo control.** Dado Conversaciones, Clientes y Por atender, cuando las abro, entonces hay un solo `FilterBar` y la paginación es del servidor.
- **Orden accesible.** Dado una columna ordenable, cuando la activo con teclado, entonces cambia el orden y se anuncia con `aria-sort`.
- **Fila clicable.** Dado una fila, cuando la pulso, entonces abre su detalle.
- **Densidad.** Dado la excepción de densidad en `DESIGN.md`, cuando se aplica, entonces las tablas muestran más filas sin romper el contraste ni el foco.

**Evidencia / Definición de Terminado:**
- `DataTable` sin `TableEnhancer` cliente; componente `FilterBar`; tests.

**Riesgos/Notas:**
- Usa la `DataTable` v2 y las plantillas del kit de [HU-DS-03](../../SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-03-kit-de-componentes-panel.md) (D-32, D-SPEC-29-1).
- Base de `<DescriptorView>` ([HU-FWK-07](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-07-descriptor-view.md)).
