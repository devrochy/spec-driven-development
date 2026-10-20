---
id: HU-MEDIA-03
titulo: Notas de voz a texto con llave híbrida
spec: SPEC-04
fase: 0
hito: 0B
workstream: Multimodalidad
prioridad: P0
critico: true
estimacion: M
impacto: [calidad_ia, diferenciacion]
req: [REQ-MEDIA-02, REQ-MEDIA-07, REQ-BILL-03]
dependencias: [HU-MEDIA-02, HU-BILL-04]
skills: ["backend-design:error-handling-as-design", "deep-research", "optimizer", "eval-author"]
estado: borrador
---

# HU-MEDIA-03 · Notas de voz a texto con llave híbrida

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-04](../spec.md).

**ID:** HU-MEDIA-03

**Título:** Notas de voz a texto con llave híbrida

**Workstream:** Multimodalidad

**Historia:** Como cliente de un negocio quiero mandar una nota de voz y que el asistente me responda como si la hubiera escrito para no tener que teclear.

**Por qué importa (valor empresarial):** En Colombia una gran parte de los mensajes de WhatsApp son audios. Sin transcripción el asistente responde "no puedo escuchar audios" y pierde la venta; con Groq cuesta (cifra interna) por nota de 30 s.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-MEDIA-02, REQ-MEDIA-07, REQ-BILL-03

**Dependencias:** [HU-MEDIA-02](HU-MEDIA-02-almacenamiento-media.md), HU-BILL-04

**Criterios de aceptación (Gherkin):**
- **Transcripción.** Dado una nota de voz en español, cuando llega, entonces se transcribe con el proveedor configurado y el turno recibe `[Nota de voz] <texto>`.
- **Llave híbrida.** Dado un negocio sin llave propia, cuando se transcribe, entonces se usa la llave de plataforma y se cobran créditos; con llave propia solo el fee.
- **Vacío.** Dado un audio sin voz entendible, cuando la transcripción viene vacía, entonces el asistente pide amablemente que repita o escriba.
- **Idioma.** Dado un negocio configurado en otro idioma, cuando transcribe, entonces usa ese idioma.
- **Costo.** Dado cada transcripción, cuando termina, entonces hay una fila `stt` en el ledger con segundos facturados (mínimo del proveedor).

**Evidencia / Definición de Terminado:**
- Tests con audios de ejemplo y mock del proveedor; prueba de conexión en el panel de Configuración.

**Riesgos/Notas:**
- Proveedores: Groq `whisper-large-v3-turbo` ((tarifa pública del proveedor)) u OpenAI `gpt-4o-mini-transcribe` ((tarifa pública del proveedor)).
