---
id: HU-FWK-14
titulo: Integraciones MCP de catálogo
spec: SPEC-22
fase: 2
hito: "2"
workstream: Framework/Plugins
prioridad: P2
critico: false
estimacion: L
impacto: [ingreso, diferenciacion]
req: [REQ-COMP-02]
dependencias: [HU-ARCH-19]
skills: ["deep-research", "backend-design:security-discipline"]
estado: borrador
---

# HU-FWK-14 · Integraciones MCP de catálogo

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-22](../spec.md).

**ID:** HU-FWK-14

**Título:** Integraciones MCP de catálogo

**Workstream:** Framework/Plugins

**Historia:** Como negocio que usa HubSpot, Shopify o Google Sheets quiero conectarlos desde un catálogo con un clic para que mi asistente use mis datos sin configurar servidores.

**Por qué importa (valor empresarial):** Convierte la capacidad MCP en integraciones vendibles y cierra el claim que hoy la landing hace sin respaldo (HubSpot, Salesforce, Pipedrive, Zoho).

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-COMP-02

**Dependencias:** [HU-ARCH-19](../../../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md)

**Criterios de aceptación (Gherkin):**
- **Catálogo.** Dado el catálogo de integraciones, cuando elijo una, entonces se conecta con OAuth o llave y quedan sus herramientas permitidas por defecto.
- **Verificadas.** Dado cada integración, cuando se publica, entonces tiene pruebas y documentación.

**Evidencia / Definición de Terminado:**
- Al menos 3 integraciones verificadas.

**Riesgos/Notas:**
- Actualizar la landing solo cuando cada una exista ([HU-GTM-10](../../../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-10-paginas-de-integraciones-y-seo.md)).
