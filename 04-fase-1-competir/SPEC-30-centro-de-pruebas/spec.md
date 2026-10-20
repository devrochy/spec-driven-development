# SPEC-30 · Centro de pruebas en el panel

> Estado SDD: Diseño aprobado (2026-10-13, D-33) · Fase 1 · Workstream Arquitectura/Prod · Dueño: Robinson Aguilar
> · Creada el 2026-10-12

## Problema

Las pruebas de cada requerimiento viven repartidas: el plan de pruebas del panel anterior a SDD
(`solvershub-comercial/PLAN-DE-PRUEBAS.md`), la guía del 0A, el guion de la prueba con usuarios de
[SPEC-29](../SPEC-29-sistema-de-diseno-unificado/spec.md), los criterios Gherkin de cada HU, notas en la bitácora y, desde el 2026-10-12, el
artifact «Camino a producción». El artifact sirve hoy, pero solo pueden marcar resultados personas de la organización
en claude.ai o editores invitados por correo, no guarda capturas, no tiene un informe por tester y no hay una forma
de que testers externos (clientes piloto, testers contratados) prueben el panel con su propia cuenta.

## Usuarios y contexto

| Usuario | Qué necesita |
|---|---|
| Dueño (master) | Invitar testers, abrir y cerrar ciclos, leer los informes y ver qué falta para pasar a producción |
| Tester interno o externo | Entrar al panel de **test** con permisos de master (menos Colaboradores), ejecutar las pruebas paso a paso, adjuntar capturas, ver su avance y enviar su informe |
| Claude (sesiones de trabajo) | Agregar las pruebas de cada HU al catálogo y leer los resultados y los informes de un ciclo |

## Por qué importa (valor empresarial)

Cada release lleva cambios en panel, app y backend. Sin un registro de qué se probó, por quién y con qué resultado,
un paso a producción depende de la memoria del dueño. Un centro de pruebas en el propio panel hace el control
repetible, deja evidencia (con capturas) por ciclo y por tester, y permite sumar testers sin tocar producción.

## Alcance

| HU | Qué entrega | Repos |
|---|---|---|
| [HU-QA-01](hu/HU-QA-01-modelo-y-api-de-pruebas.md) | Tablas de catálogo, ciclos, ejecuciones por tester, pasos, capturas e historial, y la API | agent-core |
| [HU-QA-02](hu/HU-QA-02-catalogo-versionado-desde-docs.md) | Importar `11-pruebas/catalogo.yaml` de solvershub-docs como versión del catálogo | agent-core |
| [HU-QA-03](hu/HU-QA-03-seccion-pruebas-en-el-panel.md) | Sección Plataforma › Pruebas: lista lateral, ejecución paso a paso, progreso, informe, ciclos y checklists | panel |
| [HU-QA-04](hu/HU-QA-04-rol-tester-e-invitaciones.md) | Rol tester (master en la operación, dueño en Colaboradores, solo en test) e invitaciones por correo | agent-core + panel |
| [HU-QA-05](hu/HU-QA-05-migrar-desde-el-artifact.md) | Migrar los resultados del artifact y cerrar su primer ciclo en el panel | agent-core |
| [HU-QA-06](hu/HU-QA-06-catalogo-historico-del-proyecto.md) | Catálogo histórico: todas las pruebas manuales del proyecto desde el inicio, con pasos y resultado esperado | docs |
| [HU-QA-07](hu/HU-QA-07-datos-de-prueba.md) | Datos de prueba propios con un botón (negocio, datos de ejemplo y cuentas por tester) y guía de datos externos | agent-core + panel + docs |
| [HU-QA-08](hu/HU-QA-08-pruebas-por-entorno-y-seccion.md) | Pruebas clasificadas por entorno (Panel, APK, WhatsApp, Web, API) y por sección, con filtros | agent-core + panel + docs |

## Escenarios clave (Gherkin)

