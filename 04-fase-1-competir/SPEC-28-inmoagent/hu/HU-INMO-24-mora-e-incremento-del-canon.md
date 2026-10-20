---
id: HU-INMO-24
titulo: "Mora e incremento anual del canon"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, legal]
req: [REQ-INMO-08]
dependencias: [HU-INMO-04, HU-SUB-18, HU-INMO-23]
skills: ["pagos-wompi", "deep-research", "meta-whatsapp"]
estado: borrador
---

# HU-INMO-24 · Mora e incremento anual del canon

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-24

**Título:** Mora e incremento anual del canon

**Workstream:** Verticales

**Historia:** Como inmobiliaria quiero enterarme a tiempo de la mora y proponer el incremento anual del canon dentro del tope legal, para proteger el ingreso del propietario sin violar la ley.

**Por qué importa (valor empresarial):** La mora es el mayor costo de la administración de arriendos y el incremento mal calculado es un riesgo legal (Ley 820 de 2003, art. 20).

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-08

**Dependencias:** [HU-INMO-04](HU-INMO-04-avisos-abiertos-a-habilidades.md), HU-SUB-18, [HU-INMO-23](HU-INMO-23-contrato-de-arriendo-y-canon.md)

**Criterios de aceptación (Gherkin):**
- **Mora.** Dado un cargo vencido sin pagar tras `dias_gracia`, cuando llega `subscription.past_due`, entonces el contrato pasa a en_mora y el asesor y, si está configurado, el propietario reciben aviso.
- **Incremento de vivienda.** Dado un contrato de vivienda con 12 meses al mismo canon y el IPC del año anterior cargado, cuando corre el cron, entonces se propone un canon ≤ canon × (1 + IPC) y no se aplica sin aprobación ni aviso escrito.
- **Comercial.** Dado un contrato de uso comercial, cuando corre el cron, entonces se aplica su regla pactada sin el tope de vivienda.

**Evidencia / Definición de Terminado:**
- Crons de mora, incremento y vencimiento; tabla `ajustes_canon`; plantillas de aviso; reglas legales confirmadas o marcadas por verificar.

**Riesgos/Notas:**
- Fase INMO 4 · Arriendos y medición.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- Quién carga el IPC y quién aprueba lo decide P-28.
