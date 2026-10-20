# Fase 2 · Plus (P2)

**Objetivo**: abrir los canales y segmentos siguientes: agencias con sub-cuentas, cobro internacional,
extensibilidad para clientes grandes sin fork, voz y la evidencia de confianza enterprise (ISO 27001).

| HU | Días-persona sin IA | Rango de fin |
|---:|---:|---|
| 15 | 93,5 | 2027-08-19 – 2028-02-20 |

## Criterio de salida

2 casos de estudio publicados. Al menos 3 integraciones MCP verificadas. Agencia y cobro en USD
solo si [SPEC-21](SPEC-21-agencia-e-internacional/spec.md) se retoma (parqueada, D-35).

## Specs de la fase

| Spec | Tema | HU |
|---|---|---:|
| [SPEC-21](SPEC-21-agencia-e-internacional/spec.md) | Agencia, sub-cuentas e internacional — **parqueada** (D-35) | 5 |
| [SPEC-22](SPEC-22-extensibilidad-avanzada/spec.md) | Extensibilidad avanzada | 6 |
| [SPEC-23](SPEC-23-voz-reportes-y-confianza/spec.md) | Voz, reportes, prueba social e ISO 27001 | 4 |

<!-- GENERADO:inicio -->
## HU de la fase (17)

| HU | Título | Est. | Depende de | Impacto |
|---|---|---|---|---|
| [HU-ARCH-25](SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-25-toolcontext-y-embeddings.md) | ToolContext según el contrato y embeddings por negocio | L | [HU-REP-03](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-03-transicion-de-identificadores.md) | ⚙️ 🤖 |
| [HU-ARCH-26](SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md) | Tool siguiente forzada y turnos silenciosos en el core | L | [HU-ARCH-20](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-20-guardrails-runtime.md) | 🤖 🛡️ |
| [HU-COM-16](SPEC-22-extensibilidad-avanzada/hu/HU-COM-16-multisucursal.md) | Varias sucursales en comercio | L | [HU-COM-08](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-08-domicilios.md), [HU-COM-15](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-15-modificadores-y-combos.md) | 💰 🏆 |
| [HU-FLOW-07](SPEC-22-extensibilidad-avanzada/hu/HU-FLOW-07-purpose-y-reglas-por-etapa.md) | Edición avanzada del purpose y reglas por etapa | M | [HU-FLOW-05](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-05-borrador-y-publicacion.md) | 🏆 🤖 |
| [HU-FWK-13](SPEC-22-extensibilidad-avanzada/hu/HU-FWK-13-plugin-del-tenant.md) | Plugin del tenant formalizado con scaffold completo | L | [HU-FWK-04](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md) | 🏆 |
| [HU-FWK-14](SPEC-22-extensibilidad-avanzada/hu/HU-FWK-14-integraciones-mcp.md) | Integraciones MCP de catálogo | L | [HU-ARCH-19](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md) | 💰 🏆 |
| [HU-GTM-13](SPEC-23-voz-reportes-y-confianza/hu/HU-GTM-13-prueba-social.md) | Prueba social real en la landing | S | [HU-GTM-08](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-08-activos-de-venta.md) | 💰 🛡️ |
| [HU-GTM-14](SPEC-23-voz-reportes-y-confianza/hu/HU-GTM-14-camino-iso-27001.md) | Camino a ISO 27001 | L | [HU-ARCH-22](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-22-pentest.md) | 🛡️ ⚖️ |
| [HU-MEDIA-08](SPEC-23-voz-reportes-y-confianza/hu/HU-MEDIA-08-voz-en-llamadas.md) | Voz en llamadas con ADR y spike | M | [HU-MEDIA-03](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md) | 🏆 |
| [HU-UX-07](SPEC-23-voz-reportes-y-confianza/hu/HU-UX-07-reporte-mensual.md) | Reporte mensual automático por negocio | M | [HU-UI-07](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md), HU-BILL-07 | 💰 🏆 |
| [HU-AOS-39](SPEC-27-agent-os-plus/hu/HU-AOS-39-federacion-entre-negocios.md) | Federación entre negocios con consentimiento | L | [HU-AOS-18](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-37](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-37-cuotas-y-planes.md) | 🏆 💰 |
| [HU-AOS-40](SPEC-27-agent-os-plus/hu/HU-AOS-40-sandbox-de-acciones.md) | Sandbox aislado para acciones no confiables | L | [HU-AOS-34](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-34-acciones-v2.md), [HU-ARCH-19](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md) | 🛡️ 🏆 |
| [HU-AOS-41](SPEC-27-agent-os-plus/hu/HU-AOS-41-auto-mejora-asistida.md) | Auto-mejora asistida: de fallas a versión candidata | L | [HU-AOS-32](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-32-canary-y-auto-rollback.md), [HU-AOS-33](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-33-feedback-y-propuestas.md) | 🤖 ⚙️ |
| [HU-AOS-42](SPEC-27-agent-os-plus/hu/HU-AOS-42-canal-api-y-webhooks.md) | Canal API y webhooks salientes como conexión | M | [HU-AOS-11](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-11-conexion-canonica.md) | 🏆 💰 |
| [HU-AOS-43](SPEC-27-agent-os-plus/hu/HU-AOS-43-slack-y-correo-entrante.md) | Slack y correo entrante como conexiones | L | [HU-AOS-42](SPEC-27-agent-os-plus/hu/HU-AOS-42-canal-api-y-webhooks.md) | 🏆 |
| [HU-AOS-44](SPEC-27-agent-os-plus/hu/HU-AOS-44-topologia-por-roles.md) | Topología por roles y escalado del runtime | M | [HU-AOS-29](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md) | ⚙️ |
| [HU-AOS-45](SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md) | Editor de estructura de superpoderes para el negocio | L | [HU-AOS-25](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md) | 🏆 |

### HU parqueadas (5)

Fuera del calendario y del total de arriba (D-35); se retoman por decisión.

| HU | Título | Est. | Depende de | Impacto |
|---|---|---|---|---|
| [HU-BILL-13](SPEC-21-agencia-e-internacional/hu/HU-BILL-13-cobro-internacional.md) | Cobro internacional en USD | L | [HU-BILL-12](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-12-cambio-de-plan-y-anual.md) | 💰 |
| [HU-BILL-14](SPEC-21-agencia-e-internacional/hu/HU-BILL-14-billing-de-agencia.md) | Billing de agencia con reventa y factura consolidada | L | [HU-FWK-12](SPEC-21-agencia-e-internacional/hu/HU-FWK-12-organizaciones-y-subcuentas.md), [HU-BILL-10](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-10-recargas.md) | 💰 |
| [HU-FWK-12](SPEC-21-agencia-e-internacional/hu/HU-FWK-12-organizaciones-y-subcuentas.md) | Organizaciones y sub-cuentas para agencias | M | — | 💰 🏆 |
| [HU-GTM-12](SPEC-21-agencia-e-internacional/hu/HU-GTM-12-oferta-de-agencia.md) | Oferta de agencia y white-label | M | [HU-BILL-14](SPEC-21-agencia-e-internacional/hu/HU-BILL-14-billing-de-agencia.md) | 💰 🏆 |
| [HU-SUB-17](SPEC-21-agencia-e-internacional/hu/HU-SUB-17-debito-recurrente.md) | Débito recurrente automático en el contrato de suscripción | L | HU-SUB-15 | 💰 |
<!-- GENERADO:fin -->
