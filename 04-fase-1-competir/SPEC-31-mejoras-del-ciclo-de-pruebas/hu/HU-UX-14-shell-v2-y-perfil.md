---
id: HU-UX-14
titulo: Shell v2 y perfil del usuario
spec: SPEC-31
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, operacion]
req: [REQ-UX-17]
dependencias: [HU-UX-12]
skills: ["panel-ui", "frontend-design", "backend-design:auth-and-authorization"]
estado: borrador
---

# HU-UX-14 · Shell v2 y perfil del usuario

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-UX-14

**Título:** Shell v2 y perfil del usuario

**Workstream:** UX/Onboarding

**Historia:** Como usuario del panel quiero plegar la barra desde el logo, tener mi avatar con un menú al pie (perfil, tema, cerrar sesión), ver las pestañas arriba del título y los indicadores primero en el Resumen, para moverme como en cualquier aplicación moderna.

**Por qué importa (valor empresarial):** El dueño pidió este shell en cuatro pruebas distintas. Es lo primero que ve un cliente en una demo; además hoy no existe una página para cambiar el nombre o la contraseña propios.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-17

**Dependencias:** [HU-UX-12](HU-UX-12-arreglos-rapidos-del-ciclo.md)

**Criterios de aceptación (Gherkin):**
- **Plegar junto al logo.** Dado el panel en escritorio, cuando hago clic en el ícono junto al logo, entonces la barra se pliega o se expande y recuerda mi preferencia.
- **Menú del usuario.** Dado el pie de la barra lateral, cuando hago clic en mi avatar, entonces veo Perfil, Tema claro u oscuro y Cerrar sesión.
- **Perfil.** Dado mi página de perfil, cuando cambio mi nombre o mi contraseña (escribiendo la actual), entonces se guarda y las otras sesiones abiertas se cierran si cambié la contraseña.
- **Pestañas arriba.** Dado una sección con pestañas como Cobranza, cuando entro a una ficha, entonces las pestañas aparecen arriba del título.
- **Resumen primero.** Dado el Resumen, cuando lo abro, entonces las tarjetas de indicadores aparecen antes de la bienvenida.
- **Acciones con íconos.** Dado Negocios o Equipo, cuando miro la columna de acciones, entonces veo botones de íconos con su nombre al pasar el puntero.

**Evidencia / Definición de Terminado:**
- `components/shell/sidebar.tsx`: botón de plegar en el encabezado y bloque fijo al pie con `ui/avatar.tsx` y `ui/dropdown-menu.tsx`; `components/shell/topbar.tsx` queda con la búsqueda y el negocio activo.
- Página `/perfil` con `components/templates/settings-page.tsx`; core: `PATCH /admin/me` y `POST /admin/me/password` con la contraseña actual y revocación de sesiones (ADR-0136), con tests.
- `components/ui/page-header.tsx` con las pestañas antes del título; `dashboard/page.tsx` con las tarjetas primero.
- Negocios y Equipo con `ui/icon-action.tsx`.
- APK: el mismo bloque de usuario en `CajonPanel`.

**Riesgos/Notas:**
- Notas que lo motivan: ítems 11 a 15 del [inventario de SPEC-31](../design.md#inventario).
