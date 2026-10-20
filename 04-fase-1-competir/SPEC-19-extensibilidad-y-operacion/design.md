# SPEC-19 · Diseño

- **MCP por tenant**: registro de servidores MCP por negocio con allowlist de herramientas, scopes,
  circuit breaker por servidor, timeouts y presupuesto; nunca credenciales en el AgentSpec; todo
  resultado externo es dato (invariante 7).
- **Guardrails**: bindings fail-closed (sin binding no hay tool), límites por ventana de tiempo por
  tool y por conversación, presupuesto por conversación ya existente.
- **Status page**: pública, alimentada por los checks de [HU-ARCH-07](../../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md); SLO de disponibilidad del
  webhook y del panel con su presupuesto de error.
- **Pentest**: externo, con alcance panel, API, webhooks, APK y aislamiento multi-tenant; cuestionario
  de seguridad estándar respondido y publicado bajo pedido.
- **Brand**: `solvershub-brand` publica `@solvershub/tokens` como paquete versionado que consumen
  panel, APK y landing.
