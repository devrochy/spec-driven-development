---
id: HU-UI-09
titulo: Configuración por pestañas con estado y controles claros
spec: SPEC-13
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, calidad_ia]
req: [REQ-UX-04]
dependencias: [HU-UI-02]
skills: ["frontend-design", "built-in-browser", "panel-ui"]
estado: parqueada
---

# HU-UI-09 · Configuración por pestañas con estado y controles claros

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md).

**ID:** HU-UI-09

**Título:** Configuración por pestañas con estado y controles claros

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero configurar mi asistente con pestañas que muestran su estado, opciones descritas, el horario en una grilla y el modelo elegido de una lista para no equivocarme y no perder cambios.

**Por qué importa (valor empresarial):** Hoy el horario se escribe como texto ("1 08:00-18:00") y las líneas mal escritas se descartan en silencio; el modelo es texto libre; cambiar de pestaña pierde lo editado. Cada error de configuración es una mala respuesta a un cliente.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-04

**Dependencias:** [HU-UI-02](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md)

**Criterios de aceptación (Gherkin):**
- **Pestañas con estado.** Dado Configuración, cuando la abro, entonces cada pestaña muestra su estado ("Pausado", "3 de 5", "Conectado") y la pestaña activa está en la URL.
- **Sin perder cambios.** Dado cambios sin guardar, cuando intento salir, entonces se me avisa.
- **Horario en grilla.** Dado el horario, cuando lo edito, entonces uso una grilla semanal con varias franjas por día y la zona horaria de una lista.
- **Opciones descritas.** Dado tono, emojis y estilo de mensajes, cuando elijo, entonces son tarjetas con descripción, no valores crudos.
- **Modelo de una lista.** Dado el modelo de IA, cuando elijo, entonces viene del tarifario con su costo en créditos.

**Evidencia / Definición de Terminado:**
- Componentes `ChoiceCards` y `WeeklySchedule`; tests; el editor crudo del AgentSpec queda al final, tras confirmación.

**Riesgos/Notas:**
- **2026-10-19, [D-37](../../../02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto):** el rediseño del menú v2 de [SPEC-12](../../SPEC-12-arquitectura-de-informacion/spec.md) absorbe el objetivo de esta HU (Configuración con pestañas que absorbe Mensajes fallidos y Habilidades; horario en Agenda, [HU-UX-08](../../SPEC-12-arquitectura-de-informacion/hu/HU-UX-08-agenda-unificada.md); configuración de cada conexión en su ficha, [HU-UX-09](../../SPEC-12-arquitectura-de-informacion/hu/HU-UX-09-ficha-de-conexion-por-tipo.md)). Lo que quede (grilla de horario, modelo de una lista, no perder cambios) se revisa contra esas HU antes de retomarla.
- El "Pausar asistente" pasa arriba de la pestaña.
