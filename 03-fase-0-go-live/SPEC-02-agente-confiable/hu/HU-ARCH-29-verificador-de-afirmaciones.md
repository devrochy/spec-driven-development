---
id: HU-ARCH-29
titulo: "Verificador de afirmaciones con modelo de evidencia"
spec: SPEC-02
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: false
estimacion: M
impacto: [calidad_ia, confianza, ingreso]
req: [REQ-ARCH-21]
dependencias: [HU-COM-02]
skills: ["agentcore-conventions", "backend-design:testing-with-discernment", "eval-author"]
ola: 4
estado: borrador
---

# HU-ARCH-29 · Verificador de afirmaciones con modelo de evidencia

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-02](../spec.md).

**ID:** HU-ARCH-29

**Título:** Verificador de afirmaciones con modelo de evidencia

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de un negocio quiero que, antes de enviar cada respuesta, se compruebe que montos, links, fechas, números de pedido y estados coinciden con lo que el sistema hizo, para que el asistente nunca afirme algo falso ni escale una compra válida.

**Por qué importa (valor empresarial):** Hoy tres reglas de seguridad (`crm_amount_check`, `crm_completion_check`, `calendar_completion_check`) escalan a mitad de compras válidas: se pierde la venta y el bot queda pausado. Un verificador con un modelo de evidencia común baja los falsos positivos y mantiene la promesa de "IA confiable" (constitución §1.2).

**Prioridad:** P0 go-live (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-21

**Dependencias:** [HU-COM-02](../../SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md)

**Criterios de aceptación (Gherkin):**
- **Monto con evidencia.** Dado un turno en que `generar_cotizacion` devolvió total 600000, cuando el borrador dice "$600.000", entonces la comprobación pasa; y cuando dice "$500.000", entonces se pide un reintento con el monto correcto.
- **Monto de un turno anterior.** Dado un monto confirmado por una acción en un turno anterior de la misma conversación, cuando el cliente pregunta de nuevo y el borrador lo repite, entonces la comprobación pasa y no hay escalamiento.
- **Cierre sin acción.** Dado un borrador que dice "tu pedido quedó creado" sin `crear_pedido` exitoso en el turno, cuando se verifica, entonces falla con motivo `status_sin_evidencia`, se reintenta según `guardrail_max_retries` y, si reincide, aplica la acción que configuró el negocio (`guardrail_fail_action`, ADR-0092).
- **Link exacto.** Dado un link de pago devuelto por la acción, cuando el borrador trae otra URL, entonces se reemplaza por la del servidor o se quita.
- **Configuración del negocio.** Dado un negocio con `completion_claims_custom` (ADR-0025), reglas `required_tool` (ADR-0051) o un guardrail en `disabled_guardrails`, cuando corre el verificador, entonces usa esas frases como afirmaciones de cierre, exige esas acciones y respeta lo apagado.
- **Falsos positivos medidos.** Dado el set etiquetado de respuestas correctas, cuando corre el verificador, entonces los falsos positivos son ≤ 2 % antes de retirar los tres guardrails anteriores.

**Evidencia / Definición de Terminado:**
- Verificador en el core con extracción de montos, links, fechas, referencias y frases de cierre, y evidencia de las acciones del turno y de `audit_log`.
- Integrado en el loop; los tres guardrails heurísticos se retiran solo después de medir los falsos positivos.
- Veredictos guardados por turno para métricas; set etiquetado versionado; journeys sin escalamientos falsos.

**Riesgos/Notas:**
- Parsers de moneda y fecha en español: tests con variantes reales de los negocios.
- Las frases de cierre dependen de la vertical: salen de los packs y de `completion_claims_custom` del negocio, siempre como frases literales (ADR-0025).
