---
id: HU-DS-12
titulo: Motion y microinteracciones
spec: SPEC-29
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion]
req: [REQ-UX-09]
dependencias: [HU-DS-04, HU-DS-09]
skills: ["frontend-design", "panel-ui"]
estado: borrador
---

# HU-DS-12 · Motion y microinteracciones

> Estado SDD: Lista para ejecutar — [SPEC-29](../spec.md) en Diseño aprobado (D-32).

**ID:** HU-DS-12

**Título:** Motion y microinteracciones

**Workstream:** UX/Onboarding

**Historia:** Como usuario quiero que diálogos, menús, toasts y cambios de pantalla respondan con movimientos cortos y coherentes, y que todo se quede quieto si pedí reducir el movimiento, para entender qué cambió sin distraerme.

**Por qué importa (valor empresarial):** El movimiento coherente es lo que hace que un producto se sienta terminado. Respetar "reducir movimiento" es un requisito de accesibilidad (WCAG 2.3.3) y evita mareos.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-09

**Dependencias:** [HU-DS-04](HU-DS-04-shell-adaptativo-del-panel.md), [HU-DS-09](HU-DS-09-kit-de-componentes-app.md)

**Criterios de aceptación (Gherkin):**
- **Duraciones por token.** Dado el código del panel y de la app, cuando busco duraciones sueltas (`duration-300`, `300` ms en `Animated`), entonces no hay: todas salen de `dur-*` y `ease-*`.
- **Diálogo.** Dado un diálogo, cuando se abre, entonces entra en 200 ms con opacidad y escala .98 → 1 y sale en 150 ms.
- **Reducir movimiento en el panel.** Dado `prefers-reduced-motion: reduce`, cuando abro el cajón móvil, entonces aparece sin desplazamiento.
- **Reducir movimiento en la app.** Dado "Quitar animaciones" activo en Android, cuando cierro un overlay con el gesto, entonces se cierra sin animación y el háptico se mantiene.
- **Cambio de ruta.** Dado un navegador con View Transitions, cuando cambio de sección, entonces solo el contenido principal hace un fundido de 150 ms y la barra lateral no se mueve.

**Evidencia / Definición de Terminado:**
- `core/theme/motion.ts` en la app y utilidades de Tailwind sobre los tokens en el panel.
- Grabaciones cortas con y sin reducir movimiento.

**Riesgos/Notas:**
- View Transitions es una mejora progresiva: sin soporte, el cambio es inmediato.
