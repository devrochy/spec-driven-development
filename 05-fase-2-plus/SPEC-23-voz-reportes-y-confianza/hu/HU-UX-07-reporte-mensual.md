---
id: HU-UX-07
titulo: Reporte mensual automático por negocio
spec: SPEC-23
fase: 2
hito: "2"
workstream: UX/Onboarding
prioridad: P2
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-UX-08, REQ-COMP-06]
dependencias: [HU-UI-07, HU-BILL-07]
skills: ["kpi-dashboard-design", "pdf", "marketing:performance-report"]
estado: borrador
---

# HU-UX-07 · Reporte mensual automático por negocio

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-23](../spec.md).

**ID:** HU-UX-07

**Título:** Reporte mensual automático por negocio

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero recibir cada mes un resumen de lo que hizo mi asistente (conversaciones, ventas, cobros, consumo, calidad) para ver su valor sin entrar al panel.

**Por qué importa (valor empresarial):** El reporte mensual recuerda el valor justo antes de la renovación y reduce el churn; Zendesk y SleekFlow lo venden.

**Prioridad:** P2 plus

**Estimación:** M

**REQ mapeados:** REQ-UX-08, REQ-COMP-06

**Dependencias:** [HU-UI-07](../../../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md), HU-BILL-07

**Criterios de aceptación (Gherkin):**
- **Contenido.** Dado el cierre de mes, cuando se genera, entonces incluye conversaciones, % resuelto sin humano, ventas o cobros atribuidos, consumo y comparación con el mes anterior.
- **Entrega.** Dado las preferencias del owner, cuando se envía, entonces llega por correo o WhatsApp.

**Evidencia / Definición de Terminado:**
- Job y plantilla del reporte; tests.

**Riesgos/Notas:**
- —
