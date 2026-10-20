---
id: HU-QA-09
titulo: Datos de prueba listos para el Agent OS
spec: SPEC-30
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, calidad_ia]
req: [REQ-ARCH-22]
dependencias: [HU-QA-07]
skills: ["backend-design:idempotency-and-side-effects", "panel-ui", "auditor-multitenant"]
estado: terminada
---

# HU-QA-09 · Datos de prueba listos para el Agent OS

> Estado SDD: Terminada (registro tardío, 2026-10-19). El código se mergeó antes de tener su archivo de HU: agent-core #478 (adenda de ADR-0135) y panel #83. Se escribe al poner al día los estados con [D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas).

**ID:** HU-QA-09

**Título:** Datos de prueba listos para el Agent OS

**Workstream:** Arquitectura/Prod

**Historia:** Como tester quiero que «Preparar mis datos» deje mi negocio de prueba listo para probar el Agent OS (chat web, agentes, preset y release), para correr las pruebas de Agentes sin pedirle nada a nadie.

**Por qué importa (valor empresarial):** Las pruebas del Agent OS del catálogo v7 no se podían correr sin preparar a mano conexiones, agentes y releases. Con un botón cualquier tester las corre, y el ciclo de pruebas mide el producto y no la preparación.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-22

**Dependencias:** [HU-QA-07](HU-QA-07-datos-de-prueba.md)

**Criterios de aceptación (Gherkin):**
- **Primera vez.** Dado un tester sin datos, cuando pulsa «Preparar mis datos», entonces recibe sus contraseñas y su negocio `qa-` queda con chat web activo, agentes de ventas y agenda, preset v2 aplicado y un release promovido en cada conexión.
- **Volver a pulsar.** Dado un tester con los datos listos, cuando pulsa de nuevo («Actualizar mis datos»), entonces responde sin contraseñas, pone al día el Agent OS y no duplica nada.
- **Solo su negocio.** Dado otro negocio que no es el `qa-` del tester, cuando se intenta preparar, entonces no se toca.

**Evidencia / Definición de Terminado:**
- agent-core #478: `POST /api/v1/admin/qa/datos` con `core/qa/datos_aos.py` (chat web, backfills, migración a v3, preset v2, release y banderas), solo con `QA_TESTERS_ENABLED` y `AOS_CONNECTION_ROUTING`; 201 la primera vez y 200 idempotente después.
- panel #83: «Actualizar mis datos» y el bloque del Agent OS en Plataforma › Pruebas › Datos de prueba.

**Riesgos/Notas:**
- Solo existe en test: la bandera `QA_TESTERS_ENABLED` está apagada en producción.
