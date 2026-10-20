---
id: HU-AOS-26
titulo: "Colaboración y enrutamiento en el panel"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, confianza]
req: [REQ-AOS-07, REQ-AOS-13]
dependencias: [HU-AOS-18, HU-AOS-24]
skills: ["panel-ui", "frontend-design"]
estado: borrador
---

# HU-AOS-26 · Colaboración y enrutamiento en el panel

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-26

**Título:** Colaboración y enrutamiento en el panel

**Workstream:** Agent OS

**Historia:** Como dueño quiero ver y editar quién puede pasar la conversación, encargar o consultar a quién, y cómo reparte el Coordinador, para controlar la colaboración en lenguaje claro.

**Por qué importa (valor empresarial):** El grafo de permisos A2A deja de ser un concepto técnico y pasa a ser una lista que el dueño entiende.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-07, REQ-AOS-13

**Dependencias:** [HU-AOS-18](HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-24](HU-AOS-24-editor-de-agentes.md)

**Criterios de aceptación (Gherkin):**
- **Lista accesible.** Dado los permisos del negocio (scope de negocio, ADR-0116), cuando los abre, entonces los ve como lista navegable por teclado, solo con pasar la conversación, encargar y consultar.
- **Validación en vivo.** Dado un permiso que crea un ciclo de handoff, cuando lo agrega, entonces ve la advertencia antes de guardar.
- **Probar una frase.** Dado una frase, cuando la prueba, entonces ve qué agente y procedimiento la atenderían y por qué.

**Evidencia / Definición de Terminado:**
- Lista de permisos con mapa opcional (`@xyflow/react` bajo demanda); API de grafos; tests.

**Riesgos/Notas:**
- El mapa no reemplaza a la lista: la lista es la vista accesible por defecto.
