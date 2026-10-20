---
id: HU-CONN-02
titulo: Errores 500 y bloqueos de Conexiones
spec: SPEC-08
fase: 0
hito: 0A
workstream: Canales y conexiones
prioridad: P0
critico: true
estimacion: S
impacto: [confianza]
req: [REQ-CONN-02]
dependencias: []
skills: ["backend-design:debugging-discipline", "backend-design:incident-investigator", "backend-design:testing-with-discernment"]
ola: 1
estado: terminada
---

# HU-CONN-02 · Errores 500 y bloqueos de Conexiones

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-08](../spec.md).

**ID:** HU-CONN-02

**Título:** Errores 500 y bloqueos de Conexiones

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero que las páginas de Números y de créditos de Meta carguen, que el wizard se pueda reiniciar y que el alta manual no se rompa para no quedar bloqueado en la configuración de mi canal.

**Por qué importa (valor empresarial):** Un error 500 en la configuración del canal núcleo es la peor primera impresión y genera tickets de soporte que una persona sola no puede atender. Son arreglos pequeños con impacto inmediato.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-CONN-02

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Números.** Dado una conexión con número, cuando abro Números, entonces carga (sin `PhoneNumber.status`, `meta_numbers_service.py:91`) y hay un test del endpoint.
- **Créditos.** Dado la lista de créditos de Meta, cuando se consulta, entonces responde (sin `MetaConnection.label`, `costs.py:200`) y el panel muestra el error real si lo hay.
- **Wizard tras 24 h.** Dado un wizard de ES vencido, cuando lo reinicio, entonces se reutiliza el borrador en vez de violar el índice único.
- **Alta manual.** Dado un alta manual con una conexión o número ya existente, cuando guardo, entonces recibo un mensaje claro (no un error de integridad) y, si es nueva, la WABA queda suscrita a la app.
- **Sin efectos en GET.** Dado las páginas de Números, Plantillas y Requisitos, cuando se abren, entonces no escriben en la base; la sincronización es un botón explícito.

**Evidencia / Definición de Terminado:**
- Tests de regresión de los cinco casos.

**Implementada (2026-10-02, PR #185 en `devrochy/agent-core`):**
- N-18a: `list_numbers` usaba `PhoneNumber.status` (columna inexistente) → 500. Se deriva de `code_verification_status`/`registered`/`name_status`.
- N-18b: `_credit_connections` usaba `MetaConnection.label` (inexistente) → 500. Se usa `meta_app_id`/`business_id`.
- Wizard vencido: `start_or_resume_wizard` creaba otra `MetaConnection` draft y violaba `uq_meta_connections_tenant_app`; ahora reutiliza cualquier conexión viva.
- 4 tests de integración de regresión; gate de CI verde.

**Riesgos/Notas:**
- Defectos nuevos de la auditoría del 2026-10-01.
