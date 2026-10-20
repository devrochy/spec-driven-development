# SPEC-22 · Diseño (borrador)

- **Plugin del tenant**: paquete instalable acotado a un negocio, con su propio namespace de tablas,
  revisión y despliegue por el master; scaffold con `models.py`, `jobs.py` y alembic.
- **MCP de catálogo**: servidores MCP verificados (CRM, e-commerce, hojas de cálculo) listos para
  conectar sobre [HU-ARCH-19](../../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md).
- **Flujo avanzado**: edición del `purpose` con permiso "implementador" y reglas por etapa (condiciones
  de entrada y salida), siempre con evals antes de publicar.
- **ToolContext**: ADR y bump major del contrato para agregar `tenantId`, `agentId`, `traceId`,
  `logger` y `emit`, con shim de compatibilidad.
- **Sucursales**: `branches` por negocio con menú, stock, horario y zonas propios; ruteo del pedido;
  alertas por sucursal.
