---
id: HU-AOS-17
titulo: "Enrutamiento: tarea en foco, reglas, disparadores y modo sombra"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia]
req: [REQ-AOS-06]
dependencias: [HU-AOS-15]
skills: ["eval-author", "optimizer", "agentcore-conventions"]
estado: en-curso
---

# HU-AOS-17 · Enrutamiento: tarea en foco, reglas, disparadores y modo sombra

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-17

**Título:** Enrutamiento: tarea en foco, reglas, disparadores y modo sombra

**Workstream:** Agent OS

**Historia:** Como Coordinador quiero decidir qué agente atiende con la tarea en foco, reglas y frases de disparo, y medirlo en sombra antes de activarlo, para enrutar bien sin sumar llamadas al modelo.

**Por qué importa (valor empresarial):** La ruta correcta es la primera condición de una respuesta correcta; medirla en sombra evita regresiones.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-06

**Dependencias:** [HU-AOS-15](HU-AOS-15-migracion-sin-regresion.md)

**Criterios de aceptación (Gherkin):**
- **Tarea en foco.** Dado una tarea de Ventas en foco, cuando el cliente responde un dato, entonces atiende Ventas sin clasificar.
- **Regla.** Dado el botón "Pagar", cuando llega su payload, entonces se inicia el procedimiento de la regla.
- **Disparadores.** Dado "quiero agendar una demo" sin tarea en foco, cuando se puntúa, entonces el candidato principal es `agendar_demo` con confianza ≥ 0,80.
- **Sombra.** Dado el modo sombra, cuando corre 7 días, entonces se reportan precisión y recall por procedimiento frente al comportamiento real.

**Evidencia / Definición de Terminado:**
- Router del kernel; `trigger_embeddings` por release; golden de ruteo de al menos 60 casos; coprocesador acotado por costo.

**Riesgos/Notas:**
- Sin embeddings en producción (P-19) la elección restringida del propio hilo sigue funcionando.
