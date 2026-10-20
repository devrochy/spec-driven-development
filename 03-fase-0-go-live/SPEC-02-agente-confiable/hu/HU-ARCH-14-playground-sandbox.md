---
id: HU-ARCH-14
titulo: Probar asistente sin efectos reales
spec: SPEC-02
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: false
estimacion: M
impacto: [confianza, calidad_ia]
req: [REQ-ARCH-14]
dependencias: []
skills: ["new-tool", "backend-design:testing-with-discernment", "arquitecto"]
estado: borrador
---

# HU-ARCH-14 · "Probar asistente" sin efectos reales

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-02](../spec.md) (D-SPEC-02-3).

**ID:** HU-ARCH-14

**Título:** Probar asistente sin efectos reales

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de un negocio quiero probar mi asistente en el panel sin que cree pedidos, links de pago, citas o correos reales para ajustar su comportamiento sin riesgo.

**Por qué importa (valor empresarial):** Hoy el playground corre el loop real: una prueba puede cobrar a un cliente, ocupar un horario o mandar un correo. Es un riesgo operativo y frena la experimentación que mejora la calidad.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-14

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Simulación.** Dado una tool con `side_effects=True`, cuando se llama desde el canal `test`, entonces devuelve un resultado simulado marcado `simulado: true` y no escribe en las tablas del pack.
- **Lectura real.** Dado una tool de solo lectura (inventario, disponibilidad), cuando se llama desde `test`, entonces lee datos reales.
- **Visible.** Dado el panel "Probar asistente", cuando una tool se simula, entonces la burbuja lo indica.
- **Auditoría de packs.** Dado todos los packs, cuando se revisa, entonces cada tool con efectos lo declara (test que falla si una tool nueva no declara).

**Evidencia / Definición de Terminado:**
- Tabla de tools por pack con su declaración de efectos.
- Tests del modo simulado.

**Riesgos/Notas:**
- El editor de flujo ([HU-FLOW-05](../../../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-05-borrador-y-publicacion.md)) usa este sandbox para probar borradores.
