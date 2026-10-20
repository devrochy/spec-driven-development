# SPEC-23 · Voz, reportes, prueba social e ISO 27001

> Estado SDD: En revisión · Fase 2 · Workstreams Multimodalidad, UX y GTM

## Problema

Voz en llamadas quedó fuera de v1 (D-03); no hay reporte mensual automático; la prueba social está
apagada; no hay camino a ISO 27001.

## Por qué importa (valor empresarial)

Darwin AI ofrece voz; Zendesk y SleekFlow venden reportes; todos exhiben prueba social; Hubtype usa
ISO 27001 como argumento enterprise. Son los diferenciales del siguiente nivel de mercado.

## Alcance

| HU | Qué |
|---|---|
| [HU-MEDIA-08](hu/HU-MEDIA-08-voz-en-llamadas.md) | Voz en llamadas (ADR y spike) |
| [HU-UX-07](hu/HU-UX-07-reporte-mensual.md) | Reporte mensual automático |
| [HU-GTM-13](hu/HU-GTM-13-prueba-social.md) | Prueba social real |
| [HU-GTM-14](hu/HU-GTM-14-camino-iso-27001.md) | Camino a ISO 27001 |

## Decisiones

### D-SPEC-23-1 · Voz en llamadas

| Opción | Pros | Contras |
|---|---|---|
| **A. Spike con un proveedor de voz en tiempo real y decisión por ADR con datos** | Decisión informada; costo acotado | Retrasa el lanzamiento de voz |
| B. IVR tradicional con STT | Barato y probado | Experiencia pobre frente a Darwin AI |
| C. No hacer voz | Foco en mensajería | Se cede el segmento de atención telefónica |

**Recomendación: A.** Estado: ⏳ pendiente.

## Requerimientos cubiertos

REQ-MEDIA-08, REQ-UX-08, REQ-COMP-05, REQ-COMP-06, REQ-PLUS-08.
