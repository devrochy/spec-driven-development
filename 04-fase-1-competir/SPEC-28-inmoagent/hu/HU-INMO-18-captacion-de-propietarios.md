---
id: HU-INMO-18
titulo: "Captación de inmuebles de propietarios"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, legal]
req: [REQ-INMO-05]
dependencias: [HU-INMO-04, HU-INMO-11, HU-INMO-12]
skills: ["new-tool", "turnstile-spin", "meta-whatsapp", "backend-design:security-discipline"]
estado: borrador
---

# HU-INMO-18 · Captación de inmuebles de propietarios

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-18

**Título:** Captación de inmuebles de propietarios

**Workstream:** Verticales

**Historia:** Como propietario quiero publicar mi inmueble por WhatsApp o desde un formulario compartiendo ubicación, datos y fotos, para que la inmobiliaria lo gestione sin papeleo.

**Por qué importa (valor empresarial):** El inventario es el activo de la inmobiliaria; captar más rápido que la competencia es ingreso directo.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-INMO-05

**Dependencias:** [HU-INMO-04](HU-INMO-04-avisos-abiertos-a-habilidades.md), [HU-INMO-11](HU-INMO-11-inventario-y-captaciones-en-el-panel.md), [HU-INMO-12](HU-INMO-12-geocodificacion-y-zonas.md)

**Criterios de aceptación (Gherkin):**
- **Por conversación.** Dado "quiero arrendar mi apartamento", cuando el propietario completa ubicación, datos, fotos y autorización y toca Confirmar, entonces la captación queda enviada y el asesor de la zona recibe el aviso en ≤ 1 min.
- **Sin autorización.** Dado que el propietario no acepta el tratamiento de datos, cuando intenta enviar, entonces la captación no se envía y se explica por qué.
- **Duplicado.** Dado un inmueble publicado a ≤ 30 m y del mismo tipo, cuando se envía la captación, entonces queda marcada como posible duplicado para el asesor.
- **Formulario.** Dado el formulario público con Turnstile, cuando llega una captación válida, entonces se crean el propietario y la captación con origen `formulario`.

**Evidencia / Definición de Terminado:**
- Acciones de captación con borrador idempotente por `(tenant_id, idempotency_key)`.
- Formulario en `/api/pack/pack_inmobiliario/captaciones/{slug}`: negocio solo desde el slug (`resolve_tenant_by_slug`), pack y formulario habilitados, Turnstile obligatorio y fail-closed validando hostname, límite por slug e IP, sin devolver datos existentes, cliente web sin fusionarlo con el de WhatsApp.
- Fotos bajo `tenants/<tenant_id>/captaciones/<id>/` con URL firmada; autorización de datos según P-29.

**Riesgos/Notas:**
- Fase INMO 3 · Captación y visitas.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
