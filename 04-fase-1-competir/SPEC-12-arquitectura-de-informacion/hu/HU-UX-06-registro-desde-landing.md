---
id: HU-UX-06
titulo: Registro directo desde la landing
spec: SPEC-12
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso]
req: [REQ-UX-02, REQ-COMP-08]
dependencias: [HU-SH-03, HU-SH-07]
skills: ["turnstile-spin", "frontend-design", "backend-design:security-discipline"]
estado: borrador
---

# HU-UX-06 · Registro directo desde la landing

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-12](../spec.md).

**ID:** HU-UX-06

**Título:** Registro directo desde la landing

**Workstream:** UX/Onboarding

**Historia:** Como prospecto que prefiere no conversar quiero crear mi cuenta Free desde un formulario de la landing y recibir mi invitación para empezar a probar en minutos.

**Por qué importa (valor empresarial):** Un porcentaje de prospectos no quiere hablar con un asistente antes de probar. Un formulario que reutiliza el mismo aprovisionamiento y antiabuso abre ese canal sin trabajo operativo.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-02, REQ-COMP-08

**Dependencias:** [HU-SH-03](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md), [HU-SH-07](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-07-antiabuso-y-cumplimiento.md)

**Criterios de aceptación (Gherkin):**
- **Registro.** Dado el formulario con nombre, correo, teléfono y vertical, cuando lo envío y verifico mi correo, entonces se crea mi negocio Free con el preset del vertical y recibo la invitación.
- **Antiabuso.** Dado un teléfono que ya tuvo un Free, cuando se registra, entonces se le ofrece un plan pago.
- **Términos.** Dado el registro, cuando acepto, entonces queda la aceptación con la versión vigente.

**Evidencia / Definición de Terminado:**
- Formulario con Turnstile; endpoint público que reutiliza el consumidor de aprovisionamiento; tests.

**Riesgos/Notas:**
- Comparte reglas con [HU-SH-07](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-07-antiabuso-y-cumplimiento.md).
