---
id: HU-INMO-06
titulo: "Agenda como capacidad del core"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Agenda
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, calidad_ia]
req: [REQ-INMO-06]
dependencias: [HU-INMO-05]
skills: ["agentcore-conventions", "backend-design:idempotency-and-side-effects", "adr"]
estado: borrador
---

# HU-INMO-06 · Agenda como capacidad del core

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-06

**Título:** Agenda como capacidad del core

**Workstream:** Agenda

**Historia:** Como habilidad que necesita agendar quiero reservar en la agenda del negocio con una interfaz del core, para no importar pack-calendar ni depender de que el LLM llame dos tools.

**Por qué importa (valor empresarial):** Sigue el patrón de `payment_registry` y `subscription_registry`: una sola escritura determinista que funciona igual antes y después del Agent OS (D-SPEC-28-4).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-06

**Dependencias:** [HU-INMO-05](HU-INMO-05-agenda-por-responsable.md)

**Criterios de aceptación (Gherkin):**
- **Idempotente.** Dado `reservar` con la misma `idempotency_key` dos veces, cuando se ejecuta, entonces queda una sola cita (único `(tenant_id, idempotency_key)`).
- **Choque.** Dado un horario ya ocupado en la agenda del asesor, cuando se intenta reservar, entonces devuelve un error de negocio con horarios alternativos y no una excepción.
- **Del negocio correcto.** Dado dos negocios con agenda, cuando una habilidad pide la capacidad, entonces se resuelve con `capability_for_tenant` del negocio actual y nunca con `capability_for(None)`.
- **Sin agenda.** Dado un negocio sin pack-calendar activo, cuando una habilidad pide la capacidad, entonces recibe "no disponible" y lo explica al cliente.

**Evidencia / Definición de Terminado:**
- `scheduling_registry` en el core con `disponibilidad`, `reservar`, `reagendar` y `cancelar` por `admin_id`; sin `obtener` (el estado llega por `appointment.*`).
- Implementación sin estado en la instancia; la `referencia` la pone el core con el id del pack que llama y las operaciones rechazan reservas de otro pack. ADR nuevo; tests.

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
