---
id: HU-UX-20
titulo: APK con búsqueda en Negocios, inicio sin conexión y notas de cartera
spec: SPEC-31
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-UX-23]
dependencias: [HU-UX-11]
skills: ["frontend-design"]
estado: borrador
---

# HU-UX-20 · APK con búsqueda en Negocios, inicio sin conexión y notas de cartera

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-UX-20

**Título:** APK con búsqueda en Negocios, inicio sin conexión y notas de cartera

**Workstream:** App móvil

**Historia:** Como master o dueño en la app quiero buscar un negocio, ver el Inicio con esqueletos de carga y con lo último guardado si me quedo sin conexión, y agregar notas a una cartera, para usar la app como el panel.

**Por qué importa (valor empresarial):** Son las cuatro fallas de la app que el dueño anotó en el ciclo. La app es la herramienta del día a día en la calle; un Inicio en blanco sin conexión se lee como que la app no funciona.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-23

**Dependencias:** [HU-UX-11](../../SPEC-12-arquitectura-de-informacion/hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md)

**Criterios de aceptación (Gherkin):**
- **Buscar un negocio.** Dado Plataforma › Negocios en la app, cuando escribo parte del nombre, entonces la lista se filtra.
- **Esqueletos.** Dado el Inicio, cuando carga, entonces veo bloques de precarga en lugar de un círculo girando.
- **Sin conexión.** Dado que abrí el Inicio antes y me quedé sin conexión, cuando lo abro de nuevo, entonces veo lo último guardado con un aviso de que puede estar desactualizado.
- **Notas de cartera.** Dado una cartera en la vista del dueño, cuando agrego una nota, entonces queda guardada y la veo en el detalle.

**Evidencia / Definición de Terminado:**
- `modules/herramientas/screens/HerramientasScreen.tsx` con buscador que pasa `q` a `cargarNegocios`.
- `modules/dashboard/screens/DashboardScreen.tsx` con `shared/ui/Skeleton.tsx`, caché local y `shared/ui/SyncStatus.tsx`.
- `modules/cobranza-admin/screens/CarteraDetalleScreen.tsx` con notas sobre `/pack/cobranza/portfolios/{id}/notes`.
- Tests de jest; sale por OTA si la huella sigue igual; smoke en el teléfono de pruebas.

**Riesgos/Notas:**
- Notas que lo motivan: ítem 27 del [inventario de SPEC-31](../design.md#inventario).
