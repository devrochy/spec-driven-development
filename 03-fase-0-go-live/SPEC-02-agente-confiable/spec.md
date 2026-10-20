# SPEC-02 · Agente confiable, calidad ≥95 %

> Estado SDD: Diseño aprobado · Fase 0 · Hitos 0A y 0B · Workstreams Arquitectura/Prod y Comercio

## Problema

- **El modelo por defecto ya no existe**: `deepseek-chat` y `deepseek-reasoner` se discontinuaron el
  2026-07-24 (re-verificado: `core/config.py:89-90`).
- **Meta cobra cada mensaje de servicio desde hoy (2026-10-01)** y el estilo por defecto
  `pocos_cortos` parte cada respuesta en hasta 3 burbujas (`core/config.py:143`): hasta 3 cobros por
  turno.
- **Un error de negocio apaga la habilidad**: cualquier excepción de una tool termina en
  `auto_disable_for_tenant` (re-verificado: `core/orchestrator/loop.py:670-675`). Un monto bajo el
  mínimo de Wompi en `sub_link_pago` deshabilita las suscripciones de ese negocio.
- **Acciones terminales protegidas solo por regex**: solo `crear_pedido` tiene precondición; la señal
  `escalate` que devuelven las tools no se lee; ninguna tool declara `scopes`.
- **Fuera de la ventana de 24 h no se puede escribir**: el adapter solo tiene `send_text` y
  `send_image`; recordatorios, avisos de cobro y seguimientos quedan `failed`. La respuesta humana
  fuera de ventana ya devuelve 409 `window_expired` (`api/routers/conversations.py:179-201`) pero no
  puede ofrecer una plantilla.
- **El playground ejecuta tools reales** (pedidos, links de Wompi, citas, correos).
- **Caché de Anthropic con más de 4 breakpoints** (`core/llm/anthropic_provider.py:55-62`).
- **Calidad medida a medias**: el golden set del framework está en 34–35/35, pero no hay journeys
  multi-turno de comercio ni golden set de cobranza.

## Por qué importa (valor empresarial)

La promesa de SolversHub frente a la matriz es **"IA confiable"**: que el asistente nunca invente un
monto ni afirme una acción que no ocurrió. Esta spec la convierte en mecanismo: el modelo vigente, el
costo de Meta bajo control, errores que no apagan habilidades, acciones terminales con precondiciones
y calidad medida en conversaciones completas.

## Alcance

| HU | Qué | Hito |
|---|---|---|
| [HU-ARCH-10](hu/HU-ARCH-10-modelos-deepseek-vigentes.md) ★ | Modelos DeepSeek vigentes y verificados | 0A |
| [HU-ARCH-11](hu/HU-ARCH-11-un-mensaje-por-defecto.md) ★ | `un_mensaje` por defecto y estilo editable | 0A |
| [HU-ARCH-12](hu/HU-ARCH-12-precondiciones-y-escalate.md) ★ | Precondiciones terminales, señal `escalate` y scopes | 0B |
| [HU-ARCH-13](hu/HU-ARCH-13-plantillas-fuera-de-24h.md) ★ | Plantillas de WhatsApp fuera de 24 h | 0A |
| [HU-ARCH-14](hu/HU-ARCH-14-playground-sandbox.md) | Playground con sandbox de tools | 0B |
| [HU-ARCH-15](hu/HU-ARCH-15-cache-anthropic.md) | Caché de Anthropic con ≤4 breakpoints | 0B |
| [HU-ARCH-16](hu/HU-ARCH-16-golden-set-comercio.md) ★ | Golden set y journeys de comercio | 0B |
| [HU-ARCH-17](hu/HU-ARCH-17-golden-set-cobranza.md) ★ | Golden set de cobranza | 0B |
| [HU-ARCH-18](hu/HU-ARCH-18-errores-de-negocio-no-apagan-packs.md) ★ | Errores de negocio ≠ fallas del pack | 0A |
| [HU-ARCH-28](hu/HU-ARCH-28-evals-de-consistencia-pass-k.md) ★ | Evals de consistencia: usuario simulado, aserciones de estado y pass^k | 0A |
| [HU-ARCH-29](hu/HU-ARCH-29-verificador-de-afirmaciones.md) | Verificador de afirmaciones con modelo de evidencia | 0A |

## Decisiones

