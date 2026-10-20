---
id: HU-DS-09
titulo: Kit de componentes de la app
spec: SPEC-29
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-APP-11, REQ-UX-09]
dependencias: [HU-DS-01]
skills: ["frontend-design", "/code-review"]
estado: en-curso
---

# HU-DS-09 · Kit de componentes de la app

> Estado SDD: Lista para ejecutar — [SPEC-29](../spec.md) en Diseño aprobado (D-32).

**ID:** HU-DS-09

**Título:** Kit de componentes de la app

**Workstream:** App móvil

**Historia:** Como desarrollador de la app quiero un kit en `src/shared/ui` con los mismos nombres, variantes y estados que el del panel para construir pantallas consistentes y dejar de repetir estilos en cada archivo.

**Por qué importa (valor empresarial):** Hoy 48 archivos de la app tienen colores sueltos y 58 hojas de estilo propias. El kit hace que el panel y la app se vean como un solo producto, que es el argumento de venta de [SPEC-25](../../SPEC-25-app-movil-oficial/spec.md).

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-11, REQ-UX-09

**Dependencias:** [HU-DS-01](HU-DS-01-tokens-v2.md)

**Criterios de aceptación (Gherkin):**
- **Componentes.** Dado `src/shared/ui`, cuando lo reviso, entonces existen `Button`, `IconButton`, `Field`, `Badge`, `Avatar`, `Skeleton`, `EmptyState`, `Toast`, `Sheet`, `ListItem`/`RecordRow`, `KpiTile`, `PageHeader` y `SyncStatus`, todos sobre tokens v2.
- **Blancos táctiles.** Dado cualquier control del kit, cuando mido su área táctil, entonces es de al menos 48 × 48 dp.
- **Fuente del sistema.** Dado la fuente del sistema al 200 %, cuando abro la pantalla Catálogo de desarrollo, entonces ningún texto se corta ni se superpone.
- **Tipografía de marca.** Dado el kit, cuando reviso los textos, entonces usan Montserrat e Inter y no Roboto.
- **Lector de pantalla.** Dado TalkBack activo, cuando recorro los componentes, entonces cada control anuncia nombre, rol y estado.

**Evidencia / Definición de Terminado:**
- Pantalla Catálogo (solo en builds de desarrollo) con capturas en claro y oscuro desde el OPPO.
- Tests de RNTL por componente.
- ADR-APP-07 creado.

**Riesgos/Notas:**
- Los componentes de `modules/cobranza/components` que sean genéricos (`Avatar`, `ColorBadge`, `ModalConFooter`) suben a `shared/ui`; los de dominio se quedan.
- Respetar las fronteras de ADR-APP-01 (`check-module-boundaries`).
