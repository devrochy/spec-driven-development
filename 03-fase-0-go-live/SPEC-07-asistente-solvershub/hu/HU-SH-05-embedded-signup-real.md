---
id: HU-SH-05
titulo: Embedded Signup real en el panel nuevo
spec: SPEC-07
fase: 0
hito: 0A
workstream: Canales y conexiones
prioridad: P0
critico: true
estimacion: L
impacto: [ingreso, diferenciacion]
req: [REQ-SH-05, REQ-CONN-03]
dependencias: [HU-CONN-01, HU-CONN-02]
skills: ["deep-research", "frontend-design", "built-in-browser", "backend-design:security-discipline", "meta-whatsapp", "panel-ui"]
ola: 3
estado: borrador
---

# HU-SH-05 · Embedded Signup real en el panel nuevo

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-07](../spec.md).

**ID:** HU-SH-05

**Título:** Embedded Signup real en el panel nuevo

**Workstream:** Canales y conexiones

**Historia:** Como cliente nuevo quiero conectar el WhatsApp de mi negocio desde el panel con el botón "Conectar con Facebook" y quedar listo para recibir mensajes para no depender de nadie que configure tokens.

**Por qué importa (valor empresarial):** Sin Embedded Signup, cada alta requiere que alguien copie App ID, secretos y tokens: el alta automática se detiene en el último paso. Es también lo que permite a SolversHub operar como Tech Provider de Meta, como Wati o SleekFlow.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** L

**REQ mapeados:** REQ-SH-05, REQ-CONN-03

**Dependencias:** [HU-CONN-01](../../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md), [HU-CONN-02](../../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-02-errores-500-y-bloqueos.md)

**Criterios de aceptación (Gherkin):**
- **Popup de Meta.** Dado el wizard en "Producción (Conectar con Facebook)", cuando pulso el botón, entonces se abre el flujo de Meta con el `config_id` de la plataforma.
- **Intercambio.** Dado que termino el flujo, cuando el panel recibe `authResponse.code` y el evento `WA_EMBEDDED_SIGNUP` con WABA y número, entonces el backend intercambia el código y encadena: suscribir la WABA, registrar el número con PIN, sincronizar plantillas y verificar salud.
- **Cancelación.** Dado que cierro el popup, cuando el panel recibe el evento de cancelación, entonces el wizard lo registra y ofrece reintentar.
- **Reanudar.** Dado un wizard interrumpido, cuando vuelvo, entonces veo en qué paso quedó y lo retomo; pasadas 24 h se reutiliza el borrador (sin el error 500 actual).
- **Final.** Dado el alta completa, cuando termina, entonces llego al hub de la conexión con un botón para enviar un mensaje de prueba.
- **Requisitos de Meta.** Dado la app de la plataforma, cuando se revisa, entonces la verificación del negocio, el App Review de los permisos y el `config_id` de producción están aprobados (checklist en "Plataforma → App de Meta").

**Evidencia / Definición de Terminado:**
- Alta real de un número de prueba de punta a punta con video o capturas; endpoints de estado y cancelación del wizard; ADR-0080 marcado como implementado.

**Riesgos/Notas:**
- R-01: la aprobación de Meta puede tardar semanas; empezar el trámite el primer día. Mientras tanto, BYOK de producción ([HU-CONN-06](../../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-06-byok-produccion.md)).
- Verificar contra la documentación vigente de Meta el uso de `sessionInfoVersion` y la forma del evento.
