# SPEC-04 · Notas de voz y comprobantes

> Estado SDD: En revisión · Fase 0 · Hito 0B · Workstream Multimodalidad

## Problema

No existe procesador de media: un audio o una foto llegan como texto de reemplazo y la URL de la
media se guarda vacía (`core/gateway/webhooks.py`, `gateway/channels/whatsapp/inbound.py:67-73`). La
cuota de audio y OCR cuenta mensajes que nadie procesó, y WhatsApp Web ni siquiera pasa por la cuota.
`agent-sale` ya resolvió STT, visión y OCR de comprobantes con éxito (archivos en
`agent-sale/src/media/*`, `src/vision/*`, `src/payments/ocrComprobante.ts`), pero en un solo tenant y
con prompts en código.

## Por qué importa (valor empresarial)

En Colombia los clientes escriben con audios y pagan por transferencia mandando la foto del
comprobante. Un asistente que no entiende un audio ni un comprobante obliga a un humano a intervenir
justo en el momento de la venta o del cobro. ClonAI y Darwin AI ya lo anuncian; es paridad
obligatoria y, para cobranza, la única forma de cobrar montos bajo el mínimo de Wompi (SUB-13).

## Alcance

| HU | Qué | Hito |
|---|---|---|
| [HU-MEDIA-01](hu/HU-MEDIA-01-adr-media.md) ★ | ADR de procesamiento de media en el core | 0B |
| [HU-MEDIA-02](hu/HU-MEDIA-02-almacenamiento-media.md) ★ | Descarga y almacenamiento de media | 0B |
| [HU-MEDIA-03](hu/HU-MEDIA-03-stt-notas-de-voz.md) ★ | Notas de voz a texto | 0B |
| [HU-MEDIA-04](hu/HU-MEDIA-04-dispatcher-de-vision.md) ★ | Dispatcher de visión con prueba y benchmark | 0B |
| [HU-MEDIA-05](hu/HU-MEDIA-05-ocr-comprobantes.md) ★ | OCR de comprobantes en la ruta financiera | 0B |
| [HU-MEDIA-06](hu/HU-MEDIA-06-clasificacion-de-imagenes.md) | Clasificación comprobante/producto y descripción de producto | 0B |

## Decisiones

### D-SPEC-04-1 · Dónde se procesa

| Opción | Pros | Contras |
|---|---|---|
| **A. En el consumer del core, antes del turno, con idempotencia por mensaje y caché del resultado** | Todos los canales y packs se benefician; un solo lugar de costos | El turno espera la transcripción (segundos) |
| B. Como tool que el LLM decide llamar | Flexible | El LLM puede ignorar el audio; costos impredecibles |
| C. Pack de media aparte | Desacoplado | Los packs no pueden importarse; necesita evento de todos modos |

**Recomendación: A.** Estado: ⏳ pendiente.

### D-SPEC-04-2 · Dónde se guarda la media

| Opción | Pros | Contras |
|---|---|---|
| **A. Archivos bajo `TENANTS_ROOT/<tenant>/media/` con fila en `inbound_media` (RLS) y retención configurable** | Respaldado por [HU-ARCH-03](../SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md); simple | Disco del servidor |
| B. Base64 en Postgres (como `agent-sale`) | Sin archivos | Base enorme; backups lentos |
| C. Almacenamiento S3 compatible | Escalable | Otra credencial y costo |

**Recomendación: A**, con C como evolución. Estado: ⏳ pendiente.

### D-SPEC-04-3 · Proveedor de visión por defecto

| Opción | Pros | Contras |
|---|---|---|
| A. `deepseek-flash` (multimodal desde 2026-09-10) | (costo bajo) | Calidad de OCR sin medir |
| B. `claude-haiku-4-5` | Probado en `agent-sale` (con Sonnet) | (costo mayor) |
| C. Gemini | Barato | 2.5 Flash-Lite se retira el 2026-10-20 |

**Recomendación: elegir por benchmark** de al menos 30 comprobantes reales ([HU-MEDIA-04](hu/HU-MEDIA-04-dispatcher-de-vision.md)); arrancar con
B si el benchmark no está listo. Estado: ⏳ pendiente.

## Fuera de alcance

Voz en llamadas ([HU-MEDIA-08](../../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-MEDIA-08-voz-en-llamadas.md)), visor de media en la bandeja ([HU-MEDIA-07](../../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-MEDIA-07-visor-de-media.md)), video.

## Métricas de éxito

- ≥95 % de notas de voz respondidas sin pedir que el cliente escriba.
- ≥90 % de comprobantes conciliados automáticamente (monto ± tolerancia y cuenta destino), el resto a
  revisión humana.

## Requerimientos cubiertos

REQ-ARCH-05, REQ-MEDIA-01 a REQ-MEDIA-07, REQ-BILL-03.
