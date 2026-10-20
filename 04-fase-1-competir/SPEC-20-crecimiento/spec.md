# SPEC-20 · Crecimiento comercial

> Estado SDD: Diseño aprobado · Fase 1 · Workstream GTM

## Problema

La estrategia de redes está al 0 %, no hay deck ni casos, los leads no tienen SLA medido, la landing
no tiene páginas de integraciones ni de casos de uso (sitemap de 6 URL), la matriz competitiva tiene
errores (ChatBotCorp, sin Wolkvox, columna SolversHub exagerada) y los negocios que venden
suscripciones no tienen métricas de MRR ni churn.

## Por qué importa (valor empresarial)

Después del go-live el cuello de botella pasa a ser la demanda. Estos activos convierten el producto
en un negocio que crece: contenido, prueba, SEO por vertical y, para los clientes con suscripciones,
las métricas que justifican pagar más.

## Alcance

| HU | Qué |
|---|---|
| [HU-GTM-07](hu/HU-GTM-07-redes-activas.md) | Redes activas |
| [HU-GTM-08](hu/HU-GTM-08-activos-de-venta.md) | Activos de venta |
| [HU-GTM-09](hu/HU-GTM-09-leads-con-sla.md) | Leads con SLA < 5 min |
| [HU-GTM-10](hu/HU-GTM-10-paginas-de-integraciones-y-seo.md) | Páginas de integraciones, casos de uso y SEO |
| [HU-GTM-11](hu/HU-GTM-11-matriz-corregida.md) | Matriz competitiva corregida |
| [HU-SUB-16](hu/HU-SUB-16-mrr-y-embudo.md) | MRR y embudo para negocios con suscripciones |

## Decisiones

### D-SPEC-20-1 · Canal principal de demanda

| Opción | Pros | Contras |
|---|---|---|
| **A. Contenido orgánico (LinkedIn B2B + Instagram pymes) con casos reales, apoyado por SEO vertical** | Bajo costo; construye marca; reutiliza los casos del Hito 0B | Tarda meses en rendir |
| B. Pauta pagada (Click-to-WhatsApp) | Resultados inmediatos; 72 h de mensajes gratis con Meta | Costo por lead; requiere presupuesto |
| C. Alianzas con agencias desde ya | Escala | Choca con D-01 (agencia después) |

**Recomendación: A**, con B en pruebas pequeñas medidas con la atribución de [HU-SH-09](../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-09-landing-con-atribucion.md). Estado: ⏳ pendiente.

## Requerimientos cubiertos

REQ-GTM-03, REQ-GTM-04, REQ-GTM-05, REQ-GTM-10, REQ-COMP-04, REQ-FIX-05, REQ-SUB-05.
