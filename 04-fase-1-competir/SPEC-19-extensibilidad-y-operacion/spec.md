# SPEC-19 · Extensibilidad segura y operación

> Estado SDD: Diseño aprobado · Fase 1 · Workstream Arquitectura/Prod

## Problema

No hay MCP por tenant (Lety declara 900+ integraciones), los guardrails de runtime tienen huecos
(tools sin binding corren igual, sin límites por ventana), no hay status page ni SLO medidos, no se ha
hecho un pentest, el repo arrastra deuda (≈3.088 carpetas de tests en `tenants/`, una tabla de pack en
la cadena de migraciones del core, `docs/adr` vs `docs/ADR`), el contenedor corre como root y `mypy`
no puede fallar. La marca sigue dentro del repo del panel.

## Por qué importa (valor empresarial)

Las integraciones son el criterio de compra de los clientes medianos, y la seguridad verificada
(pentest, status page) es requisito de los enterprise. La higiene reduce el costo de operar con una
sola persona.

## Alcance

| HU | Qué |
|---|---|
| [HU-ARCH-19](hu/HU-ARCH-19-mcp-por-tenant.md) | MCP por tenant |
| [HU-ARCH-20](hu/HU-ARCH-20-guardrails-runtime.md) | Guardrails de runtime completos |
| [HU-ARCH-21](hu/HU-ARCH-21-status-page-y-slos.md) | Status page y SLO medidos |
| [HU-ARCH-22](hu/HU-ARCH-22-pentest.md) | Pentest y cuestionario de seguridad |
| [HU-ARCH-23](hu/HU-ARCH-23-higiene.md) | Higiene de repos y documentación |
| [HU-ARCH-24](hu/HU-ARCH-24-contenedor-y-tipos.md) | Contenedor no-root, mypy gradual y embeddings configurables |
| [HU-ARCH-27](hu/HU-ARCH-27-turnos-timeout-y-observabilidad.md) | Turnos con timeout, cupo justo y observabilidad |
| [HU-REP-07](hu/HU-REP-07-solvershub-brand.md) | Repo `solvershub-brand` |

## Decisiones

### D-SPEC-19-1 · Cómo se conectan integraciones externas

| Opción | Pros | Contras |
|---|---|---|
| **A. Cliente MCP en el core con allowlist de herramientas por negocio, scopes y circuit breaker** | Estándar abierto; una integración sirve a muchos negocios; aislado por negocio | Hay que operar la seguridad de servidores de terceros |
| B. Solo tools declarativas HTTP (hoy) | Ya existe, con protección SSRF | Cada integración se arma a mano |
| C. Gateway de integraciones externo gestionado | Cientos de conectores listos | Datos de clientes en otro proveedor; costo por uso |

**Recomendación: A.** Estado: ⏳ pendiente.

### D-SPEC-19-2 · Status page

| Opción | Pros | Contras |
|---|---|---|
| **A. Servicio gestionado alimentado por los checks propios** | Rápido, fuera de la propia infraestructura | Costo mensual bajo |
| B. Página propia | Sin costo | Se cae junto con la plataforma |

**Recomendación: A.** Estado: ⏳ pendiente.

## Requerimientos cubiertos

REQ-ARCH-06, REQ-ARCH-07, REQ-ARCH-09, REQ-ARCH-12, REQ-ARCH-17, REQ-GTM-08, REQ-PLUS-07,
REQ-COMP-02, REQ-REP-01.
