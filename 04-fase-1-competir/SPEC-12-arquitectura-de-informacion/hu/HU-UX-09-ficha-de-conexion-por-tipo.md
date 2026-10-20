---
id: HU-UX-09
titulo: Ficha de conexión por tipo enlazada con los agentes
spec: SPEC-12
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, diferenciacion, confianza]
req: [REQ-UX-13]
dependencias: [HU-UX-02, HU-AOS-23, HU-AOS-47]
skills: ["frontend-design", "panel-ui", "built-in-browser", "meta-whatsapp"]
estado: borrador
---

# HU-UX-09 · Ficha de conexión por tipo enlazada con los agentes

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-12](../spec.md). Nace de [D-37](../../../02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto) (2026-10-19): reemplaza al hub de Meta que esperaba [HU-CONN-08](../../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md) (Hito 0B).

**ID:** HU-UX-09

**Título:** Ficha de conexión por tipo enlazada con los agentes

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero abrir cada conexión y ver en su ficha solo lo que aplica a su tipo, y saltar de una conexión a sus agentes y de un agente a sus conexiones, para gestionar mis canales sin buscar en páginas globales.

**Por qué importa (valor empresarial):** Con D-35 un agente publicado vive en una o más conexiones. Si el dueño no ve qué agente atiende qué canal, ni dónde está la salud de su número, no confía en lo que publica. Juntar en la ficha lo que hoy está en «Salud de Meta», «Herramientas», Calendario, Habilidades y Configuración elimina la mayor fuente de «no encuentro».

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-13

**Dependencias:** [HU-UX-02](HU-UX-02-menu-v2.md), [HU-AOS-23](../../SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md), [HU-AOS-47](../../SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md)

**Criterios de aceptación (Gherkin):**
- **Ficha Meta.** Dado una conexión de WhatsApp oficial (Embedded Signup o app propia), cuando abro su ficha, entonces veo Salud, Números, Plantillas, Webhook, Producción, Costos y Agentes.
- **Ficha WhatsApp Web.** Dado una conexión de WhatsApp Web (QR), cuando abro su ficha, entonces veo Vinculación (QR, reiniciar vínculo y aviso de riesgo), Estado y Agentes, y no veo Salud, Plantillas ni Producción.
- **Otras fichas.** Dado una conexión de Google Calendar, Wompi, chat web o SMTP, cuando abro su ficha, entonces veo respectivamente Cuenta, Credenciales, Apariencia e Instalación, o Credenciales, más la pestaña Agentes.
- **Salud solo en Meta.** Dado la lista de Conexiones, cuando la abro, entonces solo las filas Meta muestran un indicador de salud y ya no existe la página global «Salud de Meta».
- **Conexión → agente.** Dado la pestaña Agentes de una conexión, cuando elijo un agente, entonces llego a su ficha en Agentes.
- **Agente → conexión.** Dado la ficha de un agente, cuando abro la pestaña Conexiones, entonces veo una tabla con conexión, tipo, rol, prioridad, cuál es la principal (por defecto) y estado, y cada fila me lleva a la ficha de esa conexión.
- **Superpoderes.** Dado la ficha de un agente, cuando abro la pestaña Superpoderes, entonces veo las capacidades que tiene ese agente, y «Habilidades» solo nombra los packs en Configuración.
- **Agregar conexión.** Dado el diálogo «Agregar conexión», cuando elijo chat web, Google Calendar o WhatsApp Web, entonces llego al flujo de ese tipo (el `type.url` del tipo) y no al asistente de WhatsApp.

**Evidencia / Definición de Terminado:**
- Ruta `/conexiones/[id]` con pestañas por tipo; se mueven `conexiones/meta/_components/meta-health-actions.tsx`, `meta-health-checks.tsx` y `webhook-register.tsx`, y las páginas de `conexiones/meta/[connectionId]/` (números, plantillas, producción, pasar a producción) y `/plantillas`.
- La configuración de Google (hoy en `/calendario`), Wompi (hoy en `/habilidades/pack_payments`), chat web (hoy en Configuración) y SMTP pasa a la ficha de su conexión; WhatsApp Web deja `/conexiones/waweb` y el botón global de la lista.
- Requisitos de Meta pasa a Plataforma → App de Meta; «Probar asistente» (`/asistente`) pasa a la ficha del agente.
- `lib/agentes.ts` (`PESTANAS`) suma Conexiones y Superpoderes: la pestaña Conexiones reemplaza el texto «Atiende en …» de `app/(app)/agentes/[id]/page.tsx` por la tabla con rol, prioridad y principal, con datos de `/admin/agents/overview` y `/admin/connections/{id}/agents`.
- Corrección de `conexiones/_components/new-connection-dialog.tsx` (hoy ~153-156 en `main`): el enlace usa `type.url` en lugar de `/conexiones/whatsapp` fijo, con test por tipo.
- Redirecciones de las rutas de Conexiones de la tabla de [SPEC-12 · Diseño](../design.md#migración-despliegue-y-reversa), con test; capturas de una ficha Meta y una de WhatsApp Web.

**Riesgos/Notas:**
- Construye sobre lo que ya entregaron [HU-AOS-23](../../SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md) (panel #80, consola con los agentes de cada conexión) y [HU-AOS-47](../../SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md) (panel #82, ficha del agente con «Atiende en …» y 4 pestañas).
- Las acciones de Meta que dependen del Tech Provider o del Embedded Signup real siguen bloqueadas por los trámites del dueño; la ficha las muestra con su estado, no las habilita.
- [HU-CONN-08](../../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md) (Hito 0B) queda cubierta por esta HU en lo que toca al panel; se revisa cuando se abra el 0B.
