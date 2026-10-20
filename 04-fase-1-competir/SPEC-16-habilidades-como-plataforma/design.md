# SPEC-16 · Diseño

| Paso | Backend | Panel |
|---|---|---|
| Manifiesto | `GET /api/v1/admin/ui/manifest`: grupos e ítems filtrados por permisos y packs habilitados | Sidebar desde el manifiesto (grupos del core estáticos) |
| Descriptores | Tipos de celda (dinero con moneda, fecha, badge con etiqueta y tono, enlace, booleano), filtros, acciones por fila (tono, confirmación, endpoint, formulario), KPIs, estado vacío con acción | — |
| API de vistas | `GET /api/v1/pack/{id}/views/{vista}?q&filtros&page`, `POST …/actions/{accion}` | Ruta `app/(app)/p/[pack]/[vista]` con `<DescriptorView>` |
| Formulario | — | `anyOf` nulos, enums etiquetados, arreglos, objetos anidados, `x-widget`/`x-group`, errores por campo |
| Salida de emergencia | `kind: "custom"` | Las pantallas complejas siguen a mano |
| Contratos | Snapshots de descriptores | Test por tipo de celda y acción |

Pantallas candidatas: cobranza (alertas, auditoría, dispositivos, pagos, promesas, reportes,
monitoreo, carteras, clientes), comercio (categorías, pedidos, resumen), calendario (tipos, citas),
suscripciones (lista).
