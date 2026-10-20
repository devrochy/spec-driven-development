---
id: HU-AOS-29
titulo: "Tablero de fiabilidad"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, calidad_ia]
req: [REQ-AOS-08, REQ-AOS-12]
dependencias: [HU-AOS-18, HU-AOS-21]
skills: ["panel-ui", "kpi-dashboard-design", "data:build-dashboard"]
estado: borrador
---

# HU-AOS-29 · Tablero de fiabilidad

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-29

**Título:** Tablero de fiabilidad

**Workstream:** Agent OS

**Historia:** Como dueño quiero ver la consistencia de cada superpoder, las comprobaciones fallidas, la completitud y el costo por agente y conexión, para saber dónde mejorar.

**Por qué importa (valor empresarial):** Lo que no se mide no mejora: el tablero convierte la fiabilidad en una métrica de negocio.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-08, REQ-AOS-12

**Dependencias:** [HU-AOS-18](HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-21](HU-AOS-21-gate-de-release-pass-k.md)

**Criterios de aceptación (Gherkin):**
- **Consistencia.** Dado los nightly, cuando abre Calidad, entonces ve pass^4 por superpoder y los que están bajo el umbral.
- **Comprobaciones.** Dado fallos del verificador, cuando los filtra, entonces ve el tipo y puede marcar falsos positivos.
- **Costo.** Dado una conexión con tres agentes, cuando abre Consumo, entonces ve el costo por agente y por operación entre agentes.

**Evidencia / Definición de Terminado:**
- Vistas con las reglas de visualización del repo; API `/usage` y `/evals/runs`; tests.

**Riesgos/Notas:**
- Métricas sin línea base al principio: se marca "sin datos suficientes".
