---
id: HU-UI-06
titulo: Bandeja de conversaciones de dos paneles
spec: SPEC-13
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, diferenciacion]
req: [REQ-UX-04, REQ-FIX-04]
dependencias: [HU-UI-05, HU-ARCH-13]
skills: ["frontend-design", "figma-design-to-code", "built-in-browser", "web-perf", "panel-ui"]
estado: parqueada
---

# HU-UI-06 · Bandeja de conversaciones de dos paneles

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md) (D-SPEC-13-1, D-SPEC-13-2).

**ID:** HU-UI-06

**Título:** Bandeja de conversaciones de dos paneles

**Workstream:** UX/Onboarding

**Historia:** Como operador quiero una bandeja con la lista de conversaciones a la izquierda y el hilo a la derecha, con vista previa, pestañas, ventana de 24 h y el cuadro de respuesta abajo para atender rápido sin cambiar de página.

**Por qué importa (valor empresarial):** Es la pantalla más usada. Hoy responder exige dos cargas de página y el cuadro de respuesta está arriba del hilo. Una bandeja moderna es paridad obligatoria con todas las plataformas de la matriz.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-04, REQ-FIX-04

**Dependencias:** [HU-UI-05](HU-UI-05-tickets-reales.md), [HU-ARCH-13](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md)

**Criterios de aceptación (Gherkin):**
- **Lista.** Dado la bandeja, cuando la abro, entonces veo pestañas con contadores, conversaciones ordenadas por última actividad con vista previa, canal y estado.
- **Hilo.** Dado una conversación seleccionada, cuando la veo, entonces el cuadro de respuesta está abajo (Ctrl+Enter envía), se ve el estado de entrega y la ventana de 24 h.
- **Fuera de ventana.** Dado la ventana cerrada, cuando quiero responder, entonces el cuadro ofrece elegir una plantilla aprobada.
- **Actualización.** Dado la pestaña visible, cuando llega un mensaje, entonces aparece en menos de 10 s.
- **Acciones de ticket.** Dado una conversación escalada, cuando la abro, entonces las acciones de [HU-UI-05](HU-UI-05-tickets-reales.md) están en el encabezado.

**Evidencia / Definición de Terminado:**
- API con `last_activity_at`, último mensaje y ventana de servicio; página nueva; excepción documentada en `DESIGN.md`.

**Riesgos/Notas:**
- Accesibilidad: el hilo tiene `role="log"`.
