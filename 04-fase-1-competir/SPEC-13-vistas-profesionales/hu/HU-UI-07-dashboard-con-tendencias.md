---
id: HU-UI-07
titulo: Dashboard con período, tendencias y calidad
spec: SPEC-13
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, calidad_ia]
req: [REQ-UX-04, REQ-FIX-09]
dependencias: [HU-UI-03]
skills: ["kpi-dashboard-design", "frontend-design", "data:sql-queries", "panel-ui"]
estado: parqueada
---

# HU-UI-07 · Dashboard con período, tendencias y calidad

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md).

**ID:** HU-UI-07

**Título:** Dashboard con período, tendencias y calidad

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero ver cómo va mi asistente en el período que elija, comparado con el anterior, incluido cuántas conversaciones resolvió sin humano, para saber si me está dando resultados.

**Por qué importa (valor empresarial):** El dueño renueva cuando ve el valor. "% resuelto sin humano" es la métrica que justifica el precio frente a contratar una persona; Zendesk y SleekFlow la venden como reporte estrella.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-04, REQ-FIX-09

**Dependencias:** [HU-UI-03](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md)

**Criterios de aceptación (Gherkin):**
- **Período.** Dado el selector 7/15/30 días, cuando cambio, entonces los KPIs y el gráfico se recalculan con su variación frente al período anterior.
- **Calidad.** Dado el período, cuando lo veo, entonces aparece el % de conversaciones resueltas sin humano y el tiempo medio de respuesta.
- **Enlaces.** Dado un KPI, cuando lo pulso, entonces voy a la lista filtrada correspondiente.
- **Avisos.** Dado el consumo al 80 %, cuando entro al Resumen, entonces veo el aviso.

**Evidencia / Definición de Terminado:**
- `GET /admin/dashboard?period=` con series y comparación; gráfico SVG accesible.

**Riesgos/Notas:**
- Desde D-32 (D-SPEC-29-1) esta HU entrega los **datos**: `GET /admin/dashboard?period=` con series y comparación frente al período anterior. La UI del Resumen (KPIs, gráficos, perfiles por rol) la construye [HU-DS-07](../../SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-07-resumen-modular-por-rol.md) de [SPEC-29](../../SPEC-29-sistema-de-diseno-unificado/spec.md).
- CSAT queda para cuando exista la encuesta ([HU-COM-10](../../SPEC-18-pack-commerce-v2/hu/HU-COM-10-proactividad-v2.md)).
