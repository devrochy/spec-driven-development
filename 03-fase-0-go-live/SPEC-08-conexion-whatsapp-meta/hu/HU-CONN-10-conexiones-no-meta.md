---
id: HU-CONN-10
titulo: Arreglos de conexiones que no son de Meta
spec: SPEC-08
fase: 0
hito: 0B
workstream: Canales y conexiones
prioridad: P0
critico: false
estimacion: S
impacto: [confianza]
req: [REQ-CONN-04]
dependencias: []
skills: ["backend-design:debugging-discipline", "built-in-browser"]
estado: borrador
---

# HU-CONN-10 · Arreglos de conexiones que no son de Meta

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-08](../spec.md).

**ID:** HU-CONN-10

**Título:** Arreglos de conexiones que no son de Meta

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero que las conexiones de correo, Google Calendar y WhatsApp Web se puedan editar, desactivar y eliminar como espero para no ver errores ni conexiones que reviven solas.

**Por qué importa (valor empresarial):** Una conexión de Calendar que se reactiva sola después de desactivarla, o un "Editar" que da 404, erosionan la confianza en todo el panel. Son arreglos acotados.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** S

**REQ mapeados:** REQ-CONN-04

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Editar.** Dado WhatsApp Web o Calendar, cuando abro sus acciones, entonces no aparece "Editar" (no son de formulario) y sí "Abrir", que lleva a su página.
- **Calendar no revive.** Dado una conexión de Calendar desactivada o eliminada, cuando se refresca el token, entonces no vuelve a activarse.
- **Asistente correcto.** Dado "Agregar conexión → Google Calendar", cuando pulso "Abrir asistente", entonces voy al flujo de Calendar, no al de WhatsApp.
- **SMTP probado.** Dado una conexión SMTP nueva, cuando la guardo, entonces se hace una prueba de envío y se informa el resultado.
- **Principal solo donde aplica.** Dado una conexión que no es de mensajería, cuando abro sus acciones, entonces no aparece "Marcar principal".

**Evidencia / Definición de Terminado:**
- Corrección de `connection-actions.tsx:83`, `pack_calendar/oauth.py:221-254`, `new-connection-dialog.tsx:153-157`; tests.

**Riesgos/Notas:**
- Detalle en la auditoría de Conexiones.
