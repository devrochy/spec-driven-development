---
id: HU-SUB-16
titulo: MRR, churn y embudo para negocios con suscripciones
spec: SPEC-20
fase: 1
hito: "1"
workstream: Comercio y suscripciones
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-SUB-05]
dependencias: [HU-SUB-08, HU-SUB-15]
skills: ["kpi-dashboard-design", "data:sql-queries", "data:statistical-analysis", "panel-ui"]
estado: borrador
---

# HU-SUB-16 · MRR, churn y embudo para negocios con suscripciones

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-20](../spec.md).

**ID:** HU-SUB-16

**Título:** MRR, churn y embudo para negocios con suscripciones

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de un negocio con mensualidades quiero ver mi ingreso recurrente, altas, bajas, mora y cohortes por plan para gestionar mi negocio como un negocio de suscripción.

**Por qué importa (valor empresarial):** Convierte el superpoder en una herramienta de gestión: el negocio ve el valor del asistente en su MRR. Es un diferencial frente a plataformas de mensajería que no conocen el modelo de suscripción.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-SUB-05

**Dependencias:** HU-SUB-08, HU-SUB-15

**Criterios de aceptación (Gherkin):**
- **MRR.** Dado suscripciones activas, cuando abro Suscripciones → Métricas, entonces veo MRR, altas, bajas y su variación.
- **Mora.** Dado cargos vencidos, cuando lo veo, entonces aparece el monto en mora y su antigüedad.
- **Cohortes.** Dado los meses de alta, cuando veo cohortes, entonces se ve la retención por plan.
- **Embudo.** Dado la atribución de leads, cuando lo veo, entonces veo lead → demo → plan.

**Evidencia / Definición de Terminado:**
- Endpoint de métricas por contrato (sirve a ambos proveedores); vista; tests.

**Riesgos/Notas:**
- El tenant `solvershub` lo usa como tablero de su propio negocio.
