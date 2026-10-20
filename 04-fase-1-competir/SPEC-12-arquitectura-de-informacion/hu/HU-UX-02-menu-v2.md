---
id: HU-UX-02
titulo: Menú v2 agrupado por tarea con renombres
spec: SPEC-12
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, operacion]
req: [REQ-UX-01, REQ-UX-12]
dependencias: [HU-UX-01]
skills: ["frontend-design", "built-in-browser", "panel-ui"]
estado: en-curso
---

# HU-UX-02 · Menú v2 agrupado por tarea con renombres

> Estado SDD: En curso (rama `feat/hu-ux-02-menu-v2` de solvershub-panel) — [SPEC-12](../spec.md). Reescrita el 2026-10-19 con [D-37](../../../02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto): ya no depende de [HU-CONN-08](../../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md); el hub de cada conexión lo construye [HU-UX-09](HU-UX-09-ficha-de-conexion-por-tipo.md).

**ID:** HU-UX-02

**Título:** Menú v2 agrupado por tarea con renombres

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero un menú corto agrupado por lo que hago (atender, ver mis agentes y conexiones, agendar, vender, cobrar, consumo, equipo y configuración) con nombres que entiendo para encontrar todo sin aprender jerga.

**Por qué importa (valor empresarial):** Es la primera impresión del producto en cada sesión. Hoy un dueño con todos los packs ve 40 entradas; un menú de 11 con el agente a un toque (D-35) reduce soporte y aumenta el uso de lo que el cliente paga.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-01, REQ-UX-12

**Dependencias:** [HU-UX-01](HU-UX-01-adr-arquitectura-de-informacion.md)

**Criterios de aceptación (Gherkin):**
- **Grupos.** Dado el menú, cuando lo abro como dueño con todos los packs, entonces veo Operación (Resumen, Conversaciones, Clientes), Tu asistente (Agentes, Conexiones), Negocio (Agenda, Ventas, Cobranza) y Cuenta (Consumo y plan, Equipo, Configuración), y Plataforma solo si soy master.
- **Menú corto.** Dado un dueño con todos los packs, cuando cuento las entradas de primer nivel, entonces son 11 (como máximo 12) y ninguna se llama «Herramientas».
- **Pestañas, no hermanas.** Dado un negocio con una sección de varias páginas (Conversaciones con Escalaciones, Cobranza, Ventas, Agenda), cuando la abro, entonces sus páginas aparecen como pestañas tomadas del campo `tabs` del ítem y no como entradas hermanas del menú.
- **Mismas URLs.** Dado un enlace guardado (`/escalaciones`, `/leads`, `/dlq`, `/calendario/bloqueos`, `/cobranza/promesas`), cuando lo abro, entonces llego a la misma página que antes, ahora marcada en su grupo y pestaña nuevos.
- **Horario con la clave del backend.** Dado un colaborador con `pack_calendar:configuracion`, cuando abre Agenda, entonces ve la pestaña Horario (el panel deja de usar `pack_calendar:conexion` para el horario).
- **Renombres.** Dado el glosario, cuando reviso el menú, entonces no aparecen "Tenant", "Plugin", "Costos LLM", "Leads" ni "DLQ".
- **Solo lo habilitado.** Dado un negocio sin cobranza, cuando abre el menú, entonces no aparece Cobranza.

**Evidencia / Definición de Terminado:**
- `NAV_GROUPS` reescrito en `apps/panel-web/components/shell/nav.ts` (o manifiesto si [HU-FWK-05](../../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-05-manifiesto-de-menu.md) llegó); la entrada Agentes (sección `agents`) ya existe y se conserva.
- `lib/shell/navegacion.ts` toma las pestañas de `tabs`; `paleta.ts` (`ATAJOS_IR`) y `lib/labels.ts` al día.
- `components/shell/sidebar.test.tsx` y `lib/shell/navegacion.test.ts` al día; `typecheck`, `lint`, `build`, `test` y `api:types:check` contra `origin/develop`.
- Capturas del menú antes y después como dueño con todos los packs, con el conteo de entradas (40 → 11).

**Riesgos/Notas:**
- **Solo reagrupa: ninguna URL cambia**, así que no lleva redirecciones. Las rutas que se mueven, con sus redirecciones, son de [HU-UX-08](HU-UX-08-agenda-unificada.md) (Agenda), [HU-UX-09](HU-UX-09-ficha-de-conexion-por-tipo.md) (fichas de conexión) y [HU-UX-10](HU-UX-10-cobranza-y-ventas-en-pestanas.md) (Cobranza y Ventas).
- No hay entrada Suscripciones: el panel no tiene esa página todavía; la agrega [HU-UX-10](HU-UX-10-cobranza-y-ventas-en-pestanas.md).
- Antes del código de las fichas, el dueño revisa un prototipo clicable del menú v2.
