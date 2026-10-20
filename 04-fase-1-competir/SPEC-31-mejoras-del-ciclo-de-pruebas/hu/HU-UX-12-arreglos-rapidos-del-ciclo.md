---
id: HU-UX-12
titulo: Arreglos rápidos del ciclo de pruebas
spec: SPEC-31
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: S
impacto: [operacion, confianza]
req: [REQ-UX-16]
dependencias: [HU-UX-02]
skills: ["panel-ui", "frontend-design"]
estado: borrador
---

# HU-UX-12 · Arreglos rápidos del ciclo de pruebas

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-UX-12

**Título:** Arreglos rápidos del ciclo de pruebas

**Workstream:** UX/Onboarding

**Historia:** Como dueño quiero que los detalles que fallaron en las pruebas (tooltips que no se ven, el período de Agentes, el pago pendiente sin enlace, la doble paginación y el canal en jerga) funcionen, para no tropezar en cada sección.

**Por qué importa (valor empresarial):** Son cinco arreglos chicos que el dueño encontró en su recorrido y que dan la impresión de un producto sin terminar. Con un solo PR de panel desaparecen y destraban UX-13 (la ayuda de los campos usa el mismo tooltip).

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-UX-16

**Dependencias:** [HU-UX-02](../../SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md)

**Criterios de aceptación (Gherkin):**
- **Tooltip en la barra plegada.** Dado la barra lateral plegada, cuando paso el puntero o pongo el foco en un ícono, entonces veo su nombre completo encima de todo y no aparece una barra de scroll lateral que tape los íconos.
- **Ícono de información en una tabla.** Dado la cabecera «Permisos» de Colaboradores, cuando paso el puntero o hago clic en su ícono de información, entonces veo la explicación y la columna no se reordena.
- **Período de Agentes.** Dado que elegí 7 días en Agentes y navegué a otra pestaña, cuando vuelvo y la dirección dice 30 días, entonces el selector también muestra 30 días.
- **Pagar desde la fila.** Dado un pago pendiente en Consumo y plan, cuando miro su fila, entonces tiene una acción «Pagar» que abre el enlace de pago.
- **Una sola paginación.** Dado Clientes con más de una página, cuando miro la tabla, entonces solo veo Anterior y Siguiente, sin flechas que no hacen nada.
- **Canal legible.** Dado una conversación o un cliente de WhatsApp oficial, cuando miro la columna Canal, entonces dice «WhatsApp» y no «whatsapp_cloud».

**Evidencia / Definición de Terminado:**
- `components/ui/tooltip.tsx` con portal (Radix, como `ui/popover.tsx`); lo usan `IconoDeRiel` en `components/shell/sidebar.tsx` y las cabeceras de `components/ui/data-table.tsx`; el clic en el ícono no dispara el orden de `ui/table-enhancer.tsx`.
- `agentes/_components/agent-filters.tsx`: `key={dias}` o selector controlado.
- `plan/page.tsx`: acción con `ui/icon-action.tsx` y `checkout_url` en los pagos pendientes.
- `DataTable` con una prop que apaga `TableEnhancer` en las listas que paginan en el servidor (Clientes, Conversaciones).
- `canalLabel` de `lib/labels.ts` en Conversaciones y Clientes.
- Tests de componente de cada punto y axe; `typecheck`, `lint`, `test:coverage` y `build` en verde.

**Riesgos/Notas:**
- Notas que lo motivan: ítems 4 (paginado), 5, 6 y 7 del [inventario de SPEC-31](../design.md#inventario).
- No toca `lib/labels.ts` salvo para importar: los motivos de escalación son de [HU-UX-17](HU-UX-17-motivos-de-escalacion-legibles.md).
