---
id: HU-FWK-09
titulo: Acciones personalizadas (tools declarativas) en el panel nuevo
spec: SPEC-16
fase: 1
hito: "1"
workstream: Framework/Plugins
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion]
req: [REQ-FWK-05]
dependencias: [HU-FWK-08]
skills: ["new-tool", "backend-design:security-discipline", "backend-design:security-reviewer"]
estado: borrador
---

# HU-FWK-09 · Acciones personalizadas (tools declarativas) en el panel nuevo

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-16](../spec.md).

**ID:** HU-FWK-09

**Título:** Acciones personalizadas (tools declarativas) en el panel nuevo

**Workstream:** Framework/Plugins

**Historia:** Como implementador quiero crear y probar acciones personalizadas que llaman a la API de mi cliente desde el panel nuevo para conectar su sistema sin código y sin ir al panel clásico.

**Por qué importa (valor empresarial):** Es el único pendiente de paridad con el panel clásico (hoy enlaza a `/legacy`) y el camino sin código para integrar sistemas del cliente, que es lo que piden los clientes medianos.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FWK-05

**Dependencias:** [HU-FWK-08](HU-FWK-08-formulario-de-schema-v2.md)

**Criterios de aceptación (Gherkin):**
- **Crear.** Dado el editor, cuando defino una acción HTTP con su schema y dominio permitido, entonces se guarda con validación de SSRF (ADR-0052).
- **Probar.** Dado una acción, cuando la pruebo con datos de ejemplo, entonces veo la respuesta.
- **Límite del plan.** Dado el plan Basic con 3 acciones, cuando creo la cuarta, entonces se bloquea con explicación.
- **Retiro del legado.** Dado el panel nuevo, cuando abro Configuración avanzada, entonces ya no hay enlace a `/legacy`.

**Evidencia / Definición de Terminado:**
- Página nueva; tests; enlace al legado eliminado.

**Riesgos/Notas:**
- Completa la paridad del panel (147/148).
