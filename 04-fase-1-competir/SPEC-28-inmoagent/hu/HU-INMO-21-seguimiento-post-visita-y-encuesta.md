---
id: HU-INMO-21
titulo: "Seguimiento post-visita y encuesta"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, calidad_ia]
req: [REQ-INMO-09]
dependencias: [HU-INMO-04, HU-INMO-19, HU-INMO-20]
skills: ["meta-whatsapp", "eval-author"]
estado: borrador
---

# HU-INMO-21 · Seguimiento post-visita y encuesta

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-21

**Título:** Seguimiento post-visita y encuesta

**Workstream:** Verticales

**Historia:** Como inmobiliaria quiero preguntar después de cada visita cómo le fue al cliente y si le interesa, para avanzar el negocio y medir la satisfacción.

**Por qué importa (valor empresarial):** El seguimiento a tiempo es donde se gana o se pierde la oferta, y la encuesta alimenta el KPI de satisfacción.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-09

**Dependencias:** [HU-INMO-04](HU-INMO-04-avisos-abiertos-a-habilidades.md), [HU-INMO-19](HU-INMO-19-visitas-con-el-asesor.md), [HU-INMO-20](HU-INMO-20-oportunidades-y-asesores.md)

**Criterios de aceptación (Gherkin):**
- **Encuesta.** Dado una visita marcada como realizada, cuando pasan 2 horas, entonces el cliente recibe una encuesta de 1 a 5 y la pregunta de si le interesa.
- **Interés.** Dado "me interesa", cuando responde, entonces la oportunidad avanza y el asesor recibe aviso.
- **No asistió.** Dado una visita no asistida, cuando se registra, entonces se ofrece reprogramar una sola vez.

**Evidencia / Definición de Terminado:**
- Cron `seguimiento_post_visita`; eventos de aviso declarados con [HU-INMO-04](HU-INMO-04-avisos-abiertos-a-habilidades.md); categoría de plantilla verificada.

**Riesgos/Notas:**
- Fase INMO 3 · Captación y visitas.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
