# SPEC-12 · Arquitectura de información, glosario y onboarding avanzado

> Estado SDD: Diseño aprobado · Fase 1 · Workstream UX/Onboarding
>
> **Reorientada (2026-10-17, [D-35](../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes)):** el grupo «Asistente» del menú v2 ([HU-UX-02](hu/HU-UX-02-menu-v2.md)) pasa a **Agentes · Superpoderes · Calidad**, la consola del Agent OS ([HU-AOS-23](../SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md), [HU-AOS-24](../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md), [HU-AOS-25](../SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md), [HU-AOS-29](../SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md) y [HU-AOS-47](../SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md)), en lugar de identidad, flujo y habilidades por pack.
>
> **Ampliada (2026-10-19, [D-37](../../02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto)):** el menú v2 baja a **≤ 12 entradas de primer nivel** para el dueño, con una sección por tarea, **fichas por objeto** (conexión y agente) y pestañas dentro. [HU-UX-02](hu/HU-UX-02-menu-v2.md) deja de depender de [HU-CONN-08](../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md) (el hub de Meta pasa a la ficha de conexión, [HU-UX-09](hu/HU-UX-09-ficha-de-conexion-por-tipo.md)) y nacen [HU-UX-08](hu/HU-UX-08-agenda-unificada.md) a [HU-UX-11](hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md). Este rediseño absorbe el objetivo de [HU-UI-09](../SPEC-13-vistas-profesionales/hu/HU-UI-09-configuracion-por-pestanas.md) (parqueada por D-35).

## Problema

El menú del panel (`solvershub-panel/apps/panel-web/components/shell/nav.ts`, `NAV_GROUPS`) le muestra a un dueño
con todos los packs **40 entradas en 8 grupos** (contadas sobre `origin/main`: Operación 5, Configuración 4, Negocio 2,
Cobranza 14, Comercio 5, Calendario 5, Herramientas 5 y Plataforma, que ya incluye Alta automática). Las páginas de pack repiten esas mismas
entradas como pestañas. Problemas concretos:

- Usa términos técnicos ("Costos LLM", "Tenants", "Leads", "Bandeja de fallos") y repite "Configuración" como grupo e ítem.
- Lo de cada conexión vive en páginas globales: «Salud de Meta» (`/conexiones/meta`), «Plantillas WhatsApp»,
  «Requisitos de Meta» y «Producción» están en «Herramientas» y se le muestran a negocios sin Meta.
- La configuración de cada conexión está regada: Google en `/calendario`, Wompi en `/habilidades/pack_payments`,
  chat web en Configuración y WhatsApp Web en `/conexiones/waweb`.
- El calendario ocupa 5 entradas (Conexión, Horario de atención, Tipos de cita, Bloqueos, Citas) y los bloqueos
  se crean en una página aparte del calendario.
- La ficha del agente ([HU-AOS-47](../SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md)) solo dice «Atiende en …»
  con los nombres de sus conexiones: no muestra rol, prioridad ni cuál es la principal, ni lleva a la ficha de cada una.

El informe del ciclo de pruebas [2026-10-13](../../11-pruebas/informes/ciclo-2026-10-13.md) tiene 7 fallas de
«diseño del shell» y varias notas de «no encuentro». La propuesta base está en
[arquitectura-informacion-panel.md](../../02-vision-y-decisiones/arquitectura-informacion-panel.md); el árbol v2
de esta spec la actualiza al lenguaje de D-35.

## Usuarios y contexto

- **Dueño del negocio**: entra a ver sus agentes, sus conversaciones y su agenda; no sabe qué es un pack ni un tenant.
- **Colaborador**: ve solo las secciones que su rol permite (RBAC por `section`, ADR-0047); nunca un 403 por diseño.
- **Master**: además ve Plataforma (Negocios, App de Meta, Pruebas; Pruebas también la ven los testers en test).
- **App móvil**: el cajón lateral del panel en la app (D-34) replica la misma lista ([HU-UX-11](hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md)).

## Por qué importa (valor empresarial)

