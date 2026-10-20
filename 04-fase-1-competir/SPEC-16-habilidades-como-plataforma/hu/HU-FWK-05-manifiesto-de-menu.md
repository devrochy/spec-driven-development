---
id: HU-FWK-05
titulo: Menú del panel desde un manifiesto del backend
spec: SPEC-16
fase: 1
hito: "1"
workstream: Framework/Plugins
prioridad: P1
critico: false
estimacion: S
impacto: [operacion]
req: [REQ-FWK-05]
dependencias: [HU-FWK-04, HU-UX-01]
skills: ["frontend-design", "backend-design:auth-and-authorization"]
estado: borrador
---

# HU-FWK-05 · Menú del panel desde un manifiesto del backend

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-16](../spec.md).

**ID:** HU-FWK-05

**Título:** Menú del panel desde un manifiesto del backend

**Workstream:** Framework/Plugins

**Historia:** Como responsable del producto quiero que el menú del panel venga del backend según los packs habilitados y los permisos del usuario para que una habilidad nueva aparezca sin desplegar el panel y el menú nunca se desalinee.

**Por qué importa (valor empresarial):** El menú escrito a mano ya se desalineó (faltan Clientes y Gestores de cobranza). Con el manifiesto, cada habilidad nueva llega a todos los clientes con un release del backend.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-FWK-05

**Dependencias:** [HU-FWK-04](HU-FWK-04-catalogo-de-habilidades.md), [HU-UX-01](../../SPEC-12-arquitectura-de-informacion/hu/HU-UX-01-adr-arquitectura-de-informacion.md)

**Criterios de aceptación (Gherkin):**
- **Manifiesto.** Dado `GET /api/v1/admin/ui/manifest`, cuando lo pido, entonces recibo grupos e ítems filtrados por mis permisos y packs, en el orden del ADR de arquitectura de información.
- **Panel.** Dado el sidebar, cuando carga, entonces se arma desde el manifiesto (grupos del core fijos).
- **Pack nuevo.** Dado un pack nuevo habilitado, cuando recargo, entonces su menú aparece sin desplegar el panel.

**Evidencia / Definición de Terminado:**
- Endpoint con tests de permisos; `nav.ts` reducido a los grupos del core.

**Riesgos/Notas:**
- Usa `admin_menu` existente (`core/plugin_manager.py:453-479`).
