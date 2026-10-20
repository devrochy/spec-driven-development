# SPEC-10 · Diseño

## Kit de feedback (HU-UI-02)

| Pieza | Comportamiento |
|---|---|
| `ui/toast` | `role="status"` para éxito (se cierra a los 5 s) y `role="alert"` para error (queda); pausa con hover; animación ≤200 ms |
| `useConfirm()` | Diálogo compartido con título, consecuencia y botón en tono peligro para lo destructivo |
| `useAction()` | Ejecuta el fetch al BFF, muestra el toast, refresca la vista y hace rollback de lo optimista si falla |
| `lib/labels.ts` | Etiquetas legibles para estados, canales, roles, motivos y claves de permisos |

## Shell (HU-UI-03)

- Menú en cajón por debajo de `lg` y opción de solo iconos.
- `loading.tsx` con esqueletos por sección, `error.tsx` con reintento, `not-found.tsx` en español.
- Skip link, `aria-sort` en tablas, `aria-controls` en pestañas, selector de negocio con roles de
  listbox y teclado.
- Indicador del estado del asistente (activo/pausado) en la barra superior.

## Calidad (HU-UI-04)

- `npm run test` en CI (hoy `ci.yml:52-72` no lo corre); Vitest con jsdom y Testing Library para
  componentes; chequeo de deriva: `api:types` regenerado debe coincidir con el commiteado; axe en las
  páginas principales.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Cambios transversales tocan muchas páginas | Migrar por página con el kit nuevo, no en un solo PR |
