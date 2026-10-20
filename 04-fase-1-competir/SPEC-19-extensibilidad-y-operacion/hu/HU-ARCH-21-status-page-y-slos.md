---
id: HU-ARCH-21
titulo: Status page pública y SLO medidos
spec: SPEC-19
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, diferenciacion]
req: [REQ-ARCH-09, REQ-GTM-08]
dependencias: [HU-ARCH-07]
skills: ["backend-design:observability-by-default", "kpi-dashboard-design"]
estado: borrador
---

# HU-ARCH-21 · Status page pública y SLO medidos

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-19](../spec.md).

**ID:** HU-ARCH-21

**Título:** Status page pública y SLO medidos

**Workstream:** Arquitectura/Prod

**Historia:** Como cliente de SolversHub quiero una página pública con el estado de la plataforma y su historial para saber si un problema es mío o de la plataforma.

**Por qué importa (valor empresarial):** Los SLO publicados en `security.md` hoy no se miden. Una status page es requisito de los clientes enterprise y reduce los tickets durante un incidente.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-ARCH-09, REQ-GTM-08

**Dependencias:** [HU-ARCH-07](../../../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md)

**Criterios de aceptación (Gherkin):**
- **Página.** Dado `status.<dominio>`, cuando la abro, entonces veo el estado de webhook, panel, asistente y pagos, con historial de 90 días.
- **SLO.** Dado los SLO de disponibilidad, cuando se calcula el mes, entonces se publica el cumplimiento y el presupuesto de error.
- **Incidente.** Dado un incidente, cuando se declara, entonces la página lo muestra con actualizaciones.

**Evidencia / Definición de Terminado:**
- Status page en producción; SLO documentados en `security.md` con su medición.

**Riesgos/Notas:**
- Puede ser un servicio gestionado.
