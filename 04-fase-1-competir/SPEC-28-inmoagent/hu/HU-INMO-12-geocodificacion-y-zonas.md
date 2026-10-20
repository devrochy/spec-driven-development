---
id: HU-INMO-12
titulo: "Geocodificación con confirmación y zonas"
spec: SPEC-28
fase: 1
hito: "1"
workstream: Verticales
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, diferenciacion]
req: [REQ-INMO-03]
dependencias: [HU-INMO-02, HU-INMO-03, HU-INMO-10]
skills: ["new-tool", "backend-design:security-discipline", "deep-research"]
estado: borrador
---

# HU-INMO-12 · Geocodificación con confirmación y zonas

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-28](../spec.md).

**ID:** HU-INMO-12

**Título:** Geocodificación con confirmación y zonas

**Workstream:** Verticales

**Historia:** Como cliente quiero decir "cerca de Unicentro" o "en Chapinero" y que el asistente entienda el lugar correcto, confirmándolo conmigo, para que la búsqueda no parta de un sitio equivocado.

**Por qué importa (valor empresarial):** Un lugar mal resuelto arruina toda la búsqueda; confirmar con una lista cuesta un toque.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-INMO-03

**Dependencias:** [HU-INMO-02](HU-INMO-02-entrada-estructurada-whatsapp.md), [HU-INMO-03](HU-INMO-03-salida-interactiva.md), [HU-INMO-10](HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md)

**Criterios de aceptación (Gherkin):**
- **Nombre ambiguo.** Dado "Chapinero" con dos zonas posibles, cuando se resuelve, entonces el asistente ofrece una lista y no elige solo.
- **Pin.** Dado que el cliente compartió su ubicación, cuando busca "cerca de mí", entonces se usa el pin sin geocodificar.
- **Licencia.** Dado un proveedor que no permite guardar, cuando responde, entonces el resultado no queda en `geocache` más allá de lo permitido.
- **Proveedor caído.** Dado un timeout del geocodificador, cuando se resuelve, entonces se pide el pin o el barrio y no se inventan coordenadas.

**Evidencia / Definición de Terminado:**
- Lista cerrada de proveedores en código (nunca una URL de la configuración), por `ScopedHttp`; clave en headers o params, nunca en el texto de la URL; sin direcciones ni coordenadas en los logs.
- `geocache` por negocio, con único parcial y consulta guardada como HMAC por negocio; importación de zonas OSM; tests con dobles HTTP.

**Riesgos/Notas:**
- Fase INMO 2 · Búsqueda y geo.
- **DoR adicional:** bloqueada hasta que [P-26](../../../02-vision-y-decisiones/preguntas-abiertas.md#p-26--piloto-de-la-vertical-inmobiliaria) tenga un piloto firmado (D-31).
- El proveedor lo decide P-27.
