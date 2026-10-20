---
id: HU-REP-04
titulo: Sin marca técnica ante el cliente
spec: SPEC-00
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: S
impacto: [confianza, diferenciacion]
req: [REQ-REP-03]
dependencias: []
skills: ["backend-design:testing-with-discernment", "/code-review", "pagos-wompi"]
ola: 1
estado: terminada
---

# HU-REP-04 · Sin marca técnica ante el cliente

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-00](../spec.md).

**ID:** HU-REP-04

**Título:** Sin marca técnica ante el cliente

**Workstream:** Arquitectura/Prod

**Historia:** Como cliente final de un negocio que usa SolversHub quiero que los links de pago y las invitaciones de calendario muestren el nombre del negocio o de SolversHub, no "agent-core", para confiar en que el cobro es legítimo.

**Por qué importa (valor empresarial):** Un nombre técnico desconocido en un link de pago es la señal clásica de fraude: baja la conversión y genera reclamos. El manual de marca lo prohíbe y el Hito 0A va a cobrar dinero real.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-REP-03

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Link de Wompi.** Dado un cobro de plataforma, cuando se crea el link, entonces la descripción usa el nombre del plan y "SolversHub", no "agent-core" (`core/billing/providers/wompi.py:81`).
- **Evento de calendario.** Dado una cita creada en modo Google, cuando el invitado ve el evento, entonces el texto usa el nombre del negocio (`pack_calendar/skills.py:388`).
- **Prueba que lo impide.** Dado un texto nuevo con "agent-core" en una cadena visible al cliente, cuando corre el CI, entonces un test de búsqueda sobre las cadenas de salida (links, correos, eventos, plantillas) falla.

**Evidencia / Definición de Terminado:**
- PR con los dos cambios y el test de regresión.

**Implementada (2026-10-02, PR #195 en `devrochy/agent-core`):**
- Wompi: el link usa `<plan> · SolversHub` y `Suscripción a SolversHub — plan <plan>`; `create_payment_link` recibe `plan_name`.
- Calendar: el evento usa el nombre del negocio (`_business_name`, fallback `SolversHub`).
- Test de regresión sobre plantillas/playbooks visibles + los dos puntos; los nombres internos quedan para [HU-REP-03](HU-REP-03-transicion-de-identificadores.md).
- Captura del link de Wompi en sandbox con la descripción nueva.

**Riesgos/Notas:**
- El nombre del negocio sale de `AppSettings`; si falta, se usa "SolversHub".
- Los nombres internos (logs, OTel, título de FastAPI) quedan para [HU-REP-03](HU-REP-03-transicion-de-identificadores.md).
