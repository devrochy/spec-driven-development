# SPEC-18 · Diseño

- **Proactividad**: jobs por negocio sobre eventos `order.*` del outbox: expirar pedidos online impagos
  a los N días liberando stock; recordar transferencias pendientes; reenganchar cotizaciones frías con
  plantilla; encuesta de satisfacción 1–5 tras la entrega (con enlace a reseña si es ≥4).
- **Promociones v2**: franjas de día y hora, monto fijo, subtotal mínimo, domicilio gratis, cupones con
  límite de uso por cliente y total, ítem gratis como línea de $0; "no se acumulan" como regla
  explícita por defecto.
- **KPIs**: ventas, ticket promedio, conversión cotización → pedido, top productos y clientes, contra el
  período anterior; reporte diario o semanal al equipo por su canal preferido.
- **Búsqueda**: `unaccent` + trigram, ruta de categoría, sinónimos por negocio; recomendaciones
  "comprados juntos" desde `order_items`.
- **Modificadores**: grupos de opciones por producto (tamaño, adicionales) con precio, mínimo y máximo.
