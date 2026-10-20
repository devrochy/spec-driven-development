---
id: HU-AOS-23
titulo: "Consola de conexiones y hub"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-AOS-13]
dependencias: [HU-AOS-15]
skills: ["panel-ui", "frontend-design"]
estado: terminada
---

# HU-AOS-23 · Consola de conexiones y hub

> Estado SDD: Terminada (2026-10-18, tanda 7) — [SPEC-26](../spec.md).

**ID:** HU-AOS-23

**Título:** Consola de conexiones y hub

**Workstream:** Agent OS

**Historia:** Como dueño quiero ver mis conexiones con su Coordinador, agentes, versión, salud y consumo, y poder pausarlas, para operar mis canales desde un solo lugar.

**Por qué importa (valor empresarial):** Hace visible y operable el modelo "N conexiones por negocio" para personas no técnicas.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-13

**Dependencias:** [HU-AOS-15](HU-AOS-15-migracion-sin-regresion.md)

**Criterios de aceptación (Gherkin):**
- **Lista.** Dado un negocio con dos conexiones, cuando abre Conexiones, entonces ve por cada una Coordinador, agentes, versión activa, consistencia y consumo de 7 días.
- **Pausar.** Dado una conexión activa, cuando la pausa y confirma, entonces deja de responder y queda auditado: si es de Meta, es la pausa de ADR-0122 de su cuenta y la confirmación avisa que alcanza a todos los números de esa cuenta; si no (manual, `waweb`, `webchat`), solo esa conexión (`active = false`).
- **Permisos.** Dado un colaborador sin `conexiones:editar`, cuando abre el hub, entonces no ve las acciones de edición.

**Evidencia / Definición de Terminado:**
- Páginas del panel según `DESIGN.md`; API y tipos generados; capturas en claro, oscuro y móvil.

**Implementada (2026-10-18, tanda 7):** consola de conexiones con los agentes de cada conexión. PR [core #472](https://github.com/devrochy/agent-core/pull/472) + [panel #80](https://github.com/devrochy/solvershub-panel/pull/80).

**Riesgos/Notas:**
- El hub de Meta ([HU-CONN-08](../../../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md)) y este hub se unifican en la misma página.
