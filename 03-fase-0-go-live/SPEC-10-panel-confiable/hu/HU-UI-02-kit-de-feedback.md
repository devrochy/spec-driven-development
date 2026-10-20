---
id: HU-UI-02
titulo: Kit de feedback, confirmaciones y etiquetas legibles
spec: SPEC-10
fase: 0
hito: 0A
workstream: UX/Onboarding
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, operacion]
req: [REQ-UX-05]
dependencias: []
skills: ["frontend-design", "built-in-browser", "panel-ui"]
ola: 2
estado: terminada
---

# HU-UI-02 · Kit de feedback, confirmaciones y etiquetas legibles

> Estado SDD: Terminada — implementada 2026-10-07; verificada en test 2026-10-08 (issue [panel #28](https://github.com/devrochy/solvershub-panel/issues/28)).

**ID:** HU-UI-02

**Título:** Kit de feedback, confirmaciones y etiquetas legibles

**Workstream:** UX/Onboarding

**Historia:** Como usuario del panel quiero ver un aviso claro cuando algo sale bien o mal, que me pidan confirmación explicando la consecuencia antes de algo irreversible y leer estados en español claro para usar el panel sin miedo a equivocarme.

**Por qué importa (valor empresarial):** Eliminar una conexión o desactivar un colaborador sin confirmación ya causó pérdida de datos. Los enums crudos ("scheduled", "pocos_cortos") son la señal más fuerte de producto sin terminar. Este kit es la base que reutilizan el onboarding ([HU-SH-06](../../SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md)) y todas las vistas de la Fase 1.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-UX-05

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Toasts.** Dado una acción exitosa, cuando termina, entonces aparece un toast de éxito que se cierra solo; si falla, uno de error que queda hasta cerrarlo.
- **Confirmación con consecuencia.** Dado eliminar una conexión, desactivar un colaborador, resolver una conversación o cancelar una cita, cuando se pulsa, entonces se pide confirmación con el texto de la consecuencia y el botón en tono peligro.
- **Sin estados caseros.** Dado las páginas migradas, cuando se revisan, entonces usan `useAction` y no estados locales de carga/éxito/error ni `window.confirm`.
- **Etiquetas.** Dado estados, canales, roles y motivos de escalación, cuando se muestran, entonces salen de `lib/labels.ts` en español claro.
- **Accesible.** Dado los toasts y el diálogo, cuando se usan con teclado y lector de pantalla, entonces anuncian el mensaje y devuelven el foco.

**Evidencia / Definición de Terminado:**
- Componentes con tests; migración de las páginas con acciones irreversibles; `DESIGN.md` documenta el kit.

**Implementada (2026-10-07):** [panel #29](https://github.com/devrochy/solvershub-panel/pull/29) — Toaster (`role=status` éxito 5 s / `role=alert` error persistente) con store puro, `useConfirm()` con la consecuencia y botón `danger`, `useAction()` (fetch + toast + refresh + rollback optimista) y `lib/labels.ts` (estados, canales, roles, motivos, permisos). Migradas las acciones irreversibles (conexión, colaborador, conversación, cita/bloqueo, versión de spec): 0 `window.confirm`. `IconAction`/`ChannelIcon` a tonos semánticos. 48 tests · build OK.

**Verificada en test (2026-10-08):** con el navegador integrado y `dueno-a@demo.test`: la confirmación de «Desactivar colaborador» muestra la consecuencia, el botón en tono peligro, `role=alertdialog` y el foco inicial en Cancelar; el éxito de «Guardar identidad» se anuncia con `role=status`. Dos defectos encontrados y arreglados en [panel #37](https://github.com/devrochy/solvershub-panel/pull/37): el foco no volvía al botón al cerrar la confirmación (Cancelar o Escape; ahora vuelve a «Desactivar») y el selector de permisos mostraba claves en inglés (`Collaborators`, `Settings`, `Tenants`; ahora «Colaboradores», «Configuración», «Negocios», «Calendario · Conexión»). Re-verificado tras el deploy (`ad5aa37`).

**Riesgos/Notas:**
- `IconAction` y `ChannelIcon` pasan a tokens (sin pasteles fijos ni `hover:scale`).
