---
id: HU-FWK-06
titulo: Descriptores enriquecidos y API de vistas de packs
spec: SPEC-16
fase: 1
hito: "1"
workstream: Framework/Plugins
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, operacion]
req: [REQ-FWK-05]
dependencias: [HU-FWK-05]
skills: ["adr", "arquitecto", "backend-design:testing-with-discernment"]
estado: borrador
---

# HU-FWK-06 · Descriptores enriquecidos y API de vistas de packs

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-16](../spec.md) (D-SPEC-16-1).

**ID:** HU-FWK-06

**Título:** Descriptores enriquecidos y API de vistas de packs

**Workstream:** Framework/Plugins

**Historia:** Como desarrollador de una habilidad quiero describir sus listas, filtros, KPIs y acciones en el backend para que el panel las muestre sin escribir una pantalla.

**Por qué importa (valor empresarial):** Reduce el costo de cada habilidad nueva a la mitad y deja la UI consistente. Es la base técnica del catálogo creciente de habilidades.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-FWK-05

**Dependencias:** [HU-FWK-05](HU-FWK-05-manifiesto-de-menu.md)

**Criterios de aceptación (Gherkin):**
- **Descriptor.** Dado un pack, cuando declara una vista, entonces define columnas con tipo (dinero con moneda, fecha, badge, enlace, booleano), filtros, acciones por fila con confirmación, KPIs y estado vacío.
- **API.** Dado `GET /api/v1/pack/{id}/views/{vista}`, cuando la pido con filtros y página, entonces recibo datos y descriptor; las acciones van por `POST …/actions/{accion}` con permisos.
- **Contrato.** Dado los descriptores, cuando cambian, entonces un test de snapshot lo detecta.

**Evidencia / Definición de Terminado:**
- Extensión de `ViewDescriptor`; endpoints; OpenAPI regenerado; tests.

**Riesgos/Notas:**
- `kind: "custom"` para pantallas complejas.
