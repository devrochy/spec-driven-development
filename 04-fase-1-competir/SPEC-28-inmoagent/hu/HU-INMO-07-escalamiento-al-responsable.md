---
id: HU-INMO-07
titulo: "Relevo al asesor del caso"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: S
impacto: [operacion, confianza]
req: [REQ-INMO-07]
dependencias: [HU-INMO-10]
skills: ["agentcore-conventions", "new-tool"]
estado: borrador
---

# HU-INMO-07 · Relevo al asesor del caso

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-07

**Título:** Relevo al asesor del caso

**Workstream:** Verticales

**Historia:** Como asesor quiero que las conversaciones de mis clientes y de mis inmuebles me lleguen a mí cuando el asistente escala, para responder rápido sin que el dueño reparta a mano.

**Por qué importa (valor empresarial):** Hoy `escalate()` avisa a todos los dueños y `escalations.assigned_admin_id` no se usa (`core/orchestrator/escalation.py`, `core/db/models.py:733`). Un relevo que nadie toma es un cliente perdido.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-INMO-07

**Dependencias:** [HU-INMO-10](HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md)

**Criterios de aceptación (Gherkin):**
- **Asignación.** Dado una conversación de un cliente con asesor (oportunidad o inmueble), cuando se dispara `escalation.triggered`, entonces el pack llena `assigned_admin_id` con ese asesor y le avisa con `send_push_batch`.
- **Sin asesor.** Dado un cliente sin asesor, cuando se escala, entonces se avisa a los dueños como hoy.
- **Asesor de otro negocio.** Dado un `admin_id` que no está en `tenant_user` del negocio, cuando se intenta asignar, entonces se rechaza y se avisa a los dueños.

**Evidencia / Definición de Terminado:**
- Suscripción del pack a `escalation.triggered` (ADR-0107); sin registro nuevo en el core; tests.

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- Un registro de enrutamiento en el core solo cuando lo pida una segunda vertical.
