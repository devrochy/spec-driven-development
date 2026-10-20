---
id: HU-DS-04
titulo: Shell adaptativo del panel
spec: SPEC-29
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-UX-10, REQ-UX-06]
dependencias: [HU-DS-03, HU-UI-03]
skills: ["frontend-design", "panel-ui", "built-in-browser"]
estado: terminada
---

# HU-DS-04 · Shell adaptativo del panel

> Estado SDD: Terminada — implementada 2026-10-11.

**ID:** HU-DS-04

**Título:** Shell adaptativo del panel

**Workstream:** UX/Onboarding

**Historia:** Como dueño u operador quiero un menú que se pliegue a íconos, recuerde cómo lo dejé y me muestre dónde estoy con migas y pestañas para moverme por más de 40 secciones sin perderme.

**Por qué importa (valor empresarial):** El menú es lo primero que se ve en una demo y lo que más se usa en el día. Plegarlo da espacio a tablas y bandeja; las migas y pestañas cortan los clics para llegar a una sección hermana.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-10, REQ-UX-06

**Dependencias:** [HU-DS-03](HU-DS-03-kit-de-componentes-panel.md), [HU-UI-03](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md)

**Criterios de aceptación (Gherkin):**
- **Plegar y recordar.** Dado un escritorio de 1280 px, cuando pliego la barra lateral y recargo, entonces sigue en 72 px desde el primer render (sin salto de layout).
- **Por defecto según el ancho.** Dado un usuario sin preferencia, cuando abre el panel a 1024 px, entonces la barra está plegada; a 1440 px, expandida; a 375 px, es un cajón.
- **Plegada usable.** Dado la barra plegada, cuando paso el puntero o el foco por un ícono, entonces veo su nombre en un tooltip, y un grupo con hijos abre un menú flotante navegable con flechas.
- **Migas.** Dado que estoy en el detalle de una cartera, cuando miro el encabezado, entonces veo "Ventas y cobros › Cobranza › Carteras › <nombre>" con `aria-current` en la última.
- **Pestañas de sección.** Dado la sección Citas de Agenda, cuando la abro, entonces el encabezado muestra Citas, Tipos, Bloqueos y Horario como enlaces con `aria-current` en la actual.
- **Activo visible.** Dado cualquier página, cuando miro la barra (expandida o plegada), entonces el ítem o grupo activo se distingue sin depender solo del color.

**Evidencia / Definición de Terminado:**
- Capturas a 375, 1024 y 1440 px en claro y oscuro.
- Test del cálculo de migas desde `nav.ts`.
- ADR-0003 del panel (shell, cookie `panel_sidebar` y atajos).

**Riesgos/Notas:**
- Entra detrás de `PANEL_SHELL_V2` hasta la prueba con 5 usuarios.
- Requiere íconos propios por sección de Cobranza (hoy 12 de 14 usan `HandCoins`).
- Si [HU-UX-02](../../SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) cambia `nav.ts` al mismo tiempo, se mergea primero [HU-UX-02](../../SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md).