El encargo pide un panel "práctico, entendible y guiado". Un dueño de pyme no sabe qué es un
"tenant" ni un "pack": si no entiende el menú, no configura sus agentes y no expande su plan. La
claridad del panel es lo que permite el autoservicio que escala el negocio. Con D-35 el cliente entra a
SolversHub **a ver su agente y su data**: el menú tiene que llevarlo ahí en un toque, no esconderlo entre 40 entradas.

## Alcance

| HU | Qué |
|---|---|
| [HU-UX-01](hu/HU-UX-01-adr-arquitectura-de-informacion.md) | ADR de arquitectura de información y glosario |
| [HU-UX-02](hu/HU-UX-02-menu-v2.md) | Menú v2 (≤ 12 entradas) con grupos por tarea y renombres, sin cambiar URLs |
| [HU-UX-03](hu/HU-UX-03-ayuda-contextual.md) | Ayuda contextual y lenguaje claro |
| [HU-UX-04](hu/HU-UX-04-estados-vacios-y-permisos.md) | Estados vacíos con acción y permisos coherentes |
| [HU-UX-05](hu/HU-UX-05-guias-por-habilidad.md) | Guías por habilidad y por preset |
| [HU-UX-06](hu/HU-UX-06-registro-desde-landing.md) | Registro directo desde la landing |
| [HU-UX-08](hu/HU-UX-08-agenda-unificada.md) | Agenda unificada: Calendario · Tipos de cita · Horario, con bloqueos sobre el calendario |
| [HU-UX-09](hu/HU-UX-09-ficha-de-conexion-por-tipo.md) | Ficha de conexión por tipo y enlace Agentes ↔ Conexiones en las dos direcciones |
| [HU-UX-10](hu/HU-UX-10-cobranza-y-ventas-en-pestanas.md) | Cobranza y Ventas como una entrada cada una, con pestañas |
| [HU-UX-11](hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md) | Cajón del panel en la app alineado con el menú v2 |

### Árbol del menú v2 (D-37)

```
Operación      Resumen · Conversaciones (pestaña Escalaciones) · Clientes (ex Leads)
Tu asistente   Agentes   lista → ficha del agente [Conversaciones · Tareas · Clientes y registros · Consumo y calidad · Conexiones · Superpoderes]
               Conexiones lista → ficha /conexiones/[id] con pestañas según el tipo
Negocio        Agenda    [Calendario · Tipos de cita · Horario]
               Ventas    Comercio [Resumen · Productos · Categorías · Promociones · Pedidos] · Suscripciones
               Cobranza  Resumen + pestañas agrupadas (Operación · Monitoreo · Seguridad)
Cuenta         Consumo y plan [Plan · Costos] · Equipo [Colaboradores] · Configuración [Negocio y cuenta · Mensajes fallidos (ex DLQ) · Habilidades (packs)]
Plataforma     (solo master) Negocios · App de Meta · Pruebas
```

- Son **11 entradas** de primer nivel en 4 grupos para un dueño con todos los packs (hoy son 40 en 8 grupos,
  contadas sobre `nav.ts` de `origin/main`, que ya incluye Agentes y Alta automática). Agenda, Ventas y Cobranza
  solo aparecen si el negocio tiene la habilidad; el grupo «Herramientas» desaparece.
- [HU-UX-02](hu/HU-UX-02-menu-v2.md) **solo reagrupa**: ninguna URL cambia. Las entradas que hoy son hermanas
  (Escalaciones, las páginas de Cobranza, Comercio y Calendario) pasan a pestañas sin mover su ruta. Las rutas
  cambian después, con las fichas y secciones de [HU-UX-08](hu/HU-UX-08-agenda-unificada.md),
  [HU-UX-09](hu/HU-UX-09-ficha-de-conexion-por-tipo.md) y [HU-UX-10](hu/HU-UX-10-cobranza-y-ventas-en-pestanas.md),
  que traen sus redirecciones.
- Lenguaje D-35: el agente es la unidad; sus capacidades son **Superpoderes** y su medición es **Calidad**
  (pestaña «Consumo y calidad» de la ficha). «Habilidades» queda solo para los packs, dentro de Configuración.
