---
id: HU-ARCH-07
titulo: Observabilidad de producción con alertas
spec: SPEC-01
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, operacion]
req: [REQ-ARCH-09]
dependencias: [HU-ARCH-01]
skills: ["backend-design:observability-by-default", "kpi-dashboard-design", "incident"]
estado: borrador
---

# HU-ARCH-07 · Observabilidad de producción con alertas

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-01](../spec.md) (D-SPEC-01-2).

**ID:** HU-ARCH-07

**Título:** Observabilidad de producción con alertas

**Workstream:** Arquitectura/Prod

**Historia:** Como operador quiero errores, latencias, lag de la cola, DLQ y costo por hora visibles con alertas para enterarme de un problema antes que el cliente.

**Por qué importa (valor empresarial):** Sin medición, los SLO publicados no son verificables y cada incidente se descubre por la queja de un cliente. También cubre el riesgo de gasto de LLM sin techo antes de los créditos (R-09).

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-09

**Dependencias:** [HU-ARCH-01](HU-ARCH-01-produccion-fuera-de-dev.md)

**Criterios de aceptación (Gherkin):**
- **Healthz profundo.** Dado Postgres caído, cuando se consulta `/healthz`, entonces responde con error e indica el componente.
- **Errores.** Dado una excepción no controlada en producción, cuando ocurre, entonces aparece en Sentry con el negocio (sin datos personales) y dispara una alerta.
- **Latencia y cola.** Dado el webhook, cuando el p99 supera 1 s durante 5 minutos o la DLQ tiene entradas, entonces llega una alerta.
- **Costo.** Dado el consumo de LLM por hora, cuando supera 3 veces el promedio de la semana, entonces llega una alerta.

**Evidencia / Definición de Terminado:**
- Tablero con las señales de la tabla de `design.md`.
- Alertas probadas con un fallo provocado en test.

**Riesgos/Notas:**
- No enviar contenido de mensajes ni datos personales a terceros (Sentry, OTLP).
