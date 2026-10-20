# SPEC-27 · Diseño

Se apoya en el diseño de [SPEC-26](../../04-fase-1-competir/SPEC-26-agent-os/design.md). Las secciones citadas son de ese documento.

## Componentes y flujo

| HU | Componente | Base en [SPEC-26](../../04-fase-1-competir/SPEC-26-agent-os/spec.md) |
|---|---|---|
| [HU-AOS-39](hu/HU-AOS-39-federacion-entre-negocios.md) | `a2a_federation_grants` + funciones `federation_propose/approve/revoke` (SECURITY DEFINER) + gateway de federación que llama al agente del proveedor en **su** `tenant_scope` y devuelve solo el resultado tipado | DDL §4.3-14, D-AOS-13 |
| [HU-AOS-40](hu/HU-AOS-40-sandbox-de-acciones.md) | Ejecutor aislado (nivel T4): contenedor efímero, egress por allowlist, límites de CPU, memoria y tiempo; secretos solo los declarados | §7.7 (niveles T0–T4) |
| [HU-AOS-41](hu/HU-AOS-41-auto-mejora-asistida.md) | Análisis semanal de fallas → propuestas de frases y textos → pass^k → aprobación → canary | §7.9 |
| [HU-AOS-42](hu/HU-AOS-42-canal-api-y-webhooks.md) | Tipo de conexión `api` con clave e idempotencia; webhooks salientes firmados (HMAC) por evento | §3.4, §5.3 |
| [HU-AOS-43](hu/HU-AOS-43-slack-y-correo-entrante.md) | Adaptadores de correo entrante y Slack que producen `InboundMessage` | §3.5 |
| [HU-AOS-44](hu/HU-AOS-44-topologia-por-roles.md) | Partición de ADR-0021: `panel` y `gateway+consumer` del mismo binario (`AGENT_CORE_ROLE`); el Coordinador corre con el consumer | §3.4, D-AOS-15 |
| [HU-AOS-45](hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md) | Editor de estructura de superpoderes con el linter de `procedure/1`; procedimientos propios del negocio versionados | §3.6, §5.2 |

## Datos

- Federación: `a2a_federation_grants` (DDL en [SPEC-26](../../04-fase-1-competir/SPEC-26-agent-os/spec.md) §4.3-14). `purge_tenant` se extiende para borrar donde `consumer_tenant_id` es el negocio purgado.
- Procedimientos propios del negocio ([HU-AOS-45](hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md)): tabla con scope de negocio y versiones inmutables, igual que `agent_versions`.

## API

Conexión `api`: `POST /api/v1/channels/api/{connection_key}/messages` con firma y clave de idempotencia. Suscripciones de webhooks salientes por conexión.

## UI

Plataforma → Federaciones (solo master) y Superpoderes → "Editar estructura" para implementadores.

## ADR a crear o enmendar

- ADR de federación entre negocios (enmienda ADR-0116).
- ADR del ejecutor aislado (enmienda ADR-0005 y ADR-0052).

## Migración, despliegue y reversa

Todo detrás de banderas apagadas por defecto; la federación nace desactivada.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Fuga de datos entre negocios en la federación | Solo resultados tipados, doble consentimiento, revocación inmediata, `auditor-multitenant` |
| Costo operativo del sandbox | Solo para acciones que lo declaran |
