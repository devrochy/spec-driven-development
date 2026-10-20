---
id: HU-AOS-30
titulo: "Agentes de back-office asíncronos"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, operacion]
req: [REQ-AOS-07]
dependencias: [HU-AOS-18]
skills: ["backend-design:idempotency-and-side-effects", "new-tool", "meta-whatsapp"]
estado: borrador
---

# HU-AOS-30 · Agentes de back-office asíncronos

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-30

**Título:** Agentes de back-office asíncronos

**Workstream:** Agent OS

**Historia:** Como dueño quiero agentes que trabajen en segundo plano (seguimiento de pedidos sin pagar, conciliación, resumen para el humano) sin escribir al cliente por su cuenta, para recuperar ventas y ahorrar trabajo con control.

**Por qué importa (valor empresarial):** Es trabajo asíncrono, fuera de la conversación con el cliente: ahí un agente con contexto propio sí aporta cuando el caso lo exige.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-07

**Dependencias:** [HU-AOS-18](HU-AOS-18-permisos-limites-y-ledger-a2a.md)

**Criterios de aceptación (Gherkin):**
- **Seguimiento.** Dado un pedido sin pago a las 24 h, cuando corre el trabajo de seguimiento de pack-commerce, entonces deja una propuesta en el outbox que el Coordinador de la conexión procesa como un turno sin mensaje entrante, con la release de la conversación; fuera de 24 h solo sale una plantilla por evento (ADR-0108).
- **Crons existentes.** Dado `pack_commerce.jobs.follow_up_leads` y `follow_up_quotes`, cuando corren, entonces proponen por el mismo camino y ya no escriben directo al cliente.
- **Conexión pausada.** Dado una conexión pausada (ADR-0122), cuando llega una propuesta, entonces queda `failed` sin reintento ni escalamiento; y el trabajo no corre ni gasta LLM sobre esa conexión.
- **Sin atajos.** Dado un agente de back-office, cuando intenta enviar un mensaje directo al cliente, entonces no tiene acción para hacerlo.
- **Presupuesto.** Dado `policies.backofficeBudgetUsdMonthly` del KernelSpec, cuando el gasto del mes lo alcanza, entonces los trabajos con LLM de esa conexión dejan de correr; el tope solo baja `costo_llm_usd` del plan.
- **Resumen.** Dado un escalamiento, cuando se crea, entonces aparece un resumen del caso armado desde tareas y hechos.

**Evidencia / Definición de Terminado:**
- `core/backoffice/` solo con el runner (disparo por outbox y cron, presupuesto, ledger y salida como propuesta); los trabajos con lógica de dominio en su pack (el core no conoce pedidos); `a2a_events` con `trigger` y gasto en `usage_ledger`.
- Prompts de los trabajos con LLM en el AgentSpec del agente `kind = backoffice` o en playbooks del pack, nunca en `core/backoffice/` (invariante 3).
- `packages/pack-commerce/pack_commerce/jobs.py` con los seguimientos como propuesta (ADR-0116 §5).

**Riesgos/Notas:**
- Mensajes fuera de la ventana de 24 h: siempre por plantilla (ADR-0108).
- Hoy los tres casos se resuelven con trabajos del `worker` y una llamada al LLM donde aporta; un agente de varios pasos se suma solo con un caso real.
- Hasta esta HU, los seguimientos de `pack_commerce.jobs` son la excepción conocida a "el back-office solo propone" (ADR-0112).
