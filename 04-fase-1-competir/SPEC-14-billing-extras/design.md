# SPEC-14 · Diseño

- **Avisos**: `usage_alerts` dispara una notificación al owner por WhatsApp (plantilla) y correo al
  80 %, 100 % y al entrar al colchón, una vez por umbral y período.
- **Recargas**: tabla `credit_topups` (tenant, créditos, precio, estado, vence); el saldo del período =
  cupo del plan + recargas vigentes − consumo; las recargas se consumen después del cupo del plan.
  Cobro por `core/billing` con Wompi.
- **Cierres de período**: snapshot materializado por tenant y período (cupo, recargas, consumo,
  saldo) para reportes rápidos; la fuente sigue siendo el ledger.
- **Margen master**: por tenant, plan y modelo: ingreso del período, costo de proveedores, créditos
  vendidos, margen; alertas por margen negativo.
- **Cambio de plan**: upgrade inmediato con prorrateo por días; downgrade al próximo período; anual
  con 2 meses gratis (`interval_days = 365`).
