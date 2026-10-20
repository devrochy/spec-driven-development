---
id: HU-UI-12
titulo: Páginas de packs, Consumo y Plan compactas
spec: SPEC-13
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-UX-04, REQ-BILL-06]
dependencias: [HU-UI-08, HU-BILL-07]
skills: ["frontend-design", "kpi-dashboard-design", "panel-ui"]
estado: parqueada
---

# HU-UI-12 · Páginas de packs, Consumo y Plan compactas

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md).

**ID:** HU-UI-12

**Título:** Páginas de packs, Consumo y Plan compactas

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero que cobranza, comercio, agenda, consumo y plan se vean en pestañas y sub-menús compactos, sin páginas eternas ni botones repetidos, para encontrar lo que necesito de un vistazo.

**Por qué importa (valor empresarial):** Hoy la cartera apila 7 KPIs y 8 secciones, el resumen de cobranza tiene 11 botones que repiten el menú y Calendario muestra la misma tabla dos veces. La compacidad es exactamente lo que pidió el cliente.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-04, REQ-BILL-06

**Dependencias:** [HU-UI-08](HU-UI-08-filtros-y-tablas.md), HU-BILL-07

**Criterios de aceptación (Gherkin):**
- **Sub-navegación.** Dado Cobranza, cuando la abro, entonces la navegación interna es un sub-menú y no una fila de 11 botones.
- **Pestañas.** Dado el detalle de una cartera, cuando lo abro, entonces sus secciones son pestañas.
- **Sin duplicados.** Dado Calendario, cuando lo abro, entonces hay una sola tabla de citas y una vista semanal.
- **Consumo.** Dado Consumo, cuando lo abro, entonces hay pestañas IA y WhatsApp, gráfico por período y enlaces a las conversaciones más costosas.
- **Plan legible.** Dado Plan, cuando lo veo, entonces los límites se leen en lenguaje claro y hay llamados explícitos a recargar o cambiar de plan.

**Evidencia / Definición de Terminado:**
- Páginas migradas; capturas antes y después.

**Riesgos/Notas:**
- Las que encajan en descriptores se migran con [HU-FWK-07](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-07-descriptor-view.md).
