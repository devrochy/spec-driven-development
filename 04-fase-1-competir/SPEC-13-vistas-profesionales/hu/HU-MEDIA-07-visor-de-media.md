---
id: HU-MEDIA-07
titulo: Visor de media y transcripciones en la bandeja
spec: SPEC-13
fase: 1
hito: "1"
workstream: Multimodalidad
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, calidad_ia]
req: [REQ-MEDIA-07, REQ-UX-04]
dependencias: [HU-UI-06, HU-MEDIA-03, HU-MEDIA-04]
skills: ["frontend-design", "backend-design:security-discipline"]
estado: parqueada
---

# HU-MEDIA-07 · Visor de media y transcripciones en la bandeja

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md).

**ID:** HU-MEDIA-07

**Título:** Visor de media y transcripciones en la bandeja

**Workstream:** Multimodalidad

**Historia:** Como operador quiero escuchar las notas de voz, ver las fotos y leer lo que el sistema entendió de cada una dentro de la conversación para atender una escalación sin pedirle al cliente que repita.

**Por qué importa (valor empresarial):** Cuando el asistente escala, el humano necesita el contexto completo. Ver la transcripción junto al audio también permite auditar la calidad del STT y del OCR.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-MEDIA-07, REQ-UX-04

**Dependencias:** [HU-UI-06](HU-UI-06-bandeja-dos-paneles.md), [HU-MEDIA-03](../../../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md), [HU-MEDIA-04](../../../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md)

**Criterios de aceptación (Gherkin):**
- **Audio.** Dado una nota de voz, cuando la veo en el hilo, entonces puedo reproducirla y leer su transcripción.
- **Imagen.** Dado una foto o comprobante, cuando la veo, entonces se abre en grande con lo que leyó el OCR.
- **Permisos y retención.** Dado un colaborador sin permiso, cuando abre la conversación, entonces no ve la media; dado media vencida, entonces se indica que ya no está disponible.

**Evidencia / Definición de Terminado:**
- Endpoint de media con URL firmada y vencimiento; componente en el hilo.

**Riesgos/Notas:**
- Paridad de procesamiento en WhatsApp Web ya cubierta en [HU-MEDIA-02](../../../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md).
