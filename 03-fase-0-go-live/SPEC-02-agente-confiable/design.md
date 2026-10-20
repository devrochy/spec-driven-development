# SPEC-02 · Diseño

## Errores de negocio (HU-ARCH-18)

```
core/shared/errors.py
  BusinessError(Exception)          # resultado controlado, NUNCA deshabilita
    ├─ PaymentCapabilityError       # hoy en core/payments
    ├─ SubscriptionError            # nuevo, core/subscriptions
    └─ ToolValidationError          # datos inválidos del LLM
  PluginError                       # falla de infraestructura del pack (sí cuenta)
```

En `loop.py` el `except PluginError` sigue igual; se agrega un `except BusinessError` previo que
devuelve `{"status": e.code, "mensaje": e.public_message}` a la tool y registra un evento de
auditoría. El host (`core/mcp/host.py:147-152`) deja de envolver un `BusinessError` como
`PluginError`.

## Plantillas fuera de 24 h (HU-ARCH-13)

- `ChannelAdapter.send_template(to, template_name, language, components)` en el adapter de WhatsApp
  Cloud (`gateway/channels/whatsapp/outbound.py`).
- `sender.send_to_conversation(..., is_template=True)` deja de ser una bandera muerta: si la ventana
  está cerrada y el evento tiene plantilla mapeada, envía la plantilla; si no tiene, se registra
  `sin_plantilla` y se avisa al negocio.
- Config por negocio `message_templates_map`: `{evento: {template, language, variables: {…}}}`,
  editable en el panel (Plantillas de la conexión). Las variables se resuelven del contexto del
  evento, nunca del LLM.
- La respuesta humana con 409 `window_expired` ofrece elegir una plantilla aprobada.

## Precondiciones y señal `escalate` (HU-ARCH-12)

- Las tools terminales declaran `requires` (por ejemplo, `generar_link_pago` requiere un pedido en
  estado `confirmado`). El host valida antes de ejecutar.
- Clave reservada `_escalate` en el resultado de una tool: el core la honra de forma determinista
  (crea la escalación y pausa el bot), sin depender del texto del LLM.
- `ToolContext.message_id` para llaves de idempotencia estables entre reintentos.
- Scopes en tools de pago (`payments:create_link`) verificados contra el binding del negocio.

## Golden sets y journeys

| Set | Escenarios mínimos | Multi-turno | Dónde |
|---|---|---|---|
| Comercio y restaurante | 15 | Sí: cotización → pedido → pago simulado → estado | [HU-ARCH-16](hu/HU-ARCH-16-golden-set-comercio.md) |
| Cobranza | 15 | Sí: saldo → promesa → link → pago simulado | [HU-ARCH-17](hu/HU-ARCH-17-golden-set-cobranza.md) |
| Planes y suscripciones | 10 | Sí, con eventos y reloj simulados | HU-SUB-12 |
| Asistente SolversHub | 10 | Sí, de la demo al alta | [HU-SH-08](../SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md) |

El runner de journeys (HU-SUB-12) inyecta eventos (`payment.confirmed`) y avanza el reloj; los
resultados se guardan por versión del spec y el nightly persiste corridas sin `--tenant`.

## Consistencia y verificación (HU-ARCH-28, HU-ARCH-29)

- **Runner de consistencia** sobre el de journeys (HU-SUB-12). Cada escenario declara:
  - cliente simulado (objetivo, datos que conoce, estilo, semilla);
  - datos sembrados;
  - aserciones sobre la base al terminar;
  - tope de turnos.

  Corre k veces (k = 4 nocturno, 8 antes de una release) y guarda pass@1, pass^k y la inestabilidad atribuida en `eval_runs` y `eval_results` (columnas aditivas: `k`, `pass_1`, `pass_k`, `simulator`, `state_assertions`, `verifier`).
- **Verificador de afirmaciones** en el core:
  - Extrae montos, links, fechas, referencias y frases de cierre del borrador.
  - Los compara con la evidencia: resultados de acciones del turno (`_tool_name`, `_ok`, `_current_turn`) y de turnos anteriores (`audit_log`).
  - Si no coincide: reintento correctivo (`guardrail_max_retries`) y luego la acción que configuró el negocio (`guardrail_fail_action`: neutral o escalar, ADR-0092). La mejora viene de menos falsos positivos.
  - Lee la configuración del negocio: `completion_claims_custom` de cada habilidad (ADR-0025), reglas `required_tool` (ADR-0051) y `disabled_guardrails`.
  - Reemplaza `crm_amount_check`, `crm_completion_check` y `calendar_completion_check` solo cuando los falsos positivos son ≤ 2 % en un set etiquetado.
- En la Fase 1, el verificador suma el estado de las tareas ([SPEC-26](../../04-fase-1-competir/SPEC-26-agent-os/spec.md), [HU-AOS-06](../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-06-comandos-y-verificador-sobre-estado.md)).

## ADR

- **Enmienda a ADR-0024**: errores de negocio frente a fallas de pack.
- **ADR "Plantillas por evento"**: mapeo evento → plantilla por negocio.
- **ADR-0119 · Fiabilidad medida**: verificador de afirmaciones y evals de consistencia (pass^k).

## Riesgos

| Riesgo | Mitigación |
|---|---|
| `deepseek-flash` no soporta bien tools | Respaldo configurable (`gpt-4o-mini`) y gate de evals (R-02) |
| Plantillas rechazadas por Meta | Biblioteca de plantillas de utilidad probadas por evento |
