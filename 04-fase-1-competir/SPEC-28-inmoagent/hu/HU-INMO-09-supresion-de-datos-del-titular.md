---
id: HU-INMO-09
titulo: "Supresión de datos del titular en la vertical"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: S
impacto: [legal, confianza]
req: [REQ-INMO-12]
dependencias: [HU-INMO-10]
skills: ["backend-design:security-discipline", "db-migration", "auditor-multitenant"]
estado: borrador
---

# HU-INMO-09 · Supresión de datos del titular en la vertical

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-09

**Título:** Supresión de datos del titular en la vertical

**Workstream:** Verticales

**Historia:** Como titular de datos quiero que la inmobiliaria pueda borrar o anonimizar lo que el asistente guardó de mí, para ejercer mis derechos de la Ley 1581 de 2012.

**Por qué importa (valor empresarial):** `purge_memory` solo toca `memory_vectors` y la memoria de Redis (`core/memory/vector.py:147-188`) y el borrado lógico conserva el dato personal. La vertical guarda pines, perfiles, documentos y captaciones.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-INMO-12

**Dependencias:** [HU-INMO-10](HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md)

**Criterios de aceptación (Gherkin):**
- **Supresión.** Dado un cliente con perfil, búsquedas, captaciones y contratos, cuando el negocio ejecuta la supresión, entonces el hook `suprimir_titular(customer_id)` del pack anonimiza ubicación, preferencias implícitas, datos de captación y documento.
- **Append-only.** Dado las tablas append-only del pack, cuando corre la supresión, entonces su trigger solo permite esa anonimización y rechaza cualquier otro UPDATE o DELETE.
- **Redis.** Dado claves `inmo:{tenant}:{conversation}:*`, cuando se purga el negocio o el titular, entonces se borran.

**Evidencia / Definición de Terminado:**
- Hook por pack definido en el ADR de la vertical; trigger (nunca RULE, que rompería `purge_tenant`); claves Redis registradas para la purga; tests.

**Riesgos/Notas:**
- Fase INMO 1 · Fundaciones.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- Contratos vigentes se conservan por obligación legal (por verificar con el abogado, HU-GTM-02).
