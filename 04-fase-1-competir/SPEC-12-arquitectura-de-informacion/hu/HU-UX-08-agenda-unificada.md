---
id: HU-UX-08
titulo: Agenda unificada con calendario, tipos de cita y horario
spec: SPEC-12
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, diferenciacion]
req: [REQ-UX-14]
dependencias: [HU-UX-02, HU-CAL-01, HU-CAL-03]
skills: ["frontend-design", "panel-ui", "built-in-browser", "backend-design:migration-safety"]
estado: borrador
---

# HU-UX-08 · Agenda unificada con calendario, tipos de cita y horario

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-12](../spec.md). Nace de [D-37](../../../02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto) (2026-10-19).

**ID:** HU-UX-08

**Título:** Agenda unificada con calendario, tipos de cita y horario

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio que agenda citas quiero una sola sección Agenda donde veo el calendario, creo citas o bloqueos sobre él y ajusto los tipos de cita y el horario, para no saltar entre cinco páginas.

**Por qué importa (valor empresarial):** La agenda es lo que el agente de Agenda llena por el cliente. Si el dueño no puede bloquear un hueco o distinguir los tipos de cita de un vistazo, deja de confiar en el agente y vuelve a la libreta.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-14

**Dependencias:** [HU-UX-02](HU-UX-02-menu-v2.md), [HU-CAL-01](../../SPEC-24-agenda-y-citas/hu/HU-CAL-01-bloqueos-de-agenda.md), [HU-CAL-03](../../SPEC-24-agenda-y-citas/hu/HU-CAL-03-calendario-visual.md)

**Criterios de aceptación (Gherkin):**
- **Una entrada.** Dado un negocio con agenda, cuando abro Agenda, entonces veo las pestañas Calendario, Tipos de cita y Horario, y el menú no tiene otras entradas del calendario.
- **Cita o bloqueo.** Dado el calendario, cuando selecciono un hueco, entonces elijo «Cita» o «Bloqueo» y se crea lo elegido sin salir de la vista.
- **Bloqueos visibles.** Dado un bloqueo, cuando miro la semana, entonces se ve como evento de fondo y puedo arrastrarlo para moverlo.
- **Tipo de un vistazo.** Dado un tipo de cita con color o identificador, cuando veo sus citas en el calendario, entonces cada evento muestra ese color o identificador.
- **Horario de agendamiento.** Dado un colaborador con permiso `pack_calendar:configuracion`, cuando abre la pestaña Horario, entonces edita el horario de agendamiento (`business_hours`) sin un 403.
- **Google fuera de Agenda.** Dado un negocio que quiere conectar Google Calendar, cuando busca dónde, entonces lo encuentra en Conexiones y no en Agenda.

**Evidencia / Definición de Terminado:**
- Pestaña Calendario sobre `calendario/citas/_components/calendar-grid.tsx` (FullCalendar) con selección «Cita»/«Bloqueo», bloqueos como eventos de fondo arrastrables y color por tipo; sale la tabla duplicada de próximas citas de `/calendario`.
- Tipos de cita con color o identificador; si el tipo no lo tiene, columna nueva en `pack_calendar` con valor por defecto y migración reversible.
- La pestaña Horario conserva la clave `pack_calendar:configuracion` del backend (`packages/pack-calendar/pack_calendar/module.py:360`), que ya adopta el menú v2 de [HU-UX-02](HU-UX-02-menu-v2.md).
- Redirecciones de `/calendario`, `/calendario/citas`, `/calendario/bloqueos`, `/calendario/tipos` y `/calendario/horario` con test.
- Capturas de crear un bloqueo desde el calendario y de una semana con tipos de cita de colores.

**Riesgos/Notas:**
- La conexión con Google pasa a la ficha de conexión de [HU-UX-09](HU-UX-09-ficha-de-conexion-por-tipo.md); hasta que esa HU entre, Agenda conserva un enlace a la página actual.
- El color debe salir de los tokens de [SPEC-29](../../SPEC-29-sistema-de-diseno-unificado/spec.md) (paleta categórica con contraste AA), no de un selector libre de hex.
