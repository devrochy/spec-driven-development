---
id: HU-GTM-13
titulo: Prueba social real en la landing
spec: SPEC-23
fase: 2
hito: "2"
workstream: GTM
prioridad: P2
critico: false
estimacion: S
impacto: [ingreso, confianza]
req: [REQ-COMP-05]
dependencias: [HU-GTM-08]
skills: ["marketing:content-creation", "marketing:brand-review"]
estado: borrador
---

# HU-GTM-13 · Prueba social real en la landing

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-23](../spec.md).

**ID:** HU-GTM-13

**Título:** Prueba social real en la landing

**Workstream:** GTM

**Historia:** Como prospecto quiero ver casos y testimonios verificables de negocios como el mío para confiar en SolversHub.

**Por qué importa (valor empresarial):** Todos los competidores exhiben prueba social; hoy está oculta (`SHOW_SOCIAL_PROOF = false`) por no tener datos reales.

**Prioridad:** P2 plus

**Estimación:** S

**REQ mapeados:** REQ-COMP-05

**Dependencias:** [HU-GTM-08](../../../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-08-activos-de-venta.md)

**Criterios de aceptación (Gherkin):**
- **Verificable.** Dado cada testimonio, cuando se publica, entonces corresponde a un cliente real con autorización.
- **Activar.** Dado al menos 3 testimonios y 2 casos, cuando se publican, entonces `SHOW_SOCIAL_PROOF` pasa a `true`.

**Evidencia / Definición de Terminado:**
- Contenido publicado con autorizaciones archivadas.

**Riesgos/Notas:**
- Nunca datos inventados (los mocks actuales se borran).
