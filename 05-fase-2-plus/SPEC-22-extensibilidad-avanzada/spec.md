# SPEC-22 · Extensibilidad avanzada

> Estado SDD: Diseño aprobado · Fase 2 · Workstreams Framework/Plugins y Flujo visual

## Problema

El orden de personalización (configuración → pack → plugin del tenant → topología) tiene definido el
nivel "plugin del tenant" pero no un mecanismo formal; el scaffold de plugins genera 5 archivos sin
modelos, jobs ni migraciones. Faltan integraciones MCP de catálogo, edición avanzada del flujo, un
`ToolContext` alineado con el contrato, embeddings por negocio, tool siguiente forzada y varias
sucursales en comercio.

## Por qué importa (valor empresarial)

Es lo que permite atender clientes grandes y particulares **sin fork** (invariante 2): cadenas con
sucursales, integraciones propias y flujos avanzados. Cada uno de estos casos hoy terminaría en
desarrollo a medida.

## Alcance

| HU | Qué |
|---|---|
| [HU-FWK-13](hu/HU-FWK-13-plugin-del-tenant.md) | Plugin del tenant formalizado |
| [HU-FWK-14](hu/HU-FWK-14-integraciones-mcp.md) | Integraciones MCP de catálogo |
| [HU-FLOW-07](hu/HU-FLOW-07-purpose-y-reglas-por-etapa.md) | Edición del `purpose` y reglas por etapa |
| [HU-ARCH-25](hu/HU-ARCH-25-toolcontext-y-embeddings.md) | `ToolContext` según el contrato y embeddings por negocio |
| [HU-ARCH-26](hu/HU-ARCH-26-tool-siguiente-forzada.md) | Tool siguiente forzada y turnos silenciosos |
| [HU-COM-16](hu/HU-COM-16-multisucursal.md) | Varias sucursales |

## Decisiones

### D-SPEC-22-1 · Forma del "plugin del tenant"

| Opción | Pros | Contras |
|---|---|---|
| **A. Paquete instalable acotado a un negocio, con revisión del master y los mismos checks de invariantes** | Poder completo sin fork; mismo binario (invariante 2) | Requiere revisión humana de cada plugin |
| B. Código del cliente en sandbox (funciones aisladas) | Autoservicio | Superficie de seguridad nueva y costosa de operar |
| C. Solo tools declarativas y MCP | Cero riesgo nuevo | No cubre casos con datos o tareas propias |

**Recomendación: A.** Estado: ✅ aceptada (ADR-0089 en agent-core, 2026-10-03).

## Requerimientos cubiertos

REQ-FWK-06, REQ-COMP-02, REQ-FLOW-05, REQ-ARCH-11, REQ-ARCH-07, REQ-COM-08.
