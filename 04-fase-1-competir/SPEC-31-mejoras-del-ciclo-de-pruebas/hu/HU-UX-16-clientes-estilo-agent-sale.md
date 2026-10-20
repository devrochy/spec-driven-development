---
id: HU-UX-16
titulo: Clientes con ficha editable y pausa del agente por cliente
spec: SPEC-31
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, diferenciacion, calidad_ia]
req: [REQ-UX-19]
dependencias: [HU-UX-12]
skills: ["panel-ui", "frontend-design", "agentcore-conventions", "backend-design:query-discipline", "auditor-multitenant"]
estado: borrador
---

# HU-UX-16 · Clientes con ficha editable y pausa del agente por cliente

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-UX-16

**Título:** Clientes con ficha editable y pausa del agente por cliente

**Workstream:** UX/Onboarding

**Historia:** Como dueño quiero ver a cada cliente con lo que el agente ya sabe de él, poder corregirlo, pausar el agente solo para ese cliente, ver su clasificación y filtrar por canal o conexión, para atenderlo bien sin volver a preguntarle lo mismo.

**Por qué importa (valor empresarial):** El dueño ya opera así en agent-sale y lo pidió textual. Pausar a un cliente puntual (un reclamo, un caso delicado) sin apagar el agente para todos evita perder ventas; ver lo que el agente aprendió da confianza en que no le pregunta dos veces lo mismo.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-19

**Dependencias:** [HU-UX-12](HU-UX-12-arreglos-rapidos-del-ciclo.md)

**Criterios de aceptación (Gherkin):**
- **Pausar por cliente.** Dado un cliente en Clientes, cuando apago su interruptor «Agente», entonces el agente deja de responderle en todas sus conversaciones hasta que lo enciendo de nuevo.
- **Ficha con lo aprendido.** Dado un cliente al que el agente le guardó nombre, documento y dirección, cuando abro su ficha, entonces veo esos datos con su origen (agente o persona) y la fecha.
- **Corregir un dato.** Dado la ficha de un cliente, cuando corrijo su dirección y guardo, entonces queda guardada como dato de una persona y el agente la usa en la siguiente conversación.
- **Clasificación.** Dado un negocio con la habilidad de ventas, cuando miro Clientes, entonces cada cliente muestra su clasificación (nuevo, ocasional, frecuente, fiel o inactivo) y puedo filtrar por ella.
- **Filtrar por conexión.** Dado clientes que llegaron por dos conexiones distintas, cuando filtro por una conexión, entonces solo veo los clientes que escribieron por ella.
- **Exportar.** Dado la lista filtrada, cuando elijo exportar, entonces descargo un CSV con esas filas.

**Evidencia / Definición de Terminado:**
- Core `core/api/routers/leads.py`: `POST /admin/leads/{id}/toggle-bot` sobre `Customer.bot_paused` (ya respetado en `core/kernel/ingress.py`); `GET /admin/leads/{id}` con datos del canal y `memory_facts` con origen; `PATCH /admin/leads/{id}` que escribe **solo** por `core/memory/facts.py` con `source="human"`; filtros `channel`, `connection_id` (EXISTS sobre conversaciones) y `clasificacion`; CSV. Tests de API, de aislamiento y del escritor único.
- pack_commerce: columna de clasificación por `lead_registry`, calculada como `clasificarCliente` de agent-sale (D-SPEC-31-2).
- Panel `/leads`: interruptor con `ui/switch.tsx`, ficha lateral `ui/sheet.tsx` + `ui/field.tsx` reutilizable desde la bandeja, filtros y CSV con `lib/csv.ts`.
- Revisión de los prompts para que usen `get_customer_profile` antes de pedir un dato (eval corto en replay).

**Riesgos/Notas:**
- Notas que lo motivan: ítem 4 del [inventario de SPEC-31](../design.md#inventario); referencia de agent-sale en `src/admin/adminPanel.ts:4142-4286` y `migrations/0046`, `0050`, `0054`.
- El paginado real va en [HU-UX-12](HU-UX-12-arreglos-rapidos-del-ciclo.md).
