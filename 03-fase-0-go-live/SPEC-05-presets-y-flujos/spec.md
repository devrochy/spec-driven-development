# SPEC-05 · Presets y flujos multi-pack

> Estado SDD: Diseño aprobado (2026-10-08) · Fase 0 · Hito 0A · Workstream Framework/Plugins

## Problema

- **El flujo (ADR-0054) define la lista completa de tools**: con varios packs, oculta tools de
  calendar, cobranza y memoria; `saludo` y `escalamiento` chocan entre packs; un re-seed duplica
  secciones `core` y **pisa las secciones propias de un negocio** etiquetadas con un pack
  (`core/agents/flow.py:270-280`), como le pasa hoy al tenant `solvershub`.
- **No existe el concepto de preset**: cada negocio se arma a mano; `onboard_tenant` falla si recibe
  `pack_payments` sin claves (`core/onboarding.py:345-349`, `pack_payments/config.py:17-19`); el seed de
  datos solo cubre comercio y el CLI importa `pack_commerce.models` directamente.
- Existe el hook `BaseModule.seed_data`, pero **ningún pack lo implementa**.

## Por qué importa (valor empresarial)

Los presets son el "superpoder" en forma de producto: un tipo de negocio (restaurante, cobranza,
planes y suscripciones) se activa con un clic y queda bien configurado. Es lo que hace posible el alta
automática (D-12) y lo que convierte "listos en días" en "listos en minutos". Lety vende 12 verticales
preconfiguradas; esta spec es la base para competir con eso.

## Alcance

| HU | Qué | Hito |
|---|---|---|
| [HU-FWK-01](hu/HU-FWK-01-composicion-de-flujos.md) ★ | Composición correcta de flujos multi-pack | 0A |
| [HU-FWK-02](hu/HU-FWK-02-adr-presets.md) ★ | ADR de presets | 0A |
| [HU-FWK-03](hu/HU-FWK-03-registro-de-presets-y-seeds.md) ★ | Registro de presets, seeds por pack y alta sin fallas | 0A |

## Decisiones

### D-SPEC-05-1 · Dónde vive un preset

| Opción | Pros | Contras |
|---|---|---|
| **A. JSON versionado en el core (`core/presets/*.json`) que referencia packs y sus fragmentos** | Una fuente; versionado; revisable | Un preset nuevo requiere release del core |
| B. Cada pack declara fragmentos y el preset los compone | Packs autónomos | Componer entre packs es más difícil de razonar |
| C. Tabla editable por el master | Sin release | Sin historial ni revisión |

**Recomendación: A** (los packs aportan sus `seed_data` y su `flow.json`). **Decisión del cliente: B.** Estado: ✅ tomada (2026-10-02): cada pack declara sus fragmentos y el preset los compone.

**Cómo se aplica B (aprobado el 2026-10-08):** cada pack declara sus **fragmentos** (secciones de flujo en `flow.json`, `seed_data` y config por defecto por vertical, sin secretos). El preset es un **manifiesto corto** que solo lista los packs, los defaults de persona y `AppSettings`, los pasos de activación, el plan mínimo y el golden set base; no copia secciones ni config de los packs, las compone. Así cada pack es dueño de lo suyo y hay un solo lugar donde ver un preset completo.

### D-SPEC-05-2 · Composición de secciones

| Opción | Pros | Contras |
|---|---|---|
| **A. IDs de sección con espacio de nombres (`pack_commerce:pedido`), secciones `tenant` que ningún re-seed toca y tools del core "siempre disponibles" fuera del flujo** | Sin choques; el negocio no pierde lo suyo | Migración de flujos existentes |
| B. Un único flujo plano por negocio | Simple | Vuelven los choques al agregar packs |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): IDs con namespace por pack, secciones `tenant` intocables y tools del core siempre disponibles.

## Contenido de un preset

| Campo | Ejemplo (preset "Planes y suscripciones") |
|---|---|
| Packs | commerce, calendar, payments, subscriptions |
| Playbooks permitidos | ventas, citas, pagos, suscripciones |
| Secciones de flujo | Demo, Planes, Compra, Pago, Gestión de suscripción, Escalamiento |
| Defaults de persona y `AppSettings` | Tono, idioma, estilo `un_mensaje` |
| Config de packs (sin secretos) | `subscriptions.provider`, umbrales, campos de checkout por tipo de producto |
| Seeds | Tipo de cita "Demo", productos de ejemplo |
| Conexiones requeridas | WhatsApp |
| Plan mínimo | Basic |
| Pasos de activación | Conectar WhatsApp, cargar planes, configurar pagos |
| Golden set base | Journeys de demo y compra |

**Sin prompts** en el preset (invariante 3): referencia playbooks por nombre.

## Fuera de alcance

Aplicar presets desde el panel con diff ([HU-FWK-10](../../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-10-aplicar-preset-desde-panel.md)), presets adicionales ([HU-FWK-11](../../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-11-presets-adicionales.md)), editor visual
([SPEC-15](../../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md)).

## Métricas de éxito

- Un negocio nuevo con preset queda operativo sin pasos manuales en el backend.
- 0 secciones de negocio pisadas por un re-seed (test).

## Requerimientos cubiertos

REQ-FWK-01, REQ-FWK-02, REQ-FWK-03.
