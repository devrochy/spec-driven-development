# SPEC-17 · Diseño

- **Instagram y Messenger**: tipos de conexión disponibles en el catálogo (ADR-0069), adapters de
  salida, resolver de credenciales por conexión ([HU-CONN-01](../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md)) y hub por tipo ([HU-CONN-08](../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md)). Las reglas de
  ventana de 24 h de Meta aplican igual.
- **Chat web**: widget JS embebible por dominio permitido, sesión anónima con Turnstile, mismo loop del
  asistente con canal `web`, traspaso a WhatsApp si el cliente lo pide.
- **Campañas**: segmentos (por etiquetas, segmento de compra, estado de suscripción vía registros del
  core), plantilla aprobada, programación, límite de envíos por minuto, registro de consentimiento
  (opt-in/opt-out) y costo estimado de Meta antes de enviar; cada envío consume el fee de plantilla.
