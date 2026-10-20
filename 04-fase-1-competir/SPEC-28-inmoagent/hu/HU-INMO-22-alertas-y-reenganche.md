---
id: HU-INMO-22
titulo: "Alertas de coincidencias y reenganche de leads"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, legal]
req: [REQ-INMO-09]
dependencias: [HU-INMO-04, HU-INMO-16, HU-CHAN-03]
skills: ["meta-whatsapp", "eval-author"]
estado: borrador
---

# HU-INMO-22 · Alertas de coincidencias y reenganche de leads

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-22

**Título:** Alertas de coincidencias y reenganche de leads

**Workstream:** Verticales

**Historia:** Como cliente que no encontró lo que buscaba quiero que me avisen cuando aparezca un inmueble para mí, y como inmobiliaria quiero recuperar leads que se enfriaron.

**Por qué importa (valor empresarial):** Las alertas convierten búsquedas sin resultado en visitas futuras; el reenganche recupera inversión en leads.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-09

**Dependencias:** [HU-INMO-04](HU-INMO-04-avisos-abiertos-a-habilidades.md), [HU-INMO-16](HU-INMO-16-perfil-de-busqueda-persistente.md), [HU-CHAN-03](../../SPEC-17-canales-y-campanas/hu/HU-CHAN-03-pack-marketing.md)

**Criterios de aceptación (Gherkin):**
- **Alerta.** Dado un perfil con alertas y consentimiento, cuando se publica un inmueble que cumple sus filtros duros, entonces recibe una plantilla de marketing con el inmueble sin superar `alertas_max_por_semana`.
- **Sin consentimiento.** Dado un perfil sin consentimiento, cuando aparece una coincidencia, entonces no se envía nada.
- **Reenganche.** Dado una oportunidad sin actividad en 14 días, cuando corre el cron, entonces se envía un mensaje con consentimiento y la baja se respeta.

**Evidencia / Definición de Terminado:**
- Crons que emiten eventos y pasan por la política común de avisos ([HU-INMO-04](HU-INMO-04-avisos-abiertos-a-habilidades.md)); consentimiento con una sola fuente ([HU-CHAN-03](../../SPEC-17-canales-y-campanas/hu/HU-CHAN-03-pack-marketing.md)), sin campo propio en el pack.

**Riesgos/Notas:**
- Fase INMO 3 · Captación y visitas.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
