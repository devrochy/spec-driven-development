---
id: HU-UI-10
titulo: Colaboradores con grilla de permisos e invitaciones
spec: SPEC-13
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-UX-04]
dependencias: [HU-UI-02]
skills: ["frontend-design", "backend-design:auth-and-authorization", "backend-design:security-reviewer", "panel-ui"]
estado: parqueada
---

# HU-UI-10 · Colaboradores con grilla de permisos e invitaciones

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md).

**ID:** HU-UI-10

**Título:** Colaboradores con grilla de permisos e invitaciones

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero invitar a mi equipo y darles permisos con una grilla legible (sección × ninguno/ver/editar) para controlar quién hace qué sin escribir claves técnicas.

**Por qué importa (valor empresarial):** Los permisos mal dados son un riesgo de seguridad y los formularios con claves crudas (`section:access@scope`) invitan al error. El límite de colaboradores por plan (créditos v2) hace de esta vista un punto de expansión.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-04

**Dependencias:** [HU-UI-02](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md)

**Criterios de aceptación (Gherkin):**
- **Grilla.** Dado un colaborador, cuando edito sus permisos, entonces veo una grilla con etiquetas legibles (de `core/admin/permissions.py:30-69`).
- **Invitar.** Dado un correo, cuando invito, entonces se envía un enlace (no una contraseña que yo escribo) y veo la invitación pendiente con opción de revocarla.
- **Desactivar con consecuencia.** Dado desactivar a alguien, cuando confirmo, entonces el texto explica qué pierde y no puedo desactivarme a mí mismo.
- **Roles.** Dado un usuario que no es master, cuando crea un colaborador, entonces no ve el rol "Master".

**Evidencia / Definición de Terminado:**
- Endpoint del catálogo de secciones; vista migrada; tests.

**Riesgos/Notas:**
- El selector de negocio para agencias usa la lista de negocios del usuario, no un texto.
