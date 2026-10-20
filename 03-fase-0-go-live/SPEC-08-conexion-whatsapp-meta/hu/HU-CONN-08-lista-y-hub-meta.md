---
id: HU-CONN-08
titulo: Lista de conexiones v2 y hub de WhatsApp-Meta
spec: SPEC-08
fase: 0
hito: 0B
workstream: Canales y conexiones
prioridad: P0
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-CONN-04]
dependencias: [HU-CONN-03, HU-CONN-04, HU-SH-05, HU-UI-02]
skills: ["frontend-design", "built-in-browser", "figma-design-to-code", "meta-whatsapp", "panel-ui"]
estado: borrador
---

# HU-CONN-08 · Lista de conexiones v2 y hub de WhatsApp-Meta

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-08](../spec.md) (D-SPEC-08-1, P-08).

**ID:** HU-CONN-08

**Título:** Lista de conexiones v2 y hub de WhatsApp-Meta

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero ver mis conexiones con el icono de cada canal, su estado real y su entorno, y entrar a cada conexión de WhatsApp para gestionar sus números, plantillas, webhook, producción y costos en un solo lugar, para entender y controlar mis canales sin perderme.

**Por qué importa (valor empresarial):** Es la pantalla que más soporte genera en cualquier plataforma de WhatsApp. Reunir lo de Meta en el hub de cada conexión (como pidió el cliente) y quitar de la vista lo que no aplica reduce errores y hace profesional el producto frente a Wati o SleekFlow.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** L

**REQ mapeados:** REQ-CONN-04

**Dependencias:** [HU-CONN-03](HU-CONN-03-ciclo-de-vida-seguro.md), [HU-CONN-04](HU-CONN-04-diagnostico-confiable.md), [HU-SH-05](../../SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md), [HU-UI-02](../../SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md)

**Criterios de aceptación (Gherkin):**
- **Lista clara.** Dado la lista, cuando la abro, entonces cada fila muestra el icono del tipo (WhatsApp Meta, WhatsApp Web, correo, Calendar), nombre editable, estado con motivo, badge Prueba/Producción y "Abrir".
- **Acciones permitidas.** Dado una fila, cuando abro sus acciones, entonces solo veo las que el backend permite para ese tipo y estado; eliminar pide confirmación con la consecuencia.
- **Hub.** Dado una conexión de WhatsApp-Meta, cuando la abro, entonces veo las pestañas Resumen/Salud, Números, Plantillas, Webhook, Producción y Costos con datos de esa conexión.
- **Menú limpio.** Dado un negocio sin conexiones de Meta, cuando ve el menú, entonces no aparecen Requisitos, Producción ni Plantillas globales; los pasos de la app de la plataforma están en "Plataforma" para el master.
- **Wizard con caminos.** Dado "Agregar conexión → WhatsApp", cuando empiezo, entonces elijo Prueba (mi app), Producción (Conectar con Facebook) o Producción (mi app), con ayuda de dónde sacar cada dato, y al terminar llego al hub con un mensaje de prueba.

**Evidencia / Definición de Terminado:**
- Endpoints por conexión (resumen, webhook, readiness, costos) y `allowed_actions`; páginas del hub; capturas en claro y oscuro y en móvil.

**Riesgos/Notas:**
- Si P-08 se aprueba como "no se vende WhatsApp Web", su tipo se muestra como "solo pruebas".
