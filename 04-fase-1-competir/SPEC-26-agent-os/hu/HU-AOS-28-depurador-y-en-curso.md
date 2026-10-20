---
id: HU-AOS-28
titulo: "Depurador conversacional y panel En curso"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, confianza]
req: [REQ-AOS-04, REQ-AOS-08]
dependencias: [HU-AOS-04, HU-AOS-18, HU-ARCH-14]
skills: ["panel-ui", "frontend-design", "backend-design:observability-by-default"]
estado: borrador
---

# HU-AOS-28 · Depurador conversacional y panel En curso

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-28

**Título:** Depurador conversacional y panel En curso

**Workstream:** Agent OS

**Historia:** Como dueño o agente humano quiero ver, por cada turno, la decisión, los comandos, las acciones, los cambios de estado y las comprobaciones, y ver "En curso" al tomar una conversación, para entender y continuar sin preguntar de nuevo.

**Por qué importa (valor empresarial):** Depurar en minutos en vez de horas, y un relevo humano coherente con lo que ya pasó.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-04, REQ-AOS-08

**Dependencias:** [HU-AOS-04](HU-AOS-04-estado-de-la-conversacion.md), [HU-AOS-18](HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-ARCH-14](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-14-playground-sandbox.md)

**Criterios de aceptación (Gherkin):**
- **Línea de tiempo.** Dado un turno con cambio de agente, cuando lo abre, entonces ve decisión, comandos, acciones, estado, comprobaciones, envío y costo en ≤ 2 s.
- **En curso.** Dado una conversación escalada con una tarea abierta, cuando una persona la toma, entonces ve qué falta sin leer todo el historial.
- **Redacción.** Dado un usuario sin `observabilidad:ver`, cuando abre el depurador, entonces no ve entradas ni salidas de acciones.
- **Reproducir.** Dado un turno, cuando lo reproduce con su versión, entonces corre en el playground sin efectos reales.

**Evidencia / Definición de Terminado:**
- Línea de tiempo y tarjeta "En curso" en el panel; API `/turns/{id}`; tests.

**Riesgos/Notas:**
- Datos personales: siempre redactados (P-17).
- Desde [D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas) (2026-10-19), esta HU queda con el depurador y el panel «En curso». La bandeja de conversaciones en vivo estilo WhatsApp Web pasa a [HU-UX-15](../../SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-15-bandeja-de-conversaciones.md) y los leads con datos del canal, enriquecidos y paginados, a [HU-UX-16](../../SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-16-clientes-estilo-agent-sale.md) y [HU-UX-12](../../SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-12-arreglos-rapidos-del-ciclo.md).
