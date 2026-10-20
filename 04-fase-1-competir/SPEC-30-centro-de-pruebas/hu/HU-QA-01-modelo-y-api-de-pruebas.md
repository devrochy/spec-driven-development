---
id: HU-QA-01
titulo: Modelo y API de pruebas
spec: SPEC-30
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: ["confianza", "operacion"]
req: [REQ-ARCH-22]
dependencias: []
skills: ["db-migration", "backend-design:data-modeling-discipline", "backend-design:auth-and-authorization", "auditor-multitenant"]
estado: terminada
---

# HU-QA-01 · Modelo y API de pruebas

> Estado SDD: Lista para ejecutar — [SPEC-30](../spec.md) en Diseño aprobado (D-33).

**ID:** HU-QA-01

**Título:** Modelo y API de pruebas

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de la plataforma quiero que el catálogo, los ciclos, las ejecuciones de cada tester (pasos, notas y capturas) y sus informes se guarden en agent-core para no depender de una página externa.

**Por qué importa (valor empresarial):** Es la base del centro de pruebas: sin datos propios no hay historial confiable, evidencia ni informe por tester.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-22

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Paso con historial.** Dado un tester con su ejecución en curso, cuando marca el paso 2 de una prueba como «Falla» con una nota, entonces `qa_step_results` guarda el paso, la prueba queda en falla y `qa_events` registra el cambio con su `admin_id` y hora.
- **Captura.** Dado un paso de mi ejecución en curso, cuando subo una imagen png de 300 KB, entonces queda en `TENANTS_ROOT/.plataforma/pruebas/<run_id>/` con nombre `uuid4` y solo se sirve con sesión; un archivo de 6 MB o un `.exe` se rechaza con 422.
- **Informe.** Dado un tester con su ejecución en curso, cuando la envía, entonces queda `enviada` con el informe congelado, ya no acepta cambios (409) y se envía un correo a los masters activos con el enlace.
- **Consolidación.** Dados dos testers en el mismo ciclo, uno con la prueba en OK y otro en Falla, cuando el dueño pide el catálogo, entonces la prueba aparece en Falla.
- **Cerrar ciclo.** Dado un ciclo abierto con ejecuciones, cuando el dueño lo cierra, entonces queda `cerrado_en` con el resumen y se abre uno nuevo con las pruebas sin correr.
- **Sin acceso de negocio.** Dado un colaborador de un negocio, cuando llama a `/admin/qa/catalog`, entonces recibe 403.

**Evidencia / Definición de Terminado:**
- Migración con tablas de sistema documentadas y ADR del centro de pruebas; tests de servicio (consolidación, progreso, informe) y de API (permisos, ciclo, ejecución, captura, historial); revisión del auditor multitenant.

**Riesgos/Notas:**
- Tablas sin `tenant_id` (como `admins`): el auditor tiene que confirmar que ninguna query de negocio las toca.
- Las capturas usan el volumen persistente `TENANTS_ROOT` (el mismo de las evidencias de cobranza); su limpieza queda como punto de producción.
