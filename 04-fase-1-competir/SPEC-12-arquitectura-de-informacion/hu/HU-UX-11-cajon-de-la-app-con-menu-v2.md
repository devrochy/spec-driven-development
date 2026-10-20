---
id: HU-UX-11
titulo: Cajón del panel en la app alineado con el menú v2
spec: SPEC-12
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: S
impacto: [operacion]
req: [REQ-UX-15]
dependencias: [HU-UX-02, HU-DS-11]
skills: ["frontend-design", "built-in-browser"]
estado: borrador
---

# HU-UX-11 · Cajón del panel en la app alineado con el menú v2

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-12](../spec.md). Nace de [D-37](../../../02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto) (2026-10-19) y mantiene [D-34](../../../02-vision-y-decisiones/decisiones.md#d-34--panel-en-la-app-con-cajón-lateral-y-tema-oscuro-por-defecto-reemplaza-a-d-spec-29-5) (el cajón replica la lista del panel web).

**ID:** HU-UX-11

**Título:** Cajón del panel en la app alineado con el menú v2

**Workstream:** App móvil

**Historia:** Como dueño que revisa su negocio desde el celular quiero que el cajón de la app tenga los mismos grupos y nombres que el menú del panel web, para no aprender dos menús.

**Por qué importa (valor empresarial):** D-34 eligió el cajón porque da paridad exacta con el panel web. Si el panel cambia al menú v2 y la app no, se rompe esa paridad y el soporte tiene que explicar dos mapas.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-UX-15

**Dependencias:** [HU-UX-02](HU-UX-02-menu-v2.md), [HU-DS-11](../../SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-11-shell-del-panel-en-la-app.md)

**Criterios de aceptación (Gherkin):**
- **Misma lista.** Dado el menú v2 del panel web, cuando abro el cajón de la app como dueño, entonces veo las mismas entradas de primer nivel, en el mismo orden y con los mismos nombres.
- **Sin Herramientas.** Dado el cajón, cuando lo recorro, entonces no existe el módulo «Herramientas» y sus secciones están donde las puso el menú v2 (Conexiones, Configuración o Plataforma).
- **Pestaña interna.** Dado una entrada con pestañas (Cobranza, Ventas, Agenda), cuando la toco, entonces se abre el módulo en su primera pestaña permitida para mi rol.
- **Permisos.** Dado un colaborador sin una sección, cuando abre el cajón, entonces esa entrada no aparece.

**Evidencia / Definición de Terminado:**
- `solvershub-apk/src/navigation/menu-panel.ts` (`ModuloPanel`, `ORDEN_MODULOS` y la lista de secciones) al día con el menú v2; `menu-panel.test.ts` y `CajonPanel.test.tsx` al día.
- Enmienda de ADR-APP-07 si cambia la convención de módulos; OTA al canal de preview y capturas del cajón en un Android real.

**Riesgos/Notas:**
- Las pantallas de Agentes y de las fichas de conexión aún no existen en la app: el cajón las abre en el panel web embebido o las muestra como próximas, según lo que ya haga el shell de [HU-DS-11](../../SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-11-shell-del-panel-en-la-app.md).
- La app de campo de cobranza no cambia (D-SPEC-29-6).
