---
id: HU-UX-18
titulo: Listas y formularios de las secciones
spec: SPEC-31
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-UX-21]
dependencias: [HU-UX-12]
skills: ["panel-ui", "frontend-design"]
estado: borrador
---

# HU-UX-18 · Listas y formularios de las secciones

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-UX-18

**Título:** Listas y formularios de las secciones

**Workstream:** UX/Onboarding

**Historia:** Como dueño quiero buscar y abrir una promesa de pago, configurar una habilidad sin un formulario eterno, entender el cobro de la plataforma, encontrar los guardrails y ver como paso pendiente una habilidad sin configurar, para no perderme en las secciones.

**Por qué importa (valor empresarial):** Son las notas «no es claro» y «no encuentro» del dueño en secciones concretas. Cada una es chica, pero juntas explican buena parte de las pruebas bloqueadas.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-21

**Dependencias:** [HU-UX-12](HU-UX-12-arreglos-rapidos-del-ciclo.md)

**Criterios de aceptación (Gherkin):**
- **Promesas.** Dado Cobranza › Promesas, cuando filtro por estado y fecha y elijo una, entonces veo su detalle en un panel lateral.
- **Paleta a la promesa.** Dado la paleta de comandos, cuando elijo una promesa encontrada, entonces se abre esa promesa y no solo la ficha del cliente.
- **Formulario por grupos.** Dado la configuración de una habilidad con muchos campos, cuando la abro, entonces los campos aparecen agrupados en pestañas o bloques con título.
- **Guardrails a la vista.** Dado la ficha de un agente, cuando busco cómo apagar un guardrail, entonces hay un enlace directo a donde se configuran.
- **Habilidad sin configurar.** Dado una habilidad activa a la que le falta configuración, cuando miro los primeros pasos, entonces aparece un paso «Configura <habilidad>» que me lleva a su formulario.

**Evidencia / Definición de Terminado:**
- `cobranza/promesas/page.tsx` con `components/templates/list-page.tsx`, filtros y `ui/sheet.tsx`; `lib/shell/paleta.ts` (`rutaDeResultado`) abre la promesa.
- `x-group` en los schemas de config de pack_calendar, pack_payments y pack_cobranza; `components/domain/json-schema-form.tsx` por pestañas cuando hay grupos.
- Cobro de la plataforma: canal, estado y próximo paso de cada cobro.
- Enlace a los guardrails desde la ficha del agente; paso «configurar la habilidad» en `lib/primeros-pasos.ts` (y en el core si falta el motivo).

**Riesgos/Notas:**
- Notas que lo motivan: ítems 16 a 20 del [inventario de SPEC-31](../design.md#inventario).
