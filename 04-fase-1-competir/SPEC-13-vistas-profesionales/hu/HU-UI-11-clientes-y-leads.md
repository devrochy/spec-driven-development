---
id: HU-UI-11
titulo: Clientes con filtros, exportación y detalle
spec: SPEC-13
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, operacion]
req: [REQ-UX-04]
dependencias: [HU-UI-08]
skills: ["frontend-design", "backend-design:query-discipline", "backend-design:security-discipline", "panel-ui"]
estado: parqueada
---

# HU-UI-11 · Clientes con filtros, exportación y detalle

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md).

**ID:** HU-UI-11

**Título:** Clientes con filtros, exportación y detalle

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero filtrar mis clientes por estado, segmento, canal y ciudad, exportarlos y ver su ficha con conversaciones y pedidos para usar el panel como mi CRM.

**Por qué importa (valor empresarial):** Convertir la lista de leads en un CRM usable evita que el negocio pague otro CRM y aumenta la dependencia sana del producto. `agent-sale` ya lo tenía.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-04

**Dependencias:** [HU-UI-08](HU-UI-08-filtros-y-tablas.md)

**Criterios de aceptación (Gherkin):**
- **Filtros.** Dado Clientes, cuando filtro por estado, segmento, canal y ciudad, entonces la lista se filtra en el servidor.
- **CSV.** Dado un filtro, cuando exporto, entonces descargo un CSV con los clientes filtrados y queda auditado.
- **Ficha.** Dado un cliente, cuando lo abro, entonces veo contacto, conversaciones con enlace, pedidos, suscripciones y el interruptor del asistente para ese cliente.

**Evidencia / Definición de Terminado:**
- Endpoints de filtros y exportación; cajón de detalle; tests.

**Riesgos/Notas:**
- La exportación respeta permisos y no incluye datos sensibles sin permiso explícito.
