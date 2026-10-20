---
id: HU-DS-08
titulo: Widgets reorganizables
spec: SPEC-29
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion]
req: [REQ-UX-11]
dependencias: [HU-DS-07]
skills: ["frontend-design", "panel-ui"]
estado: borrador
---

# HU-DS-08 · Widgets reorganizables

> Estado SDD: Lista para ejecutar — [SPEC-29](../spec.md) en Diseño aprobado (D-32).

**ID:** HU-DS-08

**Título:** Widgets reorganizables

**Workstream:** UX/Onboarding

**Historia:** Como usuario del panel quiero ocultar, mostrar y reordenar los widgets de mi Resumen para tener a la vista lo que reviso cada día.

**Por qué importa (valor empresarial):** La personalización convierte el Resumen en "mi tablero" y sube su uso diario, que es la métrica de retención de esta spec.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-11

**Dependencias:** [HU-DS-07](HU-DS-07-resumen-modular-por-rol.md)

**Criterios de aceptación (Gherkin):**
- **Personalizar con teclado.** Dado "Personalizar", cuando abro el diálogo, entonces veo la lista de widgets de mi perfil con un interruptor y botones Subir y Bajar, y todo funciona con teclado.
- **Recordar.** Dado que oculté "Estado del sistema", cuando vuelvo mañana con el mismo usuario y negocio, entonces sigue oculto.
- **Por negocio.** Dado que tengo dos negocios, cuando cambio de negocio, entonces cada uno conserva su propio orden.
- **Restablecer.** Dado un Resumen personalizado, cuando pulso "Restablecer", entonces vuelve al layout por defecto de mi perfil.
- **Sin permiso no aparece.** Dado que pierdo un permiso, cuando entro, entonces el widget desaparece aunque estuviera guardado en mis preferencias.

**Evidencia / Definición de Terminado:**
- Tests del store de preferencias (`localStorage` por usuario y negocio, con try/catch).
- Captura del diálogo.

**Riesgos/Notas:**
- Sin arrastrar y soltar en esta HU: el diálogo con botones es accesible y más barato; arrastrar puede venir después con una librería accesible.
- Las preferencias no viajan entre dispositivos (D-SPEC-29-4).
