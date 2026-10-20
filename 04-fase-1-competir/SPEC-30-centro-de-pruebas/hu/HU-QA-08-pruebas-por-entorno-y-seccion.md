---
id: HU-QA-08
titulo: Pruebas por entorno y sección
spec: SPEC-30
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: S
impacto: ["confianza", "operacion"]
req: [REQ-ARCH-22]
dependencias: [HU-QA-06]
skills: ["panel-ui"]
estado: en-curso
---

# HU-QA-08 · Pruebas por entorno y sección

> Estado SDD: En curso — pedido del dueño del 2026-10-13 sobre [SPEC-30](../spec.md).

**ID:** HU-QA-08

**Título:** Pruebas por entorno y sección

**Workstream:** Arquitectura/Prod

**Historia:** Como tester quiero ver las pruebas clasificadas por entorno (panel o APK, y también WhatsApp, Web y API) y por la sección donde se ejecutan, para correr de corrido todo lo de una pantalla o todo lo del celular.

**Por qué importa (valor empresarial):** El catálogo histórico tiene 214 pruebas en unos 70 grupos que mezclan módulo y plataforma. Agrupar por dónde se ejecuta reduce los cambios de contexto (celular, panel, WhatsApp) y deja ver qué sección quedó sin probar.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-ARCH-22

**Dependencias:** [HU-QA-06](HU-QA-06-catalogo-historico-del-proyecto.md)

**Criterios de aceptación (Gherkin):**
- **Lista por entorno y sección.** Dado el catálogo v6, cuando el tester abre Pruebas › Ejecutar, entonces la lista lateral agrupa por entorno (Panel, APK, WhatsApp, Web, API) y dentro por sección, en el orden del menú del panel y de las pantallas de la APK, con el avance de cada entorno.
- **Filtros.** Dado la lista, cuando el tester filtra por entorno o por sección, entonces solo quedan esas pruebas y el filtro se recuerda al volver.
- **Catálogo válido.** Dado un catálogo v6, cuando una prueba no trae `entorno` y `area`, o trae una sección que no existe en su entorno, entonces `regenerar.py --check` falla.

**Evidencia / Definición de Terminado:**
- Catálogo v6 con `entorno` y `area` en las 214 pruebas; validación en `regenerar.py`; tests de la lista del panel; recorrido en el navegador.

**Riesgos/Notas:**
- Las secciones del panel siguen su menú (`components/shell/nav.ts`); si el menú cambia, se actualiza `QA_AREAS` en `herramientas/regenerar.py` en el mismo PR.
