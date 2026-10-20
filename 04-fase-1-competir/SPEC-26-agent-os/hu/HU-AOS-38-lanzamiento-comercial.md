---
id: HU-AOS-38
titulo: "Lanzamiento comercial (incluye validar el nombre)"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, legal]
req: [REQ-AOS-13, REQ-AOS-14]
dependencias: [HU-AOS-22, HU-AOS-26, HU-AOS-27, HU-AOS-37, HU-GTM-05, HU-ARCH-01]
skills: ["doc-coauthoring", "frontend-design"]
estado: borrador
---

# HU-AOS-38 · Lanzamiento comercial (incluye validar el nombre)

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-38

**Título:** Lanzamiento comercial (incluye validar el nombre)

**Workstream:** Agent OS

**Historia:** Como SolversHub quiero lanzar el Agent OS con mensajes honestos, una demo y un piloto, y con el nombre validado, para venderlo sin prometer lo que no hace.

**Por qué importa (valor empresarial):** Honestidad comercial (constitución §1.2) y un nombre sin conflicto legal con un competidor que ya usa "Agent OS".

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-13, REQ-AOS-14

**Dependencias:** [HU-AOS-22](HU-AOS-22-dogfooding-solvershub.md), [HU-AOS-26](HU-AOS-26-colaboracion-en-el-panel.md), [HU-AOS-27](HU-AOS-27-versiones-en-el-panel.md), [HU-AOS-37](HU-AOS-37-cuotas-y-planes.md), HU-GTM-05, [HU-ARCH-01](../../../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md)

**Criterios de aceptación (Gherkin):**
- **Claims.** Dado la landing y el material comercial, cuando se revisan, entonces cumplen el checklist de claims honestos (HU-GTM-05).
- **Nombre.** Dado el nombre comercial, cuando el abogado lo revisa, entonces está aprobado o se usa la alternativa.
- **Piloto.** Dado un negocio piloto, cuando opera 30 días, entonces sus métricas de fiabilidad están dentro de las metas.

**Evidencia / Definición de Terminado:**
- Landing y material actualizados; demo grabada; piloto con reporte.

**Riesgos/Notas:**
- Sin producción separada ([HU-ARCH-01](../../../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md)) no hay lanzamiento.
