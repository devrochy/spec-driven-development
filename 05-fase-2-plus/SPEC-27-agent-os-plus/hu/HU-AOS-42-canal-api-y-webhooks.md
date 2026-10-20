---
id: HU-AOS-42
titulo: "Canal API y webhooks salientes como conexión"
spec: SPEC-27
fase: 2
hito: "2"
workstream: Agent OS
prioridad: P2
critico: false
estimacion: M
impacto: [diferenciacion, ingreso]
req: [REQ-AOS-01]
dependencias: [HU-AOS-11]
skills: ["backend-design:auth-and-authorization", "backend-design:idempotency-and-side-effects"]
estado: borrador
---

# HU-AOS-42 · Canal API y webhooks salientes como conexión

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-27](../spec.md).

**ID:** HU-AOS-42

**Título:** Canal API y webhooks salientes como conexión

**Workstream:** Agent OS

**Historia:** Como integrador quiero conversar con un agente por API y recibir eventos firmados, para integrar el Agent OS con mis sistemas.

**Por qué importa (valor empresarial):** Abre el Agent OS a integraciones y pruebas automáticas sin canal de mensajería.

**Prioridad:** P2 plus

**Estimación:** M

**REQ mapeados:** REQ-AOS-01

**Dependencias:** [HU-AOS-11](../../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-11-conexion-canonica.md)

**Criterios de aceptación (Gherkin):**
- **Alta.** Dado una conexión de tipo `api`, cuando se crea, entonces recibe una clave y su Coordinador.
- **Mensajes idempotentes.** Dado un mensaje enviado dos veces con la misma clave de idempotencia, cuando llega, entonces se procesa una sola vez.
- **Webhooks firmados.** Dado una suscripción a `task.completed`, cuando ocurre, entonces se envía firmado con HMAC y con reintentos.

**Evidencia / Definición de Terminado:**
- Tipo de conexión `api`; endpoints; webhooks salientes firmados; tests.

**Riesgos/Notas:**
- Abuso de la API: rate limit por conexión.
