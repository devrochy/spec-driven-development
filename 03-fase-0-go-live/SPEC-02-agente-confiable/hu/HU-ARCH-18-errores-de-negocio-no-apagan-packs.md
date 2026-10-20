---
id: HU-ARCH-18
titulo: Un error de negocio nunca apaga una habilidad
spec: SPEC-02
fase: 0
hito: 0A
workstream: Framework/Plugins
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, calidad_ia]
req: [REQ-FWK-07, REQ-PLUS-01]
dependencias: []
skills: ["adr", "backend-design:error-handling-as-design", "arquitecto", "/codex:adversarial-review"]
ola: 1
estado: terminada
---

# HU-ARCH-18 · Un error de negocio nunca apaga una habilidad

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-02](../spec.md) (D-SPEC-02-1).

**ID:** HU-ARCH-18

**Título:** Un error de negocio nunca apaga una habilidad

**Workstream:** Framework/Plugins

**Historia:** Como dueño de un negocio quiero que un monto inválido, un cliente inexistente o una plantilla mal editada se respondan como un resultado controlado para que mis suscripciones, mi comercio o mi cobranza no se apaguen por un caso puntual.

**Por qué importa (valor empresarial):** Hoy cualquier excepción de una tool deshabilita el pack completo para el negocio (`core/orchestrator/loop.py:670-675`). Un plan barato bajo el mínimo de Wompi apaga las suscripciones; una plantilla con una variable mal escrita apaga el comercio. Es un riesgo de caída silenciosa del negocio del cliente.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-FWK-07, REQ-PLUS-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Error de negocio.** Dado `sub_link_pago` con un monto bajo el mínimo del proveedor, cuando se ejecuta, entonces la tool devuelve `{"status": "monto_bajo_minimo"}`, el asistente ofrece una alternativa y el pack sigue habilitado.
- **Falla de infraestructura.** Dado una tool que no puede conectar con su base o su proveedor, cuando falla, entonces se aplica el auto-deshabilitado como hoy (ADR-0024).
- **Auditoría de packs.** Dado todas las tools de commerce, payments, subscriptions, cobranza y calendar, cuando se revisan, entonces cada error de negocio conocido lanza una subclase de `BusinessError`; queda una tabla en el PR.
- **Plantilla mal editada.** Dado una plantilla de mensaje del negocio con una variable inexistente, cuando se usa, entonces se envía el texto por defecto y se avisa al negocio, sin deshabilitar el pack.

**Evidencia / Definición de Terminado:**
- Enmienda a ADR-0024 aceptada.
- Tests de los cuatro escenarios; `cob_link_suscripcion` y `sub_link_pago` corregidos (defecto 12).

**Implementada (2026-10-02, PR #194 en `devrochy/agent-core`):**
- `BusinessError` con subclases (`ValidationError`, `PaymentCapabilityError`, `SubscriptionError`). Acepta `code` y `escalate`.
- `host.execute_tool` convierte `BusinessError` en resultado controlado; el loop también (tools declarativas). El pack sigue habilitado.
- Falla real (no `BusinessError`) sigue disparando `auto_disable_for_tenant` (ADR-0024 intacto).
- `PaymentCapabilityError` hereda de `BusinessError`; `sub_link_pago` y `crear_link_para_cuota` devuelven `status: monto_bajo_minimo`.
- `_safe_format`: plantilla inválida cae al texto por defecto (no apaga comercio).
- **ADR-0088** (enmienda ADR-0024); 9 tests nuevos; suite 699 passed.

**Riesgos/Notas:**
- Cubre los defectos D8 de comercio y 12 de suscripciones.

**Auditoría de errores de negocio por pack (2026-10-02):**
| Pack | Errores de negocio migrados | Pendiente |
|---|---|---|
| payments | `PaymentRequestRejected` (Wompi) + `PaymentCapabilityError` | — |
| subscriptions | `sub_link_pago` → `monto_bajo_minimo` | tools `sub_*` de datos inválidos |
| cobranza | `crear_link_para_cuota` → `monto_bajo_minimo` | `cob_*` ya devuelven `{"error": ...}` |
| commerce | devuelve `{"error": ...}` en las tools; plantilla → `_safe_format` | migrar a `ValidationError` en HU futuras |
| calendar | devuelve `{"error": ...}`; OAuth usa `PluginError` (falla real) | — |
