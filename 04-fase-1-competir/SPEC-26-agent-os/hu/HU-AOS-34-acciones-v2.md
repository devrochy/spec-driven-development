---
id: HU-AOS-34
titulo: "Acciones v2: timeouts, reintentos, circuit breaker y respaldo"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-AOS-15]
dependencias: [HU-AOS-16]
skills: ["new-tool", "backend-design:error-handling-as-design", "backend-design:idempotency-and-side-effects"]
estado: borrador
---

# HU-AOS-34 · Acciones v2: timeouts, reintentos, circuit breaker y respaldo

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-34

**Título:** Acciones v2: timeouts, reintentos, circuit breaker y respaldo

**Workstream:** Agent OS

**Historia:** Como dueño quiero que una acción lenta o caída no arruine la conversación: que tenga un tiempo máximo, reintentos seguros y un respaldo claro, para que el cliente siempre reciba una respuesta útil.

**Por qué importa (valor empresarial):** La fiabilidad del agente también depende de sus integraciones; un proveedor caído no debe tumbar la venta.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-15

**Dependencias:** [HU-AOS-16](HU-AOS-16-habilidades-con-procedimientos-y-scope.md)

**Criterios de aceptación (Gherkin):**
- **Timeout.** Dado una acción con `timeoutMs` 5000, cuando tarda más, entonces se corta y se usa su respaldo.
- **Reintento seguro.** Dado una acción `irreversible`, cuando falla, entonces no se reintenta sola.
- **Circuit breaker.** Dado 5 fallos seguidos de una acción en un negocio, cuando llega otra llamada, entonces no se ofrece y se emite `tool.circuit.opened`.

**Evidencia / Definición de Terminado:**
- Metadatos de ejecución v2 (efecto, timeout, reintento, respaldo, scopes, clases de datos) declarados por el código del binario; `pack_versions` los copia para el linter y el panel y el runtime usa los del binario (ADR-0118 §4). Sin caché de resultados (ADR-0117 §7).
- El respaldo es un código de resultado cuyo texto sale de las respuestas configurables (ADR-0017), nunca texto literal en el manifiesto.
- Host con timeouts, reintentos y breaker; tests.

**Riesgos/Notas:**
- El breaker es por negocio y acción, para no apagar a todos por un proveedor de uno.
