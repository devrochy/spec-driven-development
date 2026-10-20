---
id: HU-ARCH-19
titulo: MCP por tenant con allowlist y circuit breaker
spec: SPEC-19
fase: 1
hito: "1"
workstream: Framework/Plugins
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, ingreso]
req: [REQ-ARCH-06, REQ-COMP-02]
dependencias: [HU-ARCH-12]
skills: ["adr", "backend-design:security-discipline", "backend-design:security-reviewer", "backend-design:boring-tech-advisor"]
estado: borrador
---

# HU-ARCH-19 · MCP por tenant con allowlist y circuit breaker

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-19](../spec.md).

**ID:** HU-ARCH-19

**Título:** MCP por tenant con allowlist y circuit breaker

**Workstream:** Framework/Plugins

**Historia:** Como negocio que usa un CRM, un ERP o una hoja de cálculo quiero conectar su servidor MCP a mi asistente, eligiendo qué herramientas puede usar, para que consulte y actualice mis sistemas sin desarrollo a medida.

**Por qué importa (valor empresarial):** Las integraciones son el criterio de compra de los clientes medianos y la mayor brecha frente a Lety (900+ vía MCP). Con allowlist, scopes y circuit breaker se hace sin poner en riesgo a otros negocios.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-ARCH-06, REQ-COMP-02

**Dependencias:** [HU-ARCH-12](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md)

**Criterios de aceptación (Gherkin):**
- **Registrar.** Dado la URL y credenciales de un servidor MCP, cuando lo registro, entonces veo sus herramientas y elijo cuáles habilitar.
- **Aislamiento.** Dado dos negocios, cuando uno usa su MCP, entonces el otro no puede verlo ni usarlo.
- **Circuit breaker.** Dado un servidor MCP que falla 5 veces seguidas, cuando ocurre, entonces se abre el circuito y el asistente lo trata como no disponible, sin deshabilitar otras habilidades.
- **Datos, no órdenes.** Dado una respuesta del MCP con instrucciones, cuando llega, entonces se trata como dato (invariante 7).

**Evidencia / Definición de Terminado:**
- ADR de MCP por tenant; cliente MCP en el core; tests de aislamiento y de fallas.

**Riesgos/Notas:**
- Plan Premium o superior.
