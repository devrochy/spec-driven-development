# SPEC-10 · Panel confiable

> Estado SDD: Diseño aprobado · Fase 0 · Hitos 0A (UI-01, UI-02) y 0B (UI-03, UI-04) · Workstream UX/Onboarding

## Problema

La revisión del panel nuevo ([panel-nuevo.md](../../01-revalidacion/panel-nuevo.md)) encontró bugs
visibles que dañan la confianza y una base de UX inconsistente:

- **Guardar la config de una habilidad escribe en el negocio equivocado** (falta `X-Tenant-Id` en
  `app/api/plugins/[pluginId]/route.ts:37-41`).
- Precios de comercio en USD; el formulario de schema pierde el error del backend y envía números como
  texto; acciones irreversibles sin confirmación; switches optimistas sin rollback; botón destructivo en
  verde; menú desalineado con el backend.
- Sin toasts ni diálogo de confirmación compartido (53 estados locales y 9 confirmaciones caseras);
  enums crudos a la vista.
- Shell sin menú móvil, sin `loading`, `error` ni `not-found`; 404 en inglés.
- 12 tests que el CI no corre; sin control de deriva de los tipos de la API.

## Por qué importa (valor empresarial)

El panel es donde el cliente decide si el producto es "profesional". Un dato guardado en el negocio
de otro es, además, un incidente de aislamiento ante el cliente. Las vistas operativas nuevas
(tickets, bandeja, dashboard) llegan en la Fase 1 ([SPEC-13](../../04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md)); aquí se arregla lo que hace perder la
confianza y se crea la base que reutilizan todas las pantallas.

## Alcance

| HU | Qué | Hito |
|---|---|---|
| [HU-UI-01](hu/HU-UI-01-bugs-visibles.md) ★ | Lote de bugs visibles | 0A |
| [HU-UI-02](hu/HU-UI-02-kit-de-feedback.md) ★ | Kit de feedback y etiquetas legibles | 0A |
| [HU-UI-03](hu/HU-UI-03-shell.md) | Shell: móvil, carga, error, 404, accesibilidad | 0B |
| [HU-UI-04](hu/HU-UI-04-calidad-del-panel.md) | Calidad del panel: tests en CI, deriva de tipos, axe | 0B |

## Decisiones

### D-SPEC-10-1 · Sistema de notificaciones en la UI

| Opción | Pros | Contras |
|---|---|---|
| **A. Toasts propios sobre Radix (`ui/toast`) + `useConfirm` + `useAction` (fetch, toast, refresco, rollback)** | Sigue `DESIGN.md`; sin dependencias nuevas; reemplaza 53 estados | Construirlo |
| B. Librería de toasts externa | Rápido | Otro estilo que adaptar a los tokens |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): toasts propios sobre Radix + `useConfirm` + `useAction`.

## Fuera de alcance

Vistas operativas profesionales ([SPEC-13](../../04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md)), arquitectura de información y glosario ([SPEC-12](../../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md)),
páginas por descriptores ([SPEC-16](../../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/spec.md)).

## Métricas de éxito

- 0 bugs visibles de la lista de la revisión.
- 100 % de acciones irreversibles con confirmación.
- Tests del panel corriendo en CI con cobertura de los componentes base.

## Requerimientos cubiertos

REQ-UX-05, REQ-UX-06.