- Modelo por defecto (✅ tomada: D-22, `deepseek-flash` con respaldo `gpt-4o-mini`): ver [P-05](../../02-vision-y-decisiones/preguntas-abiertas.md#p-05--modelo-por-defecto-con-la-llave-de-plataforma).

### D-SPEC-02-1 · Cómo distinguir error de negocio de falla de infraestructura

| Opción | Pros | Contras |
|---|---|---|
| **A. Jerarquía de excepciones en el core (`BusinessError` con subclases `PaymentCapabilityError`, `SubscriptionError`, `ValidationError`); el host las convierte en resultado controlado de la tool; solo el resto cuenta para el auto-deshabilitado** | Explícito, auditable, un solo lugar | Hay que auditar las tools de todos los packs |
| B. Cada tool atrapa sus errores | Sin cambios en el core | Depende de la disciplina de cada pack; ya falló |
| C. Umbral: deshabilitar solo tras N fallas seguidas | Tolera errores aislados | Sigue apagando packs por errores de negocio repetidos |

**Recomendación: A** (enmienda ADR-0024). Estado: ✅ tomada (2026-10-02): jerarquía `BusinessError` en el core.

### D-SPEC-02-2 · Mapeo evento → plantilla

| Opción | Pros | Contras |
|---|---|---|
| **A. Config por negocio: clave de evento (`subscription.charge_created`, `appointment.reminder`…) → plantilla aprobada + variables; texto de respaldo dentro de la ventana** | Cada negocio usa sus plantillas; sin código | Hay que crear y aprobar plantillas por negocio |
| B. Plantillas fijas de plataforma | Simple | Meta las aprueba por WABA: no sirven entre negocios |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): config por negocio (evento → plantilla + variables).

### D-SPEC-02-3 · Sandbox del playground

| Opción | Pros | Contras |
|---|---|---|
| **A. Las tools con efectos declaran `side_effects=True`; en el canal `test` el host las ejecuta en modo simulado y devuelve un resultado ficticio marcado** | El asistente se prueba de punta a punta sin efectos | Cada pack declara sus tools |
| B. Base de datos de prueba por negocio | Realismo total | Costoso y lento |

**Recomendación: A.** Estado: ✅ tomada (2026-10-03): `side_effects=True` + canal `test` simulado.

### D-SPEC-02-4 · Cómo se mide la calidad del asistente

| Opción | Pros | Contras |
|---|---|---|
| **A. pass^k (k intentos por escenario) con usuario simulado y aserciones sobre el estado final, además del pass@1 actual** | Mide consistencia y resultado; atribuye la inestabilidad | Más cómputo en el nightly |
| B. Solo pass@1 del golden (hoy) | Barato | Un error que aparece 1 de cada 4 veces no se ve |

**Recomendación: A** (D-28, ADR-0119). Estado: ✅ tomada (2026-10-08): pass^4 se reporta en el 0A y el umbral vigente (≥95 % tres noches) no cambia.

### D-SPEC-02-5 · Cómo se verifica lo que dice el asistente

| Opción | Pros | Contras |
|---|---|---|
| **A. Un verificador determinista con modelo de evidencia común (acciones del turno y de turnos anteriores) que reemplaza los guardrails heurísticos tras medir falsos positivos** | Menos escalamientos falsos; reproducible | Parsers por tipo de afirmación |
| B. Seguir con `crm_amount_check`, `crm_completion_check` y `calendar_completion_check` | Ya existen | Escalan compras válidas |

**Recomendación: A** (D-28, ADR-0119). Estado: ✅ tomada (2026-10-08).

## Fuera de alcance

Tool siguiente forzada en el core ([HU-ARCH-26](../../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md), Fase 2), guardrails de runtime completos con límites
por ventana ([HU-ARCH-20](../../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-20-guardrails-runtime.md)).

## Métricas de éxito

- Golden sets ≥95 % durante 3 noches seguidas en comercio, cobranza y asistente SolversHub.
- 0 habilidades auto-deshabilitadas por errores de negocio.
- Mensajes de Meta por conversación ≈ turnos (no 3× turnos).
- 0 recordatorios `failed` por ventana vencida.
- pass^4 reportado cada noche para el framework y `solvershub`; falsos positivos del verificador ≤ 2 % y 0 escalamientos a mitad de compra en los journeys.

## Requerimientos cubiertos

REQ-ARCH-07, REQ-ARCH-10, REQ-ARCH-14, REQ-ARCH-15, REQ-ARCH-18, REQ-ARCH-20, REQ-ARCH-21, REQ-FIX-08,
REQ-FWK-07, REQ-COMP-03, REQ-PLUS-01.
