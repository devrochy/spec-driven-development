# SPEC-14 · Billing: avisos, recargas, margen y cambio de plan

> Estado SDD: Parqueada (2026-10-17, D-35) salvo [HU-BILL-12](hu/HU-BILL-12-cambio-de-plan-y-anual.md) · Fase 1 · Workstream Billing

**Parqueada (2026-10-17, [D-35](../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes)):** avisos de consumo, recargas y margen master esperan a que los planes por agentes (HU-BILL-05) estén en producción con clientes de pago. [HU-BILL-12](hu/HU-BILL-12-cambio-de-plan-y-anual.md) (cambio de plan con prorrateo y ciclo anual) sigue en `borrador` y se ejecuta con HU-BILL-05, que la referencia.

## Problema

El núcleo de créditos (SPEC-03) bloquea y avisa en el panel, pero falta lo que convierte un bloqueo en
ingreso: avisos fuera del panel, recargas, visión de margen para la plataforma y cambio de plan con
prorrateo y ciclos anuales.

## Por qué importa (valor empresarial)

Las recargas son ingreso incremental sin costo de venta; el plan anual adelanta caja y baja el churn;
la vista de margen evita que un cliente o un modelo caro destruyan la rentabilidad sin que nadie lo
note. Wati vende créditos Astra con exactamente esta lógica.

## Alcance

| HU | Qué |
|---|---|
| [HU-BILL-09](hu/HU-BILL-09-avisos-de-consumo.md) | Avisos de consumo fuera del panel |
| [HU-BILL-10](hu/HU-BILL-10-recargas.md) | Recargas de créditos y cierres de período |
| [HU-BILL-11](hu/HU-BILL-11-margen-master.md) | Vista master de margen |
| [HU-BILL-12](hu/HU-BILL-12-cambio-de-plan-y-anual.md) | Cambio de plan con prorrateo y ciclos anuales |

## Decisiones

- Vigencia de recargas: [P-07](../../02-vision-y-decisiones/preguntas-abiertas.md#p-07--vigencia-de-las-recargas).

### D-SPEC-14-1 · Paquetes de recarga

| Opción | Pros | Contras |
|---|---|---|
| **A. 3 paquetes fijos (por ejemplo 10.000, 30.000 y 100.000 créditos) con descuento por volumen y monto ≥ mínimo de Wompi** | Simple de vender y de cobrar | Menos flexible |
| B. Monto libre | Flexible | Montos bajo el mínimo de Wompi |

**Recomendación: A.** Estado: ⏳ pendiente.

## Requerimientos cubiertos

REQ-BILL-08 a REQ-BILL-11.
