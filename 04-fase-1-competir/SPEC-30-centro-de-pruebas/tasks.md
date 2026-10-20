# SPEC-30 · Tareas

| Orden | HU | Título | Tamaño | Depende de |
|---|---|---|---|---|
| 1 | [HU-QA-01](hu/HU-QA-01-modelo-y-api-de-pruebas.md) | Modelo y API de pruebas | M | — |
| 2 | [HU-QA-02](hu/HU-QA-02-catalogo-versionado-desde-docs.md) | Catálogo versionado desde docs | S | [HU-QA-01](hu/HU-QA-01-modelo-y-api-de-pruebas.md) |
| 3 | [HU-QA-03](hu/HU-QA-03-seccion-pruebas-en-el-panel.md) | Sección Pruebas en el panel | M | [HU-QA-01](hu/HU-QA-01-modelo-y-api-de-pruebas.md) |
| 4 | [HU-QA-04](hu/HU-QA-04-rol-tester-e-invitaciones.md) | Rol tester e invitaciones | M | [HU-QA-03](hu/HU-QA-03-seccion-pruebas-en-el-panel.md) |
| 5 | [HU-QA-05](hu/HU-QA-05-migrar-desde-el-artifact.md) | Migrar resultados desde el artifact | S | [HU-QA-02](hu/HU-QA-02-catalogo-versionado-desde-docs.md), [HU-QA-03](hu/HU-QA-03-seccion-pruebas-en-el-panel.md) |
| 6 | [HU-QA-06](hu/HU-QA-06-catalogo-historico-del-proyecto.md) | Catálogo histórico del proyecto | L | — |
| 7 | [HU-QA-07](hu/HU-QA-07-datos-de-prueba.md) | Datos de prueba propios y guía de datos | M | [HU-QA-04](hu/HU-QA-04-rol-tester-e-invitaciones.md) |
| 8 | [HU-QA-08](hu/HU-QA-08-pruebas-por-entorno-y-seccion.md) | Pruebas por entorno y sección | S | [HU-QA-06](hu/HU-QA-06-catalogo-historico-del-proyecto.md) |
| 9 | [HU-QA-09](hu/HU-QA-09-datos-de-prueba-para-el-agent-os.md) | Datos de prueba listos para el Agent OS | M | [HU-QA-07](hu/HU-QA-07-datos-de-prueba.md) |

**Esfuerzo**: 5 M + 3 S + 1 L ≈ 32,5 días-persona sin IA.

**Orden de ejecución acordado (2026-10-13):** docs (esta spec y el esquema v2 del catálogo) → catálogo histórico
([HU-QA-06](hu/HU-QA-06-catalogo-historico-del-proyecto.md), en 2 o 3 PRs, en paralelo con el código) → agent-core con [HU-QA-01](hu/HU-QA-01-modelo-y-api-de-pruebas.md) y [HU-QA-02](hu/HU-QA-02-catalogo-versionado-desde-docs.md) →
agent-core con la parte de backend de [HU-QA-04](hu/HU-QA-04-rol-tester-e-invitaciones.md) → panel con [HU-QA-03](hu/HU-QA-03-seccion-pruebas-en-el-panel.md) y la parte de panel de [HU-QA-04](hu/HU-QA-04-rol-tester-e-invitaciones.md) → deploy a test y
prueba con una cuenta externa → [HU-QA-05](hu/HU-QA-05-migrar-desde-el-artifact.md).

Mientras se construye, el registro sigue en el artifact «Camino a producción» y el catálogo en
[11-pruebas/catalogo.yaml](../../11-pruebas/catalogo.yaml).
