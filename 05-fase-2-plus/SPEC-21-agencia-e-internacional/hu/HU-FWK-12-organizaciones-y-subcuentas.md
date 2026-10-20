---
id: HU-FWK-12
titulo: Organizaciones y sub-cuentas para agencias
spec: SPEC-21
fase: 2
hito: "2"
workstream: Framework/Plugins
prioridad: P2
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-FWK-08, REQ-PLUS-05b]
dependencias: []
skills: ["adr", "arquitecto", "backend-design:auth-and-authorization", "auditor-multitenant"]
estado: parqueada
---

# HU-FWK-12 · Organizaciones y sub-cuentas para agencias

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-21](../spec.md) (D-SPEC-21-1).

**ID:** HU-FWK-12

**Título:** Organizaciones y sub-cuentas para agencias

**Workstream:** Framework/Plugins

**Historia:** Como agencia quiero administrar los negocios de mis clientes desde una organización, con mis colaboradores y permisos heredados, para operar muchos asistentes sin crear usuarios en cada uno.

**Por qué importa (valor empresarial):** Es el habilitador del canal de agencias (D-01, "agencia después"). Cada agencia trae decenas de negocios sin costo de adquisición directo.

**Prioridad:** P2 plus

**Estimación:** M

**REQ mapeados:** REQ-FWK-08, REQ-PLUS-05b

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Organización.** Dado una agencia, cuando crea su organización, entonces puede crear o vincular negocios hijos.
- **Permisos heredados.** Dado un colaborador de la organización, cuando entra, entonces ve los negocios según su rol sin invitación por negocio.
- **Aislamiento.** Dado dos organizaciones, cuando una lista sus negocios, entonces no ve los de la otra.

**Evidencia / Definición de Terminado:**
- ADR de organizaciones; migración aditiva; tests de aislamiento.

**Riesgos/Notas:**
- No rompe el RLS por negocio: la organización solo agrega autorización.