- **Ejecución paso a paso.** Dado un tester en Pruebas, cuando elige una prueba de la lista lateral y aprueba sus
  pasos uno a uno, entonces cada paso queda guardado al instante y su progreso sube.
- **Falla con evidencia.** Dado un tester en el paso 2 de una prueba, cuando lo marca «Falla», escribe una nota y pega
  una captura, entonces el paso queda en falla con la captura y el historial muestra su nombre y la hora.
- **Informe.** Dado un tester con su ejecución avanzada, cuando pulsa «Enviar informe» y confirma, entonces la
  ejecución queda en solo lectura, el dueño recibe un correo con el enlace y el informe se puede descargar.
- **Tester en Colaboradores.** Dado un tester en test con un negocio activo, cuando abre Colaboradores, entonces
  gestiona las cuentas de ese negocio como su dueño, pero no puede crear masters ni tocar cuentas de plataforma.
- **Solo en test.** Dada producción sin la variable `QA_TESTERS_ENABLED`, cuando una cuenta tester intenta entrar,
  entonces el login falla.
- **Ciclo nuevo.** Dado el ciclo actual, cuando el dueño lo cierra y abre «Release 2026-11», entonces el cerrado queda
  como foto fija y las pruebas del nuevo arrancan sin correr.
- **Catálogo versionado.** Dado un PR mergeado que cambia `catalogo.yaml`, cuando se importa, entonces el panel
  muestra la versión nueva y los ciclos cerrados conservan la versión con la que se corrieron.

## Decisiones

### D-SPEC-30-1 · Dónde vive el catálogo de pruebas

| Opción | Pros | Contras |
|---|---|---|
| A. Archivo YAML en solvershub-docs, importado al panel | Versionado con git, se revisa en el mismo PR de la HU, Claude lo edita sin tocar la base | Cambiar una prueba pide un PR |
| B. Editable solo en el panel | Rápido para el dueño | Se pierde el historial de git y el vínculo con la HU |
| C. YAML como fuente, más notas editables en el panel | Lo mejor de ambos | Dos lugares que explicar |

**Recomendación: A**, elegida por el dueño el 2026-10-13. El catálogo es parte del requerimiento y se versiona con
él; los resultados viven en el panel.

### D-SPEC-30-2 · Qué puede hacer un tester y dónde existe

| Opción | Pros | Contras |
|---|---|---|
| A. Rol `tester` = master en la operación y dueño del negocio activo en Colaboradores, **solo en test** (variable `QA_TESTERS_ENABLED`) | Puede probar de verdad todo el panel, Colaboradores incluida, y la app; no gestiona cuentas de plataforma; en producción no existe | Ve todos los negocios de test; hay que revisar cada chequeo de master; las cuentas que cree en test quedan después de revocarlo |
| B. Rol `tester` con acceso solo a la sección Pruebas | Riesgo mínimo | No puede ejecutar las pruebas del panel, que es lo que se pide |
| C. Rol `tester` igual a master, también en producción | Sirve para pruebas en vivo | Un externo vería datos reales de clientes (riesgo legal y de privacidad) |

