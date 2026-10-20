# SPEC-21 · Agencia, sub-cuentas e internacional

> Estado SDD: Parqueada (2026-10-17, D-35) · Fase 2 · Workstreams Framework/Plugins y Billing

**Parqueada (2026-10-17, [D-35](../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes)):** agencia, sub-cuentas y cobro internacional no sirven a «SolversHub vende agentes» mientras no haya clientes directos de pago; D-01 ya la dejó para después. Se retoma con la primera agencia interesada (como P-15 con la federación).

## Problema

D-01 dejó el modelo de agencia para después, pero con el modelo de datos listo (REQ-PLUS-05b). Hoy
el `Tenant` es plano y solo existe "un admin con varios negocios" y el selector de negocio. El cobro
es solo en COP con Wompi y no hay débito automático.

## Por qué importa (valor empresarial)

Lety construyó su negocio sobre agencias que revenden (1.000+ agencias declaradas). Las sub-cuentas
con billing consolidado y markup convierten a cada agencia en un canal de ventas, y el cobro en USD
abre LATAM y el mercado hispano de EE. UU.

## Alcance

| HU | Qué |
|---|---|
| [HU-FWK-12](hu/HU-FWK-12-organizaciones-y-subcuentas.md) | ADR y modelo de organizaciones y sub-cuentas |
| [HU-BILL-13](hu/HU-BILL-13-cobro-internacional.md) | Cobro internacional en USD |
| [HU-BILL-14](hu/HU-BILL-14-billing-de-agencia.md) | Billing de agencia con reventa |
| [HU-SUB-17](hu/HU-SUB-17-debito-recurrente.md) | Débito recurrente automático |
| [HU-GTM-12](hu/HU-GTM-12-oferta-de-agencia.md) | Oferta de agencia y white-label |

## Decisiones

### D-SPEC-21-1 · Modelo de agencia

| Opción | Pros | Contras |
|---|---|---|
| **A. `Organization` padre con negocios hijos; permisos heredados; billing consolidado opcional** | Escala a agencias grandes; compatible con RLS por negocio | Cambios en auth y billing |
| B. Solo "admin con varios negocios" (hoy) | Sin cambios | Sin billing consolidado ni marca propia |

**Recomendación: A.** Estado: ⏳ pendiente.

## Requerimientos cubiertos

REQ-FWK-08, REQ-PLUS-05b, REQ-BILL-12, REQ-SUB-07, REQ-GTM-13.
