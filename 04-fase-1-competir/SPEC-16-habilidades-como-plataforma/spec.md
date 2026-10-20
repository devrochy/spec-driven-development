# SPEC-16 · Habilidades como plataforma

> Estado SDD: Diseño aprobado · Fase 1 · Workstream Framework/Plugins
>
> **Reorientada (2026-10-17, [D-35](../../02-vision-y-decisiones/decisiones.md#d-35--solvershub-vende-agentes)):** una habilidad es una capacidad que se le da a un agente, no la unidad que se vende. Esta spec es prerrequisito de [HU-AOS-16](../SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md) (instalación por scope), [HU-AOS-24](../SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md) (editor de agentes) y [HU-AOS-46](../SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) (presets v2): el catálogo, los descriptores, el formulario de schema y aplicar preset sirven a los agentes del negocio.

## Problema

Las páginas de cada pack en el panel nuevo están escritas a mano (Cobranza 35 archivos, Comercio 10,
Calendario 7) y el menú es estático, así que **un pack nuevo exige desplegar el panel** y el menú ya
se desalineó del backend. El backend ya tiene `admin_menu` y `ViewDescriptor`
(`core/admin/view_registry.py:20-75`) sin exponerlos por `/api/v1`. Las tools declarativas solo viven
en `/legacy`. No hay catálogo de habilidades con descripción ni forma de aplicar un preset desde el
panel.

## Por qué importa (valor empresarial)

Es lo que hace a SolversHub una **plataforma de habilidades** y no un producto con pantallas fijas:
una habilidad nueva (marketing, reservas, encuestas) llega a todos los clientes con un release del
backend. Reduce el costo de cada habilidad nueva y acelera el catálogo que compite con las 12
verticales de Lety.

## Alcance

| HU | Qué |
|---|---|
| [HU-FWK-04](hu/HU-FWK-04-catalogo-de-habilidades.md) | Catálogo de habilidades con metadatos |
| [HU-FWK-05](hu/HU-FWK-05-manifiesto-de-menu.md) | Manifiesto de menú desde el backend |
| [HU-FWK-06](hu/HU-FWK-06-descriptores-y-api-de-vistas.md) | Descriptores enriquecidos y API de vistas |
| [HU-FWK-07](hu/HU-FWK-07-descriptor-view.md) | `<DescriptorView>` genérico |
| [HU-FWK-08](hu/HU-FWK-08-formulario-de-schema-v2.md) | Formulario de schema v2 |
| [HU-FWK-09](hu/HU-FWK-09-tools-declarativas-panel.md) | Acciones personalizadas (tools declarativas) en el panel nuevo |
| [HU-FWK-10](hu/HU-FWK-10-aplicar-preset-desde-panel.md) | Aplicar un preset desde el panel |
| [HU-FWK-11](hu/HU-FWK-11-presets-adicionales.md) | Presets adicionales |

## Decisiones

### D-SPEC-16-1 · Alcance de los descriptores

| Opción | Pros | Contras |
|---|---|---|
| **A. Listas, CRUD simple, KPIs y acciones por fila por descriptor; pantallas complejas siguen a mano (`kind: "custom"`)** | Cubre ~60 % de las pantallas sin perder flexibilidad | Dos formas de hacer pantallas |
| B. Todo por descriptor | Uniforme | Las pantallas complejas (cartera, bandeja) se vuelven inmanejables |

**Recomendación: A.** Estado: ⏳ pendiente.

## Requerimientos cubiertos

REQ-FWK-02, REQ-FWK-04, REQ-FWK-05, REQ-PLUS-05.
