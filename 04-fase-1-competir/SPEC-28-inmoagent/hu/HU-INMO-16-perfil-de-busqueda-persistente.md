---
id: HU-INMO-16
titulo: "Perfil de búsqueda persistente y feedback"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, ingreso]
req: [REQ-INMO-04]
dependencias: [HU-INMO-15]
skills: ["new-tool", "backend-design:data-modeling-discipline"]
estado: borrador
---

# HU-INMO-16 · Perfil de búsqueda persistente y feedback

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-16

**Título:** Perfil de búsqueda persistente y feedback

**Workstream:** Verticales

**Historia:** Como cliente que vuelve quiero que el asistente recuerde lo que busco y lo que no me gustó, para no repetir todo.

**Por qué importa (valor empresarial):** La búsqueda de vivienda dura semanas; recordar el perfil sube la conversión y habilita las alertas.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-04

**Dependencias:** [HU-INMO-15](HU-INMO-15-recomendaciones-y-relajacion.md)

**Criterios de aceptación (Gherkin):**
- **Retomar.** Dado un perfil activo de hace 10 días, cuando el cliente escribe "¿tienes algo nuevo?", entonces se busca con su perfil y se confirma en una línea antes.
- **Preferencias implícitas.** Dado varios "no me interesa" por falta de parqueadero, cuando se puntúa, entonces sube el peso del parqueadero dentro del tope.
- **Sin pin crudo.** Dado una búsqueda con el pin del cliente, cuando se registra en `busquedas`, entonces se guarda la zona o una celda gruesa, no la coordenada.

**Evidencia / Definición de Terminado:**
- Tablas `perfiles_busqueda` y `recomendaciones` en uso; resumen corto en el perfil del cliente; tests.

**Riesgos/Notas:**
- Fase INMO 2 · Búsqueda y geo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
