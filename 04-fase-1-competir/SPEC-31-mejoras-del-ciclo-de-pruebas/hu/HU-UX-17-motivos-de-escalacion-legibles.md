---
id: HU-UX-17
titulo: Motivos de escalación legibles con lista cerrada
spec: SPEC-31
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, calidad_ia]
req: [REQ-UX-20]
dependencias: []
skills: ["panel-ui", "frontend-design", "agentcore-conventions", "adr"]
estado: borrador
---

# HU-UX-17 · Motivos de escalación legibles con lista cerrada

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-UX-17

**Título:** Motivos de escalación legibles con lista cerrada

**Workstream:** UX/Onboarding

**Historia:** Como dueño quiero ver por qué el agente escaló cada conversación en palabras claras, con un color por tipo de motivo y la posibilidad de filtrar, para decidir rápido a qué atender primero.

**Por qué importa (valor empresarial):** Hoy el motivo sale como texto técnico (nombre de una herramienta o un código), y el que escribe el agente es libre. Con una lista cerrada el dueño entiende el motivo de un vistazo y el producto puede medir por qué escala el agente.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-20

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Motivo en palabras.** Dado una escalación porque una acción del agente falló, cuando abro Escalaciones, entonces veo «Acción de Ventas falló» y no el nombre técnico de la herramienta.
- **Lista cerrada del agente.** Dado que el agente decide escalar, cuando llama a la herramienta de escalar, entonces solo puede elegir solicitud del cliente, queja, fuera de alcance, intentos fallidos, monto alto u otro, más un detalle libre.
- **Color y filtro.** Dado la lista de escalaciones, cuando filtro por «Queja», entonces solo veo esas, y los motivos de riesgo se ven en tono de advertencia.
- **Texto completo.** Dado un resumen largo, cuando hago clic en él, entonces lo leo completo en un panel lateral.
- **Lo ya guardado.** Dado escalaciones viejas con el motivo libre, cuando las veo, entonces aparecen como «Otro» con su texto original como detalle.

**Evidencia / Definición de Terminado:**
- Core: `escalate_to_human` con enum y `detalle` (`core/tools/core_skill.py`); `EscalationItem.reason_code` y `reason_label` (`core/api/routers/escalations.py`) con los códigos del sistema (`keyword`, `llm_error`, `plugin:<tool>`, `regla:<x>`, `persona_forbidden_phrase`, `send_failed`, `turns_unresolved`, `max_iterations`); `?reason_code=`. Enmienda del ADR de escalaciones.
- Panel `escalaciones/page.tsx`: etiqueta y color por motivo, filtro, resumen completo en `ui/sheet.tsx`; catálogo ampliado en `lib/labels.ts`.
- Tests de API, del panel y de compatibilidad con motivos viejos.

**Riesgos/Notas:**
- Nota que lo motiva: ítem 3 del [inventario de SPEC-31](../design.md#inventario); referencia de agent-sale en `src/orchestrator/toolDefinitions.ts:299-318` y `src/admin/adminPanel.ts:4554-4583`.
- La bandeja ([HU-UX-15](HU-UX-15-bandeja-de-conversaciones.md)) reutiliza estas etiquetas.
