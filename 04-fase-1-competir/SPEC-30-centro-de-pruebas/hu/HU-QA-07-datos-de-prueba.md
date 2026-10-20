---
id: HU-QA-07
titulo: Datos de prueba propios y guía de datos
spec: SPEC-30
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: ["confianza", "operacion"]
req: [REQ-ARCH-22]
dependencias: [HU-QA-04]
skills: ["backend-design:idempotency-and-side-effects", "panel-ui", "auditor-multitenant"]
estado: en-curso
---

# HU-QA-07 · Datos de prueba propios y guía de datos

> Estado SDD: En curso — pedido del dueño del 2026-10-13 sobre [SPEC-30](../spec.md) (D-SPEC-30-6).

**ID:** HU-QA-07

**Título:** Datos de prueba propios y guía de datos

**Workstream:** Arquitectura/Prod

**Historia:** Como tester quiero preparar con un botón mi propio negocio de prueba con datos de ejemplo y cuentas de dueño, gestor y colaborador, y tener una guía de cómo conseguir los datos externos, para ejecutar las pruebas sin pedir contraseñas ni pisar los datos de otros.

**Por qué importa (valor empresarial):** Sin datos y cuentas propias, un tester externo no puede correr la mayoría de las pruebas: 45 piden la cuenta del dueño de Cobranza Demo y sus contraseñas no se reparten.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-22

**Dependencias:** [HU-QA-04](HU-QA-04-rol-tester-e-invitaciones.md)

**Criterios de aceptación (Gherkin):**
- **Preparar mis datos.** Dado un tester en test sin datos propios, cuando pulsa «Preparar mis datos», entonces se crea su negocio de prueba con Comercio, Agenda y Cobranza, productos, una cartera con clientes al día, en mora y sin préstamo, tipos de cita y una cita, y ve las cuentas de dueño, gestor y colaborador con sus contraseñas una sola vez.
- **Sin duplicar.** Dado un tester que ya tiene datos propios, cuando vuelve a pulsar «Preparar mis datos», entonces responde que ya existen y ofrece generar contraseñas nuevas, sin crear otro negocio.
- **Contraseñas nuevas.** Dado un tester con datos propios, cuando pide contraseñas nuevas, entonces las tres cuentas cambian de contraseña, sus sesiones se cierran y las nuevas se muestran una sola vez.
- **Solo en test.** Dado un entorno sin `QA_TESTERS_ENABLED`, cuando alguien pide preparar datos, entonces responde 409 y no crea nada.
- **Guía de datos.** Dado la pestaña Datos de prueba, cuando el tester la abre, entonces ve cada dato externo (tarjeta de Wompi, correo con alias, celular autorizado en Meta, SMTP) con qué es, para qué pruebas sirve y cómo conseguirlo, y cada prueba enlaza a los datos que requiere.

**Evidencia / Definición de Terminado:**
- Tests de servicio y de integración (crear, idempotencia, contraseñas nuevas, solo test, aislamiento); revisión del auditor multitenant; recorrido en el navegador; catálogo v6 con la sección `datos` y `requiere` en las pruebas.

**Riesgos/Notas:**
- Las cuentas generadas usan el dominio reservado `.test` y no reciben correo; las pruebas de correo usan un correo con alias propio (guía de datos).
- Los negocios de prueba se llaman «QA · …» con slug `qa-…`; el master los purga desde Negocios cuando un tester se va.
