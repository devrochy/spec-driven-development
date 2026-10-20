---
id: HU-APP-20
titulo: "Escrituras móviles"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-APP-07]
dependencias: [HU-APP-10, HU-APP-11, HU-APP-12]
skills: [frontend-design, panel-ui]
estado: terminada
---

# HU-APP-20 · Escrituras móviles

> Estado SDD: Terminada — implementada 2026-10-07.

**ID:** HU-APP-20

**Título:** Escrituras móviles

**Workstream:** App móvil

**Historia:** Como dueño de un negocio quiero crear desde la app lo que hoy solo creo en el escritorio (productos, categorías, promociones, tipos de cita, bloqueos y colaboradores), para operar el negocio sin abrir el panel web.

**Por qué importa (valor empresarial):** La réplica total del panel exige que la app deje de ser solo consulta. Estas son las escrituras de mayor frecuencia en la operación diaria (catálogo, agenda y equipo) y cierran la brecha "ver pero no tocar".

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-10](HU-APP-10-comercio-movil.md), [HU-APP-11](HU-APP-11-calendario-movil.md), [HU-APP-12](HU-APP-12-configuracion-movil.md)

**Criterios de aceptación (Gherkin):**
- **Comercio.** Dado un dueño, cuando pulsa "+ Nuevo" en productos/categorías/promociones, entonces crea el registro y la lista se refresca.
- **Calendario.** Dado un dueño, cuando pulsa "+ Nuevo" en tipos o bloqueos, entonces crea el tipo (nombre+duración) o el bloqueo (inicio/fin/motivo).
- **Equipo.** Dado un dueño, cuando invita un colaborador (correo+clave+rol), entonces el colaborador aparece en la lista.

**Evidencia / Definición de Terminado:**
- Modales de creación en Comercio, Calendario y Configuración contra `ProductSave`, `CategorySave`, `PromotionSave`, `TypeSave`, `BlockIn` y `CollaboratorCreate` verificados en el OpenAPI; 4 tests nuevos.

**Implementada (2026-10-07):** [solvershub-apk #126](https://github.com/devrochy/solvershub-apk/pull/126) — modales "+ Nuevo"/"+ Invitar" en los tres módulos con validación y recarga tras crear. 622/622 tests.

**Riesgos/Notas:**
- Las fechas del bloqueo se ingresan como texto (AAAA-MM-DD HH:MM); un date-picker nativo queda para iteración posterior.
