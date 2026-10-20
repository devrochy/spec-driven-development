# SPEC-04 · Diseño

## Flujo de ingesta

```
webhook ─► consumer ─► ¿media? ─no─► turno normal
                         │
                         sí
                         ▼
             descargar (Graph API, ≤16 MB, timeout 20 s) ─► inbound_media (RLS)
                         │
            ┌────────────┴─────────────┐
          audio                       imagen
            │                           │
     STT (llave híbrida,         ¿pedido/cuota con pago pendiente?
     idioma del negocio)            │sí                 │no
            │                  clasificar           describir producto
            │                  comprobante/producto  (playbook del pack)
            │                     │comprobante           │
            ▼                     ▼                      ▼
   texto "[Nota de voz] …"   OCR {monto, cuenta}    "[Foto de producto] …"
   → turno                   → ruta financiera       → turno
                               (sin LLM conversacional)
```

- Idempotencia: caché del resultado por `external_message_id` (TTL 1 h) para los reintentos del
  consumer ([HU-ARCH-06](../SPEC-01-produccion-segura/hu/HU-ARCH-06-consumer-y-dlq.md)).
- Costos: cada llamada escribe su fila en el ledger (`stt`, `vision`) con `key_mode`.
- Los prompts de clasificación, descripción y OCR viven en playbooks del pack dueño (invariante 3).

## Datos

`inbound_media`: `tenant_id`, `conversation_id`, `message_id`, `kind` (audio/imagen), `mime_type`,
`path`, `bytes`, `sha256`, `processed_text`, `retention_until`. `payment_receipts` (cobranza y
comercio): `tenant_id`, referencia del pedido o cuota, `ocr_monto`, `ocr_cuenta`, `resultado`
(`aprobado_auto`, `rechazado_auto`, `pendiente_revision`, `aprobado_admin`, `rechazado_admin`),
`intentos`.

## ADR

- **ADR "Procesamiento de media en el core"** (alcance, privacidad, retención, costos).

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Comprobantes falsos | Tolerancia de monto, cuenta destino del negocio, 2 intentos y revisión humana |
| Datos personales en imágenes | Retención limitada y aviso en el DPA (HU-GTM-02) |
