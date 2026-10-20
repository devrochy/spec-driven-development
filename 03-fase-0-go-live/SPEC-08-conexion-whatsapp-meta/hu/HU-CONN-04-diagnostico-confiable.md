---
id: HU-CONN-04
titulo: Diagnóstico confiable de la conexión
spec: SPEC-08
fase: 0
hito: 0A
workstream: Canales y conexiones
prioridad: P0
critico: true
estimacion: S
impacto: [confianza, operacion]
req: [REQ-CONN-02]
dependencias: [HU-CONN-01]
skills: ["backend-design:observability-by-default", "backend-design:testing-with-discernment", "meta-whatsapp"]
ola: 3
estado: terminada
---

# HU-CONN-04 · Diagnóstico confiable de la conexión

> Estado SDD: Terminada (2026-10-08) — desplegada y verificada en test (core `1fbef61`, panel `39c794c`).

**ID:** HU-CONN-04

**Título:** Diagnóstico confiable de la conexión

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero que "Diagnosticar" diga la verdad sobre mi conexión y me lleve a arreglar lo que falla para resolver problemas sin llamar a soporte.

**Por qué importa (valor empresarial):** Un verde falso es peor que un rojo: el negocio cree que todo funciona mientras sus clientes no reciben respuesta. El autodiagnóstico es lo que permite a una persona soportar a muchos clientes.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-CONN-02

**Dependencias:** [HU-CONN-01](HU-CONN-01-credenciales-por-conexion.md)

**Criterios de aceptación (Gherkin):**
- **Sin verde falso.** Dado una conexión sin token válido, cuando diagnostico, entonces el resultado es `error` con el motivo (no `connected`).
- **Salud fusionada.** Dado un diagnóstico manual o el cron horario, cuando guardan la salud, entonces se fusiona con lo existente y se conservan `coexistence` y `billing.manual_status`.
- **Reparación.** Dado un chequeo fallido con acción de reparación, cuando se muestra, entonces el enlace aparece y lleva al lugar correcto.
- **Solo chequeos.** Dado la vista de salud, cuando lista resultados, entonces no muestra como chequeos campos que no lo son.

**Evidencia / Definición de Terminado:**
- Tests de `decide_status` y de la fusión; corrección de `meta/page.tsx:180-185`.

**Implementada (2026-10-08, [agent-core #311](https://github.com/devrochy/agent-core/pull/311) + [panel #45](https://github.com/devrochy/solvershub-panel/pull/45)):**

| Criterio | Cómo quedó |
|---|---|
| Sin verde falso | Ya lo resolvía ADR-0102: una conexión solo mejora con el token verificado contra Meta, y una BYOK sin credenciales pasa a `error`. Test de integración nuevo: una conexión `connected` con el token rechazado por Meta pasa a `error`, con el motivo, y el check queda primero con `reauthorize`. |
| Salud fusionada | Ya estaba (`merge_health` en el diagnóstico manual y en el cron, con test que conserva `coexistence` y `billing.manual_status`). Arreglo: marcar la facturación guardaba solo `manual_status` y el check desaparecía hasta el próximo diagnóstico. |
| Reparación | Defecto de `meta/page.tsx:180-185`: el enlace se buscaba por la clave del check (`token_valid`) en un mapa de acciones (`reauthorize`) y nunca aparecía. Ahora sale de `repair_action` (`lib/meta-salud.ts`) y cubre las 6 acciones del backend; "Créditos" llevaba a `/costos`, que son los costos del LLM. |
| Solo chequeos | `GET /admin/meta/health` devuelve `checks` (solo objetos con `ok`, en orden de gravedad) y `billing_manual_status`. El panel ya no lista `coexistence`, `token_scope_check` ni `webhook_subscription_active`. |

Además, la vista de salud ya no lista conexiones eliminadas.

**Evidencia:** core 1150 unitarios + 502 de integración, `auditor-multitenant` sin hallazgos; panel 97 tests (5 nuevos), `tsc`, `eslint` y build. En test, la conexión de `solvershub` muestra los 8 checks con nombre legible y detalle, sin los datos del alta (verificado en el navegador). Las reparaciones de un check fallido quedan cubiertas por los tests del panel: en test todos los checks pasan.

**Riesgos/Notas:**
- [HU-CONN-01](HU-CONN-01-credenciales-por-conexion.md) sigue `en-curso` solo por Embedded Signup; el resolver que usa esta HU está verificado con BYOK real.
- Sin cambio a propósito: un token que vence en menos de 7 días da `token_valid` en falla y la conexión pasa a `error` (lo usa el cron de vencimiento). Si se prefiere `degraded`, va aparte.
- Defectos 2 y 3 de la auditoría.
