# SPEC-21 · Diseño (borrador)

- `organizations` (sin RLS de negocio, con su propia política) y `tenants.organization_id`; roles de
  organización que heredan acceso a sus negocios.
- Billing de agencia: la organización paga un plan mayorista y cobra a sus negocios con su markup;
  factura consolidada.
- White-label: dominio y marca de la agencia en el panel y en los textos al cliente final.
- Internacional: segundo proveedor de cobro de plataforma (Stripe u otro) y precios en USD en el
  catálogo; impuestos por país.
- Débito automático: tarjeta tokenizada o débito recurrente como capacidad del contrato de
  suscripción (`auto_charge`).
