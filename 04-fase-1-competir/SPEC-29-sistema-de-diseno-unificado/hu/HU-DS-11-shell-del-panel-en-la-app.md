---
id: HU-DS-11
titulo: Shell del panel en la app con cajón lateral y tema oscuro
spec: SPEC-29
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, operacion]
req: [REQ-APP-11]
dependencias: [HU-DS-09]
skills: ["frontend-design", "/code-review"]
estado: terminada
---

# HU-DS-11 · Shell del panel en la app con cajón lateral y tema oscuro

> Estado SDD: Terminada el 2026-10-16 — apk #156, #157, #158 y #159 en `develop`; smoke en el OPPO en verde; OTA `preview` grupo `36bab8dd…`.

**ID:** HU-DS-11

**Título:** Shell del panel en la app con cajón lateral y tema oscuro

**Workstream:** App móvil

**Historia:** Como dueño o supervisor que usa la app quiero el mismo menú del panel web (hamburguesa y lista agrupada de secciones) y el tema oscuro del panel para moverme por el negocio desde el celular sin aprender otra navegación.

**Por qué importa (valor empresarial):** Hoy el panel en la app tiene 8 pestañas truncadas, una lista «Más» que no navega y ningún toggle de tema: probarlo es una pérdida de tiempo. Con el cajón del panel web y el tema oscuro, la app pasa de «réplica» a herramienta diaria del dueño y se puede probar de verdad.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-11

**Dependencias:** [HU-DS-09](HU-DS-09-kit-de-componentes-app.md)

**Criterios de aceptación (Gherkin):**
- **Cajón por permisos.** Dado un dueño con Cobranza y Comercio activos, cuando abre el panel en la app y toca la hamburguesa, entonces ve los grupos Operación, Cobranza, Comercio, Configuración y Herramientas con las secciones de sus permisos, y no ve Calendario ni Negocio.
- **Packs plegados.** Dado el cajón recién abierto, cuando mira los grupos, entonces Cobranza, Comercio y Calendario están plegados y Operación desplegado, como en el sidebar del panel web.
- **Sección abre pestaña.** Dado el cajón abierto, cuando toca Cobranza › Gestores, entonces el cajón se cierra y la pantalla de Cobranza se abre en la pestaña Gestores con el header del panel arriba.
- **Tema oscuro por defecto.** Dado un usuario que nunca eligió tema, cuando abre la app, entonces arranca en oscuro; cuando toca el toggle del header o del cajón, entonces pasa a claro y la elección persiste al reabrir.
- **Campo intacto.** Dado un gestor, cuando entra a su cartera, entonces ve las mismas vistas y el mismo menú lateral de siempre, en oscuro con el navy de los tokens.
- **Push y Búsqueda navegan.** Dado un push de escalación o un resultado de Búsqueda, cuando se toca, entonces la app abre el módulo y la pestaña correspondientes.

**Evidencia / Definición de Terminado:**
- Capturas claro/oscuro del header, el cajón y una pantalla por módulo desde el OPPO; smoke Maestro `e2e/smoke-panel-dueno.yaml` y `e2e/smoke-cobranza.yaml` en verde.
- Tests de navegación por rol (owner, master, colaborador sin permisos) y gate del campo (`MenuLateral.test.tsx` y `menu-campo.test.tsx` sin cambios).
- ADR-APP-07 enmendado y ADR-APP-02 con el árbol real.
- OTA gradual 10/50/100 con la nota del tema oscuro.

**Riesgos/Notas:**
- Sin dependencias nativas (nada de `@react-navigation/drawer`): el `Drawer` del kit es `Animated` + `Pressable`, así que sale por EAS Update con el runtime actual.
- El campo ([HU-DS-10](HU-DS-10-cobranza-de-campo-con-el-kit.md)) solo cambia en que arranca en oscuro (D-SPEC-29-6 para vistas y flujo).
- El Resumen móvil por rol es [HU-DS-13](HU-DS-13-resumen-movil-por-rol.md). TanStack Query (ADR-APP-04) sigue sin instalarse: se recomienda enmendar el ADR.
- Código: apk #156, #157, #158 y #159 (relanzamiento a `develop`). OTA publicada el 2026-10-16.