- Agentes y Conexiones son una relación de muchos a muchos (`ConnectionAgentInstance`: rol, prioridad, por
  defecto): no se anidan, se enlazan en las dos direcciones.

## Escenarios clave (Gherkin)

- **Menú corto.** Dado un dueño con todos los packs, cuando abre el panel, entonces ve como máximo 12 entradas de primer nivel y ninguna se llama «Herramientas».
- **Por tarea.** Dado el menú v2, cuando lo recorro, entonces veo los grupos Operación (Resumen, Conversaciones, Clientes), Tu asistente (Agentes, Conexiones), Negocio (Agenda, Ventas, Cobranza) y Cuenta (Consumo y plan, Equipo, Configuración), y Plataforma solo si soy master.
- **Ficha del agente.** Dado un agente publicado, cuando abro su ficha, entonces veo las pestañas Conversaciones, Tareas, Clientes y registros, Consumo y calidad, Conexiones y Superpoderes.
- **Agente → conexión.** Dado la pestaña Conexiones del agente, cuando elijo una conexión, entonces llego a la ficha de esa conexión.
- **Conexión → agente.** Dado la pestaña Agentes de una conexión, cuando elijo un agente, entonces llego a la ficha de ese agente.
- **Salud solo en Meta.** Dado una conexión de WhatsApp Web (QR), cuando abro su ficha, entonces veo Vinculación, Estado y Agentes, y no veo Salud, Plantillas ni Producción.
- **Agenda en una entrada.** Dado un negocio con agenda, cuando abro Agenda, entonces veo las pestañas Calendario, Tipos de cita y Horario, y puedo crear un bloqueo seleccionando un hueco del calendario.
- **Solo lo habilitado.** Dado un negocio sin cobranza, cuando abre el menú, entonces no aparece Cobranza.
- **Sin romper enlaces.** Dado un enlace guardado (`/escalaciones`, `/calendario/bloqueos`, `/conexiones/meta`), cuando lo abro, entonces llego a la misma página (el menú v2 no cambia URLs) o, si una HU posterior movió la ruta, a su pestaña nueva.
- **Glosario.** Dado el panel, cuando reviso los textos de usuario, entonces no aparecen «Tenant», «Plugin», «Costos LLM», «Leads» ni «DLQ».

## Decisiones

Opciones A/B/C del menú (por tarea, por habilidad o solo renombrar) en
[arquitectura-informacion-panel.md](../../02-vision-y-decisiones/arquitectura-informacion-panel.md#opciones).
**Recomendación: A (por tarea).** Estado: ✅ tomada ([D-37](../../02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto)),
con fichas por objeto y pestañas internas.

### D-SPEC-12-1 · Tour guiado

| Opción | Pros | Contras |
|---|---|---|
| **A. Tour propio liviano (5 pasos, con los componentes del panel)** | Sin dependencias; respeta `DESIGN.md` | Construirlo |
| B. Librería de tours | Rápido | Estilo ajeno y peso extra |

**Recomendación: A** (lo construye [HU-SH-06](../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md) y aquí se extiende). Estado: ⏳ pendiente.

## Fuera de alcance

- Construir el menú desde el manifiesto del backend ([HU-FWK-05](../SPEC-16-habilidades-como-plataforma/hu/HU-FWK-05-manifiesto-de-menu.md)): el menú v2 sigue en `nav.ts`.
- El hub de Meta del Hito 0B tal como lo pensaba [HU-CONN-08](../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md): lo reemplaza la ficha de conexión por tipo.
- Nuevas capacidades de backend, salvo el color o identificador del tipo de cita en `pack_calendar` si hace falta ([HU-UX-08](hu/HU-UX-08-agenda-unificada.md)).

## Métricas de éxito

- Entradas de primer nivel para un dueño con todos los packs: de 40 a 11 (meta ≤ 12).
- % de negocios que completan los primeros pasos en 24 h.
- Tickets de soporte y notas de prueba por "no encuentro X" a la mitad.

## Requerimientos cubiertos

REQ-UX-01, REQ-UX-02, REQ-UX-03, REQ-UX-12, REQ-UX-13, REQ-UX-14, REQ-UX-15, REQ-COMP-08.
