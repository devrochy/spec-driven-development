---
id: HU-QA-04
titulo: Rol tester e invitaciones
spec: SPEC-30
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: ["confianza"]
req: [REQ-ARCH-22]
dependencias: [HU-QA-03]
skills: ["backend-design:auth-and-authorization", "backend-design:security-reviewer", "panel-ui", "auditor-multitenant"]
estado: terminada
---

# HU-QA-04 · Rol tester e invitaciones

> Estado SDD: Lista para ejecutar — [SPEC-30](../spec.md) en Diseño aprobado (D-33).

**ID:** HU-QA-04

**Título:** Rol tester e invitaciones

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño quiero invitar testers internos y externos con un rol que pueda hacer todo lo de un master en la operación y gestionar Colaboradores como dueño del negocio activo, y solo en el entorno de test, para que prueben el producto completo sin tocar producción ni las cuentas de plataforma.

**Por qué importa (valor empresarial):** Permite sumar clientes piloto o testers contratados a los ciclos de prueba con cuenta propia, revocable y sin acceso a producción.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-22

**Dependencias:** [HU-QA-03](HU-QA-03-seccion-pruebas-en-el-panel.md)

**Criterios de aceptación (Gherkin):**
- **Invitación.** Dado el dueño en Pruebas › Testers, cuando invita a un correo externo, entonces llega un correo con un enlace de un solo uso y al abrirlo el tester define su contraseña y entra al panel.
- **Colaboradores como dueño.** Dado un tester en test con un negocio activo, cuando abre Colaboradores, entonces crea, invita y gestiona las cuentas de ese negocio, y crear un master, cambiar la contraseña de un master o vincular entre negocios responde con error.
- **Opera como master.** Dado un tester en test, cuando crea un negocio de prueba o entra a la app de campo, entonces puede hacerlo como lo haría un master.
- **Solo en test.** Dado un entorno sin `QA_TESTERS_ENABLED`, cuando una cuenta tester intenta entrar o alguien intenta crear un tester, entonces el login falla y la creación responde 409.
- **Cuentas protegidas.** Dado el owner de un negocio, cuando intenta cambiar la contraseña, vincular o desactivar a un tester, entonces recibe 403.
- **Revocar.** Dado un tester activo, cuando el dueño lo revoca, entonces su sesión deja de funcionar en el siguiente pedido.

**Evidencia / Definición de Terminado:**
- Matriz de permisos master, tester, owner y colaborador en tests de API; tests del panel (el tester ve Colaboradores y Pruebas); revisión de seguridad y del auditor multitenant; prueba manual con una cuenta externa real en test.

**Riesgos/Notas:**
- Reusa el enlace firmado con HMAC de las invitaciones ([HU-SH-06](../../../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md)) y el RBAC por sección (ADR-0047).
- En producción no se carga `QA_TESTERS_ENABLED`: queda como punto del checklist de paso a producción.
