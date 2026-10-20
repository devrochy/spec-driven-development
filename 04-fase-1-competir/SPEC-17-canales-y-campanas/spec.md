# SPEC-17 · Canales y campañas

> Estado SDD: Diseño aprobado · Fase 1 · Workstream Canales y conexiones

## Problema

Solo hay salida por WhatsApp (Meta y Web) y correo. Instagram y Messenger tienen entrada pero no
salida (el código vive en ramas sin mergear), no hay chat web, y las plantillas se gestionan pero no
existe un módulo de campañas con segmentos y consentimiento.

## Por qué importa (valor empresarial)

Respond.io, SleekFlow y Lety atienden por Instagram, Messenger y web; Interakt, Wati y ClonAI venden
campañas. Sin estos canales, SolversHub queda fuera de negocios cuyo cliente llega por Instagram
(moda, belleza) y no puede recuperar ventas con mensajes salientes.

## Alcance

| HU | Qué |
|---|---|
| [HU-CHAN-01](hu/HU-CHAN-01-instagram-y-messenger.md) | Instagram y Messenger con salida |
| [HU-CHAN-02](hu/HU-CHAN-02-chat-web.md) | Chat web embebible |
| [HU-CHAN-03](hu/HU-CHAN-03-pack-marketing.md) | Pack de marketing: campañas, segmentos y consentimiento |

## Decisiones

### D-SPEC-17-1 · Campañas como pack o como core

| Opción | Pros | Contras |
|---|---|---|
| **A. Pack `pack-marketing` que usa el envío de plantillas del core** | Se activa por plan; no infla el core | Necesita segmentos de otros packs vía registros del core |
| B. Campañas en el core | Disponible para todos | El core crece con lógica comercial |

**Recomendación: A.** Estado: ⏳ pendiente.

## Requerimientos cubiertos

REQ-FIX-01, REQ-FIX-02, REQ-COMP-01, REQ-COMP-03.
