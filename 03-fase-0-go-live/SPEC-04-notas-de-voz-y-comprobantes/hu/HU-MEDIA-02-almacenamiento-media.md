---
id: HU-MEDIA-02
titulo: Descarga y almacenamiento de media entrante
spec: SPEC-04
fase: 0
hito: 0B
workstream: Multimodalidad
prioridad: P0
critico: true
estimacion: M
impacto: [calidad_ia, operacion]
req: [REQ-MEDIA-01, REQ-MEDIA-06, REQ-ARCH-05]
dependencias: [HU-MEDIA-01]
skills: ["db-migration", "backend-design:idempotency-and-side-effects", "auditor-multitenant", "backend-design:security-discipline"]
estado: borrador
---

# HU-MEDIA-02 · Descarga y almacenamiento de media entrante

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-04](../spec.md).

**ID:** HU-MEDIA-02

**Título:** Descarga y almacenamiento de media entrante

**Workstream:** Multimodalidad

**Historia:** Como dueño de un negocio quiero que los audios y fotos que envían mis clientes se descarguen y guarden de forma segura para que el asistente pueda entenderlos y yo pueda revisarlos después.

**Por qué importa (valor empresarial):** Es la base de todo lo multimodal: sin descarga no hay transcripción, OCR ni evidencia de pago. Hoy la URL de la media se guarda vacía y el contenido se pierde.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-MEDIA-01, REQ-MEDIA-06, REQ-ARCH-05

**Dependencias:** [HU-MEDIA-01](HU-MEDIA-01-adr-media.md)

**Criterios de aceptación (Gherkin):**
- **Descarga.** Dado un audio entrante de WhatsApp Cloud, cuando llega, entonces se descarga con las credenciales de la conexión, se guarda bajo `TENANTS_ROOT` y se registra en `inbound_media` con su hash.
- **Límites.** Dado un archivo de más de 16 MB o una descarga que tarda más de 20 s, cuando se procesa, entonces se responde al cliente con un mensaje configurable y queda registrado.
- **Idempotencia.** Dado el mismo mensaje reintentado, cuando se procesa de nuevo, entonces no se descarga ni se guarda dos veces.
- **Aislamiento y retención.** Dado dos negocios, cuando uno lista su media, entonces no ve la del otro; dado el vencimiento de retención, cuando corre el job, entonces los archivos se eliminan y la fila queda marcada (soft-delete).
- **WhatsApp Web.** Dado un audio por WhatsApp Web, cuando llega, entonces pasa por el mismo procesamiento y por la cuota.

**Evidencia / Definición de Terminado:**
- Migración con RLS, tests de descarga con mock de la Graph API, test de aislamiento.

**Riesgos/Notas:**
- Para BYOK la descarga necesita el resolver de credenciales ([HU-CONN-01](../../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md)).
