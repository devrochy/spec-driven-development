# SPEC-13 · Vistas profesionales del panel

> Estado SDD: Parqueada (2026-10-17, D-35) · Fase 1 · Workstream UX/Onboarding

**Parqueada (2026-10-17, [D-35](../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes)):** son vistas por habilidad (bandeja, tickets, leads, packs y plan compactos) y con D-35 el panel pasa a ser por agente. Lo útil va a [HU-AOS-28](../SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md) (bandeja «En curso» en vivo con contador de mensajes nuevos, tickets, leads con los datos generales del canal y paginado) y a [HU-AOS-29](../SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md) (tendencias y calidad); el `FilterBar` y las tablas densas ([HU-UI-08](hu/HU-UI-08-filtros-y-tablas.md)) ya viven en [HU-DS-03](../SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-03-kit-de-componentes-panel.md); el contrato de datos del dashboard ([HU-UI-07](hu/HU-UI-07-dashboard-con-tendencias.md)) lo consumen [HU-DS-07](../SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-07-resumen-modular-por-rol.md) y [HU-AOS-29](../SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md); la grilla de colaboradores ([HU-UI-10](hu/HU-UI-10-colaboradores-y-permisos.md)) se atiende con los P0 del ciclo de pruebas 2026-10-13; cuenta y notificaciones ([HU-UI-13](hu/HU-UI-13-cuenta-y-notificaciones.md)) y el visor de media ([HU-MEDIA-07](hu/HU-MEDIA-07-visor-de-media.md)) se retoman cuando un cliente los pida.

**Absorbida en parte (2026-10-19, [D-37](../../02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto)):** el objetivo de [HU-UI-09](hu/HU-UI-09-configuracion-por-pestanas.md) (configuración por pestañas) lo toma el rediseño del menú v2 de [SPEC-12](../SPEC-12-arquitectura-de-informacion/spec.md): Configuración absorbe Mensajes fallidos y Habilidades, el horario de agendamiento pasa a Agenda ([HU-UX-08](../SPEC-12-arquitectura-de-informacion/hu/HU-UX-08-agenda-unificada.md)) y la configuración de cada conexión a su ficha ([HU-UX-09](../SPEC-12-arquitectura-de-informacion/hu/HU-UX-09-ficha-de-conexion-por-tipo.md)). [HU-UI-09](hu/HU-UI-09-configuracion-por-pestanas.md) sigue parqueada para no duplicar.

## Problema

Las pantallas que los operadores usan todos los días son más débiles que las de `agent-sale`
([panel-nuevo.md](../../01-revalidacion/panel-nuevo.md)): Conversaciones es una tabla y no una bandeja;
Escalaciones es de solo lectura; el Dashboard no tiene tendencias; Colaboradores muestra claves de
permisos; Leads no tiene filtros ni exportación; Configuración pierde cambios al cambiar de pestaña;
las páginas de packs son largas y repiten el menú; no hay perfil, recuperación de contraseña ni
notificaciones; la media que mandan los clientes no se puede ver.

## Por qué importa (valor empresarial)

El cliente pidió vistas "más completas, profesionales y compactas". Son las pantallas donde se gana o
se pierde la percepción de calidad frente a Respond.io, SleekFlow o Zendesk, que venden la bandeja y
los tickets como el corazón de su producto.

## Alcance

| HU | Qué | Top 15 |
|---|---|---|
| [HU-UI-05](hu/HU-UI-05-tickets-reales.md) | Tickets reales en "Por atender" | #2 |
| [HU-UI-06](hu/HU-UI-06-bandeja-dos-paneles.md) | Bandeja de dos paneles | #3 |
| [HU-UI-07](hu/HU-UI-07-dashboard-con-tendencias.md) | Dashboard con tendencias y calidad | #7 |
| [HU-UI-08](hu/HU-UI-08-filtros-y-tablas.md) | `FilterBar` único y tablas densas | #8 |
| [HU-UI-09](hu/HU-UI-09-configuracion-por-pestanas.md) | Configuración por pestañas con estado | #9 |
| [HU-UI-10](hu/HU-UI-10-colaboradores-y-permisos.md) | Colaboradores con grilla de permisos | #10 |
| [HU-UI-11](hu/HU-UI-11-clientes-y-leads.md) | Clientes con filtros, CSV y detalle | #12 |
| [HU-UI-12](hu/HU-UI-12-packs-costos-y-plan-compactos.md) | Packs, Consumo y Plan compactos | #13 |
| [HU-UI-13](hu/HU-UI-13-cuenta-y-notificaciones.md) | Cuenta y notificaciones a operadores | #11 |
| [HU-MEDIA-07](hu/HU-MEDIA-07-visor-de-media.md) | Visor de media y transcripción | — |

## Decisiones

### D-SPEC-13-1 · Excepciones a `DESIGN.md`

| Opción | Pros | Contras |
|---|---|---|
| **A. Documentar dos excepciones: tablas densas y bandeja a todo el ancho** | La bandeja y las tablas necesitan espacio | Más reglas |
| B. Mantener el contenedor de 1200 px | Coherencia | Bandeja apretada |

**Recomendación: A.** Estado: ⏳ pendiente.

### D-SPEC-13-2 · Actualización de la bandeja

| Opción | Pros | Contras |
|---|---|---|
| **A. Polling cada 5–10 s mientras la pestaña está visible** | Simple; funciona con el BFF | Algo de carga |
| B. Server-Sent Events o WebSocket | Tiempo real | Infra nueva detrás del túnel |

**Recomendación: A** en la Fase 1. Estado: ⏳ pendiente.

## Métricas de éxito

- Tiempo medio de respuesta humana a una escalación a la mitad.
- % de escalaciones resueltas desde el panel sin salir a WhatsApp.

## Requerimientos cubiertos

REQ-UX-04, REQ-UX-07, REQ-FIX-04, REQ-FIX-09, REQ-BILL-06, REQ-MEDIA-07.