**Recomendación: A**, elegida por el dueño el 2026-10-13 ("que puedan ejecutar las acciones de un master pero el
único acceso que no pueden tener es el de colaboradores"; "solo en test"). El mismo día el dueño pidió habilitar
también Colaboradores "para que pueda hacer las pruebas de esta sección": ahí el tester actúa como **dueño del
negocio activo**, no como master. Gestionar cuentas de plataforma (crear masters, tocar cuentas de master o tester,
vincular entre negocios, gestionar testers) sigue siendo solo de master, y una cuenta tester no la puede tocar un
owner.

### D-SPEC-30-3 · Si las pruebas son de la plataforma o de cada negocio

| Opción | Pros | Contras |
|---|---|---|
| A. De la plataforma (master y testers) | Una sola lista por release; simple | Un negocio cliente no puede usarla para sus propias pruebas |
| B. Por negocio | Cada cliente probaría su asistente | Multiplica catálogos; no es lo que se pidió |

**Recomendación: A**, elegida por el dueño el 2026-10-13. Si un cliente pide pruebas propias, es otra spec.

### D-SPEC-30-4 · Evidencia de cada prueba

| Opción | Pros | Contras |
|---|---|---|
| A. Nota de texto con enlaces | Rápido, sin almacenamiento nuevo | Las capturas quedan fuera del panel |
| B. Nota y capturas adjuntas por paso | Todo en un lugar; el informe trae la evidencia | Almacenamiento y límites nuevos |

**Recomendación: A** en el borrador; el dueño eligió **B** el 2026-10-13. Las capturas (jpeg, png, webp o pdf, hasta
5 MB) se guardan en el volumen persistente `TENANTS_ROOT` bajo `.plataforma/pruebas/`, el mismo que ya guarda las
evidencias de cobranza, así que no hace falta un bucket nuevo.

### D-SPEC-30-5 · Cómo se registran las ejecuciones y el informe

| Opción | Pros | Contras |
|---|---|---|
| A. Una ejecución por tester y ciclo, con informe propio que se envía al dueño (panel + correo + descarga) | Cada informe es de una persona; el ciclo consolida a todos | Más tablas |
| B. Un solo resultado compartido por prueba | Simple | El último que marca pisa al anterior; no hay informe por persona |

**Recomendación: A**, elegida por el dueño el 2026-10-13. El ciclo muestra una prueba como Falla si algún tester la
falló, Bloqueada si alguno quedó bloqueado, OK si alguno la aprobó, y Sin correr si nadie la corrió. Al enviar el
informe la ejecución queda en solo lectura, llega un correo a los masters con el enlace y el informe se puede
imprimir a PDF o descargar en Markdown.

### D-SPEC-30-6 · Cómo consigue el tester los datos para probar

| Opción | Pros | Contras |
|---|---|---|
| A. Botón «Preparar mis datos»: negocio de prueba propio con datos de ejemplo y cuentas generadas | Cada tester tiene lo suyo, sin pedir contraseñas ni pisarse | Un negocio por tester en test que hay que limpiar |
| B. Guía de datos: qué es cada dato y cómo conseguirlo | Sirve para lo externo (Wompi, Meta, correo) | Las cuentas siguen dependiendo del dueño |
| C. Cofre de credenciales compartidas en el panel | Rápido | Todos usan las mismas cuentas y se pisan los datos |

**Recomendación: A + B**, elegida por el dueño el 2026-10-13: el botón para lo que se puede generar y la guía para lo
externo. Las cuentas demo (master@demo.test, dueno-a@demo.test, gestor@demo.test) quedan para el equipo interno.

## Fuera de alcance

- Pruebas automáticas (E2E, evals): siguen en sus CI; el centro registra el resultado manual.
- Pruebas de cada negocio cliente (D-SPEC-30-3).
- Rol tester en producción (D-SPEC-30-2).
- Pestaña «Prueba con usuarios» en el panel: sigue en el artifact hasta [HU-QA-05](hu/HU-QA-05-migrar-desde-el-artifact.md).
- Limpieza automática de capturas viejas: queda como punto de producción en el catálogo.

## Métricas de éxito

| Métrica | Meta | Cómo se mide |
|---|---|---|
| Release con ciclo cerrado | 100 % de los pasos a producción con un ciclo cerrado y sin pruebas en «Falla» | Ciclos del panel |
| Tester sin gestión de cuentas | 0 rutas de colaboradores, invitaciones o testers accesibles para el rol tester | Matriz de permisos en tests + revisión de seguridad |
| Rol tester fuera de producción | Login de tester rechazado sin `QA_TESTERS_ENABLED` | Test + checklist de paso a producción |
| Catálogo al día | Cada HU que cambia comportamiento toca `catalogo.yaml` en su PR | Revisión de PRs de docs |

## Requerimientos cubiertos

REQ-ARCH-22.
